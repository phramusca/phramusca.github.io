---
layout: content
---

# Système de fichiers

Plus d'infos sur les systèmes de fichiers:

- <http://doc.ubuntu-fr.org/systeme_de_fichiers>
- <http://ww2.ac-creteil.fr/reseaux/systemes/linux/systemes-fichiers.html>
- <http://www.linux-kheops.com/doc/fsstnd/index.htm>
- <http://www.framasoft.net/article2425.html>

## Disques locaux et réseaux

- [Disques Locaux](../Disques_Locaux)
- [Disques Réseau](../Disques_Réseau)

## Droits (chmod)

- <http://doc.ubuntu-fr.org/droits>
- <http://www.debian.org/doc/manuals/debian-reference/ch01.fr.html#_filesystem_permissions>

### Changer les droits

    chmod -R u+w-x,g+w-x,o-wx,a+rX /mon/repertoire/

- Change les droits récursivement dans le répertoire:
  - donne les droits de lecture à tous (a+r) ainsi que le droit d'ouvrir
    les répertoires (a+X)
  - donne les droits d'écriture a l'utilisateur et au groupe
  - enlève les droits d'écriture au autres

### UGO et umask

tu connais la notion de droit sur les dossiers/fichiers (rwx =\> Read
Write eXecute) ? le fameux ugo (UserGroupOther)

tu as deja vu en faisant un ls -l dans un dossier que cela se présente
toujours par

`-rwxr-x--- users group taille fichier`

ben le fameux UGO peut se presenter sous forme de combinaison chiffrée.

r=4 w=2 x=1

tiens on dirait du binaire. pour l'utilisateur sur ma ligne précédente
on avait rwx =\> 4+2+1 = 7 pour le groupe on avait r-x =\> 4 + 1 = 5
pour les autres on avait --- =\> 0

les droits ugo sur ce fichier serait 750.

le umask c'est pour préciser ce qui doit être enlevé des droits maximum
(777), mais toujours en logique ugo

umask 022 : => j'enleve rien pour l'utilisateur : => 7 - 0 = 7 : => j'enleve 2 pour le groupe : => 7 - 2 = 5 : => j'enleve 2 pour les autres : => 7 - 2 = 5

donc droit 755 sur ce montage. donc rwx pour l'utilisateur qui fait le
montage r-x pour le groupe de l'utilisateur r-x pour les autres

## Caractère Tilde ~ dans nautilus

Les fichiers ou dssiers dont le nom fini par ~ (tilda) sont considérés
comme des fichiers/dossiers de sauvegarde par Nautilus et sont donc
cachés.

Pour les voir, afficher les fichiers cachés ...

## lost+found

Lors d'un crash disque ou de la réparation d'un disque au démarrage
(fdsck), il se peut que des données soient perdues. Celle-ci peuvent se
retrouver dans le répertoire "lost+found" (attention : dossier caché)

------------------------------------------------------------------------

Retour à [Misc](Misc)
