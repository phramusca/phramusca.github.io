# TODO - Plan d'amélioration du projet Jekyll

## 📝 TODOs

Voir TODO Tree.

## 🔧 Tâches d'amélioration structurelles

### 1. ✅ Standardiser les noms de fichiers dans `_wiki/`

Les noms des pages Markdown non conformes ont été normalisés en minuscules
ASCII et `snake_case`, y compris dans `_wiki/archive/`. Les liens internes
concernés ont été mis à jour.

### 2. Organiser le dossier `_wiki/archive/`

**Impact** : Faible, organisation  
**Problème** : Le dossier `archive/` contient du contenu archivé mais sa structure n'est pas claire

**À faire** :

- Documenter pourquoi ces fichiers sont archivés
- Vérifier s'ils doivent rester accessibles ou être complètement exclus
- Peut-être les exclure du build si ce sont vraiment des archives

### 3. Améliorer la structure des données `soft_list.yaml`

**Impact** : Faible, organisation  
**Problème** : Le fichier fait 450+ lignes et peut être difficile à maintenir

**Options** :

- Garder un seul fichier (préférence actuelle) mais mieux structuré
- Ajouter des commentaires pour séparer les sections
- Vérifier la cohérence des données

**Note** : L'utilisateur préfère garder un seul fichier, donc on se concentre sur l'organisation et les commentaires

### 4. Vérifier les liens internes cassés

**Impact** : Moyen, nécessite vérification manuelle  
**Problème** : Après la migration depuis MediaWiki, certains liens internes peuvent être cassés

**À faire** :

- Scanner les fichiers markdown pour les liens internes
- Vérifier que les pages référencées existent
- Corriger les liens cassés

### 5. Optimiser les images

**Impact** : Faible, optimisation  
**Problème** : Les images peuvent être optimisées (taille, format)

**À faire** :

- Vérifier la taille des images dans `assets/images/wiki/`
- Optimiser si nécessaire (compression, format WebP si supporté)
- S'assurer que toutes les images sont bien référencées

## ✅ Tâches complétées

- ✅ Nettoyer les dossiers vides (`_posts/data/`, `_includes/images/`)
- ✅ Corriger le TODO obsolète dans `ventoy.md`
- ✅ Déplacer les fichiers markdown des logiciels hors de `_includes/`
- ✅ Créer un `.gitignore` approprié
- ✅ Nettoyer les dossiers vides/inutilisés
- ✅ Centraliser les images
- ✅ Organiser les layouts
- ✅ Standardiser les noms de fichiers en snake_case (pour les logiciels)
- ✅ Ajouter un README.md complet
- ✅ Exclure les fichiers de documentation du build
- ✅ Documenter les collections, includes, layouts dans le README

## 📝 Notes

- Tester chaque changement localement avant de commit
- Faire des commits atomiques (un changement à la fois)
- Vérifier que le site fonctionne après chaque modification
- Les fichiers dans `_wiki/archive/` peuvent être exclus du build si nécessaire
