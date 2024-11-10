# GIMP

GIMP est un équivalent Open Source de Photoshop.

## GIF animés

<http://www.infetech.com/article.php3?id_article=166>

- Ouvrir la première image
- Rajouter les autres photos dans le menu "Fichier-\>ouvrir comme un
  calque"
- (Mettre les calques dans le bon ordre)
- Enregistrer Sous - GIF
- Choisir "enregistrer en tant qu’animation"
- Enfin, dans le dernier écran, on choisit boucle infinie (pour que
  l’animation tourne en boucle), une image par calque (sinon les images
  s’emplient) ainsi aue la vitesse de défilement des images (700 ms par
  ex)

## Panorama Tools

Il existe un plugin des [Panorama
Tools](http://sourceforge.net/projects/panotools/) pour GIMP.

### Installation

- Télécharger le plugin ici:
  <http://panotools.svn.sourceforge.net/viewvc/panotools/trunk/gimp-plugin-ng/>
- Installer les dépendances suivantes (au moins) par le gestionnaire de
  paquets:
  - automake1.10 (car 1.11 ne marche pas apparement)
  - intltool
  - autoconf
- Extraire l'archive téléchargée
- En ligne de commande, se placer dans le dossier source et lancer:
  - sh autogen.sh
  - make
  - sudo make install

Il est peut être nécessaire d'installer au préalable les Pano tools,
mais ce n'est pas sur car je les ai installés avant.. Au cas ou, voici
la procédure d'installation:

- Télécharger "libpano13-2.9.17.tar.gz" depuis
  <http://sourceforge.net/projects/panotools/>
- Installer les dépendances suivantes (au moins) par le gestionnaire de
  paquets:
  - libpng-dev
  - libjpeg-dev
  - libtiff-dev
- En ligne de commande, se placer dans le dossier source et lancer:
  - ./configure
  - make
  - sudo make install

### Utilisation

Je ne connais qu'une utilisation :
<http://replay.waybackmachine.org/20040215114320/http://www.panoguide.com/technique/circular.html>

Il en existe surement d'autres, a vous de jouer.

------------------------------------------------------------------------

Retour à [Programmes](Programmes)
