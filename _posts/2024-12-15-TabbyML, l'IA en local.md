---
layout: default
excerpt: "TabbyML offre une expérience de codage AI enrichissante et personnalisable. En local."
title: "TabbyML, l'IA en local"
---

# TabbyML

[TabbyML](https://www.tabbyml.com/) offre une expérience de codage AI enrichissante et personnalisable. 

C'est "le concurrent open source du CoPilot de GitHub". Et ça tourne en local !

La suite détaille l'installation avec Docker (Compose) mais TabbyML peut aussi etre installé sur [Apple](https://tabby.tabbyml.com/docs/quick-start/installation/apple/), [Linux](https://tabby.tabbyml.com/docs/quick-start/installation/linux/) ou [Windows](https://tabby.tabbyml.com/docs/quick-start/installation/windows/).

## Installation

### Avec Docker

Pour tester rapidement, utiliser la commande docker:

- CPU seulement:

    ```shell
    docker run \                 
        --entrypoint /opt/tabby/bin/tabby-cpu \
        -it \
        -p 8080:8080 \
        -e LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/compat:$LD_LIBRARY_PATH \
        -v $HOME/.tabby:/data registry.tabbyml.com/tabbyml/tabby \   
        serve --device cpu --model StarCoder-1B --chat-model Qwen2-1.5B-Instruct
    ```
    
- Pareil, mais pour profiter du SSD (disque `/` dans mon cas). 
    - Nécessite d'aller dans `Settings / Ressources / File Sharing` (Docker Desktop) et ajouter `/.tabby` dans la liste des `Virtual file shares`. 
    - Mais c'est bien plus rapide !

    ```shell
    docker run \
    --entrypoint /opt/tabby/bin/tabby-cpu \
    -it \
    -p 8080:8080 \
    -e LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/compat:$LD_LIBRARY_PATH \
    -v /.tabby:/data  registry.tabbyml.com/tabbyml/tabby \
    serve --device cpu --model StarCoder-1B --chat-model Qwen2-1.5B-Instruct
    ```

- En montant le dossier des repos git pour pouvoir les ajouter dans Tabby comme fournisseur de contexte Git local.

    ```shell
    docker run \
    --entrypoint /opt/tabby/bin/tabby-cpu \
    -it \
    -p 8080:8080 \
    -e LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/compat:$LD_LIBRARY_PATH \
    -v /.tabby:/data \
    -v $HOME/Documents/04-Creations/Dev/Repos:/repos \
    registry.tabbyml.com/tabbyml/tabby \
    serve --device cpu --model StarCoder-1B --chat-model Qwen2-1.5B-Instruct
    ```

- Avec GPU, voir la doc: [Installation avec Docker](https://tabby.tabbyml.com/docs/quick-start/installation/docker/)

### Avec Docker Compose:

- Créer un fichier `docker-compose.yaml`:

    - CPU seulement:

    ```yaml
    version: '3.5'

    services:
        tabby:
            restart: unless-stopped
            image: registry.tabbyml.com/tabbyml/tabby
            entrypoint: /opt/tabby/bin/tabby-cpu
            command: serve --device cpu --model StarCoder-1B --chat-model Qwen2-1.5B-Instruct
            volumes:
                - "/.tabby:/data"
                - "$HOME/Documents/04-Creations/Dev/Repos:/repos"
            ports:
                - 8080:8080
            environment:
                - LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/compat:$LD_LIBRARY_PATH
    ```
    
    - Avec GPU, voir la doc: [Installation avec Docker Compose](https://tabby.tabbyml.com/docs/quick-start/installation/docker-compose/)
- Lancer TabbyML: `docker compose up -d`
   
## Configuration

 - Aller sur [http://localhost:8080/](http://localhost:8080/)
    - Créer un compte
    - *Optionnel*: [Ajouter un fournisseur de contexte Git local](https://tabby.tabbyml.com/docs/administration/context/#adding-a-repository-through-admin-ui) avec comme URL `file:///repos/MonRepoGit`
 - Installer l'extension pour [VSCode](https://tabby.tabbyml.com/docs/extensions/installation/vscode/), [intellij](https://tabby.tabbyml.com/docs/extensions/installation/intellij/) or [VIM](https://tabby.tabbyml.com/docs/extensions/installation/vim/), puis [configurer l'IDE](https://tabby.tabbyml.com/docs/quick-start/setup-ide/).
 
## Aller plus loin

- Avec une bonne machine, il est possible de passer sur des [modèles](https://tabby.tabbyml.com/docs/models/) plus performants
    - Essayer avec un GPU, car avec mon "AMD Ryzen 5 Pro 3400G" c'est lent, mais lent !
- [Créer un fichier de configuration](https://tabby.tabbyml.com/docs/extensions/configurations/) pour l'extension IDE.
    - Spécifiquement pour le [Code Completion](https://tabby.tabbyml.com/docs/administration/code-completion/)
    - La [configuration du modèle](https://tabby.tabbyml.com/docs/administration/model/)
- [Mise à jour](https://tabby.tabbyml.com/docs/administration/upgrade/):
    - [Faire une sauvegarde](https://tabby.tabbyml.com/docs/administration/backup/)
    - Télécharger la dernière image: `docker pull tabbyml/tabby`
    - Redémarrer le container
- [Faire une sauvegarde](https://tabby.tabbyml.com/docs/administration/backup/)
- [Configurer le SMTP](https://tabby.tabbyml.com/docs/administration/smtp/) pour l'envoi de mail aux utilisateurs