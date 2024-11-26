# Installer un programme sous Linux

## Magasins d'applications

[Linux Mint](../dist/Mint.md) comme [Ubuntu](../dist/Ubuntu.md) et d'autres distributions [Linux](../README.md) ont une logithèque, facilement disponible depuis le menu principal.

Ceci est la méthode à privilégier dans tous les cas, pour plus de facilité, de sécurité et de compatibilité.

## Installer un paquet

### Distributions basées sur Debian (Linux Mint, Ubuntu,...)

Les [distributions Linux basées sur Debian](../README.md#distributions-basées-sur-debian-linux-mint-ubuntu), comme [Linux Mint](../dist/Mint.md) ou [Ubuntu](../dist/Ubuntu.md), ainsi que Debian bien sûr, utilisent le format de paquet `deb`, donc les [programmes](../soft/README.md) fonctionnent sur les deux.

#### Installer un paquet .deb

Si le paquet n'est pas disponible dans les logithèques, il est parfois disponible soit:

- sous forme de fichier `.deb` à télécharger. Il suffit de l'ouvrir pour l'installer.
- dans un dépôt alternatif et généralement le site vous indiquera les commandes à effectuer.

##### Paquet

Les paquets ont étés conçus pour permettre d'éviter la compilation des sources ainsi que pour la gestion des dépendances entre les différents [programmes](../soft/README.md) (beaucoup de [programmes](../soft/README.md) sous [Linux](../README.md) sont dépendants les uns des autres).

Ils peuvent être gérés avec le gestionnaire graphique [Synaptic](apt://synaptic) ou en ligne de commande avec [apt](https://fr.wikipedia.org/wiki/Advanced_Packaging_Tool).

Pour plus d'info, voir [wikipedia](http://fr.wikipedia.org/wiki/Paquet_%28logiciel%29).

##### Dépôt

Un dépôt (ou repository en anglais) est un serveur qui contient les paquets nécessaires pour installer des [programmes](../soft/README.md) sous [Linux](../README.md).

Pour plus d'info, voir [doc.ubuntu-fr.org](<http://doc.ubuntu-fr.org/applications/apt/depots>)

### Autres distributions

Référez vous aux internets, je ne connais que deb pour les distributions de type Debian.

## En compilant les sources

Ceci est la manière originelle d'installer un programme sous [Linux](../README.md), mais est à réserver aux utilisateurs avertis
!!! Dans tous les cas, mieux vaut privilégier l'utilisation de paquets !

Dans la plupart des cas, cela se révèle relativement simple, mais au moindre petit problème, cela peux vite devenir galère.

Perso, ça fait des années que je n'ai pas eu besoin de compiler une application !

Si vous insistez: [Tutoriel compilation](http://doc.ubuntu-fr.org/tutoriel/compilation) sur doc.ubuntu-fr.org
