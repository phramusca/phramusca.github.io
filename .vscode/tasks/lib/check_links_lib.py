#!/usr/bin/env python3
"""
Bibliothèque commune pour la vérification des liens dans les fichiers Markdown.
Factorise le code commun entre la vérification des liens internes et externes.
"""

import re
import os
import sys
from pathlib import Path
from typing import List, Tuple, Optional
from urllib.parse import urlparse, urljoin, unquote, quote


class LinkExtractor:
    """Extrait les liens des fichiers Markdown et YAML."""
    
    # Début de lien Markdown : [texte](  ([^\]]+ peut contenir des sauts de ligne)
    MARKDOWN_LINK_PATTERN = re.compile(
        r'\[([^\]]+)\]\(',
        re.MULTILINE
    )
    
    # Autoliens : <http://...> ou <https://...>
    AUTOLINK_PATTERN = re.compile(
        r'<(https?://[^>\s]+)>',
        re.MULTILINE
    )
    
    # URLs nues dans les fichiers YAML (ex: url_website: https://...)
    YAML_URL_PATTERN = re.compile(
        r'https?://[^\s\'"<>]+',
        re.MULTILINE
    )
    
    # Pattern pour les liens Liquid (à ignorer)
    LIQUID_PATTERN = re.compile(
        r'\{\{.*?\}\}|\{%.*?%\}',
        re.MULTILINE | re.DOTALL
    )
    
    @staticmethod
    def is_liquid_template(text: str, start_pos: int, end_pos: int) -> bool:
        """Vérifie si un lien est dans un template Liquid."""
        # Vérifier le contexte autour du lien
        context_start = max(0, start_pos - 50)
        context_end = min(len(text), end_pos + 50)
        context = text[context_start:context_end]
        
        # Chercher les balises Liquid
        return bool(LinkExtractor.LIQUID_PATTERN.search(context))
    
    @staticmethod
    def extract_links(file_path: Path) -> List[Tuple[int, str, str]]:
        """
        Extrait tous les liens d'un fichier :
        - Markdown : liens [texte](url) (y compris multi-lignes) et autoliens <http://...>
        - YAML : URLs nues (http://..., https://...)
        
        Returns:
            List de tuples (numéro_ligne, texte_lien, url)
        """
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"⚠️  Erreur lors de la lecture de {file_path}: {e}", file=sys.stderr)
            return []
        
        if file_path.suffix in ('.yml', '.yaml'):
            return LinkExtractor._extract_yaml_links(content)
        
        # Liens trouvés : (position dans le contenu, texte, url)
        found: List[Tuple[int, str, str]] = []
        # Portions du contenu déjà couvertes par un lien Markdown [texte](url)
        markdown_spans: List[Tuple[int, int]] = []

        # Lire les liens jusqu'à leur parenthèse fermante, en respectant les parenthèses de l'URL.
        position = 0
        while True:
            match = LinkExtractor.MARKDOWN_LINK_PATTERN.search(content, position)
            if match is None:
                break

            url_start = match.end()
            depth = 1
            cursor = url_start
            while cursor < len(content) and depth:
                if content[cursor] == '\\':
                    cursor += 2
                    continue
                if content[cursor] == '(':
                    depth += 1
                elif content[cursor] == ')':
                    depth -= 1
                cursor += 1

            if depth:
                position = match.end()
                continue

            markdown_spans.append((match.start(), cursor))

            url = content[url_start:cursor - 1].strip()
            # Texte éventuellement multi-lignes : normaliser pour l'affichage
            text = ' '.join(match.group(1).split())
            
            # Syntaxe [texte](<url>) : retirer les chevrons
            if url.startswith('<') and url.endswith('>'):
                url = url[1:-1].strip()
            
            # Ignorer les liens vides
            if not url:
                position = cursor
                continue
            
            # Ignorer les liens Liquid
            if LinkExtractor.is_liquid_template(content, match.start(), cursor):
                position = cursor
                continue
            
            found.append((match.start(), text, url))
            position = cursor

        # Autoliens <http://...> (hors liens Markdown déjà trouvés)
        for match in LinkExtractor.AUTOLINK_PATTERN.finditer(content):
            if any(start <= match.start() < end for start, end in markdown_spans):
                continue
            
            # Ignorer les liens Liquid
            if LinkExtractor.is_liquid_template(content, match.start(), match.end()):
                continue
            
            found.append((match.start(), "", match.group(1)))

        # Conserver l'ordre d'apparition et calculer les numéros de ligne
        found.sort(key=lambda link: link[0])
        return [
            (content.count('\n', 0, start) + 1, text, url)
            for start, text, url in found
        ]
    
    @staticmethod
    def _extract_yaml_links(content: str) -> List[Tuple[int, str, str]]:
        """Extrait les URLs nues d'un fichier YAML (ex: url_website: https://...)."""
        links = []
        for line_num, line in enumerate(content.split('\n'), start=1):
            for match in LinkExtractor.YAML_URL_PATTERN.finditer(line):
                links.append((line_num, "", match.group(0)))
        return links


