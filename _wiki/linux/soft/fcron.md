---
layout: software
---

# Fcron

**Fcron** est un planificateur de tâches (daemon + `fcrontab`), alternative à **cron** et **anacron**. Le projet est ancien ; pour du récent et intégré au système, voir plus bas.

## Installation

L’installation amont se fait par **compilation des sources**. Procédure et prérequis : [documentation officielle — How to install fcron](https://yo8192.github.io/fcron/install.html#AEN206).

## Configuration (aperçu)

Tâches avec **`fcrontab`** (ex. `fcrontab -e`). Syntaxe détaillée : doc du projet et [Ubuntu-fr](https://doc.ubuntu-fr.org/fcron).

## Alternatives plus modernes

En pratique : **[systemd timers](https://systemd.io/)** (unités `.timer` + `.service`), ou **cron** / **anacron** selon le besoin.
