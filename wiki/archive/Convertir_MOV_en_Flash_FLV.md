# Convertir MOV en Flash FLV

Faire une page sur la convertion de vidéos. Ajouter <http://doc.ubuntu-fr.org/winff> WinFF dans la liste des programmes.
Même si celui ci n'est plus développé depuis 2003, il utilise ffmpeg qui lui est mis à jour et les commandes marchent toujours (essais fait le 13/2/2010 d'un fichier MP4 en AV(DivX) et FLV).

## Convertir des videos QuicTime MOV en Flash FLV

- Installer mencoder et ffmpeg depuis le gestionnaire de [paquets](Paquet).
- Transformer le MOV en AVI: mencoder -mc 0 -noskip -oac pcm -ovc lavc
  -ffourcc DX50 -o output.avi input.mov
- Transformer l'AVI en FLV (video Flash): ffmpeg -i input.avi -ab 56 -ar
  44100 -b 512 -r 15 -s 320x240 -f flv output.flv

Avec:

- ab : audio bitrate
- ar : audio frequency
- r : frame rate (Hz)
- b : video bitrate (kbits/s)
- s : size

Source : <http://recitmst.qc.ca/wikinimst/wakka.php?wiki=VideoSousLinux>
