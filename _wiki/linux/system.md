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

## Samba

Samba est un logiciel libre qui permet de partager des fichiers et des imprimantes sur les réseaux locaux. Il est compatible avec les systèmes Windows, Linux et macOS.

### Installation et configuration

Installer [samba](apt://samba) et vérifier la version installée :

```shell
smbd --version
```

Pour partager un répertoire, il faut:

- que le user linux ait un mot de passe samba

  ```shell
  sudo smbpasswd -a myUser
  ```

- qu'il ait les droits d'accès (et de modification si on veut autoriser `read only = no`) au répertoire à partager.

  ```shell
  sudo mkdir -p /home/myUser/partage
  sudo chown -R myUser:myUser /home/myUser/partage
  sudo chmod -R ug=rwX,o= /home/myUser/partage
  ```

- Editer le fichier de configuration de Samba pour ajouter et configurer le partage.

  ```shell
  sudo nano /etc/samba/smb.conf
  ```

  ```ini
  [NomDuPartage]
    path = /home/myUser/partage
    browseable = yes
    read only = no
    valid users = myUser
    create mask = 0660
    directory mask = 0770
  ```

- browseable = yes : le partage apparaît dans la liste des partages. Ça ne donne pas, à lui seul, le droit d’y accéder.
- read only = no : Samba autorise les modifications. Il faut aussi que Linux autorise l’écriture.
- valid users = myUser : seul myUser peut se connecter à ce partage.
- create mask et directory mask : limites de permissions appliquées aux nouveaux fichiers et dossiers créés via Samba. Elles ne changent pas les permissions des éléments déjà présents. 0660 et 0770 sont plus restrictifs : ils autorisent lecture, écriture et accès pour le propriétaire et le groupe, mais pas pour les autres. Les permissions Linux peuvent toutefois encore restreindre l’accès.

Redémarrer le service Samba pour prendre en compte les modifications :

```shell
sudo systemctl restart smbd
```

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

## Planification des tâches

Il y a plusieurs façons de planifier des tâches sur Linux. Les plus courantes sont `cron`, `anacron`, `fcron` et les timers systemd.

| Choix              | À privilégier quand…                                                                                                  | Atouts / limites                                                                                                                                                                                                                                      |
| ------------------ | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **systemd timers** | Le script est important, ou tu veux un service bien intégré au système                                                | Logs dans le journal, gestion des dépendances et des erreurs, configuration explicite. `Persistent=true` permet de rattraper une échéance manquée pendant que la machine était éteinte — une exécution au retour, pas toutes les exécutions manquées. |
| **cron**           | C’est une commande simple, sur une machine toujours allumée                                                           | Très répandu et facile à installer. Attention à l’environnement minimal (PATH, répertoire courant, variables) ; les tâches manquées pendant l’arrêt ne sont généralement pas rattrapées.                                                              |
| **fcron**          | Tu as besoin de ses fonctions particulières, par exemple gérer des tâches quand la machine n’est pas toujours allumée | Alternative à cron, mais moins courante. Pour un nouveau déploiement, elle apporte rarement un avantage décisif face aux timers systemd.                                                                                                              |

**En bref : systemd timer par défaut sur une distribution moderne ; cron pour la simplicité ou la portabilité ; fcron seulement pour un besoin spécifique.**

## Exemple de timer systemd

Un timer systemd s’appuie sur deux fichiers : un **service** qui lance le script, et un **timer** qui définit quand le lancer. Pour une tâche personnelle, crée-les dans `~/.config/systemd/user/`.

Par exemple, pour lancer `/home/alice/bin/mon-script.sh` tous les jours à 2 h 30 :

`~/.config/systemd/user/mon-script.service` :

```ini
[Unit]
Description=Exécute mon script

[Service]
Type=oneshot
ExecStart=/home/alice/bin/mon-script.sh
```

`~/.config/systemd/user/mon-script.timer` :

```ini
[Unit]
Description=Planifie mon script chaque jour

[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true

[Install]
WantedBy=timers.target
```

Remplace `/home/alice` par ton chemin réel et vérifie que le script est exécutable (`chmod +x ~/bin/mon-script.sh`). Active ensuite le timer :

```bash
systemctl --user daemon-reload
systemctl --user enable --now mon-script.timer
```

Pour vérifier la prochaine exécution et consulter les logs :

```bash
systemctl --user list-timers
journalctl --user -u mon-script.service
```

Avec `Persistent=true`, si l’ordinateur était éteint à l’heure prévue, le timer lance le script au prochain démarrage de la session. Sans cette option, l’exécution manquée est ignorée.

La syntaxe de `OnCalendar` est détaillée dans la [documentation systemd (systemd.time)](https://www.freedesktop.org/software/systemd/man/latest/systemd.time.html#Calendar%20Events).

Pour gérer systemd avec une interface graphique, **Cockpit** propose une interface web qui permet notamment de consulter et de gérer les services. Pour créer un timer utilisateur comme celui-ci, les fichiers et les commandes `systemctl --user` restent souvent le plus simple.
