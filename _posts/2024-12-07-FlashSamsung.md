---
layout: content
excerpt: Comment remmetre le système à zéro avec la dernière image officielle ou avec LineageOS. 
title: Flash tablette Samsung Galaxy Note 10.1 (SM-P600) avec image officielle ou avec LineageOS.
---

# Flash Samsung Galaxy Note 10.1 (SM-P600)

## Pour remettre à zéro avec la dernière image officielle:

- Installer Heimdall
    ```
    sudo apt update
    sudo apt install adb fastboot heimdall-flash
    ```
- Télécharger le dernier firmware sur [samfw.com](https://samfw.com/firmware/SM-P600/XEF)
    - Dézipper SAMFW.COM_SM-P600_XEF_P600XXSDRI1_fac.zip
        - Dézipper les 3 tar dans un dossier `firmware` par ex, pour avoir:
            - boot.img
            - cache.img
            - hidden.img
            - LT03WIFI_EUR_OPEN.pit
            - param.bin
            - recovery.img
            - sboot.bin
            - system.img
- Sur la tablette, passer en mode download:
    - Appuyer quelques secondes sur `Volume bas` (le plus près de Power) `+ Home + Power`
    - Comme indiqué, appuyer sur `Volume haut` pour confirmer
- Depuis le dossier `firmware`, lancer:
    ```
    sudo heimdall flash --BOOT boot.img --SYSTEM system.img --RECOVERY recovery.img --CACHE cache.img --HIDDEN hidden.img --PIT LT03WIFI_EUR_OPEN.pit
    ```
 - Et voila, la tablette devrait rebooter comme en sortie d'usine

> Vérifier la connexion à la tablette: `sudo heimdall detect`
>
> Passer en mode recovery: `Volume haut` (le plus éloigné de Power) `+ Home + Power`. Pour un faire un wipe data/recovery par example.

## Mettre une version plus récente mais non-officielle (LineageOS)

1. Pré-requis

    1. Télécharger un custom recovery :
        Le recovery par défaut de Samsung ne permet pas d'installer des ROMs personnalisées. Vous devrez installer TWRP (Team Win Recovery Project), qui est un recovery custom.
        Pour SM-P600:  [samsunggalaxynote1012014exynos.html](https://twrp.me/samsung/samsunggalaxynote1012014exynos.html).

    1. Télécharger une ROM personnalisée. 
        Pour SM-P600:  [https://wiki.lineageos.org/devices/n1awifi/](https://wiki.lineageos.org/devices/n1awifi/)
        Mais plus officiellement supporté. Trouvé ceci à la place: https://xdaforums.com/t/rom-unofficial-lineageos-17-1-for-sm-p600.4471521/

    1. Télécharger les GApps : https://sourceforge.net/projects/opengapps/files/arm/20220215/open_gapps-arm-10.0-stock-20220215.zip/download?use_mirror=freefr&r=&use_mirror=autoselect
        Les ROMs personnalisées ne contiennent généralement pas les applications Google (Play Store, etc.).
        Téléchargez les GApps compatibles avec la version d'Android que vous installez via OpenGApps.

    1. Charge complète de la tablette :
        Assurez-vous que la tablette a au moins 80 % de batterie.

    1. Un ordinateur fonctionnel :
        Vous utiliserez votre PC pour installer TWRP.

1. Installer TWRP

    1. Mettre la tablette en mode Download :
        Éteignez-la, puis maintenez les boutons Volume Bas + Home + Power.

    1. Flasher TWRP:
         ```
         sudo heimdall flash --RECOVERY twrp-2.7.1.1-lt03wifiue.img --no-reboot
         ```

    1. Redémarrer en mode Recovery immédiatement :
        Eteindre en laissant appuyer sur Power
        redémarrer directement en mode Recovery en maintenant `Volume Haut + Home + Power`. Cela évite que le recovery par défaut écrase TWRP.

1. Copier les fichiers sur la tablette

    Connectez la tablette à votre PC en mode Recovery TWRP.
    Montez le stockage de la tablette :
        Dans TWRP, allez dans Mount > activez USB Storage.
    Copiez la ROM et les GApps sur la mémoire interne ou une carte SD.
    
3. Effectuer une sauvegarde (Nandroid Backup) -- si besoin

    Dans TWRP, allez dans Backup.
    Sélectionnez Boot, System, et Data.
    Sauvegardez sur la mémoire interne ou une carte SD (important en cas de problème).

4. Wipe complet

    Now tap Wipe.
Now tap Format Data and continue with the formatting process. This will remove encryption and delete all files stored in the internal storage.
Return to the previous menu and tap Advanced Wipe, then select the Cache and System partitions and then Swipe to Wipe.
    
5. Installer la ROM et les GApps

    Retournez au menu principal de TWRP.
    Sélectionnez Install.
    Choisissez la ROM que vous avez copiée et confirmez l’installation.
    Répétez pour les GApps après avoir installé la ROM.

6. Redémarrer dans le système

    Une fois l’installation terminée, allez dans Reboot > System.
    Soyez patient : le premier démarrage peut prendre plusieurs minutes.
