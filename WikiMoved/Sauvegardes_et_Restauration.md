# Sauvegarde et Restauration

## Architecture

4 disques:

- 1 disque / interne ext3 35Go contenant le /home
- 1 disque /media/disk interne ext3 164Go
- 1 disque /media/MyBook externe USB FAT32 466Go MyBook maitre contenant
  tous mes documents (Musique, Videos, ...) et des copies de / et /home
- 1 disque /media/Musiquexxxx externe Ethernet Samba ~500Go contenant
  une copie du disque MyBook

Rien n'est stocké dans le home (disque système), mais il y a des liens
dans le home vers disque MyBook:

Le répertoire */home/xxxx/Divers/Nouveau/Backups/1.scripts/* contient
des [Scripts de Backup](Scripts_de_Backup "wikilink"). Il contient aussi
un tableau récapitulant l'organisation et backups de mes disques

**Utiliser le cron (http://doc.ubuntu-fr.org/cron et l'interface Kcron
pour configurer plus facilement)**

    voir aussi gnome-schedule
    ou manuellement: [http://www.jkconception.com/dotclear/index.php/2007/07/09/21-les-crons-ou-les-taches-planifiees-sous-linux](http://www.jkconception.com/dotclear/index.php/2007/07/09/21-les-crons-ou-les-taches-planifiees-sous-linux)

**ESSAYER D'UTILISER rdiff-backup A LA PLACE DE rsync**

## IMPORTANT - ATTENTION

'''Certaines actions ne sont pas gérées par les scripts de backup, et
doivent donc être faite manuellement:

- synchroniser la base locale avec la base distante manuellement:
  [Sauvegardes MySQL](Sauvegardes_MySQL "wikilink")
- mettre a jour SVN (Subversion).

------------------------------------------------------------------------

Retour à [Perso](Perso "wikilink").
