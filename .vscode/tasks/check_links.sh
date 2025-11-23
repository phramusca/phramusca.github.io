#!/bin/bash
# Script pour vérifier les liens avec différentes méthodes
# Usage: ./scripts/check_links.sh [internal|external|both|htmlproofer|lychee|all]

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Le script est dans .vscode/tasks/, donc remonter de 2 niveaux pour arriver à la racine du projet
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
SITE_DIR="$PROJECT_DIR/_site"

# Couleurs pour l'affichage
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔍 Vérification des liens morts${NC}\n"

TOOL="${1:-both}"

# Fonction pour vérifier les liens internes (script maison)
check_internal() {
    echo -e "${GREEN}📋 Vérification des liens internes (script maison)...${NC}\n"
    cd "$PROJECT_DIR"
    
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ python3 n'est pas installé${NC}"
        exit 1
    fi
    
    python3 "$PROJECT_DIR/.vscode/tasks/check_internal_links.py"
    return $?
}

# Fonction pour vérifier les liens externes (script maison)
check_external() {
    echo -e "${GREEN}📋 Vérification des liens externes (script maison avec cache)...${NC}\n"
    cd "$PROJECT_DIR"
    
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ python3 n'est pas installé${NC}"
        exit 1
    fi
    
    python3 "$PROJECT_DIR/.vscode/tasks/check_external_links.py"
    return $?
}

# Fonction pour vérifier avec htmlproofer
check_htmlproofer() {
    echo -e "${GREEN}📋 Vérification avec htmlproofer (analyse _site)...${NC}\n"
    echo -e "${YELLOW}ℹ️  Analyse de _site pour avoir les liens résolus par Jekyll${NC}\n"
    cd "$PROJECT_DIR"
    
    if ! command -v bundle &> /dev/null; then
        echo -e "${RED}❌ bundle n'est pas installé${NC}"
        exit 1
    fi
    
    # Vérifier que le site est construit
    if [ ! -d "$SITE_DIR" ]; then
        echo -e "${YELLOW}⚠️  Le dossier _site n'existe pas. Construction du site...${NC}\n"
        bundle exec jekyll build
    fi
    
    bundle exec htmlproofer _site \
        --checks Links,Images,Scripts \
        --no-enforce-https \
        --allow-hash-href \
        --ignore-urls "/#.*/" \
        --ignore-urls "mailto:.*" \
        --ignore-urls "tel:.*" \
        --typhoeus '{ "timeout": 10, "connecttimeout": 10 }'
    
    return $?
}

# Fonction pour vérifier avec lychee
check_lychee() {
    echo -e "${GREEN}📋 Vérification avec lychee (analyse _site)...${NC}\n"
    echo -e "${YELLOW}ℹ️  Analyse de _site pour avoir les liens résolus par Jekyll${NC}\n"
    cd "$PROJECT_DIR"
    
    if ! command -v lychee &> /dev/null; then
        echo -e "${YELLOW}⚠️  lychee n'est pas installé${NC}"
        echo -e "Installation avec: cargo install lychee"
        echo -e "Ou téléchargement depuis: https://github.com/lycheeverse/lychee/releases\n"
        exit 1
    fi
    
    # Vérifier que le site est construit
    if [ ! -d "$SITE_DIR" ]; then
        echo -e "${YELLOW}⚠️  Le dossier _site n'existe pas. Construction du site...${NC}\n"
        bundle exec jekyll build
    fi
    
    lychee _site \
        --format detailed \
        --verbose \
        --exclude-all-private \
        --exclude "^mailto:.*" \
        --exclude "^tel:.*" \
        --exclude "^#.*$" \
        --exclude "^/assets/.*" \
        --exclude "^/search\\.json.*" \
        --exclude "^JaMuz$" \
        --exclude "^http://localhost:8086/.*" \
        --exclude "^https://samfw.com/firmware/SM-P600/XEF" \
        --exclude "^http://www.planete-android.com/.*" \
        --exclude "^http://browse.geekbench.ca/user/xxxxAailes/profile" \
        --exclude "^http://meta.wikimedia.org/wiki/Aide:Contenu" \
        --exclude "^http://www.jkconception.com/dotclear/index.php/2007/07/09/21-les-crons-ou-les-taches-planifiees-sous-linux" \
        --exclude "^http://xxxxxxx.yyyyy.free.fr/" \
        --timeout 10 \
        --max-concurrency 5 \
        --exclude-path ".lycheeignore"
    
    return $?
}

# Exécuter les vérifications
EXIT_CODE=0

case "$TOOL" in
    internal)
        check_internal
        EXIT_CODE=$?
        ;;
    external)
        check_external
        EXIT_CODE=$?
        ;;
    both)
        check_internal
        INTERNAL_EXIT=$?
        echo -e "\n${YELLOW}────────────────────────────────────────${NC}\n"
        check_external
        EXTERNAL_EXIT=$?
        if [ $INTERNAL_EXIT -ne 0 ] || [ $EXTERNAL_EXIT -ne 0 ]; then
            EXIT_CODE=1
        fi
        ;;
    htmlproofer)
        check_htmlproofer
        EXIT_CODE=$?
        ;;
    lychee)
        check_lychee
        EXIT_CODE=$?
        ;;
    all)
        check_internal
        INTERNAL_EXIT=$?
        echo -e "\n${YELLOW}────────────────────────────────────────${NC}\n"
        check_external
        EXTERNAL_EXIT=$?
        echo -e "\n${YELLOW}────────────────────────────────────────${NC}\n"
        check_htmlproofer
        HTMLPROOFER_EXIT=$?
        echo -e "\n${YELLOW}────────────────────────────────────────${NC}\n"
        check_lychee
        LYCHEE_EXIT=$?
        if [ $INTERNAL_EXIT -ne 0 ] || [ $EXTERNAL_EXIT -ne 0 ] || [ $HTMLPROOFER_EXIT -ne 0 ] || [ $LYCHEE_EXIT -ne 0 ]; then
            EXIT_CODE=1
        fi
        ;;
    *)
        echo -e "${RED}❌ Usage: $0 [internal|external|both|htmlproofer|lychee|all]${NC}"
        echo -e "\nOptions:"
        echo -e "  internal    - Vérifie les liens internes (script maison)"
        echo -e "  external    - Vérifie les liens externes (script maison avec cache)"
        echo -e "  both        - Vérifie les liens internes et externes (scripts maison)"
        echo -e "  htmlproofer - Vérifie avec htmlproofer (analyse _site)"
        echo -e "  lychee      - Vérifie avec lychee (analyse _site)"
        echo -e "  all         - Toutes les méthodes"
        exit 1
        ;;
esac

if [ $EXIT_CODE -eq 0 ]; then
    echo -e "\n${GREEN}✅ Vérification terminée${NC}"
else
    echo -e "\n${RED}❌ Vérification terminée avec des erreurs${NC}"
fi

exit $EXIT_CODE
