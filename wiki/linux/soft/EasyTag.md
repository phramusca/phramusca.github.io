# EasyTag

TODO: Revoir

Logiciel d'éditions des tags MP3 (ID3) très complet.

## Configuration

- Onglet "Divers":
  - Lecteur audio: amarok -p
  - Position des boîtes de dialogue: Position de la souris.
- Onglet "Paramètre du nom des fichiers"
  - Cocher "Changer la date de modification du répertoire parent au
    fichier (recommandé si utilisation d'Amarok)
- Onglet "Paramètres des tags ID3"
  - Pour :
    - éviter un bug avec Amarok
      (<http://forum.ubuntu-fr.org/viewtopic.php?pid=1808988#p1808988> et
      <http://bugs.kde.org/show_bug.cgi?id=151657>)
    - pouvoir avoir les pochettes et le genre sur Archos Gmini 402,
      voici ma config :
      - EasyTag 2.1.4, utilisation de v2.3 UTF16 (ou éventuellement
        ISO-8859-1) sans V1
      - Pochette: JPEG (taille critique constatée 815 Ko, a paufiner).
        Attention, si le MP3 était originalement écrit en v2.4, il faut
        enlever la pochette, enregistrer puis la réinsérer (et
        enregistrer à nouveau bien sur).
