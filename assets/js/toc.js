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
    details.open = false; // Replié par défaut

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
