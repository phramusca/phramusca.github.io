/**
 * Génère automatiquement une table des matières (TOC) à partir des titres de la page
 * Affiche la TOC flottante sur la droite, alignée en haut, repliée par défaut
 */
(function() {
  'use strict';

  /**
   * Filtre les en-têtes à exclure du TOC
   * @param {NodeList|Array} allHeadings - Tous les en-têtes trouvés
   * @returns {Array} - En-têtes filtrés à inclure dans le TOC
   */
  function filterHeadings(allHeadings) {
    return Array.from(allHeadings).filter(heading => {
      // Exclure les h1 de la TOC (ils seront utilisés comme titre)
      const level = parseInt(heading.tagName.charAt(1));
      if (level === 1) return false;
      
      // Exclure les en-têtes dans les sections de contenu inclus (comme .toggle-content)
      // C'est la règle principale : tout ce qui est dans .toggle-content est exclu
      if (heading.closest('.toggle-content')) return false;
      
      // Exclure les en-têtes avec la classe no_toc seulement s'ils ne sont pas des sections principales
      // (les sections principales comme "Sur le Web" et "Ma Sélection" doivent apparaître même avec no_toc)
      // On considère h2 et h3 comme sections principales
      if (heading.classList.contains('no_toc') && level > 3) {
        return false;
      }
      
      return true;
    });
  }

  /**
   * Détecte les catégories et sous-catégories dans les tableaux et les ajoute au TOC
   * @param {Array} headings - Liste des en-têtes existants
   * @returns {Array} - Liste étendue avec les catégories, triée par position dans le DOM
   */
  function addCategoriesToTOC(headings) {
    const mainContent = document.querySelector('#main_content') || document.querySelector('main') || document.body;
    const categories = [];
    
    // Chercher les catégories dans les tableaux (strong dans td avec colspan="4")
    const categoryRows = mainContent.querySelectorAll('table td[colspan="4"] strong');
    
    categoryRows.forEach((strong, index) => {
      const td = strong.closest('td');
      const tr = td.closest('tr');
      
      // Déterminer le niveau : h3 pour les catégories principales (centrées), h4 pour les sous-catégories
      const tdStyle = td.getAttribute('style') || '';
      const isMainCategory = tdStyle.includes('text-align: center') || tdStyle.includes('text-align:center');
      const level = isMainCategory ? 3 : 4;
      
      // Générer un ID unique pour la catégorie
      const categoryId = 'category-' + index + '-' + strong.textContent.toLowerCase()
        .replace(/[^\w\s-]/g, '')
        .replace(/\s+/g, '-')
        .replace(/-+/g, '-')
        .trim();
      
      // Créer une ancre sur la ligne du tableau
      if (!tr.id) {
        tr.id = categoryId;
      }
      
      // Créer un pseudo-en-tête pour la catégorie
      const categoryHeading = {
        tagName: 'H' + level,
        textContent: strong.textContent.trim(),
        id: categoryId,
        level: level,
        element: tr, // Utiliser la ligne du tableau comme référence pour le tri
        isCategory: true // Marquer comme catégorie pour référence
      };
      
      categories.push(categoryHeading);
    });
    
    // Fusionner les catégories avec les en-têtes existants
    const allItems = [...headings, ...categories];
    
    // Trier par position dans le DOM
    allItems.sort((a, b) => {
      const aElement = a.element || a;
      const bElement = b.element || b;
      
      // Comparer les positions dans le DOM
      const position = aElement.compareDocumentPosition(bElement);
      if (position & Node.DOCUMENT_POSITION_FOLLOWING) {
        return -1;
      } else if (position & Node.DOCUMENT_POSITION_PRECEDING) {
        return 1;
      }
      return 0;
    });
    
    return allItems;
  }

  function generateTOC() {
    const tocContainer = document.getElementById('toc-container');
    if (!tocContainer) return;

    const mainContent = document.querySelector('#main_content') || document.querySelector('main') || document.body;
    const allHeadings = mainContent.querySelectorAll('h1, h2, h3, h4, h5, h6');
    let headings = filterHeadings(allHeadings);
    
    // Convertir les NodeList en objets avec les propriétés nécessaires
    headings = Array.from(headings).map(heading => ({
      tagName: heading.tagName,
      textContent: heading.textContent,
      id: heading.id,
      level: parseInt(heading.tagName.charAt(1)),
      element: heading
    }));
    
    // Ajouter les catégories du tableau au TOC
    headings = addCategoriesToTOC(headings);
    
    if (headings.length === 0) {
      tocContainer.style.display = 'none';
      return;
    }

    // Créer le conteneur flottant
    const floatingContainer = document.createElement('div');
    floatingContainer.id = 'toc-floating';

    // Trouver le h1 pour l'utiliser comme titre
    const firstH1 = mainContent.querySelector('h1');
    let tocTitle = 'Table des matières';
    let tocTitleId = null;
    
    if (firstH1) {
      tocTitle = firstH1.textContent.trim();
      // Obtenir ou créer l'ID du h1
      if (!firstH1.id) {
        tocTitleId = firstH1.textContent.toLowerCase()
          .replace(/[^\w\s-]/g, '')
          .replace(/\s+/g, '-')
          .replace(/-+/g, '-')
          .trim();
        firstH1.id = tocTitleId;
      } else {
        tocTitleId = firstH1.id;
      }
    }

    // Créer le titre avec lien vers le h1
    const titleElement = document.createElement('div');
    titleElement.className = 'toc-title';
    if (tocTitleId) {
      const titleLink = document.createElement('a');
      titleLink.href = '#' + tocTitleId;
      titleLink.className = 'toc-title-link';
      titleLink.textContent = tocTitle;
      titleElement.appendChild(titleLink);
    } else {
      titleElement.textContent = tocTitle;
    }

    const nav = document.createElement('nav');
    nav.className = 'toc-nav';

    const ul = document.createElement('ul');
    ul.className = 'toc-list';

    const ulStack = [ul]; // Pile pour suivre les niveaux de listes
    let currentLevel = 2; // Commence à h2 (h1 exclu)

    headings.forEach(function(heading) {
      const level = heading.level || parseInt(heading.tagName.charAt(1));
      const id = heading.id || heading.textContent.toLowerCase()
        .replace(/[^\w\s-]/g, '')
        .replace(/\s+/g, '-')
        .replace(/-+/g, '-')
        .trim();

      // Si l'ID n'existe pas, le créer sur l'élément original
      if (!heading.id && heading.element) {
        heading.id = id;
        if (heading.element.tagName === 'STRONG') {
          // Pour les catégories, l'ID est sur la ligne du tableau
          const tr = heading.element.closest('tr');
          if (tr) tr.id = id;
        } else {
          heading.element.id = id;
        }
      }

      // Ajuster la pile de listes selon le niveau
      if (level > currentLevel) {
        // Descendre : créer des listes imbriquées dans le dernier li
        while (currentLevel < level) {
          const lastLi = ulStack[ulStack.length - 1].lastElementChild;
          if (lastLi) {
            let nestedUl = lastLi.querySelector('ul.toc-list');
            if (!nestedUl) {
              nestedUl = document.createElement('ul');
              nestedUl.className = 'toc-list';
              lastLi.appendChild(nestedUl);
            }
            ulStack.push(nestedUl);
          } else {
            // Si la liste est vide, créer un nouveau ul au même niveau
            const newUl = document.createElement('ul');
            newUl.className = 'toc-list';
            ulStack.push(newUl);
          }
          currentLevel++;
        }
      } else if (level < currentLevel) {
        // Remonter : retirer des listes de la pile
        while (currentLevel > level && ulStack.length > 1) {
          ulStack.pop();
          currentLevel--;
        }
      }

      // Créer l'élément de liste et le lien
      const li = document.createElement('li');
      li.className = `toc-item toc-level-${level}`;

      const a = document.createElement('a');
      a.href = '#' + id;
      a.className = 'toc-link';
      a.textContent = heading.textContent.trim();

      li.appendChild(a);
      ulStack[ulStack.length - 1].appendChild(li);

      currentLevel = level;
    });

    nav.appendChild(ul);
    floatingContainer.appendChild(titleElement);
    floatingContainer.appendChild(nav);
    
    // Positionner la TOC à droite du contenu, fixe lors du scroll
    const container = mainContent.closest('.container');
    
    /**
     * Calcule la position du TOC au niveau du titre principal (h1) du contenu
     * @returns {number} Position en pixels depuis le haut de la fenêtre
     */
    function calculateTopPosition() {
      // Chercher le premier h1 dans le contenu principal
      const firstH1 = mainContent.querySelector('h1');
      if (firstH1) {
        const rect = firstH1.getBoundingClientRect();
        // Positionner au niveau du haut du titre
        return Math.max(rect.top, 20);
      }
      
      // Si pas de h1, utiliser le début du contenu principal
      const mainContentRect = mainContent.getBoundingClientRect();
      return Math.max(mainContentRect.top, 20);
    }
    
    // Calculer la position une seule fois au chargement (fixe ensuite)
    let fixedTopPosition = 20; // Valeur par défaut
    
    function updateTOCPosition() {
      if (container && mainContent) {
        const containerRect = container.getBoundingClientRect();
        
        // Position fixe : top reste toujours à la même position
        floatingContainer.style.position = 'fixed';
        floatingContainer.style.top = fixedTopPosition + 'px';
        // Positionner juste à droite du container : left = right du container + 20px
        floatingContainer.style.left = (containerRect.right + 20) + 'px';
        floatingContainer.style.right = 'auto';
      } else {
        // Fallback si pas de container
        floatingContainer.style.position = 'fixed';
        floatingContainer.style.top = fixedTopPosition + 'px';
        floatingContainer.style.right = '20px';
        floatingContainer.style.left = 'auto';
      }
    }
    
    // Calculer la position après que le DOM soit rendu
    function initializePosition() {
      // Attendre que le layout soit calculé
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          fixedTopPosition = calculateTopPosition();
          updateTOCPosition();
        });
      });
    }
    
    // Initialiser la position
    initializePosition();
    
    // Mettre à jour la position au scroll (seulement left pour rester alignée) et au redimensionnement
    window.addEventListener('scroll', updateTOCPosition);
    window.addEventListener('resize', () => {
      // Recalculer seulement au redimensionnement (pas au scroll)
      fixedTopPosition = calculateTopPosition();
      updateTOCPosition();
    });
    
    document.body.appendChild(floatingContainer);

    // Masquer le conteneur original
    tocContainer.style.display = 'none';
  }

  // Exécuter au chargement de la page
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', generateTOC);
  } else {
    generateTOC();
  }
})();
