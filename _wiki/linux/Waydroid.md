---
layout: content
---

# Waydroid

[Waydroid](https://waydro.id/) permet de lancer des applications Android

## Général

- Installation:  [https://waydro.id/#install](https://waydro.id/#install)
- Mise à jour: ```sudo waydroid upgrade```

## Lancer des applications

Différent comportement selon le mode de session chois au démarrage de Linux Mint:

### Cinnamon on Wayland

Simply double-click "Jamuz android" on Desktop, or use:

```console
waydroid app launch org.phramusca.jamuz
```

- TODO: H2 have a windowed mode ?
- TODO: H2 change keyword to azerty as it is on cinnamon default ?
  - Aucune des solutions ci-dessous ne marche:
    - pas d'onglet "Disposition" dans menu "Clavier" des "Paramètres.
    - pas de résultat avec la ligne de commande, french est pourtant selectionné par défaut et il n'y a pas d'erreur à l'execution, mais toujours en qwerty
  - [https://www.numetopia.fr/comment-changer-la-disposition-du-clavier-dans-linux-mint/#changer_dispo_clavier_en_cli](https://www.numetopia.fr/comment-changer-la-disposition-du-clavier-dans-linux-mint/#changer_dispo_clavier_en_cli)

### Cinnamon (default)

=> TODO: Revoir cette partie

<https://waydro.id/#install>

Hard to start but works somehow, need to find out how ?

A solution, from <https://github.com/waydroid/waydroid/issues/282>

```console
sudo killall waydroid
sudo waydroid container start # Possibly could use `&` at the end.
waydroid session start # In separate terminal, possibly could use `&` at the end.
```

seem to work, to be clarified

<https://www.apkmirror.com/>

<https://manpages.ubuntu.com/manpages/focal/en/man5/weston.ini.5.html#launcher%20section>

`sudo mount --bind ~/Documents ~/.local/share/waydroid/data/media/0/Documents`

### Weston

Do not use this. You can only open a terminal window and I do not know to escape from this unless using `reboot` command.
