# Amarok

Logiciel de musique complet et très agréable à utiliser.

## Amarok 2

**Attention: Amarok 2.0 n'est pas au point**

En passant à Ubuntu 9.04, Amarok passe en version 2.0 qui présente pas
mal de changements, dont:

- Support exclusif de MySQL comme base de données embarquée. Pour s'y
  connecter: [Amarok2 et MySQL](Amarok2_et_MySQL "wikilink")
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

A partir de lucid (10.04 LTS), il faut au préalable installer le paquet
[libmysqlclient15off_5.0.51a-3ubuntu5.8_i386.deb](http://fr.archive.ubuntu.com/ubuntu/pool/main/m/mysql-dfsg-5.0/libmysqlclient15off_5.0.51a-3ubuntu5.8_i386.deb)

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

### Connection MySQL

Utiliser MySQL comme moteur de BDD est plus rapide et permet d'accéder à
sa bibliothèque musicale avec MySQL (et donc PhP, ...).

### En français dans le texte

Pour passer amarok en français, installer le [paquet](Paquet "wikilink")
[kde-i18n-fr](apt://kde-i18n-fr)

------------------------------------------------------------------------

Retour à [Programmes](Programmes "wikilink")
