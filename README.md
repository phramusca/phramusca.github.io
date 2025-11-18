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

### Dépannage

#### Erreur "bundle: command not found"
```bash
gem install bundler
```

#### Erreur de port déjà utilisé
```bash
# Tuer le processus sur le port 4000
lsof -ti:4000 | xargs kill -9
```

#### Rebuild complet
```bash
bundle exec jekyll clean
bundle exec jekyll build
bundle exec jekyll serve
```

## 📁 Structure du projet

```
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
└── PLAN_AMELIORATION.md # Plan d'amélioration (exclu du build)
```

## 📝 Ajouter un logiciel

Pour ajouter un nouveau logiciel à la liste :

1. **Ajouter dans `_data/soft_list.yaml`** dans la catégorie appropriée :
   ```yaml
   - nom: Nom du Logiciel
     apt: nom-du-paquet
     url_internal: nom_du_logiciel  # En snake_case, correspond au nom du fichier .md
     url_doc_ubuntu_fr: https://doc.ubuntu-fr.org/...
     url_website: https://...
     url_repository: https://github.com/...
     description: Description du logiciel
   ```

2. **Créer la page dans `_wiki/linux/soft/nom_du_logiciel.md`** (nom en snake_case) :
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

- `default` : Layout par défaut du thème (pages-themes/hacker)
- `software` : Layout pour les pages de logiciels (inclut automatiquement les infos via `software_info.html`)

## 🔗 Système de logiciels

Le système de gestion des logiciels utilise :

- **`_data/soft_list.yaml`** : Liste structurée par catégories avec toutes les informations
- **`url_internal`** : Identifiant en snake_case qui correspond au nom du fichier `.md` (ex: `calibre`, `ripper_x`)
- **`_includes/linux/soft/table.html`** : Affiche la liste des logiciels avec contenu expandable
- **`_includes/linux/soft/software_info.html`** : Affiche automatiquement les infos (Ubuntu-fr, Site, Repo)
- **`_layouts/software.html`** : Layout qui inclut automatiquement `software_info.html` pour les pages de logiciels

**Convention de nommage** : Tous les fichiers de logiciels sont en **snake_case** (ex: `easy_tag.md`, `google_earth.md`).

## 🔧 Technologies

- **Jekyll** : Générateur de site statique
- **GitHub Pages** : Hébergement
- **Liquid** : Moteur de templates
- **Kramdown** : Processeur Markdown

## 📄 Licence

Ce site est un projet personnel. Le contenu est sous licence appropriée selon les sources originales.

## 🔗 Liens

- Site en ligne : https://phramusca.github.io
- Repository : https://github.com/phramusca/phramusca.github.io

---

*Ce site a été converti depuis MediaWiki en utilisant [mediawiki-to-gfm](https://github.com/outofcontrol/mediawiki-to-gfm) fin 2024, lui-même migré depuis Wikini fin 2009.*

