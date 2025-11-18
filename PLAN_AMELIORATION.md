# Plan d'amélioration du projet Jekyll

## 📋 Tâches à faire

### 1. Mettre à jour le README
**Objectif** : Documenter les derniers changements et améliorer la documentation

**À ajouter** :
- Documentation sur les posts (structure, front matter, etc.)
- Explication du système de logiciels (soft_list.yaml, url_internal, snake_case)
- Comment fonctionnent les collections wiki
- Structure des includes et layouts

---

### 2. ✅ Vérifier la structure `assets/` vs `_assets/` - **FAIT**
**Question** : Pourquoi `assets/` et pas `_assets/` ? Est-ce standard Jekyll ?

**Réponse** : 
- `assets/` est **standard Jekyll** pour les fichiers statiques (CSS, JS, images)
- Les dossiers avec `_` (comme `_posts/`, `_layouts/`) sont des dossiers spéciaux Jekyll qui ne sont **pas copiés tels quels** dans `_site/`
- `assets/` est **copié tel quel** dans `_site/`, ce qui est ce qu'on veut pour les fichiers statiques
- **Conclusion** : `assets/` est correct, pas besoin de changer

---

### 3. ✅ Exclure des fichiers du build - **FAIT**
**Problème** : `README.md`, `PLAN_AMELIORATION.md` apparaissaient dans `_site/`

**Solution appliquée** : Ajout de `exclude` dans `_config.yml`

**Fichiers exclus** :
- `README.md`
- `PLAN_AMELIORATION.md`
- `TEST_LOCAL.md`
- `.devcontainer/`
- `.vscode/`
- `.git/`
- `.gitignore`
- `Gemfile`
- `Gemfile.lock`

**Résultat** : Ces fichiers ne sont plus copiés dans `_site/` lors du build

---

## ✅ Tâches complétées

- ✅ Déplacer les fichiers markdown des logiciels hors de `_includes/`
- ✅ Créer un `.gitignore` approprié
- ✅ Nettoyer les dossiers vides/inutilisés
- ✅ Centraliser les images
- ✅ Organiser les layouts
- ✅ Standardiser les noms de fichiers en snake_case
- ✅ Ajouter un README.md
- ✅ Exclure les fichiers de documentation du build

---

## 📝 Notes

- Tester chaque changement localement avant de commit
- Faire des commits atomiques (un changement à la fois)
- Vérifier que le site fonctionne après chaque modification
