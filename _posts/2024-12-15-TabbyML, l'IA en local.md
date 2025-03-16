---
layout: default
excerpt: TabbyML offre une expérience de codage AI enrichissante et personnalisable. En local.
title: TabbyML, l'IA en local
---

# TabbyML

[TabbyML](https://www.tabbyml.com/) offre une expérience de codage AI enrichissante et personnalisable. 

C'est "le concurrent open source du CoPilot de GitHub". Et ça tourne en local !

La suite détaille l'installation avec Docker (Compose) mais TabbyML peut aussi etre installé sur [Apple](https://tabby.tabbyml.com/docs/quick-start/installation/apple/), [Linux](https://tabby.tabbyml.com/docs/quick-start/installation/linux/) ou [Windows](https://tabby.tabbyml.com/docs/quick-start/installation/windows/).

## Installation

Pour profiter du GPU (fortement recommandé), il faut d'abord installer NVIDIA Container Toolkit.

1. Désinstallation de Docker Desktoop (optionnel)
    
    ```bash
    sudo apt-get remove docker-desktop
    sudo rm -rf ~/.docker /var/lib/docker
    sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    sudo apt-get autoremove
    ```
    
2. Installation de NVIDIA Container Toolkit

    - Installez les outils nécessaires :

    ```bash
    sudo apt-get update
    sudo apt-get install -y software-properties-common
    ```

    - Ajoutez le dépôt NVIDIA :

    ```bash
    distribution=$(
    . /etc/os-release
    echo $ID$VERSION_ID
    )
    sudo curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
    curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list |
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' |
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
    sudo apt-get update
    ```

    - Installez NVIDIA Container Toolkit :

    ```bash
    sudo apt-get install -y nvidia-container-toolkit
    ```

    - Configurez le runtime Docker :

    ```bash
    sudo nvidia-ctk runtime configure --runtime=docker
    sudo systemctl restart docker
    ```

3. Test avec NVIDIA SMI

    ```bash
    sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
    ```

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

    ```yaml
    services:
        tabby:
            restart: unless-stopped
            image: registry.tabbyml.com/tabbyml/tabby
            command: serve --model Qwen2.5-Coder-1.5B --chat-model Qwen2.5-Coder-1.5B-Instruct --device cuda
            volumes:
                    - "/.tabby:/data"
                    - "$HOME/Documents/04-Creations---ICI/Dev --- ICI/Repos:/repos"
            ports:
            - 8086:8080
            deploy:
            resources:
                reservations:
                devices:
                    - driver: nvidia
                    count: 1
                    capabilities: [gpu]
    ```

- Lancer TabbyML: `docker compose up -d`

- Aller à `http://localhost:8086` et suivre les instructions pour créer le compte admin.

- Pour mettre à jour:

    ```bash
    docker compose pull
    docker compose up -d --force-recreate
    ```
    
- Pour voir les logs (ça peut etre long à démarrer):

    ```bash
    docker logs tabby-tabby-1 -f
    ```

#### Configurations

Je n'ai pas une carte graphique surpuissante et surtout elle n'a que 8Go de RAM.

Donc, je ne peux utiliser les versions 7 ni 13, à moins de faire  des réglages, comme suggéré par ChatGPT mais non testé:

- 4-bit or 8-bit quantization to reduce VRAM usage.
- Use GGUF/GGML models optimized for lower memory consumption.
- Offload part of the model to CPU/RAM if needed (but expect slower response times).

Voici ma configuration et les modèles testés:

- Carte Graphique: Nvidia RTX 4060
- RAM: 16 Go
- Processeur: Ryzen 7 5700X

| type       | B  | Model ID                    | License                           | Type Licence        |  Pays            |  Propriétaire                   | status   |
|------------|----|-----------------------------|-----------------------------------|---------------------|------------------|---------------------------------|----------|
| chat-model | 5  | Qwen2-1.5B-Instruct         | Apache 2.0                        | Open source         | Chine            | Alibaba Cloud                   | ok       |
| chat-model | 5  | Qwen2.5-Coder-0.5B-Instruct | Apache 2.0                        | Open source         | Chine            | Alibaba Cloud                   | ok       |
| chat-model | 5  | Qwen2.5-Coder-1.5B-Instruct | Apache 2.0                        | Open source         | Chine            | Alibaba Cloud                   | ok       |
| chat-model | 7  | CodeGemma-7B-Instruct       | Gemma License                     | Propriétaire        | États-Unis       | Google DeepMind                 | bug      |
| chat-model | 7  | CodeQwen-7B-Chat            | Tongyi Qianwen License            | Propriétaire        | Chine            | Alibaba Cloud                   | bug      |
| chat-model | 7  | Mistral-7B                  | Apache 2.0                        | Open source         | France           | Mistral AI                      | bug      |
| chat-model | 7  | Qwen2.5-Coder-7B-Instruct   | Apache 2.0                        | Open source         | Chine            | Alibaba Cloud                   | bug      |
| chat-model | 9  | Yi-Coder-9B-Chat            | Apache 2.0                        | Open source         | Chine            | 01.AI                           | bug      |
| chat-model | 14 | Qwen2.5-Coder-14B-Instruct  | Apache 2.0                        | Open source         | Chine            | Alibaba Cloud                   | bug      |
| chat-model | 22 | Codestral-22B               | Mistral AI Non-Production License | Propriétaire        | France           | Mistral AI                      | bug      |
| chat-model | 32 | Qwen2.5-Coder-32B-Instruct  | Apache 2.0                        | Open source         | Chine            | Alibaba Cloud                   | bug      |
| model      | 1  | StarCoder-1B                | BigCode-OpenRAIL-M                | Open source éthique | International    | BigCode (Hugging Face)          | ok       |
| model      | 2  | CodeGemma-2B                | Gemma License                     | Propriétaire        | États-Unis       | Google DeepMind                 | ok       |
| model      | 3  | DeepseekCoder-1.3B          | Deepseek License                  | Propriétaire        | Chine            | DeepSeek                        | ok       |
| model      | 3  | Qwen2.5-Coder-3B            | Apache 2.0                        | Open source         | Chine            | Alibaba Cloud                   | ok       |
| model      | 3  | StarCoder-3B                | BigCode-OpenRAIL-M                | Open source éthique | International    | BigCode (Hugging Face)          | ok       |
| model      | 3  | StarCoder2-3B               | BigCode-OpenRAIL-M                | Open source éthique | International    | BigCode (Hugging Face)          | ok       |
| model      | 5  | Qwen2.5-Coder-0.5B          | Apache 2.0                        | Open source         | Chine            | Alibaba Cloud                   | ok       |
| model      | 5  | Qwen2.5-Coder-1.5B          | Apache 2.0                        | Open source         | Chine            | Alibaba Cloud                   | ok       |
| model      | 7  | CodeGemma-7B                | Gemma License                     | Propriétaire        | États-Unis       | Google DeepMind                 | bug      |
| model      | 7  | CodeLlama-7B                | Llama 2                           | Propriétaire        | États-Unis       | Meta                            | bug      |
| model      | 7  | CodeQwen-7B                 | Tongyi Qianwen License            | Propriétaire        | Chine            | Alibaba Cloud                   | bug & ok |
| model      | 7  | DeepseekCoder-6.7B          | Deepseek License                  | Propriétaire        | Chine            | DeepSeek                        | bug      |
| model      | 7  | Qwen2.5-Coder-7B            | Apache 2.0                        | Open source         | Chine            | Alibaba Cloud                   | bug      |
| model      | 7  | StarCoder-7B                | BigCode-OpenRAIL-M                | Open source éthique | International    | BigCode (Hugging Face)          | bug      |
| model      | 7  | StarCoder2-7B               | BigCode-OpenRAIL-M                | Open source éthique | International    | BigCode (Hugging Face)          | bug      |
| model      | 13 | CodeLlama-13B               | Llama 2                           | Propriétaire        | États-Unis       | Meta                            | bug      |
| model      | 14 | Qwen2.5-Coder-14B           | Apache 2.0                        | Open source         | Chine            | Alibaba Cloud                   | bug      |
| model      | 22 | Codestral-22B               | Mistral AI Non-Production License | Propriétaire        | France           | Mistral AI                      | bug      |
| model      | ?  | DeepSeek-Coder-V2-Lite      | Deepseek License                  | Propriétaire        | Chine            | DeepSeek                        | bug      |

> "bug" réfère à [ce bug](https://github.com/TabbyML/tabby/issues/2803), [ce bug](https://github.com/TabbyML/tabby/issues/3512) ou [ce bug](https://github.com/TabbyML/tabby/issues/3056). Mais c'est surtout que ma machine n'est pas assez puissante.

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