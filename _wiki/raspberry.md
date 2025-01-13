---
layout: default
---

# Raspberry

## Mise à jour

Un petit script pour faire la maintenance du système (mises à jour et nettoyage des paquets inutilisés)

- Créer un script `update.sh`

```bash
#!/bin/bash

sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo apt autoclean
sudo apt clean packages

echo "-------------------- Press enter to exit "--------------------
read case;
```

- Créer un ficher `Update & clean.desktop`

```ini
[Desktop Entry]
Type=Application
Name=Update & clean
Exec=lxterminal -e /home/raph/Documents/Update.sh
Icon=/usr/share/icons/Adwaita/48x48/legacy/software-update-available.png
Terminal=false
```

TODO: Automatiser avec cron

TODO: Comment rafraichir l'icone de mise à jour ??