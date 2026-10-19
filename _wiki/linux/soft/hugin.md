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

### *De Chat GPT, 11/2024, A TESTER :*

Pour afficher une image panoramique cylindrique ou sphérique en mode immersif dans un navigateur web, plusieurs options modernes existent, remplaçant le QTVR d’autrefois. Voici quelques solutions populaires et performantes :

1. [Pannellum](https://pannellum.org/)
   - **Description** : Pannellum est une bibliothèque JavaScript open-source permettant d’afficher des panoramas à 360° dans un navigateur sans dépendre de plugins.
   - **Avantages** : Léger, rapide et facile à intégrer. Fonctionne avec des images equirectangulaires et propose une vue immersive fluide.

2. [Marzipano](http://www.marzipano.net/)
   - **Description** : Marzipano est également une bibliothèque JavaScript open-source pour créer des panoramas à 360°. Elle prend en charge les images cylindriques et sphériques et est compatible avec les navigateurs modernes.
   - **Avantages** : Puissant et flexible, il permet de créer des expériences de réalité virtuelle (VR) et est compatible avec Google Cardboard.

4. [A-Frame](https://aframe.io/)
   - **Description** : A-Frame est un framework basé sur Three.js, conçu pour créer des expériences VR en HTML et JavaScript. Il permet de créer des environnements immersifs très rapidement.
   - **Avantages** : Accessible pour ceux qui n’ont pas une forte expérience en programmation et très efficace pour créer des expériences interactives VR en 360°.

- https://pchen66.github.io/Panolens/
- https://github.com/lequangios/webgl-panorama-player?tab=readme-ov-file
