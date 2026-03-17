#!/bin/bash
# Script d'installation post-création du dev container
# Exécuté automatiquement lors de la création du container

set -euo pipefail

echo "🚀 Configuration du dev container..."
echo ""

# Installation des dépendances Ruby
echo "📦 Installation des dépendances Ruby (bundle install)..."
# NOTE: certains gems natifs (ex: prism) peuvent échouer de façon intermittente
# quand Bundler compile en parallèle dans l'overlay filesystem du devcontainer.
# On force une installation séquentielle et on installe dans le workspace,
# sans dépendre d'un répertoire de config potentiellement non inscriptible.
export BUNDLE_APP_CONFIG="$PWD/.bundle"
export BUNDLE_PATH="$PWD/vendor/bundle"
export BUNDLE_JOBS="1"
bundle install --retry 3
echo "✅ Dépendances Ruby installées"
echo ""

# Vérification des outils installés
echo "🔍 Vérification des outils installés..."
echo ""

if command -v bundle &> /dev/null; then
    echo "✅ bundle: $(bundle --version)"
else
    echo "❌ bundle non trouvé"
fi

if bundle exec jekyll --version &> /dev/null; then
    echo "✅ jekyll: $(bundle exec jekyll --version)"
else
    echo "❌ jekyll non trouvé (essayez: bundle exec jekyll --version)"
fi

if bundle exec htmlproofer --version &> /dev/null; then
    echo "✅ htmlproofer: $(bundle exec htmlproofer --version 2>&1 | head -1)"
else
    echo "❌ htmlproofer non trouvé (essayez: bundle exec htmlproofer --version)"
fi

if command -v lychee &> /dev/null; then
    echo "✅ lychee: $(lychee --version)"
else
    echo "⚠️  lychee non trouvé (devrait être installé dans l'image Docker)"
    echo "   Vous pouvez l'installer manuellement avec: cargo install lychee"
fi

echo ""
echo "🎉 Configuration terminée !"
echo ""
echo "💡 Commandes utiles:"
echo "   - Vérifier les liens: ./scripts/check_links.sh [htmlproofer|lychee|both]"
echo ""

