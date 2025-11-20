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
import json
import argparse
import urllib.parse
from pathlib import Path
from typing import List, Tuple, Set, Optional, Dict
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from datetime import datetime, timedelta
import time

# Configuration
BASE_DIR = Path(__file__).parent
CACHE_FILE = BASE_DIR / '.link_check_cache.json'
EXCLUDE_DIRS = {'_site', '.git', 'vendor', 'node_modules', '.jekyll-cache', '.sass-cache'}
EXCLUDE_FILES = {'README.md', 'TODO.md', 'Gemfile', 'Gemfile.lock'}

# Patterns pour extraire les liens markdown
MARKDOWN_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')
HTML_LINK_PATTERN = re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)

# Cache en mémoire pour éviter de vérifier plusieurs fois la même URL externe dans une session
external_url_cache = {}


def is_external_url(url: str) -> bool:
    """Détermine si une URL est externe."""
    parsed = urllib.parse.urlparse(url)
    return bool(parsed.netloc) and not url.startswith('/')


def load_cache() -> Dict:
    """Charge le cache depuis le fichier JSON."""
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def save_cache(cache: Dict):
    """Sauvegarde le cache dans le fichier JSON."""
    try:
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(cache, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"⚠️  Erreur lors de la sauvegarde du cache: {e}")


def is_cache_valid(cache_entry: Dict, cache_days: int) -> bool:
    """Vérifie si une entrée du cache est encore valide."""
    if 'checked_date' not in cache_entry:
        return False
    
    try:
        checked_date = datetime.fromisoformat(cache_entry['checked_date'])
        expiry_date = checked_date + timedelta(days=cache_days)
        return datetime.now() < expiry_date
    except (ValueError, KeyError):
        return False


def get_cache_key(file_path: Path, link_url: str, is_external: bool) -> str:
    """Génère une clé unique pour le cache."""
    rel_path = file_path.relative_to(BASE_DIR)
    return f"{rel_path}:{link_url}:{'ext' if is_external else 'int'}"


def get_cached_result(cache: Dict, cache_key: str, cache_days: int) -> Optional[Tuple[bool, str]]:
    """
    Récupère un résultat depuis le cache s'il est encore valide.
    Retourne (is_valid, error_message) ou None si pas de cache valide.
    """
    if cache_key not in cache:
        return None
    
    entry = cache[cache_key]
    if not is_cache_valid(entry, cache_days):
        return None
    
    # Pour les liens internes, vérifier que le fichier existe toujours
    if not entry.get('is_external', True):
        expected_path = entry.get('expected_path')
        if expected_path and not Path(expected_path).exists():
            # Le fichier n'existe toujours pas, le cache est valide
            return (False, f"Fichier introuvable: {Path(expected_path).relative_to(BASE_DIR)}")
        elif expected_path and Path(expected_path).exists():
            # Le fichier existe maintenant, le cache n'est plus valide
            return None
    
    return (entry.get('is_valid', False), entry.get('error', ''))


def update_cache(cache: Dict, cache_key: str, is_valid: bool, error: str, 
                 is_external: bool, expected_path: Optional[str] = None):
    """Met à jour le cache avec un nouveau résultat."""
    cache[cache_key] = {
        'is_valid': is_valid,
        'error': error,
        'checked_date': datetime.now().isoformat(),
        'is_external': is_external,
        'expected_path': expected_path
    }


