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

TODO: Ceci est une mise à jour de 10/2026 par Copilot. Solutions à tester.

Pour publier un panorama Hugin sur un hébergement de pages personnelles, un lecteur HTML/JavaScript suffit : aucun traitement côté serveur n'est nécessaire. Le panorama et, si souhaité, les fichiers du lecteur peuvent être téléversés comme des fichiers ordinaires.

| Préférence | Solution | Intérêt | À savoir |
| --- | --- | --- | --- |
| 1 | [Pannellum](https://pannellum.org/) | Le choix le plus simple pour afficher un panorama équirectangulaire. Léger, libre, intégrable dans une page et disponible par CDN. Il accepte aussi les panoramas multirésolution et les visites avec points d'intérêt. | Pas de mode casque VR intégré. La version publiée la plus récente vérifiée est [2.5.7](https://github.com/mpetroff/pannellum/releases/tag/2.5.7). |
| 2 | [Photo Sphere Viewer](https://photo-sphere-viewer.js.org/) | Alternative libre plus riche, avec des extensions pour les marqueurs et les visites. Le projet est actif ; version publiée vérifiée : [5.15.1](https://github.com/mistic100/Photo-Sphere-Viewer/releases/tag/5.15.1). | Plus lourd et plus complexe à intégrer que Pannellum, notamment à cause de ses modules et extensions. Il faut publier les fichiers JavaScript/CSS nécessaires ou les charger depuis un CDN. |

Les deux peuvent être utilisés sur un hébergement statique. Un CDN évite de téléverser les fichiers du lecteur, mais rend la page dépendante de ce service tiers ; l'hébergement local des fichiers donne davantage de contrôle.

### Panorama immersif avec un casque VR

TODO: Ceci est une nouveauté de 10/2026 par Copilot. Solution à tester.

[A-Frame](https://aframe.io/) convient pour afficher un panorama dans le navigateur du casque, puis passer en réalité virtuelle avec WebXR. Ce n'est pas seulement un lecteur d'image 360° : c'est un framework de scènes 3D, mais un panorama simple tient dans une page HTML.

#### Exemple minimal pour Oculus Quest 2

Placer l'image équirectangulaire exportée par Hugin, par exemple `panorama.jpg`, à côté du fichier `index.html` :

```html
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Panorama 360°</title>
  <script src="https://aframe.io/releases/1.8.0/aframe.min.js"></script>
</head>
<body>
  <a-scene>
    <a-sky src="panorama.jpg"></a-sky>
    <a-camera look-controls></a-camera>
  </a-scene>
</body>
</html>
```

Téléverser `index.html` et `panorama.jpg` sur l'hébergement, puis ouvrir la page dans le navigateur du Quest 2. Le bouton VR d'A-Frame permet d'entrer dans la vue casque lorsque WebXR est disponible.

**Condition importante :** WebXR exige une origine sécurisée, normalement HTTPS (ou `localhost` pour les essais locaux). Il faut donc vérifier que l'adresse des pages personnelles Free est bien accessible en HTTPS. Si elle ne l'est pas, le panorama restera consultable dans un navigateur classique, mais le mode casque nécessitera un hébergement HTTPS.

Voir la [documentation d'installation d'A-Frame](https://aframe.io/docs/1.8.0/introduction/installation.html) et les explications de MDN sur les [contextes sécurisés](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts).
