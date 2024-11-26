---
layout: default
---

<p id="logiciel-details"></p>

<script>
  // Extract URL parameter 'name'
  const urlParams = new URLSearchParams(window.location.search);
  const logicielName = urlParams.get('name');

  // Load the YAML data using Liquid
  const data = {{ site.data.linux.soft.list | jsonify }};

  // Recursive function to search through categories and logiciels
  function findLogiciel(categories, name) {
    for (const category of categories) {
      // Check logiciels in the current category
      if (category.logiciels) {
        const logiciel = category.logiciels.find(l => l.nom.toLowerCase() === name.toLowerCase());
        if (logiciel) {
          return logiciel; // Return the found logiciel
        }
      }
      // Check nested categories recursively
      if (category.categories) {
        const result = findLogiciel(category.categories, name);
        if (result) {
          return result;
        }
      }
    }
    return null; // Not found
  }

  // Search for the logiciel
  const foundLogiciel = findLogiciel(data.categories, logicielName);

  // Display logiciel details
  if (foundLogiciel) {
    document.getElementById('logiciel-details').innerHTML = `
      <h1>${foundLogiciel.nom}</h1>
      <p>${foundLogiciel.description || 'No description available.'}</p>
      <ul>
        ${foundLogiciel.url_doc_ubuntu_fr ? `<li><a href="${foundLogiciel.url_doc_ubuntu_fr}" target="_blank">Documentation Ubuntu</a></li>` : ''}
        ${foundLogiciel.url_website ? `<li><a href="${foundLogiciel.url_website}" target="_blank">Official Website</a></li>` : ''}
        ${foundLogiciel.url_repository ? `<li><a href="${foundLogiciel.url_repository}" target="_blank">Repository</a></li>` : ''}
      </ul>
    `;
  } else {
    document.getElementById('logiciel-details').textContent = "Logiciel not found.";
  }
</script>