def normalize_internal_link(link: str, base_file: Path) -> Path:
    """
    Normalise un lien interne pour trouver le fichier correspondant en tenant compte de Jekyll.
    
    Les liens peuvent être:
    - wiki/docker -> _wiki/docker.md
    - wiki/linux/soft/calibre -> _wiki/linux/soft/calibre.md
    - /wiki/linux -> _wiki/linux.md
    - 2024/12/07/FlashSamsung -> _posts/2024-12-07-FlashSamsung.md
    - Sauvegardes_MySQL (dans _wiki/perso/) -> _wiki/perso/Sauvegardes_MySQL.md
    - ../linux (depuis _wiki/perso/) -> _wiki/linux.md
    """
    original_link = link
    
    # Enlever le slash initial s'il existe
    link = link.lstrip('/')
    
    # Enlever le fragment/ancre (#) - Jekyll les gère nativement
    if '#' in link:
        link = link.split('#')[0]
    
    # Enlever le query string
    if '?' in link:
        link = link.split('?')[0]
    
    # Cas spécial: liens vers la racine
    if link == '' or link == 'index':
        return BASE_DIR / 'index.md'
    
    # Cas des posts: format YYYY/MM/DD/Titre (Jekyll transforme ça en permalink)
    post_pattern = re.compile(r'^(\d{4})/(\d{2})/(\d{2})/(.+)$')
    post_match = post_pattern.match(link)
    if post_match:
        year, month, day, title = post_match.groups()
        # Jekyll transforme les titres avec espaces en tirets
        title_normalized = title.replace(' ', '-').replace('_', '-')
        post_file = BASE_DIR / '_posts' / f"{year}-{month}-{day}-{title_normalized}.md"
        if post_file.exists():
            return post_file
        # Essayer avec le titre original
        post_file = BASE_DIR / '_posts' / f"{year}-{month}-{day}-{title}.md"
        if post_file.exists():
            return post_file
    
    # Cas des pages wiki: wiki/... (Jekyll collection avec permalink /wiki/:path/)
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
        # Essayer avec underscores remplacés
        wiki_file = BASE_DIR / '_wiki' / f"{wiki_path.replace(' ', '_')}.md"
        if wiki_file.exists():
            return wiki_file
        # Retourner le chemin attendu même s'il n'existe pas (pour le message d'erreur)
        return BASE_DIR / '_wiki' / f"{wiki_path}.md"
    
    # Cas des liens relatifs depuis le fichier courant (important pour Jekyll)
    if not link.startswith('http') and not link.startswith('/'):
        # Lien relatif au fichier courant
        relative_file = base_file.parent / link
        if relative_file.exists():
            return relative_file
        # Essayer avec .md
        if not link.endswith(('.md', '.html', '.jpg', '.png', '.gif', '.svg')):
            relative_file = base_file.parent / f"{link}.md"
            if relative_file.exists():
                return relative_file
            # Essayer avec underscores (MediaWiki utilise des underscores)
            relative_file = base_file.parent / f"{link.replace(' ', '_')}.md"
            if relative_file.exists():
                return relative_file
            # Essayer avec tirets
            relative_file = base_file.parent / f"{link.replace(' ', '-')}.md"
            if relative_file.exists():
                return relative_file
        
        # Si le fichier courant est dans _wiki, chercher aussi dans _wiki
        if '_wiki' in str(base_file):
            wiki_file = BASE_DIR / '_wiki' / f"{link}.md"
            if wiki_file.exists():
                return wiki_file
            wiki_file = BASE_DIR / '_wiki' / f"{link.replace(' ', '_')}.md"
            if wiki_file.exists():
                return wiki_file
            # Si le fichier courant est dans un sous-dossier de _wiki, chercher dans ce sous-dossier
            if base_file.parent != BASE_DIR / '_wiki':
                rel_to_wiki = base_file.parent.relative_to(BASE_DIR / '_wiki')
                wiki_sub_file = BASE_DIR / '_wiki' / rel_to_wiki / f"{link}.md"
                if wiki_sub_file.exists():
                    return wiki_sub_file
                wiki_sub_file = BASE_DIR / '_wiki' / rel_to_wiki / f"{link.replace(' ', '_')}.md"
                if wiki_sub_file.exists():
                    return wiki_sub_file
    
    # Cas par défaut: chercher dans _wiki (collection Jekyll)
    wiki_file = BASE_DIR / '_wiki' / f"{link}.md"
    if wiki_file.exists():
        return wiki_file
    
    # Essayer avec underscores (MediaWiki)
    wiki_file = BASE_DIR / '_wiki' / f"{link.replace(' ', '_')}.md"
    if wiki_file.exists():
        return wiki_file
    
    # Essayer comme chemin complet dans _wiki
    wiki_file = BASE_DIR / '_wiki' / link
    if wiki_file.exists():
        return wiki_file
    
    # Si le lien commence par .., gérer les chemins relatifs
    if original_link.startswith('../'):
        parent_path = base_file.parent.parent
        rel_link = original_link[3:]  # Enlever ../
        target = parent_path / rel_link
        if target.exists():
            return target
        if not rel_link.endswith('.md'):
            target = parent_path / f"{rel_link}.md"
            if target.exists():
                return target
    
    return BASE_DIR / link


