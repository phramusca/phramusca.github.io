# Plan d'amélioration du projet Jekyll

## 📋 Tâches à faire

### 1. Nettoyer les fichiers/dossiers obsolètes
**Problème** : Certains fichiers/dossiers semblent obsolètes ou inutilisés

**À vérifier/supprimer** :
- `_wiki/linux/soft-old.md` : Fichier avec des TODOs, semble être une ancienne version (à archiver ou supprimer)
- `_posts/data/` : Dossier vide dans `_posts/` (à supprimer)
- `_includes/images/` : Dossier vide (à supprimer)

**Action** :
- Vérifier le contenu et l'usage de ces fichiers
- Supprimer ou archiver si obsolètes
- Documenter si conservés

---

### 2. Standardiser les noms de fichiers dans `_wiki/`
**Problème** : Mélange de conventions de nommage dans `_wiki/`

**Fichiers avec espaces/majuscules** :
- `_wiki/linux/system/Disques_Locaux.md`
- `_wiki/linux/system/Disques_Réseau.md`
- `_wiki/linux/system/Installer_un_programme_sous_Linux.md`
- `_wiki/linux/system/Système_de_Fichiers.md`
- `_wiki/linux/tuto/Créer un panoramique avec Hugin.md`
- `_wiki/perso/Ma_Configuration_LAMP.md`
- `_wiki/perso/Mes_Résultats.md`
- `_wiki/perso/Sauvegardes_et_Restauration.md`
- `_wiki/perso/Sauvegardes_MySQL.md`
- `_wiki/perso/Scripts_de_Backup.md`
- Et d'autres dans `_wiki/archive/`

**Solution** :
- Convertir en snake_case progressivement
- Mettre à jour les liens internes
- Vérifier que les URLs fonctionnent toujours (Jekyll gère les espaces mais c'est moins propre)

**Impact** :
- URLs plus propres
- Meilleure compatibilité cross-platform
- Cohérence avec les fichiers de logiciels déjà en snake_case

---

### 3. Organiser le dossier `_wiki/archive/`
**Problème** : Le dossier `archive/` contient du contenu archivé mais sa structure n'est pas claire

**À faire** :
- Documenter pourquoi ces fichiers sont archivés
- Vérifier s'ils doivent rester accessibles ou être complètement exclus
- Peut-être les exclure du build si ce sont vraiment des archives

---

### 4. Améliorer la structure des données `soft_list.yaml`
**Problème** : Le fichier fait 450+ lignes et peut être difficile à maintenir

**Options** :
- Garder un seul fichier (préférence actuelle) mais mieux structuré
- Ajouter des commentaires pour séparer les sections
- Vérifier la cohérence des données

**Note** : L'utilisateur préfère garder un seul fichier, donc on se concentre sur l'organisation et les commentaires

---

### 5. Vérifier les liens internes cassés
**Problème** : Après la migration depuis MediaWiki, certains liens internes peuvent être cassés

**À faire** :
- Scanner les fichiers markdown pour les liens internes
- Vérifier que les pages référencées existent
- Corriger les liens cassés

---

### 6. Optimiser les images
**Problème** : Les images peuvent être optimisées (taille, format)

**À faire** :
- Vérifier la taille des images dans `assets/images/wiki/`
- Optimiser si nécessaire (compression, format WebP si supporté)
- S'assurer que toutes les images sont bien référencées

---

## ✅ Tâches complétées

- ✅ Déplacer les fichiers markdown des logiciels hors de `_includes/`
- ✅ Créer un `.gitignore` approprié
- ✅ Nettoyer les dossiers vides/inutilisés
- ✅ Centraliser les images
- ✅ Organiser les layouts
- ✅ Standardiser les noms de fichiers en snake_case (pour les logiciels)
- ✅ Ajouter un README.md complet
- ✅ Exclure les fichiers de documentation du build
- ✅ Documenter les collections, includes, layouts dans le README

---

## 📝 Notes

- Tester chaque changement localement avant de commit
- Faire des commits atomiques (un changement à la fois)
- Vérifier que le site fonctionne après chaque modification
- Les fichiers dans `_wiki/archive/` peuvent être exclus du build si nécessaire

