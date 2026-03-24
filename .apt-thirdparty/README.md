# apt-thirdparty whitelist

Source de la whitelist signée utilisée par `apt-thirdparty-handler`.

## Structure

- `apps.d/*.conf` : définition d'une app installable via `apt-thirdparty://<app-id>`
- `../apt-thirdparty/apps.tar` : archive publiée
- `../apt-thirdparty/apps.tar.asc` : signature détachée de l'archive
- `../apt-thirdparty/whitelist-signing.pub` : clé publique à distribuer aux clients

## Workflow

1. Modifier/ajouter des fichiers `.conf` dans `apps.d/`
2. Lancer la tâche VS Code: `🔐 Signer la whitelist apt-thirdparty`
   (utilise `tools/build-whitelist-bundle.sh`)
3. (si besoin) exporter la clé publique:
  `gpg --armor --export "<votre clé>" > apt-thirdparty/whitelist-signing.pub`
4. Commit/push du repo

## Recommandations clé GPG

- Type: `ECC (sign only)`
- Courbe: `Curve 25519` (défaut)
- Expiration: `1y` (renouvelable)
- Passphrase: fortement recommandée (longue, unique, stockée dans un gestionnaire)

## Export / import / backup des clés (changement de machine)

> Objectif : pouvoir continuer à signer `apt-thirdparty/apps.tar.asc` après migration, panne ou réinstallation.

### 1) Sauvegarde (machine source)

Remplacez `<KEY_ID>` par l'empreinte (`fingerprint`) ou l'identifiant de votre clé :

```bash
# Créer un dossier de backup local
mkdir -p ~/.gnupg-backup
chmod 700 ~/.gnupg-backup

# Export clé privée (indispensable pour signer)
gpg --armor --export-secret-keys <KEY_ID> > ~/.gnupg-backup/whitelist-signing.private.asc

# Export clé publique (distribution / vérification)
gpg --armor --export <KEY_ID> > ~/.gnupg-backup/whitelist-signing.pub.asc

# Export confiance locale (ownertrust)
gpg --export-ownertrust > ~/.gnupg-backup/ownertrust.txt

# (Recommandé) certificat de révocation
gpg --output ~/.gnupg-backup/whitelist-signing.revocation.asc --gen-revoke <KEY_ID>
```

### 2) Vérifier la sauvegarde

```bash
ls -lh ~/.gnupg-backup
gpg --list-packets ~/.gnupg-backup/whitelist-signing.private.asc >/dev/null
```

Stockez ces fichiers dans un emplacement chiffré et hors machine (gestionnaire de secrets, coffre chiffré, support externe chiffré).

### 3) Restauration / import (machine cible)

```bash
# Import des clés
gpg --import ~/.gnupg-backup/whitelist-signing.private.asc
gpg --import ~/.gnupg-backup/whitelist-signing.pub.asc

# Import de la confiance
gpg --import-ownertrust ~/.gnupg-backup/ownertrust.txt

# Vérifier la présence de la clé secrète
gpg --list-secret-keys --keyid-format LONG
```

### 4) Test de signature

Dans le repo :

```bash
./tools/build-whitelist-bundle.sh
gpg --verify apt-thirdparty/apps.tar.asc apt-thirdparty/apps.tar
```

Si la vérification passe, la migration de la clé est opérationnelle.

