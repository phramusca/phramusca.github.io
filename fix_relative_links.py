#!/usr/bin/env python3
"""
Script pour détecter et proposer des corrections pour les liens relatifs incorrects
dans les fichiers markdown du wiki Jekyll.

Les liens relatifs simples comme [Linux](Linux) doivent être écrits avec le chemin relatif
correct : [Linux](../linux) depuis windows.md vers linux.md
"""

import re
from pathlib import Path
from typing import List, Tuple, Optional

BASE_DIR = Path(__file__).parent
WIKI_DIR = BASE_DIR / '_wiki'
MARKDOWN_LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')

# Fichiers à exclure
EXCLUDE_DIRS = {'_site', '.git', 'vendor', 'node_modules', '.jekyll-cache', '.sass-cache'}


def find_markdown_files() -> List[Path]:
    """Trouve tous les fichiers markdown dans _wiki."""
    markdown_files = []
    
    for root, dirs, files in os.walk(WIKI_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                markdown_files.append(file_path)
    
    return markdown_files


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
    # Utiliser Path('') pour représenter le dossier racine
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


def analyze_file(file_path: Path, wiki_files: dict) -> List[Tuple[int, str, str, str]]:
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


def fix_file(file_path: Path, issues: List[Tuple[int, str, str, str]]) -> bool:
    """Corrige les liens dans un fichier."""
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


def main():
    import os
    import argparse
    
    parser = argparse.ArgumentParser(description='Détecte et corrige les liens relatifs incorrects dans le wiki')
    parser.add_argument('--fix', action='store_true', help='Corriger automatiquement les liens')
    args = parser.parse_args()
    
    print("🔍 Recherche des liens relatifs incorrects dans le wiki...\n")
    
    # Récupérer tous les fichiers wiki
    wiki_files = get_all_wiki_files()
    print(f"📚 {len(wiki_files)} fichiers wiki trouvés\n")
    
    # Trouver tous les fichiers markdown
    md_files = find_markdown_files()
    print(f"📄 Analyse de {len(md_files)} fichiers markdown...\n")
    
    all_issues = []
    for md_file in md_files:
        issues = analyze_file(md_file, wiki_files)
        if issues:
            rel_path = md_file.relative_to(BASE_DIR)
            all_issues.append((md_file, rel_path, issues))
    
    # Afficher les résultats
    if not all_issues:
        print("✅ Aucun lien relatif incorrect trouvé !")
        return
    
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
    if args.fix:
        print("\n🔧 Correction automatique en cours...\n")
        fixed_count = 0
        for file_path, rel_path, issues in all_issues:
            if fix_file(file_path, issues):
                fixed_count += len(issues)
                print(f"✅ {rel_path}: {len(issues)} lien(s) corrigé(s)")
        
        print(f"\n✅ {fixed_count} lien(s) corrigé(s) au total !")
    else:
        print("\n💡 Utilisez --fix pour corriger automatiquement tous les liens")


if __name__ == '__main__':
    import os
    main()

