---
layout: software
---

# Hugin

Hugin permet de réaliser de panoramiques en assemblant des photos.

TODO: Lister les paramètres et astuces pour faire un panoramique cylindrique ou sphérique avec Hugin

## Post Processing

TODO *A VALIDER (11/2024) !*

### jhead

Une fois le panoramique créé, il faut, avec jhead :

- lui donner la date et les données EXIF de la première photo du
  panoramique :

`jhead -te '1erePhotoduPano.JPG' 'panoramique1.jpg'`

- régénérer l'aperçu (thumbnail) :

`jhead -rgt 'panoramique1.jpg'`

### Intégration Web

TODO: Reparcourir tout ça et trouver la meilleure solution en 2026

#### OpenPanorama

- Spécifications Open Source du format XML : <http://www.openpanorama.org/>
- Player gratuit: <http://www.immervision.com/fr/multimedia/multimedia_download/player.php?player=PlayerPROJava>

##### Exemples

###### Fichier HTML

```html
<HTML>
<HEAD>
    <title>TEST PANO VIEWER</TITLE>
</HEAD>
<BODY>
    <APPLET archive="PurePlayerPro.jar" code="PurePlayerPro" width="461" height="306">
        <param name="panorama" value="panorama.xml">
        <param name="optimizememory" value="true">
        <param name="antialiasing" value="everytime">
        <param name="mousespeed" value="100">
    </APPLET>
</BODY>
</HTML>
```

###### Fichier panorama.xml (pano.jpg fait 180° horizontal et 90° vertical)

```html
<?xml version="1.0" encoding="utf-8" ?>
<panorama angleType="degree" ns="http://www.immervision.com/panorama">
    <camera>
        <entryPoint pan="170"/>
            <limits maxTilt="45" minTilt="-45" maxPan="175" minPan="-175"/>
    </camera>
    <panoCylinder>
        <image file="pano.jpg"/>
    </panoCylinder> 
</panorama>
```

### *De Chat GPT, 11/2024, A TESTER :*

Pour afficher une image panoramique cylindrique ou sphérique en mode immersif dans un navigateur web, plusieurs options modernes existent, remplaçant le QTVR d’autrefois. Voici quelques solutions populaires et performantes :

1. [Pannellum](https://pannellum.org/)
   - **Description** : Pannellum est une bibliothèque JavaScript open-source permettant d’afficher des panoramas à 360° dans un navigateur sans dépendre de plugins.
   - **Avantages** : Léger, rapide et facile à intégrer. Fonctionne avec des images equirectangulaires et propose une vue immersive fluide.

2. [Marzipano](http://www.marzipano.net/)
   - **Description** : Marzipano est également une bibliothèque JavaScript open-source pour créer des panoramas à 360°. Elle prend en charge les images cylindriques et sphériques et est compatible avec les navigateurs modernes.
   - **Avantages** : Puissant et flexible, il permet de créer des expériences de réalité virtuelle (VR) et est compatible avec Google Cardboard.

3. [Three.js](https://threejs.org/) avec WebGL
   - **Description** : Three.js est une bibliothèque JavaScript très puissante pour le rendu 3D. Elle permet d’afficher des panoramas sphériques en utilisant WebGL.
   - **Avantages** : Extrêmement personnalisable et compatible avec une large gamme de formats et de dispositifs VR.

4. [Google VR View for the Web](https://developers.google.com/vr/)
   - **Description** : Google VR View permet d’intégrer des images panoramiques en 360° avec une option immersive pour les appareils mobiles et compatibles VR.
   - **Avantages** : Facile à intégrer pour des images 360°, même s'il est un peu limité comparé à des solutions plus flexibles comme Three.js.

5. [A-Frame](https://aframe.io/)
   - **Description** : A-Frame est un framework basé sur Three.js, conçu pour créer des expériences VR en HTML et JavaScript. Il permet de créer des environnements immersifs très rapidement.
   - **Avantages** : Accessible pour ceux qui n’ont pas une forte expérience en programmation et très efficace pour créer des expériences interactives VR en 360°.

Si vous souhaitez une solution légère et simple, **Pannellum** ou **Marzipano** sont d’excellents choix. Pour une plus grande personnalisation et des effets immersifs avancés, **Three.js** ou **A-Frame** sont à privilégier. Ces options fonctionnent toutes sans plugins externes et sont compatibles avec les principaux navigateurs modernes.

----

TODO *D'autres, trouvailles sur internet en 11/2024, A TESTER:*

- https://pchen66.github.io/Panolens/
- https://krpano.com/home/
- https://github.com/lequangios/webgl-panorama-player?tab=readme-ov-file

----

TODO *Du TRES vieux, à archiver:*

En attendant que le prometteur [PanoSalado](http://panozona.com/wiki/Main_Page) soit vraiment accessible, je pense que je vais opter pour [Pano2VR](http://gardengnomesoftware.com/pano2vr.php) qui est malheureusement commercial au prix raisonnable mais non négligeable de 60€. Une version de démo Linux est disponible qui marche bien.

[Un aperçu des solutions Flash disponibles](http://www.nicolasburtey.net/visite-virtuelle-flash/)

A essayer quand même: PanoSalado en v1 car des tutos sont dispos:

- <http://benemie.fr/blog/tutoriel-utilisation-de-panosalado/>
- <http://www.sweethome3d.com/blog/2010/04/28/advanced_rendering_plug_in.html>
  (avec aussi PTViewer tuto)
- D'autres à retrouver (google)

La solution dans [Visionneuse Panoramique](../visionneuse_panoramique) n'est finalement pas si
bonne. Le format OpenPanoram ne semble pas avoir pris et est finalement
spécifique à la société ImmerVision.

----

Retour à [Programmes](Programmes)
