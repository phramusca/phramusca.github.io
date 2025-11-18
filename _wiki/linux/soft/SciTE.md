---
layout: software
---

# SciTE

## Documentation

<http://scintilla.sourceforge.net/SciTEDoc.html>

## Options

Les options se configurent dans des fichiers:

- Options / "Open Global Options File" pour la config globale
  (multi-utilisateur). Nécessite d'être super-utilisateur
- Options / "Open User Options File" pour la config de l'utilisateur
  courant. **Recommandé**

Voici ma configuration:

    #Pour activer l'auto-complétion:
    autocompleteword.automatic=1

    #Pour n'avoir qu'une seule instance:
    check.if.already.open=1

    #Pour ajouter recherche récursive et insensibilité à la casse:
    find.command=grep -r -i --line-number "$(find.what)" $(find.files)

    #Pour une division de l'écran horizontale:
    split.vertical=0

    #Pour changer le type de fichier à rechercher/ouvrir par défaut:
    find.files=*.c *.cxx *.h *.php
    source.files=*.php *.js

    #Pour avoir UTF-8 par défaut:
    code.page=65001

------------------------------------------------------------------------

Retour à [Programmes](Programmes)
