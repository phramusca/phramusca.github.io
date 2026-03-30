#!/usr/bin/env bash
# Gère des unités systemd .mount avant docker.service (disques externes, etc.)
# Usage : sudo ./docker-pre-mount-disks.sh [list|add|remove]
# Sans argument : menu interactif.
set -euo pipefail

STATE_FILE="/etc/docker/pre-mount-disks.units"
DOCKER_DROPIN="/etc/systemd/system/docker.service.d/10-docker-pre-mount-disks.conf"
MARKER="docker-pre-mount-disks"

die() { echo "Erreur : $*" >&2; exit 1; }

strip_cr() { printf '%s' "${1//$'\r'/}"; }

read_tty() {
  if [[ -r /dev/tty ]]; then
    read -r -p "$1" "$2" </dev/tty
  else
    read -r -p "$1" "$2"
  fi
}

require_root() {
  [[ "$(id -u)" -eq 0 ]] || die "lancer avec sudo"
}

write_docker_dropin() {
  mkdir -p /etc/systemd/system/docker.service.d
  if [[ ! -f "$STATE_FILE" ]] || [[ ! -s "$STATE_FILE" ]]; then
    rm -f "$DOCKER_DROPIN"
    return
  fi
  mapfile -t units < <(grep -v '^[[:space:]]*#' "$STATE_FILE" | grep -v '^[[:space:]]*$' || true)
  [[ ${#units[@]} -eq 0 ]] && rm -f "$DOCKER_DROPIN" && return
  local line=""
  for u in "${units[@]}"; do
    line+="$u "
  done
  line=${line%% }
  cat > "$DOCKER_DROPIN" <<EOF
# Généré par $MARKER — ne pas éditer à la main
[Unit]
After=$line
Requires=$line
EOF
}

cmd_list() {
  require_root
  if [[ ! -f "$STATE_FILE" ]] || [[ ! -s "$STATE_FILE" ]]; then
    echo "Aucun disque enregistré ($STATE_FILE vide)."
    return
  fi
  echo "Unités enregistrées :"
  while IFS= read -r unit; do
    [[ -z "$unit" ]] && continue
    local f="/etc/systemd/system/$unit"
    local where what
    where=$(grep -E '^Where=' "$f" 2>/dev/null | head -1 | cut -d= -f2- || echo "?")
    what=$(grep -E '^What=' "$f" 2>/dev/null | head -1 | cut -d= -f2- || echo "?")
    local st
    st=$(systemctl is-active "$unit" 2>/dev/null || echo "inconnu")
    echo "  - $unit"
    echo "      Where=$where  What=$what  état=$st"
  done < "$STATE_FILE"
}

summarize_mount_unit() {
  local unit=$1 f w t s
  f="/etc/systemd/system/$unit"
  w=$(grep -E '^Where=' "$f" 2>/dev/null | head -1 | cut -d= -f2- || echo "?")
  t=$(grep -E '^What=' "$f" 2>/dev/null | head -1 | cut -d= -f2- || echo "?")
  s=$(systemctl is-active "$unit" 2>/dev/null || echo "?")
  printf 'Where=%s | What=%s | état=%s' "$w" "$t" "$s"
}

cmd_add() {
  require_root
  local -a vk vu vf vl vm
  vk=(); vu=(); vf=(); vl=(); vm=()
  while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    eval "$line"
    [[ -n "${UUID:-}" ]] || continue
    [[ -n "${FSTYPE:-}" ]] || continue
    [[ "$FSTYPE" == "swap" ]] && continue
    vk+=("$KNAME")
    vu+=("$UUID")
    vf+=("$FSTYPE")
    vl+=("${LABEL:-}")
    vm+=("${MOUNTPOINT:-}")
  done < <(lsblk -n -P -o KNAME,UUID,FSTYPE,LABEL,MOUNTPOINT 2>/dev/null)

  local uuid="" fstype="" suggested_where=""
  if [[ ${#vu[@]} -gt 0 ]]; then
    echo "Volumes détectés — choisissez celui à monter avant Docker :"
    local i=1 j
    for j in "${!vu[@]}"; do
      printf '  %2d) /dev/%-12s  %-8s  %s  label=%s  %s\n' \
        "$i" "${vk[$j]}" "${vf[$j]}" "${vu[$j]}" \
        "${vl[$j]:--}" "${vm[$j]:-(non monté)}"
      ((i++)) || true
    done
    echo "   0) Saisir l’UUID à la main (cas particulier)"
    read_tty "Numéro : " choice
    choice=$(strip_cr "$choice")
    choice=${choice//[[:space:]]/}
    if [[ "$choice" == "0" ]]; then
      read_tty "UUID du volume : " uuid
      uuid=$(strip_cr "$uuid")
      read_tty "Type de système de fichiers [ext4] : " fstype
      fstype=$(strip_cr "${fstype:-}")
      fstype=${fstype:-ext4}
    elif [[ "$choice" =~ ^[0-9]+$ ]] && (( choice >= 1 && choice <= ${#vu[@]} )); then
      local k=$((choice - 1))
      uuid="${vu[$k]}"
      fstype="${vf[$k]}"
      suggested_where="${vm[$k]}"
    else
      die "numéro invalide (0 à ${#vu[@]})"
    fi
  else
    echo "Aucun volume avec UUID détecté — saisie manuelle."
    read_tty "UUID du volume : " uuid
    uuid=$(strip_cr "$uuid")
    read_tty "Type de système de fichiers [ext4] : " fstype
    fstype=$(strip_cr "${fstype:-}")
    fstype=${fstype:-ext4}
  fi

  [[ -n "$uuid" ]] || die "UUID vide"
  [[ "$uuid" =~ ^[0-9a-fA-F-]{10,}$ ]] || die "UUID invalide"
  [[ -e "/dev/disk/by-uuid/$uuid" ]] || die "pas de périphérique /dev/disk/by-uuid/$uuid (branchez le disque ou vérifiez l’UUID)"

  local where="" def=""
  suggested_where=$(strip_cr "${suggested_where:-}")
  if [[ -n "$suggested_where" && "$suggested_where" =~ ^/ ]]; then
    def=$suggested_where
  fi
  if [[ -n "$def" ]]; then
    read_tty "Point de montage absolu [$def] (Entrée = garder) : " where
  else
    read_tty "Point de montage absolu (ex. /media/${SUDO_USER:-user}/Data) : " where
  fi
  where=$(strip_cr "$where")
  [[ -z "$where" && -n "$def" ]] && where=$def
  [[ -n "$where" ]] || die "point de montage vide"
  [[ "$where" =~ ^/ ]] || die "le chemin doit commencer par /"
  if [[ -z "${fstype:-}" ]]; then
    read_tty "Type de système de fichiers [ext4] : " fstype
    fstype=$(strip_cr "${fstype:-}")
    fstype=${fstype:-ext4}
  fi

  local owner_def=""
  if [[ -n "${SUDO_USER:-}" ]]; then
    owner_def="${SUDO_USER}:${SUDO_USER}"
  elif [[ -e "$where" ]]; then
    owner_def=$(stat -c '%U:%G' "$where" 2>/dev/null || true)
  else
    local parent
    parent=$(dirname "$where")
    [[ -e "$parent" ]] && owner_def=$(stat -c '%U:%G' "$parent" 2>/dev/null || true)
  fi
  [[ -z "$owner_def" ]] && owner_def="root:root"

  read_tty "Propriétaire du point de montage (user:group) [$owner_def] (Entrée = garder) : " owner
  owner=$(strip_cr "$owner")
  [[ -z "$owner" ]] && owner=$owner_def

  if ! command -v systemd-escape >/dev/null 2>&1; then
    die "systemd-escape introuvable (paquet systemd)"
  fi
  local unit
  unit=$(systemd-escape -p --suffix=mount "$where")
  local unitfile="/etc/systemd/system/$unit"

  if [[ -e "$unitfile" ]]; then
    grep -q "$MARKER" "$unitfile" 2>/dev/null || \
      die "existe déjà : $unitfile (pas géré par ce script — supprimez-le ou renommez le point de montage)"
  fi

  mkdir -p "$(dirname "$STATE_FILE")"
  touch "$STATE_FILE"

  if grep -qxF "$unit" "$STATE_FILE" 2>/dev/null; then
    die "déjà enregistré : $unit"
  fi

  cat > "$unitfile" <<EOF
# Managed by $MARKER
[Unit]
Description=Mount for Docker data ($where)
Before=docker.service

[Mount]
What=/dev/disk/by-uuid/$uuid
Where=$where
Type=$fstype
Options=defaults

[Install]
WantedBy=multi-user.target
EOF

  mkdir -p "$where"
  chown "$owner" "$where" || die "chown impossible"

  echo "$unit" >> "$STATE_FILE"
  write_docker_dropin

  systemctl daemon-reload
  systemctl enable "$unit"
  systemctl start "$unit"
  systemctl daemon-reload
  systemctl restart docker

  echo "OK : $unit activé, docker redémarré. Vérifiez : systemctl status $unit"
}

cmd_remove() {
  require_root
  if [[ ! -f "$STATE_FILE" ]] || [[ ! -s "$STATE_FILE" ]]; then
    echo "Rien à supprimer."
    return
  fi
  mapfile -t arr < <(grep -v '^[[:space:]]*#' "$STATE_FILE" | grep -v '^[[:space:]]*$')
  [[ ${#arr[@]} -eq 0 ]] && echo "Rien à supprimer." && return

  echo "Unités enregistrées — choisissez celle à retirer :"
  local i=1
  for u in "${arr[@]}"; do
    echo "  $i) $u"
    echo "      $(summarize_mount_unit "$u")"
    ((i++)) || true
  done
  read_tty "Numéro à supprimer (Entrée = annuler) : " n
  n=$(strip_cr "$n")
  n=${n//[[:space:]]/}
  [[ -z "$n" ]] && echo "Annulé." && return
  [[ "$n" =~ ^[0-9]+$ ]] || die "numéro invalide"
  (( n >= 1 && n <= ${#arr[@]} )) || die "hors plage"

  local unit="${arr[$((n-1))]}"
  systemctl disable --now "$unit" 2>/dev/null || true
  rm -f "/etc/systemd/system/$unit"

  local tmp
  tmp=$(mktemp)
  grep -vxF "$unit" "$STATE_FILE" > "$tmp" || true
  mv "$tmp" "$STATE_FILE"

  write_docker_dropin
  systemctl daemon-reload
  systemctl restart docker
  echo "OK : $unit retiré, docker redémarré."
}

interactive() {
  require_root
  while true; do
    echo
    echo "=== Disques avant Docker ($MARKER) ==="
    echo "  1) list   — lister les unités enregistrées"
    echo "  2) add    — ajouter un disque (liste + point de montage)"
    echo "  3) remove — retirer une unité"
    echo "  q) quitter"
    read_tty "> " choice
    choice=$(strip_cr "$choice")
    case "$choice" in
      1) cmd_list ;;
      2) cmd_add ;;
      3) cmd_remove ;;
      q|Q) echo "Au revoir."; exit 0 ;;
      *) echo "Choix invalide." ;;
    esac
  done
}

usage() {
  echo "Usage: sudo $0 [list|add|remove]"
  echo "Sans argument : menu interactif."
  echo "Fichiers : $STATE_FILE, $DOCKER_DROPIN"
}

main() {
  case "${1:-}" in
    list) cmd_list ;;
    add) cmd_add ;;
    remove) cmd_remove ;;
    -h|--help) usage ;;
    "") interactive ;;
    *) usage; exit 1 ;;
  esac
}

main "$@"
