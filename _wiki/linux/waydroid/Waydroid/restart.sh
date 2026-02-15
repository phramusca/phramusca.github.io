sudo killall waydroid
sudo waydroid container start &
waydroid session start &
sudo umount ~/.local/share/waydroid/data/media/0/Music
sudo mount --bind ~/Musique-BAK/Archive ~/.local/share/waydroid/data/media/0/Music
sh ./start.sh
