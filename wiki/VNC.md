# VNC

VNC est installé par défaut dans Ubuntu.

## Client

Pour se connecter à un autre PC:

`vncviewer <Ip ou nom>:<port>`

(ex: vncviewer xxxx-desktop:0)

## Serveur

Pour permettre à d'autres ordinateurs de se connecter, lancer
"Système\Préférences\Bureau à distance"

**Attention: VNC (vino-server) peut bouffer toutes les ressources CPU
!?**

### IP non-fixe

(c'est le cas de la majorité d'entre nous)

La solution est d'utiliser un DNS dynamique
(http://doc.ubuntu-fr.org/serveur/dns_dynamique).

Le plus connu, car notamment gratuit, en plus d'être performant est
DynDNS.

Plus d'informations sur sa configuration :
<http://www.andesi.org/index.php?node=135>

Résumé de la configuration :

1. Inscription sur le site :
    <https://www.dyndns.com/account/create.html>
2. Paramètres à saisir pour configurer un routeur :
    1. Fournisseur de service DNS dynamique : `www.dyndns.org`
    2. Noms de domaine de DNS dynamique :
        <ce_que_vous_avez_choisi>.dyndns.org
    3. Identifiant pour le service de DNS dynamique : le login de votre
        compte sur le site `www.dyndns.org`
    4. Mot de passe pour le service de DNS dynamique : le mot de passe
        de votre compte sur le site `www.dyndns.org`
    5. Interface du service de DNS dynamique: eth0 ou ppp0 ou ... selon
        la configuration système de votre connexion internet

------------------------------------------------------------------------

Retour à [Programmes](Programmes)
