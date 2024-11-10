# Visualiseurs Alternatifs

Un aperçu : <http://www.coagul.org/article.php3?id_article=531>

Avant d'opter pour [Gwenview](Gwenview), j'ai essayé
plusieurs logiciels. Les voici : (trouver le plus rapide. Vérifier
conservation données EXIF)

| Nom            | Version testée           | EXIF              | Édition                            | Vue dossiers | Diaporama           | Catégories                                          | Plus                                                       | Interface   | [apt-url](Apt-url) (Installation) |
|----------------|--------------------------|-------------------|------------------------------------|--------------|---------------------|----------------------------------------------------|------------------------------------------------------------|-------------|------------------------------------|
| Eye of Gnome   | 2.28.1 (04/02/2010)     | Lecture           | Rotation *                         | Non          | Oui *               | Non                                                | Celui par défaut de [Ubuntu](Ubuntu), simple et efficace. | Bonne       | par défaut                        |
|                |                          |                   |                                    |              |                     |                                                    | N'enregistre pas les images modifiées par défaut.         |             |                                    |
|                |                          |                   |                                    |              |                     |                                                    | Diaporama seulement en plein écran.                        |             |                                    |
|                |                          |                   |                                    |              |                     |                                                    | Greffons disponibles (comment les trouver/installer ?).  |             |                                    |
|                |                          |                   |                                    |              |                     |                                                    | Panneau latéral grisé (besoin de greffon(s) ?).          |             |                                    |
| Gwenview       | ??? (A refaire)         | Visualisation en installant le paquet kdegraphics-kfile-plugins. | Edition du commentaire seulement. | Oui          | Fenetre ou plein ecran | Non                                                | Utilise les Kipi                                          | Bonne       | [gwenview](apt://gwenview)         |
|                |                          |                   |                                    |              |                     |                                                    | *A tester : modules Kipi*                                   |             |                                    |
| GQview         | ??? (A refaire)         | Lecture           | Rotation. Envoi dans editeur externe. | Oui          | Oui, fenêtre ou plein écran. Récursif possible. | Mots-clefs (sauvegardés dans $HOME/.gqview/metadata)    | Recherche doublons                                      | Bonne !     |                                    |
|                |                          |                   |                                    |              |                     |                                                    | (Plutôt lent)                                             |             |                                    |
| Gthumb         | ??? (A refaire)         | Lecture           | Rotation, Luminosité, Découper, améliorer, .... Envoi dans editeur externe. | Oui          | Oui, fenêtre ou plein écran. | Oui (dans .comments du répertoire courant)           | Recherche doublons. Création image index. Création album Web | Moins pratique que GQview, mais édition avancée et modification date EXIF. |                                    |
|                |                          |                   |                                    |              |                     |                                                    | (à tester : les différentes fonctions d'édition)       |             |                                    |
| F-Spot         | ??? (A refaire)         | Lecture. Modification avancée de la date (à comparer avec JBrout). | Rotation, couleurs, netteté.       | Fonctionnement obligatoire par album (import des photos avec copie locale ou non) | Oui, seulement en plein écran.                          | Oui (gestion ?)                                   | Explorations (Flickr, PicasaWeb ou "Gallery", "Original Photo Gallery", HTML, dossier) | Semblable à Picasa.                                       |                                    |
|                |                          |                   |                                    |              |                     |                                                    | (mode gestionnaire - A tester : fonctions export album) Aide dispo ici : [http://f-spot.org/User_Guide](http://f-spot.org/User_Guide) |                                    |
| Jbrout         | 0.2                      | Lecture (en affichage plein écran). Modification avancée de la date (à comparer avec F-Spot). | Rotation                            | Fonctionnement obligatoire par albums (ajout de dossiers virtuels) | Oui, seulement en plein écran avec infos EXIF. | Oui (gestion ?)                                   | Export PicasaWeb, HTML, dossier                             | Sobre       |                                    |
|                |                          |                   |                                    |              |                     |                                                    | Attention, pas encore stable (version 0.2)                |             |                                    |
| digikam        | ??? (A refaire)         | ?                 | Utilise les Kipi.                  | ?            | ?                   | ?                                                  | Utilise les Kipi                                          | ?           |                                    |
|                |                          |                   |                                    |              |                     |                                                    | *pas mal. pourquoi il recopie les albums dans un dossier albums ? permet de modifier la date et d'ajouter des commentaires* |             |                                    |
| kimdaba        | ??? (A refaire)         | ?                 | Utilise les Kipi.                  | ?            | ?                   | ?                                                  | Utilise les Kipi                                          | ?           |                                    |
|                |                          |                   |                                    |              |                     |                                                    | *id digikam ? modif date, et ajouts onglets, descr, ...* |             |                                    |


## Trouver installation et tester

- KuickShow (simple et rapide). Pas dans synaptic ? quel Depot ?
- mapivi : a tester. Pas dans synaptic ? quel Depot ?
- showimg : impossible a installer ! (jalix.org)

------------------------------------------------------------------------

Retour à [Programmes](Programmes)
