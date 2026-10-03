---
layout: content
---

# Raspberry

## Installation

Depuis un PC:

- installer Raspberry Pi Imager: [rpi-imager](apt://rpi-imager) ([documentation](https://www.raspberrypi.com/documentation/))
- Créer une microSD avec le Raspberry Pi OS (64-bit)

## Configuration du Raspberry

- Mettre à jour:

  ```shell
  sudo rpi-update
  ```

- **Depuis le PC**, copier les clés ssh (publiques):

  ```shell
  ssh-copy-id UTILISATEUR@ADRESSE_DU_PI
  ```

- [Pimp My terminal](../linux/system/terminal#pimp-my-terminal)
- [Installer la mise à jour automatique](#mise-à-jour-automatique)
- [Installer Docker](/wiki/docker#installation)
- [Configurer docker](/wiki/docker#monter-un-disque-externe-avant-de-lancer-docker) pour monter les disques externes avant de lancer les images
- Installer [Portainer](/wiki/docker#portainer-ce) et les autres [applications docker](/wiki/docker#docker-compose) depuis Portainer.
- (Configuer le réseau pour [l'accès aux applications Docker par leur nom](/wiki/docker#accéder-aux-applications-docker-par-leur-nom))
- [Configurer VNC](#tunnel-ssh-pour-vnc-sur-raspberry-pi-5) (ayant eu dernièrement pleins de problèmes de connexion dues au problème de l'auth (avec un truc appelé pam), j'ai créé un tunnel ssh, ce qui a résolu le problème et me permet de me connecter sans authentification comme pour ssh)

## Tunnel SSH pour VNC sur Raspberry Pi 5

Accès VNC chiffré et authentifié par clé SSH, sans mot de passe VNC.  
Principe : wayvnc n'écoute que sur `localhost` du Pi ; TigerVNC passe par le tunnel SSH.

```text
TigerVNC ──► localhost:5900 (PC) ──► tunnel SSH ──► localhost:5900 (Pi: wayvnc)
```

### 1. Configurer wayvnc côté Pi

Éditer `/etc/wayvnc/config` :

```ini
enable_auth=false
address=127.0.0.1
port=5900
```

Puis redémarrer le service :

```bash
sudo systemctl restart wayvnc
```

wayvnc n'est plus joignable depuis le réseau : seule une session SSH sur le Pi peut y accéder.

### 2. Créer le tunnel depuis le PC

>/!\ Il faut avoir copié les clés ssh sur le pi avant de lancer cette commande

```bash
ssh -N -L 5900:localhost:5900 UTILISATEUR@ADRESSE_DU_PI
```

- `-L 5900:localhost:5900` : redirige le port 5900 local vers le 5900 du Pi
- `-N` : n'ouvre pas de shell, juste le tunnel

Laisser cette commande tourner dans un terminal.

### 3. Se connecter avec TigerVNC

Dans TigerVNC Viewer, se connecter à :

```text
localhost:5900
```

Aucune authentification VNC n'est demandée : c'est la clé SSH qui joue ce rôle, et le trafic est chiffré de bout en bout.

### 4. Tunnel avec reconnexion automatique

Pour éviter de relancer la commande à chaque coupure (réseau, veille du Pi) ou redémarrage du PC

1. Dans `~/.ssh/config` du PC :

    ```text
    Host rpi5-vnc
        HostName ADRESSE_DU_PI
        User UTILISATEUR
        ServerAliveInterval 30
        ServerAliveCountMax 3
        ExitOnForwardFailure yes
    ```

1. Créer le fichier ~/.config/systemd/user/rpi5-vnc-tunnel.service

    ```ini
    [Unit]
    Description=Tunnel SSH VNC vers rpi5
    After=network-online.target

    [Service]
    ExecStart=/usr/bin/ssh -N -o ExitOnForwardFailure=yes -o ServerAliveInterval=30 -o ServerAliveCountMax=3 -L 5900:localhost:5900 rpi5-vnc
    Restart=always
    RestartSec=5

    [Install]
    WantedBy=default.target
    ```

1. Activer et lancer :

    ```bash
    systemctl --user daemon-reload
    systemctl --user enable --now rpi5-vnc-tunnel.service
    ```

    `ServerAliveInterval` détecte les connexions mortes en \~90 s et ferme le tunnel proprement au lieu de rester bloqué.

Commandes utiles:

```bash
systemctl --user status rpi5-vnc-tunnel    # état du tunnel
journalctl --user -u rpi5-vnc-tunnel -f   # logs en direct
systemctl --user stop rpi5-vnc-tunnel     # arrêter
systemctl --user disable rpi5-vnc-tunnel  # désactiver au démarrage
```

Le tunnel tourne en arrière-plan dès l'ouverture de session : TigerVNC se connecte simplement à localhost:5900, rien d'autre à faire.

> **Note** : si la session SSH utilise une clé protégée par passphrase, ajouter un agent ssh (ssh-add) au démarrage de la session, ou une clé sans passphrase dédiée au tunnel (restrictive : restrict,command=echo dans authorized_keys du Pi).

### 5. Vérifications et dépannage

| Problème                              | Vérification                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| « Connection refused » dans TigerVNC  | Le tunnel tourne-t-il ? `ssh -N -L ...` doit rester ouvert                                              |
| Tunnel se ferme aussitôt              | Port 5900 déjà utilisé en local : essayer `-L 5901:localhost:5900` puis se connecter à `localhost:5901` |
| Écran noir / connexion qui se détache | Écran HDMI du Pi : fixer une résolution dans `raspi-config` → Display Options → Screen Resolution       |
| wayvnc injoignable                    | `sudo systemctl status wayvnc` et `ss -tlnp \| grep 5900` : doit écouter sur `127.0.0.1:5900`            |

### Récap sécurité

- Authentification : **clé SSH** (aucun mot de passe, côté Pi comme côté VNC)
- Chiffrement : **SSH** de bout en bout
- Exposition réseau : **aucune** — le port 5900 n'est ouvert que sur le localhost du Pi
- La box ne doit pas avoir de redirection du port 22 ou 5900 vers le Pi (à vérifier)

## Mise à jour automatique

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
