Soundjuicer permet de convertir les CDs en fichiers MP3.

ATTENTION: PB VBR et Durée affichage dans Amarok ! A vérifier !!!

[Plus d'infos sur Ubuntu-fr](http://doc.ubuntu-fr.org/sound_juicer)

### Installation

Installé par défaut dans [Ubuntu](Ubuntu "wikilink"), mais il faut
installer le [paquet](paquet "wikilink")
[gstreamer0.10-plugins-ugly-multiverse](apt://gstreamer0.10-plugins-ugly-multiverse)
pour pouvoir encoder en MP3.

### Configuration

Apparemment, il est possible de créer de nouveaux profils, mais
impossible de les sélectionner dans la liste !? Donc, le mieux est de
modifier un profil existant.

La config par défaut pour les MP3 semble bonne cela dit:

`audio/x-raw-int,rate=44100,channels=2 ! lamemp3enc name=enc target=0 quality=6 ! xingmux ! id3v2mux`

Pour avoir du VBR au bitrate moyen de 192, avec le nouvel algo de lame,
utiliser:

`audio/x-raw-int,rate=44100,channels=2 ! lame name=enc vbr=4 vbr-mean-bitrate=192 ! id3v2mux`

Pour utiliser le preset standard, en VBR:

`audio/x-raw-int,rate=44100,channels=2 ! lame name=enc preset=1001 ! id3v2mux`

(preset=standard : This preset should generally be transparent to most
people on most music and is already quite high in quality. The resulting
bitrate should be in the 170-210kbps range, according to music
complexity.)

Pour les options du plugin lame:

`gst-inspect-0.10 lame`

Pour une description des preset lame:

`lame --preset help`

------------------------------------------------------------------------

Retour à [Programmes](Programmes "wikilink")