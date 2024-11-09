# Scripts de Backup

**Cette page est obsolète. Pour référence seulement**

## 1.backupAll.sh

```sh
#!/bin/bash

###############################################################
# 1.backupAll.sh :
#   Ce batch appelle:
#       - 2.backupDatabase.sh   pour sauvegarde des bases
#       - 2.backupScript.sh         pour tous les repertoires a sauvegarder. 
###############################################################

pathScript=~/Divers/Nouveau/Backups/1.scripts/
pathScriptComplet=${pathScript}2.backupDatabase.sh

echo "******************************************************************************"
echo "*** Quoi :        Databases"
echo "*** Destination:  /home/xxxx/Divers/Nouveau/Backups/DumpDatabase/"
echo "******************************************************************************"

# ATTENTION: Apparement mysqldump n'aime pas le ~ au lieu de /home/xxxx/ mais ds script seulement !?
sh ${pathScriptComplet} xxxxxxxyyyyy "/home/xxxx/Divers/Nouveau/Backups/2.backups/DumpDatabase/"
sh ${pathScriptComplet} amarok "/home/xxxx/Divers/Nouveau/Backups/2.backups/DumpDatabase/"

echo "******************************************************************************"
echo "*** Quoi :        Fichiers de config du home"
echo "******************************************************************************"

pathScriptComplet=${pathScript}2.backupScript.sh

sh ${pathScriptComplet} ~/.evolution/ ~/Divers/Nouveau/Backups/2.backups evolution -i
#sh ${pathScriptComplet} ~/.gaim/ ~/Divers//NouveauBackups/2.backups gaim
sh ${pathScriptComplet} ~/.gftp/ ~/Divers/Nouveau/Backups/2.backups gftp -i
sh ${pathScriptComplet} ~/.tomboy/ ~/Divers/Nouveau/Backups/2.backups tomboy -i
sh ${pathScriptComplet} ~/Desktop/ ~/Divers/Nouveau/Backups/2.backups Desktop -i
sh ${pathScriptComplet} /usr/share/scite/ ~/Divers/Nouveau/Backups/2.backups scite -i

echo ""
echo "Fin des sauvegardes."
echo ""
echo ""
```

## 2.backupAllHdd.sh

```sh
#!/bin/bash

###############################################################
# 1.backupAllHdd.sh :
#   Ce batch appelle backupScript.sh pour tous les repertoires a sauvegarder. 
###############################################################

if [ $# -ne 1 ]
then
  echo "Merci de préciser le dossier de sauvegarde."
  exit
fi

pathArchiveTo=$1
pathScript=~/Divers/Nouveau/Backups/1.scripts/

#Sauvegarde BackupAll
pathScriptComplet=${pathScript}1.backupAll.sh

sh ${pathScriptComplet}

echo "******************************************************************************"
echo "*************  Sauvegarde du disque 'DATA' sur HDD ***************************"
echo "******************************************************************************"

echo "******************************************************************************"
echo "*** Quoi :        Dossier du home"
echo "*** Destination:  Hdd externe ($1)"
echo "******************************************************************************"

#Sauvegarde les répertoires choisis du home
pathScriptComplet=${pathScript}2.backupScript.sh

sh ${pathScriptComplet} ~/Creations/Nouveau/ ${pathArchiveTo} Creations
sh ${pathScriptComplet} ~/Divers/Nouveau/ ${pathArchiveTo} Divers
sh ${pathScriptComplet} ~/Images/Nouveau/ ${pathArchiveTo} Images
sh ${pathScriptComplet} ~/Installs/Nouveau/ ${pathArchiveTo} Installs
sh ${pathScriptComplet} ~/Musique/Nouveau/ ${pathArchiveTo} Musique
sh ${pathScriptComplet} ~/Transfert/Nouveau/ ${pathArchiveTo} Transfert
sh ${pathScriptComplet} ~/Video/Nouveau/ ${pathArchiveTo} Video

echo ""
echo "Fin des sauvegardes."
echo ""
echo ""

read -p "Appuie sur 'EntrÃ©e' pour fermer."
```

## 2.backupScript.sh

