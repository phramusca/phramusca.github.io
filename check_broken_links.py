#!/usr/bin/env python3
"""
Script pour vérifier les liens morts (internes et externes) dans un site Jekyll.

Usage:
    python3 check_broken_links.py [--external] [--internal] [--verbose]

Options:
    --external    Vérifier uniquement les liens externes
    --internal    Vérifier uniquement les liens internes
    --verbose     Afficher plus de détails
"""

import os
import re
import sys
import argparse
import urllib.parse
from pathlib import Path
from typing import List, Tuple, Set
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import time

# Configuration
BASE_DIR = Path(__file__).parent
EXCLUDE_DIRS = {'_site', '.git', 'vendor', 'node_modules', '.jekyll-cache', '.sass-cache'}
EXCLUDE_FILES = {'README.md', 'TODO.md', 'Gemfile', 'Gemfile.lock'}

# Patterns pour extraire les liens markdown
MARKDOWN_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')
HTML_LINK_PATTERN = re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)

# Cache pour éviter de vérifier plusieurs fois la même URL externe
external_url_cache = {}


def is_external_url(url: str) -> bool:
    """Détermine si une URL est externe."""
    parsed = urllib.parse.urlparse(url)
    return bool(parsed.netloc) and not url.startswith('/')


def normalize_internal_link(link: str, base_file: Path) -> Path:
    """
    Normalise un lien interne pour trouver le fichier correspondant.
    
    Les liens peuvent être:
    - wiki/docker -> _wiki/docker.md
    - wiki/linux/soft/calibre -> _wiki/linux/soft/calibre.md
    - /wiki/linux -> _wiki/linux.md
    - 2024/12/07/FlashSamsung -> _posts/2024-12-07-FlashSamsung.md
    """
    # Enlever le slash initial s'il existe
    link = link.lstrip('/')
    
    # Enlever le fragment/ancre (#)
    if '#' in link:
        link = link.split('#')[0]
    
    # Enlever le query string
    if '?' in link:
        link = link.split('?')[0]
    
    # Cas spécial: liens vers la racine
    if link == '' or link == 'index':
        return BASE_DIR / 'index.md'
    
    # Cas des posts: format YYYY/MM/DD/Titre
    post_pattern = re.compile(r'^(\d{4})/(\d{2})/(\d{2})/(.+)$')
    post_match = post_pattern.match(link)
    if post_match:
        year, month, day, title = post_match.groups()
        post_file = BASE_DIR / '_posts' / f"{year}-{month}-{day}-{title}.md"
        if post_file.exists():
            return post_file
        # Essayer avec extension .html
        post_file = BASE_DIR / '_posts' / f"{year}-{month}-{day}-{title}.html"
        if post_file.exists():
            return post_file
    
    # Cas des pages wiki: wiki/...
    if link.startswith('wiki/'):
        wiki_path = link[5:]  # Enlever "wiki/"
        # Essayer avec .md
        wiki_file = BASE_DIR / '_wiki' / f"{wiki_path}.md"
        if wiki_file.exists():
            return wiki_file
        # Essayer comme dossier avec index.md
        wiki_file = BASE_DIR / '_wiki' / wiki_path / 'index.md'
        if wiki_file.exists():
            return wiki_file
        # Essayer comme chemin complet
        wiki_file = BASE_DIR / '_wiki' / f"{wiki_path}.md"
        return wiki_file
    
    # Cas des liens relatifs depuis le fichier courant
    if not link.startswith('http') and not link.startswith('/'):
        # Lien relatif au fichier courant
        relative_file = base_file.parent / link
        if relative_file.exists():
            return relative_file
        # Essayer avec .md
        if not link.endswith('.md'):
            relative_file = base_file.parent / f"{link}.md"
            if relative_file.exists():
                return relative_file
    
    # Cas par défaut: chercher dans _wiki
    wiki_file = BASE_DIR / '_wiki' / f"{link}.md"
    if wiki_file.exists():
        return wiki_file
    
    # Essayer comme chemin complet dans _wiki
    wiki_file = BASE_DIR / '_wiki' / link
    if wiki_file.exists():
        return wiki_file
    
    return BASE_DIR / link


def check_external_link(url: str, timeout: int = 10) -> Tuple[bool, str]:
    """
    Vérifie si un lien externe est accessible.
    Retourne (is_valid, error_message)
    """
    # Utiliser le cache
    if url in external_url_cache:
        return external_url_cache[url]
    
    try:
        # Ajouter https:// si pas de schéma
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        req = Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0 (compatible; LinkChecker/1.0)')
        
        with urlopen(req, timeout=timeout) as response:
            status = response.getcode()
            if 200 <= status < 400:
                external_url_cache[url] = (True, '')
                return (True, '')
            else:
                error = f"Status {status}"
                external_url_cache[url] = (False, error)
                return (False, error)
    
    except HTTPError as e:
        error = f"HTTP {e.code}: {e.reason}"
        external_url_cache[url] = (False, error)
        return (False, error)
    
    except URLError as e:
        error = f"URL Error: {str(e.reason)}"
        external_url_cache[url] = (False, error)
        return (False, error)
    
    except Exception as e:
        error = f"Error: {str(e)}"
        external_url_cache[url] = (False, error)
        return (False, error)


