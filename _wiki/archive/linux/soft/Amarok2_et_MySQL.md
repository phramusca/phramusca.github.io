---
layout: default
---

# Amarok2 et MySQL

**Apparemment, dans la version 2.2 et + [Amarok](../Amarok) gère
ceci lui-même comme dans la version 1.4**

Source originale: <http://forum.ubuntu-fr.org/viewtopic.php?id=280537>

Je conseillerai de faire avant tout une sauvegarde d'un éventuel dossier
amarok dans /var/lib/mysql (genre la base de la version 1.x), avec:

`sudo mv /var/lib/mysql/amarok /var/lib/mysql/amarok1-Backup`

La technique consiste donc à déplacer le dossier amarok dans ce dossier
:

`sudo cp -r ~/.kde/share/apps/amarok/mysqle/amarok /var/lib/mysql/`

Il faut ensuite supprimer le dossier une fois copié:

`sudo rm ~/.kde/share/apps/amarok/mysqle/amarok`

Ensuite, créer un lien symbolique vers ce dossier déplacé :

`ln -s /var/lib/mysql/amarok ~/.kde/share/apps/amarok/mysqle/`

Normalement, à cette étape, si vous redémarrez
[Amarok](../Amarok), tout doit fonctionner ! Le seul problème
c'est que le serveur mySQL (en particulier au travers de phpmyadmin) ne
peut pas accéder aux fichiers de la base de données pour des questions
de droits (on voit la base dans phpmyadmin mais on ne peut pas accéder
aux tables). Ma solution a donc été de brutalement appliquer des chmod
sur le dossier amarok (rwx pour le dossier lui-même et rw pour les
fichiers du dossier si mes souvenirs sont bons).

Voilà normalement, vous devriez alors avoir une base à la fois
accessible via MySQL/phpmyadmin et amarok !

NB: Parfois des MAJ de la base via amarok ne sont pas prises en compte
tout de suite dans phpmyadmin. Dans ce cas, un reboot du serveur SQL
permet de résoudre le problème : Code:

`sudo /etc/init.d/mysql restart`

------------------------------------------------------------------------

Retour à [Amarok](../Amarok)