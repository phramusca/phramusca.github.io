---
layout: default
---

# Docker

Voici quelques programmes que j'utilise avec Docker.

## Portainer CE

[Doc installation docker linux](https://docs.portainer.io/start/install-ce/server/docker/linux)

En résumé:
  
-  Créer un volume pour le stockage de la base de données:

    `docker volume create portainer_data`

- Télécharger et installer Portainer CE:

    `docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:2.21.5`

- Naviguer vers [https://localhost:9443](https://localhost:9443) et suivre la procédure d'installation.

## Forjero

[Doc installation](https://forgejo.org/docs/latest/admin/installation-docker/)

```yaml
services:
  forgejo:
    image: codeberg.org/forgejo/forgejo:9.0.0
    container_name: forgejo
    restart: unless-stopped
    volumes:
      - ${VOLUME_PATH}/forgejo/data:/data/gitea
    ports:
      - 3000:3000
```

with `.env` file:

```ini
  VOLUME_PATH="/chemin/avec des espaces"
```

## Lazy Docker

[Doc installation](https://github.com/jesseduffield/lazydocker?tab=readme-ov-file#docker)

Pour Raspberry Pi 5:

```yaml
version: '3'
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

## Romm

[Doc installation](https://github.com/rommapp/romm/wiki/Quick-Start-Guide)

```yaml
version: "3"

volumes:
  mysql_data:

services:
  romm:
    image: rommapp/romm:3.7.2
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
    # image: mariadb:latest # if you experience issues, try: linuxserver/mariadb:latest
    image: linuxserver/mariadb:latest
    container_name: romm-db
    restart: unless-stopped
    environment:
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} # Use a unique, secure password
      - MYSQL_DATABASE=romm
      - MYSQL_USER=romm-user
      - MYSQL_PASSWORD=${DB_PASSWD}
    volumes:
      - mysql_data:/var/lib/mysql  #Cannot change. Folder user is 911, cannot see files, and if chown, docker crashes with db connection
```

with `.env` file:

```ini
VOLUME_PATH="/chemin/avec des espaces"
DB_PASSWD=
MYSQL_ROOT_PASSWORD=
TH_SECRET_KEY=
IGDB_CLIENT_ID=
IGDB_CLIENT_SECRET=
MOBYGAMES_API_KEY=
STEAMGRIDDB_API_KEY=
```
