# Tester le site Jekyll localement

1. **Ouvrir dans VS Code avec Dev Container** :
   - Ouvrez le projet dans VS Code
   - Appuyez sur `F1` ou `Ctrl+Shift+P`
   - Tapez "**Dev Containers: Reopen in Container**"
   - Attendez que le container se construise (première fois : ~2-3 min)

2. **Installer les dépendances** (automatique au premier lancement, sinon) :
   - Appuyez sur `F1` ou `Ctrl+Shift+P`
   - Tapez "**Tasks: Run Task**"
   - Sélectionnez "**Bundle: Install**"
   - OU dans le terminal : `bundle install`

3. **Lancer le serveur de développement** :
   - Appuyez sur `F1` ou `Ctrl+Shift+P`
   - Tapez "**Tasks: Run Task**"
   - Sélectionnez "**Jekyll: Serve (développement)**"
   - OU dans le terminal : `bundle exec jekyll serve --livereload`

4. **Accéder au site** :
   - Le site sera accessible sur `http://localhost:4000`
   - Les modifications sont rechargées automatiquement (livereload)

## Commandes utiles

- **Build le site** : `bundle exec jekyll build`
- **Nettoyer le build** : `bundle exec jekyll clean`
- **Serveur sans livereload** : `bundle exec jekyll serve`

## Tasks VS Code disponibles

- `Jekyll: Serve (développement)` - Lance le serveur avec livereload
- `Jekyll: Build` - Construit le site sans le servir
- `Jekyll: Clean` - Nettoie le dossier `_site/`
- `Bundle: Install` - Installe les dépendances Ruby

## Dépannage

### Erreur "bundle: command not found"
```bash
gem install bundler
```

### Erreur de port déjà utilisé
```bash
# Tuer le processus sur le port 4000
lsof -ti:4000 | xargs kill -9
```

### Rebuild complet
```bash
bundle exec jekyll clean
bundle exec jekyll build
bundle exec jekyll serve
```