def extract_links(content: str) -> List[Tuple[str, str]]:
    """
    Extrait tous les liens d'un contenu markdown/HTML.
    Retourne une liste de tuples (link_text, link_url)
    """
    links = []
    
    # Extraire les liens markdown [text](url)
    for match in MARKDOWN_LINK_PATTERN.finditer(content):
        text, url = match.groups()
        links.append((text, url))
    
    # Extraire les liens HTML <a href="url">
    for match in HTML_LINK_PATTERN.finditer(content):
        url = match.group(1)
        links.append(('', url))
    
    return links


def find_markdown_files() -> List[Path]:
    """Trouve tous les fichiers markdown à analyser."""
    markdown_files = []
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Exclure certains dossiers
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file.endswith(('.md', '.html')) and file not in EXCLUDE_FILES:
                file_path = Path(root) / file
                markdown_files.append(file_path)
    
    return markdown_files


def check_links(check_internal: bool = True, check_external: bool = True, verbose: bool = False):
    """Fonction principale pour vérifier les liens."""
    print("🔍 Recherche des fichiers markdown...")
    files = find_markdown_files()
    print(f"   Trouvé {len(files)} fichiers\n")
    
    broken_internal = []
    broken_external = []
    total_internal = 0
    total_external = 0
    
    for file_path in files:
        try:
            content = file_path.read_text(encoding='utf-8')
            links = extract_links(content)
            
            for link_text, link_url in links:
                # Ignorer les liens spéciaux (mailto:, javascript:, etc.)
                if any(link_url.startswith(prefix) for prefix in ['mailto:', 'javascript:', 'tel:', 'apt://', '#']):
                    continue
                
                # Ignorer les liens Liquid/Jekyll ({{ ... }})
                if '{{' in link_url or '{%' in link_url:
                    continue
                
                if is_external_url(link_url):
                    total_external += 1
                    if check_external:
                        if verbose:
                            print(f"   Vérification externe: {link_url}")
                        is_valid, error = check_external_link(link_url)
                        if not is_valid:
                            broken_external.append((file_path, link_text, link_url, error))
                            if verbose:
                                print(f"      ❌ Lien mort: {error}")
                        time.sleep(0.1)  # Éviter de surcharger les serveurs
                
                else:
                    total_internal += 1
                    if check_internal:
                        normalized = normalize_internal_link(link_url, file_path)
                        if not normalized.exists():
                            broken_internal.append((file_path, link_text, link_url, str(normalized)))
                            if verbose:
                                print(f"   ❌ Lien interne mort dans {file_path.name}: {link_url} -> {normalized}")
        
        except Exception as e:
            print(f"⚠️  Erreur lors de la lecture de {file_path}: {e}")
    
    # Afficher les résultats
    print("\n" + "="*70)
    print("📊 RÉSULTATS")
    print("="*70)
    
    if check_internal:
        print(f"\n🔗 Liens internes:")
        print(f"   Total: {total_internal}")
        print(f"   Morts: {len(broken_internal)}")
        
        if broken_internal:
            print(f"\n   ❌ Liens internes morts:")
            for file_path, link_text, link_url, expected_path in broken_internal:
                print(f"      📄 {file_path.relative_to(BASE_DIR)}")
                print(f"         Lien: [{link_text}]({link_url})")
                print(f"         Fichier attendu: {expected_path}")
                print()
        else:
            print("   ✅ Aucun lien interne mort trouvé!")
    
    if check_external:
        print(f"\n🌐 Liens externes:")
        print(f"   Total: {total_external}")
        print(f"   Morts: {len(broken_external)}")
        
        if broken_external:
            print(f"\n   ❌ Liens externes morts:")
            for file_path, link_text, link_url, error in broken_external:
                print(f"      📄 {file_path.relative_to(BASE_DIR)}")
                print(f"         Lien: [{link_text}]({link_url})")
                print(f"         Erreur: {error}")
                print()
        else:
            print("   ✅ Aucun lien externe mort trouvé!")
    
    print("\n" + "="*70)
    
    # Code de sortie
    if (check_internal and broken_internal) or (check_external and broken_external):
        return 1
    return 0


def main():
    parser = argparse.ArgumentParser(
        description='Vérifie les liens morts dans un site Jekyll',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python3 check_broken_links.py              # Vérifie tous les liens
  python3 check_broken_links.py --internal   # Vérifie uniquement les liens internes
  python3 check_broken_links.py --external   # Vérifie uniquement les liens externes
  python3 check_broken_links.py --verbose    # Mode verbeux
        """
    )
    
    parser.add_argument('--internal', action='store_true',
                       help='Vérifier uniquement les liens internes')
    parser.add_argument('--external', action='store_true',
                       help='Vérifier uniquement les liens externes')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Afficher plus de détails')
    
    args = parser.parse_args()
    
    check_internal = not args.external
    check_external = not args.internal
    
    if args.internal and args.external:
        print("❌ Erreur: --internal et --external ne peuvent pas être utilisés ensemble")
        sys.exit(1)
    
    sys.exit(check_links(check_internal, check_external, args.verbose))


if __name__ == '__main__':
    main()

