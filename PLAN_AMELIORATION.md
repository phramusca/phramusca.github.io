# Plan d'amélioration de l'organisation du projet Jekyll

## 🔴 URGENT - Problèmes critiques

### 1. ✅ Déplacer les fichiers markdown des logiciels hors de `_includes/` - **FAIT**
**Solution appliquée** : Les fichiers ont été déplacés dans `_wiki/linux/soft/` avec un layout `software.html` qui inclut automatiquement les informations du logiciel.

**Résultat** : 
- 21 fichiers `.md` maintenant dans `_wiki/linux/soft/`
- Layout `software.html` créé pour automatiser l'affichage
- Include `software_info.html` pour réutiliser les infos (Ubuntu-fr, Site, Repo)

---

### 2. ✅ Créer un `.gitignore` approprié - **FAIT**
**Solution appliquée** : `.gitignore` créé avec toutes les entrées standards Jekyll.

**Résultat** : 
- `_site/`, `.sass-cache/`, `.jekyll-cache/`, etc. maintenant ignorés
- `Gemfile.lock` ignoré (compatible GitHub Pages)

---

## 🟠 IMPORTANT - Améliorations structurelles

### 3. ✅ Nettoyer les dossiers vides/inutilisés - **FAIT**
**Problème** : `_markdown/`, `notices/`, `scripts/` étaient vides et polluaient la structure.

**Analyse** : 
- Ces dossiers n'étaient **pas des dossiers standards Jekyll**
- Jekyll utilise : `_posts/`, `_layouts/`, `_includes/`, `_data/`, `_site/`, etc.
- Ces dossiers étaient des restes d'une ancienne structure ou des dossiers prévus mais jamais utilisés

**Solution appliquée** : 
- Vérification effectuée : aucun fichier dedans, aucune référence dans le code
- Dossiers supprimés

**Résultat** : Structure plus claire

---

### 4. ✅ Centraliser les images - **FAIT**
**Problème** : Images dispersées entre `assets/images/` et `_wiki/data/`

**Solution appliquée** : 
- Créé `assets/images/wiki/` pour les images du wiki
- Déplacé 4 images de `_wiki/data/` vers `assets/images/wiki/`
- Mis à jour toutes les références dans les fichiers markdown (4 fichiers)
- Supprimé le dossier `_wiki/data/` vide

**Résultat** : 
- Organisation plus logique
- Toutes les images du wiki centralisées dans `assets/images/wiki/`
- Images générales du site dans `assets/images/`
- Références mises à jour avec chemins absolus (`/assets/images/wiki/...`)

---

### 5. ~~Améliorer la structure des données des logiciels~~~~ - **IGNORÉ**
**Décision** : Garder un seul fichier `_data/soft_list.yaml`. La structure actuelle est maintenable et préférée.

---

## 🟡 MOYEN - Optimisations

### 6. ✅ Organiser les layouts - **FAIT**
**Solution appliquée** : 
- Supprimé `simple.md` (fichier de test non utilisé)
- Créé `software.html` pour les pages de logiciels
- Layouts documentés dans le README

**Résultat** : 
- Layouts clairs et documentés
- `software.html` automatise l'affichage des infos des logiciels

---

### 7. Standardiser les noms de fichiers
**Problème** : Mélange de conventions (espaces, underscores, majuscules)

**Solution** : 
- Standardiser sur **snake_case** (ex: `nom_du_logiciel.md`, `google_earth.md`)
- Plus facile à sélectionner en entier le nom
- Renommer progressivement les fichiers
- Mettre à jour les références

**Impact** : 
- Compatibilité cross-platform
- URLs plus propres
- Meilleure sélection dans les éditeurs

---

### 8. ✅ Ajouter un README.md - **FAIT**
**Solution appliquée** : Créé `README.md` avec :
- Description du projet
- Structure des dossiers
- Instructions de développement local (depuis TEST_LOCAL.md)
- Comment ajouter un logiciel
- Documentation des layouts
- Commandes utiles et dépannage

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

