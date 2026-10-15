---
layout: software
---

# Grsync

[Grsync](http://doc.ubuntu-fr.org/grsync) est une interface graphique pour la commande [rsync](https://doc.ubuntu-fr.org/rsync) qui est un logiciel de synchronisation de fichiers.

 Il permet aux utilisateurs de configurer et d'exécuter des tâches de synchronisation de manière conviviale, sans avoir à utiliser la ligne de commande.

## Exclude files/folders

[rsync man](http://www.delafond.org/traducmanfr/man/man1/rsync.1.html)

```console
--exclude-from=FICHIER
   Cette option est similaire à l'option --exclude, mais ajoute les motifs d'exclusion listés dans le fichier FICHIER
à la liste d'exclusion. Les lignes vides dans FICHIER ou les lignes commençant par «;» ou par «#» sont ignorées.
Si FICHIER est - alors la liste sera lue depuis l'entrée standard.
```

Example de `FICHIER`:

```sh
#- **/.git
#- **/app/build/
#- **/.idea
#- **/.gradle
- **/Repos
```

## Alternatives (A TESTER)

Voici des outils Linux pour sauvegarder et versionner des fichiers spécifiques, similaires à Timeshift mais ciblant les fichiers et dossiers, avec options en ligne de commande ou interface graphique.

| Outil        | Versionnement | Interface | Adapté pour             | Configuration |
| ------------ | ------------- | --------- | ----------------------- | ------------- |
| rsnapshot    | Oui           | CLI       | Sauvegardes versionnées | Modéré        |
| Back In Time | Oui           | GUI/CLI   | Utilisation facile      | Facile        |
| Borg + Vorta | Oui           | GUI/CLI   | Sauvegardes robustes    | Modéré        |
| Déjà Dup     | Oui           | GUI       | Sauvegarde simple       | Facile        |

1. **rsnapshot** (ligne de commande)
   - `rsnapshot` est un utilitaire basé sur `rsync` pour les sauvegardes incrémentielles, gérant des versions en utilisant des liens symboliques.
   - **Installation** : Généralement disponible dans les dépôts (ex. `sudo apt install rsnapshot`).
   - Permet de prendre des instantanés fréquents de dossiers, pour restaurer des versions spécifiques.
2. **Back In Time** (GUI et ligne de commande)
   - `Back In Time` est une interface graphique (et en ligne de commande) pour créer des sauvegardes incrémentielles de fichiers et dossiers spécifiques. Il utilise `rsync` et `diff` pour stocker des versions.
   - **Avantages** :
     - Interface facile à utiliser.
     - Peut être configuré pour des sauvegardes automatiques.
   - **Installation** : Disponible dans les dépôts (ex. `sudo apt install backintime-qt`).
3. **Borg Backup + Vorta** (GUI pour Borg)
   - **Borg** est un utilitaire de ligne de commande pour des sauvegardes dédupliquées et chiffrées. Il est très performant pour les sauvegardes de fichiers en raison de sa déduplication.
   - **Vorta** est une interface graphique qui facilite l’utilisation de Borg.
   - **Installation** :
     - Borg : `sudo apt install borgbackup`
     - Vorta : disponible via des AppImage ou dans certains dépôts (comme Flatpak).
4. **Déjà Dup** (GUI)
   - Déjà Dup est un utilitaire de sauvegarde pour l’environnement GNOME, simple d’utilisation, permettant de configurer des sauvegardes automatiques de fichiers spécifiques.
   - **Installation** : Disponible dans la plupart des distributions (ex. `sudo apt install deja-dup`).
