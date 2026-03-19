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
- `🔍 Vérifier les liens internes (script maison)` - Vérifie les liens internes directement dans les fichiers Markdown
- `🔍 Vérifier les liens externes (script maison)` - Vérifie les liens externes avec cache
- `🔍 Vérifier les liens (scripts maison)` - Vérifie les liens internes et externes
- `🔍 Vérifier les liens (htmlproofer)` - Vérifie avec htmlproofer (analyse _site)
- `🔍 Vérifier les liens (lychee)` - Vérifie avec lychee (analyse _site)
- `🔍 Vérifier les liens (toutes les méthodes)` - Toutes les méthodes

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
layout: content
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
  
- **`content`** : Layout pour le contenu principal (pages wiki et posts)
  - Hérite de `default`
  - Inclut automatiquement le gestionnaire de liens (distinction interne/externe, ouverture dans nouvel onglet)
  - Inclut automatiquement la table des matières (TOC) flottante
  - Utilisé par défaut pour toutes les pages dans `_wiki/` (sauf les logiciels) et pour tous les posts
  - Facilite l'extension et l'évolution des fonctionnalités communes au contenu
  
- **`software`** : Layout pour les pages de logiciels
  - Hérite de `content` (donc inclut aussi le gestionnaire de liens et la TOC)
  - Inclut automatiquement les informations du logiciel (Ubuntu-fr, Site, Repo) via `software_info.html`
  - Utilisé dans les fichiers de `_wiki/linux/soft/` avec `layout: software`

**Utilisation** : Spécifiez le layout dans le front matter YAML en haut du fichier :

```markdown
---
layout: content
---
```

ou

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

## 📑 Table des matières (TOC)

Le site inclut un système automatique de génération de table des matières pour les pages markdown.

### Utilisation automatique

Le layout `content` inclut automatiquement la table des matières. **Aucune action n'est nécessaire** - la TOC est automatiquement disponible sur toutes les pages utilisant `layout: content` (pages wiki et posts).

### Fonctionnalités

- **Génération automatique** : La TOC est générée par JavaScript à partir des titres de la page (h2 à h6)
- **Flottante** : La TOC apparaît sous forme de bouton flottant sur le côté droit de la page
- **Repliée par défaut** : Le bouton permet d'ouvrir/fermer la TOC à tout moment
- **Imbrication** : Les sous-sections sont automatiquement imbriquées selon leur niveau
- **Navigation** : Cliquer sur un lien dans la TOC ferme automatiquement le panneau
- **Fermeture** : La TOC se ferme en cliquant en dehors, en appuyant sur `Escape`, ou en cliquant sur un lien
- **Ancres automatiques** : Les IDs sont générés automatiquement pour les titres si absents
- **Style cohérent** : Utilise le thème vert du site
- **Responsive** : S'adapte aux petits écrans

### Utilisation manuelle (optionnelle)

Si vous souhaitez utiliser la TOC manuellement dans une page qui n'utilise pas le layout `content`, vous pouvez inclure :

```markdown
{% include toc.html %}
```

### Alternative : Syntaxe Kramdown

Vous pouvez aussi utiliser directement la syntaxe kramdown dans le markdown.

**Important** : La syntaxe `{:toc}` doit être placée après une liste vide :

```markdown
- Table des matières
{:toc}

# Titre principal

## Section 1
...
```

Cette syntaxe génère une TOC basique intégrée dans le contenu, sans le style flottant personnalisé. La liste sera remplacée par la table des matières générée automatiquement.

## 🔍 Moteur de recherche

Le site inclut un moteur de recherche qui indexe automatiquement toutes les pages wiki et les posts.

### Exclusion de sections dans la recherche

Si une page inclut du contenu d'autres pages (par exemple via des includes), vous pouvez exclure certaines sections de l'indexation pour éviter les doublons dans les résultats de recherche.

**Utilisation** :

1. Ajoutez le flag `exclude_search_sections: true` dans le front matter de la page :

```yaml
---
layout: content
title: Ma Page
exclude_search_sections: true
---
```

2. Entourez les sections à exclure avec les marqueurs HTML suivants dans vos templates/includes :

```html
<!-- SEARCH_EXCLUDE_START -->
Contenu à exclure de l'indexation
<!-- SEARCH_EXCLUDE_END -->
```

**Exemple** : La page "Programmes" (`_wiki/linux/soft.md`) utilise cette fonctionnalité pour exclure le contenu des pages individuelles de logiciels qui sont incluses dans le tableau, tout en gardant le reste de la page (introduction, noms de logiciels, descriptions) indexable.

## 🔍 Vérification des liens morts

Ce projet utilise une approche hybride pour vérifier les liens morts :

### Méthodes disponibles

#### Scripts maison (recommandés pour le développement)

