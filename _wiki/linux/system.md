---
layout: content
---

# Système

## Terminal

Voir [terminal](../system/terminal)

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

```bash
chmod -R u+w-x,g+w-x,o-wx,a+rX /mon/repertoire/
```

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

Monter un répertoire distant via SSH avec `sshfs` (basé sur FUSE).

- Documentation : <http://doc.ubuntu-fr.org/ssh#monter_un_repertoire_distant_en_utilisant_sshfs>

Installation :

```bash
sudo apt install sshfs
```

Monter :

```bash
mkdir -p /media/$USER/serveur
sshfs utilisateur@serveur.local:/ /media/$USER/serveur
```

### Montage automatique au démarrage avec `/etc/fstab`

Créer le point de montage si nécessaire, puis ajouter une ligne à `/etc/fstab` :

```bash
mkdir -p /media/$USER/serveur
sudo nano /etc/fstab
```

L'équivalent de la commande SSHFS ci-dessus est :

```fstab
utilisateur@serveur.local:/ /media/utilisateur/serveur fuse.sshfs _netdev,user,allow_other,reconnect,IdentityFile=/home/utilisateur/.ssh/id_ed25519,UserKnownHostsFile=/home/utilisateur/.ssh/known_hosts,ServerAliveInterval=15,ServerAliveCountMax=3 0 0
```

- Le chemin dans `/etc/fstab` est absolu : contrairement au shell, le fichier ne développe ni `~` ni `$USER`.
- Remplacer `utilisateur` et `serveur.local` par le nom d'utilisateur et l'adresse du serveur ; le chemin distant `/` peut être remplacé par le répertoire à monter.
- `_netdev` indique à systemd que le montage dépend du réseau.
- `allow_other` autorise les autres utilisateurs locaux à accéder aux fichiers. C'est nécessaire ici car systemd monte le partage en tant que root ; cette option ne donne pas aux utilisateurs le droit de démonter le montage.
- `user` autorise un utilisateur à demander le montage via `mount`, mais ne transfère pas la propriété d'un montage démarré par systemd. `reconnect` demande à SSHFS de réessayer après une coupure.
- `IdentityFile` et `UserKnownHostsFile` indiquent la clé privée et les clés d'hôtes SSH de l'utilisateur local. Choisir une clé dont la clé publique est autorisée sur le serveur. Le chemin `id_ed25519` ci-dessus est un exemple : si seule `id_rsa` est autorisée, utiliser `/home/utilisateur/.ssh/id_rsa`. C'est utile au montage automatique, qui ne peut pas compter sur l'agent SSH de la session interactive.
- `ServerAliveInterval` et `ServerAliveCountMax` permettent de détecter plus rapidement une connexion interrompue.
- Ne pas ajouter `nofail` avec les configurations où SSHFS/FUSE reçoit cette option comme option inconnue.

Pour un montage sans intervention au démarrage, la clé privée ne doit pas demander de phrase secrète (sauf configuration supplémentaire).

Pour savoir quelle clé le serveur accepte, lancer `ssh -v utilisateur@serveur.local` et repérer `Server accepts key`. Si plusieurs clés sont autorisées, Ed25519 est généralement préférable à RSA, mais on peut garder RSA si nécessaire ou si c'est la seule clé déjà installée sur le serveur.

Tester la configuration sans redémarrer :

```bash
sudo systemctl daemon-reload
unit=$(systemd-escape --path --suffix=mount "/media/$USER/serveur")
sudo systemctl start "$unit"
findmnt /media/$USER/serveur
```

Consulter l'état et les journaux en cas d'erreur :

```bash
sudo systemctl status "$unit" --no-pager
sudo journalctl -b -u "$unit" -n 50 --no-pager
```

Arrêter/démonter le partage :

```bash
sudo systemctl stop "$unit"
```

Le montage est géré par l'unité système et appartient donc à root. `allow_other` autorise l'accès aux fichiers, pas le démontage sans privilèges. Pour le démonter, utiliser `systemctl stop` avec `sudo` plutôt que `fusermount -u`. Après avoir modifié `/etc/fstab`, recharger les unités avec `systemctl daemon-reload` ; cette commande n'est pas nécessaire après un redémarrage.

Avec cette configuration, sans l'option `nofail`, une indisponibilité du serveur peut faire échouer l'unité au démarrage ; le journal systemd indiquera l'erreur. Une fois le serveur joignable, démarrer à nouveau l'unité avec `sudo systemctl start "$unit"`.

### Utilisation de clefs publiques/privées

[doc.ubuntu-fr.org/](https://doc.ubuntu-fr.org/ssh#authentification_par_un_systeme_de_cles_publiqueprivee)

Générer la clef:

```bash
ssh-keygen -t ed25519
```

La copier sur le serveur distant:

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub username@ipaddress
```

Et voila, maintenant il faut utiliser la paraphrase (si renseignée) pour se connecter au serveur distant et non plus le mot de passe de l'utilisateur distant.

TODO: Faire section FTP, et ajouter FileZilla et lftp (script. et gui ? => faire des liens avec doc internet/free.fr)
