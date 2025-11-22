#!/bin/bash
# Script pour vérifier les liens avec htmlproofer et lychee
# Usage: ./scripts/check_links.sh [htmlproofer|lychee|both]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SITE_DIR="$PROJECT_DIR/_site"

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔍 Vérification des liens morts${NC}\n"

# Vérifier que le site est construit
if [ ! -d "$SITE_DIR" ]; then
    echo -e "${YELLOW}⚠️  Le dossier _site n'existe pas. Construction du site...${NC}\n"
    cd "$PROJECT_DIR"
    bundle exec jekyll build
fi

TOOL="${1:-both}"

# Fonction pour vérifier avec htmlproofer
check_htmlproofer() {
    echo -e "${GREEN}📋 Vérification avec htmlproofer...${NC}\n"
    cd "$PROJECT_DIR"
    
    if ! command -v bundle &> /dev/null; then
        echo -e "${RED}❌ bundle n'est pas installé${NC}"
        exit 1
    fi
    
    bundle exec htmlproofer "$SITE_DIR" \
        --checks Links,Images,Scripts \
        --no-enforce-https \
        --allow-hash-href \
        --ignore-urls '/#.*/' \
        --ignore-urls 'mailto:.*' \
        --ignore-urls 'tel:.*' \
        --ignore-urls 'apt://.*' \
        --typhoeus '{ "timeout": 10, "connecttimeout": 10 }'
}

# Fonction pour vérifier avec lychee
check_lychee() {
    echo -e "${GREEN}📋 Vérification avec lychee...${NC}\n"
    cd "$PROJECT_DIR"
    
    if ! command -v lychee &> /dev/null; then
        echo -e "${YELLOW}⚠️  lychee n'est pas installé${NC}"
        echo -e "Installation avec: cargo install lychee"
        echo -e "Ou téléchargement depuis: https://github.com/lycheeverse/lychee/releases\n"
        exit 1
    fi
    
    lychee "$SITE_DIR" \
        --verbose \
        --no-progress \
        --exclude-all-private \
        --exclude '^mailto:.*' \
        --exclude '^tel:.*' \
        --exclude '^apt://.*' \
        --exclude '^#.*$' \
        --exclude '^/assets/.*' \
        --exclude '^/search\.json.*' \
        --timeout 10 \
        --max-concurrency 5
}

# Exécuter les vérifications
case "$TOOL" in
    htmlproofer)
        check_htmlproofer
        ;;
    lychee)
        check_lychee
        ;;
    both)
        check_htmlproofer
        echo -e "\n${YELLOW}────────────────────────────────────────${NC}\n"
        check_lychee
        ;;
    *)
        echo -e "${RED}❌ Usage: $0 [htmlproofer|lychee|both]${NC}"
        exit 1
        ;;
esac

echo -e "\n${GREEN}✅ Vérification terminée${NC}"

