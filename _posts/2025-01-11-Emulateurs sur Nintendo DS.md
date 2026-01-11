---
layout: content
excerpt: Utiliser Kekatsu et Romm pour télécharger des émulateurs et des roms sur Nintendo DS
title: Emulateurs de jeux pour Nintendo DS
---

# Emulateurs de jeux pour Nintendo DS

## Installation

- Télécharger le [R4iSDHC kernel](http://www.r4i-sdhc.com/downloade.asp) qui correpond.
  - Pour moi, c'est le [R4SDHC DUAL CORE Download](http://www.r4i-sdhc.com/download/R4i-V4.3%20French.zip)
- Décompresser et copier sur la carte SD:
  - `R4.dat` (game kernel)
  - `moonshl2` (video kernel)
  - `R4iMenu` (R4i interface)
- Insérer la carte SD dans le R4SDHC
- Démarrer la DS
  - Je préfère un skin ("peau" :smile:) plus sobre, genre `Wood` ou `Sky`.

> Note: `moonshl2` est le lecteur vidéo (`MEDIA` dans le menu) et apparait aussi dans `GAME`
>
> Pour avoir le Wifi, il faut le configurer à travers un jeu DS (ex "Mario Kart DS")

### Kekatsu-DS

[Kekatsu-DS](https://github.com/cavv-dev/Kekatsu-DS) est un installateur de jeux et logiciels pour Nintendo DS.

1. Télécharger `Kekatsu.nds` depuis la [dernière release](https://github.com/cavv-dev/Kekatsu-DS/releases/latest).

1. Créer un dossier nommé `Kekatsu` à la racine de la carte SD.

1. Copier `Kekatsu.nds` dans le dossier `Kekatsu` (ou n'importe ou sur la carte SD)

1. Créer un fichier texte nommé `databases.txt` dans le dossier `Kekatsu`.

    Voici une liste à mettre dans le fichiers `databases.txt` pour récupérer les listes depuis [Romm](/wiki/docker.md#romm) et [UDB-Kekatsu-DS](https://github.com/cavv-dev/UDB-Kekatsu-DS) (une sélection de logiciels DS et DSi de [Universal-DB](https://db.universal-team.net/ds/), dont des [émulateurs](https://db.universal-team.net/ds/category/emulator) transposée au format Kekatsu).

    Bien entendu, remplacer `192.168.1.12` par l'IP ou est déployé romm.

    ```text
    udb=https://gist.githubusercontent.com/cavv-dev/3c0cbc1b63ac8ca0c1d9f549403afbf1/raw/
    romm-atari2600=http://192.168.1.12/api/feeds/kekatsu/atari2600
    romm-atari5200=http://192.168.1.12/api/feeds/kekatsu/atari5200
    romm-atari7800=http://192.168.1.12/api/feeds/kekatsu/atari7800
    romm-gamegear=http://192.168.1.12/api/feeds/kekatsu/gamegear
    romm-gb=http://192.168.1.12/api/feeds/kekatsu/gb
    romm-gba=http://192.168.1.12/api/feeds/kekatsu/gba
    romm-gbc=http://192.168.1.12/api/feeds/kekatsu/gbc
    romm-megadrive=http://192.168.1.12/api/feeds/kekatsu/genesis-slash-megadrive
    romm-nds=http://192.168.1.12/api/feeds/kekatsu/nds
    romm-nes=http://192.168.1.12/api/feeds/kekatsu/nes
    romm-sms=http://192.168.1.12/api/feeds/kekatsu/sms
    romm-snes=http://192.168.1.12/api/feeds/kekatsu/snes
    romm-wonderswan=http://192.168.1.12/api/feeds/kekatsu/wonderswan
    romm-wonderswan-color=http://192.168.1.12/api/feeds/kekatsu/wonderswan-color
    ```

1. Kekatsu apparait comme un jeu DS.

Configuer:

- Downloads directory: / (Les jeux/applis nds ne doivent pas dépasser un dossier dans l'arborescence)
- Check for update on start: No (plus de mises à jour depuis longtemps)

#### Emulateurs

| Console          | Dossier RomM              | Emulateur                                                         | Tele Emu * | Tele Romm ** | Test Emu                   |
| ---------------- | ------------------------- | ----------------------------------------------------------------- | ---------- | ------------ | -------------------------- |
| Atari 2600       | `atari2600`               | [StellaDS](https://db.universal-team.net/ds/stellads)             | OK         | Facile       | 2 OK                       |
| Atari 5200       | `atari5200`               | [A5200DS](https://db.universal-team.net/ds/a5200ds)               | OK         | Facile       | 2 OK, 1 KO                 |
| Atari 7800       | `atari7800`               | [A7800DS](https://db.universal-team.net/ds/a7800ds)               | OK         | Facile       | 1 OK, 4 KO                 |
| Game Gear        | `gamegear`                | [S8DS](https://db.universal-team.net/ds/s8ds)                     | OK         | Facile       | 2 OK, 1 bizarre            |
| Game Boy         | `gb`                      | [GameYob](https://db.universal-team.net/ds/gameyob)               | OK         | Facile       | 4 OK                       |
| Game Boy Advance | `gba`                     | [GBARunner2](https://db.universal-team.net/ds/gbarunner2)         | OK         | Difficile    | WARNING ! ***              |
| Game Boy Color   | `gbc`                     | [GameYob](https://db.universal-team.net/ds/gameyob)               | OK         | Facile       | 2 OK                       |
| Mega Drive       | `genesis-slash-megadrive` | [PicoDriveTWL](https://db.universal-team.net/ds/picodrivetwl)     | Pas trouvé |              |                            |
| "                | "                         | [jEnesisDS](https://db.universal-team.net/ds/jenesisds)           | OK         | Facile       | 4 OK ****                  |
| NDS              | `nds`                     | N/A                                                               | N/A        |              |                            |
| NES              | `nes`                     | [NesDS](https://db.universal-team.net/ds/nesds)                   | Fail       | Facile       | ?                          |
| Master System    | `sms`                     | [S8DS](https://db.universal-team.net/ds/s8ds)                     | OK         | Facile       | 2 OK, 1 KO                 |
| SNES             | `snes`                    | [lolSnes](https://db.universal-team.net/ds/lolsnes)               | OK         | Facile       | 1 sans son, 4 KO *****     |
| WonderSwan       | `wonderswan`              | [NitroSwan](https://db.universal-team.net/ds/nitroswan)           | OK         | Facile       | 1 OK, 1 KO. Ecran vertical |
| WonderSwan Color | `wonderswan-color`        | [NitroSwan](https://db.universal-team.net/ds/nitroswan)           | OK         | Facile       | 2 KO ("File too large!")   |
| Atari 8-bit      | Unavailable               | [A8DS](https://db.universal-team.net/ds/a8ds)                     | OK         | ?            |                            |
| ScuummVM         | Unavailable               | [ScuummVM](https://db.universal-team.net/ds/scummvm)              | OK         |              |                            |
| Coleco           | Unavailable               | [ColecoDS](https://db.universal-team.net/ds/colecods)             | OK         |              |                            |
| "                | "                         | [S8DS](https://db.universal-team.net/ds/s8ds)                     | OK         |              |                            |
| Nintellivision   | Unavailable               | [Nintellivision](https://db.universal-team.net/ds/nintellivision) | Fail       |              |                            |

**\*** Status du téléchargement de l'émulateur depuis Universal-DB via kekatsu

**\*\*** Status du téléchargement depuis romm via kekatsu

**\*\*\*** GBARunner2 marche mal. Les jeux plantent souvent dès le début, parfois après le menu, au lancement du jeu.

**\*\*\*\*** Attention: reconnait d'autres formats apparement.

**\*\*\*\*\*** Les roms doivent se trouver dans un dossier snes, à la racine. Seul Mario World a marché et encore sans le son.
