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

/home/raph/.local/share/fonts/MesloLGS NF Bold.ttf: MesloLGS NF:style=Bold
/home/raph/.local/share/fonts/MesloLGS NF Italic.ttf: MesloLGS NF:style=Italic
/home/raph/.local/share/fonts/MesloLGS NF Bold Italic.ttf: MesloLGS NF:style=Bold Italic
/home/raph/.local/share/fonts/MesloLGS NF Regular.ttf: MesloLGS NF:style=Regular


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

Le script `HotspotWEP.sh`:

```bash
#!/bin/bash

# Hotspot WEP optimisé pour Nintendo DS Lite + Android
# Utilise des commandes modernes (ip, iw, nftables/iptables)

set -euo pipefail  # Arrêt en cas d'erreur, variables non définies, erreurs dans les pipes

# Vérifier les privilèges root
if [[ $EUID -ne 0 ]]; then
    echo "❌ Ce script nécessite des privilèges root"
    echo "   Utilisez: sudo $0 $*"
    exit 1
fi

# Configuration
readonly SSID="NDS"
readonly WEP_KEY="1234567890"
readonly WIFI_INTERFACE="wlan0"
readonly CONFIG_DIR="/tmp/hotspot_nds"
readonly PID_FILE_HOSTAPD="${CONFIG_DIR}/hostapd.pid"
readonly PID_FILE_DNSMASQ="${CONFIG_DIR}/dnsmasq.pid"

# Détection automatique de l'interface Ethernet
detect_eth_interface() {
    # Cherche la première interface Ethernet active (pas loopback, pas wlan)
    local iface
    for iface in /sys/class/net/*; do
        local name=$(basename "$iface")
        # Ignorer loopback, WiFi, et interfaces virtuelles
        if [[ "$name" != "lo" && "$name" != "$WIFI_INTERFACE" && "$name" != "docker0" && ! "$name" =~ ^br- ]]; then
            # Vérifier si c'est une interface physique (pas virtuelle)
            # Sur Raspberry Pi, eth0 est l'interface Ethernet standard
            if [[ -e "$iface/device" ]] || [[ "$name" =~ ^eth ]] || [[ "$name" =~ ^enp ]] || [[ "$name" =~ ^enx ]] || [[ "$name" =~ ^usb ]]; then
                if ip link show "$name" 2>/dev/null | grep -q "state UP"; then
                    echo "$name"
                    return 0
                fi
            fi
        fi
    done
    # Fallback: chercher eth0 ou enp* même si pas UP (pour Raspberry Pi)
    if ip link show eth0 &>/dev/null 2>&1; then
        echo "eth0"
    elif ip -o link show 2>/dev/null | grep -oP 'enp[^:]+' | head -1; then
        ip -o link show 2>/dev/null | grep -oP 'enp[^:]+' | head -1
    else
        echo "eth0"  # Fallback par défaut
    fi
}

readonly ETH_INTERFACE=$(detect_eth_interface)

# Vérification des prérequis
check_requirements() {
    local missing=()
    
    command -v hostapd >/dev/null 2>&1 || missing+=("hostapd")
    command -v dnsmasq >/dev/null 2>&1 || missing+=("dnsmasq")
    command -v ip >/dev/null 2>&1 || missing+=("iproute2")
    command -v iw >/dev/null 2>&1 || missing+=("iw")
    
    if [[ ${#missing[@]} -gt 0 ]]; then
        echo "❌ Outils manquants: ${missing[*]}"
        echo "   Installez-les avec: sudo apt install ${missing[*]}"
        exit 1
    fi
    
    # Vérifier si l'interface WiFi existe
    if ! ip link show "$WIFI_INTERFACE" &>/dev/null; then
        echo "❌ Interface WiFi '$WIFI_INTERFACE' introuvable"
        exit 1
    fi
    
    # Vérifier si l'interface supporte le mode AP
    if ! iw phy | grep -q "AP"; then
        echo "⚠️  Attention: L'interface peut ne pas supporter le mode AP"
    fi
}

# Vérifier si le hotspot est déjà actif
is_running() {
    [[ -f "$PID_FILE_HOSTAPD" ]] && kill -0 "$(cat "$PID_FILE_HOSTAPD")" 2>/dev/null
}

# Nettoyage en cas d'erreur
cleanup_on_error() {
    echo "❌ Erreur détectée, nettoyage..."
    stop_hotspot
    exit 1
}

trap cleanup_on_error ERR

# Créer le répertoire de configuration
mkdir -p "$CONFIG_DIR"

start_hotspot() {
    if is_running; then
        echo "⚠️  Le hotspot est déjà actif"
        return 0
    fi
    
    echo "🔧 Démarrage du hotspot (compatible DS Lite et Android)..."
    
    # Arrêter NetworkManager sur l'interface WiFi si présent
    if command -v nmcli >/dev/null 2>&1; then
        echo "   Désactivation de NetworkManager sur $WIFI_INTERFACE..."
        nmcli device set "$WIFI_INTERFACE" managed no 2>/dev/null || true
    fi
    
    # Arrêter wpa_supplicant si présent (Raspberry Pi)
    systemctl stop wpa_supplicant 2>/dev/null || true
    pkill -f wpa_supplicant 2>/dev/null || true
    
    # Configurer l'interface WiFi
    # Note: Sur Raspberry Pi, on ne change pas le type manuellement
    # hostapd le fera automatiquement
    echo "   Configuration de l'interface $WIFI_INTERFACE..."
    ip link set "$WIFI_INTERFACE" down 2>/dev/null || true
    sleep 1
    
    # Créer la configuration hostapd (WEP obligatoire pour DS)
    echo "   Configuration de hostapd..."
    cat > "${CONFIG_DIR}/hostapd.conf" <<EOF
interface=$WIFI_INTERFACE
driver=nl80211
ssid=$SSID
hw_mode=g
channel=1
wep_default_key=0
wep_key0=$WEP_KEY
country_code=FR
# Optimisations pour compatibilité DS
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
# Configuration IP (hostapd configurera l'interface)
# Sur Raspberry Pi, hostapd gère le changement de type d'interface
EOF
    
    # Créer la configuration dnsmasq
    echo "   Configuration de dnsmasq..."
    cat > "${CONFIG_DIR}/dnsmasq.conf" <<EOF
interface=$WIFI_INTERFACE
bind-interfaces
dhcp-range=10.0.0.100,10.0.0.200,255.255.255.0,1h
dhcp-option=3,10.0.0.1
dhcp-option=6,10.0.0.1
# DNS simple pour DS
server=8.8.8.8
server=8.8.4.4
log-queries
log-dhcp
EOF
    
    # Activer le forwarding IP
    echo "   Activation du forwarding IP..."
    sysctl -w net.ipv4.ip_forward=1 >/dev/null
    
    # Configurer le NAT avec nftables (moderne) ou iptables (fallback)
    echo "   Configuration du NAT..."
    if command -v nft >/dev/null 2>&1; then
        # Utiliser nftables (plus moderne)
        nft flush ruleset 2>/dev/null || true
        nft add table ip nat
        nft add chain ip nat postrouting { type nat hook postrouting priority 100 \; }
        nft add rule ip nat postrouting oifname "$ETH_INTERFACE" masquerade
        nft add table ip filter
        nft add chain ip filter forward { type filter hook forward priority 0 \; }
        nft add rule ip filter forward iifname "$WIFI_INTERFACE" oifname "$ETH_INTERFACE" accept
        nft add rule ip filter forward iifname "$ETH_INTERFACE" oifname "$WIFI_INTERFACE" ct state related,established accept
    else
        # Fallback sur iptables
        iptables -t nat -F
        iptables -F
        iptables -t nat -A POSTROUTING -o "$ETH_INTERFACE" -j MASQUERADE
        iptables -A FORWARD -i "$WIFI_INTERFACE" -o "$ETH_INTERFACE" -j ACCEPT
        iptables -A FORWARD -i "$ETH_INTERFACE" -o "$WIFI_INTERFACE" -m state --state RELATED,ESTABLISHED -j ACCEPT
    fi
    
    # Arrêter les instances existantes
    pkill -f "dnsmasq.*${CONFIG_DIR}/dnsmasq.conf" 2>/dev/null || true
    pkill -f "hostapd.*${CONFIG_DIR}/hostapd.conf" 2>/dev/null || true
    sleep 1
    
    # Lancer hostapd en premier (il configure l'interface en mode AP)
    # Sur Raspberry Pi, hostapd doit être lancé avant de configurer l'IP
    echo "   Démarrage de hostapd..."
    hostapd -B -P "${PID_FILE_HOSTAPD}" "${CONFIG_DIR}/hostapd.conf"
    sleep 3  # Attendre que hostapd configure l'interface
    
    # Vérifier que hostapd est bien démarré
    if ! kill -0 "$(cat "$PID_FILE_HOSTAPD")" 2>/dev/null; then
        echo "❌ Échec du démarrage de hostapd"
        stop_hotspot
        exit 1
    fi
    
    # Configurer l'adresse IP après que hostapd ait mis l'interface en mode AP
    echo "   Configuration de l'adresse IP..."
    ip addr add 10.0.0.1/24 dev "$WIFI_INTERFACE" 2>/dev/null || true
    ip link set "$WIFI_INTERFACE" up
    
    # Lancer dnsmasq
    echo "   Démarrage de dnsmasq..."
    dnsmasq -C "${CONFIG_DIR}/dnsmasq.conf" -x "${PID_FILE_DNSMASQ}" &
    sleep 1
    
    echo ""
    echo "✅ Hotspot '$SSID' démarré avec succès !"
    echo "   📡 SSID: $SSID"
    echo "   🔑 Clé WEP: $WEP_KEY"
    echo "   🌐 IP du routeur: 10.0.0.1"
    echo "   📱 Plage DHCP: 10.0.0.100 - 10.0.0.200"
    echo "   🎮 Compatible Nintendo DS Lite et Android"
    echo ""
    echo "   Pour arrêter: sudo $0 stop"
}

stop_hotspot() {
    if ! is_running; then
        echo "ℹ️  Le hotspot n'est pas actif"
        return 0
    fi
    
    echo "⏹  Arrêt du hotspot..."
    
    # Arrêter hostapd
    if [[ -f "$PID_FILE_HOSTAPD" ]]; then
        local pid=$(cat "$PID_FILE_HOSTAPD")
        kill "$pid" 2>/dev/null || true
        rm -f "$PID_FILE_HOSTAPD"
    else
        pkill -f "hostapd.*${CONFIG_DIR}/hostapd.conf" 2>/dev/null || true
    fi
    
    # Arrêter dnsmasq
    if [[ -f "$PID_FILE_DNSMASQ" ]]; then
        local pid=$(cat "$PID_FILE_DNSMASQ")
        kill "$pid" 2>/dev/null || true
        rm -f "$PID_FILE_DNSMASQ"
    else
        pkill -f "dnsmasq.*${CONFIG_DIR}/dnsmasq.conf" 2>/dev/null || true
    fi
    
    sleep 1
    
    # Désactiver le forwarding
    sysctl -w net.ipv4.ip_forward=0 >/dev/null 2>&1 || true
    
    # Nettoyer les règles de filtrage
    if command -v nft >/dev/null 2>&1; then
        nft flush ruleset 2>/dev/null || true
    else
        iptables -t nat -F 2>/dev/null || true
        iptables -F 2>/dev/null || true
    fi
    
    # Réinitialiser l'interface WiFi
    ip addr flush dev "$WIFI_INTERFACE" 2>/dev/null || true
    ip link set "$WIFI_INTERFACE" down 2>/dev/null || true
    
    # Sur Raspberry Pi, hostapd a changé le type, on le remet en managed
    # Mais on évite de le faire si ça échoue (certaines interfaces le font automatiquement)
    iw dev "$WIFI_INTERFACE" set type managed 2>/dev/null || true
    sleep 1
    ip link set "$WIFI_INTERFACE" up 2>/dev/null || true
    
    # Réactiver wpa_supplicant sur Raspberry Pi
    systemctl start wpa_supplicant 2>/dev/null || true
    
    # Réactiver NetworkManager si présent
    if command -v nmcli >/dev/null 2>&1; then
        nmcli device set "$WIFI_INTERFACE" managed yes 2>/dev/null || true
    fi
    
    # Nettoyer les fichiers de configuration
    rm -rf "$CONFIG_DIR"
    
    echo "✅ Hotspot arrêté"
}

status_hotspot() {
    if is_running; then
        local hostapd_pid=$(cat "$PID_FILE_HOSTAPD")
        local dnsmasq_pid=$(cat "$PID_FILE_DNSMASQ" 2>/dev/null || echo "N/A")
        
        echo "✅ Hotspot actif"
        echo "   SSID: $SSID"
        echo "   Clé WEP: $WEP_KEY"
        echo "   IP: 10.0.0.1"
        echo "   hostapd PID: $hostapd_pid"
        echo "   dnsmasq PID: $dnsmasq_pid"
        echo "   Interface WiFi: $WIFI_INTERFACE"
        echo "   Interface Ethernet: $ETH_INTERFACE"
    else
        echo "❌ Hotspot inactif"
    fi
}

# Vérifier les prérequis avant d'exécuter
check_requirements

# Gestion des arguments
case "${1:-}" in
    start)
        start_hotspot
        ;;
    stop)
        stop_hotspot
        ;;
    status|restart)
        if [[ "$1" == "restart" ]]; then
            stop_hotspot
            sleep 2
            start_hotspot
        else
            status_hotspot
        fi
        ;;
    *)
        echo "Usage: $0 {start|stop|status|restart}"
        echo ""
        echo "Commandes:"
        echo "  start   - Démarrer le hotspot WEP"
        echo "  stop    - Arrêter le hotspot"
        echo "  status  - Afficher l'état du hotspot"
        echo "  restart - Redémarrer le hotspot"
        exit 1
        ;;
esac
```
