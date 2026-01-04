---
layout: content
excerpt: Jouer en VR avec un casque Meta Quest 2 et un volant ThrusthMaster T150, à l'aide de SteamVR et ALVR.
title: Jouer en VR avec un Quest 2 et un volant
---

# Jouer en VR sur Steam

Comment jouer en VR sur Linux avec un casque Meta Quest 2 et un volant ThrusthMaster T150, à l'aide de SteamVR et ALVR.

Ce post est inspiré de ce [post reddit](https://www.reddit.com/r/linux_gaming/comments/1apuds8/my_setup_experience_with_meta_quest_2_on_linux/?tl=fr).

## Installation

- [Installer Steam](https://store.steampowered.com/about/), créer un compte, ...
  - Installer [SteamVR](https://store.steampowered.com/app/250820/SteamVR/?l=french)
  - Installer un jeu ou appli compatible VR, voir [les jeux](#les-jeux)
- Installer [ALVR](https://github.com/alvr-org/ALVR) sur le PC
  - ( Au besoin: [Installation Guide](https://github.com/alvr-org/ALVR/wiki/Installation-guide) et [Troubleshooting](https://github.com/alvr-org/ALVR/wiki/Linux-Troubleshooting) )
  - Télécharger [alvr_launcher_linux.tar.gz](https://github.com/alvr-org/ALVR/releases/latest/download/alvr_launcher_linux.tar.gz)
  - Dézipper
    - Dans un dossier qui ne contient que des caractères ASCII - anglais seulement - et pour lequel l'utilisateur a les droits d'écriture)
    - Pour ma part, j'ai copié `ALVR Launcher` sur le Bureau.
  - Double cliquer sur `ALVR Launcher`
    - Cliquer sur `Add version`
      - Cliquer sur `Install` (pour une installation par défaut garder `channel` et `version` tels quels)
      - Attendre la fin du téléchargement et de l'installation

- Installer ALVR sur le casque
  - Il faut d'abord activer le mode développeur pour pouvoir installer un apk:
    - [Créer une organisation](https://developer.oculus.com/manage/organizations/create/)
    - Sur l'appli Android `Meta Horizon` (téléphone ou tablette), connecter le casque (j'ai du effacer les données de l'appli pour pouvoir re-connecter le casque), Choisir `Paramètres du casque`, puis `Mode développeur` et activer le mode.
  - Ensuite, connecter le casque en USB-C (sur le casque directement, sans l'extension de batterie !) au PC.
  - Sur le casque, cliquer sur la notification `USB détécté`, puis `Autoriser` le débogage USB.
  - Sur le PC, lancer `ALVR Launcher`
    - Cliquer sur `Install APK`
    - Attendre la fin de l'installation
  - Déconnecter le casque de l'USB (plus besoin)
  - Sur le casque:
    - L'appli devrait apparaitre dans la bibliothèque, dans `Sources inconnues`
    - lancer `ALVR` si pas fait tout seul
  - Sur le PC, dans `ALVR Launcher`, cliquer sur `Launch`
    - Dans `Installation`, lancer `Run setup wizard` (surtout pour ajouter le règles de firewall), puis `Register ALVR driver`.
    - Cliquer sur `Launch SteamVR` et attendre qu'il soit lancé et connecté à ALVR
    - Dans `Devices`, un appareil devrait apparaitre dans `New Wireless Devices` (le casque doit etre actif). Cliquer sur `Trust`
  - Il faut redémarrer SteamVR pour qu'il puisse enregistrer le pilote. Ensuite, ça devrait marcher.

> Il est possible qu'il faille redemarrer le PC et ou le casque à un ou plusieurs moments, mais je ne sais plus quand...

## Lancer un jeu  

- Double cliquer sur `ALVR Launcher`
  - Cliquer sur `Launch`
  - Cliquer sur `Launch SteamVR`
- Mettre le casque et jouer
  - Le menu Oculus se fait avec la manette droite
  - Le menu SteamVR avec la gauche

> Penser à régler la sortie audio et le micro de Linux vers le casque

### Les jeux

Voici les jeux que j'ai pu essayer. Tous ne marchent pas mais seulement 2 sur 7 pour le moment.

Se référer à la base [protondb.com](https://www.protondb.com) pour connaitre la compatibilité pour d'autres jeux.

|                                                                                                     |                                  |            |
| --------------------------------------------------------------------------------------------------- | -------------------------------- | ---------- |
| Nom                                                                                                 | Description                      | Fonctionne |
| [Google Earth VR](https://store.steampowered.com/app/348250/Google_Earth_VR/)                       | Gratuit                          | ✅         |
| [Epic Roller Coasters](https://store.steampowered.com/app/787790/Epic_Roller_Coasters/)             | Gratuit                          | ✅         |
| [The Lab](https://store.steampowered.com/app/450390/The_Lab/)                                       | Gratuit                          | ✅         |
| [Adventure Climb VR](https://store.steampowered.com/app/1040430/Adventure_Climb_VR/)                | Gratuit                          | ❌         |
| [RaceRoom_Racing_Experience](https://store.steampowered.com/app/211500/RaceRoom_Racing_Experience/) | Gratuit                          | ❌         |
| [DiRT Rally 2.0](https://store.steampowered.com/app/690790/DiRT_Rally_20/)                          | Payant mais top avec un volant ! | ✅         |
| [Half-Life Alyx](#half-life-alyx)                                                                   | Payant                           | ✅         |
|                                                                                                     |                                  |            |

#### Half-Life Alyx

Workaround (fix sous-titres): <https://www.protondb.com/app/546560>

Il faut créer 2 liens symboliques entièrement en minuscule, car le jeu s'attend à ça.

- Passer le dossier Steam en minuscule

```bash
ln -sv ~/.local/share/Steam ~/.local/share/steam
```

- Passer le dossier du jeu en minuscule aussi

  ```bash
  ln -sv /path/to/steamapps/common/Half-Life\ Alyx /path/to/steamapps/common/half-life\ alyx
  ```

  - Dans mon cas:

  ```bash
  ln -sv /steam-games/steamapps/common/Half-Life\ Alyx /steam-games/steamapps/common/half-life\ alyx
  ```

### Volant

Le ThrusthMaster T150ThrusthMaster T150 doit être en mode `PS3` pour fonctionner sous PC.

[Oversteer](https://github.com/berarma/oversteer?tab=readme-ov-file). Indispensable ? En tout cas permet de tester son volant.
