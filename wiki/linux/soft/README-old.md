# Programmes

## Ma Sélection

TODO: <https://doc.ubuntu-fr.org/ventoy>

TODO: Ajouter les programmes / nettoyer le répertoire local Installs

### Applications

#### Accessoires

TODO: Ajouter:

- Flatseal (/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=com.github.tchx84)
- rpi-imager (Raspberry Pi Imager)
- KeePass2
- Solaar
- Spectacle (Capture d'écran avec apparement plus d'options que "Capture d'écran")
- VNote (Prise de notes en markdown)

#### Autre

TODO: Faire le tri entre Wayland (à revoir aussi) et le reste

#### Bureautique

TODO: Ajouter:

- Calibre
- gLabels
- PDFsamBasic

#### Education

TODO: Ajouter:

- Atelier Linotte
- GCompris
- Tux Math
- [Jeux educatifs](https://doc.ubuntu-fr.org/educatif)

#### Graphisme

TODO: Ajouter:

- Dia
- digiKam
- gscan2pdf
- Sweet Home 3D
- XSane (=> Integrer page locale sur imprimante lexmark)

Installés par défaut:

- Dessin
- Numérisuer de documents
- Pix

#### Internet

TODO Rajouter:

- 4kyoutubetomp3
- MEGAsync
- Remmina
- RClone Browser
- TigerVNC (voir page sur VNC)
- Gnome Web (avec WebKitGTK)
- Wireshark

|                                                     |                                             |                                             |
| --------------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| Nom                                                 | Description                                 | Installation [apturl](../system/Apt-url.md) |
| gFTP                                                | Client FTP (File Transfer Protocol)         | [gftp](apt://gftp)                          |
| [JDownloader](http://doc.ubuntu-fr.org/jdownloader) | Gestionnaire de téléchargement de fichiers. | N/A                                         |

TODO: Faire section FTP, avec aussi FileZilla et lftp (script. et gui ?)

|      |                                     |                                             |
| ---- | ----------------------------------- | ------------------------------------------- |
| Nom  | Description                         | Installation [apturl](../system/Apt-url.md) |
| gFTP | Client FTP (File Transfer Protocol) | [gftp](apt://gftp)                          |

TODO: Revoir ou archiver ceux la:

|            |                                                                                                |                                                    |
| ---------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Nom        | Description                                                                                    | Installation [apturl](../system/Apt-url.md)        |
| [VNC](VNC) | Remote Desktop (Pour prendre le contrôle d'un PC à distance)                                   |                                                    |
| Evolution  | équivalent ou presque d'Outlook                                                                | inclus par défaut dans [Ubuntu](linux/dist/Ubuntu) |
| Empathy    | Messagerie instantanée compatible avec MSN (Windows Live), Jabber, Google Talk, AIM, yahoo,... | inclus par défaut dans [Ubuntu](linux/dist/Ubuntu) |

#### Jeux

TODO (11/2024): A revoir avec Proton, Steam ... Faire une page dédiée

TODO: Voir les jeux installés si bien, sinon supprimer

> Rien n'est installé ici par défaut

- [PlayOnLinux](http://www.playonlinux.com/fr/) (supporté par [Wine](Wine))

#### Programmation

TODO: Revoir cette section

> Rien n'est installé ici par défaut

Plus d'informations, voir la page [Développement](../../dev/README.md).

|                                   |                                                 |                                                                    |                                             |
| --------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------- |
| Nom                               | Ubuntu-fr                                       | Description                                                        | Installation [apturl](../system/Apt-url.md) |
| [Meld](Meld)                      |                                                 | Comparaison de fichiers / répertoires.                             | [meld](apt://meld)                          |
| sqlitebrowser                     | [sqlitebrowser.org](https://sqlitebrowser.org/) | Administration de bases Sqlite                                     | [sqlitebrowser](apt://sqlitebrowser)        |
| [Mono](../../dev/Mono.md)         |                                                 | Implémentation libre de .NET avec comme éditeur MonoDevelop        | N/A                                         |
| [NetBeans](../../dev/NetBeans.md) | [netbeans](http://doc.ubuntu-fr.org/netbeans)   | IDE de Sun axé Java mais aussi Python, C, C++, Ruby, XML, PHP, ... | N/A                                         |
| Gambas                            | [Gambas](http://doc.ubuntu-fr.org/Gambas)       | le presque Visual Basic libre                                      | [gambas3](apt://gambas3)                    |

#### Son et Vidéo

TODO : !!!!!!!!!!!!!!!! REPRENDRE ICI (en sync avec page archive)

##### Audio

TODO: Review this list

|                    |                                             |                                                                                                                                             |                                             |
| ------------------ | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Nom                | Ubuntu-fr                                   | Description                                                                                                                                 | Installation [apturl](../system/Apt-url.md) |
| [EasyTag](EasyTag) | [easytag](http://doc.ubuntu-fr.org/easytag) | Éditeur de Tags Id3                                                                                                                         | [easytag](apt://easytag)                    |
| easyMP3Gain        | [mp3gain](http://doc.ubuntu-fr.org/mp3gain) | Normalisation du volume des musiques dans un dossier ou fichier par fichier par replayGain                                                  | [easymp3gain-gtk](apt://easymp3gain-gtk)    |
| [mp3Splt](Mp3Splt) |                                             | Découper des MP3s                                                                                                                           | [mp3splt-gtk](apt://mp3splt-gtk)            |
| [RipperX](RipperX) |                                             | Rip & Encodage MP3 (ou [Soudjuicer](Soudjuicer) par défaut dans Ubuntu, mais avec des problèmes en VBR) *A tester aussi : [Grip](Grip) ...* | [ripperx](apt://ripperx)                    |

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

|                                                      |                                                                                                                                                                                  |                                                                                   |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Nom                                                  | Description                                                                                                                                                                      | Installation [apturl](../system/Apt-url.md)                                       |
| [vlc](http://doc.ubuntu-fr.org/vlc)                  | Lecteur video. Voir aussi totem, kaffeine,...                                                                                                                                    | [vlc](apt://vlc)                                                                  |
| [winff](http://doc.ubuntu-fr.org/winff)              | WinFF est une interface graphique à FFmpeg très simple d'utilisation et personnalisable. Voir aussi: [Convertir MOV en Flash FLV](Convertir_MOV_en_Flash_FLV)                    | [winff](apt://winff) + [codecs](http://ubuntuforums.org/showthread.php?t=1117283) |
| [avidemux](http://doc.ubuntu-fr.org/avidemux)        | Editeur vidéo, considéré comme l'équivalent de VirtualDub. Voir aussi [Fusionner 2 fichiers avi avec mencoder](http://www.ubuntuhowtos.com/howtos/merge_avi_files_with_mencoder) | [avidemux](apt://avidemux)                                                        |
| [Arista Transcoder](http://doc.ubuntu-fr.org/arista) | logiciel de conversion vidéo                                                                                                                                                     | [arista](apt://arista)                                                            |
|                                                      |                                                                                                                                                                                  |                                                                                   |
| [QuickTime](QuickTime)                               | QuickTime pour Linux                                                                                                                                                             |                                                                                   |
| DVDShrink                                            | xDVDShrink - a tester                                                                                                                                                            |                                                                                   |
| [ManDVD](http://doc.ubuntu-fr.org/mandvd)            | Création simplifiée de DVD-vidéos, a tester                                                                                                                                      |                                                                                   |

#### Outils système

|                                                     |                                                                                                                |                                                          |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Nom                                                 | Description                                                                                                    | Installation [apturl](../system/Apt-url.md)              |
| yakuake                                             | permet de lancer un shell (Terminal) "rétractible" en pressant F12 - très pratique                             | [yakuake](apt://yakuake)                                 |
| [rsync](soft/rsync)                                 | Synchronisation de fichiers.                                                                                   | [grsync](apt://grsync)                                   |
| [rclone](soft/rclone)                               | Manipuler les fichiers sur des stockages cloud.                                                                | [rclone-browser](apt://rclone-browser)                   |
| [ForemostGUI](http://doc.ubuntu-fr.org/foremostgui) | IHM pour foremost, logiciel de récupération de données                                                         | Voir [ForemostGUI](http://doc.ubuntu-fr.org/foremostgui) |
| [VirtualBox](http://doc.ubuntu-fr.org/virtualbox)   | Solution de virtualisation de systèmes d'exploitation. [Images toutes prêtes](http://virtualboxes.org/images/) | Voir [VirtualBox](http://doc.ubuntu-fr.org/virtualbox)   |


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

|                                                        |                                         |                                                                                                                                                                                |                                             |
| ------------------------------------------------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| Nom                                                    | Ubuntu-fr                               | Description                                                                                                                                                                    | Installation [apturl](../system/Apt-url.md) |
| [convmv](Convmv)                                       |                                         | Conversion de caractères (noms de fichiers)                                                                                                                                    | [convmv](apt://convmv)                      |
| [Disques_Réseau#mount.cifs](Disques_Réseau#mount.cifs) |                                         | Pour monter des dossiers partagés Windows ou Samba                                                                                                                             | [smbfs](apt://smbfs)                        |
| [fcron](Fcron)                                         | [fcron](http://doc.ubuntu-fr.org/fcron) | FCron permet de pallier les défauts de Cron et d'Anacron.                                                                                                                      | [fcron](apt://fcron)                        |
| RAR (archive)                                          | [rar](http://doc.ubuntu-fr.org/rar)     | RAR est un format d'archive (un peu comme ZIP), c'est aussi le nom de l'application pour les gérer. [RAR avec mot de passe](http://forum.ubuntu-fr.org/viewtopic.php?id=83892) | Voir site Ubuntu                            |

Les suivants sont à répartir dans les menus appropriés :

|                                                             |                                                            |                                                    |
| ----------------------------------------------------------- | ---------------------------------------------------------- | -------------------------------------------------- |
| Nom                                                         | Description                                                | Installation [apturl](../system/Apt-url.md)        |
| [BOINC](BOINC)                                              | Calcul partagé                                             | N/A                                                |
| [Google Earth](Google_Earth)                                | La Terre vue du ciel                                       | N/A                                                |
| [Sunclock](http://www.arvernes.com/wiki/index.php/Sunclock) | Carte avec zones ensoleillées                              | N/A                                                |
| K3B                                                         | Gravure CD/DVD                                             |                                                    |
| [Wine](Wine)                                                | Windows Emulation                                          |                                                    |
| Gwhere                                                      | Catalogueur de CDs/DVDs                                    |                                                    |
| OpenOffice                                                  | Office (tableur, traitement de texte, présentations, BDD)  | inclus par défaut dans [Ubuntu](linux/dist/Ubuntu) |
| Antivirus                                                   | Complètement inutile                                       | N/A                                                |
| kFileReplace                                                | Changer un texte par un autre dans des fichiers (a tester) |                                                    |
| [Virtual Box](http://doc.ubuntu-fr.org/virtualbox)          | Virtualisation                                             |                                                    |

### Système

Ici sont regroupées tout ce qui concerne la configuration du système.

#### Préférences

|                                                                                   |                                                                                                                                                                                                                                                 |                                                                      |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Nom                                                                               | Description                                                                                                                                                                                                                                     | Installation [apturl](../system/Apt-url.md)                          |
| [Compiz Fusion](http://doc.ubuntu-fr.org/compiz_fusion) (simple)                  | Configuration des effets de bureau. Recommandé.                                                                                                                                                                                                 | [simple-ccsm](apt://simple-ccsm)                                     |
| [Compiz Fusion](http://doc.ubuntu-fr.org/compiz_fusion) (avancé)                  | Configuration avancée des effets de bureau.                                                                                                                                                                                                     | [compizconfig-settings-manager](apt://compizconfig-settings-manager) |
| [nautilus-actions](http://doc.ubuntu-fr.org/nautilus-actions)                     | Configuration des actions de Nautilus (gestionnaire fichiers) [Comparaison avec nautilus-scripts](http://www.commentcamarche.net/faq/6357-editer-le-menu-contextuel-de-nautilus-navigateur-de-fichiers)                                         | [nautilus-actions](apt://nautilus-actions)                           |
| [nautilus-scripts](http://doc.ubuntu-fr.org/nautilus_scripts)                     | Scripts pour Nautilus (menu contextuel). [Bibliothèque de scripts](http://g-scripts.sourceforge.net/) [Comparaison avec nautilus-actions](http://www.commentcamarche.net/faq/6357-editer-le-menu-contextuel-de-nautilus-navigateur-de-fichiers) |                                                                      |
| Applications au démarrage                                                         | Configuration des programmes à lancer au démarrage de [Ubuntu](linux/dist/Ubuntu)                                                                                                                                                               | par défaut dans [Ubuntu](linux/dist/Ubuntu)                          |
| [Nautilus Cover Thumbnailer](http://software.flogisoft.com/cover-thumbnailer/fr/) | Afficher les pochettes des albums de musique dans nautilus, prévisualiser les images contenues dans un dossier et plus encore.                                                                                                                  | Via PPA. Refer to link.                                              |

#### Administration

|              |                                                       |                                                                                    |                                                                 |
| ------------ | ----------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Nom          | ubuntu-fr                                             | Description                                                                        | Installation [apturl](../system/Apt-url.md)                     |
| Gparted      | [gparted](http://doc.ubuntu-fr.org/gparted)           | Partitionnement de disque.                                                         | [gparted](apt://gparted)                                        |
| Disk-Manager | [disk-manager](http://doc.ubuntu-fr.org/disk-manager) | Gestionnaire de disques. Voir [Disques Locaux](Disques_Locaux)                     | N/A. Voir [disk-manager](http://doc.ubuntu-fr.org/disk-manager) |
| Gufw         | [gufw](http://doc.ubuntu-fr.org/gufw)                 | Interface graphique du pare-feu UFW, celui par défaut dans Ubuntu (10.10 au moins) | [gufw](apt://gufw)                                              |

Pimp your terminal:

- [ZSH](https://doc.ubuntu-fr.org/zsh)
- [Oh My Zsh](https://ohmyz.sh/)
  - [powerlevel10k](https://github.com/romkatv/powerlevel10k#oh-my-zsh)
    theme
  - Useful plugins : [Shell sous
    stéroides](https://www.tronyxworld.be/2020/zsh_omz_p10k/)
    - kubectl
    - kube.ps1

### Tableaux de bord

Par défaut, il y a 2 tableaux de bord installés dans
[Ubuntu](linux/dist/Ubuntu):

- 1 en haut comprenant:
  - à gauche La barre de menus (Applications, Raccourcis et Système)
    dont le contenu est décrit dans les sections ci-dessus
  - à droite:
    - une Applet de notification (son, messageries)
    - une Horloge
    - une Applet de notification de session (Un endroit pour modifier
      votre état de présence, changer d'utilisateur ou fermer votre
      session.)
- 1 en bas comprenant:
  - à gauche:
    - Bouton d'affichage du bureau
    - Liste des fenêtres
  - à droite:
    - Sélecteur d'espaces de travail
    - Applet Corbeille

Il est possible de rajouter d'autres tableaux de bord (click-droit sur
un existant et "Nouveau tableau de bord") et de les supprimer
(click-droit sur le tableau de bord et "Supprimer ce tableau de bord").

Il est aussi possible d'ajouter (click-droit sur un tableau de bord et
"Ajouter au tableau de bord"), de déplacer ou de supprimer (click-droit
sur un élément et "Déplacer" ou "Enlever du tableau de bord") les
éléments des tableaux de bord.

Voici quelques tableaux de bord:

|                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                  |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Nom                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                      | Installation [apturl](../system/Apt-url.md)      |
| [File Browser Applet](http://doc.ubuntu-fr.org/file-browser-applet) | Il permet de parcourir le contenu de votre ordinateur et d'ouvrir des fichiers sans avoir à utiliser de navigateur de fichiers. Son but n'est pas de remplacer un véritable gestionnaire de fichiers tel que Nautilus ; parfois vous voulez juste ouvrir un document sans avoir à ouvrir un dossier, le parcourir, ouvrir le document et refermer le dossier. Cet applet vous épargne simplement quelques clics. | [file-browser-applet](apt://file-browser-applet) |

------------------------------------------------------------------------

Retour à l'[Accueil](README)
