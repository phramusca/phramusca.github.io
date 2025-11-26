/**
 * Génère automatiquement une table des matières (TOC) à partir des titres de la page
 * Affiche la TOC flottante sur la droite, alignée en haut, repliée par défaut
 */
(function() {
  'use strict';

  function generateTOC() {
    const tocContainer = document.getElementById('toc-container');
    if (!tocContainer) return;

    const mainContent = document.querySelector('#main_content') || document.querySelector('main') || document.body;
    const headings = mainContent.querySelectorAll('h2, h3, h4, h5, h6');
    
    if (headings.length === 0) {
      tocContainer.style.display = 'none';
      return;
    }

    // Créer le conteneur flottant
    const floatingContainer = document.createElement('div');
    floatingContainer.id = 'toc-floating';

    // Créer l'élément details/summary pour un TOC pliable
    const details = document.createElement('details');
    details.className = 'toc-details';
    details.open = true; // Déplié par défaut

    const summary = document.createElement('summary');
    summary.className = 'toc-summary';
    summary.textContent = 'Table des matières';

    const nav = document.createElement('nav');
    nav.className = 'toc-nav';

    const ul = document.createElement('ul');
    ul.className = 'toc-list';

    const ulStack = [ul]; // Pile pour suivre les niveaux de listes
    let currentLevel = 2; // Commence à h2

    headings.forEach(function(heading) {
      const level = parseInt(heading.tagName.charAt(1));
      const id = heading.id || heading.textContent.toLowerCase()
        .replace(/[^\w\s-]/g, '')
        .replace(/\s+/g, '-')
        .replace(/-+/g, '-')
        .trim();

      // Si l'ID n'existe pas, le créer
      if (!heading.id) {
        heading.id = id;
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
    details.appendChild(summary);
    details.appendChild(nav);
    floatingContainer.appendChild(details);
    
    // Positionner la TOC à droite du contenu, fixe lors du scroll
    const container = mainContent.closest('.container');
    
    // Capturer la position initiale du top (relative à la fenêtre, ne changera pas)
    let fixedTopPosition = 20; // Position par défaut
    
    if (container && mainContent) {
      // Trouver le premier <hr> dans le contenu
      const firstHr = mainContent.querySelector('hr');
      
      if (firstHr) {
        const hrRect = firstHr.getBoundingClientRect();
        // Capturer la position initiale relative à la fenêtre : juste en dessous du hr
        fixedTopPosition = hrRect.bottom + 20; // Position relative à la fenêtre (getBoundingClientRect)
      } else {
        // Si pas de hr, utiliser le début du contenu
        const mainContentRect = mainContent.getBoundingClientRect();
        fixedTopPosition = mainContentRect.top + 20;
      }
    }
    
    function updateTOCPosition() {
      if (container && mainContent) {
        const containerRect = container.getBoundingClientRect();
        
        // Position fixe : top reste fixe (ne change pas lors du scroll)
        floatingContainer.style.position = 'fixed';
        floatingContainer.style.top = fixedTopPosition + 'px';
        // Positionner juste à droite du container : left = right du container + 20px
        // Cette position est recalculée pour rester alignée avec le container
        floatingContainer.style.left = (containerRect.right + 20) + 'px';
        floatingContainer.style.right = 'auto'; // Désactiver right pour utiliser left
      } else {
        // Fallback si pas de container
        floatingContainer.style.position = 'fixed';
        floatingContainer.style.top = '20px';
        floatingContainer.style.right = '20px';
        floatingContainer.style.left = 'auto';
      }
    }
    
    // Calculer la position initiale
    updateTOCPosition();
    
    // Mettre à jour la position au scroll (seulement left pour rester alignée) et au redimensionnement
    window.addEventListener('scroll', updateTOCPosition);
    window.addEventListener('resize', updateTOCPosition);
    
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
