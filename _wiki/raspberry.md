---
layout: content
---

# Raspberry

## Installation

- Installer [rpi-imager](apt://rpi-imager)
  - Documentation: https://www.raspberrypi.com/documentation/

- TODO: Configurer un certificat pour connexion ssh

- TODO: Booster le pi: https://korben.info/raspberry-pi-5-optimisation-performances-sdram.html

TODO: Bouger ça dans Linux:

- [Pimp My Terminal](https://stackabuse.com/pimp-my-terminal-an-introduction-to-oh-my-zsh/)
  
- [ZSH](https://doc.ubuntu-fr.org/zsh)
- [Oh My Zsh](https://ohmyz.sh/)
  - [powerlevel10k](https://github.com/romkatv/powerlevel10k#oh-my-zsh)

  ```shell
  sudo apt install zsh
  ```
  
  ```shell
  chsh -s $(which zsh)
  ```

  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

Install powerlevel10k (TODO: trouver alternative, plus maintenu)

  https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#oh-my-zsh

Installer les polices pour powerlevel10k et les configurer dans les différents terminaux voulus

  https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#meslo-nerd-font-patched-for-powerlevel10k

  ➜  ~ mkdir ~/.local/share/fonts/
➜  ~ cp Téléchargements/MesloLGS\ NF\ Bold\ Italic.ttf ~/.local/share/fonts/
➜  ~ cp Téléchargements/MesloLGS\ NF\ Bold.ttf ~/.local/share/fonts/ 
➜  ~ cp Téléchargements/MesloLGS\ NF\ Italic.ttf ~/.local/share/fonts/ 
➜  ~ cp Téléchargements/MesloLGS\ NF\ Regular.ttf ~/.local/share/fonts/ 
➜  ~ fc-cache -fv
~/.local/share/fonts/

➜  ~ fc-list | grep "Meslo"           

~/.local/share/fonts/MesloLGS NF Bold.ttf: MesloLGS NF:style=Bold
~/.local/share/fonts/MesloLGS NF Italic.ttf: MesloLGS NF:style=Italic
~/.local/share/fonts/MesloLGS NF Bold Italic.ttf: MesloLGS NF:style=Bold Italic
~/.local/share/fonts/MesloLGS NF Regular.ttf: MesloLGS NF:style=Regular


Installer powerlevel10k

  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"

    nano ~/.zshrc

  Open ~/.zshrc, find the line that sets ZSH_THEME, and change its value to "powerlevel10k/powerlevel10k".

  Open a new terminal session, and follow the p10k configuration wizard.

Install unofficial

- https://github.com/zsh-users/zsh-syntax-highlighting
  - https://stackabuse.com/pimp-my-terminal-an-introduction-to-oh-my-zsh/
   
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

- https://github.com/zsh-users/zsh-autosuggestions
  - https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh

  git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions


- Install official Oh My Zsh plugins from https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins

  - Git - in essence, this plugin is a bundle of predefined aliases that helps you speed up the usage of Git in a terminal. Instead of git status, you can write gst, instead of git add, you can write ga, etc. Take a look at the list of all aliases to get a feel for the shortcuts.
  - sudo - a very useful plugin that enables you to add sudo as the prefix to the current or previous command, just by pressing ESC two times.
  - z - this plugin aims to boost your productivity by enabling you to navigate through directories with as few clicks as possible. It keeps track of your most visited directories and enables you to navigate to them by typing just a few characters from the desired directory path.
  - kubectl ?
  - kube.ps1 ?
  - les autre s?


Activer les plugins en éditant `nano ~/.zshrc`

    plugins = (git z sudo zsh-syntax-highlighting zsh-autosuggestions)

Relancer le terminal pour profiter des plugins.

> Note: avec lxterminal, il faut redémarrer le raspberry pour qu'il démarre avec zsh par défaut.

TODO: Voir, tester et documenter partie "Creating Aliases" de https://stackabuse.com/pimp-my-terminal-an-introduction-to-oh-my-zsh/

- [Installer Docker](/wiki/docker#installation)
- [Configurer docker](/wiki/docker#monter-un-disque-externe-avant-de-lancer-docker) pour monter les disques externes avant de lancer les images
- Installer [Portainer](/wiki/docker#portainer-ce)

## Mise à jour

Un petit script pour faire la maintenance du système (mises à jour et nettoyage des paquets inutilisés)

- Créer un script `~/Documents/scripts/Update.sh`

```bash
#!/bin/bash

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get autoremove -y
sudo apt-get autoclean
sudo apt-get clean

echo "-------------------- Press enter to exit "--------------------
read case;
```

- Créer un ficher `Update & clean.desktop`

```ini
[Desktop Entry]
Type=Application
Name=Update & clean
Exec=lxterminal -e ~/Documents/Update.sh
Icon=/usr/share/icons/AdwaitaLegacy/48x48/legacy/software-update-available.png
Terminal=false
```

### Automatiser la mise à jour

Ouvrir la configuration de crontab avec cette commande:

```bash
crontab -e
```

En fin de fichier, ajouter la ligne suivante:

```bash
0 4 * * * /bin/bash ~/Documents/scripts/Update.sh >> ~/Documents/scripts/Update.log 2>&1
```

Ceci va lancer le script tous les jours à 4H du matin.

Pour info, les options de base pour une ligne crontab sont :

```text
┌───────── minute (0 - 59)
│ ┌─────── heure (0 - 23)
│ │ ┌───── jour du mois (1 - 31)
│ │ │ ┌─── mois (1 - 12)
│ │ │ │ ┌─ jour de la semaine (0 - 7) (dimanche = 0 ou 7)
│ │ │ │ │
* * * * * commande à exécuter
```

Pour plus d’options:

```bash
man 5 crontab
```

#### Logs rotatifs

Pour éviter de saturer l'espace disque, il convient de mettre en place des logs rotatifs:

Créer un fichier de configuration logrotate:

```bash
sudo mousepad /etc/logrotate.d/Update
```

Avec le contenu suivant:

```text
~/Documents/scripts/Update.log {
    daily
    rotate 30
    missingok
    notifempty
    compress
    delaycompress
    copytruncate
}
```

- `daily`: Tourner tous les jours
- `rotate 30`: Garde 30 logs (≈30 jours)
- `missingok` : Si le fichier de log n’existe pas, logrotate ne génère pas d’erreur (il « ignore » le fichier manquant).
- `notifempty` : Si le fichier de log est vide, logrotate ne le fait pas tourner (pas de rotation pour un fichier vide).
- `compress`: Les vieux logs sont compréssés (gzip)
- `copytruncate`: Pour les scripts qui gardent le fichier de log ouvert

Pour forcer la rotation et ainsi la tester: `sudo logrotate -f /etc/logrotate.d/Update`

#### Rafraichir l'icône de mise à jour

TODO: Comment rafraichir l'icone de mise à jour ??

## Hotspot WEP pour Nintendo DS

La Nintendo DS ne supporte que les clefs WEP. La freebox ne permet plus de configurer le WiFi avec ce format.

Il me faut donc créer un hotspot. Heureusement mon Raspberry a le Wifi disponible puisque connecté en filaire.

### 📌 Notes

- **WEP est obsolète et non sécurisé** - À utiliser uniquement pour la DS Lite

### Prérequis

```bash
sudo apt install hostapd dnsmasq iproute2 iw
````

### Script du hotspot

Utilisation:

```bash
Usage: ./HotspotWEP.sh {start|stop|status|restart}

Commandes:
  start   - Démarrer le hotspot WEP
  stop    - Arrêter le hotspot
  status  - Afficher l'état du hotspot
  restart - Redémarrer le hotspot
```

Le script: [HotspotWEP.sh](raspberry/HotspotWEP.sh)
