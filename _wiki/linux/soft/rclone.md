---
layout: software
---

# rclone

[rclone](https://rclone.org/) est un outil en ligne de commande pour gérer des fichiers locaux et des espaces de stockage en ligne.

## Tiers des backends

Les tiers indiquent le niveau de maturité et de prise en charge des backends rclone :

| Tier | Niveau       | Signification                                                         |
| ---- | ------------ | --------------------------------------------------------------------- |
| 1    | Core         | Production, backend de premier plan                                   |
| 2    | Stable       | Bien pris en charge, avec quelques lacunes mineures                   |
| 3    | Supported    | Fonctionne dans de nombreux cas, avec des réserves connues            |
| 4    | Experimental | Expérimental : utilisation prudente, lacunes ou changements possibles |
| 5    | Deprecated   | Obsolète : plus maintenu ni pris en charge                            |

Par exemple, **Proton Drive est classé Tier 4** : faites d'abord des essais avec des données non critiques et conservez une copie de sauvegarde. Voir la [définition officielle des tiers](https://rclone.org/tiers/).

## Mettre à jour rclone sous Linux Mint

La version des dépôts APT peut être ancienne. Par exemple, le backend Proton Drive nécessite rclone 1.64.0 ou plus récent. La version actuellement utilisée se vérifie avec :

```console
rclone version
```

### Depuis une version récente de rclone

À partir de rclone 1.55, la commande `selfupdate` permet d'installer la dernière version stable. Sur Linux Mint, dérivé d'Ubuntu/Debian, utiliser le format `deb` :

```console
sudo rclone selfupdate --package deb
```

Pour vérifier la version installable sans effectuer la mise à jour :

```console
rclone selfupdate --check
```

### Si `selfupdate` n'est pas disponible

Utiliser la procédure officielle d'installation pour Linux :

```console
sudo -v && curl https://rclone.org/install.sh | sudo bash
```

Cette méthode installe la version stable actuelle.

La mise à jour du programme ne supprime normalement pas la configuration de l'utilisateur, stockée dans `~/.config/rclone/rclone.conf`.

### Documentation officielle

- [Installation de rclone](https://rclone.org/install/)
- [Commande `rclone selfupdate`](https://rclone.org/commands/rclone_selfupdate/)
