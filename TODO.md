# TODO - Plan d'amélioration du projet Jekyll

## 📝 TODOs

Voir TODO Tree.

## 🔧 Tâches d'amélioration structurelles

### 1. ✅ Améliorer la structure des données `soft_list.yaml`

**Impact** : Faible, organisation  
**Problème** : Le fichier fait 450+ lignes et peut être difficile à maintenir

Le catalogue reste dans un seul fichier, avec des commentaires de structure et des valeurs `archive` uniformisées. Les logiciels de l'ancienne archive ont été ajoutés au catalogue avec `archive: true`; seuls les logiciels sont conservés sous forme d'entrées, pas les pages d'archive.

### 2. Vérifier les liens internes cassés

**Impact** : Moyen, nécessite vérification manuelle  
**Problème** : Après la migration depuis MediaWiki, certains liens internes peuvent être cassés

**À faire** :

- Scanner les fichiers markdown pour les liens internes
- Vérifier que les pages référencées existent
- Corriger les liens cassés

### 3. Optimiser les images

**Impact** : Faible, optimisation  
**Problème** : Les images peuvent être optimisées (taille, format)

**À faire** :

- Vérifier la taille des images dans `assets/images/wiki/`
- Optimiser si nécessaire (compression, format WebP si supporté)
- S'assurer que toutes les images sont bien référencées

## 📝 Notes

- Tester chaque changement localement avant de commit
- Faire des commits atomiques (un changement à la fois)
- Vérifier que le site fonctionne après chaque modification
- Les fichiers dans `_wiki/archive/` peuvent être exclus du build si nécessaire
