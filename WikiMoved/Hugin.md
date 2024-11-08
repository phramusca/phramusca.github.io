Hugin permet de réaliser de panoramiques en assemblant des photos.

# Installation

Hugin est présent dans les dépôts Ubuntu, mais pas pas dans sa dernière
version.

Pour avoir accès aux dernières versions, notamment la version 2010.2 qui
inclut les masques
([tutoriel](http://hugin.sourceforge.net/tutorials/Blend-masks/en.shtml))
il faut installer le PPA (voir [doc
Ubuntu-fr](http://doc.ubuntu-fr.org/hugin)

# Post Processing

## jhead

Une fois le panoramique créé, il faut, avec jhead :

- lui donner la date et les données EXIF de la première photo du
  panoramique :

`jhead -te '1erePhotoduPano.JPG' 'panoramique1.jpg'`

- régénérer l'aperçu (thumbnail) :

`jhead -rgt 'panoramique1.jpg'`

## Intégration Web

En attendant que le prometteur
[PanoSalado](http://panozona.com/wiki/Main_Page) soit vraiment
accessible, je pense que je vais opter pour
[Pano2VR](http://gardengnomesoftware.com/pano2vr.php) qui est
malheureusement commercial au prix raisonnable mais non négligeable de
60€. Une version de démo Linux est disponible qui marche bien.

[Un aperçu des solutions Flash
disponibles](http://www.nicolasburtey.net/visite-virtuelle-flash/)

A essayer quand même: PanoSalado en v1 car des tutos sont dispos:

- <http://benemie.fr/blog/tutoriel-utilisation-de-panosalado/>
- <http://www.sweethome3d.com/blog/2010/04/28/advanced_rendering_plug_in.html>
  (avec aussi PTViewer tuto)
- D'autres à retrouver (google)

La solution dans [Visionneuse
Panoramique](Visionneuse_Panoramique "wikilink") n'est finalement pas si
bonne. Le format OpenPanoram ne semble pas avoir pris et est finalement
spécifique à la société ImmerVision.

------------------------------------------------------------------------

Retour à [Programmes](Programmes "wikilink")