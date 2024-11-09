# LAMP

LAMP (Linux, Apache, Mysql, Php/Perl)

## Installation et Configuration

Se référer à la documentation [lamp sur
ubuntu-fr](http://doc.ubuntu-fr.org/lamp).

[Ma Configuration LAMP](Ma_Configuration_LAMP "wikilink")

## Résolution de problèmes

### MySQL

Pour ma part en général ce sont Amarok ou mon site local (qui utilisent
MySQL) qui m'avertissent d'un problème. J'ai eu 2 problèmes et dans les
2 cas, Amarok ou Php m'ont donné une erreur du genre :

`Can't connect to local MySQL server through socket '/tmp/mysql.sock'`

Pas facile de faire la différence a priori, car dans les 2 cas cela
avait rapport avec l'emplacement des bases de données (normalement
/var/lib/mysql). Heureusement lancer mysql a la main (/etc/init.d/mysql
start) permet d'en savoir plus:

- Dans un cas, c'était un problème d'espace.
- Dans l'autre, un problème de lien vers un dossier inexistant.

#### Problème espace disque

Si lorsque tu démarre mysql, tu as un message du genre:

`/etc/init.d/mysql: ERROR: The partition with /var/lib/mysql is too full!`

Alors, vérifie que le disque en question n'est pas plein (commande df
par ex). Si il n'est pas plein, alors tu as peut être mal lu le message
d'erreur et il peut s'agir d'un problème de lien rompu (voir astuce
ci-dessous).

#### Problème de lien rompu

Le message d'erreur "partition (...) too full" peut être accompagné
d'autres, comme dans l'exemple ci-dessous:

```sh
xxxx@xxxx-desktop:~$ /etc/init.d/mysql start
  df: /var/lib/mysql/.': No such file or directory 
 df: no file systems processed open: Permission denied
 /etc/init.d/mysql: ERROR: The partition with /var/lib/mysql is too full!
```

Dans mon cas, ce dossier était un lien vers un autre dossier sur un
autre disque (voir partie installation dans la page courante). Or
j'avais changé l'emplacement de ces données. Pour résoudre le problème
j'ai recréé le lien pointant vers le bon emplacement.

Il peut aussi s'agir d'un problème de permissions ou plus grave de
dossier effacé ou corrompu. Dans ce dernier cas, une réinstallation de
MySQL peut s'avérer utile, moyennant la perte des bases, d'où l'intérêt
de faire des backups réguliers ;).

------------------------------------------------------------------------

Retour à [Développement Web](Développement_Web "wikilink").
