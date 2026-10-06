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

### Montage automatique au démarrage et démontage sans `sudo`

Pour monter le partage au démarrage tout en pouvant le démonter comme utilisateur, lancer SSHFS depuis un service systemd utilisateur. Contrairement à une entrée `/etc/fstab`, ce service s'exécute avec les droits de l'utilisateur et celui-ci reste propriétaire du montage.

Si une entrée `/etc/fstab` existe déjà pour ce même point de montage, la commenter ou la retirer et arrêter l'unité système correspondante avant de continuer : un seul mécanisme doit gérer le montage.

Créer le point de montage :

```bash
mkdir -p /media/$USER/serveur

```

Créer le service suivant, en remplaçant `utilisateur` et `serveur.local` :

```bash
nano ~/.config/systemd/user/sshfs-serveur.service
```

```ini
[Unit]
Description=Montage SSHFS du serveur distant

[Service]
Type=simple
ExecStart=/usr/bin/sshfs -f utilisateur@serveur.local:/ /media/%u/serveur -o reconnect,IdentityFile=%h/.ssh/id_ed25519,ServerAliveInterval=15,ServerAliveCountMax=3
ExecStop=-/usr/bin/fusermount3 -u /media/%u/serveur
Restart=on-failure
RestartSec=15

[Install]
WantedBy=default.target
```

Dans le fichier de service, `%u` est remplacé par le nom de l'utilisateur et `%h` par son dossier personnel. `-f` garde SSHFS au premier plan pour que systemd puisse suivre le processus. `Restart=on-failure` réessaie si le montage échoue au démarrage, par exemple si le réseau n'est pas encore prêt.

Activer le démarrage du gestionnaire systemd utilisateur dès le démarrage de la machine, puis activer et lancer le service :

```bash
sudo loginctl enable-linger "$USER"
systemctl --user daemon-reload
systemctl --user enable --now sshfs-serveur.service
```

Vérifier le service et le montage :

```bash
systemctl --user status sshfs-serveur.service
findmnt /media/$USER/serveur
```

L'utilisateur peut monter, démonter et remonter le partage sans `sudo` :

```bash
systemctl --user stop sshfs-serveur.service
systemctl --user start sshfs-serveur.service
```

Les journaux du service sont consultables avec :

```bash
journalctl --user -u sshfs-serveur.service
```

La clé privée doit être utilisable sans demande interactive au démarrage. Si elle est protégée par une phrase secrète, il faut prévoir une solution d'agent SSH dans la session utilisateur.

### Alternative : montage système avec `/etc/fstab`

Une entrée `/etc/fstab` est montée par systemd en tant que root. Il faut `allow_other` pour que l'utilisateur puisse accéder aux fichiers, mais le démontage se fait avec `sudo systemctl stop`. Utiliser cette méthode si le montage doit être géré comme un montage système.

Ajouter une entrée à `/etc/fstab` en remplaçant les valeurs d'exemple :

```fstab
utilisateur@serveur.local:/ /media/utilisateur/serveur fuse.sshfs _netdev,user,allow_other,reconnect,IdentityFile=/home/utilisateur/.ssh/id_ed25519,UserKnownHostsFile=/home/utilisateur/.ssh/known_hosts,ServerAliveInterval=15,ServerAliveCountMax=3 0 0
```

Après avoir créé le point de montage et enregistré `/etc/fstab`, recharger systemd puis démarrer l'unité :

```bash
sudo systemctl daemon-reload
sudo systemctl start "$(systemd-escape --path --suffix=mount "/media/$USER/serveur")"
findmnt /media/$USER/serveur
```

Pour l'arrêter, utiliser `sudo systemctl stop "$(systemd-escape --path --suffix=mount "/media/$USER/serveur")"`. `allow_other` autorise l'accès aux fichiers, mais ne permet pas à l'utilisateur de démonter lui-même le montage.

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
