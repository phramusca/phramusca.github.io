# Développement

Cette page traite du développement de logiciels et d'applications ou
sites Internet.

## Outils et généralités

Pour une liste des logiciels et outils de développement, se référer à
[Programmes#Programmation](Programmes#Programmation "wikilink")

### Contrôle de version

Subversion est la solution Open Source centralisée du moment

[Choix d'un hébergeur](http://www.svnhostingcomparison.com/) Subversion

A priori, en version décentralisée, ce serait plutot GIT, A TESTER:

- <http://doc.ubuntu-fr.org/git>
- <http://www.unixgarden.com/index.php/administration-systeme/git-pour-les-futurs-barbus>
- <http://www.alexgirard.com/git-book/index.html>

### Hébergement de code

[Sourceforge](Sourceforge "wikilink") est un fournisseurs parmi
d'autres.

[savannah.gnu.org](http://savannah.gnu.org/) en est un autre.

[Comparatif d'hébergements de code
SVN](http://www.svnhostingcomparison.com/)

### Paquets Debian

- Créer son paquet Debian: (**A TESTER**)
  - <http://doc.ubuntu-fr.org/tutoriel/creer_un_paquet>
  - <http://alp.developpez.com/tutoriels/debian/creer-paquet/>
  - <http://case.oncle-tom.net/2007/creer-son-propre-paquetage-deb-gtwitter/>

### Sites généralistes

De nombreux sites fournissant du code source et/ou des tutoriels
existent:

- <http://www.developpez.com/>
- <http://www.planet-source-code.com/>
- <http://www.codes-sources.com/>
- ...

Un peu d'humour:

- <http://www.commitstrip.com/>
- <http://www.risacher.com/la-rache/>
- <http://lesjoiesducode.tumblr.com/>

### Misc

- Jeux de caractères: <http://openweb.eu.org/articles/jeux_caracteres/>

## Logiciels IDE

### NetBeans

[NetBeans](NetBeans "wikilink") est l'IDE de Sun (malheureusement repris
maintenant par Oracle) axé Java mais aussi Python, C, C++, Ruby, XML,
PHP, ... Disponible sous Linux et Windows.

### MonoDevelop

[Mono](Mono "wikilink") est une implémentation libre de .NET avec comme
éditeur MonoDevelop

### Gambas

Gambas se veut le presque Visual Basic libre

## Applications "lourdes"

### Java

Contenu transféré sur la page [Java](Java "wikilink") ...

### Visual Basic

Un de mes premiers langages utilisés avec VB6 ...

Je ne pense pas utilser ça encore, surtout que ça ne marche que sous
Windows. Gambas pourrait être une alternative, mais je préfère me
concentrer sur Java en ce moment.

- <http://www.freevbcode.com/>

## Applications et sites Internet

Pour tester en ligne du code HTML, Javascript et CSS:
<http://jsfiddle.net/>

### PhP / MySQL

Mon éditeur de prédilection est [NetBeans](NetBeans "wikilink"). Voir la
page dédiée pour l'installation et la configuration cet IDE pour une
utilisation avec PhP.

Serveur Web : Solution [LAMP](LAMP "wikilink") (Linux, Apache, Mysql,
Php/Perl)

Misc: [Visionneuse Panoramique](Visionneuse_Panoramique "wikilink")

#### Astuces

##### Changer la couleur d'une icone PNG transparente avec GD

- Tout d'abord, il faut créer l'icône avec GIMP:
  - Créer une image avec un fond transparent
  - Dessiner l'icone en noir (seule cette couleur sera remplacée par une
    autre dans l'exemple qui suit)
  - Pour passer en mode couleurs indexées (png8), c'est dans le menu
    image \> mode \> couleurs indexées
  - Enregistrer ensuite en PNG (options par défaut)
- Ensuite, le script Php:



```php
<?php
//Load original icon
$imgfile="myIcon.png";
$image = imagecreatefrompng($imgfile);
//Get index of black color
$index = imageColorclosest($image,0,0,0);
//Get replacement color
$tbase = str_replace("#", '', '#FF2299');
$baseR = hexdec(substr($tbase,0,2));
$baseG = hexdec(substr($tbase,2,2));
$baseB = hexdec(substr($tbase,4,2));
//Replace black with new color
imagecolorset($image,$index,$baseR,$baseG,$baseB);
//Output image with black color replaced
header('Content-type: image/png');
imagepng($image);
imagedestroy($image);
?>
```

### Javascript (et frameworks)

- Using POST method in Ajax (XMLHTTPRequest):
  <http://www.openjs.com/articles/ajax_xmlhttp_using_post.php>
- Prototype Window (gestionnaire de fenêtres DHTML):
  <http://prototype-window.xilinus.com/>
- jQuery: <http://jquery.com/>
- jQuery UI (User Interfaces): <http://jqueryui.com/home>
- Dynamic Drive (DHTML scripts): <http://www.dynamicdrive.com/>
- JavaScript toolbox: <http://www.javascripttoolbox.com/>
- L'editeur JavaScript: <http://www.editeurjavascript.com/>

### Divers

Voir [Firefox](Firefox "wikilink") pour une liste de plugins utiles au
développement.

- [Envoi de mails en
  localhost](http://totalement.geek.oupas.fr/article/2007/11/27/envoyer-des-mails-depuis-php-avec-ubuntu-et-esmtp):
  - Installer [esmtp](apt://esmtp) (d'autres alternatives existent,
    renseigne toi)
  - Editer /etc/esmtprc pour y indiquer le serveur SMTP à utiliser
    ([autres configs genre
    gmail](http://esmtp.sourceforge.net/manual.html#interfacing-with-particular-mail-servers))
  - Créer un lien de sendmail vers esmtp:
    - sudo ln -s /usr/bin/esmtp /usr/sbin/sendmail

## Bases de données

### MySQL

- <http://www.techiecorner.com/485/how-to-monitor-sql-query-in-mysql/>
- [phpMyBackup](http://www.m-tecs.net/?a=products&b=pmb&c=en)
- [Comparaison type de
  base](http://www.supportsages.com/blog/2010/08/mysql-storage-engines-an-overview-their-limitations-and-an-attempt-for-comparison/)
  (MyISAM, InnoDB, ...)

## Divers

Cette section regroupe des idées en vrac. J'essaierai de prendre le
temps de ranger un peu tout ça ...

*Ruby/GTK2: <http://www.bawet.org/article.php3?id_article=60>*

- API Allocine
  - <http://www.phpcs.com/codes/API-ALLOCINE-V3_52259.aspx>
  - <http://wiki.gromez.fr/dev/api/allocine> (source pour l'api php
    ci-dessus)

Voir aussi Cine-passion (sur XBMC) qui a apparemnt aussi une API:
<http://passion-xbmc.org/scraper/index2.php?Page=Home>