def check_external_link(url: str, timeout: int = 10, use_session_cache: bool = True) -> Tuple[bool, str]:
    """
    Vérifie si un lien externe est accessible.
    Retourne (is_valid, error_message)
    """
    # Utiliser le cache de session pour éviter les vérifications multiples dans la même exécution
    if use_session_cache and url in external_url_cache:
        return external_url_cache[url]
    
    try:
        # Normaliser l'URL pour le cache
        original_url = url
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        req = Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0 (compatible; LinkChecker/1.0)')
        
        with urlopen(req, timeout=timeout) as response:
            status = response.getcode()
            if 200 <= status < 400:
                result = (True, '')
                if use_session_cache:
                    external_url_cache[original_url] = result
                return result
            else:
                error = f"Status {status}"
                result = (False, error)
                if use_session_cache:
                    external_url_cache[original_url] = result
                return result
    
    except HTTPError as e:
        error = f"HTTP {e.code}: {e.reason}"
        result = (False, error)
        if use_session_cache:
            external_url_cache[original_url] = result
        return result
    
    except URLError as e:
        error = f"URL Error: {str(e.reason)}"
        result = (False, error)
        if use_session_cache:
            external_url_cache[original_url] = result
        return result
    
    except Exception as e:
        error = f"Error: {str(e)}"
        result = (False, error)
        if use_session_cache:
            external_url_cache[original_url] = result
        return result


def extract_links(content: str) -> List[Tuple[str, str, int]]:
    """
    Extrait tous les liens d'un contenu markdown/HTML avec leur numéro de ligne.
    Retourne une liste de tuples (link_text, link_url, line_number)
    """
    links = []
    lines = content.split('\n')
    
    # Extraire les liens markdown [text](url)
    for line_num, line in enumerate(lines, start=1):
        for match in MARKDOWN_LINK_PATTERN.finditer(line):
            text, url = match.groups()
            links.append((text, url, line_num))
    
    # Extraire les liens HTML <a href="url">
    for line_num, line in enumerate(lines, start=1):
        for match in HTML_LINK_PATTERN.finditer(line):
            url = match.group(1)
            links.append(('', url, line_num))
    
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


def make_file_link(file_path: Path, line_num: int) -> str:
    """
    Crée un lien cliquable vers un fichier à une ligne spécifique.
    Format compatible avec VSCode (file:// avec URL encodée).
    """
    abs_path = file_path.resolve()
    # Encoder l'URL pour gérer les espaces et caractères spéciaux
    abs_path_encoded = urllib.parse.quote(str(abs_path), safe='/:')
    # Format file:// avec : au lieu de #L (format qui fonctionne dans VS Code)
    return f"file://{abs_path_encoded}:{line_num}"


def group_by_file(links: List[Tuple]) -> dict:
    """Groupe les liens morts par fichier."""
    grouped = {}
    for item in links:
        file_path = item[0]
        if file_path not in grouped:
            grouped[file_path] = []
        grouped[file_path].append(item[1:])  # Exclure file_path de la liste
    return grouped


