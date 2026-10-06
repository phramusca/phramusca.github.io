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

### Montage au démarrage, démontage utilisateur et accès depuis Nemo

Cette configuration combine `/etc/fstab` et un service systemd utilisateur afin de répondre aux trois besoins : monter le partage au démarrage, pouvoir le démonter sans `sudo` et le remonter facilement depuis Nemo.

> **Note:** *Une entrée `fstab` montée automatiquement par systemd est montée par le gestionnaire système, donc en root. L'option FUSE `allow_other` peut autoriser l'accès aux fichiers depuis la session utilisateur, mais elle ne donne pas le droit de démonter le montage : cela nécessite toujours `sudo`. Un service systemd utilisateur, lui, monte le partage sous le compte de l'utilisateur, qui peut donc le démonter sans privilèges ; toutefois, l'entrée peut disparaître de Nemo une fois le montage arrêté. On déclare donc le partage dans `/etc/fstab` avec `noauto`, puis le service utilisateur le monte au démarrage. Nemo peut alors aussi le monter à la demande.*

Créer le point de montage :

```bash
mkdir -p /media/$USER/serveur
```

Ajouter à `/etc/fstab` (remplacer `utilisateur`, `serveur` et `.local`) :

```fstab
utilisateur@serveur.local:/ /media/utilisateur/serveur fuse.sshfs noauto,user,reconnect,IdentityFile=/home/utilisateur/.ssh/id_ed25519,UserKnownHostsFile=/home/utilisateur/.ssh/known_hosts,ServerAliveInterval=15,ServerAliveCountMax=3 0 0
```

- `noauto` empêche systemd de monter lui-même le partage en root au démarrage.
- `user` autorise l'utilisateur à monter et démonter le partage.
- `reconnect` et les options `ServerAlive` aident à gérer les coupures réseau.
- `IdentityFile` et `UserKnownHostsFile` pointent vers les fichiers SSH de l'utilisateur local.

Créer `~/.config/systemd/user/sshfs-serveur.service` :

```ini
[Unit]
Description=Montage SSHFS du serveur distant

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/bin/mount /media/%u/serveur
ExecStop=-/usr/bin/fusermount3 -u /media/%u/serveur

[Install]
WantedBy=default.target
```

L'unité utilise l'entrée `fstab` pour monter le partage en tant qu'utilisateur, plutôt que de le monter en root. Activer le gestionnaire systemd utilisateur au démarrage, puis activer le service :

```bash
sudo loginctl enable-linger "$USER"
systemctl --user daemon-reload
systemctl --user enable --now sshfs-serveur.service
```

Tester et contrôler le montage :

```bash
findmnt /media/$USER/serveur
systemctl --user status sshfs-serveur.service
```

Après démontage depuis Nemo, l'entrée reste visible dans son panneau latéral ; cliquer dessus remonte le partage. `x-gvfs-show` n'est pas nécessaire dans cette configuration avec Nemo. On peut aussi démonter/remonter via le menu contextuel de Nemo, ou depuis un terminal :

```bash
fusermount3 -u /media/$USER/serveur
mount /media/$USER/serveur
```

La clé doit être utilisable sans demande interactive au démarrage. `allow_other` n'est pas nécessaire ici : SSHFS est monté par l'utilisateur qui l'utilise.

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
