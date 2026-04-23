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

TODO: Tester ça sur le boox

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

### Configuration OPDS

Pour ajouter le catalogue OPDS dans une application :

1. Ouvrir l'application de lecture
2. Aller dans les paramètres / bibliothèques / catalogues OPDS (selon l'application)
3. Ajouter un nouveau catalogue avec l'URL : `http://rpi5.local:8083/opds`
4. Si authentification requise, utiliser les identifiants Calibre-Web

### Applications pour lire OPDS sur Android Boox

TODO: Tester ces applications sur le boox

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
