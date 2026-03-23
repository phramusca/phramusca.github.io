#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

APPS_DIR="${APT_THIRDPARTY_APPS_DIR:-$WORKSPACE_ROOT/.apt-thirdparty/apps.d}"
PUBLIC_DIR="${APT_THIRDPARTY_PUBLIC_DIR:-$WORKSPACE_ROOT/apt-thirdparty}"
ARCHIVE_PATH="$PUBLIC_DIR/apps.tar"
SIG_PATH="$PUBLIC_DIR/apps.tar.asc"
KEY_ID="${APT_THIRDPARTY_SIGNING_KEY:-${1:-}}"

if [[ -z "$KEY_ID" ]]; then
  echo "Usage: $0 <gpg-key-id-or-email>" >&2
  echo "Or define APT_THIRDPARTY_SIGNING_KEY in environment." >&2
  exit 1
fi

if [[ ! -d "$APPS_DIR" ]]; then
  echo "Apps directory not found: $APPS_DIR" >&2
  exit 1
fi

if ! compgen -G "$APPS_DIR/*.conf" >/dev/null; then
  echo "No .conf files found in: $APPS_DIR" >&2
  exit 1
fi

mkdir -p "$PUBLIC_DIR"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

mkdir -p "$TMP_DIR/apps.d"
cp "$APPS_DIR"/*.conf "$TMP_DIR/apps.d"/

tar -cf "$ARCHIVE_PATH" -C "$TMP_DIR" apps.d
gpg --armor --detach-sign --local-user "$KEY_ID" --output "$SIG_PATH" "$ARCHIVE_PATH"

echo "Whitelist signed successfully:"
echo "  $ARCHIVE_PATH"
echo "  $SIG_PATH"
echo
echo "Optional public key export:"
echo "  gpg --armor --export \"$KEY_ID\" > \"$PUBLIC_DIR/whitelist-signing.pub\""
