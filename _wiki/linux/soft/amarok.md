---
layout: software
---

# Amarok

Logiciel de musique complet et très agréable à utiliser.

## Amarok 2

**Attention: Amarok 2.0 n'est pas au point**

En passant à Ubuntu 9.04, Amarok passe en version 2.0 qui présente pas
mal de changements, dont:

- Support exclusif de MySQL comme base de données embarquée.
- et d'autres, mais surtout:
- pleins de problèmes (voir forum ubuntu fr)
- Apparement il manque un paquet pour Xine lors de la mise a jour:
  phonon-backend-xine

**Je vous conseille fortement de revenir à la version 1.4.10 :**

- Ajouter la clef:

     `sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com B9F1C432AE74AE63`

- rajouter dans les sources de mise a jour:

deb <http://ppa.launchpad.net/bogdanb/ppa/ubuntu> karmic main

deb-src <http://ppa.launchpad.net/bogdanb/ppa/ubuntu> karmic main

A partir de lucid (10.04 LTS), il faut au préalable installer le paquet libmysqlclient15off_5.0.51a-3ubuntu5.8_i386.deb

- faire la mise a jour:

     `sudo apt-get remove amarok && sudo apt-get install amarok14`

Source: <http://forum.ubuntu-fr.org/viewtopic.php?id=311176>

## Forks de Amarok 1.4.x

Il existe de nombreux forks (embranchements) de Amarok 1.4
(http://digitizor.com/2010/07/27/gereqi-and-pana-two-more-amarok-1-4-clones/):

- [Clementine](http://doc.ubuntu-fr.org/clementine), facile à installer par un .deb et apparemment bon (on peux même
  utiliser la wiimote comme télécommande), mais ne supporte pas MySQL
  comme Bdd :(
- Gereki, plus minimaliste, facile à installer par un .deb. supporte
  MySQL (et SQLLite). A FINIR DE TESTER
- Pana, plus dur a installer (pas de .deb):
  <http://www.ubuntugeek.com/pana-a-music-player-based-on-amarok-1-4.html#more-4664>
  . Je n'ai pas réussi à installer la version 1.4.16 sur Ubuntu 11.04

## Options pour Amarok 1.4.10

### Xine

Utiliser le moteur xine permet la fonction de fondu enchainés entre les
chansons.

### moodbar

moodbar est un logiciel (disponible dans les paquets) Après
installation, une option dans Amarok permet de visualiser cette mood
(humeur). Gadget, mais sympa.

### Scripts pour Amarok

- **replaygain**: <http://kde-apps.org/content/show.php?content=26073>
- usb_device_amaroKscript (gestion des appareils USB - ex Archos):
  - Installer [kdebase](apt://kdebase) (pour kfminfo)
  - Installer [mp3info](apt://mp3info)
  - Installer le script:
    <http://kde-apps.org/content/show.php/usb_device_amaroKscript?content=35156>
- copyCover :
  <http://kde-apps.org/content/show.php/CopyCover+%28amaroK+Script%29?content=22517>
- Smart DJ, a tester (pb install)

J'ai eu le problème avec replaygain qui n'apparaissait pas dans la liste
des scripts. J'ai du supprimer le répertoire replaygain sous
/home/xxxx/.kde/share/apps/amarok/scripts/amarok_replaygain/ puis le
réinstaller. Il est alors apparu à nouveau dans le gestionnaire de
scripts d'AmaroK

### Amarok2 et MySQL

**Apparemment, dans la version 2.2 et + Amarok gère
ceci lui-même comme dans la version 1.4**

Source originale: <http://forum.ubuntu-fr.org/viewtopic.php?id=280537>

Je conseillerai de faire avant tout une sauvegarde d'un éventuel dossier
amarok dans /var/lib/mysql (genre la base de la version 1.x), avec:

`sudo mv /var/lib/mysql/amarok /var/lib/mysql/amarok1-Backup`

La technique consiste donc à déplacer le dossier amarok dans ce dossier
:

`sudo cp -r ~/.kde/share/apps/amarok/mysqle/amarok /var/lib/mysql/`

Il faut ensuite supprimer le dossier une fois copié:

`sudo rm ~/.kde/share/apps/amarok/mysqle/amarok`

Ensuite, créer un lien symbolique vers ce dossier déplacé :

`ln -s /var/lib/mysql/amarok ~/.kde/share/apps/amarok/mysqle/`

Normalement, à cette étape, si vous redémarrez Amarok, tout doit
fonctionner ! Le seul problème c'est que le serveur mySQL (en particulier
au travers de phpmyadmin) ne peut pas accéder aux fichiers de la base de
données pour des questions de droits (on voit la base dans phpmyadmin mais
on ne peut pas accéder aux tables). Ma solution a donc été de brutalement
appliquer des chmod sur le dossier amarok (rwx pour le dossier lui-même et
rw pour les fichiers du dossier si mes souvenirs sont bons).

Voilà normalement, vous devriez alors avoir une base à la fois
accessible via MySQL/phpmyadmin et amarok !

NB: Parfois des MAJ de la base via amarok ne sont pas prises en compte
tout de suite dans phpmyadmin. Dans ce cas, un reboot du serveur SQL
permet de résoudre le problème : Code:

`sudo /etc/init.d/mysql restart`

### En français dans le texte

Pour passer Amarok en français, installer le paquet
[kde-i18n-fr](apt://kde-i18n-fr)
