## Monter un disque

Monter un disque signifie le rendre accessible en lecture, écriture
et/ou exécution, sous la forme d'un "dossier" du système de fichiers
(ex: /media/disk) Normalement, [Ubuntu](Ubuntu "wikilink") gère très
bien le montage automatique des disques internes et externe. Il peut
arriver cependant de devoir, pour une raison ou une autre, configurer un
disque manuellement. Le plus simple est d'utiliser disk-manager (qui
n'est plus par défaut sous [Ubuntu](Ubuntu "wikilink") 8.04, mais
disponible dans les [paquets](paquet "wikilink")). La méthode classique,
un peu plus délicate à mettre en place, est de modifier directement le
fichier /etc/fstab qui configure le montage des disques.

### disk-manager

L'outil disk-manager permet de gérer le fichier /etc/fstab de manière
graphique.

Plus d'infos sur disk-manager: <http://doc.ubuntu-fr.org/disk-manager>

Cas des partitions Windows (FAT32, NTFS):
<http://doc.ubuntu-fr.org/tutoriel/comment_acceder_a_ses_partitions_windows>

Mes options pour disque externe USB FAT32 My Book :

`rw,user,auto,gid=1000,uid=1000,umask=002,iocharset=utf8,codepage=850,shortname=mixed`

- umask=002 : 775 (rwxrwxr.x) =\> choisi pour permettre a www-data (user
  apache), dans mon groupe, de modifier les fichiers
- umask=013 : 764 (rwxrw.r..) =\> non retenu car sinon pas de x sur les
  dossiers et donc impossible de les ouvrir
- umask=000 : 777 (rwxrwxrwx) =\> Attention, trou de sécurité !!
- umask=111 : 666 (rw.rw.rw.) =\> pas viable, impossible d'ouvrir les
  dossiers

### /etc/fstab

Le montage automatique des partitions est configurable en root avec le
fichier /etc/fstab (ex: pour monter le disque /dev /sdb3 sur
/media/disk, il faut rajouter la ligne:

`/dev/sdb3 /media/disk                  ext3    defaults,errors=remount-ro 0       1`

dans /etc/fstab pour que le disque soit monté automatiquement au
démarrage d'Ubuntu.)

Plus d'infos: [1](http://www.lea-linux.org/cached/index/Fstab.html)

## Changer le nom de volume

Extrait de <http://forum.ubuntu-fr.org/viewtopic.php?pid=435962> Testé
uniquement mlabel (et avec succès)

Il est décevant de s'apercevoir que la partition montée sur le bureau ne
reprenne pas le nom qu'on lui a spécifié dans /etc/fstab et le point de
montage de /media mad. Cela tient au label (nom de volume) affecté à la
partition, le plus souvent sous Windows. Le label peut être utilisé par
mount, fsck, /etc/fstab en spécifiant LABEL=nom_volume à la place du nom
de périphérique comme /dev/hdb1.

Gparted ne gère pas les labels, QTParted quant à lui se contente de les
lire (sous la rubrique 'étiquette').

Pour connaître les informations des partitions montées (type de
partition et label) utiliser la commande :

`mount -l`

*Partition Ext2 et Ext3* On utilise la commande tune2fs sur une
partition préalablement démontée. Par exemple, pour changer le label de
hdb1 :

`   sudo umount /dev/hdb1`
`   sudo tune2fs -L nom_de_volume /dev/hdb1`

Le nom de volume ne doit pas excéder 16 caractères pour une partition
Ext 2.

*Partition Fat* On utilise mlabel. Pour cela, il est nécessaire
d'installer le [paquet](paquet "wikilink") mtools par l'intermédiaire de
synaptic ou par la commande :

`   sudo apt-get install mtools`

On édite le fichier /etc/mtools.conf pour modifier la rubrique consacrée
aux disques IDE afin d'affecter une lettre à chaque partition Fat, comme
dans l'exemple suivant :

`gksudo gedit /etc/mtools.conf`

`# # First IDE hard disk partition`
`# drive c: file="/dev/hda1"`
`drive d: file="/dev/hda5"`
`drive e: file="/dev/hda6"`
`drive f: file="/dev/hda7"`
`drive g: file="/dev/hda8"`

Pour modifier le nom de volume de /dev/hda5, il suffira de saisir la
commande suivante :

`   sudo mlabel d:nom_de_volume`

A noter les commandes suivantes :

`   mlabel -s d:        pour afficher le label existant de /dev/hda5`
`   sudo mlabel -c d:    pour effacer le label existant de /dev/hda5`

------------------------------------------------------------------------

Retour à [Misc](Misc "wikilink")