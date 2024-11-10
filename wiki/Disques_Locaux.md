# Disques Locaux

Use `Disks` and/or `gparted` to see errors and check, to partition and manage drives.

If drive is mounted and cannot unmount as used, boot to a live linux to perform some operations.

`sudo fdisk -l` to list disks and get /dev/xxx identifier

## Monter un disque

Monter un disque signifie le rendre accessible en lecture, écriture
et/ou exécution, sous la forme d'un "dossier" du système de fichiers
(ex: /media/disk) Normalement, [Ubuntu](linux/dist/Ubuntu) gère très
bien le montage automatique des disques internes et externe. Il peut
arriver cependant de devoir, pour une raison ou une autre, configurer un
disque manuellement. Le plus simple est d'utiliser disk-manager (qui
n'est plus par défaut sous [Ubuntu](linux/dist/Ubuntu) 8.04, mais
disponible dans les [paquets](Paquet)). La méthode classique,
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

```sh
sudo umount /dev/hdb1
sudo tune2fs -L nom_de_volume /dev/hdb1
```

Le nom de volume ne doit pas excéder 16 caractères pour une partition
Ext 2.

*Partition Fat* On utilise mlabel. Pour cela, il est nécessaire
d'installer le [paquet](Paquet) mtools par l'intermédiaire de
synaptic ou par la commande :

`sudo apt-get install mtools`

On édite le fichier /etc/mtools.conf pour modifier la rubrique consacrée
aux disques IDE afin d'affecter une lettre à chaque partition Fat, comme
dans l'exemple suivant :

`gksudo gedit /etc/mtools.conf`

```sh
# # First IDE hard disk partition
# drive c: file="/dev/hda1"
drive d: file="/dev/hda5"
drive e: file="/dev/hda6"
drive f: file="/dev/hda7"
drive g: file="/dev/hda8"
```

Pour modifier le nom de volume de /dev/hda5, il suffira de saisir la
commande suivante :

   `sudo mlabel d:nom_de_volume`

A noter les commandes suivantes :

```sh
mlabel -s d:        pour afficher le label existant de /dev/hda5
sudo mlabel -c d:    pour effacer le label existant de /dev/hda5
```

## Fix bad blocks

[Source](https://askubuntu.com/questions/1278032/fixing-bad-sectors-of-a-hard-drive)

> do NOT abort a bad block scan!

> do NOT bad block a SSD

> backup your important files FIRST!

> this will take many hours

First check with `fsck -f /dev/sdXX` and repeat the fsck command if there were errors

Then launch `sudo e2fsck -fcky /dev/sdXX`

The -k is important, because it saves the previous bad block table, and adds any new bad blocks to that table. Without -k, you loose all of the prior bad block information.

The -fcky parameter...

   ```
   -f    Force checking even if the file system seems clean.
   -c    This option causes e2fsck to use badblocks(8) program to do
         a read-only scan of the device in order to find any bad blocks.
         If any bad blocks are found, they are added to the bad block
         inode to prevent them from being allocated to a file or direc‐
         tory.  If this option is specified twice, then the bad block scan
         will be done using a non-destructive read-write test.
   -k    When combined with the -c option, any existing bad blocks in the
         bad blocks list are preserved, and any new bad blocks found by
         running badblocks(8) will be added to the existing bad blocks
         list.
   -y    Assume an answer of `yes' to all questions; allows e2fsck to be
         used non-interactively. This option may not be specified at the
         same time as the -n or -p options.
   ```

------------------------------------------------------------------------

Retour à [Misc](Misc)