- **Liens internes** : Vérifie directement les fichiers Markdown source
  - ✅ Numéros de ligne corrects (du Markdown, pas du HTML)
  - ✅ Pas besoin de build Jekyll
  - ✅ Résolution intelligente des chemins relatifs
  - ❌ Ne vérifie pas les images/scripts
  
- **Liens externes** : Vérifie les URLs HTTP/HTTPS
  - ✅ Numéros de ligne corrects
  - ✅ Cache de 7 jours pour éviter les vérifications répétées
  - ✅ Pas besoin de build Jekyll
  - ❌ Plus lent que les outils spécialisés

**Scripts** : `.vscode/tasks/check_internal_links.py` et `.vscode/tasks/check_external_links.py`

#### Outils externes (recommandés pour la vérification complète)

- **htmlproofer** : Analyse le site généré (`_site/`)
  - ✅ Vérifie les images, scripts, structure HTML
  - ✅ Intégré à l'écosystème Ruby/Jekyll
  - ❌ Numéros de ligne du HTML (pas du Markdown)
  - ❌ Nécessite un build Jekyll

- **lychee** : Analyse le site généré (`_site/`)
  - ✅ Très rapide (écrit en Rust)
  - ✅ Vérification asynchrone
  - ❌ Numéros de ligne du HTML (pas du Markdown)
  - ❌ Nécessite un build Jekyll

### Utilisation

#### Tâches VS Code

- **🔍 Vérifier les liens internes (script maison)** : Vérifie les liens internes
- **🔍 Vérifier les liens externes (script maison)** : Vérifie les liens externes avec cache
- **🔍 Vérifier les liens (scripts maison)** : Vérifie les deux types de liens
- **🔍 Vérifier les liens (htmlproofer)** : Utilise htmlproofer
- **🔍 Vérifier les liens (lychee)** : Utilise lychee
- **🔍 Vérifier les liens (toutes les méthodes)** : Toutes les méthodes

#### Script shell

```bash
# Scripts maison (recommandés pour le développement)
./.vscode/tasks/check_links.sh internal    # Liens internes uniquement
./.vscode/tasks/check_links.sh external     # Liens externes uniquement
./.vscode/tasks/check_links.sh both         # Les deux (scripts maison)

# Outils externes (pour vérification complète)
./.vscode/tasks/check_links.sh htmlproofer  # htmlproofer
./.vscode/tasks/check_links.sh lychee       # lychee
./.vscode/tasks/check_links.sh all          # Toutes les méthodes
```

#### Commandes manuelles

**Scripts maison** :

```bash
# Liens internes
python3 .vscode/tasks/check_internal_links.py

# Liens externes (avec cache dans .cache/external_links_cache.json)
python3 .vscode/tasks/check_external_links.py
```

**htmlproofer** :

```bash
bundle exec jekyll build
bundle exec htmlproofer _site --checks Links,Images,Scripts --no-enforce-https --allow-hash-href --ignore-urls '/#.*/' --ignore-urls 'mailto:.*' --ignore-urls 'tel:.*'
```

**lychee** :

```bash
bundle exec jekyll build
lychee _site --format detailed --verbose --exclude-all-private --exclude "^mailto:.*" --exclude "^tel:.*" --exclude "^#.*$"
```

### Configuration

#### Liens ignorés

Tous les outils ignorent automatiquement :

- Les ancres (`#...`)
- Les liens `mailto:`
- Les liens `tel:`
- Les liens `apt://`, `snap://`, `flatpak+https://` (protocoles système non-HTTP)
- Les projets externes (comme `JaMuz`)
- Les templates Liquid (`{url}`, `{title}`, etc.)

#### Cache

- **Scripts maison (liens externes)** : Cache de 7 jours dans `.cache/external_links_cache.json`
- **htmlproofer** : Cache de 7 jours (configuré dans `.htmlproofer.yml`)
- **lychee** : Pas de cache par défaut

### Recommandations

- **Développement quotidien** : Utilisez les scripts maison (`internal` et `external`)
  - Numéros de ligne corrects
  - Pas besoin de build
  - Rapide pour les liens internes
  
- **Vérification complète** : Utilisez `all` ou les outils externes
  - Vérifie aussi les images et scripts
  - Analyse le site généré (liens résolus par Jekyll)
  - Détection plus robuste des erreurs réseau

### Notes importantes

1. **Build requis** :
   - **Scripts maison** : Pas de build requis ✅
   - **htmlproofer/lychee** : Nécessitent un build Jekyll (`_site/` doit exister)
2. **Numéros de ligne** :
   - **Scripts maison** : Numéros de ligne du Markdown source ✅
   - **htmlproofer/lychee** : Numéros de ligne du HTML généré
3. **GitHub Pages** : Les outils externes nécessitent un build local
4. **Cache** : Le cache des liens externes est stocké dans `.cache/` (ignoré par git)

## 🚫 Exclure des fichiers du build

Pour exclure des fichiers du build Jekyll, ajoutez-les dans `_config.yml` :

```yaml
exclude:
  - README.md
  - TODO.md
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
