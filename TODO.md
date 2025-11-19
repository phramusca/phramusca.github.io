# TODO - Plan d'amélioration du projet Jekyll

## 🚀 Quick Wins (à faire en premier)

### 1. Nettoyer les dossiers vides
**Impact** : Faible, nettoyage simple  
**Fichiers** :
- `_posts/data/` : Dossier vide à supprimer
- `_includes/images/` : Dossier vide à supprimer

**Action** : Supprimer ces dossiers

---

### 2. Corriger le TODO dans ventoy.md
**Impact** : Faible, correction simple  
**Fichier** : `_wiki/linux/soft/ventoy.md`

**Problème** : Ligne 4 contient "TODO: Rajouter layout partout" mais le layout est déjà présent (ligne 2)

**Action** : Supprimer la ligne 4

---

### 3. Archiver ou supprimer soft-old.md
**Impact** : Faible, nettoyage  
**Fichier** : `_wiki/linux/soft-old.md`

**Problème** : Fichier avec beaucoup de TODOs, semble être une ancienne version

**Action** :
- Déplacer dans `_wiki/archive/linux/soft-old.md` OU
- Supprimer si vraiment obsolète

---

### 4. Nettoyer les fichiers avec "TODO: Revoir"
**Impact** : Moyen, nécessite vérification du contenu  
**Fichiers** :
- `_wiki/linux/soft/wine.md` : Ligne 7 "TODO: Revoir et/ou archiver"
- `_wiki/linux/soft/meld.md` : Ligne 8 "TODO: A revoir"
- `_wiki/linux/soft/easy_tag.md` : Ligne 7 "TODO: Revoir"

**Action** :
- Vérifier le contenu de chaque fichier
- Soit mettre à jour le contenu, soit archiver, soit supprimer le TODO si le contenu est OK

---

## 📝 TODOs dans les fichiers de logiciels

### Calibre (`_wiki/linux/soft/calibre.md`)
- Ligne 40 : `TODO: Comment gérer les collections, l'état de lecture (reading, read, ... le %), ... ?`
- Ligne 46 : `TODO`
- Ligne 50 : `TODO`
- Ligne 62 : `TODO`
- Ligne 72 : `TODO: Essayer des alternatives:`
- Ligne 77 : `TODO; Reprendre la doc (bien faite) :https://christophe-rhein.canoprof.fr/eleve/Fabricolages/Comment_creer_une_bibliotheque_numerique_de_3000_livres/activities/biblio_autonome.xhtml`
- Ligne 81 : `TODO: Ajouter un moteur de recherche js (comme sur phramusca.github.io)`
- Ligne 83 : `TODO , documenter: Support OPDS sur Kobo (fnac) inenviseagable https://www.liseuses.net/liseuses-opds/ sauf à passer sur une inBook https://www.liseuses.net/les-liseuses-inkbook-chez-youboox/`
- Ligne 103 : `TODO: Lancer avec java8 pour résoudre les problèmes d'encodage de caractères`
- Ligne 130 : `TODO:`
- Ligne 141 : `TODO: On y était presque :(`

**Action** : Passer en revue et compléter ou supprimer ces TODO

---

### VNC (`_wiki/linux/soft/vnc.md`)
- Ligne 7 : `TODO: Mettre à jour (TigerVNC, gvncviewer, Remmina, authentification - certificats, ...)`

**Action** : Mettre à jour la documentation VNC

---

### Mono (`_wiki/linux/soft/mono.md`)
- Ligne 58 : `- [Subversion](Subversion): **TODO**`

**Action** : Compléter ou supprimer cette ligne

---

### Hugin (`_wiki/linux/soft/hugin.md`)
- Ligne 5 : `Hugin est un bal bla bla .... TODO`
- Ligne 7 : `TODO: Ajouter une mention mise à jour sur toutes les pages mises à jour`
- Ligne 20 : `TODO *A VALIDER (11/2024) !*`
- Ligne 65 : `TODO *D'autres, trouvailles sur internet en 11/2024, A TESTER:*`
- Ligne 73 : `TODO *Du TRES vieux, à archiver:*`

**Action** : Compléter la description, valider les infos, archiver l'ancien contenu

---

### BOINC (`_wiki/linux/soft/boinc.md`)
- Ligne 6 : `TODO: Supprimer les liens de niveau 1 (tous les fichiers  dans ce dossier), car contenu intégré dans soft`
- Ligne 14 : `TODO: Comment lancer \`boinc\` ?`
- Ligne 27 : `TODO: Voir https://boinc.berkeley.edu/gui_rpc.php`

**Action** : Compléter la documentation BOINC

---

### Waydroid (`_wiki/linux/Waydroid.md`)
- Ligne 26 : `TODO: H2 have a windowed mode ?`
- Ligne 27 : `TODO: H2 change keyword to azerty as it is on cinnamon default ?`
- Ligne 35 : `=> TODO: Revoir cette partie`

**Action** : Compléter la documentation Waydroid, notamment pour Cinnamon

---

### Tuto Hugin (`_wiki/linux/tuto/Créer un panoramique avec Hugin.md`)
- Ligne 7 : `TODO: Lister les paramètres et astuces pour faire un panoramique cylindrique ou sphérique avec Hugin`

**Action** : Compléter le tutoriel

---

### System Index (`_wiki/linux/system/index.md`)
- Ligne 7 : `TODO : Faire de cette page le README for Système !!`

**Action** : Améliorer cette page pour en faire une page d'index/README pour la section Système

---

## 🔧 Tâches d'amélioration structurelles

### 5. Standardiser les noms de fichiers dans `_wiki/`
**Impact** : Moyen, nécessite mise à jour des liens  
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
- Vérifier que les URLs fonctionnent toujours

**Impact** :
- URLs plus propres
- Meilleure compatibilité cross-platform
- Cohérence avec les fichiers de logiciels déjà en snake_case

---

### 6. Organiser le dossier `_wiki/archive/`
**Impact** : Faible, organisation  
**Problème** : Le dossier `archive/` contient du contenu archivé mais sa structure n'est pas claire

**À faire** :
- Documenter pourquoi ces fichiers sont archivés
- Vérifier s'ils doivent rester accessibles ou être complètement exclus
- Peut-être les exclure du build si ce sont vraiment des archives

---

### 7. Améliorer la structure des données `soft_list.yaml`
**Impact** : Faible, organisation  
**Problème** : Le fichier fait 450+ lignes et peut être difficile à maintenir

**Options** :
- Garder un seul fichier (préférence actuelle) mais mieux structuré
- Ajouter des commentaires pour séparer les sections
- Vérifier la cohérence des données

**Note** : L'utilisateur préfère garder un seul fichier, donc on se concentre sur l'organisation et les commentaires

---

### 8. Vérifier les liens internes cassés
**Impact** : Moyen, nécessite vérification manuelle  
**Problème** : Après la migration depuis MediaWiki, certains liens internes peuvent être cassés

**À faire** :
- Scanner les fichiers markdown pour les liens internes
- Vérifier que les pages référencées existent
- Corriger les liens cassés

---

### 9. Optimiser les images
**Impact** : Faible, optimisation  
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