```sh
#!/bin/bash

###############################################################
# 2.backupScript.sh : 
#   Ce batch sauvegarde un repertoire ($1) en mode synchronisé (--del): $2/$3
#   Usage: sh 2.backupScript.sh <Source> <Destination> <Nom du dossier destination> <Option>
#     Option -i : Mode incrémental en plus, dans répertoire "<Nom du dossier destination>-Incr"
###############################################################

if [ $# -lt 3 ]
then
  echo "Usage: sh 2.backupScript.sh <Source> <Destination> <Nom du dossier destination>"
  exit
fi

nameLogFile="$(date +%Y%m%d%H%M%S).$3.log"
pathLogFile="/home/xxxx/Divers/Nouveau/Backups/1.scripts/Logs/${nameLogFile}"
dateDuJour="$(date +%Y%m%d%H%M%S)"

echo "Source:   $1"
echo "Destination:  $2/$3/"
echo "Log:      ${nameLogFile}"
echo "Syncronisation en cours ..."

rsync -aq --delete $1 $2/$3/ > ${pathLogFile} 2>&1
if [ "$?" = "0" ] 
then
    echo "  RÃ©sultat: Pas d'erreurs. LOG supprimÃ©"
    rm ${pathLogFile}
else
    echo "---------------------------------------" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
    echo "Date:${dateDuJour}" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
    echo "Mode Syncronisation:" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
    echo "  Source:     $1" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
    echo "  Destination:    $2/$3/\n" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
    cat ${pathLogFile} >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
    echo "---------------------------------------" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
    #rm ${pathLogFile}
    echo "  RÃ©sultat: !! ERRREURS !! Voir LOG sur le bureau !"
fi

# Mode incrémental en option (-i)
if [ "$4" = "-i" ]
    then
        echo "Mode incrÃ©mental en cours ..."
        nameLogFile=${nameLogFile}"-Incr"
        pathLogFile=${pathLogFile}"-Incr"
        rsync -aq $1 $2/$3-Incr/ > ${pathLogFile} 2>&1
        #2>&1
        if [ "$?" = "0" ] 
        then
            echo "  RÃ©sultat: Pas d'erreurs. LOG supprimÃ©"
            rm ${pathLogFile}
        else
            echo "---------------------------------------" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
            echo "Date:${dateDuJour}" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
            echo "Mode Incrémental:" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
            echo "  Source:     $1" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
            echo "  Destination:    $2/$3/\n" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
            cat ${pathLogFile} >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
            echo "---------------------------------------" >> ~/Desktop/!!!--ERREURS-Backups--LISEZMOI!!!
            #rm ${pathLogFile}
            echo "  RÃ©sultat: !! ERRREURS !! Voir LOG sur le bureau !"
        fi
    fi

echo "------------------------------------------------------------------"
```

## 2.backupDatabase.sh

```sh
#!/bin/bash

###############################################################
# 1.backupDatabase.sh
#   Ce batch sauvegarde une base de données <Database name> dqns <Destination>
#   (Compatibilité MySQL 4.0, puis comprÃ©ssÃ© en bzip2)
#       Usage: sh 2.backupDatabase.sh <Database name> <Destination>
###############################################################

if [ $# -lt 2 ]
then
  echo "Usage: sh 2.backupDatabase.sh <Database name> <Destination>"
  exit
fi

dateDuJour="$(date +%Y%m%d%H%M%S)"
nameDumpFile="$1/$(date +%u).$(date +%A)/$(date +%H)"
pathDumpFile=$2

echo "Sauvegarde de la base $1 en cours ..."

mysqldump -u root -pxxxxxxxxxxxxxxxx --opt --compatible=mysql40 $1 > ${pathDumpFile}${nameDumpFile}.sql 

if [ "$?" = "0" ] 
then

    bzip2 -fq ${pathDumpFile}/${nameDumpFile}.sql
    
    if [ "$?" = "0" ] 
    then
        echo "  $1 sauvegardÃ© dans: ${pathDumpFile}${nameDumpFile}.sql.bz2"
        echo "------------------------------------------------------------------"
    else
        echo "Erreur (bzip2). Date:${dateDuJour}\n---------------------------------------" >> ~/Desktop/!!!--ERREURS-Backup-Database--LISEZMOI!!!
        echo "  !! ERRREURS bzip2 !! Voir LOG sur le bureau !"
    fi
else
    echo "Erreur (mysqldump). $1\nDate:${dateDuJour}\n---------------------------------------" >> ~/Desktop/!!!--ERREURS-Backup-Database--LISEZMOI!!!
    echo "  !! ERRREURS mysqldump !! Voir LOG sur le bureau !"
fi
```

## 3.restoreDB.sh

```sh
########################################################################################################
## Utilisation : sh restoreDB.sh <Dump file> <Database name>                                                                                                                                                           ##
## Exemples:                                                                                                                           ##
##  sh ~/Divers/Nouveau/Backups/1.scripts/3.restoreDB.sh /home/xxxx/Creations/Nouveau/Internet/DumpDatabase/xxxxxxxyyyyy/1.lundi/01.sql.bz2 xxxxxxxyyyyy  ##
##  sh ~/Divers/Nouveau/Backups/1.scripts/3.restoreDB.sh /home/xxxx/Creations/Nouveau/Internet/DumpDatabase/amarok/3.mercredi./14.sql.bz2 amarok               ##
########################################################################################################


if [ $# -ne 2 ]
then
  echo "Usage: sh restoreDB.sh <Dump file> <Database name>" 
  exit
fi

# Copies the archive dump file to a temp folder
cp $1 ~/restoreDB.sql.bz2

# Un-Bzip the archive dump file
bzip2 -df ~/restoreDB.sql.bz2

# Creates new database
mysql -u root -pxxxxxxxxxxxxxxxx -e 'CREATE DATABASE $2 DEFAULT CHARACTER SET latin1 COLLATE latin1_general_ci'

# Restore the database from the dump file
mysql -u root -pxxxxxxxxxxxxxxxx $2 < ~/restoreDB.sql
rm ~/restoreDB.sql
echo "Database $2 crée avec le fichier $1."
```

Retour à [Sauvegardes et Restauration](Sauvegardes_et_Restauration "wikilink")
