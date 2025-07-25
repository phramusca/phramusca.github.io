---
layout: default
---

# Raspberry

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
Icon=/usr/share/icons/Adwaita/48x48/legacy/software-update-available.png
Terminal=false
```

### Automatiser la mise à jour

Ouvrir la configuration de crontab avec cette commande:

`crontab -e`

En fin de fichier, ajouter la ligne suivante:

`0 4 * * * /bin/bash ~/Documents/scripts/Update.sh >> ~/Documents/scripts/Update.log 2>&1`

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

Pour plus d’options: `man 5 crontab`.

#### Logs rotatifs

Pour eviter de saturer l'espace disque, il convient de mettre en place des logs rotatifs:

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

- daily: rotate every day
- rotate 30: keep 30 logs (≈30 days)
- compress: old logs are gzipped
- copytruncate: for scripts that keep the log file open

#### Rafraichir l'icône de mise à jour

TODO: Comment rafraichir l'icone de mise à jour ??
