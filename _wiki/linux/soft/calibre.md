---
layout: software
---

# Calibre

Accès à la [librairie Kobo](https://www.kobo.com/fr/fr/library).

Signaler erreurs Babelio: <https://babelio.freshdesk.com/support/tickets/new> 

## Installation

[Voir l’entrée dans la liste des programmes](../#category-1-bureautique)

## Configuration

- Installer les extensions suivantes depuis `Préférences / Extensions`:
  - [DeDRM](https://github.com/noDRM/DeDRM_tools/releases) pour supprimer les DRM.
    - Dernière version Beta 10.0.9 de 2023
    - ATTENTION: Liste aussi les extraits de livre, venant des livres "Recommandés" par ex. Généralement ils n'ont pas de DRM, mais ce ne sont peut etre pas les seuls.
    - [Guide d'installation](https://www.epubor.com/enlvement-des-drm-avec-calibre.html)
  - [Babelio_db](https://www.mobileread.com/forums/showthread.php?t=349713)
  - [Find Duplicates](https://www.mobileread.com/forums/showthread.php?t=131017)
- **IMPORTANT** Configurer `Télécharger les métadonnées`:
  - **Déselectionner** globalement les champs comme `Note` par ex, pour ne pas voir ses propres données écrasées !
  - Ne garder que Babelio_db, ou déselectionner `étiquettes` des autres..
  - Voir les autres options si besoin

### Envoyer vers le périphérique

Je trouve préférable d'envoyer les livres venant de Calibre dans un dossier spécifique, au lieu d'à la racine directement.

Pour cela, dans `Périphérique/Configurer ce périphérique`, il suffit d'ajouter un dossier dans le `Modèle de sauvegarde`.

Exemple: `calibre/{author_sort}/{title} - {authors}` (au lieu de `{author_sort}/{title} - {authors}` par défaut). Bien sur, il est possible de changer le modèle. Voir la documentation dans Calibre.

> Attention, il ne vaut mieux pas toucher aux dossiers cachés:

```shell
├── .adobe-digital-editions  # Gestion des DRM
├── .kobo                    # Fichiers système de Kobo
│   ├── ...
│   ├── kepub                # Stockage des libres Kobo
│   └── ...
└── .kobo-images             # Un cache des images Kobo a priori
```

TODO: Comment gérer les collections, l'état de lecture (reading, read, ... le %), ... ?

## Calibre web

### OPDS

Le flux OPDS est accessible à l'adresse : `http://rpi5.local:8083/opds`

### calibre-web

<https://phramusca.github.io/wiki/docker/#calibre-web>

<https://github.com/janeczku/calibre-web#calibre-web>

<http://rpi5.local:8083/>

<http://rpi5.local:8083/opds>

### Applications pour lire OPDS sur Android Boox

<https://github.com/janeczku/calibre-web/wiki/FAQ#which-opds-readers-work-with-calibre-web>

Pour accéder au flux OPDS de Calibre-Web sur une liseuse Android Boox, plusieurs applications sont recommandées :

#### **KOReader** (Recommandé pour Boox)

- Open-source, optimisé pour les appareils à encre électronique
- Excellente prise en charge OPDS
- Personnalisation avancée (polices, marges, thèmes)
- Support de nombreux formats (EPub, PDF, MOBI, etc.)
- Synchronisation de la progression de lecture
- Site : <https://koreader.com/>

#### **Moon+ Reader**

- Application populaire avec connexion directe aux catalogues Calibre
- Support OPDS
- Formats : EPub, PDF, MOBI, CHM, CBR, CBZ
- Personnalisation étendue (polices, thèmes, modes de lecture)

#### **ReadEra**

- Interface épurée, sans publicité
- Support OPDS et Calibre
- Formats : EPub, PDF, MOBI, AZW, DJVU, FB2
- Conserve les métadonnées, séries et informations auteurs
- Thèmes et polices personnalisables

#### **Aldiko**

- Support OPDS intégré
- Interface conviviale
- Options de personnalisation

#### **FBReader**

- Open-source, multi-plateforme
- Support OPDS
- Personnalisation (polices, couleurs, marges)

### Configuration OPDS

Pour ajouter le catalogue OPDS dans une application :

1. Ouvrir l'application de lecture
2. Aller dans les paramètres / bibliothèques / catalogues OPDS
3. Ajouter un nouveau catalogue avec l'URL : `http://rpi5.local:8083/opds`
4. Si authentification requise, utiliser les identifiants Calibre-Web

### KOReader

TODO

### calibre2opds: Obsolète

> Attention: pas de mises à jour depuis 2015, version 3.15 (et 2 betas en 2018, non testées) !
>
> => Bien compliqué, plus maintenu, bugs d'affichages, ... mieux vaut utiliser calibre-web

[Repo GitHub](https://github.com/calibre2opds/calibre2opds)

- TODO: Essayer des alternatives:
  - <https://github.com/mikespub-org/seblucas-cops>
  - <https://github.com/janeczku/calibre-web>
  - BicBucStriim: trouver un fork compatbile php de free.fr

- TODO; Reprendre la doc (bien faite) :<https://christophe-rhein.canoprof.fr/eleve/Fabricolages/Comment_creer_une_bibliotheque_numerique_de_3000_livres/activities/biblio_autonome.xhtml> 
  - l'adapter à mes besoins
  - Voir comment exporter que certains tags
  
- TODO: Ajouter un moteur de recherche js (comme sur phramusca.github.io)

TODO , documenter: Support OPDS sur Kobo (fnac) inenviseagable <https://www.liseuses.net/liseuses-opds/> sauf à passer sur une inBook <https://www.liseuses.net/les-liseuses-inkbook-chez-youboox/>

### Installer calibre2opds

- [Télécharger calibre2opds](https://calibre2opds.wordpress.com/downloads/) 3.5-369
- Lancer le fichier `calibre2opds-3.5-369.jar`
- Choisir le dossier d'installation (par défaut: `~/Calibre2opds`)
- Une fois l'installation finie:
  - Corriger le lanceur `rungui.sh`, ligne ``44``:

    ```bash
    if [ "$1" = "-enableassertions" ] || [ "$old" != "$scriptdir" ]; then
    ```

  - Et le rendre executable

    ```shell
    chmod +x ~/Calibre2opds/rungui.sh
    ```

TODO: Lancer avec java8 pour résoudre les problèmes d'encodage de caractères

- Isntaller Java8
  - sudo apt install openjdk-8-jre

- Trouver le chemin
  - update-java-alternatives --list

- Voici un script pour le lancer avec Java 8 sans changer le java par défaut

  ```bash
  #!/bin/bash

  JAVA8_BIN="/usr/lib/jvm/java-1.8.0-openjdk-amd64/bin/java"
  C2O_JAR="$HOME/Calibre2opds/OpdsOutput-3.5-SNAPSHOT.jar"

  # Lancer Calibre2opds avec Java 8
  "$JAVA8_BIN" -jar "$C2O_JAR" &>/dev/null

  ```

### Lancer calibre2opds

  ```shell
  ~/Calibre2opds/rungui.sh
  ```

TODO:

- ~/Documents/04-Creations/Internet/00-Archives -----/0000-raphael.camus-A_CLASSER/2024-Scripts/SiteCalibreUpdate.sh
- ~/Documents/04-Creations/Internet/00-Archives -----/0000-raphael.camus-A_CLASSER/2024-Online/config/calibreUsers.txt
- ~/VirtualBoxes/2023_11_Windows.old__Ebook_save/Users/Test/

#### Problèmes d'images

TODO: On y était presque :(

```shell
✘  ~/Documents/03-Divers/Livres  ./FixImagesForCalibre2opds.sh
=== Nettoyage des images dans : Bibliothèque calibre ===
Sauvegardes dans : backup_covers_20251011_234129
69095 fichiers trouvés.
Traitement: [==============================>] 100% (69095/69095)   ./FixImagesForCalibre2opds.sh: ligne 80: fin de fichier (EOF) prématurée lors de la recherche du « " » correspondant
```

Si vous avez des erreurs sur la lecture de fichiers image, vous pouvez les convertir avec ce script

```bash
#!/bin/bash

# Utilisation : ./FixImagesForCalibre2opds.sh [DOSSIER_CIBLE]
# Par défaut : "Bibliothèque calibre" (dans le dossier courant)

TARGET_DIR="${1:-Bibliothèque calibre}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="backup_covers_$TIMESTAMP"
mkdir -p "$BACKUP_DIR"
COUNT=0

echo "=== Nettoyage des images dans : $TARGET_DIR ==="
echo "Sauvegardes dans : $BACKUP_DIR"

# Compte des fichiers
echo -n "Compte des fichiers: 0"
TOTAL=0
while IFS= read -r -d '' file; do
    ((TOTAL++))
    [ $((TOTAL % 100)) -eq 0 ] && echo -ne "\rCompte des fichiers: $TOTAL"
done < <(find "$TARGET_DIR" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) -print0)

# Efface complètement la ligne et affiche le résultat final
echo -e "\r\033[K$TOTAL fichiers trouvés."

# Deuxième passe pour le traitement
CURRENT=0
LAST_PERCENT=0
files=()
while IFS= read -r -d '' file; do
    files+=("$file")
done < <(find "$TARGET_DIR" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) -print0)

for file in "${files[@]}"; do
    ((CURRENT++))

    # Calcul du pourcentage (limité à 100%)
    PERCENT=$((CURRENT * 100 / TOTAL))
    [ $PERCENT -gt 100 ] && PERCENT=100

    # Traitement des fichiers
    colorspace=$(identify -format "%[colorspace]" "$file" 2>/dev/null)

    if [[ "$colorspace" == "CMYK" ]]; then
        rel_path="${file#$TARGET_DIR/}"
        backup_path="$BACKUP_DIR/$(dirname "$rel_path")"
        mkdir -p "$backup_path"

        echo -e "\n[CONVERSION] $rel_path"
        echo "  Avant : $colorspace"
        convert "$file" -colorspace RGB -strip "$file" 2>/dev/null
        new_colorspace=$(identify -format "%[colorspace]" "$file" 2>/dev/null)
        echo "  Après : $new_colorspace"
        cp "$file" "$backup_path/" 2>/dev/null
        echo "  --> Sauvegardée dans $backup_path/"
        ((COUNT++))
    else
        if file "$file" | grep -qi "PhotometricInterpretation=CMYK"; then
            rel_path="${file#$TARGET_DIR/}"
            backup_path="$BACKUP_DIR/$(dirname "$rel_path")"
            mkdir -p "$backup_path"

            echo -e "\n[NETTOYAGE] $rel_path (métadonnées CMYK)"
            convert "$file" -strip "$file" 2>/dev/null
            cp "$file" "$backup_path/" 2>/dev/null
            echo "  --> Métadonnées nettoyées, sauvegardée dans $backup_path/"
            ((COUNT++))
        fi
    fi

    # Mise à jour de la progression toutes les 100 images ou si le pourcentage change
    if (( CURRENT % 100 == 0 )) || (( PERCENT != LAST_PERCENT )); then
        PROGRESS_BAR=$(printf "%${PERCENT}s" | tr ' ' '=')
        PROGRESS_BAR=${PROGRESS_BAR:0:30}
        echo -ne "\rTraitement: [$PROGRESS_BAR>] ${PERCENT}% ($CURRENT/$TOTAL)   "
        LAST_PERCENT=$PERCENT
    fi
done

echo -e "\n--------------------------------------------------"
echo "Traitement terminé. $COUNT images corrigées sur $TOTAL."

```
