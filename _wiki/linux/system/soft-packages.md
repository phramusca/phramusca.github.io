---
layout: content
title: Système de gestion de paquets
---

# {{ page.title }}

- [APT](https://salsa.debian.org/apt-team/apt) ([ubuntu-fr](https://doc.ubuntu-fr.org/apt))
  - Paquets “classiques” pour les [distributions Linux basées sur Debian](../../#distributions-basées-sur-debian-linux-mint-ubuntu)
  - Installation facile par [apt-url](http://doc.ubuntu-fr.org/apturl), ex [apt://gimp](apt://gimp)
  - Ligne de commande: `sudo apt install <pkg>`
- [Flatpak](https://flatpak.org/) ([ubuntu-fr](https://doc.ubuntu-fr.org/flatpak))
  - Apps (surtout GUI) via [flathub.org](https://flathub.org) principalement.
  - Disponible nativement dans le store de Linux Mint.
  - Indisponible dans le store de Ubuntu, à [installer/configurer](https://flathub.org/fr/setup/Ubuntu).
  - Installation facile par URL, ex [flathub://com.usebruno.Bruno](flatpak+https://dl.flathub.org/repo/appstream/com.usebruno.Bruno). Necessite un [handler](https://github.com/phramusca/flatpak-https-handler) pour Linux Mint.
  - Ligne de commande: `flatpak install flathub <appID>`
- [AppImage](https://appimage.org/) ([ubuntu-fr](https://doc.ubuntu-fr.org/appimage))
  - Un seul fichier exécutable, pratique pour tester une version.
  - Pas d'installation.
  - Ligne de commande: `chmod +x fichier.AppImage && ./fichier.AppImage`
- [Snap](https://snapcraft.io/) ([ubuntu-fr](https://doc.ubuntu-fr.org/flatpak))
  - Format Ubuntu/Canonical avec Snap Store **propriétaire**. **Non recommandé !**
  - Installation facile par URL: [snap://bruno](snap://bruno)
  - Ligne de commande: `sudo snap install <pkg>`
  - Par défaut sous Ubuntu (snapd et snap-store préinstallé).
  - [Désactivé par défaut](https://linuxmint-user-guide.readthedocs.io/en/latest/snap.html) sous Linux Mint (snapd verrouillé; nécessite déverrouillage + installation + ``snap install snap-store`` pour liens ``snap://``).
- Code source
  - Non recommandé, sauf si le programme n'est pas disponible autrement.
  - [Tutoriel compilation](http://doc.ubuntu-fr.org/tutoriel/compilation)
