---
layout: default
---

<div id="logiciel-details"></div>

<script>
  const urlParams = new URLSearchParams(window.location.search);
  const logicielName = urlParams.get('name');
  const data = {{ site.data.soft_list | jsonify }};

  function findLogiciel(categories, name) {
    for (const category of categories) {
      if (category.logiciels) {
        const logiciel = category.logiciels.find(l => l.nom.toLowerCase() === name.toLowerCase());
        if (logiciel) {
          return logiciel;
        }
      }
      if (category.categories) {
        const result = findLogiciel(category.categories, name);
        if (result) {
          return result;
        }
      }
    }
    return null;
  }

  const foundLogiciel = findLogiciel(data.categories, logicielName);
  const detailsContainer = document.getElementById('logiciel-details');

  if (foundLogiciel) {
    const aptLink = foundLogiciel.apt 
    ? (foundLogiciel.apt.startsWith('http://') || foundLogiciel.apt.startsWith('https://')
        ? `<a href="${foundLogiciel.apt}">${foundLogiciel.nom}</a>` 
        : `<a href="apt://${foundLogiciel.apt}">apt://${foundLogiciel.apt}</a>`)
    : 'Not available';

    detailsContainer.innerHTML = `
      <h1>${foundLogiciel.nom}</h1>
      <p>${foundLogiciel.description || 'Pas de description disponible.'}</p>
      <ul>
        ${aptLink ? `<li>Installation: ${aptLink}</li>` : ''}
        ${foundLogiciel.url_doc_ubuntu_fr ? `<li>Documentation Ubuntu: <a href="${foundLogiciel.url_doc_ubuntu_fr}" target="_blank">${foundLogiciel.url_doc_ubuntu_fr}</a></li>` : ''}
        ${foundLogiciel.url_website ? `<li>Site Internet: <a href="${foundLogiciel.url_website}" target="_blank">${foundLogiciel.url_website}</a></li>` : ''}
        ${foundLogiciel.url_repository ? `<li>Repository: <a href="${foundLogiciel.url_repository}" target="_blank">${foundLogiciel.url_repository}</a></li>` : ''}
      </ul>
    `;

    //Affichage du contenu du markdowwn indiqué par url_internal
    if (foundLogiciel.url_internal) {
      fetch("../"+foundLogiciel.url_internal)
        .then(response => {
          if (!response.ok) {
            throw new Error('Fichier non trouvé');
          }
          return response.text();
        })
        .then(htmlContent => {
          // Supprimer l'élément header si présent
          const tempDiv = document.createElement('div');
          tempDiv.innerHTML = htmlContent;
          const header = tempDiv.querySelector('header');
          if (header) {
            header.remove(); 
          }
          const innerContent = tempDiv.innerHTML;
          detailsContainer.innerHTML += `
            <div><h3>Plus d'infos :</h3>${innerContent}</div>
          `;
        })
        .catch(error => {
          detailsContainer.innerHTML += `<p>Erreur lors du chargement du fichier interne: ${error.message}</p>`;
        });
    }
  } else {
    detailsContainer.textContent = 'Logiciel introuvable.';
  }
</script>


