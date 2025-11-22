---
layout: content
---

# Ubuntu

Ubuntu (à prononcer « Ou-boun-tou ») est une distribution de [Linux](../) populaire ... jusqu'à l'adoption du bureau [Unity](http://doc.ubuntu-fr.org/unity) très déroutant et qui a conduit de nombreux utilisateurs (comme moi) à se tourner vers [Linux Mint](../Mint).

**Cette page n'est donc plus à jour depuis 2017 environ quand le support de Gnome 2 (Gnome classic) a été supprimé.**

- [Ubuntu sur Wikipédia](https://fr.wikipedia.org/wiki/Ubuntu_(syst%C3%A8me_d%27exploitation))
- [Communauté francophone des utilisateurs d'Ubuntu (officiel)](http://www.ubuntu-fr.org/) : Documentation, forum, ...
- [Site Officiel en anglais](http://www.ubuntu.com/)
- [Versions](http://distrowatch.com/table.php?distribution=ubuntu)

## Installation

Ubuntu se décline en plusieurs versions

- Ubuntu, basé sur le bureau Gnome.
- K- Ubuntu, basé sur le bureau KDE.
- autres ...

La version principale est - Ubuntu. Les [programmes](../soft/) présents sur les [dépôts](Dépôt) (valables pour toutes les versions)  sont donc plus adaptés à - Ubuntu.

Pour choisir la version qui te convient et pour plus de détails sur l'installation, tu peux consulter la [page consacrée](http://doc.ubuntu-fr.org/installation) sur le site de la Communauté francophone des utilisateurs d'Ubuntu.

*Forums, aide, FAQ, ... :* <http://forum.ubuntu-fr.org/>

*Documentation :* <http://doc.ubuntu-fr.org/>

### Test

Si tu es sous Windows, mais que tu veux tester Linux, sans désinstaller
Windows, il y a deux possibilités :

#### LiveCD

Le CD d'installation d'Ubuntu est aussi un Live CD, c'est a dire qu'il
est possible de démarrer Ubuntu directement du CD sans l'installer sur
le disque dur. Cela permet de tester l'interface. Sur le bureau
d'Ubuntu, un raccourci est disponible pour lancer une installation sur
le disque dur (pense à faire une sauvegarde de tes données avant dans le
cas d'une mauvaise manipulation).

#### Virtualisation (Virtual Box)

Très simple et pas de bidouilles à faire avec cette solution d'Oracle:
[VirtualBox](http://www.virtualbox.org/)

[Images toutes prêtes](http://virtualboxes.org/images/)

[Partage dossier Windows sous hôte Ubuntu](http://www.commentcamarche.net/faq/21387-virtualbox-partage-d-un-dossier-windows-sous-un-hote-ubuntu)

Pour info, il existe d'autres solutions de virtualisation: VMWare, Virtual PC, ...

### Vieille Bécane ?

Sur un vieux PC, le lancement du Live CD peux poser des problèmes. Pour éviter ce problème, il suffit:

- de télécharger une version alternate d'ubuntu
  <http://www.ubuntu-fr.org/telechargement>
- d'installer Ubuntu : <http://doc.ubuntu-fr.org/installation_alternate>
  - soit en choisissant "installer".
  - soit en ligne de commande (pour occuper un minimum d'espace disque
    et/ou pour pouvoir maitriser au mieux l'installation)

### Et après

Tu peux maintenant utiliser ton nouvel environnement, installer de nouveaux [programmes](Programmes), ...

**Un truc important à savoir est que le mot de passe superutilisateur (root), qui est notamment demandé pour installer des [programmes](Programmes), n'est autre que le mot de passe de l'utilisateur principal, choisi lors de l'installation.**

*En mode console, pour passer en root (superutilisateur), tapez sudo suivi de la commande (ex : sudo chmod 664 toto.txt pour changer les droits d'un fichier).*

## Unity

Ubuntu 11.04 a introduit une nouvelle interface développée par Canonical (la société derrière Ubuntu) appelée [Unity](http://doc.ubuntu-fr.org/unity).

Cette interface est un peu déroutante au premier abord, mais il est possible d'utiliser l'interface gnome classique, ou le Gnome Shell (qui est l'équivalent de Unity mais fait par l'équipe de Gnome):

- Sous Ubuntu 11.04 le choix "Interface classique" est disponible dans le choix de la session
- Sous Ubuntu 11.10, il faut :
  - installer [gnome-classic](apt://gnome-classic) pour avoir le menu [Gnome](Gnome) classique
  - ou installer [gnome-shell](apt://gnome-shell) pour avoir Gnome Shell.

[Activer le cube 3D avec Unity](http://www.le-libriste.fr/ubuntu/configuration-dunity/activer-le-cube-3d-avec-unity/)

Installer [Classic Menu Indicator](http://www.florian-diesch.de/software/classicmenu-indicator/), pour avoir accès aux programmes un peu comme "à l'ancienne"


