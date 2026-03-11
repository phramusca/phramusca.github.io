---
layout: content
---

# Terminal

## Pimp My Terminal

Source: [Pimp My Terminal](https://stackabuse.com/pimp-my-terminal-an-introduction-to-oh-my-zsh/)

- Installer [zsh](https://doc.ubuntu-fr.org/zsh)

    ```shell
    sudo apt install zsh
    ```

- Passer sous zsh

    ```shell
    chsh -s $(which zsh)
    ```

- Installer [Oh My Zsh](https://ohmyz.sh/)

    ```shell
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
    ```

- Installer le thème [powerlevel10k](https://github.com/romkatv/powerlevel10k#oh-my-zsh) (Plus maintenu. TODO: trouver alternative parmis les autres [thèmes](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes))

  - Installer la famille de police [MesloLGS NF](https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#meslo-nerd-font-patched-for-powerlevel10k)

    - WSL / Windows: Installer les polices sous Windows, avec double-click
    - Linux: Installer les polices avec double-click
    - Raspberry:
  
        ```shell
        mkdir ~/.local/share/fonts/
        cp Téléchargements/MesloLGS\ NF\ Bold\ Italic.ttf ~/.local/share/fonts/
        cp Téléchargements/MesloLGS\ NF\ Bold.ttf ~/.local/share/fonts/
        cp Téléchargements/MesloLGS\ NF\ Italic.ttf ~/.local/share/fonts/
        cp Téléchargements/MesloLGS\ NF\ Regular.ttf ~/.local/share/fonts/
        fc-cache -fv
        fc-list | grep "Meslo"
        ```

  - Configurer les terminaux (Windows Terminal, Tilix, ...) et outils (VSCode, ...) pour [utiliser cette famille de polices](https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#manual-font-installation)
  - Installer powerlevel10k

    ```shell
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
    ```

  - Configurer `zsh` pour utiliser ce thème:

    ```shell
    nano ~/.zshrc
    ```

    - Find the line that sets ZSH_THEME, and change its value to "powerlevel10k/powerlevel10k".
    - Open a new terminal session, and follow the p10k configuration wizard.

- Installer des plugins non-officiels, comme:
  - [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlightinghttps://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md#oh-my-zsh)

    ```shell
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
    ```

  - [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh)

    ```shell
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    ```

- Installer des [plugins officiels](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins) comme:

  | Plugin                                                                | Description                                                                                                                                                                                      |
  | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | [git](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git)     | Ce plugin est un ensemble d’alias prédéfinis pour accélérer l’utilisation de Git dans le terminal. Par exemple : `gst` au lieu de `git status`, `ga` au lieu de `git add`, etc.                  |
  | [sudo](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/sudo)   | Ce plugin permet d’ajouter `sudo` en préfixe de la commande courante ou précédente en appuyant deux fois sur `ESC`.                                                                              |
  | [z](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/z)         | Ce plugin améliore la productivité en permettant de naviguer rapidement dans l’arborescence. Il garde une trace des répertoires les plus visités et permet d’y accéder avec quelques caractères. |
  | [aws](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/aws)     | Ce plugin fournit la complétion pour awscli v2 et quelques utilitaires pour gérer les profils/régions AWS et les afficher dans l’invite.                                                         |
  | [azure](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/azure) | Ce plugin fournit la complétion pour Azure CLI et quelques utilitaires pour gérer les abonnements Azure et les afficher dans l’invite.                                                           |

- Activer les plugins en éditant `nano ~/.zshrc`

    ```text
    plugins = (git z sudo zsh-syntax-highlighting zsh-autosuggestions)
    ```

- Relancer le terminal pour profiter des plugins.

    > Note: Sous raspberry, avec lxterminal, il faut redémarrer le raspberry pour qu'il démarre avec zsh par défaut.

> Un [CheatSheet](https://github.com/ohmyzsh/ohmyzsh/wiki/Cheatsheet) avec notamment les alias
