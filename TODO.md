# TODO - Plan d'amélioration du projet Jekyll

## 📝 TODOs

Voir TODO Tree.

## 🔧 Tâches d'amélioration structurelles

### 1. Améliorer la structure des données `soft_list.yaml`

**Impact** : Faible, organisation  
**Problème** : Le fichier fait 450+ lignes et peut être difficile à maintenir

**Options** :

- Garder un seul fichier (préférence actuelle) mais mieux structuré
- Ajouter des commentaires pour séparer les sections
- Vérifier la cohérence des données

**Note** : L'utilisateur préfère garder un seul fichier, donc on se concentre sur l'organisation et les commentaires

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
