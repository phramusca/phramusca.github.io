---
layout: content
---

# Waydroid

[Waydroid](https://waydro.id/) permet de lancer des applications Android mais nécessite un environnement Wayland.

> Pas facile à installer et à utiliser. Attendons que Wayland devienne le mode par défaut et remplace X11, comme c'est le cas sur Ubuntu depuis 26.04.

TODO: Que faire du contenu du dossier _wiki/linux/waydroid ?

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
