#!/usr/bin/env bash
set -euo pipefail

SOURCE="${HOME}/JaMuz/JaMuz.db"
REMOTE='One Drive raphael_camus_free_fr:'
BACKUP_DIR="${REMOTE}/JaMuz-backup"
LATEST="${BACKUP_DIR}/JaMuz.db"
RETENTION_MONTHS="${1:-1}"

if [[ ! "$RETENTION_MONTHS" =~ ^[0-9]+$ ]]; then
  echo "Usage: $0 [retention_months]" >&2
  exit 2
fi

if [[ ! -f "$SOURCE" ]]; then
  echo "Fichier source introuvable : $SOURCE" >&2
  exit 1
fi

STAMP=$(date +%Y-%m-%d_%H-%M-%S_%N)
BACKUP="${BACKUP_DIR}/JaMuz_${STAMP}.db"

# Créer un snapshot à chaque exécution, tout en conservant la copie courante.
rclone copyto "$SOURCE" "$BACKUP" -P
rclone copyto "$SOURCE" "$LATEST" -P

CUTOFF=$(date -d "$RETENTION_MONTHS months ago" +%s)
REMOTE_FILES=$(rclone lsf --files-only "$BACKUP_DIR")

while IFS= read -r FILE; do
  if [[ "$FILE" =~ ^JaMuz_([0-9]{4}-[0-9]{2}-[0-9]{2})_([0-9]{2})-([0-9]{2})-([0-9]{2})_[0-9]{9}\.db$ ]]; then
    BACKUP_EPOCH=$(date -d "${BASH_REMATCH[1]} ${BASH_REMATCH[2]}:${BASH_REMATCH[3]}:${BASH_REMATCH[4]}" +%s)
    if (( BACKUP_EPOCH < CUTOFF )); then
      rclone deletefile "${BACKUP_DIR}/${FILE}"
      echo "Sauvegarde supprimée (plus de ${RETENTION_MONTHS} mois) : $FILE"
    fi
  fi
done <<< "$REMOTE_FILES"