# phramusca.github.io

Site personnel hébergé sur GitHub Pages, construit avec Jekyll. Ce site contient un wiki avec des informations sur Linux, Windows, Android, Docker, et d'autres sujets techniques.

## 🚀 Développement local

### Prérequis

- VS Code avec l'extension Dev Containers
- Docker (pour le dev container)

### Installation et lancement

1. **Ouvrir dans VS Code avec Dev Container** :
   - Ouvrez le projet dans VS Code
   - Appuyez sur `F1` ou `Ctrl+Shift+P`
   - Tapez "**Dev Containers: Reopen in Container**"
   - Attendez que le container se construise (première fois : ~2-3 min)

2. **Installer les dépendances** (automatique au premier lancement, sinon) :
   - Appuyez sur `F1` ou `Ctrl+Shift+P`
   - Tapez "**Tasks: Run Task**"
   - Sélectionnez "**Bundle: Install**"
   - OU dans le terminal : `bundle install`

3. **Lancer le serveur de développement** :
   - Appuyez sur `F1` ou `Ctrl+Shift+P`
   - Tapez "**Tasks: Run Task**"
   - Sélectionnez "**Jekyll: Serve (développement)**"
   - OU dans le terminal : `bundle exec jekyll serve --livereload`

4. **Accéder au site** :
   - Le site sera accessible sur `http://localhost:4000`
   - Les modifications sont rechargées automatiquement (livereload)

### Commandes utiles

- **Build le site** : `bundle exec jekyll build`
- **Nettoyer le build** : `bundle exec jekyll clean`
- **Serveur sans livereload** : `bundle exec jekyll serve`

### Tasks VS Code disponibles

- `Jekyll: Serve (développement)` - Lance le serveur avec livereload
- `Jekyll: Build` - Construit le site sans le servir
- `Jekyll: Clean` - Nettoie le dossier `_site/`
- `Bundle: Install` - Installe les dépendances Ruby

## 📁 Structure du projet

```bash
.
├── _config.yml          # Configuration Jekyll
├── _data/               # Données (YAML, JSON)
│   └── soft_list.yaml   # Liste des logiciels Linux
├── _includes/           # Snippets réutilisables (templates)
│   └── linux/
│       └── soft/        # Templates pour la liste des logiciels
├── _layouts/            # Layouts (templates de pages)
│   └── software.html      # Layout pour les pages de logiciels
├── _posts/              # Articles de blog
├── _wiki/               # Collection wiki (contenu principal)
│   ├── linux/
│   │   └── soft/        # Pages individuelles des logiciels
│   ├── windows/
│   ├── android/
│   └── ...
├── assets/              # Fichiers statiques (CSS, JS, images)
│   └── images/          # Images
│       └── wiki/        # Images du wiki
├── Gemfile              # Dépendances Ruby
├── README.md            # Documentation du projet
└── .gitignore           # Fichiers ignorés par Git
```

> Notes:
>
> - assets/ est standard Jekyll (copié tel quel dans _site/)
> - Les dossiers avec \_ (comme \_posts/, \_layouts/) sont spéciaux
> - Certains fichiers sont exclus du build Jekyll (voir _config.yml > exclude)

## 📝 Ajouter un logiciel

Pour ajouter un nouveau logiciel à la liste :

1. **Ajouter dans `_data/soft_list.yaml`** dans la catégorie appropriée :

   ```yaml
   - nom: Nom du Logiciel
     apt: nom-du-paquet
     url_internal: nom_du_logiciel  # En snake_case, correspond au nom du fichier .md dans le dossier _includes/linux/soft
     url_doc_ubuntu_fr: https://doc.ubuntu-fr.org/...
     url_website: https://...
     url_repository: https://github.com/...
     description: Description du logiciel
   ```

1. **Créer la page dans `_wiki/linux/soft/nom_du_logiciel.md`** (nom en snake_case) :

   ```markdown
   ---
   layout: software
   ---
   
   # Nom du Logiciel
   
   Contenu de la page...
   ```

   **Important** :

   - Le `url_internal` dans le YAML doit correspondre exactement au nom du fichier (sans `.md`)
   - Le layout `software` inclut automatiquement les informations (Ubuntu-fr, Site, Repo) depuis `soft_list.yaml`
   - Les fichiers doivent être en **snake_case** (ex: `easy_tag.md`, `google_earth.md`)

## 📰 Ajouter un article (post)

Les articles de blog sont dans `_posts/` avec le format : `YYYY-MM-DD-Titre.md`

**Structure d'un post** :

