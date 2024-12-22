---
layout: default
excerpt: Utiliser des touches différentes pour naviguer dans Recalbox avec le clavier.
title: Remapper le clavier dans Recalbox
---

# Remapper le clavier dans Recalbox

J'ai installé Recalbox sur un vieux PC portable. Malheureusement de nombreuses touches du clavier ne fonctionnent plus et d'autres pas très bien.

Afin de ne pas avoir à utiliser un clavier externe, j'ai voulu remapper (reconfigurer) les touches du clavier pour une utilisation dans l'interface de Recalbox (EmulationStation).

Voici les [touches clavier utilisées](https://wiki.recalbox.com/fr/tutorials/others/emulationstation-use-with-keyboard-and-mouse#commandes-du-clavier):

| Manette | Clavier       |
| ------- | ------------- |
| Start   | Entrée        |
| Select  | Espace        |
| L1      | Page Up (⇞)   |
| R1      | Page Down (⇟) |
| Hotkey  | Échap         |
| A       | S             |
| B       | A             |
| X       | P             |
| Y       | L             |

> - Cette configuration n'est utile que dans l'interface de Recalbox, PAS dans les jeux. 
>    - Pour mapper le clavier sur la manette (jeux ordinateurs nécessitant un clavier), voir [Pad To Keyword](https://wiki.recalbox.com/fr/advanced-usage/pad-to-keyboard)
>    - Pour configurer le clavier dans les jeux, voir le [Wiki de Recalbox](https://wiki.recalbox.com/fr/home). C'est peut-être possible mais par émulateur. Recalbox est fait pour utiliser des manettes.
>    - Au fait, les boutons `X` et `L1` ne servant pas dans l'interface, pourquoi les mapper ?

> Je ne sais pas à quoi sert `hotkey"` puisque dans la conf initiale, j'ai `Espace` et dans ma configuration la touche `*` mais c'est toujours `Escape` qui est utilisé pour sortir d'un jeu.

1. Tester les touches du clavier
    - Connecter recalbox en ssh
    - Stopper interface graphique

        ```shell
        /etc/init.d/S31emulationstation stop
        ```

    - Tester le clavier
        - Lancer `evtest` pour lister les périphériques
        - Choisir le clavier dans la liste
        - Tester les touches
    
    - Redémarrer l'interface:

        ```shell
        /etc/init.d/S31emulationstation start
        ```

2. Modifier le fichier de configuration:

    ```shell
    nano /recalbox/share/system/.emulationstation/es_input.cfg
    ```

    - Par défaut, j'avais

        ```xml
        <inputConfig type="keyboard" deviceName="Keyboard" deviceGUID="-1" deviceNbAxes="0" deviceNbHats="0" deviceNbButtons="120">
            <input name="a" type="key" id="115" value="1" code="168" />
            <input name="b" type="key" id="97" value="1" code="168" />
            <input name="y" type="key" id="108" value="1" code="168" />
            <input name="x" type="key" id="112" value="1" code="168" />
            <input name="down" type="key" id="1073741905" value="1" code="168" />
            <input name="hotkey" type="key" id="32" value="1" code="168" />
            <input name="left" type="key" id="1073741904" value="1" code="168" />
            <input name="pagedown" type="key" id="1073741902" value="1" code="168" />
            <input name="pageup" type="key" id="1073741899" value="1" code="168" />
            <input name="right" type="key" id="1073741903" value="1" code="168" />
            <input name="select" type="key" id="32" value="1" code="168" />
            <input name="start" type="key" id="13" value="1" code="168" />
            <input name="up" type="key" id="1073741906" value="1" code="168" />
        </inputConfig>
        ```

    - Je voulais reconfigurer ainsi, trouvant les bon ids (Decimal Value) pour chaque touche dans le [KeyCode SDL](https://wiki.libsdl.org/SDL2/SDLKeycodeLookup)

    | Manette | Clavier   | id         | SDL              |
    | ------- | --------- | ---------- | ---------------- |
    | A       | P         | 112        | SDLK_p           |
    | B       | L         | 108        | SDLK_l           |
    | X       | O         | 111        | SDLK_o           |
    | Y       | K         | 107        | SDLK_k           |
    | Start   | N         | 110        | SDLK_n           |
    | Select  | B         | 98         | SDLK_b           |
    | L1      | ç         | 57         | SDLK_9           |
    | R1      | à         | 48         | SDLK_0           |
    | Hotkey  | *         | 1073741909 | SDLK_KP_MULTIPLY |
    | Up      | A         | 97         | SDLK_a           |
    | Down    | Q         | 113        | SDLK_q           |
    | Left    | Caps Lock | 1073741881 | SDLK_CAPSLOCK    |
    | Right   | S         | 115        | SDLK_s           |

    - Ce qui donne au final:

        ```xml
        <inputConfig type="keyboard" deviceName="Keyboard" deviceGUID="-1" deviceNbAxes="0" deviceNbHats="0" deviceNbButtons="120">
            <input name="a" type="key" id="112" value="1" code="168" />
            <input name="b" type="key" id="108" value="1" code="168" />
            <input name="y" type="key" id="107" value="1" code="168" />
            <input name="x" type="key" id="111" value="1" code="168" />
            <input name="down" type="key" id="113" value="1" code="168" />
            <input name="hotkey" type="key" id="1073741909" value="1" code="168" />
            <input name="left" type="key" id="1073741881" value="1" code="168" />
            <input name="pagedown" type="key" id="48" value="1" code="168" />
            <input name="pageup" type="key" id="57" value="1" code="168" />
            <input name="right" type="key" id="115" value="1" code="168" />
            <input name="select" type="key" id="98" value="1" code="168" />
            <input name="start" type="key" id="110" value="1" code="168" />
            <input name="up" type="key" id="97" value="1" code="168" />
        </inputConfig>
        ```

    - Ensuite, redémarrer l'interface:
        
        ```shell
        /etc/init.d/S31emulationstation restart
        ```
