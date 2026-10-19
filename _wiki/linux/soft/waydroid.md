---
layout: software
---

# Waydroid

[Waydroid](https://waydro.id/) permet de lancer des applications Android mais nécessite un environnement Wayland.

> Pas facile à installer et à utiliser. Attendons que Wayland devienne le mode par défaut et remplace X11, comme c'est le cas sur Ubuntu depuis 26.04.

## Général

- Installation:  [https://waydro.id/#install](https://waydro.id/#install)
- Mise à jour: ```sudo waydroid upgrade```

## Lancer des applications

Le comportement diffère selon le mode de session choisi au démarrage de Linux Mint :

### Cinnamon on Wayland

> Encore en beta. Attendre que Wayland devienne le mode par défaut et remplace X11, comme c'est le cas sur Ubuntu depuis 26.04.

Double-cliquer sur `Jamuz android` sur le bureau, ou utiliser :

```console
waydroid app launch org.phramusca.jamuz
```

- Comment passer en mode fenêtré ?
- Comment passer le clavier en AZERTY (par défaut sur Cinnamon) ?
  - Aucune des solutions ci-dessous ne fonctionne :
    - pas d'onglet "Disposition" dans le menu "Clavier" des "Paramètres".
    - pas de résultat avec la ligne de commande ; `french` est pourtant sélectionné par défaut et il n'y a pas d'erreur à l'exécution, mais le clavier reste en QWERTY.
  - [https://www.numetopia.fr/comment-changer-la-disposition-du-clavier-dans-linux-mint/#changer_dispo_clavier_en_cli](https://www.numetopia.fr/comment-changer-la-disposition-du-clavier-dans-linux-mint/#changer_dispo_clavier_en_cli)

### Cinnamon (default; X11)

<https://waydro.id/#install>

Difficile à démarrer mais fonctionne parfois ; à préciser.

Une solution, depuis <https://github.com/waydroid/waydroid/issues/282> :

```console
sudo killall waydroid
sudo waydroid container start # Possiblement avec `&` à la fin.
waydroid session start # Dans un autre terminal, possiblement avec `&` à la fin.
```

Semble fonctionner, à clarifier.

Enfin ça marchait (voir dossier waydroid dans ce wiki) jusqu'au 15/2 après une mise à jour de waydroid effectuée dans Weston/waydroid

Depuis jamuz ne se lance plus :(

<https://www.apkmirror.com/>

<https://manpages.ubuntu.com/manpages/focal/en/man5/weston.ini.5.html#launcher%20section>

`sudo mount --bind ~/Documents ~/.local/share/waydroid/data/media/0/Documents`

### Weston

Ne pas utiliser. On ne peut ouvrir qu'une fenêtre de terminal, et je ne sais pas en sortir proprement sans utiliser la commande `reboot`.

## Anciens scripts et fichiers de configuration

Ces fichiers sont conservés comme archive de mon ancienne configuration. Vérifier
les chemins et les commandes avant de les utiliser sur une autre installation.

### `start.sh`

```sh
# weston -c ~/Bureau/Waydroid/weston.ini --width=412 --height=732 --socket=mysocket
weston -c ~/Bureau/Waydroid/weston.ini --width=1280 --height=1024 --socket=mysocket
```

### `restart.sh`

```sh
sudo killall waydroid
sudo waydroid container start &
waydroid session start &
sudo umount ~/.local/share/waydroid/data/media/0/Music
sudo mount --bind ~/Musique-BAK/Archive ~/.local/share/waydroid/data/media/0/Music
sh ./start.sh
```

### `weston.ini`

```ini
[keyboard]
keymap_layout=fr
numlock-on=true

[launcher]
icon=/usr/share/icons/Mint-X/apps/24/terminal.png
path=/usr/bin/weston-terminal

[launcher]
; icon=~/.local/share/waydroid/data/icons/org.phramusca.jamuz.png
icon=~/Bureau/Waydroid/org.phramusca.jamuz.png
path=/usr/bin/waydroid app launch org.phramusca.jamuz
```

### `JaMuz Android.desktop`

```ini
[Desktop Entry]
Type=Application
Name=JaMuz
Exec=waydroid app launch org.phramusca.jamuz
Icon=~/.local/share/waydroid/data/icons/org.phramusca.jamuz.png
Categories=X-WayDroid-App;
X-Purism-FormFactor=Workstation;Mobile;
Actions=app_settings;
Name[fr_FR]=JaMuz Android

[Desktop Action app_settings]
Name=App Settings
Exec=waydroid app intent android.settings.APPLICATION_DETAILS_SETTINGS package:org.phramusca.jamuz
```
