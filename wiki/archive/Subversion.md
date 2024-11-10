# SubVersion

[Subversion](http://doc.ubuntu-fr.org/subversion) (abrégé SVN) est un système de gestion de versions visant à remplacer CVS.

[Installation](apt://subversion)

## RapidSVN

[RapidSVN](apt://rapidsvn) est un GUI pour SVN. (sous windows, je recommande TortoiseSVN)

Cependant, il ne permet pas de créer des repository SVN. Pour cela, il faut lancer en ligne de commande:

    sudo svnadmin create /var/svn/projet1

*A essayer aussi, SVN intégré dans nautilus:*

`sudo apt-get install nautilus-script-collection-svn`

`nautilus-script-manager enable Subversion`

## SVN par le web

- Configuration avec Apache (**A TESTER**):
  - <http://doc.ubuntu-fr.org/subversion>
  - <http://hikage.developpez.com/linux/tutoriels/subversion/?page=page_2#LII-D-3>
  - <http://www.toutprogrammer.com/wiki/Installation_et_utilisation_de_base_de_Subversion#Cr.C3.A9ation_et_configuration_d.27un_r.C3.A9f.C3.A9rentiel>
  - <http://www.vogelweith.com/debian_server/09_subversion.php#x1-80003.1>
- USVN: <http://linuxfr.org/2007/05/30/22561.html>