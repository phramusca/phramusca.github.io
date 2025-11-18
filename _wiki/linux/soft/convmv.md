---
layout: software
---

# Convmv

Cet outil permet de convertir les noms de fichier d'un systeme
d'encodage de caracteres a un autre

`convmv -r -i -f iso-8859-1 -t utf8 '/media/hda3/xxxx/'`

(remplacer "/media/hda3/xxxx/" par le chemin approprié)

Ensuite relancer avec l'option --notest pour appliquer les changements
proposés.

**Attention :**

- ne pas utiliser l'option --nosmart car trop dangeureuse !
- La copie sur un support en FAT32 (avec cp ou nautilus) ne semble pas
  marcher avec des caractères invalides: modifie l'encodage en cas de
  caractères invalides, mais pas correctement (caractères supprimés).
- La copie avec rsync ne semble pas marcher avec des caractères
  invalides.

Exemples:

- Fichier transféré d'une partition Windows sur une partition UTF-8
  ext3: convmv -f cp850 -t utf-8 -r
- Fichier extrait d'une archive: convmv -f iso-8859-1 -t utf-8 -r

Plus d'info : sur
[ubuntu-fr](http://doc.ubuntu-fr.org/tutoriel/comment_resoudre_les_problemes_invalid_encoding)
et plus généralement: [Recherche convm sur
ubuntu-fr](http://doc.ubuntu-fr.org/?do=search&id=convmv)

------------------------------------------------------------------------

Retour à [Programmes#Divers, sans IHM](Programmes#Divers,_sans_IHM)
