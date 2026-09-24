---
layout: content
---

# Docker

J'utilise [Docker](https://www.docker.com/) pour faire tourner quelques services sur mon [Raspberry](/wiki/raspberry) Pi.

## Installation

Installation depuis la [liste des logiciels](../linux/soft#category-6-programmation)

- Puis, ajouter l'utilisateur au groupe docker (pour éviter d'utiliser `sudo` à chaque commande docker)

  ```shell
  sudo usermod -aG docker $USER
  ```

  > ⚠️ **Important** : Il faut se déconnecter et se reconnecter (ou redémarrer) pour que les changements de groupe prennent effet.

- Voir la version de docker

  ```shell
  docker --version
  ```

### Sinon, manuellement

- Ajouter la clé GPG de Docker

  ```shell
  sudo install -m 0755 -d /etc/apt/keyrings
  ```

  ```shell
  curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
  ```

  ```shell
  sudo chmod a+r /etc/apt/keyrings/docker.gpg
  ```

- Ajouter le dépôt Docker (choisir **une** ligne selon la base — voir [la doc officielle](https://docs.docker.com/engine/install/)) :

  Debian / Raspberry Pi OS :

  ```shell
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```

  Ubuntu / Linux Mint :

  ```shell
  echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  ```

- Mettre à jour les dépôts et installer la **version courante** du dépôt (moteur + CLI + containerd ; plugins optionnels)

  ```shell
  sudo apt-get update
  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
  ```

- Démarrer Docker

  ```shell
  sudo systemctl start docker
  ```

  ```shell
  sudo systemctl enable docker
  ```

- Ajouter l'utilisateur au groupe docker (pour éviter d'utiliser `sudo` à chaque commande docker)

  ```shell
  sudo usermod -aG docker $USER
  ```

  > ⚠️ **Important** : Il faut se déconnecter et se reconnecter (ou redémarrer) pour que les changements de groupe prennent effet.

- Voir la version de docker

  ```shell
  docker --version
  ```

## Suppression

```shell
# Arrêter Docker
sudo systemctl stop docker
sudo systemctl stop docker.socket

# Désinstaller Docker et ses dépendances
sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Supprimer les fichiers de configuration et données
# /!\ Ne pas supprimer si vous voulez garder les volumes, ...
# sudo rm -rf /var/lib/docker
# sudo rm -rf /var/lib/containerd
# sudo rm -rf /etc/docker
```

## Docker Compose

### Portainer CE

Vérifier la **compatibilité** entre la version du moteur Docker et Portainer sur [les prérequis Portainer](https://docs.portainer.io/start/install-ce/requirements-and-prerequisites) (les exigences évoluent avec les versions).

[Documentation d'installation](https://docs.portainer.io/start/install-ce/server/docker/linux)

```yaml
services:
  portainer:
    image: portainer/portainer-ce:lts
    container_name: portainer
    restart: unless-stopped
    security_opt:
      - no-new-privileges:true
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - ${VOLUME_PATH}/portainer:/data
    ports:
      - "9443:9443"
```

Avec fichier `.env` :

```ini
  VOLUME_PATH="/chemin/avec des espaces"
```

- Naviguer vers [https://localhost:9443](https://localhost:9443) et suivre la procédure d'installation.

### Forgejo

[Documentation d'installation](https://forgejo.org/docs/latest/admin/installation-docker/)

```yaml
services:
  forgejo:
    image: codeberg.org/forgejo/forgejo:9.0.0
    container_name: forgejo
    restart: unless-stopped
    volumes:
      - ${VOLUME_PATH}/forgejo/data:/data
    ports:
      - 3000:3000
```

Avec fichier `.env` :

```ini
  VOLUME_PATH="/chemin/avec des espaces"
```

#### Se connecter aux repos git avec `ssh`

1. **Configuration de Forgejo**

   - Modifier le fichier `/data/gitea/conf/app.ini` pour activer le serveur SSH intégré de Forgejo sur le port 2222:

     ```ini
     [server]
     DOMAIN = rpi5.local
     SSH_DOMAIN = rpi5.local
     START_SSH_SERVER = true
     SSH_LISTEN_PORT = 2222
     ```

   - Modifier le fichier `docker-compose.yml` pour exposer le port 2222:

      ```yaml
      ports:
        - "3000:3000"
        - "2222:2222"
      ```

   - Redémarrer le conteneur Docker pour prendre en compte la nouvelle configuration.

1. **Configuration du client SSH**

   - Créer l'hôte `forgejo` dans `~/.ssh/config` sur la machine cliente :

      ```config
      # Pour Git/Forgejo (git@rpi5.local)
      Host forgejo
        HostName rpi5.local
        User git
        Port 2222
      ```

   - Changer l'URL du remote Git :

     ```bash
     git remote set-url origin git@forgejo:phramusca/taratata-downloader.git
     ```

   - Ajouter la clé publique du client dans l'interface web Forgejo (Settings > SSH Keys).

   - Tester la connexion SSH :

      ```bash
      ssh git@rpi5.local -p 2222
      ```

      ou

      ```bash
      ssh git@forgejo
      ```

     Ce qui doit donner un message du genre:

      ```text
      PTY allocation request failed on channel 0
      Hi there, xxxxxx! You've successfully authenticated with the key named yyyyy, but Forgejo does not provide shell access.
      If this is unexpected, please log in with password and setup Forgejo under another user.
      Connection to rpi5.local closed.
      ```

   - Tester les commandes Git (`git fetch`, `git pull`, `git push`, ...) qui doivent fonctionner sans demander de mot de passe.

### Lazy Docker

[Documentation d'installation](https://github.com/jesseduffield/lazydocker?tab=readme-ov-file#docker)

Pour Raspberry Pi 5 :

```yaml
services:
  lazydocker:
    build:
      context: https://github.com/jesseduffield/lazydocker.git
      args:
        BASE_IMAGE_BUILDER: arm64v8/golang
        GOARCH: arm64
        GOARM:
    image: lazyteam/lazydocker
    container_name: lazydocker
    stdin_open: true
    tty: true
    restart: unless-stopped
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ${VOLUME_PATH}/lazydocker/config:/.config/jesseduffield/lazydocker
```

Avec fichier `.env` :

```ini
  VOLUME_PATH="/chemin/avec des espaces"
```

Puis lancer avec :

```sh
docker exec -it lazydocker lazydocker
```

### Romm

[Documentation](https://github.com/rommapp/romm/wiki/Quick-Start-Guide)

```yaml
volumes:
  mysql_data:

services:
  romm:
    image: rommapp/romm:3.7.3
    container_name: romm
    restart: unless-stopped
    environment:
      - DB_HOST=romm-db
      - DB_NAME=romm # doit correspondre à MYSQL_DATABASE dans MariaDB
      - DB_USER=romm-user # doit correspondre à MYSQL_USER dans MariaDB
      - DB_PASSWD=${DB_PASSWD} # doit correspondre à MYSQL_PASSWORD dans MariaDB
      - ROMM_AUTH_SECRET_KEY=${ROMM_AUTH_SECRET_KEY} # clé : openssl rand -hex 32
      - IGDB_CLIENT_ID=${IGDB_CLIENT_ID} # créer un ID et un secret sur IGDB
      - IGDB_CLIENT_SECRET=${IGDB_CLIENT_SECRET} # https://api-docs.igdb.com/#account-creation
      - MOBYGAMES_API_KEY=${MOBYGAMES_API_KEY} # https://www.mobygames.com/info/api/
      - STEAMGRIDDB_API_KEY=${STEAMGRIDDB_API_KEY} # https://github.com/rommapp/romm/wiki/Generate-API-Keys#steamgriddb
    volumes:
      - ${VOLUME_PATH}/cache/romm_resources:/romm/resources # ressources IGDB (jaquettes, captures, etc.)
      - ${VOLUME_PATH}/cache/romm_redis_data:/redis-data # cache pour les tâches en arrière-plan
      - ${VOLUME_PATH}/library:/romm/library # bibliothèque de jeux
      - ${VOLUME_PATH}/assets:/romm/assets # sauvegardes et états uploadés, etc.
      - ${VOLUME_PATH}/config:/romm/config # répertoire du config.yml
    ports:
      - 80:8080
    depends_on:
      - romm-db

  romm-db:
    image: linuxserver/mariadb:10.11.8
    container_name: romm-db
    restart: unless-stopped
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} # mot de passe root unique et solide
      - MYSQL_DATABASE=romm
      - MYSQL_USER=romm-user
      - MYSQL_PASSWORD=${DB_PASSWD}
    volumes:
      - ${VOLUME_PATH}/mariadb/config:/config
```

Avec fichier `.env` :

```ini
VOLUME_PATH="/chemin/avec des espaces"
DB_PASSWD=
MYSQL_ROOT_PASSWORD=
ROMM_AUTH_SECRET_KEY=
IGDB_CLIENT_ID=
IGDB_CLIENT_SECRET=
MOBYGAMES_API_KEY=
STEAMGRIDDB_API_KEY=
```

### Calibre Web

[https://github.com/janeczku/calibre-web](https://github.com/janeczku/calibre-web)

```yaml
services:
  calibre-web:
    image: linuxserver/calibre-web
    container_name: calibre-web
    ports:
      - 8083:8083
    volumes:
      - ${VOLUME_PATH}/books:/app/calibre-web/books
      - ${VOLUME_PATH}/config:/config
    restart: unless-stopped
```

Avec fichier `.env` :

```ini
VOLUME_PATH="/chemin/avec des espaces"
```

### Wanderer

[Wanderer](https://wanderer.to/) est une base de données de sentiers GPX (ou Kml) décentralisée et auto-hébergée. Vous pouvez télécharger vos trajets GPS enregistrés ou en créer de nouveaux et ajouter diverses métadonnées pour créer un catalogue facilement consultable.

```yaml
x-common-env: &cenv
  MEILI_URL: http://search:7700
  MEILI_MASTER_KEY: ${MEILI_MASTER_KEY}

services:
  search:
    container_name: wanderer-search
    image: getmeili/meilisearch:v1.36.0
    environment:
      <<: *cenv
      MEILI_NO_ANALYTICS: "true"
    ports:
      - 7700:7700
    networks:
      - wanderer
    volumes:
      - ${WANDERER_DATA_DIR:-./data}/data.ms:/meili_data/data.ms
    restart: unless-stopped
    healthcheck:
      test: curl --fail http://localhost:7700/health || exit 1
      interval: 15s
      retries: 10
      start_period: 20s
      timeout: 10s
  db:
    container_name: wanderer-db
    image: flomp/wanderer-db
    depends_on:
      search:
        condition: service_healthy
    environment:
      <<: *cenv
      POCKETBASE_ENCRYPTION_KEY: ${POCKETBASE_ENCRYPTION_KEY}
      ORIGIN: ${WANDERER_ORIGIN:-http://localhost:3000}
      POCKETBASE_CRON_SYNC_SCHEDULE: ${POCKETBASE_CRON_SYNC_SCHEDULE}
    ports:
      - "8090:8090"
    networks:
      - wanderer
    restart: unless-stopped
    volumes:
      - ${WANDERER_DATA_DIR:-./data}/pb_data:/pb_data
    healthcheck:
      test: ["CMD", "/curl", "--fail", "http://localhost:8090/health"]
      interval: 15s
      retries: 10
      start_period: 20s
      timeout: 10s
  web:
    container_name: wanderer-web
    image: flomp/wanderer-web
    depends_on:
      search:
        condition: service_healthy
      db:
        condition: service_healthy
    environment:
      <<: *cenv
      ORIGIN: ${WANDERER_ORIGIN:-http://localhost:3000}
      BODY_SIZE_LIMIT: Infinity
      PUBLIC_POCKETBASE_URL: http://db:8090
      PUBLIC_DISABLE_SIGNUP: "false"
      UPLOAD_FOLDER: /app/uploads
      UPLOAD_USER: ${UPLOAD_USER:-}
      UPLOAD_PASSWORD: ${UPLOAD_PASSWORD:-}
      PUBLIC_OVERPASS_API_URL: https://overpass-api.de
      PUBLIC_VALHALLA_URL: https://valhalla1.openstreetmap.de
      PUBLIC_NOMINATIM_URL: https://nominatim.openstreetmap.org
    volumes:
      - ${WANDERER_DATA_DIR:-./data}/uploads:/app/uploads
      # - ${WANDERER_DATA_DIR:-./data}/about.md:/app/build/client/md/about.md
    ports:
      - "${WANDERER_WEB_PORT:-3000}:3000"
    networks:
      - wanderer
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "/curl", "--fail", "http://localhost:3000/"]
      interval: 15s
      retries: 10
      start_period: 20s
      timeout: 10s

networks:
  wanderer:
    driver: bridge
```

Fichier `.env` ([dépôt](https://github.com/open-wanderer/wanderer), [documentation](https://wanderer.to/welcome)) :

```ini
# Chemin des données de Wanderer
WANDERER_DATA_DIR="/chemin/vers/données/wanderer"

# URL exacte dans le navigateur : protocole + hôte + port, sinon erreurs CORS.
# WANDERER_ORIGIN=http://localhost:3000
# Port sur l'hôte pour l'interface web. Doit être cohérent avec WANDERER_ORIGIN.
# WANDERER_WEB_PORT=3000

# MEILI_MASTER_KEY : en production ou instance exposée, clé obligatoire (pas celle du dépôt). Générer : openssl rand -hex 32
MEILI_MASTER_KEY=

# POCKETBASE_ENCRYPTION_KEY : base neuve — openssl rand -hex 16 avant le 1er lancement (doc Wanderer) ; ne pas changer après (déchiffrement cassé)
POCKETBASE_ENCRYPTION_KEY=

# POCKETBASE_CRON_SYNC_SCHEDULE : absent du compose d'origine ; expression cron de synchro PocketBase (décommenter si besoin)
# POCKETBASE_CRON_SYNC_SCHEDULE="0 */2 * * *"

# UPLOAD_USER / UPLOAD_PASSWORD : optionnel ; HTTP basic sur l'endpoint d'upload si renseignés
# UPLOAD_USER=
# UPLOAD_PASSWORD=
```

## Accéder aux applications Docker par leur nom

Pour accéder aux applications sans mémoriser un port, j'utilise deux services
complémentaires :

- [Pi-hole](https://pi-hole.net/) fournit le DNS local et fait correspondre les
  noms aux adresses IP ;
- [Nginx Proxy Manager](https://nginxproxymanager.com/) est le reverse proxy :
  il reçoit les requêtes HTTP/HTTPS sur les ports `80`/`443` et les transmet au
  bon conteneur.

L'architecture est par exemple la suivante :

```text
romm.rpi5.home.arpa
        │
        ├── DNS Pi-hole ──> 192.168.1.92
        │
        └── Nginx Proxy Manager:80/443
                         └──> RomM:8082
```

On utilise ici `home.arpa`, réservé aux réseaux domestiques. Le suffixe
`rpi5.local` est fourni par mDNS/Avahi pour le nom de l'hôte, mais il ne crée
pas automatiquement de sous-domaines comme `romm.rpi5.local`. Il vaut donc
mieux utiliser un domaine local géré par son propre DNS :

```text
http://romm.rpi5.home.arpa
http://portainer.rpi5.home.arpa
```

### Nginx Proxy Manager

Nginx Proxy Manager doit être le seul service qui utilise les ports `80` et
`443` de l'hôte. Les applications peuvent continuer à utiliser leurs ports
actuels (par exemple `8082` pour RomM), mais ces ports ne sont plus nécessaires
dans l'URL des clients.

```yaml
services:
  app:
    image: 'jc21/nginx-proxy-manager:2.15.1'
    restart: unless-stopped
    ports:
      # These ports are in format <host-port>:<container-port>
      - '80:80' # Public HTTP Port
      - '443:443' # Public HTTPS Port
      - '81:81' # Admin Web Port
      # Add any other Stream port you want to expose
      # - '21:21' # FTP
    environment:
      TZ: "Europe/Paris"

      # Uncomment this if you want to change the location of
      # the SQLite DB file within the container
      # DB_SQLITE_FILE: "/data/database.sqlite"

      # Uncomment this if IPv6 is not enabled on your host
      # DISABLE_IPV6: 'true'
    volumes:
      - ${VOLUME_PATH}/data:/data
      - ${VOLUME_PATH}/letsencrypt:/etc/letsencrypt
```

Avec fichier `.env` :

```ini
VOLUME_PATH="/chemin/avec des espaces"
```

Après le déploiement, l'interface d'administration est disponible sur
`http://rpi5.local:81`. Dans **Hosts > Proxy Hosts**, ajouter par exemple :

| Domain Names | Scheme | Forward Host | Forward Port |
| --- | --- | --- | ---: |
| `romm.rpi5.home.arpa` | `http` | `192.168.1.92` | `8082` |

Activer **Websockets Support** si l'application en a besoin. Pour les autres
applications, ajouter un proxy host avec le même principe :

```text
portainer.rpi5.home.arpa  -> 192.168.1.92:9000
immich.rpi5.home.arpa     -> 192.168.1.92:2283
```

Ne pas exposer le port `81` sur Internet. Il sert uniquement à administrer
Nginx Proxy Manager depuis le réseau local.

### Pi-hole et DNS local

Pi-hole est le serveur DNS utilisé par les appareils du réseau. Il doit être
joignable sur le port DNS `53` de l'hôte. Dans son interface
(`http://rpi5.local:8085` avec la configuration ci-dessous), ajouter les
enregistrements dans **Local DNS > DNS Records** :

| Domaine | Adresse IP |
| --- | --- |
| `romm.rpi5.home.arpa` | `192.168.1.92` |
| `portainer.rpi5.home.arpa` | `192.168.1.92` |

Tous les noms utilisés dans Nginx Proxy Manager doivent avoir un
enregistrement DNS Pi-hole qui pointe vers l'adresse IP du Raspberry Pi.
Pi-hole ne redirige pas le trafic web : il fait uniquement la résolution du
nom. C'est Nginx Proxy Manager qui choisit ensuite l'application et son port.

```yaml
# More info at https://github.com/pi-hole/docker-pi-hole/ and https://docs.pi-hole.net/
services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    ports:
      # DNS Ports
      - "53:53/tcp"
      - "53:53/udp"
      # Default HTTP Port
      - "8085:80/tcp"
      # Default HTTPs Port. FTL will generate a self-signed certificate
      - "4435:443/tcp"
      # Uncomment the line below if you are using Pi-hole as your DHCP server
      #- "67:67/udp"
      # Uncomment the line below if you are using Pi-hole as your NTP server
      #- "123:123/udp"
    environment:
      # Set the appropriate timezone for your location (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones), e.g:
      TZ: 'Europe/Paris'
      # Set a password to access the web interface. Not setting one will result in a random password being assigned
      FTLCONF_webserver_api_password: 'CHANGER_CE_MOT_DE_PASSE'
      # If using Docker's default `bridge` network setting the dns listening mode should be set to 'ALL'
      FTLCONF_dns_listeningMode: 'ALL'
    # Volumes store your data between container upgrades
    volumes:
       - ${VOLUME_PATH}:/etc/pihole
    restart: unless-stopped
```

Avec fichier `.env` :

```ini
VOLUME_PATH="/chemin/avec des espaces"
```

### Configurer le DNS distribué par le routeur

Le serveur DHCP du routeur doit annoncer l'adresse IP de Pi-hole comme serveur
DNS. Dans la Freebox, ouvrir l'application Freebox ou l'interface
d'administration, puis rechercher les paramètres du réseau local, du DHCP ou
des serveurs DNS. Renseigner :

```text
Serveur DNS primaire : 192.168.1.92
```

Laisser le DNS secondaire vide permet d'éviter que les clients contournent
Pi-hole pour les noms locaux. Si la Freebox impose un DNS secondaire, il faut
vérifier qu'il ne prend pas la priorité sur Pi-hole.

La réservation DHCP de l'adresse `192.168.1.92` doit rester active (ou cette
adresse doit être configurée statiquement sur le Raspberry Pi), car le routeur
doit toujours retrouver Pi-hole à la même adresse.

### Renouveler le réseau sur les hôtes clients

Après avoir modifié les paramètres DHCP/DNS, les appareils doivent récupérer la
nouvelle configuration. Le plus simple est par le gestionnaire de réseau de la distrib. Sinon, en ligne de commande, il faut: 

Identifier la connexion active :

```sh
nmcli -f NAME,DEVICE connection show --active
```

Exemple de sortie:

```sh
NAME                  DEVICE          
Connexion Ethernet 1  enxa84a6391096a 
docker0               docker0         
lo                    lo              
lxcbr0                lxcbr0          
veth7372412           veth7372412     
virbr0                virbr0 
```

Dans cet exemple, la connexion active est `Connexion Ethernet 1` sur
l'interface `enxa84a6391096a`. La désactiver puis la réactiver demande une
nouvelle configuration DHCP :

```sh
sudo nmcli connection down id "Connexion Ethernet 1"
sudo nmcli connection up id "Connexion Ethernet 1"
```

Le nom de l'interface (`enxa84a6391096a`) n'est pas le nom à utiliser avec
`nmcli connection down/up` : ces commandes attendent le nom de la connexion,
ici `Connexion Ethernet 1`.

Vérifier ensuite que Pi-hole est bien utilisé et que le nom se résout :

```sh
resolvectl dns
getent hosts romm.rpi5.home.arpa
curl -I http://romm.rpi5.home.arpa
```

## Monter un disque externe avant de lancer docker

J'utilise un disque externe pour stocker les données des services Docker. Le disque doit être monté **avant** `docker.service`. Un script automatise les unités `.mount` et le *drop-in* `docker.service` (`After=` / `Requires=`).

### Script [docker-pre-mount-disks.sh](../../scripts/docker-pre-mount-disks.sh)

```sh
chmod +x docker-pre-mount-disks.sh
sudo ./docker-pre-mount-disks.sh          # menu interactif
sudo ./docker-pre-mount-disks.sh list
sudo ./docker-pre-mount-disks.sh add      # liste + numéro ; chemin [défaut = montage actuel]
sudo ./docker-pre-mount-disks.sh remove   # liste des unités avec détail, puis numéro
```

- **État** : liste des unités dans `/etc/docker/pre-mount-disks.units` ; *drop-in* Docker : `/etc/systemd/system/docker.service.d/10-docker-pre-mount-disks.conf`.
- **add** : liste les volumes avec UUID/FSTYPE (via `lsblk -P`) ; tu choisis le **numéro** (ou `0` pour saisir l'UUID à la main). Le point de montage est demandé avec le **chemin actuel** (`MOUNTPOINT`) comme défaut entre crochets si le volume est déjà monté ; **Entrée** le conserve. Le **propriétaire** propose par défaut `USER:USER`, sinon le propriétaire du répertoire ou du parent ; **Entrée** le conserve (tu peux saisir `root:root` si besoin). Puis `chown` du point de montage. Vérifie `/dev/disk/by-uuid/…`, crée l'unité `*.mount` (nom via `systemd-escape`), active le montage, régénère le *drop-in* et redémarre Docker.
- **remove** : liste numérotée avec les colonnes **Where / What / état** (où / quoi / état) pour chaque unité, puis choix du numéro.
- Après une réinstall, il suffit de **remettre le script** et, si les fichiers système ont sauté, de refaire **add** pour chaque disque (mêmes UUID et chemins).

Vérification après redémarrage :

```sh
sudo systemctl status media-…-.mount
sudo systemctl status docker
```

### Référence manuelle (sans script)

Procédure :

- Identifier l'UUID du disque USB :

  ```sh
  lsblk -o NAME,UUID,MOUNTPOINT
  ```

  - Notez l'UUID du disque correspondant.

- Créer un fichier d'unité systemd `.mount` pour gérer le montage du disque :  

  ```sh
  sudo nano /etc/systemd/system/media-myuser-MyDiskLabel.mount
  ```

  - Y insérer le contenu suivant, en remplaçant `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` par l'UUID du disque :  

    ```toml
    [Unit]  
    Description=Montage du disque USB MyDiskLabel  
    Before=docker.service  

    [Mount]  
    What=/dev/disk/by-uuid/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  
    Where=/media/myuser/MyDiskLabel  
    Type=ext4  
    Options=defaults  

    [Install]  
    WantedBy=multi-user.target
    ```

- Créer le répertoire de montage :  

   ```sh
   sudo mkdir -p /media/myuser/MyDiskLabel
   sudo chown myuser:myuser /media/myuser/MyDiskLabel
   ```

- Recharger la configuration de `systemd` et activer l'unité :

   ```sh
   sudo systemctl daemon-reload
   sudo systemctl enable media-myuser-MyDiskLabel.mount
   sudo systemctl start media-myuser-MyDiskLabel.mount
  ```

- Vérifier que le montage fonctionne :

   ```sh
   sudo systemctl status media-myuser-MyDiskLabel.mount
   ls /media/myuser/MyDiskLabel
  ```

- Configurer Docker pour attendre le montage :  

   ```sh
   sudo systemctl edit docker.service
   ```

  - Ajouter les lignes suivantes :  

      ```toml
      [Unit]  
      After=media-myuser-MyDiskLabel.mount  
      Requires=media-myuser-MyDiskLabel.mount  
      ```

  - Pour plusieurs disques, les séparer par un espace dans `After=` et `Requires=`.

      ```toml
      [Unit]
      After=media-myuser-MyDiskLabel.mount media-myuser-MySecondDisk.mount
      Requires=media-myuser-MyDiskLabel.mount media-myuser-MySecondDisk.mount
      ```

- Enregistrer le fichier, recharger systemd et redémarrer Docker :

    ```sh
   sudo systemctl daemon-reload  
   sudo systemctl restart docker
   ```

- Redémarrer le Raspberry Pi et vérifier que :

  - le disque est monté sur `/media/myuser/MyDiskLabel` ;
  - Docker démarre correctement après le montage :

    ```sh
    sudo systemctl status media-myuser-MyDiskLabel.mount
    sudo systemctl status docker
    ```

(voir [systemd.mount](https://www.freedesktop.org/software/systemd/man/systemd.mount.html)).
