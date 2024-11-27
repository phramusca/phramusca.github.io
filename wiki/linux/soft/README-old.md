# Programmes

## Ma Sélection

### Applications

#### Accessoires

#### Autre

TODO: Faire le tri entre Wayland (à revoir aussi) et le reste

#### Bureautique

TODO: archiver: "livret-2.deb": https://www.biotechno.fr/BookletImposer.html) VS bookletimposer

#### Education


#### Graphisme

TODO: Ajouter: XSane (=> Integrer page locale sur imprimante lexmark)

#### Internet

TODO Rajouter ?

- 4kyoutubetomp3
- MEGAsync

TODO: Revoir rsync / rclone:

- [rclone](soft/rclone)
- Manipuler les fichiers sur des stockages cloud.
- [rclone-browser](apt://rclone-browser)

TODO: Faire section "Remote desktop / VNC" mais tester avant avec Rpi et d'autres
- [VNC](VNC)
- Remmina
- TigerVNC (voir page sur VNC)
- autres ? https://doc.ubuntu-fr.org/bureau_a_distance

TODO: Faire section FTP, et ajouter FileZilla et lftp (script. et gui ?)

#### Jeux

TODO (11/2024): A revoir avec Proton, Steam ... Faire une page dédiée

TODO: Voir les jeux installés si bien, sinon supprimer

> Rien n'est installé ici par défaut

- [PlayOnLinux](http://www.playonlinux.com/fr/) (supporté par [Wine](Wine))

#### Programmation

> Rien n'est installé ici par défaut

TODO: Revoir cette section

|                                   |                                               |                                                                    |                                             |
| --------------------------------- | --------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------- |
| Nom                               | Ubuntu-fr                                     | Description                                                        | Installation [apturl](../system/Apt-url.md) |
| [Mono](../../dev/Mono.md)         |                                               | Implémentation libre de .NET avec comme éditeur MonoDevelop        | N/A                                         |
| [NetBeans](../../dev/NetBeans.md) | [netbeans](http://doc.ubuntu-fr.org/netbeans) | IDE de Sun axé Java mais aussi Python, C, C++, Ruby, XML, PHP, ... | N/A                                         |
| Gambas                            | [Gambas](http://doc.ubuntu-fr.org/Gambas)     | le presque Visual Basic libre                                      | [gambas3](apt://gambas3)                    |

Plus d'informations, voir la page [Développement](../../dev/README.md).

#### Son et Vidéo

TODO: Ajouter:

- Audacity
- pavucontrol (PulseAudio Volume Control)
- Sound Converter; soundconverter; Converts audio files into other formats
- Hypnotix (Watch TV)
- Mixxx
- Molotov
- Qobuz Downloader
- SimpleScreenRecorder
- (SoulSeek)
- [Soudjuicer](Soudjuicer) Rip & Encodage (tjs problèmes en VBR ?)
  - A tester aussi : [Grip](Grip)
- K3B


##### Audio

TODO: Review this list

|             |                                             |                                                                                            |                                             |
| ----------- | ------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------- |
| Nom         | Ubuntu-fr                                   | Description                                                                                | Installation [apturl](../system/Apt-url.md) |
| easyMP3Gain | [mp3gain](http://doc.ubuntu-fr.org/mp3gain) | Normalisation du volume des musiques dans un dossier ou fichier par fichier par replayGain | [easymp3gain-gtk](apt://easymp3gain-gtk)    |

TODO: Comparer Jamuz (perfs) avec <https://doc.ubuntu-fr.org/rhythmbox> (installé par défaut)

TODO: Faire un paquet deb pour JaMuz, puis faire un PPA ou mieux ajouter dans les repos ubuntu/linux mint/debian

TODO: Move to JaMuz

- Genre icons (for future use):
  - <http://www.iconarchive.com/show/music-genre-icons-by-sirubico.html>
  - <http://www.flickr.com/groups/itunesgenres/pool/>
  - <http://myssynen.deviantart.com/art/Music-genre-images-71751056>
  - <http://www.mede8erforum.com/index.php?topic=5472.0>
  - <http://www.iconeasy.com/iconset/music-genre-icons/>

##### Vidéo

TODO:  Voir aussi [Fusionner 2 fichiers avi avec mencoder](http://www.ubuntuhowtos.com/howtos/merge_avi_files_with_mencoder)

TODO:  Voir aussi: [Convertir MOV en Flash FLV](Convertir_MOV_en_Flash_FLV)

#### Administration

TODO: Ajouter:
- Back In Time ?
- Disks - gnome-disks
- htop
- Mission Center
- WoeUSB (Prepare Microsoft Windows installation USB with ease.)

TODO: /!\ Comment gérer rsync/grsync et autres cas de gui pour outil de ligne de commande

|                 |                                             |                            |                                             |
| --------------- | ------------------------------------------- | -------------------------- | ------------------------------------------- |
| Nom             | ubuntu-fr                                   | Description                | Installation [apturl](../system/Apt-url.md) |
| Gparted         | [gparted](http://doc.ubuntu-fr.org/gparted) | Partitionnement de disque. | [gparted](apt://gparted)                    |
| [grsync](rsync) | Synchronisation de fichiers.                | [grsync](apt://grsync)     |                                             |
| [VirtualBox](http://doc.ubuntu-fr.org/virtualbox)   | Solution de virtualisation de systèmes d'exploitation. [Images toutes prêtes](http://virtualboxes.org/images/) | Voir [VirtualBox](http://doc.ubuntu-fr.org/virtualbox)   |


#### Préférences

TODO: Ajouter:
- Guake



### A REVOIR

--------------------------------------------------------------------
TODO !!!!!!!!!!!!!!!!!!!!!! Ce qui suit est à archiver ou a revoir
--------------------------------------------------------------------


|                                                                                   |                                                                                          |                                                                      |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Nom                                                                               | Description                                                                              | Installation [apturl](../system/Apt-url.md)                          |
| [Compiz Fusion](http://doc.ubuntu-fr.org/compiz_fusion) (simple)                  | Configuration des effets de bureau. Recommandé.                                          | [simple-ccsm](apt://simple-ccsm)                                     |
| [Compiz Fusion](http://doc.ubuntu-fr.org/compiz_fusion) (avancé)                  | Configuration avancée des effets de bureau.                                              | [compizconfig-settings-manager](apt://compizconfig-settings-manager) |
| [nautilus-actions](http://doc.ubuntu-fr.org/nautilus-actions)                     | Configuration des actions de Nautilus (gestionnaire fichiers)                            | [nautilus-actions](apt://nautilus-actions)                           |
| [nautilus-scripts](http://doc.ubuntu-fr.org/nautilus_scripts)                     | Scripts pour Nautilus (menu contextuel).                                                 |                                                                      |
| [Nautilus Cover Thumbnailer](http://software.flogisoft.com/cover-thumbnailer/fr/) | Afficher les pochettes des albums de musique dans nautilus, prévisualiser les images ... | Via PPA. Refer to link.                                              |

> Compiz ne marche pas avec Cinnamon (apparement) mais il ya des extensions comme https://github.com/linuxmint/cinnamon-spices-extensions/tree/master/compiz-windows-effect@hermes83.github.com


[Comparaison avec nautilus-scripts](http://www.commentcamarche.net/faq/6357-editer-le-menu-contextuel-de-nautilus-navigateur-de-fichiers)
[Bibliothèque de scripts](http://g-scripts.sourceforge.net/) nautilus

#### Outils système

|                                                     |                                                                                                                |                                                          |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Nom                                                 | Description                                                                                                    | Installation [apturl](../system/Apt-url.md)              |
| [ForemostGUI](http://doc.ubuntu-fr.org/foremostgui) | IHM pour foremost, logiciel de récupération de données                                                         | Voir [ForemostGUI](http://doc.ubuntu-fr.org/foremostgui) |


Les suivants sont à répartir dans les menus appropriés :

|                                                             |                                                            |                                                    |
| ----------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------- |
| Nom                                                         | Description                                                | Installation [apturl](../system/Apt-url.md)        |
| [Google Earth](Google_Earth)                                | La Terre vue du ciel                                       | N/A                                                |
| [Sunclock](http://www.arvernes.com/wiki/index.php/Sunclock) | Carte avec zones ensoleillées                              | N/A                                                |
| [Wine](Wine)                                                | Windows Emulation                                          |                                                    |
| Gwhere                                                      | Catalogueur de CDs/DVDs                                    |                                                    |
| OpenOffice                                                  | Office (tableur, traitement de texte, présentations, BDD)  | inclus par défaut dans [Ubuntu](linux/dist/Ubuntu) |
| Antivirus                                                   | Complètement inutile                                       | N/A                                                |
| kFileReplace                                                | Changer un texte par un autre dans des fichiers (a tester) |                                                    |



TODO Tester et intégrer ce qui suit (de Chat GPT):

##### Outils de Sauvegarde Versionnée pour Fichiers sous Linux

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

#### Divers, sans IHM

Les programmes suivants n'ont pas d'interface graphique, mais sont quand
même bien pratiques:

|                                                        |                                         |                                                                                                     |                                             |
| ------------------------------------------------------ | --------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Nom                                                    | Ubuntu-fr                               | Description                                                                                         | Installation [apturl](../system/Apt-url.md) |
| [convmv](Convmv)                                       |                                         | Conversion de caractères (noms de fichiers)                                                         | [convmv](apt://convmv)                      |
| [Disques_Réseau#mount.cifs](Disques_Réseau#mount.cifs) |                                         | Pour monter des dossiers partagés Windows ou Samba                                                  | [smbfs](apt://smbfs)                        |
| [fcron](Fcron)                                         | [fcron](http://doc.ubuntu-fr.org/fcron) | FCron permet de pallier les défauts de Cron et d'Anacron.                                           | [fcron](apt://fcron)                        |
| RAR (archive)                                          | [rar](http://doc.ubuntu-fr.org/rar)     | RAR est un format d'archive (un peu comme ZIP), c'est aussi le nom de l'application pour les gérer. | Voir site Ubuntu                            |

> [RAR avec mot de passe](http://forum.ubuntu-fr.org/viewtopic.php?id=83892)

Pimp your terminal:

- [ZSH](https://doc.ubuntu-fr.org/zsh)
- [Oh My Zsh](https://ohmyz.sh/)
  - [powerlevel10k](https://github.com/romkatv/powerlevel10k#oh-my-zsh)
    theme
  - Useful plugins : [Shell sous stéroides](https://www.tronyxworld.be/2020/zsh_omz_p10k/)
    - kubectl
    - kube.ps1


TODO: Inclure les applis par défaut dans Mint 21.3 et 22


------------------------------------------------------------------------

Retour à l'[Accueil](README)
