#!/usr/bin/env python3
"""
Génère les configurations des outils de vérification de liens à partir de
la whitelist commune (.vscode/tasks/link_whitelist.txt) :

- .lycheeignore                            (lu automatiquement par lychee)
- .htmlproofer.yml                         (bloc ignore_urls entre marqueurs ; référence,
                                            le CLI htmlproofer ne charge pas de fichier)
- .vscode/tasks/generated/whitelist_cli.sh (variable HTMLPROOFER_IGNORE_URLS,
                                            sourcée par check_links.sh pour --ignore-urls)

Les scripts maison Python lisent link_whitelist.txt directement,
ils n'ont pas besoin de cette génération.

Usage: python3 .vscode/tasks/generate_link_configs.py
"""

import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
WHITELIST_FILE = SCRIPT_DIR / "link_whitelist.txt"
GENERATED_DIR = SCRIPT_DIR / "generated"

BEGIN_MARKER = "# >>> GENERATED FROM .vscode/tasks/link_whitelist.txt - ne pas editer a la main >>>"
END_MARKER = "# <<< END GENERATED <<<"

# Motifs spécifiques à lychee (analyse du site généré _site/)
# /!\ pas de commentaire en fin de ligne dans .lycheeignore : la ligne entière est le regex
LYCHEE_SPECIFIC = [
    ("Assets locaux (existants sur le serveur web, pas forcément dans _site)", r"^/assets/.*"),
    ("Fichier JSON généré", r"^/search\.json.*"),
]

# Motifs spécifiques à htmlproofer (en plus de la whitelist commune)
HTMLPROOFER_SPECIFIC = [
    r"#.*",  # Ignorer toutes les URLs contenant un fragment
]


def load_whitelist() -> tuple[list[str], list[str]]:
    """
    Charge link_whitelist.txt.

    Returns:
        (lignes_brutes, motifs) où lignes_brutes conserve les commentaires
        de section (pour .lycheeignore) et motifs ne contient que les regex.
    """
    raw_lines: list[str] = []
    patterns: list[str] = []

    for line in WHITELIST_FILE.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            raw_lines.append(stripped)
            continue
        re.compile(stripped)  # Valide le regex
        raw_lines.append(stripped)
        patterns.append(stripped)

    return raw_lines, patterns


def generate_lycheeignore(raw_lines: list[str]) -> Path:
    """Réécrit entièrement .lycheeignore (lu automatiquement par lychee)."""
    lines = [
        "# Configuration lychee - URLs à ignorer",
        "# Documentation: https://github.com/lycheeverse/lychee",
        "# Ce fichier est lu automatiquement par lychee",
        "#",
        BEGIN_MARKER,
        "# (regénéré par : python3 .vscode/tasks/generate_link_configs.py)",
        "",
        *raw_lines,
        "",
        END_MARKER,
        "",
        "# Motifs spécifiques à lychee (analyse du site généré _site/)",
    ]
    for comment, pattern in LYCHEE_SPECIFIC:
        lines.append(f"# {comment}")
        lines.append(pattern)

    target = PROJECT_ROOT / ".lycheeignore"
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return target


def generate_htmlproofer_yml(patterns: list[str]) -> Path:
    """Remplace le bloc ignore_urls de .htmlproofer.yml entre les marqueurs."""
    target = PROJECT_ROOT / ".htmlproofer.yml"
    content = target.read_text(encoding="utf-8")

    block = [f"  {BEGIN_MARKER}"]
    block += [f"  - '/{p}/'" for p in patterns]
    block.append(f"  {END_MARKER}")

    new_content, count = re.subn(
        re.escape(BEGIN_MARKER) + r".*?" + re.escape(END_MARKER),
        lambda _: "\n".join(block),
        content,
        flags=re.DOTALL,
    )
    if count != 1:
        print(f"❌ Marqueurs introuvables dans {target}", file=sys.stderr)
        print(f"   Ajoutez '{BEGIN_MARKER}' et '{END_MARKER}' dans la section ignore_urls.", file=sys.stderr)
        sys.exit(1)

    target.write_text(new_content, encoding="utf-8")
    return target


def generate_cli_sh(patterns: list[str]) -> Path:
    """Génère le snippet shell sourcé par check_links.sh pour htmlproofer --ignore-urls.

    htmlproofer attend une liste de regex délimités par '/' et séparés par
    des virgules : --ignore-urls '/regex1/,/regex2/'
    (une alternation unique "(a|b)" passée en string ne matchera rien).
    """
    all_patterns = patterns + HTMLPROOFER_SPECIFIC
    ignore_urls = ",".join(f"/{p}/" for p in all_patterns)
    if "," in "".join(all_patterns):
        # htmlproofer découpe --ignore-urls sur les virgules
        print("❌ La whitelist contient une virgule, incompatible avec --ignore-urls d'htmlproofer", file=sys.stderr)
        sys.exit(1)
    if "'" in ignore_urls:
        print("❌ La whitelist contient un guillemet simple, incompatible avec le snippet shell généré", file=sys.stderr)
        sys.exit(1)

    GENERATED_DIR.mkdir(exist_ok=True)
    target = GENERATED_DIR / "whitelist_cli.sh"
    target.write_text(
        "# Généré par generate_link_configs.py depuis link_whitelist.txt - ne pas éditer à la main\n"
        f"HTMLPROOFER_IGNORE_URLS='{ignore_urls}'\n",
        encoding="utf-8",
    )
    return target


def main():
    if not WHITELIST_FILE.exists():
        print(f"❌ Whitelist commune introuvable: {WHITELIST_FILE}", file=sys.stderr)
        sys.exit(1)

    raw_lines, patterns = load_whitelist()
    print(f"📋 {len(patterns)} motifs chargés depuis {WHITELIST_FILE.relative_to(PROJECT_ROOT)}")

    for generated in (
        generate_lycheeignore(raw_lines),
        generate_htmlproofer_yml(patterns),
        generate_cli_sh(patterns),
    ):
        print(f"✅ {generated.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
