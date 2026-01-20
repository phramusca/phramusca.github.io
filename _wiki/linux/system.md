---
layout: content
---

# Système

## Système de fichiers

### Disques Locaux

Utiliser les outils `Disques` et/ou `gparted` pour gérer les disques (vérifier/fixer les erreurs, partitionner, changer le nom de volume, ...).

Si un disque est monté et ne peut pas être démonté parce qu’il est utilisé, démarrez sur un live CD/USB Linux pour effectuer certaines opérations.

La commande `sudo fdisk -l` permet de lister les disques et d’obtenir le nom du périphérique `/dev/xxx`.

#### Monter un disque

Les clés USB et les disques durs externes, etc sont montés automatiquement en général dans les distributions récentes.

##### /etc/fstab

Le montage automatique des partitions est configurable en root avec le fichier /etc/fstab (ex: pour monter le disque /dev /sdb3 sur `/media/disk`, il faut rajouter la ligne:

```text
/dev/sdb3 /media/disk                  ext3    defaults,errors=remount-ro 0       1
```

dans `/etc/fstab` pour que le disque soit monté automatiquement au démarrage de Linux.

### Droits (chmod)

- <http://doc.ubuntu-fr.org/droits>
- <http://www.debian.org/doc/manuals/debian-reference/ch01.fr.html#_filesystem_permissions>

#### Changer les droits

    chmod -R u+w-x,g+w-x,o-wx,a+rX /mon/repertoire/

- Change les droits récursivement dans le répertoire:
  - donne les droits de lecture à tous (a+r) ainsi que le droit d'ouvrir
    les répertoires (a+X)
  - donne les droits d'écriture a l'utilisateur et au groupe
  - enlève les droits d'écriture au autres

#### UGO et umask

tu connais la notion de droit sur les dossiers/fichiers (rwx =\> Read Write eXecute) ? le fameux ugo (UserGroupOther)

tu as deja vu en faisant un ls -l dans un dossier que cela se présente toujours par

`-rwxr-x--- users group taille fichier`

ben le fameux UGO peut se presenter sous forme de combinaison chiffrée.

r=4 w=2 x=1

tiens on dirait du binaire. pour l'utilisateur sur ma ligne précédente on avait rwx =\> 4+2+1 = 7 pour le groupe on avait r-x =\> 4 + 1 = 5
pour les autres on avait --- =\> 0

les droits ugo sur ce fichier serait 750.

le umask c'est pour préciser ce qui doit être enlevé des droits maximum
(777), mais toujours en logique ugo

umask 022 : => j'enleve rien pour l'utilisateur : => 7 - 0 = 7 : => j'enleve 2 pour le groupe : => 7 - 2 = 5 : => j'enleve 2 pour les autres : => 7 - 2 = 5

donc droit 755 sur ce montage. donc rwx pour l'utilisateur qui fait le
montage r-x pour le groupe de l'utilisateur r-x pour les autres

### lost+found

Lors d'un crash disque ou de la réparation d'un disque au démarrage
(fdsck), il se peut que des données soient perdues. Celle-ci peuvent se retrouver dans le répertoire "lost+found" (attention : dossier caché)

## Icônes

Les icônes se trouvent ici : `/usr/share/icons/`

## Alias bash ou zsh

Pour faire un alias de commande, il faut l'ajouter

- `~/.bashrc` pour bash
- `~/.zshrc` pour zsh

en ajoutant une ligne, par exemple pour un alias `ll` de `ls -la`

```bash
alias ll='ls -la'
```

Ensuite, relancer le shell avec la commande `exec bash` ou `exec zsh`

[Exemples d'alias](http://forum.ubuntu-fr.org/viewtopic.php?id=20437)

## SSH FS

TODO: A relire et vérifier ces informations

sshfs (ssh file system):
<http://doc.ubuntu-fr.org/ssh#monter_un_repertoire_distant_en_utilisant_sshfs>

Monter:

     sshfs username@ipaddress:/RepertoireDistant /EmplacementDeMontage

Démonter:

     fusermount -u /EmplacementDeMontage

### Utilisation de clefs publiques/privées

[doc.ubuntu-fr.org/](https://doc.ubuntu-fr.org/ssh#authentification_par_un_systeme_de_cles_publiqueprivee)

Générer la clef:

     ssh-keygen -t dsa

(ne pas utiliser de paraphrase permet de se connecter - par script par
exemple - sans avoir à taper de paraphrase, mais cela est moins
sécurisé. Ubuntu permet aussi, lors de la connection avec paraphrase de
cocher une option pour ne plus avoir à rentrer la paraphrase)

La copier sur le serveur distant:

     ssh-copy-id -i ~/.ssh/id_dsa.pub username@ipaddress

Et voila, maintenant il faut utiliser la paraphrase pour se connecter au
serveur distant et non plus le mot de passe de l'utilisateur distant.