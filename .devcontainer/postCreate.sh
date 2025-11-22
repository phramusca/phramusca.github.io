#!/bin/bash
# Script d'installation post-création du dev container
# Exécuté automatiquement lors de la création du container

set -e

echo "🚀 Configuration du dev container..."
echo ""

# Installation des dépendances Ruby
echo "📦 Installation des dépendances Ruby (bundle install)..."
bundle install
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

if command -v jekyll &> /dev/null; then
    echo "✅ jekyll: $(jekyll --version)"
else
    echo "❌ jekyll non trouvé"
fi

if command -v htmlproofer &> /dev/null; then
    echo "✅ htmlproofer: $(htmlproofer --version 2>&1 | head -1)"
else
    echo "❌ htmlproofer non trouvé"
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

