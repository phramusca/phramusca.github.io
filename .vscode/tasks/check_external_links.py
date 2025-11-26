#!/usr/bin/env python3
"""
Script pour vérifier les liens externes dans les fichiers Markdown.
Vérifie que les URLs HTTP/HTTPS sont accessibles.
Utilise un cache pour éviter de vérifier plusieurs fois les mêmes URLs.
"""

import sys
import json
import time
import hashlib
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple
import urllib.request
import urllib.error
import ssl

# Ajouter le dossier lib au path
sys.path.insert(0, str(Path(__file__).parent / "lib"))

from check_links_lib import (
    LinkExtractor,
    LinkClassifier,
    find_markdown_files,
    make_file_link
)


class LinkCache:
    """Cache pour les résultats de vérification des liens externes."""
    
    def __init__(self, cache_file: Path, cache_duration_days: int = 7):
        self.cache_file = cache_file
        self.cache_duration = timedelta(days=cache_duration_days)
        self.cache: Dict[str, Dict] = self._load_cache()
    
    def _load_cache(self) -> Dict[str, Dict]:
        """Charge le cache depuis le fichier."""
        if not self.cache_file.exists():
            return {}
        
        try:
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    
    def _save_cache(self):
        """Sauvegarde le cache dans le fichier."""
        try:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️  Erreur lors de la sauvegarde du cache: {e}", file=sys.stderr)
    
    def _get_cache_key(self, url: str) -> str:
        """Génère une clé de cache pour une URL."""
        return hashlib.md5(url.encode()).hexdigest()
    
    def get(self, url: str) -> Optional[Dict]:
        """Récupère un résultat depuis le cache."""
        key = self._get_cache_key(url)
        
        if key not in self.cache:
            return None
        
        entry = self.cache[key]
        cached_time = datetime.fromisoformat(entry['timestamp'])
        
        # Vérifier si le cache est encore valide
        if datetime.now() - cached_time > self.cache_duration:
            del self.cache[key]
            return None
        
        return entry
    
    def set(self, url: str, is_valid: bool, status_code: Optional[int] = None, error: Optional[str] = None):
        """Met en cache un résultat."""
        key = self._get_cache_key(url)
        self.cache[key] = {
            'url': url,
            'is_valid': is_valid,
            'status_code': status_code,
            'error': error,
            'timestamp': datetime.now().isoformat()
        }
    
    def save(self):
        """Sauvegarde le cache."""
        self._save_cache()


class ExternalLinkChecker:
    """Vérifie les liens externes."""
    
    def __init__(self, cache: LinkCache, timeout: int = 10):
        self.cache = cache
        self.timeout = timeout
        # Créer un contexte SSL qui accepte les certificats auto-signés (pour le développement)
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE
    
    def check_url(self, url: str) -> Tuple[bool, Optional[int], Optional[str]]:
        """
        Vérifie une URL.
        
        Returns:
            (is_valid, status_code, error_message)
        """
        # Vérifier le cache
        cached = self.cache.get(url)
        if cached is not None:
            return cached['is_valid'], cached.get('status_code'), cached.get('error')
        
        # Vérifier l'URL
        try:
            req = urllib.request.Request(url, method='HEAD')
            req.add_header('User-Agent', 'Mozilla/5.0 (compatible; LinkChecker/1.0)')
            
            with urllib.request.urlopen(req, timeout=self.timeout, context=self.ssl_context) as response:
                status_code = response.getcode()
                is_valid = 200 <= status_code < 400
                
                # Mettre en cache
                self.cache.set(url, is_valid, status_code)
                
                return is_valid, status_code, None
        
        except urllib.error.HTTPError as e:
            status_code = e.code
            is_valid = False
            error = f"HTTP {status_code}: {e.reason}"
            
            # Mettre en cache même les erreurs
            self.cache.set(url, is_valid, status_code, error)
            
            return is_valid, status_code, error
        
        except urllib.error.URLError as e:
            is_valid = False
            error = f"Erreur réseau: {str(e.reason)}"
            
            # Mettre en cache
            self.cache.set(url, is_valid, None, error)
            
            return is_valid, None, error
        
        except Exception as e:
            is_valid = False
            error = f"Erreur: {str(e)}"
            
            # Mettre en cache
            self.cache.set(url, is_valid, None, error)
            
            return is_valid, None, error


def main():
    project_root = Path.cwd()
    cache_file = project_root / ".cache" / "external_links_cache.json"
    cache_file.parent.mkdir(exist_ok=True)
    
    cache = LinkCache(cache_file, cache_duration_days=7)
    checker = ExternalLinkChecker(cache, timeout=10)
    
    markdown_files = find_markdown_files(project_root)
    
    if not markdown_files:
        print("❌ Aucun fichier Markdown trouvé", file=sys.stderr)
        sys.exit(1)
    
    errors = []
    total_links = 0
    checked_files = 0
    cached_count = 0
    
    print(f"🔍 Vérification des liens externes dans {len(markdown_files)} fichiers...\n")
    
    for file_path in markdown_files:
        links = LinkExtractor.extract_links(file_path)
        
        if not links:
            continue
        
        checked_files += 1
        file_errors = []
        
        for line_num, text, url in links:
            # Ignorer les liens non-externes
            if not LinkClassifier.is_external(url):
                continue
            
            total_links += 1
            
            # Vérifier si c'est dans le cache
            cached = cache.get(url)
            if cached is not None:
                cached_count += 1
            
            # Vérifier le lien
            is_valid, status_code, error_msg = checker.check_url(url)
            
            if not is_valid:
                file_errors.append((line_num, url, text, status_code, error_msg))
        
        if file_errors:
            rel_path = file_path.relative_to(project_root)
            errors.append((rel_path, file_errors))
    
    # Sauvegarder le cache
    cache.save()
    
    # Afficher les résultats
    print(f"✅ {checked_files} fichiers analysés, {total_links} liens externes vérifiés")
    if cached_count > 0:
        print(f"   ({cached_count} résultats depuis le cache)\n")
    else:
        print()
    
    if errors:
        print(f"❌ {len(errors)} fichiers avec des erreurs:\n")
        
        for rel_path, file_errors in errors:
            # Reconstruire le chemin absolu pour make_file_link
            file_path = project_root / rel_path
            print(f"📄 {rel_path}:")
            for line_num, url, text, status_code, error_msg in file_errors:
                file_link = make_file_link(file_path, line_num)
                link_display = f"[{text}]({url})" if text else f"({url})"
                print(f"   Ligne {line_num}: {link_display}")
                print(f"      🔗 {file_link}")
                if status_code:
                    print(f"      → HTTP {status_code}")
                if error_msg:
                    print(f"      → {error_msg}")
            print()
        
        sys.exit(1)
    else:
        print("✅ Tous les liens externes sont valides !")
        sys.exit(0)


if __name__ == "__main__":
    main()