def is_captcha_protected(error: str) -> bool:
    """Détermine si une erreur suggère une protection par captcha."""
    error_lower = error.lower()
    captcha_indicators = ['captcha', '403', 'forbidden', 'cloudflare', 'rate limit', '429', 
                          'too many requests', 'blocked', 'challenge']
    return any(indicator in error_lower for indicator in captcha_indicators)


def check_links(check_internal: bool = True, check_external: bool = True, 
                verbose: bool = False, cache_days: int = 7, clear_cache: bool = False,
                interactive: bool = False):
    """Fonction principale pour vérifier les liens."""
    # Charger le cache
    if clear_cache:
        cache = {}
        if CACHE_FILE.exists():
            CACHE_FILE.unlink()
            print("🗑️  Cache effacé\n")
    else:
        cache = load_cache()
        if cache:
            print(f"📦 Cache chargé ({len(cache)} entrées)\n")
    
    print("🔍 Recherche des fichiers markdown...")
    files = find_markdown_files()
    print(f"   Trouvé {len(files)} fichiers\n")
    
    broken_internal = []
    broken_external = []
    interactive_links = []  # Liens à vérifier en mode interactif
    total_internal = 0
    total_external = 0
    cached_count = 0
    checked_count = 0
    
    for file_path in files:
        try:
            content = file_path.read_text(encoding='utf-8')
            links = extract_links(content)
            
            for link_text, link_url, line_num in links:
                # Ignorer les liens spéciaux (mailto:, javascript:, etc.)
                if any(link_url.startswith(prefix) for prefix in ['mailto:', 'javascript:', 'tel:', 'apt://', '#']):
                    continue
                
                # Ignorer les liens Liquid/Jekyll ({{ ... }})
                if '{{' in link_url or '{%' in link_url:
                    continue
                
                if is_external_url(link_url):
                    total_external += 1
                    if check_external:
                        cache_key = get_cache_key(file_path, link_url, True)
                        cached_result = get_cached_result(cache, cache_key, cache_days)
                        
                        if cached_result is not None:
                            # Utiliser le résultat du cache
                            cached_count += 1
                            is_valid, error = cached_result
                            if not is_valid:
                                broken_external.append((file_path, link_text, link_url, error, line_num))
                            if verbose:
                                print(f"   📦 Cache: {link_url} -> {'✅' if is_valid else '❌'}")
                        else:
                            # Vérifier le lien
                            checked_count += 1
                            if verbose:
                                print(f"   🔍 Vérification externe: {link_url}")
                            is_valid, error = check_external_link(link_url)
                            
                            # En mode interactif, si le lien est protégé par captcha, on le met de côté
                            if interactive and not is_valid and is_captcha_protected(error):
                                interactive_links.append((file_path, link_text, link_url, error, line_num))
                                if verbose:
                                    print(f"      ⚠️  Protection détectée (captcha/rate limit), sera vérifié en mode interactif: {error}")
                            else:
                                update_cache(cache, cache_key, is_valid, error, True)
                                if not is_valid:
                                    broken_external.append((file_path, link_text, link_url, error, line_num))
                                    if verbose:
                                        print(f"      ❌ Lien mort: {error}")
                            time.sleep(0.1)  # Éviter de surcharger les serveurs
                
                else:
                    total_internal += 1
                    if check_internal:
                        normalized = normalize_internal_link(link_url, file_path)
                        cache_key = get_cache_key(file_path, link_url, False)
                        cached_result = get_cached_result(cache, cache_key, cache_days)
                        
                        if cached_result is not None:
                            # Utiliser le résultat du cache
                            cached_count += 1
                            is_valid, error = cached_result
                            if not is_valid:
                                broken_internal.append((file_path, link_text, link_url, error, line_num))
                            if verbose:
                                print(f"   📦 Cache: {link_url} -> {'✅' if is_valid else '❌'}")
                        else:
                            # Vérifier le lien
                            checked_count += 1
                            file_exists = normalized.exists()
                            expected_path_str = str(normalized)
                            error_msg = f"Fichier introuvable: {normalized.relative_to(BASE_DIR)}" if not file_exists else ""
                            
                            update_cache(cache, cache_key, file_exists, error_msg, False, expected_path_str)
                            
                            if not file_exists:
                                broken_internal.append((file_path, link_text, link_url, expected_path_str, line_num))
                                if verbose:
                                    print(f"   ❌ Lien interne mort dans {file_path.name}: {link_url} -> {normalized}")
        
        except Exception as e:
            print(f"⚠️  Erreur lors de la lecture de {file_path}: {e}")
    
    # Gérer les liens interactifs (mode captcha)
    if interactive and interactive_links:
        print("\n" + "="*70)
        print("🌐 VÉRIFICATION INTERACTIVE")
        print("="*70)
        print(f"\n⚠️  {len(interactive_links)} lien(s) nécessitent une vérification manuelle")
        print("   (protégés par captcha ou rate limit)\n")
        
        grouped = group_by_file(interactive_links)
        for file_path in sorted(grouped.keys()):
            rel_path = file_path.relative_to(BASE_DIR)
            print(f"   📄 {rel_path}")
            for link_text, link_url, error, line_num in grouped[file_path]:
                file_link = make_file_link(file_path, line_num)
                link_display = f"[{link_text}]({link_url})" if link_text else f"({link_url})"
                print(f"      Ligne {line_num}: {link_display}")
                print(f"         🔗 {file_link}")
                print(f"         Erreur automatique: {error}")
        
        print("\n" + "─"*70)
        response = input("\n💬 Voulez-vous ouvrir ces liens dans votre navigateur pour vérification manuelle? (o/N): ").strip().lower()
        
        if response in ['o', 'oui', 'y', 'yes']:
            import webbrowser
            print("\n🌐 Ouverture des liens...")
            for file_path, link_text, link_url, error, line_num in interactive_links:
                # Normaliser l'URL
                url = link_url
                if not url.startswith(('http://', 'https://')):
                    url = 'https://' + url
                print(f"   🔗 Ouverture: {url}")
                webbrowser.open(url)
                time.sleep(1)  # Petit délai entre chaque ouverture
            
            print("\n" + "─"*70)
            print("\n💬 Pour chaque lien, indiquez s'il est valide (o/N) ou tapez 'q' pour quitter:\n")
            
            for file_path, link_text, link_url, error, line_num in interactive_links:
                url = link_url
                if not url.startswith(('http://', 'https://')):
                    url = 'https://' + url
                
                while True:
                    response = input(f"   ✅ Le lien {url} est-il valide? (o/N/q): ").strip().lower()
                    if response == 'q':
                        print("\n   ⏭️  Arrêt de la vérification interactive")
                        break
                    elif response in ['o', 'oui', 'y', 'yes']:
                        # Lien valide
                        cache_key = get_cache_key(file_path, link_url, True)
                        update_cache(cache, cache_key, True, '', True)
                        break
                    elif response in ['n', 'non', 'no', '']:
                        # Demander la raison
                        reason = input(f"   ❌ Raison (optionnel): ").strip()
                        cache_key = get_cache_key(file_path, link_url, True)
                        error_msg = reason if reason else "Vérifié manuellement: lien mort"
                        update_cache(cache, cache_key, False, error_msg, True)
                        broken_external.append((file_path, link_text, link_url, error_msg, line_num))
                        break
                    else:
                        print("   ⚠️  Réponse invalide. Tapez 'o' pour valide, 'N' pour invalide, ou 'q' pour quitter.")
                
                if response == 'q':
                    break
    
    # Sauvegarder le cache
    save_cache(cache)
    
    # Afficher les statistiques du cache
    if cached_count > 0 or checked_count > 0:
        print(f"\n📊 Statistiques:")
        print(f"   Liens vérifiés: {checked_count}")
        print(f"   Liens depuis le cache: {cached_count}")
        if interactive_links:
            print(f"   Liens en mode interactif: {len(interactive_links)}")
        print()
    
    # Afficher les résultats
    print("\n" + "="*70)
    print("📊 RÉSULTATS")
    print("="*70)
    
    if check_internal:
        print(f"\n🔗 Liens internes:")
        print(f"   Total: {total_internal}")
        print(f"   Morts: {len(broken_internal)}")
        
        if broken_internal:
            print(f"\n   ❌ Liens internes morts (groupés par fichier):\n")
            grouped = group_by_file(broken_internal)
            for file_path in sorted(grouped.keys()):
                rel_path = file_path.relative_to(BASE_DIR)
                print(f"   📄 {rel_path}")
                for link_text, link_url, expected_path, line_num in grouped[file_path]:
                    file_link = make_file_link(file_path, line_num)
                    link_display = f"[{link_text}]({link_url})" if link_text else f"({link_url})"
                    print(f"      Ligne {line_num}: {link_display}")
                    print(f"         🔗 {file_link}")
                    # Afficher le chemin attendu de manière propre
                    if expected_path:
                        if Path(expected_path).is_absolute():
                            expected_display = Path(expected_path).relative_to(BASE_DIR)
                        else:
                            expected_display = expected_path
                        # Enlever le préfixe "Fichier introuvable: " si présent
                        if isinstance(expected_display, str) and expected_display.startswith("Fichier introuvable: "):
                            expected_display = expected_display.replace("Fichier introuvable: ", "")
                        print(f"         Fichier attendu: {expected_display}")
                print()
        else:
            print("   ✅ Aucun lien interne mort trouvé!")
    
    if check_external:
        print(f"\n🌐 Liens externes:")
        print(f"   Total: {total_external}")
        print(f"   Morts: {len(broken_external)}")
        
        if broken_external:
            print(f"\n   ❌ Liens externes morts (groupés par fichier):\n")
            grouped = group_by_file(broken_external)
            for file_path in sorted(grouped.keys()):
                rel_path = file_path.relative_to(BASE_DIR)
                print(f"   📄 {rel_path}")
                for link_text, link_url, error, line_num in grouped[file_path]:
                    file_link = make_file_link(file_path, line_num)
                    link_display = f"[{link_text}]({link_url})" if link_text else f"({link_url})"
                    print(f"      Ligne {line_num}: {link_display}")
                    print(f"         🔗 {file_link}")
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
  python3 check_broken_links.py --cache-days 30  # Cache valide 30 jours
  python3 check_broken_links.py --clear-cache    # Efface le cache
        """
    )
    
    parser.add_argument('--internal', action='store_true',
                       help='Vérifier uniquement les liens internes')
    parser.add_argument('--external', action='store_true',
                       help='Vérifier uniquement les liens externes')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Afficher plus de détails')
    parser.add_argument('--cache-days', type=int, default=7,
                       help='Nombre de jours de validité du cache (défaut: 7)')
    parser.add_argument('--clear-cache', action='store_true',
                       help='Effacer le cache avant de vérifier')
    parser.add_argument('--interactive', action='store_true',
                       help='Mode interactif pour les liens protégés par captcha (ouvre dans le navigateur)')
    
    args = parser.parse_args()
    
    check_internal = not args.external
    check_external = not args.internal
    
    if args.internal and args.external:
        print("❌ Erreur: --internal et --external ne peuvent pas être utilisés ensemble")
        sys.exit(1)
    
    if args.interactive and not check_external:
        print("❌ Erreur: --interactive ne peut être utilisé qu'avec --external")
        sys.exit(1)
    
    sys.exit(check_links(check_internal, check_external, args.verbose, 
                        args.cache_days, args.clear_cache, args.interactive))


if __name__ == '__main__':
    main()

