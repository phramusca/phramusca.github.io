Fcron permet de contôler les tâches planifiées. Il est mieux que cron et
anacron.

Contenu de fcrontab (fcrontab -e)

\# utiliser /bin/bash pour lancer les commandes, quoique puisse indiquer
/etc/passwd

SHELL=/bin/bash

@ 5h /usr/bin/mono
/home/xxxx/Creations/dev/MyBackups/BackupDrives/bin/Release/BackupDrives.exe
--schedule

------------------------------------------------------------------------

Retour à [Programmes](Programmes "wikilink")