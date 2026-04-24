---
layout: content
---

# Programmes

## Ma Sélection

### Applications

#### Programmation

TODO: Rajouter:

- Visual Studio Code
- Git gui clients (FAIRE LE TRI)
  - Gitkraken: seulement open source. Pas de private ni de self-hosted
  - GitAhead: discontinued
  - SmartGit: payant. A tester maintenant que licence open source
  - Gittyup: continuation of gitAhead but does not work :(
  - Gitnuro: pareil, freeze
  - Sublime Merge: pas mal, à tester davantage.
    - Sublime Merge may be downloaded and evaluated for free, however a license must be purchased for continued use. There is currently no enforced time limit for the evaluation (22/4/2024)
  - gitg: gnome. pas mal, à tester davantage
  - git-cola, a tester
  - gitbutler, a tester
  - gitk, a tester
  - QGit, a tester
  - kommit, a tester
  - sourcegit, a tester
  - source app, a tester
  - kdesvn, a tester

#### Son et Vidéo

TODO: Ajouter ?

- Qobuz Downloader
- SoulSeek

##### Audio

TODO: Comparer Jamuz (perfs) avec <https://doc.ubuntu-fr.org/rhythmbox> (installé par défaut)

TODO: Faire un paquet deb pour JaMuz, puis faire un PPA ou mieux ajouter dans les repos ubuntu/linux mint/debian

TODO: Move to JaMuz

- Genre icons (for future use):
  - <http://www.iconarchive.com/show/music-genre-icons-by-sirubico.html>
  - <http://www.flickr.com/groups/itunesgenres/pool/>
  - <http://myssynen.deviantart.com/art/Music-genre-images-71751056>
  - <http://www.mede8erforum.com/index.php?topic=5472.0>
  - <http://www.iconeasy.com/iconset/music-genre-icons/>

- Une [liste de lecteurs](http://doc.ubuntu-fr.org/lecteur_audio) sur Ubuntu-fr
- Mon comparateur (en cours):
  <http://socialcompare.com/fr/comparison/linux-open-source-audio-players-p4v154w>
- Alternatives à AmaroK:
  <http://alternativeto.net/software/amarok/?platform=linux&license=free>

##### Vidéo

TODO:  Voir aussi [Fusionner 2 fichiers avi avec mencoder](http://www.ubuntuhowtos.com/howtos/merge_avi_files_with_mencoder)

TODO:  Voir aussi: [Convertir MOV en Flash FLV](../../archive/Convertir_MOV_en_Flash_FLV)

#### Administration

TODO: Ajouter:

- Back In Time ?
- Disks - gnome-disks
- Mission Center
- WoeUSB (Prepare Microsoft Windows installation USB with ease.)

TODO: /!\ Comment gérer rsync/grsync et autres cas de gui pour outil de ligne de commande

|                                                   |                                                                                                                |                                                        |                                          |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------- |
| Nom                                               | ubuntu-fr                                                                                                      | Description                                            | Installation [apturl](../system/Apt-url) |
| Gparted                                           | [gparted](http://doc.ubuntu-fr.org/gparted)                                                                    | Partitionnement de disque.                             | [gparted](apt://gparted)                 |
| [grsync](../soft/rsync)                           | Synchronisation de fichiers.                                                                                   | [grsync](apt://grsync)                                 |                                          |
| [VirtualBox](http://doc.ubuntu-fr.org/virtualbox) | Solution de virtualisation de systèmes d'exploitation. [Images toutes prêtes](http://virtualboxes.org/images/) | Voir [VirtualBox](http://doc.ubuntu-fr.org/virtualbox) |                                          |

|                                                      |                                                                                          |                                                                                   |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Nom                                                  | Description                                                                              | [apt-url](Apt-url) (Installation)                                                 |
| [winff](http://doc.ubuntu-fr.org/winff)              | WinFF est une interface graphique à FFmpeg très simple d'utilisation et personnalisable. | [winff](apt://winff) + [codecs](http://ubuntuforums.org/showthread.php?t=1117283) |
| [avidemux](http://doc.ubuntu-fr.org/avidemux)        | Editeur vidéo, considéré comme l'équivalent de VirtualDub.                               | [avidemux](apt://avidemux)                                                        |
| [Arista Transcoder](http://doc.ubuntu-fr.org/arista) | logiciel de conversion vidéo                                                             | [arista](apt://arista)                                                            |
| [QuickTime](../../../QuickTime)                      | QuickTime pour Linux                                                                     |                                                                                   |
| DVDShrink                                            | xDVDShrink - a tester                                                                    |                                                                                   |
| [ManDVD](http://doc.ubuntu-fr.org/mandvd)            | Création simplifiée de DVD-vidéos, a tester                                              |                                                                                   |

### A REVOIR

TODO Tester et intégrer ce qui suit (de Chat GPT):

#### Outils de Sauvegarde Versionnée pour Fichiers sous Linux

Voici des outils Linux pour sauvegarder et versionner des fichiers spécifiques, similaires à Timeshift mais ciblant les fichiers et dossiers, avec options en ligne de commande ou interface graphique.

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

##### Comparaison rapide

| Outil        | Versionnement | Interface | Adapté pour             | Configuration |
| ------------ | ------------- | --------- | ----------------------- | ------------- |
| rsnapshot    | Oui           | CLI       | Sauvegardes versionnées | Modéré        |
| Back In Time | Oui           | GUI/CLI   | Utilisation facile      | Facile        |
| Borg + Vorta | Oui           | GUI/CLI   | Sauvegardes robustes    | Modéré        |
| Déjà Dup     | Oui           | GUI       | Sauvegarde simple       | Facile        |

En fonction de vos besoins (sauvegarde fréquente, déduplication, interface graphique), **Back In Time** et **Vorta** sont de bons choix avec une interface graphique, tandis que **rsnapshot** est très efficace en ligne de commande.
