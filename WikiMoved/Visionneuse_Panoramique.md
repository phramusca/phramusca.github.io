Une fois l'image panoramique cree avec [Hugin](Hugin "wikilink"), voici
une méthode gratuite pour mettre un panoramique en ligne, en Java (a la
façon d'un QTVR - QuickTime Virtual Reality).

## OpenPanorama

- Spécifications Open Source du format XML :
  <http://www.openpanorama.org/>
- Player gratuit:
  <http://www.immervision.com/fr/multimedia/multimedia_download/player.php?player=PlayerPROJava>

### Exemples

#### Fichier HTML:

`<HTML>`
`<HEAD>`
`    <title>TEST PANO VIEWER</TITLE>`
`</HEAD>`
`<BODY>`
`    <APPLET archive="PurePlayerPro.jar" code="PurePlayerPro" width="461" height="306">`
`        <param name="panorama" value="panorama.xml">`
`        <param name="optimizememory" value="true">`
`        <param name="antialiasing" value="everytime">`
`        <param name="mousespeed" value="100">`
`    </APPLET>`
`</BODY>`
`</HTML>`

#### Fichier panorama.xml (pano.jpg fait 180° horizontal et 90° vertical):

`<?xml version="1.0" encoding="utf-8" ?>`
`<panorama angleType="degree" ns="http://www.immervision.com/panorama">`
`    <camera>`
`        <entryPoint pan="170"/>`
`            <limits maxTilt="45" minTilt="-45" maxPan="175" minPan="-175"/>`
`    </camera>`
`    <panoCylinder>`
`        <image file="pano.jpg"/>`
`    </panoCylinder> `
`</panorama>`

------------------------------------------------------------------------

Retour à [Hugin](Hugin "wikilink")

Retour à [Developement Web](Developement_Web "wikilink")