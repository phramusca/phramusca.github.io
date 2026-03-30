---
layout: content
---

# Raspberry

## Installation

- Installer [rpi-imager](apt://rpi-imager) ([documentation](https://www.raspberrypi.com/documentation/))
- Mettre à jour:

  ```shell
  sudo rpi-update
  ```

- Copier les clés ssh (publiques) (depuis le PC):

  ```shell
  ssh-copy-id UTILISATEUR@ADRESSE_DU_PI
  ```

- [Pimp My terminal](../linux/system/terminal#pimp-my-terminal)
- [Installer Docker](/wiki/docker#installation)
- [Configurer docker](/wiki/docker#monter-un-disque-externe-avant-de-lancer-docker) pour monter les disques externes avant de lancer les images
- Installer [Portainer](/wiki/docker#portainer-ce)

## Mise à jour

### Paquet Debian `apt-auto-update` (recommandé)

- Télécharger [apt-auto-update_*.deb](https://github.com/phramusca/apt-auto-update/releases/latest)

Le projet **[apt-auto-update](https://github.com/phramusca/apt-auto-update)** installe la commande **`apt-auto-update`** : même idée que l’ancien script (mise à jour + nettoyage), avec **activation / désactivation** de la planification et **nettoyage à la suppression** du paquet.

Détails : README du dépôt [apt-auto-update](https://github.com/phramusca/apt-auto-update).

### Ancienne méthode : script utilisateur + crontab

Un petit script pour faire la maintenance du système (mises à jour et nettoyage des paquets inutilisés), par exemple `~/Documents/scripts/Update.sh` :

```bash
#!/bin/bash

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get autoremove -y
sudo apt-get autoclean
sudo apt-get clean

echo "-------------------- Press enter to exit --------------------"
read -r
```

Raccourci bureau (exemple) : fichier `Update & clean.desktop` :

```ini
[Desktop Entry]
Type=Application
Name=Update & clean
Exec=lxterminal -e ~/Documents/scripts/Update.sh
Icon=/usr/share/icons/AdwaitaLegacy/48x48/legacy/software-update-available.png
Terminal=false
```

#### Automatiser avec crontab utilisateur

```bash
crontab -e
```

Exemple (tous les jours à 4h) :

```bash
0 4 * * * /bin/bash ~/Documents/scripts/Update.sh >> ~/Documents/scripts/Update.log 2>&1
```

Rappel des champs cron :

```text
┌───────── minute (0 - 59)
│ ┌─────── heure (0 - 23)
│ │ ┌───── jour du mois (1 - 31)
│ │ │ ┌─── mois (1 - 12)
│ │ │ │ ┌─ jour de la semaine (0 - 7) (dimanche = 0 ou 7)
│ │ │ │ │
* * * * * commande à exécuter
```

`man 5 crontab` pour la suite.

#### Logs rotatifs (méthode manuelle)

Fichier `/etc/logrotate.d/Update` (adapter le chemin du `.log`) :

```text
/home/UTILISATEUR/Documents/scripts/Update.log {
    daily
    rotate 30
    missingok
    notifempty
    compress
    delaycompress
    copytruncate
}
```

- `daily` : rotation chaque jour  
- `rotate 30` : garder environ 30 jours  
- `missingok` / `notifempty` : ignorer fichier absent ou vide  
- `compress` : anciens journaux en gzip  
- `copytruncate` : adapté si le script garde le fichier ouvert  

Test : `sudo logrotate -f /etc/logrotate.d/Update`

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
