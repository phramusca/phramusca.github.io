# QuickTime

## QTVR

On peux utiliser Quicktime avec [Wine](Wine). C'est assez
lent, mais c'est le plus simple pour voir les MOV:
<http://www.apple.com/fr/quicktime/download/>

FreePV : <http://freepv.sourceforge.net/>

!! Jamais réussi à l'installer !!

Il faut aussi installer la version dev des dépendances listées sur le
site. Voir le résultat de "./configure" pour connaitre les librairies
manquantes. Pour "OpenGL (Mesa3D or other)", il s'agit de "libglu1-mesa"
(et la version dev).

## Installation de QuickTime 4 Linux

ATTENTION : Apparemment, ne serait qu'une librairie, pas un logiciel. il
faudrait préférer la librairie "libquicktime" qui permet de voir des
vidéos MOV (pas les QTVR) dans tous les lecteurs Multimédia.

- Installer "nasm" depuis le gestionnaire de
  [paquets](Paquet)
- Télécharger les sources de "QuickTime 4 Linux" et "Libmpeg3" sur
  <http://heroinewarrior.com/quicktime.php3>
- Decompresser les archives "QuickTime 4 Linux" et "Libmpeg3".
- Faire un `sudo chmod -R 777 <REPERTOIRE>` sur les deux répertoires
  extraits pour être sur d'avoir les droits pour compiler

      README:
      "Your directory structure should thus be:
      /my_directory
      /my_directory/libmpeg3-*.*.*
      /my_directory/quicktime4linux-*.*.*

      type "make" in the libmpeg3 directory.
      type "make" in the quicktime directory.
      type "make util" to get quicktime to build some utilities. "

------------------------------------------------------------------------

Retour à [Programmes](Programmes)
