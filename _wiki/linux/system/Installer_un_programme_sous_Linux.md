---
layout: content
---

# Installer un programme sous Linux

Il existe plusieurs façons d'installer des programmes sous linux.

|                                                                                           | Store                                                   | Description                                                                                                                 | Installation facile par URL                                                                    | Ligne de commande                                 | [Ubuntu](../dist/Ubuntu)                         | [Linux Mint](../dist/Mint)                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [APT](https://salsa.debian.org/apt-team/apt) ([ubuntu-fr](https://doc.ubuntu-fr.org/apt)) | Selon OS.                                               | Paquets “classiques” de la distro (intégration système, libs/CLI/services).                                                 | [apt-url](../system/apturl), ex [apt://gimp](apt://gimp)                                       | `sudo apt install <pkg>`                          | ✅ Par défaut.                                   | ✅ Par défaut.                                                                                                                                                                                               |
| [AppImage](https://appimage.org/) ([ubuntu-fr](https://doc.ubuntu-fr.org/appimage))       | N/A                                                     | Un seul fichier exécutable, pas d’installation, pratique pour tester/épingler une version. Pas de sandbox par défaut.       | N/A. Pas d'installation.                                                                       | `chmod +x fichier.AppImage && ./fichier.AppImage` | ✅ Possible (téléchargement + `chmod +x`).       | ✅ Possible (téléchargement + `chmod +x`).                                                                                                                                                                   |
| [Flatpak](https://flatpak.org/) ([ubuntu-fr](https://doc.ubuntu-fr.org/flatpak))          | [Flathub](https://flathub.org) ou autres.               | Apps (surtout GUI) via Flathub, sandbox (portals/bubblewrap), bon cross-distro. Pas de `flatpak://` (plutôt `.flatpakref`). | [flathub.org](https://flathub.org), ex [Bruno](https://flathub.org/en/apps/com.usebruno.Bruno) | `flatpak install flathub <appID>`                 | ⚠️ Pas par défaut (à installer/configurer).    | ✅ Possible (souvent via la logithèque/Flathub).                                                                                                                                                             |
| [Snap](https://snapcraft.io/) ([ubuntu-fr](https://doc.ubuntu-fr.org/flatpak))            | [Snap Store](https://snapcraft.io/store) exclusivement. | ⚠️ Format Ubuntu/Canonical avec Snap Store **propriétaire**. **Non recommandé !**                                         | [snap://bruno](snap://bruno)                                                                   | `sudo snap install <pkg>`                         | ✅ Par défaut (snapd et snap-store préinstallé). | ❌ [Désactivé par défaut](https://linuxmint-user-guide.readthedocs.io/en/latest/snap.html) (snapd verrouillé; nécessite déverrouillage + installation + ``snap install snap-store`` pour liens ``snap://``). |

[flatpak+https://dl.flathub.org/repo/appstream/dev.tchx84.Gameeky.flatpakref](flatpak+https://dl.flathub.org/repo/appstream/dev.tchx84.Gameeky.flatpakref)

[https://flathub.org/fr/apps/dev.tchx84.Gameeky/install](https://flathub.org/fr/apps/dev.tchx84.Gameeky/install)

[https://flathub.org/apps/dev.tchx84.Gameeky/flatpakhttps](https://flathub.org/apps/dev.tchx84.Gameeky/flatpakhttps)

> Flatpak pour Ubuntu: https://flathub.org/fr/setup/Ubuntu car si y'a bien un handler sous Ubuntu pour flatpak+https, ça ouvre une popup disant "Aucune application disponible" car les fichiers .flatpakref ne sont associés à aucun type d'application.


## Magasins d'applications

[Linux Mint](../dist/Mint) comme [Ubuntu](../dist/Ubuntu) et d'autres distributions [Linux](../) ont une logithèque, facilement disponible depuis le menu principal.

Ceci est la méthode à privilégier dans tous les cas, pour plus de facilité, de sécurité et de compatibilité.

## Installer un paquet

### Distributions basées sur Debian (Linux Mint, Ubuntu,...)

Les [distributions Linux basées sur Debian](../#distributions-basées-sur-debian-linux-mint-ubuntu), comme [Linux Mint](../dist/Mint) ou [Ubuntu](../dist/Ubuntu), ainsi que Debian bien sûr, utilisent le format de paquet `deb`, donc les [programmes](../soft/) fonctionnent sur les deux.

#### Installer un paquet .deb

Si le paquet n'est pas disponible dans les logithèques, il est parfois disponible soit:

- sous forme de fichier `.deb` à télécharger. Il suffit de l'ouvrir pour l'installer.
- dans un dépôt alternatif et généralement le site vous indiquera les commandes à effectuer.

##### Paquet

Les paquets ont étés conçus pour permettre d'éviter la compilation des sources ainsi que pour la gestion des dépendances entre les différents [programmes](../soft/) (beaucoup de [programmes](../soft/) sous [Linux](../) sont dépendants les uns des autres).

Ils peuvent être gérés avec le gestionnaire graphique [Synaptic](apt://synaptic) ou en ligne de commande avec [apt](https://fr.wikipedia.org/wiki/Advanced_Packaging_Tool).

Pour plus d'info, voir [wikipedia](http://fr.wikipedia.org/wiki/Paquet_%28logiciel%29).

##### Dépôt

Un dépôt (ou repository en anglais) est un serveur qui contient les paquets nécessaires pour installer des [programmes](../soft/) sous [Linux](../).

Pour plus d'info, voir [doc.ubuntu-fr.org](<http://doc.ubuntu-fr.org/applications/apt/depots>)

### Autres distributions

Référez vous aux internets, je ne connais que deb pour les distributions de type Debian.

## En compilant les sources

Ceci est la manière originelle d'installer un programme sous [Linux](../), mais est à réserver aux utilisateurs avertis
!!! Dans tous les cas, mieux vaut privilégier l'utilisation de paquets !

Dans la plupart des cas, cela se révèle relativement simple, mais au moindre petit problème, cela peux vite devenir galère.

Perso, ça fait des années que je n'ai pas eu besoin de compiler une application !

Si vous insistez: [Tutoriel compilation](http://doc.ubuntu-fr.org/tutoriel/compilation) sur doc.ubuntu-fr.org
