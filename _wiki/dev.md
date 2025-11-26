---
layout: content
---

# Développement

Cette page traite du développement de logiciels et d'applications ou sites Internet.

## Outils et généralités

Ma liste de [logiciels et outils de développement](linux/soft/)

### Contrôle de version

- [git](http://doc.ubuntu-fr.org/git)

### Hébergement de code

- [github](https://github.com/)

### Paquets Debian

- Créer son paquet Debian: (**A TESTER**)
  - <http://doc.ubuntu-fr.org/tutoriel/creer_un_paquet>
  - <http://alp.developpez.com/tutoriels/debian/creer-paquet/>

### Sites généralistes

De nombreux sites fournissant du code source et/ou des tutoriels existent:

- <http://www.developpez.com/>
- ...

### Misc

- Jeux de caractères: <http://openweb.eu.org/articles/jeux_caracteres/>

## Logiciels IDE

### NetBeans

[NetBeans](../linux/soft/netbeans) est l'IDE de Sun (malheureusement repris maintenant par Oracle) axé Java mais aussi Python, C, C++, Ruby, XML, PHP, ... Disponible sous Linux et Windows.

### Mono

[Mono](../linux/soft/mono) est une implémentation libre de .NET avec comme éditeur MonoDevelop

### Gambas

Gambas se veut le presque Visual Basic libre

## Applications "lourdes"

### Java

Contenu transféré sur la page [Java](../dev/Java) ...

### Visual Basic

Un de mes premiers langages utilisés avec VB6 ...

Je ne pense pas utiliser ça encore, surtout que ça ne marche que sous
Windows.

## Applications et sites Internet

Pour tester en ligne du code HTML, Javascript et CSS:
<http://jsfiddle.net/>

### PhP / MySQL

Mon éditeur de prédilection est [NetBeans](../linux/soft/netbeans). Voir la
page dédiée pour l'installation et la configuration cet IDE pour une
utilisation avec PhP.

Serveur Web : Solution [LAMP](../dev/LAMP) (Linux, Apache, Mysql,
Php/Perl)

Misc: [Visionneuse Panoramique](../linux/soft/visionneuse_panoramique)

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
- jQuery: <http://jquery.com/>
- jQuery UI (User Interfaces): <https://jqueryui.com/>

### Divers

Voir [Firefox](../archive/linux/soft/Firefox) pour une liste de plugins utiles au développement.

- Envoi de mails en localhost:
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