```markdown
---
layout: default
excerpt: Résumé court de l'article
title: Titre de l'article
---

Contenu de l'article en markdown...
```

**Exemple** : `_posts/2025-03-07-gTile.md`

Les posts apparaissent automatiquement sur la page d'accueil via `{% for post in site.posts %}`.

## 🎨 Layouts disponibles

Les layouts sont des templates de pages définis dans `_layouts/` :

- **`default`** : Layout par défaut du thème (pages-themes/hacker)
  - Utilisé par défaut pour toutes les pages
  - Peut être surchargé en spécifiant un autre layout dans le front matter
  
- **`software`** : Layout pour les pages de logiciels
  - Hérite de `default`
  - Inclut automatiquement les informations du logiciel (Ubuntu-fr, Site, Repo) via `software_info.html`
  - Utilisé dans les fichiers de `_wiki/linux/soft/` avec `layout: software`

**Utilisation** : Spécifiez le layout dans le front matter YAML en haut du fichier :

```markdown
---
layout: software
---
```

## 🔗 Système de logiciels

Le système de gestion des logiciels utilise :

- **`_data/soft_list.yaml`** : Liste structurée par catégories avec toutes les informations
- **`url_internal`** : Identifiant en snake_case qui correspond au nom du fichier `.md` (ex: `calibre`, `ripper_x`)
- **`_includes/linux/soft/table.html`** : Affiche la liste des logiciels avec contenu expandable
- **`_includes/linux/soft/software_info.html`** : Affiche automatiquement les infos (Ubuntu-fr, Site, Repo)
- **`_layouts/software.html`** : Layout qui inclut automatiquement `software_info.html` pour les pages de logiciels

**Convention de nommage** : Tous les fichiers de logiciels sont en **snake_case** (ex: `easy_tag.md`, `google_earth.md`).

## 📚 Collections Jekyll

Les **collections** permettent d'organiser du contenu en dehors des posts. Le projet utilise la collection `wiki` :

**Configuration dans `_config.yml`** :

```yaml
collections:
  wiki:
    output: true        # Génère des fichiers HTML pour chaque page
    permalink: /wiki/:path/  # Structure d'URL : /wiki/linux/soft/calibre/
```

**Structure** :

- Les fichiers sont dans `_wiki/` (dossier avec `_` = collection Jekyll)
- Accessibles via `site.wiki` dans les templates Liquid
- Chaque fichier devient une page accessible via son chemin relatif

**Exemple d'utilisation** :

```liquid
{% for page in site.wiki %}
  <a href="{{ page.url }}">{{ page.title }}</a>
{% endfor %}
```

## 🧩 Includes

Les **includes** (`_includes/`) sont des snippets réutilisables de code Liquid/HTML :

- **`_includes/linux/soft/table.html`** : Génère le tableau de la liste des logiciels
  - Utilisé dans les pages de catégories de logiciels
  - Affiche les logiciels avec contenu expandable
  
- **`_includes/linux/soft/software_info.html`** : Affiche les infos d'un logiciel
  - Peut être utilisé avec `{% include linux/soft/software_info.html logiciel=logiciel %}`
  - Ou automatiquement dans le layout `software`

**Utilisation** :

```liquid
{% include linux/soft/software_info.html logiciel=logiciel %}
```

## 🚫 Exclure des fichiers du build

Pour exclure des fichiers du build Jekyll, ajoutez-les dans `_config.yml` :

```yaml
exclude:
  - README.md
  - PLAN_AMELIORATION.md
  - .devcontainer/
  # ... etc
```

**Important** : En Jekyll 3.x, définir `exclude` remplace la liste par défaut. Il faut donc inclure les exclusions par défaut de Jekyll (`.sass-cache/`, `node_modules/`, `vendor/`, etc.) si vous définissez une liste personnalisée.

Les fichiers exclus ne seront pas copiés dans `_site/` lors du build.

## 🔧 Technologies

- **GitHub Pages** : Hébergement
- **Jekyll** : Générateur de site statique
- **Kramdown** : Processeur Markdown
- **Liquid** : Moteur de templates

## 📄 Licence

Ce site est un projet personnel. Le contenu est sous licence appropriée selon les sources originales.

## 🔗 Liens

- Site en ligne : https://phramusca.github.io
- Repository : https://github.com/phramusca/phramusca.github.io

---

*Ce site a été converti depuis MediaWiki en utilisant [mediawiki-to-gfm](https://github.com/outofcontrol/mediawiki-to-gfm) fin 2024, lui-même migré depuis Wikini fin 2009.*
