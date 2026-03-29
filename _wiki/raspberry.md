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
