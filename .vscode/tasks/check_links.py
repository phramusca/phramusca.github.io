#!/usr/bin/env python3
"""
Outil unifié pour vérifier et corriger les liens dans un site Jekyll.

Fonctionnalités:
- Vérification des liens internes et externes (mortes, protégées)
- Détection et correction des liens relatifs incorrects
- Mode interactif pour les liens externes protégés par captcha
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

# Configuration - BASE_DIR doit pointer vers la racine du projet (2 niveaux au-dessus)
SCRIPT_DIR = Path(__file__).parent.resolve()
BASE_DIR = SCRIPT_DIR.parent.parent.resolve()
CACHE_FILE = SCRIPT_DIR / '.link_check_cache.json'  # Cache dans .vscode/tasks/
WIKI_DIR = BASE_DIR / '_wiki'
EXCLUDE_DIRS = {'_site', '.git', 'vendor', 'node_modules', '.jekyll-cache', '.sass-cache', '.vscode'}
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
    try:
        rel_path = file_path.relative_to(BASE_DIR)
    except ValueError:
        rel_path = file_path
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


# ============================================================================
# Fonctions pour la détection et correction des liens relatifs incorrects
# ============================================================================

def is_relative_link(link_url: str) -> bool:
    """Détermine si un lien est relatif simple (sans chemin)."""
    if not link_url:
        return False
    # Ignorer les liens externes, absolus, avec protocole, etc.
    if any(link_url.startswith(prefix) for prefix in 
           ['http://', 'https://', '/', './', '../', 'mailto:', 'javascript:', 'tel:', 'apt://', '#']):
        return False
    # Ignorer les liens Liquid/Jekyll
    if '{{' in link_url or '{%' in link_url:
        return False
    # Lien relatif simple (juste un nom)
    return '/' not in link_url and not link_url.endswith(('.md', '.html', '.jpg', '.png', '.gif'))


def get_all_wiki_files() -> dict:
    """Retourne un dictionnaire de tous les fichiers wiki indexés par leur nom (normalisé)."""
    wiki_files = {}
    
    if not WIKI_DIR.exists():
        return wiki_files
    
    for md_file in WIKI_DIR.rglob('*.md'):
        # Normaliser le nom (enlever extension, convertir en minuscule)
        name_lower = md_file.stem.lower()
        wiki_files[name_lower] = md_file
        # Aussi indexer avec underscores/tirets normalisés
        name_normalized = name_lower.replace(' ', '_').replace('-', '_')
        if name_normalized != name_lower:
            wiki_files[name_normalized] = md_file
    
    return wiki_files


def find_wiki_file_by_name(name: str, wiki_files: dict) -> Optional[Path]:
    """Trouve un fichier wiki par son nom (insensible à la casse)."""
    name_lower = name.lower()
    name_normalized = name_lower.replace(' ', '_').replace('-', '_')
    
    # Chercher exactement
    if name_lower in wiki_files:
        return wiki_files[name_lower]
    if name_normalized in wiki_files:
        return wiki_files[name_normalized]
    
    # Chercher avec variations
    for key, file_path in wiki_files.items():
        if key.lower() == name_lower or key.lower().replace('_', '-') == name_lower:
            return file_path
    
    return None


def calculate_relative_path(from_file: Path, to_file: Path) -> str:
    """
    Calcule le chemin relatif de from_file vers to_file.
    Dans Jekyll, _wiki/windows.md génère /wiki/windows/, donc pour aller vers linux.md
    depuis windows.md, il faut remonter d'un niveau: ../linux
    """
    from_rel = from_file.relative_to(WIKI_DIR)
    to_rel = to_file.relative_to(WIKI_DIR)
    
    # Obtenir les parties du chemin (sans le nom de fichier)
    from_dir_parts = list(from_rel.parent.parts) if from_rel.parent != Path('.') else []
    to_dir_parts = list(to_rel.parent.parts) if to_rel.parent != Path('.') else []
    
    # Trouver le préfixe commun
    common_length = 0
    min_len = min(len(from_dir_parts), len(to_dir_parts))
    for i in range(min_len):
        if from_dir_parts[i] == to_dir_parts[i]:
            common_length += 1
        else:
            break
    
    # Calculer le nombre de niveaux à remonter
    # On doit toujours remonter d'au moins un niveau pour sortir du dossier de la page générée
    up_levels = len(from_dir_parts) - common_length + 1  # +1 pour sortir du dossier de la page
    
    # Construire le chemin relatif
    parts = []
    # Ajouter les .. pour remonter
    parts.extend(['..'] * up_levels)
    
    # Ajouter le chemin vers la destination
    if common_length < len(to_dir_parts):
        parts.extend(to_dir_parts[common_length:])
    
    # Ajouter le nom du fichier (sans extension .md pour Jekyll)
    parts.append(to_rel.stem)
    
    # Construire le chemin final
    rel_path = '/'.join(parts)
    
    return rel_path


def analyze_relative_links(file_path: Path, wiki_files: dict) -> List[Tuple[int, str, str, str]]:
    """
    Analyse un fichier et retourne les liens relatifs incorrects.
    Retourne une liste de tuples (line_num, link_text, current_link, suggested_link)
    """
    issues = []
    
    try:
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, start=1):
            for match in MARKDOWN_LINK_PATTERN.finditer(line):
                link_text, link_url = match.groups()
                
                # Ignorer les liens Liquid/Jekyll
                if '{{' in link_url or '{%' in link_url:
                    continue
                
                # Si c'est un lien relatif simple
                if is_relative_link(link_url):
                    # Chercher le fichier correspondant
                    target_file = find_wiki_file_by_name(link_url, wiki_files)
                    
                    if target_file:
                        # Calculer le chemin relatif correct
                        correct_path = calculate_relative_path(file_path, target_file)
                        
                        # Si le chemin actuel est différent, c'est un problème
                        if link_url != correct_path:
                            issues.append((line_num, link_text, link_url, correct_path))
    
    except Exception as e:
        print(f"⚠️  Erreur lors de l'analyse de {file_path}: {e}")
    
    return issues


def fix_relative_links_in_file(file_path: Path, issues: List[Tuple[int, str, str, str]]) -> bool:
    """Corrige les liens relatifs dans un fichier."""
    try:
        content = file_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        # Trier les issues par numéro de ligne décroissant pour éviter les problèmes d'index
        issues_sorted = sorted(issues, key=lambda x: x[0], reverse=True)
        
        for line_num, link_text, current_link, suggested_link in issues_sorted:
            # Remplacer le lien dans la ligne
            old_pattern = f'[{link_text}]({current_link})'
            new_pattern = f'[{link_text}]({suggested_link})'
            
            if line_num <= len(lines):
                lines[line_num - 1] = lines[line_num - 1].replace(old_pattern, new_pattern)
        
        # Sauvegarder le fichier
        file_path.write_text('\n'.join(lines), encoding='utf-8')
        return True
    except Exception as e:
        print(f"⚠️  Erreur lors de la correction de {file_path}: {e}")
        return False


def check_and_fix_relative_links(fix: bool = False) -> int:
    """Vérifie et corrige les liens relatifs incorrects."""
    print("🔍 Recherche des liens relatifs incorrects dans le wiki...\n")
    
    # Récupérer tous les fichiers wiki
    wiki_files = get_all_wiki_files()
    print(f"📚 {len(wiki_files)} fichiers wiki trouvés\n")
    
    # Trouver tous les fichiers markdown dans _wiki
    md_files = []
    if WIKI_DIR.exists():
        for root, dirs, files in os.walk(WIKI_DIR):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    md_files.append(file_path)
    
    print(f"📄 Analyse de {len(md_files)} fichiers markdown...\n")
    
    all_issues = []
    for md_file in md_files:
        issues = analyze_relative_links(md_file, wiki_files)
        if issues:
            try:
                rel_path = md_file.relative_to(BASE_DIR)
            except ValueError:
                rel_path = md_file
            all_issues.append((md_file, rel_path, issues))
    
    # Afficher les résultats
    if not all_issues:
        print("✅ Aucun lien relatif incorrect trouvé !")
        return 0
    
    print("=" * 70)
    print("⚠️  LIENS RELATIFS INCORRECTS TROUVÉS")
    print("=" * 70)
    print()
    
    total_count = 0
    for file_path, rel_path, issues in all_issues:
        print(f"📄 {rel_path}")
        for line_num, link_text, current_link, suggested_link in issues:
            print(f"   Ligne {line_num}: [{link_text}]({current_link})")
            print(f"      → Devrait être: [{link_text}]({suggested_link})")
        total_count += len(issues)
        print()
    
    print("=" * 70)
    print(f"📊 Total: {total_count} lien(s) à corriger")
    print("=" * 70)
    
    # Corriger automatiquement si demandé
    if fix:
        print("\n🔧 Correction automatique en cours...\n")
        fixed_count = 0
        for file_path, rel_path, issues in all_issues:
            if fix_relative_links_in_file(file_path, issues):
                fixed_count += len(issues)
                print(f"✅ {rel_path}: {len(issues)} lien(s) corrigé(s)")
        
        print(f"\n✅ {fixed_count} lien(s) corrigé(s) au total !")
        
        # Mettre à jour le cache pour les liens relatifs corrigés
        # Charger le cache existant
        cache = load_cache()
        updated_cache = False
        
        for file_path, rel_path, issues in all_issues:
            for line_num, link_text, current_link, suggested_link in issues:
                # Marquer les anciens liens comme valides (ils sont corrigés maintenant)
                cache_key = get_cache_key(file_path, current_link, False)
                update_cache(cache, cache_key, True, '', False)
                updated_cache = True
        
        if updated_cache:
            save_cache(cache)
            print("💾 Cache mis à jour pour les liens relatifs corrigés")
        
        return 0
    else:
        print("\n💡 Utilisez --fix-relative pour corriger automatiquement tous les liens")
        return 1


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
                                # En mode interactif, mettre aussi les liens du cache non valides de côté
                                if interactive:
                                    interactive_links.append((file_path, link_text, link_url, error, line_num))
                                    if verbose:
                                        print(f"   📦 Cache: {link_url} -> ❌ (sera vérifié en mode interactif)")
                                else:
                                    broken_external.append((file_path, link_text, link_url, error, line_num))
                            if verbose and not (interactive and not is_valid):
                                print(f"   📦 Cache: {link_url} -> {'✅' if is_valid else '❌'}")
                        else:
                            # Vérifier le lien
                            checked_count += 1
                            if verbose:
                                print(f"   🔍 Vérification externe: {link_url}")
                            is_valid, error = check_external_link(link_url)
                            
                            # En mode interactif, mettre tous les liens non valides de côté pour vérification manuelle
                            if interactive and not is_valid:
                                interactive_links.append((file_path, link_text, link_url, error, line_num))
                                if verbose:
                                    if is_captcha_protected(error):
                                        print(f"      ⚠️  Protection détectée (captcha/rate limit), sera vérifié en mode interactif: {error}")
                                    else:
                                        print(f"      ⚠️  Lien mort, sera vérifié en mode interactif: {error}")
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
    
    # Gérer les liens interactifs (tous les liens externes non valides)
    if interactive and interactive_links:
        print("\n" + "="*70)
        print("🌐 VÉRIFICATION INTERACTIVE")
        print("="*70)
        print(f"\n⚠️  {len(interactive_links)} lien(s) externe(s) ont échoué lors de la vérification automatique")
        print("   Vous pouvez les vérifier manuellement dans votre navigateur\n")
        
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
        response = input("\n💬 Voulez-vous vérifier ces liens manuellement? (o/N): ").strip().lower()
        
        if response in ['o', 'oui', 'y', 'yes']:
            import webbrowser
            should_exit = False
            
            for i, (file_path, link_text, link_url, error, line_num) in enumerate(interactive_links, 1):
                if should_exit:
                    break
                    
                # Normaliser l'URL
                url = link_url
                if not url.startswith(('http://', 'https://')):
                    url = 'https://' + url
                
                link_display = f"[{link_text}]({link_url})" if link_text else f"({link_url})"
                file_link = make_file_link(file_path, line_num)
                print(f"\n{'─'*70}")
                print(f"Lien {i}/{len(interactive_links)}: {link_display}")
                print(f"   Erreur automatique: {error}")
                print(f"   📄 Fichier source: {file_link}")
                
                # Ouvrir automatiquement le lien
                print(f"   🔗 Ouverture de {url}...")
                webbrowser.open(url)
                time.sleep(0.5)  # Petit délai
                
                # Demander si le lien est valide
                while True:
                    user_response = input(f"   ✅ Ce lien est-il valide? (o/N/i pour ignorer/q pour quitter): ").strip().lower()
                    if user_response == 'q':
                        print("\n   ⏭️  Arrêt de la vérification interactive")
                        should_exit = True
                        break
                    elif user_response in ['o', 'oui', 'y', 'yes']:
                        # Lien valide
                        cache_key = get_cache_key(file_path, link_url, True)
                        update_cache(cache, cache_key, True, '', True)
                        print(f"   ✅ Lien marqué comme valide dans le cache")
                        break
                    elif user_response in ['i', 'ignore', 'ignorer']:
                        # Ignorer le lien (exemples, etc.)
                        cache_key = get_cache_key(file_path, link_url, True)
                        update_cache(cache, cache_key, True, 'Ignoré (lien d\'exemple)', True)
                        print(f"   ⏭️  Lien ignoré (marqué comme valide mais ignoré)")
                        break
                    elif user_response in ['n', 'non', 'no', '']:
                        # Lien invalide
                        cache_key = get_cache_key(file_path, link_url, True)
                        error_msg = "Vérifié manuellement: lien mort"
                        update_cache(cache, cache_key, False, error_msg, True)
                        broken_external.append((file_path, link_text, link_url, error_msg, line_num))
                        print(f"   ❌ Lien marqué comme mort dans le cache")
                        break
                    else:
                        print("   ⚠️  Réponse invalide. Tapez 'o' pour valide, 'N' pour invalide, 'i' pour ignorer, ou 'q' pour quitter.")
            
            # Sauvegarder le cache après la vérification interactive
            save_cache(cache)
            print(f"\n{'─'*70}")
            print("💾 Cache mis à jour avec les résultats de la vérification interactive")
        else:
            # Si l'utilisateur n'a pas voulu vérifier, on les met dans broken_external
            for file_path, link_text, link_url, error, line_num in interactive_links:
                broken_external.append((file_path, link_text, link_url, error, line_num))
    
    # Sauvegarder le cache (sauf si on est en mode interactif et qu'on n'a pas encore fini)
    # Le cache sera sauvegardé après la vérification interactive
    if not (interactive and interactive_links):
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
            # Vérifier s'il y a des liens protégés par captcha
            captcha_links = [link for link in broken_external if is_captcha_protected(link[3])]
            
            print(f"\n   ❌ Liens externes morts (groupés par fichier):\n")
            grouped = group_by_file(broken_external)
            for file_path in sorted(grouped.keys()):
                try:
                    rel_path = file_path.relative_to(BASE_DIR)
                except ValueError:
                    rel_path = file_path
                print(f"   📄 {rel_path}")
                for link_text, link_url, error, line_num in grouped[file_path]:
                    file_link = make_file_link(file_path, line_num)
                    link_display = f"[{link_text}]({link_url})" if link_text else f"({link_url})"
                    print(f"      Ligne {line_num}: {link_display}")
                    print(f"         🔗 {file_link}")
                    print(f"         Erreur: {error}")
                print()
            
            # Proposer le mode interactif si des liens sont protégés ou si des liens ont échoué
            if not interactive and (captcha_links or broken_external):
                print("─" * 70)
                if captcha_links:
                    print(f"💡 {len(captcha_links)} lien(s) semble(nt) protégé(s) par captcha/rate limit")
                else:
                    print(f"💡 {len(broken_external)} lien(s) externe(s) ont échoué")
                print("   Utilisez --interactive pour vérifier ces liens manuellement dans votre navigateur")
                print("─" * 70)
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
        description='Outil unifié pour vérifier et corriger les liens dans un site Jekyll',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  python3 check_links.py                      # Vérifie tous les liens
  python3 check_links.py --internal            # Vérifie uniquement les liens internes
  python3 check_links.py --external            # Vérifie uniquement les liens externes
  python3 check_links.py --verbose             # Mode verbeux
  python3 check_links.py --fix-relative         # Corrige les liens relatifs incorrects
  python3 check_links.py --external --interactive  # Mode interactif pour captcha
  python3 check_links.py --cache-days 30       # Cache valide 30 jours
  python3 check_links.py --clear-cache          # Efface le cache
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
    parser.add_argument('--check-relative', action='store_true',
                       help='Détecte les liens relatifs incorrects dans le wiki (sans corriger)')
    parser.add_argument('--fix-relative', action='store_true',
                       help='Corrige automatiquement les liens relatifs incorrects dans le wiki')
    
    args = parser.parse_args()
    
    # Si --check-relative ou --fix-relative est spécifié, on fait uniquement ça
    if args.check_relative or args.fix_relative:
        return check_and_fix_relative_links(fix=args.fix_relative)
    
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

