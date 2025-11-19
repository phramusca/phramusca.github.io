---
layout: wiki
---

# Réseau

## Contrôle parental

Il existe sous linux plusieurs solutions de contrôle parental:
<http://doc.ubuntu-fr.org/tutoriel/comment_mettre_en_place_un_controle_parental>

Pour ma part, j'ai choisi
[OpenDNS](http://doc.ubuntu-fr.org/tutoriel/comment_mettre_en_place_un_controle_parental#opendns).
Il s'agit de remplacer le DNS, le service qui remplace l'adresse
internet texte en adresse machine ( ex "<http://ubuntu-fr.org>" en
adresse machine : "80.125.12.55" ) de son fournisseur d'accès par un
autre qui bloquera certains sites (configurables) et permet aussi
d'autres services intéressants.

Pour info, les DNS de Free.fr sont: 212.27.40.241 et 212.27.40.240
(utile si configuration par utilisateur)

### Modification du tutoriel

Si la session des enfants est lancée en premier, OpenDNS sera actifs sur
toutes les sessions. A l'inverse, si un autre utilisateur démarre sa
session en premier, OpenDNS ne sera pas actif pour toutes les sessions,
y compris pour la session des enfants !

Pour que les modifications de /etc/resolv.conf soient prises en compte
alors que le réseau est déjà lancé, il faut soit redémarrer la machine
(et on se retrouve dans la situation décrite plus haut), soit redémarrer
le réseau avec la commande suivante. Problème, si la session des enfants
n'a pas les droits d'administration (même en sudo, donc le rajouter dans
script /usr/sbin/opendns ne sert à rien), ils ne pourront pas le faire.

     sudo /etc/init.d/networking restart

#### Solution (installation)

Suivre le tutoriel comme indiqué. Puis, on va créer 2 scripts (qui ne
pourront être lancés qu'avec les droits d'admin) qui permettront (aux
parents avec droits d'admin) d'activer ou de désactiver OpenDNS
(attention pour toutes les sessions ouvertes) à volonté.

Création du script d'activation:

     sudo gedit /usr/sbin/opendnsEnable

mettre a l'intérieur les lignes suivantes:

     #!/bin/bash

    #Get and set the OpenDNS settings
    wget -O - -q --http-user=opendnslogin --http-passwd=opendnspassword https://updates.opendns.com/nic/update
    cp /etc/resolv.child /etc/resolv.conf

    #Restart the network to take the new settings into account
    /etc/init.d/networking restart

Création du script de désactivation:

     sudo gedit /usr/sbin/opendnsDisable

mettre a l'intérieur les lignes suivantes:

     #!/bin/bash

    cp /etc/resolv.adult /etc/resolv.conf

    #Restart the network to take the new settings into account
    /etc/init.d/networking restart

Donner les bons droits aux scripts:

     sudo chown root:root /usr/sbin/opendnsEnable
    sudo chown root:root /usr/sbin/opendnsDisable
    sudo chmod 755 /usr/sbin/opendnsEnable
    sudo chmod 755 /usr/sbin/opendnsDisable

#### Utilisation

Pour désactiver (temporairement) openDNS, il faut lancer :

     gksudo opendnsDisable

Et ensuite le réactiver (ne pas oublier) avec:

     gksudo opendnsEnable

Le plus simple ensuite d'utilisation est de créer des lanceurs.

**Attention**: les changements ne sont pris en compte par Firefox (et
les autres navigateurs internet ?) qu'après un redémarrage du programme.

## Proxy

Dans le menu Système \\ Préférences \\ Serveur Mandataire

On peux aussi mettre à jour la variable d'environnement:

     export http_proxy=http://utilisateur:motdepasse@monproxy:leport

Certaines applications n'utilisent pas cette configuration générale,
et/ou permettent de configurer un proxy particulier pour cette
application:

- Firefox : dans les options
- Synaptic: dans les options
- apt-get: Utilise la variable d'environnement
- wget: Modifier (en root / sudo) le fichier /etc/wgetrc:
  - http_proxy =
    [http://utilisateur:motdepasse@monproxy:leport](http://utilisateur:motdepasse@monproxy:leport)
  - proxy = on (ou utiliser l'option de commande -Y yes)
- Eclipse: dans les options
- RapidSVN: editer en root le fichier /etc/subversion/servers et
  modifier la section \[global\]
- AmaroK (sous Gnome, donc Ubuntu), modifier le fichier
  ~/.kde/share/config/kioslaverc et rajouter les lignes suivantes:
  - \[Proxy Settings\]\[\$i\]
  - ProxyType=1
  - httpProxy=[http://utilisateur:motdepasse@monproxy:leport](http://utilisateur:motdepasse@monproxy:leport)
  - httpsProxy=[http://utilisateur:motdepasse@monproxy:leport](http://utilisateur:motdepasse@monproxy:leport)
  - ftpProxy=[http://utilisateur:motdepasse@monproxy:leport](http://utilisateur:motdepasse@monproxy:leport)

Pour OpenSUSE 11.2, éditer le fichier /etc/sysconfig/proxy en root
(apparemment le GUI "Serveur mandataire ne met pas ce fichier à jour qui
est utilisé par YaST - gestionnaire de paquets)

## Installer un modem SpeedTouch USB

Le guide ici :
<http://doc.ubuntu-fr.org/materiel/modem_adsl_speedtouch_330_speedtouch_ng>

Pour 9 Telecom : PPPoE, 8.35 . Nécessite donc d'installer br2684ctl,
puis speedtouch-ng. Pour Edgy Eft (aussi pour dapper, mais je n'en n'ai
pas eu besoin), lancer ensuite les fixs (update-rc.d). Redémarrer et
c'est bon.

Pour revenir en Wifi (ou autre connexion), désinstaller speedtouch-ng,
configurer la nouvelle connexion à utiliser. Un redémarrage du système
peux être nécessaire.

------------------------------------------------------------------------

Retour à [Misc](Misc)
