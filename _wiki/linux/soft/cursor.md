# Cursor

[Cursor](https://cursor.com/fr/) est un éditeur IA et un agent de programmation

## Installation

Comme indiqué dans la [documentation](https://cursor.com/docs/getting-started/installation), la méthode recommandée est d'utiliser le deb.

```bash
# Ajouter la clé GPG de Cursor
curl -fsSL https://downloads.cursor.com/keys/anysphere.asc | gpg --dearmor | sudo tee /etc/apt/keyrings/cursor.gpg > /dev/null

# Ajouter le dépôt Cursor
echo "deb [arch=amd64,arm64 signed-by=/etc/apt/keyrings/cursor.gpg] https://downloads.cursor.com/aptrepo stable main" | sudo tee /etc/apt/sources.list.d/cursor.list > /dev/null

# Mettre à jour et installer
sudo apt update
sudo apt install cursor
```

## Mise à jour

```bash
sudo apt update
sudo apt upgrade cursor
```

> En cas d'erreurs lors de apt upgrade, voir [Installing Cursor via APT deb package breaks apt update](https://forum.cursor.com/t/installing-cursor-via-apt-deb-package-breaks-apt-update/132008/16)

## AppImage

Il existe aussi une méthode pour installer Cursor via AppImage, mais elle est **déconseillée**.

Téléchargez le fichier .AppImage depuis cursor.com/downloads, puis :

```bash
chmod +x Cursor-*.AppImage
./Cursor-*.AppImage
```

Pour l'installation et la mise à jour, il est possible d'utiliser le script suivant:

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/hieutt192/Cursor-ubuntu/Cursor-ubuntu24.04/manage_cursor.sh)"
```

Script source: <https://github.com/hieutt192/Cursor-ubuntu/tree/Cursor-ubuntu24.04>
