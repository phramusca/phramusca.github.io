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
3. (si besoin) exporter la clé publique:
  `gpg --armor --export "<votre clé>" > apt-thirdparty/whitelist-signing.pub`
4. Commit/push du repo

## Recommandations clé GPG

- Type: `ECC (sign only)`
- Courbe: `Curve 25519` (défaut)
- Expiration: `1y` (renouvelable)
- Passphrase: fortement recommandée (longue, unique, stockée dans un gestionnaire)

