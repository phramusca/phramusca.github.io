---
layout: default
---

<!-- https://github.com/christian-fei/Simple-Jekyll-Search -->
<script src="https://cdn.jsdelivr.net/npm/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js"></script>
<script>
document.addEventListener('DOMContentLoaded', function() {
  SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results'),
    json: "{{ '/search.json' | relative_url }}",
    searchResultTemplate: '<li><a href="{url}">{title}</a></li>',
    noResultsText: 'Aucun résultat trouvé',
    limit: 10
  });
});
</script>

# Welcome

## Projects

- [JaMuz](JaMuz) - Keep your music in check and enjoy it too!
- [Code Samples](https://github.com/phramusca/Samples/tree/main) - Pieces of code

### Under Development

- [Cook And Freeze](https://github.com/phramusca/CookAndFreeze) - With CookAndFreeze for Android, easily manage recipients (content and frozen date) stored in your freezer (or elsewhere).
- [Rom Manager](https://github.com/phramusca/RomManager)

## Le Carré Français 🇫🇷

<input type="text" id="search-input" placeholder="Rechercher...">
<div id="results"></div>
------------------------------------------------------------------------

### Wiki

⚠️ En reconstruction

- [Docker](wiki/docker)
- [Linux](wiki/linux)
  - [Programmes](wiki/linux/soft) ✅
  - [Système](wiki/linux/system) ⚠️
- [Windows](wiki/windows)
- [Android](wiki/android) ⚠️
- [Raspberry](wiki/raspberry) ⚠️
- [Développement](wiki/dev) ⚠️
  - [Java](wiki/dev/Java) ⚠️

### Publications

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }}) <sub><sup>{{ post.date | date: "%d/%m/%Y" }}</sup></sub>
  - <small>*{{ post.excerpt }}* </small>
{% endfor %}

------------------------------------------------------------------------

*Ce site a été converti depuis [MediaWiki](wiki/MediaWiki) en utilisant [mediawiki-to-gfm](https://github.com/outofcontrol/mediawiki-to-gfm) fin 2024, lui-même migré depuis Wikini fin 2009.*
