---
layout: content
---

# Ma Configuration LAMP

## Installation

- Installer [LAMP](apt://apache2,mysql-server,php5,php5-mysql)
- Installer [ImageMagick](apt://php5-imagick)
- Installer [phpMyAdmin](apt://phpmyadmin)

## Apache

### Virtual Host

#### Méthode 1: création d'un nouvel hôte

(Tiré de la doc Netbeans "[Configuring the PHP Development Environment
in Linux
Ubuntu](http://netbeans.org/kb/docs/php/configure-php-environment-ubuntu.html)")

Créer une copie de l'hôte virtuel par défaut:

    sudo cp /etc/apache2/sites-available/default /etc/apache2/sites-available/rconline

Editer ce nouveau fichier:

    gksudo scite /etc/apache2/sites-available/rconline

Remplacer /var/www par /home/xxxx/Creations/Internet/CheckOut, comme
ci-dessous:

    DocumentRoot /home/xxxx/Creations/Internet/CheckOut
    <Directory />
        Options FollowSymLinks
        AllowOverride None
    </Directory>
    <Directory /home/xxxx/Creations/Internet/CheckOut/>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride None
        Order allow,deny
        allow from all
    </Directory>

Désactiver l'hôte par défaut et activer le nouveau:

    sudo a2dissite default && sudo a2ensite rconline

Relancer Apache:

    sudo /etc/init.d/apache2 reload

#### Méthode 2: Par lien symbolique

Cette méthode est simple à mettre en œuvre, mais la méthode 1 est
préférable.

`ln -s /home/xxxx/Creations/Nouveau/Internet/CheckOut/ /var/www/`

**ATTENTION** : Bien penser à donner les droits appropriés (trouver
mieux que 777) à l'utilisateur www-data. Problème (28/03/2010:
Impossible de faire marcher le site. Erreur 403 Forbidden, même en
mettant /var/www et la cible du lien Checkout en 777 et propriétaire
www-data !!??)

### Php

- Configurer Php:
  - Editer le fichier de configuration:

`sudo scite /etc/php5/apache2/php.ini`

- - Décommenter extension=msql.so
  - Laisser/vérifier register_globals a Off (pour PHP5 et + sur Free)
  - Relancer Apache:

`sudo /etc/init.d/apache2 reload`

### htaccess

Cette section est ici pour réference suelement car je n'utilise plus de
comptes htaccess (seulement des "deny from all")

`htpasswd -c /var/www/CheckOut/password/.htpasswd xxxxxxx.yyyyy`

Pour bien faire, rajouter ensuite tous les logins, à partir de
password/liste.txt :

`<login>:<password>`

devient:

`htpasswd -b /var/www/CheckOut/password/.htpasswd <login> <password>`

## MySQL

### Déplacer les bases dans le home

Par défaut les bases MySQl sont stockées sous /var/lib/mysql/ donc dans
la partition système.

Il peut être plus judicieux de les stocker dans le /home (si sur une
partition ou disque différent).

J'ai choisi de les stocker sous /home/xxxx/Databases/mysql/ (qui inclut
également des sauvegardes sous la forme de script SQL)

- Arrêter MySQL:

    `sudo service mysql stop`

- Déplacer (L'utilisation de 'mv' permet de ne pas modifier les droits originaux.):

**ATTENTION**: Sauter cette étape s'il s'agit d'une reconfiguration et
que les bases sont déjà sous /home/xxxx/Databases/mysql !

    `sudo mv /var/lib/mysql /home/xxxx/Databases/mysql`

- Éditer le fichier de configuration:

    `sudo scite /etc/mysql/my.cnf`

- Dans la section \[mysqld\], changer :

`datadir        = /var/lib/mysql`

par

`datadir        = /home/xxxx/Databases/mysql`

- Configurer AppArmor:

    `sudo scite /etc/apparmor.d/usr.sbin.mysqld`

- Changer les 2 occurrences de "/var/lib/mysql" en "/home/xxxx/Databases/mysql"

  ```sh
  /var/lib/mysql/ r,
  /var/lib/mysql/** rwk,
  ```

- relancer AppArmor

    `sudo service apparmor reload`

- Relancer MySQL:

    `sudo service mysql start`

**Attention:** L'utilisateur "mysql" doit aussi avoir les droits (j'ai
mis rwx mais quel est le minimum ? a priori +r+X) depuis / jusqu'à
/home/xxxx/Databases

### Configurer en UTF-8

Editer le fichier de configuration:

    sudo scite /etc/mysql/my.cnf

A ce jour (1/4/2011 et ce n'est pas une blague), il suffirait d'ajouter
les deux lignes suivantes à la fin de la section « \[mysqld\] » du
fichier /etc/mysql/my.cnf :

```sh
character-set-server=utf8
skip-character-set-client-handshake
```

Auparavant, je rajoutais:

\[client\] default-character-set = utf8 \[mysqld\] default-character-set
= utf8 default-collation = utf8_general_ci

## Données site RC Online

A REVOIR, notamment les 2 liens ci-dessous:

- [Sauvegardes et Restauration](../Sauvegardes_et_Restauration)
- [Sauvegardes MySQL](../Sauvegardes_MySQL)
