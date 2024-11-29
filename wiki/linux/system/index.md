---
layout: default
---

# Système

TODO : Faire de cette page le README for Système !!

- [Système de Fichiers](system/Système_de_Fichiers)
  - [Système](system/Système)
  - [Réseau](Réseau)
  - [Waydroid](Waydroid)

ET ci-dessous:

---------------------------------------------------------

## Applications par défaut et menu

*A développer*

- ~/.local/share/applications : contient les raccourcis
- [doc Gnome pour le
  menu](http://library.gnome.org/admin/system-admin-guide/stable/menustructure-0.html.fr)
  - ~/.config/menus/applications.menu : le fichier de configuration du
    menu (préférer l'édition par [1](apt://alacarte))
- [doc Gnome pour
  MIME](http://library.gnome.org/admin/system-admin-guide/stable/mimetypes-0.html.fr)
- /etc/gnome/defaults.list : applications par défaut pour gnome
- <http://blog.vucica.net/2009/05/debianubuntu-gnome-restoring-nautilus-as-default-folder-viewer-opener.html>
- ... a compléter !!

- <http://forum.ubuntu-fr.org/viewtopic.php?pid=7036991>

## Lancement programmes au démarrage

Pour lancer des programmes au démarrage d'[Ubuntu](linux/dist/Ubuntu)
et/ou pour gérer les sessions (restauration de session), aller à Système
→ Préférences → Sessions

## Sudo

- sudo permet de lancer des commandes en root sans ouvrir de session
  root
- Le mot de passe root (le même que le user courant ayant les droits
  admin) est demandé à chaque fois, avec un timeout
- [sudo sur ubuntu-fr](http://doc.ubuntu-fr.org/sudo)
- gksudo, en mode graphique est préférable
- Se déconnecter sans attendre le timeout: sudo -k
- Configuration: sudo visudo ([sudoers sur
  ubuntu-fr](http://doc.ubuntu-fr.org/sudoers))
- [Explications en anglais
  ubuntu.com](https://help.ubuntu.com/community/Sudoers)
  - Exemple: permettre de monter des disques Samba (rajouter à la fin du
    fichier):

```sh
#Samba mount
Cmnd_Alias MOUNT = /bin/mount,/bin/umount,/sbin/mount.cifs,/sbin/umount.cifs
ALL ALL = NOPASSWD: MOUNT
```

## Icônes

Les icônes se trouvent ici : /usr/share/icons/

## Benchmark

Un benchmark est un logiciel qui teste les capacités d'un PC

- pi : Lancer

`./pi 20`

[ftp://pi.super-computing.org/Linux/super_pi.tar.gz](ftp://pi.super-computing.org/Linux/super_pi.tar.gz)

- geekbenchmark : <http://www.primatelabs.ca/geekbench/index.html>

[Mes Résultats](Mes_Résultats)

## Reprendre une installation

`dpkg --configure -a`

## Alias bash

Pour faire un alias de bash, par exemple ll remplaçant ls -la, il faut
dé-commenter la ligne correspondante dans ~/.bashrc

Ensuite, relancer le bash avec la commande exec bash

[Liste non exhaustive d'alias](http://forum.ubuntu-fr.org/viewtopic.php?id=20437)

## Clavier

### Pavé numérique

Si le clavier numérique ne marche plus, c'est peut être que l'option
"guider la souris avec le pad numérique" a été activée. Pour la
désactiver, aller dans le menu préférences\>clavier ou via le raccourci
Ctrl+Shift+NumLock.

### Accents perdus

<http://forum.ubuntu-fr.org/viewtopic.php?id=362479>

## Souris

Pour configurer les boutons supplémentaires d'une souris:
<https://les-enovateurs.com/parametrer-bouton-de-souris-ubuntu>

Pour MX Master:

- Installation

  ```sh
  sudo apt-get install xbindkeys xautomation x11-utils 
  xbindkeys --defaults > $HOME/.xbindkeysrc
  ```

- Identifier les boutons
  
  ```sh
  xev -event mouse | grep Button --before-context=1 --after-context=2
  ```

- Modifier la configuration

  ```sh
  xed $HOME/.xbindkeysrc
  ```

  - Left button

      ```sh
      # Left button: previous
      "xte 'keydown Alt_L' 'key Left' 'keyup Alt_L'"
      b:8
      ```
  
  - Other left button: next

      ```sh
      # Other left button: next
      "xte 'keydown Alt_L' 'key Right' 'keyup Alt_L'"
      b:9
      ```

  - Thumb wheel scroll left

    ```sh
    # Thumb wheel scroll left
    "xte 'keydown Control_L' 'key Left' 'keyup Control_L'"
    b:6
    ```

  - Thumb wheel scroll right

    ```sh
    # Thumb wheel scroll right
    "xte 'keydown Control_L' 'key Right' 'keyup Control_L'"
    b:7
    ```

- Relancer:

  ```sh
  xbindkeys -p
  ```

------------------------------------------------------------------------

Retour à [Misc](Misc)
