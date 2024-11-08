Sous [Linux](Linux "wikilink"), les programmes (logiciels) peuvent êtres
installés de plusieurs manières :

# En utilisant des [paquets](paquet "wikilink")

L'avantage d'[Ubuntu](Ubuntu "wikilink"), ainsi que d'autres
distributions [Linux](Linux "wikilink"), est que la grande majorité des
programmes libres sont disponibles sous forme de
[paquets](paquet "wikilink") sur les [dépôts](dépôt "wikilink") de votre
distribution [Linux](Linux "wikilink") préférée.

Ceci est la méthode à privilégier dans tous les cas, pour plus de
facilité, de sécurité et de compatibilité.

Sous [ubuntu](ubuntu "wikilink"), pour gérer les
[paquets](paquet "wikilink") (installer/désinstaller des programmes), il
y a plusieurs façons:

- soit, depuis le menu de la barre d'outil principale:
  - "Applications\Logithèque Ubuntu"
  - "Système\Administration\Ajouter/supprimer des applications"
- soit utiliser un gestionnaire graphique comme
  [Synaptic](apt://synaptic).
- soit utiliser les liens <apt://> (voir [Système#Liens <apt://>
  (apt-url)](Système#Liens_apt:/_(apt-url) "wikilink")) disponibles sur
  certains sites proposant l'installation de programmes
  [Linux](Linux "wikilink") (comme ce wiki)
- soit utiliser la ligne de commande apt-get dans un terminal.

Ces méthodes sont toutes équivalentes, mais alors que les premières sont
plus faciles pour tout un chacun (débutant ou confirmé), la dernière
(ligne de commande) permet plus de souplesse (à réserver aux
utilisateurs avancés).

*Pour profiter de toutes les mises a jour Standard (mais stable) de
versions d'Ubuntu et non pas seulement des LTS (Long Time Support -
Support à Long Terme), il faut le choisir dans les options de Synaptic*

Pour plus d'information :
<http://doc.ubuntu-fr.org/applications/apt/depots>

`A essayer: easyubuntu (avec `[`Ubuntu`](Ubuntu "wikilink")`) et/ou easykubuntu (K`[`Ubuntu`](Ubuntu "wikilink")`)`

# En compilant les sources

Ceci est la manière originelle d'installer un programme sous
[Linux](Linux "wikilink"), mais est à réserver aux utilisateurs avertis
!!! Dans tous les cas, mieux vaut privilégier l'utilisation de
[paquets](paquet "wikilink") !

Dans la plupart des cas, cela se révèle relativement simple, mais au
moindre petit problème, cela peux vite devenir galère.

[Tutoriel](http://doc.ubuntu-fr.org/tutoriel/compilation)

Note: [Ubuntu](Ubuntu "wikilink") ne permet pas de compiler des sources
par défaut. Pour pouvoir compiler, il faut installer g++ (depuis les
[dépôts](dépôt "wikilink") d'[ubuntu](ubuntu "wikilink"))

*Désinstallation*: pour pouvoir désinstaller un programme compilé avec
les sources, il faut garder les sources au même endroit et lancer

    sudo make uninstall

, ou alors si la commande

    sudo checkinstall

a été utilisée, il suffit de désinstaller le \[paquet\] avec
[Synaptic](Synaptic "wikilink").

------------------------------------------------------------------------

Retour à [Programmes](Programmes "wikilink")