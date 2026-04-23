---
layout: software
---

# TigerVNC

Je l'utilise en Flatpak avec un lanceur `.desktop` qui ouvre directement un profil `.tigervnc` (créé avec l'application).

## Installation

[Voir l’entrée dans la liste des programmes](../#category-4-internet)

## Lancement avec un fichier `.tigervnc`

Commande utilisée:

```shell
/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=/app/bin/vncviewer org.tigervnc.vncviewer /home/username/.var/app/org.tigervnc.vncviewer/vnc/rpi5.tigervnc
```

## Exemple de fichier `.desktop`

```ini
[Desktop Entry]
Name=VNC Pi5
Exec=/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=/app/bin/vncviewer org.tigervnc.vncviewer /home/username/.var/app/org.tigervnc.vncviewer/vnc/rpi5.tigervnc
Comment=
Terminal=false
PrefersNonDefaultGPU=false
Icon=org.tigervnc.vncviewer
Type=Application
```

Adapter le chemin `/home/username/...` au nom de l'utilisateur.
