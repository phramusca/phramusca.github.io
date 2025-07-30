---
layout: default
---

# Docker

J'utilise [Docker](https://www.docker.com/) pour faire tourner quelques services sur mon Raspberry Pi.

## Docker Compose

### Portainer CE

[Doc installation docker linux](https://docs.portainer.io/start/install-ce/server/docker/linux)

En résumé:
  
-  Créer un volume pour le stockage de la base de données:

    `docker volume create portainer_data`

- Télécharger et installer Portainer CE:

    `docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:2.21.5`

- Naviguer vers [https://localhost:9443](https://localhost:9443) et suivre la procédure d'installation.

### Forgejo

[Doc installation](https://forgejo.org/docs/latest/admin/installation-docker/)

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

with `.env` file:

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

   - Changer l’URL du remote Git :

     ```bash
     git remote set-url origin git@forgejo:phramusca/taratata-downloader.git
     ```

   - Ajouter la clé publique du client dans l’interface web Forgejo (Settings > SSH Keys).

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

[Doc installation](https://github.com/jesseduffield/lazydocker?tab=readme-ov-file#docker)

Pour Raspberry Pi 5:

```yaml
services:
  lazydocker:
    build:
      context: https://github.com/jesseduffield/lazydocker.git
      args:
        BASE_IMAGE_BUILDER: golang
        GOARCH: amd64
        GOARM:
    image: lazyteam/lazydocker
    container_name: lazydocker
    stdin_open: true
    tty: true
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ${VOLUME_PATH}/lazydocker/config:/.config/jesseduffield/lazydocker
```

with `.env` file:

```ini
  VOLUME_PATH="/chemin/avec des espaces"
```

Then launch it using:

```sh
docker exec -it lazydocker lazydocker
```

### Romm

[Doc installation](https://github.com/rommapp/romm/wiki/Quick-Start-Guide)

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
      - DB_NAME=romm # Should match MYSQL_DATABASE in mariadb
      - DB_USER=romm-user # Should match MYSQL_USER in mariadb
      - DB_PASSWD=${DB_PASSWD} # Should match MYSQL_PASSWORD in mariadb
      - ROMM_AUTH_SECRET_KEY=${ROMM_AUTH_SECRET_KEY} # Generate a key with `openssl rand -hex 32`
      - IGDB_CLIENT_ID=${IGDB_CLIENT_ID} # Generate an ID and SECRET in IGDB
      - IGDB_CLIENT_SECRET=${IGDB_CLIENT_SECRET} # https://api-docs.igdb.com/#account-creation
      - MOBYGAMES_API_KEY=${MOBYGAMES_API_KEY} # https://www.mobygames.com/info/api/
      - STEAMGRIDDB_API_KEY=${STEAMGRIDDB_API_KEY} # https://github.com/rommapp/romm/wiki/Generate-API-Keys#steamgriddb
    volumes:
      - ${VOLUME_PATH}/cache/romm_resources:/romm/resources # Resources fetched from IGDB (covers, screenshots, etc.)
      - ${VOLUME_PATH}/cache/romm_redis_data:/redis-data # Cached data for background tasks
      - ${VOLUME_PATH}/library:/romm/library # Your game library
      - ${VOLUME_PATH}/assets:/romm/assets # Uploaded saves, states, etc.
      - ${VOLUME_PATH}/config:/romm/config # Path where config.yml is stored
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
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} # Use a unique, secure password
      - MYSQL_DATABASE=romm
      - MYSQL_USER=romm-user
      - MYSQL_PASSWORD=${DB_PASSWD}
    volumes:
      - ${VOLUME_PATH}/mariadb/config:/config
```

with `.env` file:

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

## Monter un disque externe avant de lancer docker

J'utilise un disque externe pour stocker les données des services docker. Pour être sûr que le disque est monté avant de lancer docker, il faut créer un fichier d'unité `.mount` pour gérer le montage de votre disque externe. Voici les étapes pour le faire :

- Identifier l'UUID du disque USB :
   
  ```sh
  lsblk -o NAME,UUID,MOUNTPOINT
  ```
   - Notez l'UUID du disque correspondant.

- Créer un fichier d'unité systemd `.mount` pour gérer le montage de votre disque :  

  ```sh
  sudo nano /etc/systemd/system/media-myuser-MAXTOR.mount
  ```
   
   - Ajoutez-y le contenu suivant, en remplaçant `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` par l'UUID de votre disque :  

      ```toml
      [Unit]  
      Description=Mount MAXTOR USB Drive  
      Before=docker.service  

      [Mount]  
      What=/dev/disk/by-uuid/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  
      Where=/media/myuser/MAXTOR  
      Type=ext4  
      Options=defaults  

      [Install]  
      WantedBy=multi-user.target
      ```

- Créer le répertoire de montage :  
   
   ```sh
   sudo mkdir -p /media/myuser/MAXTOR
   sudo chown myuser:myuser /media/myuser/MAXTOR
   ```

- Recharger la configuration de `systemd` et activer l'unité
   
   ```sh
   sudo systemctl daemon-reload
   sudo systemctl enable media-myuser-MAXTOR.mount
   sudo systemctl start media-myuser-MAXTOR.mount
  ```

- Vérifier que le montage fonctionne:
   
   ```sh
   sudo systemctl status media-myuser-MAXTOR.mount
   ls /media/myuser/MAXTOR
  ```

- Configurer Docker pour attendre le montage :  
   
   ```sh
   sudo systemctl edit docker.service
   ```
   
   - Ajoutez les lignes suivantes :  

      ```toml
      [Unit]  
      After=media-myuser-MAXTOR.mount  
      Requires=media-myuser-MAXTOR.mount  
      ```

- Sauvegardez, rechargez et redémarrez Docker-  :  

    ```sh
   sudo systemctl daemon-reload  
   sudo systemctl restart docker
   ```

- Redémarrez votre Raspberry Pi et vérifiez que :  
   - Le disque est monté sur `/media/myuser/MAXTOR`  
   - Docker démarre correctement après le montage-  :  
   
   ```sh
   sudo systemctl status media-myuser-MAXTOR.mount
   sudo systemctl status docker
   ```