# Fichier de whitelist commun à tous les outils (scripts maison, htmlproofer, lychee).
# htmlproofer et lychee sont régénérés depuis ce fichier par generate_link_configs.py.
WHITELIST_FILE = Path(__file__).resolve().parent.parent / "link_whitelist.txt"


def load_whitelist_patterns(whitelist_file: Path = WHITELIST_FILE) -> List[str]:
    """Charge les motifs de la whitelist commune (un regex par ligne, # = commentaire)."""
    patterns = []
    try:
        with open(whitelist_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    re.compile(line)  # Valide le regex
                    patterns.append(line)
    except FileNotFoundError:
        print(f"⚠️  Whitelist commune introuvable: {whitelist_file}", file=sys.stderr)
    return patterns


class LinkClassifier:
    """Classe les liens en internes ou externes."""
    
    # Protocoles à ignorer (ne sont pas vérifiables)
    IGNORED_PROTOCOLS = {'mailto', 'tel', 'apt', 'apt-thirdparty', 'snap', 'flatpak+https', 'file'}
    
    # Liens à ignorer complètement (chargés depuis la whitelist commune link_whitelist.txt)
    IGNORED_PATTERNS = load_whitelist_patterns()
    
    @staticmethod
    def is_ignored(url: str) -> bool:
        """Vérifie si un lien doit être ignoré."""
        # Vérifier les patterns
        for pattern in LinkClassifier.IGNORED_PATTERNS:
            if re.match(pattern, url):
                return True
        
        # Vérifier les protocoles
        parsed = urlparse(url)
        if parsed.scheme in LinkClassifier.IGNORED_PROTOCOLS:
            return True
        
        return False
    
    @staticmethod
    def is_internal(url: str) -> bool:
        """Détermine si un lien est interne."""
        # Liens ignorés ne sont ni internes ni externes
        if LinkClassifier.is_ignored(url):
            return False
        
        # Liens avec protocole HTTP/HTTPS sont externes
        if url.startswith(('http://', 'https://')):
            return False
        
        # Liens relatifs (./, ../, /) sont internes
        if url.startswith(('./', '../', '/')):
            return True
        
        # Liens sans protocole sont internes (ex: wiki/page, page.md)
        if not re.match(r'^[a-zA-Z][a-zA-Z\d+\-.]*:', url):
            return True
        
        return False
    
    @staticmethod
    def is_external(url: str) -> bool:
        """Détermine si un lien est externe."""
        if LinkClassifier.is_ignored(url):
            return False
        
        # Liens HTTP/HTTPS sont externes
        if url.startswith(('http://', 'https://')):
            return True
        
        return False


class InternalLinkResolver:
    """Résout les liens internes vers les fichiers sources."""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.wiki_dir = project_root / "_wiki"
        self.posts_dir = project_root / "_posts"

    def resolve_wiki_url(self, link: str, from_file: Path) -> Optional[Path]:
        """Résout un lien relatif comme le navigateur depuis le permalink Jekyll."""
        if not from_file.is_relative_to(self.wiki_dir):
            return None

        wiki_path = from_file.relative_to(self.wiki_dir).with_suffix('').as_posix()
        source_url = f"/wiki/{wiki_path}/"
        public_path = unquote(urlparse(urljoin(source_url, link)).path)
        if public_path.startswith('/wiki/'):
            target = self.wiki_dir / public_path.removeprefix('/wiki/')
        else:
            target = self.project_root / public_path.lstrip('/')

        if target.is_file():
            return target

        if target.is_dir():
            index_file = target / 'index.md'
            if index_file.is_file():
                return index_file

            sibling_page = target.parent / f"{target.name}.md"
            if sibling_page.is_file():
                return sibling_page

        if not target.suffix:
            markdown_file = target.with_suffix('.md')
            if markdown_file.is_file():
                return markdown_file

        return None
    
    def normalize_internal_link(self, link: str, from_file: Path) -> Optional[Path]:
        """
        Normalise un lien interne vers un chemin de fichier.
        
        Args:
            link: Le lien (ex: "../linux", "wiki/page", "/wiki/page")
            from_file: Le fichier source du lien
        
        Returns:
            Le chemin du fichier cible, ou None si introuvable
        """
        # Enlever les ancres
        link = link.split('#')[0]
        if not link:
            return None
        
        # Dans _wiki/, les liens relatifs sont résolus comme le navigateur :
        # depuis l'URL publiée de la page (permalink /wiki/.../), pas depuis le dossier source
        if not link.startswith('/') and from_file.is_relative_to(self.wiki_dir):
            return self.resolve_wiki_url(link, from_file)
        
        # Liens absolus commençant par /
        if link.startswith('/'):
            # Enlever le / initial
            link = link[1:]
            # Si commence par wiki/, chercher dans _wiki
            if link.startswith('wiki/'):
                link = link[5:]  # Enlever "wiki/"
                target = self.wiki_dir / link
            else:
                # Autre lien absolu
                target = self.project_root / link
        # Liens relatifs
        elif link.startswith('./'):
            link = link[2:]
            target = from_file.parent / link
        elif link.startswith('../'):
            # Compter le nombre de ../
            parts = link.split('/')
            up_levels = 0
            remaining = []
            for part in parts:
                if part == '..':
                    up_levels += 1
                else:
                    remaining.append(part)
            
            # Remonter les niveaux
            target_dir = from_file.parent
            for _ in range(up_levels):
                target_dir = target_dir.parent
            
            if remaining:
                target = target_dir / '/'.join(remaining)
            else:
                target = target_dir

            # Les liens internes peuvent aussi pointer vers des scripts ou
            # d'autres fichiers qui ne sont pas des pages Markdown.
            if target.is_file():
                return target
            
            # Chercher le fichier .md correspondant
            if target.is_file() and target.suffix == '.md':
                return target
            
            # Si c'est un dossier, chercher index.md ou un fichier .md avec le même nom
            if target.is_dir():
                index_file = target / 'index.md'
                if index_file.exists():
                    return index_file
                
                # Chercher un fichier .md avec le nom du dossier
                md_file = target.parent / f"{target.name}.md"
                if md_file.exists():
                    return md_file
            
            # Si c'est un fichier sans extension, essayer .md
            if not target.suffix:
                md_file = target.with_suffix('.md')
                if md_file.exists():
                    return md_file
            
            # Si le target n'existe pas, essayer de trouver un fichier .md proche
            if not target.exists():
                md_file = target.with_suffix('.md')
                if md_file.exists():
                    return md_file
                
                # Si target est un dossier qui n'existe pas, chercher un .md parent
                if target.suffix == '':
                    md_file = target.parent / f"{target.name}.md"
                    if md_file.exists():
                        return md_file
                    
                    # Si on est dans _wiki et qu'on remonte à la racine, chercher aussi dans _wiki
                    # Ex: depuis _wiki/windows.md, ../linux devrait trouver _wiki/linux.md
                    if from_file.is_relative_to(self.wiki_dir) and target_dir == self.project_root and remaining:
                        wiki_target = self.wiki_dir / '/'.join(remaining)
                        wiki_md = wiki_target.with_suffix('.md')
                        if wiki_md.exists():
                            return wiki_md
            
            public_target = self.resolve_wiki_url(link, from_file)
            if public_target:
                return public_target

            return None
        else:
            # Lien relatif simple
            target = from_file.parent / link
        
        # Les liens internes peuvent aussi pointer vers des scripts ou d'autres
        # fichiers qui ne sont pas des pages Markdown.
        if target.is_file():
            return target
        
        # Si c'est un dossier, chercher index.md ou un fichier .md avec le même nom
        if target.is_dir():
            index_file = target / 'index.md'
            if index_file.exists():
                return index_file
            
            # Chercher un fichier .md avec le nom du dossier
            md_file = target.parent / f"{target.name}.md"
            if md_file.exists():
                return md_file
        
        # Si c'est un fichier sans extension, essayer .md
        if not target.suffix:
            md_file = target.with_suffix('.md')
            if md_file.exists():
                return md_file
        
        # Si le target n'existe pas, essayer de trouver un fichier .md proche
        if not target.exists():
            md_file = target.with_suffix('.md')
            if md_file.exists():
                return md_file
            
            # Si target est un dossier qui n'existe pas, chercher un .md parent
            if target.suffix == '':
                md_file = target.parent / f"{target.name}.md"
                if md_file.exists():
                    return md_file

        public_target = self.resolve_wiki_url(link, from_file)
        if public_target:
            return public_target
        
        return None
    
    def check_internal_link(self, link: str, from_file: Path) -> Tuple[bool, Optional[str]]:
        """
        Vérifie si un lien interne est valide.
        
        Returns:
            (is_valid, error_message)
        """
        # Enlever les ancres
        link_clean = link.split('#')[0]
        if not link_clean:
            return True, None  # Lien d'ancre seulement, valide
        
        # Pour les liens absolus vers assets/, vérifier directement le fichier
        if link_clean.startswith('/assets/'):
            asset_path = self.project_root / link_clean[1:]  # Enlever le / initial
            if asset_path.exists():
                return True, None
            else:
                return False, f"Fichier asset introuvable: {link_clean}"
        
        # Pour les autres liens, utiliser normalize_internal_link
        target = self.normalize_internal_link(link, from_file)
        
        if target is None:
            return False, f"Fichier introuvable pour le lien: {link}"
        
        if not target.exists():
            return False, f"Fichier n'existe pas: {target.relative_to(self.project_root)}"
        
        return True, None


def find_source_files(project_root: Path) -> List[Path]:
    """Trouve tous les fichiers sources contenant des liens (Markdown + données YAML)."""
    source_files = []
    
    # Fichiers dans _wiki
    wiki_dir = project_root / "_wiki"
    if wiki_dir.exists():
        source_files.extend(wiki_dir.rglob("*.md"))
    
    # Fichiers dans _posts
    posts_dir = project_root / "_posts"
    if posts_dir.exists():
        source_files.extend(posts_dir.glob("*.md"))
    
    # Données YAML (ex: _data/soft_list.yaml contient url_website, url_repository...)
    data_dir = project_root / "_data"
    if data_dir.exists():
        source_files.extend(data_dir.glob("*.yml"))
        source_files.extend(data_dir.glob("*.yaml"))
    
    return sorted(source_files)


def make_file_link(file_path: Path, line_num: int) -> str:
    """
    Crée un lien cliquable vers un fichier à une ligne spécifique.
    Format compatible avec VSCode (file:// avec URL encodée).
    """
    abs_path = file_path.resolve()
    # Encoder l'URL pour gérer les espaces et caractères spéciaux
    abs_path_encoded = quote(str(abs_path), safe='/:')
    # Format file:// avec : au lieu de #L (format qui fonctionne dans VS Code)
    return f"file://{abs_path_encoded}:{line_num}"
