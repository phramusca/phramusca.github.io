# BOINC

BOINC est un gestionnaire de projets de calcul partagé. En gros, ce programme permet de participer à des programmes de recherche, en donnant du temps de calcul de son ordinateur (lorsque celui-ci est inactif seulement). Le premier programme grand public a été SEITI@Home, un programme de recherche de signaux extraterrestres. Depuis, de nombreux autres projets ont vu le jour, en climatologie, medecine, ...

- Gérer son compte: http://boincstats.com/bam/
- Les projets: https://boinc.berkeley.edu/projects.php

TODO: Comment lancer `boinc` ? 
 - Créé des fichiers à l'emplacement ou il est lancé :(
 - Pb avec gui_rpc_auth.cfg au lancement du GUI
 - Pb: Le gui ne lance pas `boinc` tout seul comme il devrait

## Attacher des projets

Après avoir créé un compte BAM, il faut pour attacher ou réattacher des projets: - Aller dans le menu du site de BAM et choisir "Gestion Ressources" - Cocher "Rattache par defaut ?" - Resynchroniser le BOINC manager avec BAM.

## Invalid Password ?

Si tu as une erreur "invalid password" au démarrage de BOINC, alors il faut vider le fichier gui_rpc_auth.cfg dans le /home

TODO: Voir https://boinc.berkeley.edu/gui_rpc.php