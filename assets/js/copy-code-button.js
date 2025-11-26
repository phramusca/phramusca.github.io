// Ajouter un bouton "copier" à tous les blocs de code
document.addEventListener('DOMContentLoaded', function() {
  // Trouver tous les blocs de code (seulement les éléments pre)
  const codeBlocks = document.querySelectorAll('pre');
  
  codeBlocks.forEach(function(preBlock) {
    // Éviter les doublons si on a déjà un bouton
    if (preBlock.querySelector('.copy-code-button')) {
      return;
    }
    
    // Créer le bouton
    const button = document.createElement('button');
    button.className = 'copy-code-button';
    button.setAttribute('aria-label', 'Copier le code');
    button.textContent = '📋 Copier';
    
    // Obtenir le texte à copier (depuis le code à l'intérieur du pre, ou directement depuis le pre)
    const codeElement = preBlock.querySelector('code');
    const codeText = codeElement ? (codeElement.textContent || codeElement.innerText) : (preBlock.textContent || preBlock.innerText);
    
    // Ajouter l'événement de clic
    button.addEventListener('click', function() {
      // Copier dans le presse-papiers
      navigator.clipboard.writeText(codeText).then(function() {
        // Feedback visuel
        const originalText = button.textContent;
        button.textContent = '✅ Copié !';
        button.classList.add('copied');
        
        setTimeout(function() {
          button.textContent = originalText;
          button.classList.remove('copied');
        }, 2000);
      }).catch(function(err) {
        // Fallback pour les navigateurs plus anciens
        const textArea = document.createElement('textarea');
        textArea.value = codeText;
        textArea.style.position = 'fixed';
        textArea.style.opacity = '0';
        document.body.appendChild(textArea);
        textArea.select();
        try {
          document.execCommand('copy');
          button.textContent = '✅ Copié !';
          button.classList.add('copied');
          setTimeout(function() {
            button.textContent = '📋 Copier';
            button.classList.remove('copied');
          }, 2000);
        } catch (err) {
          button.textContent = '❌ Erreur';
          setTimeout(function() {
            button.textContent = '📋 Copier';
          }, 2000);
        }
        document.body.removeChild(textArea);
      });
    });
    
    // Ajouter le bouton au bloc de code
    // Le CSS gère déjà le position: relative pour pre
    preBlock.appendChild(button);
  });
});

