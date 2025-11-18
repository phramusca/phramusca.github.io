# Plan d'amélioration de l'organisation du projet Jekyll

## 🔴 URGENT - Problèmes critiques

### 1. Déplacer les fichiers markdown des logiciels hors de `_includes/`
**Problème** : Les fichiers comme `Calibre.md`, `Meld.md`, etc. sont dans `_includes/` alors que ce dossier est destiné aux snippets réutilisables (templates, partials), pas au contenu.

**Solution** : Créer un dossier dédié pour le contenu des logiciels
- Option A (recommandée) : Créer `_data/soft_content/` et y déplacer tous les `.md`
- Option B : Créer `_soft/` comme collection Jekyll
- Option C : Les intégrer dans `_wiki/linux/soft/` avec une structure cohérente

**Impact** : 
- Améliore la maintenabilité
- Respecte les conventions Jekyll
- Facilite la gestion du contenu

**Fichiers concernés** : 21 fichiers `.md` dans `_includes/`

---

### 2. Créer un `.gitignore` approprié
**Problème** : Le dossier `_site/` (build Jekyll) et `vendor/` sont versionnés, ce qui pollue le repo.

**Solution** : Créer un `.gitignore` avec :
```
_site/
.sass-cache/
.jekyll-cache/
.jekyll-metadata
vendor/
.bundle/
*.gem
*.gemfile.lock
.DS_Store
```

**Impact** : 
- Réduit la taille du repo
- Évite les conflits de merge
- Pratique standard Jekyll

---

## 🟠 IMPORTANT - Améliorations structurelles

### 3. Nettoyer les dossiers vides/inutilisés
**Problème** : `_markdown/`, `notices/`, `scripts/` sont vides et polluent la structure.

**Solution** : 
- Supprimer s'ils ne sont pas utilisés
- Ou documenter leur usage prévu dans un README

**Impact** : Structure plus claire

---

### 4. Centraliser les images
**Problème** : Images dispersées entre `assets/images/` et `_wiki/data/`

**Solution** : 
- Garder `assets/images/` pour les images générales du site
- Créer `assets/images/wiki/` pour les images du wiki
- Déplacer `_wiki/data/*.jpg` vers `assets/images/wiki/`
- Mettre à jour les références dans les fichiers markdown

**Impact** : 
- Organisation plus logique
- Facilite la maintenance
- Meilleure performance (assets optimisés)

---

### 5. Améliorer la structure des données des logiciels
**Problème** : Le fichier `_data/soft_list.yaml` est très long (450+ lignes) et difficile à maintenir.

**Solution** : 
- Option A : Diviser par catégorie (`_data/soft/accessoires.yaml`, `_data/soft/bureautique.yaml`, etc.)
- Option B : Créer une structure avec des fichiers séparés pour chaque logiciel
- Option C : Garder un seul fichier mais mieux structuré avec des commentaires

**Impact** : 
- Meilleure maintenabilité
- Facilite l'ajout/modification de logiciels
- Réduit les risques d'erreurs

---

## 🟡 MOYEN - Optimisations

### 6. Organiser les layouts
**Problème** : Un seul layout `simple.md` dans `_layouts/`, mais le projet utilise `default` (du thème).

**Solution** : 
- Créer des layouts personnalisés si nécessaire
- Documenter l'usage des layouts

---

### 7. Standardiser les noms de fichiers
**Problème** : Mélange de conventions (espaces, underscores, majuscules)

**Solution** : 
- Standardiser sur kebab-case (ex: `calibre.md`, `google-earth.md`)
- Renommer progressivement les fichiers
- Mettre à jour les références

**Impact** : 
- Compatibilité cross-platform
- URLs plus propres
- Meilleure lisibilité

---

### 8. Ajouter un README.md
**Problème** : Pas de documentation sur la structure du projet.

**Solution** : Créer un `README.md` avec :
- Description du projet
- Structure des dossiers
- Comment ajouter un logiciel
- Comment contribuer
- Instructions de build local

---

## 📋 Ordre d'exécution recommandé

1. **Créer `.gitignore`** (5 min) - Impact immédiat, pas de risque
2. **Déplacer les fichiers markdown** (30 min) - Impact majeur, nécessite tests
3. **Nettoyer les dossiers vides** (5 min) - Simple, pas de risque
4. **Centraliser les images** (20 min) - Nécessite mise à jour des références
5. **Améliorer la structure des données** (1h) - Refactoring plus important
6. **Standardiser les noms** (30 min) - Peut être fait progressivement
7. **Ajouter README** (15 min) - Documentation

---

## 📝 Notes

- Tester chaque changement localement avant de commit
- Faire des commits atomiques (un changement à la fois)
- Mettre à jour les références dans tous les fichiers concernés
- Vérifier que le site fonctionne après chaque modification

