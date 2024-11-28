---
layout: default
---

# Welcome

## Projects

- [JaMuz](JaMuz) - Keep your music in check and enjoy it too!
- [Code Samples](https://github.com/phramusca/Samples/tree/main) - Pieces of code

### Under Development

- [Cook And Freeze](https://github.com/phramusca/CookAndFreeze) - With CookAndFreeze for Android, easily manage recipients (content and frozen date) stored in your freezer (or elsewhere).
- [Rom Manager](https://github.com/phramusca/RomManager)

## Wiki en français

Il s'agit plutôt d'un bloc-notes de mon expérience (professionnelle et personnelle) dans ce domaine.

/!\ EN RECONSTRUCTION /!\

- [Linux](wiki/linux/)
- [Windows](wiki/windows/)
- [Android](wiki/android/)
- [Raspberry](wiki/raspberry/)
- [Développement](wiki/dev/)
  - [Java](wiki/dev/Java.md)

------------------------------------------------------------------------

<h1>Blog</h1>
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - <small>{{ post.date | date: "%d %B %Y" }}
      <p>{{ post.excerpt }}</p></small>
    </li>
  {% endfor %}
</ul>

------------------------------------------------------------------------

*Ce site a été converti depuis [MediaWiki](wiki/MediaWiki) en utilisant [mediawiki-to-gfm](https://github.com/outofcontrol/mediawiki-to-gfm) fin 2024, lui-même migré depuis Wikini fin 2009.*
