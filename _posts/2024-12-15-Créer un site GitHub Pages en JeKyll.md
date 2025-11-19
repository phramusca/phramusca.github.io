---
layout: default
excerpt:  Créer un site GitHub Pages en JeKyll
title: Créer un site GitHub Pages en JeKyll
---

# JeKyll

- Faire un lien avec image ET texte

   [<img src="https://github.com/fluidicon.png" alt="GitHub Logo" width="50"> GitHub](https://github.com)

- A Tester: https://kramdown.gettalong.org/converter/html.html#toc

## Installation et utilisation de Simple-Jekyll-Search

### Étape 1 : Télécharger Simple-Jekyll-Search

1. Téléchargez le fichier `simple-jekyll-search.min.js` depuis le dépôt GitHub officiel :  
   [https://github.com/christian-fei/Simple-Jekyll-Search](https://github.com/christian-fei/Simple-Jekyll-Search).

2. Placez ce fichier dans un dossier de votre site Jekyll, par exemple :  
   `assets/js/`.

### Étape 2 : Ajouter un fichier JSON pour les données de recherche

   {% raw %}

   ```liquid
   ---
   layout: null
   ---
   [
     {% for post in site.posts %}
     {
       "title": "{{ post.title | escape }}",
       "url": "{{ post.url | absolute_url }}",
       "date": "{{ post.date | date: '%Y-%m-%d' }}",
       "content": "{{ post.content | strip_html | truncate: 200 }}"
     }{% if forloop.last == false %},{% endif %}
     {% endfor %}
   ]
   ```

   {% endraw %}

### Étape 3 : Ajouter le champ de recherche et un conteneur pour les résultats

1. Ajoutez le code suivant dans un fichier HTML (par exemple, `default.html` ou `index.html`) où vous voulez afficher la barre de recherche :

   ```html
   <input type="text" id="search-input" placeholder="Rechercher..." />
   <div id="results-container"></div>
   ```

### Étape 4 : Intégrer Simple-Jekyll-Search

1. Ajoutez le script suivant à la fin de votre fichier HTML (après avoir inclus `simple-jekyll-search.min.js`) :

   ```html
   <script src="/assets/js/simple-jekyll-search.min.js"></script>
   <script>
     SimpleJekyllSearch({
       searchInput: document.getElementById('search-input'),
       resultsContainer: document.getElementById('results-container'),
       json: '/search.json',
       searchResultTemplate: '<li><a href="{url}">{title}</a></li>',
       noResultsText: 'Aucun résultat trouvé',
       limit: 10,
       fuzzy: false
     });
   </script>
   ```

### Étape 5 : Tester la recherche

1. Lancez votre site localement avec `jekyll serve`.
2. Accédez à la page où vous avez ajouté la barre de recherche et testez son fonctionnement.

### Notes

- **Personnalisation** : Vous pouvez modifier le fichier `searchResultTemplate` pour afficher plus d'informations (comme la date ou un extrait de contenu).
- **Performance** : Ce plugin est conçu pour les petits sites. Si vous avez un site avec beaucoup de contenu, envisagez une solution de recherche plus robuste.
