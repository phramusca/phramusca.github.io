---
layout: default
---

# Disques Réseau

Je ne parle ici que de réseau Windows, n'ayant pas eu l'occasion de
tester comment marche le réseau Linux.

## Partager des dossiers

Pour pouvoir partager des dossiers avec le monde Windows, il faut
installer le service Samba.

Tous les détails ici : <http://doc.ubuntu-fr.org/samba>

### User shares

Les partages utilisateurs peuvent être géré en ligne de commande [Doc
sur
samba.org](http://samba.org/samba/docs/man/manpages-3/smb.conf.5.html)

### Administrative shares

En plus des partages utilisateurs, il est possible de créer des partages
administratifs. Ceux-ci sont listés dans smb.conf, contrairement aux
partages utilisateurs

Il existe plusieurs interfaces graphiques pour les configurer. Une
d'elle (simple à utiliser) est
[system-config-samba](http://doc.ubuntu-fr.org/system-config-samba)

**Attention:** Il est surement nécessaire de configurer le
[Firewall](Programmes.md#administration)
pour que les dossiers soient visibles sur le réseau!

## Ouvrir un dossier réseau

Pour monter un disque réseau, il existe plusieurs méthodes:

- [Ubuntu](linux/dist/Ubuntu) peut monter un disque facilement à travers
  Nautilus, mais ne permet pas d'accéder aux fichiers autrement qu'avec
  Nautilus (ex: <smb://disk> et non /media/disk).
- mount.cifs, le remplacant de smbmount (car CIFS remplace SMBFS)
- fstab: Ceci monte les disques au démarrage automatiquement (ou non
  d'ailleurs)

### mount.cifs

Pour pouvoir utiliser la commande mount.cifs, il faut installer le
[paquet](Paquet) [smbfs](apt:smbfs)

Ensuite, utiliser la commande mount.cifs. Par exemple, pour monter :

- le disque réseau //192.168.0.2/Musiquexxxx
- sur le disque local /media/Musiquexxxx
- avec l'utilisateur réseau toto et le mot de passe tutu (utilisateur
  Windows ou Samba)
- pour l'utilisateur local par défaut d'Ubuntu, le tien normalement
  (id=1000,gid=1000)
- sur le domaine WORKGROUP

```sh
mount.cifs //192.168.0.2/Musiquexxxx /media/Musiquexxxx -o user=toto,password=tutu,id=1000,gid=1000,domain=WORKGROUP,iocharset=utf8
```

**Attention**: Pour pouvoir utiliser cette commande par un utilisateur
non-root, il est nécessaire de lui donner les droits avec
[visudo](Système.md#sudo)

### fstab

/etc/fstab est un fichier de configuration qui permet de monter des
dossiers automatiquement au démarrage de la machine (de façon
permanente).

**ATTENTION: A réserver aux utilisateurs avancés**

Plus d'infos sur [ubuntu-fr](http://doc.ubuntu-fr.org/mount_fstab).

Exemple:

//192.168.0.10/Musiquexxxx /media/Musiquexxxx/ cifs
user=toto,password=tutu,iocharset=utf8,uid=1000,gid=1000 0 0

Ceci monte:

- le lecteur réseau //192.168.0.10/Musiquexxxx
- à l'emplacement: /media/Musiquexxxx/
- avec l'utilisateur user=toto,password=tutu (utilisateur Samba ou
  Windows)
- iocharset=utf8: type d'encodage (UTF-8 devient maintenant la norme
  internationale)
- uid=1000: spécifie le n° du user propriétaire des fichiers (si omis :
  root)
- gid=1000: spécifie le n° du groupe propriétaire des fichiers (si omis
  : root)

### smbmount

Ce programme est obsolète et n'est plus maintenu. mount.cifs (voir
ci-dessus) devrait être utilisé à la place.

[smbmount
manpage](http://manpages.ubuntu.com/manpages/gutsy/man8/smbmount.8.html):
WARNING: smbmount is deprecated and not maintained any longer.
mount.cifs (mount -t cifs) should be used instead of smbmount.

## MyBook World Edition

Comme je n'arrivais plus à changer les droits sur MyBook
(http://forum.ubuntu-fr.org/viewtopic.php?id=388450), je me suis donc
décidé à installer SSH dessus. Finalement, ce n'est vraiment pas
difficile: <http://mybookworld.wikidot.com/ssh-enable>

1.Change dans l'adresse web suivante "Mybook-Ip-Address" par l'IP du
MBWE, et lance le lien dans un navigateur internet
([Firefox](Firefox) par ex.):

<http://Mybook-Ip-Address/auth/firmware_upgrade.pl?fwserver=highlevelbits.free.fr/download/MBWE/MBWE-SSH-ENABLE>

2\. Dis oui ou OK ou je ne sais plus quoi quand on te demande si tu veux
mettre à jour

3\. Comme indiqué sur un autre blog, l'interface web peux indiquer une
erreur de téléchargement. Ça a été mon cas, mais en vérifiant le log
dans PUBLIC, j'ai pu constater ("SSH will be activated at next reboot")
que ça s'était finalement bien passé.

4\. Un petit reboot de la bête et ensuite connexion SSH avec:

     ssh root@Mybook-Ip-Address

mot de passe: root

et voila !

## SSH

Connection simple:

     ssh username@ipaddress

### SSH FS

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

------------------------------------------------------------------------

Retour à [Misc](Misc)
