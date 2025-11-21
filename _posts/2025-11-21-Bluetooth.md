---
layout: default
excerpt: Activer un dongle Bluetooth sous linux mint et appairer des périphériques
title: Bluetooth sous linux
---

# Connecter un appareil Bluetooth

Normalement, un PC avec du Bluetooth aura les outils décrits ci-dessous déjà installé. 

Si ce n'est pas le cas, voici commment faire:

## 1. Vérifier que le dongle Bluetooth est reconnu

Ouvrir un terminal et exécuter :

```bash
lsusb
```

Chercher une ligne mentionnant "Bluetooth" ou le fabricant du dongle Bluetooth.

## 2. Installer les outils Bluetooth

Si ce n’est pas déjà fait, installe les paquets nécessaires :

```bash
sudo apt update
sudo apt install bluez blueman
```
- `bluez` : pile Bluetooth officielle pour Linux.
- `blueman` : interface graphique pour gérer le Bluetooth.

## 3. Activer le service Bluetooth

Démarrer et activer le service Bluetooth :

```bash
sudo systemctl start bluetooth
sudo systemctl enable bluetooth
```

## 4. Lancer l’appairage

### Via l’interface graphique (Blueman)

- Ouvrir `Blueman` depuis le menu des applications.
- Cliquer sur `"Rechercher"` pour détecter du périphérique.
- Sélectionner le périphérique dans la liste et cliquer sur `"Appairer"`.
- Si demandé, confirmer le code PIN (souvent `0000` ou `1234`).

### Via le terminal

Si Blueman ne fonctionne pas, utiliser la ligne de commande :

```bash
bluetoothctl
```

Puis, dans l’interface `bluetoothctl` :

```bash
power on
agent on
scan on
```

Attendre que le périphérique apparaisse (ex: `Device XX:XX:XX:XX:XX:XX MX Master 4`), puis :

```bash
pair XX:XX:XX:XX:XX:XX
connect XX:XX:XX:XX:XX:XX
trust XX:XX:XX:XX:XX:XX
```

(Remplacer `XX:XX:XX:XX:XX:XX` par l’adresse MAC du périphérique.)

