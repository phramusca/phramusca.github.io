# apt-thirdparty whitelist signée

Source de la whitelist signée utilisée par `apt-thirdparty-handler`.

## Structure

- `apps.d/*.conf` : définition d'une app installable via `apt-thirdparty://<app-id>`
- `../apt-thirdparty/apps.tar` : archive publiée
- `../apt-thirdparty/apps.tar.asc` : signature détachée de l'archive
- `../apt-thirdparty/whitelist-signing.pub` : clé publique à distribuer aux clients

## Workflow

1. Modifier/ajouter des fichiers `.conf` dans `apps.d/`
2. Lancer la tâche VS Code: `🔐 Signer la whitelist apt-thirdparty`
   (utilise `tools/build-whitelist-bundle.sh`, qui vérifie aussi automatiquement la signature)
3. (Optionnel) Vérification manuelle :
   `gpg --verify apt-thirdparty/apps.tar.asc apt-thirdparty/apps.tar`
4. Exporter la clé publique (à faire au premier setup, puis uniquement en cas de rotation/changement de clé) :
  `gpg --armor --export "<votre clé>" > apt-thirdparty/whitelist-signing.pub`
5. Commit/push du repo

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

# (Optionnel mais recommandé) certificat de révocation
# Générer ce fichier NE révoque PAS la clé immédiatement.
# Il sert de "bouton d'urgence" à publier/importer plus tard en cas de compromission.
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
gpg --verify apt-thirdparty/apps.tar.asc apt-thirdparty/apps.tar
```

Si la vérification passe, la migration de la clé est opérationnelle.

### 5) (Optionnel) Révoquer réellement la clé plus tard

Utilisez cette procédure seulement en cas d'incident (clé privée compromise/perdue).

```bash
# 1) Importer le certificat de révocation (cela marque la clé comme révoquée localement)
gpg --import ~/.gnupg-backup/whitelist-signing.revocation.asc

# 2) Vérifier l'état (doit indiquer que la clé est révoquée)
gpg --list-keys --keyid-format LONG <KEY_ID>
```

Ensuite, côté publication :

1. Générer une nouvelle clé de signature.
2. Publier la nouvelle clé publique dans `apt-thirdparty/whitelist-signing.pub`.
3. Resigner `apt-thirdparty/apps.tar` avec la nouvelle clé.
4. Demander aux clients de rafraîchir/réinstaller le keyring de confiance.
