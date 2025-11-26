#!/usr/bin/env python3
"""
Script pour vérifier les liens internes dans les fichiers Markdown.
Vérifie que les fichiers/dossiers référencés existent.
"""

import sys
from pathlib import Path

# Ajouter le dossier lib au path
sys.path.insert(0, str(Path(__file__).parent / "lib"))

from check_links_lib import (
    LinkExtractor,
    LinkClassifier,
    InternalLinkResolver,
    find_markdown_files,
    make_file_link
)


def main():
    project_root = Path.cwd()
    resolver = InternalLinkResolver(project_root)
    
    markdown_files = find_markdown_files(project_root)
    
    if not markdown_files:
        print("❌ Aucun fichier Markdown trouvé", file=sys.stderr)
        sys.exit(1)
    
    errors = []
    total_links = 0
    checked_files = 0
    
    print(f"🔍 Vérification des liens internes dans {len(markdown_files)} fichiers...\n")
    
    for file_path in markdown_files:
        links = LinkExtractor.extract_links(file_path)
        
        if not links:
            continue
        
        checked_files += 1
        file_errors = []
        
        for line_num, text, url in links:
            # Ignorer les liens non-internes
            if not LinkClassifier.is_internal(url):
                continue
            
            total_links += 1
            
            # Vérifier le lien
            is_valid, error_msg = resolver.check_internal_link(url, file_path)
            
            if not is_valid:
                file_errors.append((line_num, url, text, error_msg))
        
        if file_errors:
            rel_path = file_path.relative_to(project_root)
            errors.append((rel_path, file_errors))
    
    # Afficher les résultats
    print(f"✅ {checked_files} fichiers analysés, {total_links} liens internes vérifiés\n")
    
    if errors:
        print(f"❌ {len(errors)} fichiers avec des erreurs:\n")
        
        for rel_path, file_errors in errors:
            # Reconstruire le chemin absolu pour make_file_link
            file_path = project_root / rel_path
            print(f"📄 {rel_path}:")
            for line_num, url, text, error_msg in file_errors:
                file_link = make_file_link(file_path, line_num)
                link_display = f"[{text}]({url})" if text else f"({url})"
                print(f"   Ligne {line_num}: {link_display}")
                print(f"      🔗 {file_link}")
                print(f"      → {error_msg}")
            print()
        
        sys.exit(1)
    else:
        print("✅ Tous les liens internes sont valides !")
        sys.exit(0)


if __name__ == "__main__":
    main()

