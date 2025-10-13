#!/usr/bin/env python3
"""
Generate mkdocs.yml configuration file with full navigation structure.
"""

import os
from pathlib import Path
import yaml

def create_nav_structure(docs_root):
    """Create navigation structure by scanning docs directory."""

    # Manual main navigation structure based on README.md
    nav = [
        {'Home': 'README.md'},
    ]

    # Add main sections
    if (docs_root / 'overview' / 'overview.md').exists():
        nav.append({'Overview': 'overview/overview.md'})

    if (docs_root / 'faq' / 'faq.md').exists():
        nav.append({'FAQ': 'faq/faq.md'})

    # User Manual - Tour Operator & Director (largest section)
    user_manual_dir = docs_root / 'user-manual-tour-operator-director'
    if user_manual_dir.exists():
        user_manual_nav = build_directory_nav(user_manual_dir, docs_root)
        if user_manual_nav:
            nav.append({'User Manual - Tour Operator & Director': user_manual_nav})

    # CMS User Guide
    cms_dir = docs_root / 'user-guide-cms'
    if cms_dir.exists():
        cms_nav = build_directory_nav(cms_dir, docs_root)
        if cms_nav:
            nav.append({'User Guide - CMS': cms_nav})

    # Support Tickets
    if (docs_root / 'support-tickets-instructions' / 'support-tickets-instructions.md').exists():
        nav.append({'Support Tickets Instructions': 'support-tickets-instructions/support-tickets-instructions.md'})

    return nav

def build_directory_nav(directory, docs_root):
    """Recursively build navigation for a directory."""
    items = []

    # Get all items in directory
    try:
        dir_items = sorted(directory.iterdir(), key=lambda x: (not x.is_file(), x.name))
    except Exception as e:
        print(f"Error reading {directory}: {e}")
        return items

    for item in dir_items:
        if item.is_file() and item.suffix == '.md':
            # Add markdown file
            rel_path = item.relative_to(docs_root).as_posix()
            # Use file name (without extension) as title
            title = item.stem.replace('-', ' ').replace('_', ' ').title()
            items.append({title: rel_path})

        elif item.is_dir() and not item.name.startswith('.') and not item.name.startswith('_'):
            # Recursively process subdirectory
            sub_nav = build_directory_nav(item, docs_root)
            if sub_nav:
                # Use directory name as title
                title = item.name.replace('-', ' ').replace('_', ' ').title()
                items.append({title: sub_nav})

    return items

def generate_mkdocs_yml(docs_root):
    """Generate complete mkdocs.yml configuration."""

    # Build navigation
    nav = create_nav_structure(docs_root)

    # Complete configuration
    config = {
        'site_name': 'GPTE Documentation',
        'site_description': 'GP Travel Enterprise User Documentation',
        'site_author': 'GPTE Team',

        'theme': {
            'name': 'material',
            'palette': [
                {
                    'scheme': 'default',
                    'primary': 'indigo',
                    'accent': 'indigo',
                    'toggle': {
                        'icon': 'material/brightness-7',
                        'name': 'Switch to dark mode'
                    }
                },
                {
                    'scheme': 'slate',
                    'primary': 'indigo',
                    'accent': 'indigo',
                    'toggle': {
                        'icon': 'material/brightness-4',
                        'name': 'Switch to light mode'
                    }
                }
            ],
            'features': [
                'navigation.tabs',
                'navigation.sections',
                'navigation.expand',
                'navigation.top',
                'navigation.tracking',
                'navigation.indexes',
                'search.suggest',
                'search.highlight',
                'search.share',
                'content.code.copy',
                'content.code.annotate',
                'toc.follow',
                'toc.integrate'
            ],
            'font': {
                'text': 'Roboto',
                'code': 'Roboto Mono'
            }
        },

        'plugins': [
            'search'
        ],

        'markdown_extensions': [
            'tables',
            'fenced_code',
            'codehilite',
            'admonition',
            'attr_list',
            'md_in_html',
            'pymdownx.details',
            'pymdownx.superfences',
            'pymdownx.highlight',
            'pymdownx.inlinehilite',
            'pymdownx.snippets',
            'pymdownx.tabbed',
            {
                'toc': {
                    'permalink': True,
                    'toc_depth': 3
                }
            }
        ],

        'extra_css': [
            'assets/custom.css'
        ],

        'nav': nav
    }

    return config

def main():
    """Main function."""
    script_dir = Path(__file__).parent
    docs_root = script_dir / 'docs'
    output_file = script_dir / 'mkdocs.yml'

    if not docs_root.exists():
        print(f"Error: docs directory not found at {docs_root}")
        return

    print("=" * 60)
    print("MkDocs Configuration Generator")
    print("=" * 60)
    print(f"Docs root: {docs_root}")
    print(f"Output file: {output_file}")
    print()

    # Generate configuration
    print("Generating navigation structure...")
    config = generate_mkdocs_yml(docs_root)

    # Count markdown files
    md_files = list(docs_root.rglob('*.md'))
    print(f"Found {len(md_files)} markdown files")
    print()

    # Write YAML file
    print("Writing mkdocs.yml...")
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print()
    print("=" * 60)
    print("SUCCESS!")
    print("=" * 60)
    print(f"Created: {output_file}")
    print()
    print("Next steps:")
    print("  1. Review mkdocs.yml")
    print("  2. Run: mkdocs build")
    print("  3. Run: mkdocs serve")
    print("  4. Open: http://127.0.0.1:8000")
    print("=" * 60)

if __name__ == '__main__':
    main()