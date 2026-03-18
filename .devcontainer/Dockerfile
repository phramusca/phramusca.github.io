# Dockerfile pour le dev container Jekyll
FROM mcr.microsoft.com/devcontainers/ruby:3.2

# Installer Rust et Cargo pour l'utilisateur vscode (utilisateur par défaut des dev containers)
USER vscode
WORKDIR /home/vscode

# Installer Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Installer lychee
RUN export PATH="$HOME/.cargo/bin:$PATH" && \
    cargo install lychee && \
    rm -rf $HOME/.cargo/registry/cache

# Retourner à root pour les configurations système
USER root

# Ajouter cargo au PATH pour tous les utilisateurs
ENV PATH="${PATH}:/home/vscode/.cargo/bin"

# Mettre à jour le PATH dans le profil bash pour tous les utilisateurs
RUN echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> /etc/bash.bashrc && \
    echo 'export PATH="/home/vscode/.cargo/bin:$PATH"' >> /etc/bash.bashrc

