---
layout: software
---

# rsync

[rsync](https://doc.ubuntu-fr.org/rsync) (pour remote synchronization ou synchronisation à distance) est un logiciel de synchronisation de fichiers.

[Grsync](http://doc.ubuntu-fr.org/grsync) est une interface graphique pour la commande [rsync](https://doc.ubuntu-fr.org/rsync).

## Exclude files/folders

[rsync man](http://www.delafond.org/traducmanfr/man/man1/rsync.1.html)

```console
--exclude-from=FICHIER
   Cette option est similaire à l'option --exclude, mais ajoute les motifs d'exclusion listés dans le fichier FICHIER
à la liste d'exclusion. Les lignes vides dans FICHIER ou les lignes commençant par «;» ou par «#» sont ignorées.
Si FICHIER est - alors la liste sera lue depuis l'entrée standard.
```

Example de `FICHIER`:

```sh
#- **/.git
#- **/app/build/
#- **/.idea
#- **/.gradle
- **/Repos
```
