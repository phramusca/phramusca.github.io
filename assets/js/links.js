/**
 * Traite les liens pour distinguer les liens internes et externes
 * - Ajoute target="_blank" et rel="noopener noreferrer" aux liens externes
 * - Ajoute une classe pour le style CSS
 */
(function() {
  'use strict';

  // Fonction pour déterminer si un lien est externe
  function isExternalLink(href) {
    if (!href) return false;
    
    // Liens internes : /, ./, ../, #, ou pas de protocole
    if (href.startsWith('/') || 
        href.startsWith('./') || 
        href.startsWith('../') || 
        href.startsWith('#') ||
        href.startsWith('wiki/') ||
        href.startsWith('apt://') ||
        !href.match(/^[a-zA-Z][a-zA-Z\d+\-.]*:/)) {
      return false;
    }
    
    // Liens externes : http, https, mailto:, etc.
    if (href.match(/^(https?:)?\/\//)) {
      // Vérifier si c'est le même domaine
      try {
        const linkUrl = new URL(href, window.location.origin);
        const currentUrl = new URL(window.location.href);
        // Si c'est le même domaine, c'est un lien interne
        if (linkUrl.hostname === currentUrl.hostname || 
            linkUrl.hostname === '' ||
            linkUrl.hostname === 'phramusca.github.io') {
          return false;
        }
      } catch (e) {
        // Si l'URL est invalide, on considère que c'est externe
      }
      return true;
    }
    
    // Autres protocoles (mailto:, tel:, etc.) sont considérés comme externes
    return href.includes(':');
  }

  // Traiter tous les liens de la page
  function processLinks() {
    const links = document.querySelectorAll('a[href]');
    const currentHost = window.location.hostname;
    
    links.forEach(function(link) {
      const href = link.getAttribute('href');
      
      if (isExternalLink(href)) {
        // Ajouter target="_blank" et rel="noopener noreferrer" pour la sécurité
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
        link.classList.add('external-link');
      } else {
        // Lien interne
        link.classList.add('internal-link');
      }
    });
  }

  // Exécuter au chargement de la page
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', processLinks);
  } else {
    processLinks();
  }
})();

