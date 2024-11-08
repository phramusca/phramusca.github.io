Les scripts de backup font une sauvegarde de la base de données avec
mysqsldump.

(Ces scripts sauvegardent également les sauvegardes faites par le site
local et distant.)

**Par contre, il faut impérativement faire des sauvegardes régulières de
la base distante sur le site distant !!**

## Avec mon site Web

- Le site distant et le site local peuvent gérer la sauvegarde de base
  (backupDB.php).
- Le site local permet aussi de restaurer des bases (dosql.php).

### Sauvegarde

- Faire une sauvegarde de la base distante (xxxxxxx.yyyyy) (sur
  <http://xxxxxxx.yyyyy.free.fr>)
- Synchroniser la base locale (xxxxxxxyyyyy) avec la sauvegarde de la
  base distante (sur web local)
- Faire des sauvegardes des bases locale (xxxxxxx et amarok) (sur
  web local)

### Restauration

- Avec PhPMyAdmin en local: créer une base "xxxxxxxyyyyy" (collation
  "latin1_general_ci", ou utiliser "ALTER DATABASE \`xxxxxxxyyyyy\`
  DEFAULT CHARACTER SET latin1 COLLATE latin1_general_ci" pour la
  changer.)
- Importer avec doSQL
- idem pour Amarok

## Avec script de backup

Les [Scripts de Backup](Scripts_de_Backup "wikilink") font aussi une
sauvegarde de la base, mais en utilisant mysqldump. L'avantage est que
ces sauvegardes peuvent être programmées avec cron. Voir [Sauvegardes et
Restauration](Sauvegardes_et_Restauration "wikilink") pour les détails.

------------------------------------------------------------------------

Retour à [Sauvegardes et
Restauration](Sauvegardes_et_Restauration "wikilink")