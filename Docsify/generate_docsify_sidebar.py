#!/usr/bin/env python3
"""
Generate a complete Docsify sidebar from all markdown files in the docs directory.
"""

import os
from pathlib import Path

def get_title_from_file(filepath):
    """Extract the first H1 title from a markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# '):
                    return line[2:].strip()
        # If no H1 found, use filename
        return filepath.stem.replace('-', ' ').title()
    except Exception:
        return filepath.stem.replace('-', ' ').title()

def collect_all_files(docs_dir):
    """Collect all markdown files with their relative paths."""
    files = []
    for root, dirs, filenames in os.walk(docs_dir):
        # Skip hidden and special directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and not d.startswith('_')]

        for filename in filenames:
            if filename.endswith('.md') and not filename.startswith('_'):
                filepath = Path(root) / filename
                rel_path = filepath.relative_to(docs_dir)
                files.append((rel_path, filepath))

    return sorted(files, key=lambda x: str(x[0]))

def path_depth(path):
    """Get the depth of a path."""
    return len(path.parts)

def generate_sidebar(files):
    """Generate sidebar markdown from files."""
    lines = ['<!-- Auto-generated sidebar -->', '', '* [Home](/)']

    current_depth = 0
    path_stack = []

    for rel_path, full_path in files:
        parts = rel_path.parts
        depth = len(parts) - 1  # Don't count the file itself

        # Get title from file
        title = get_title_from_file(full_path)

        # Calculate indentation
        indent = '  ' * depth

        # Convert path to forward slashes for Docsify
        link_path = str(rel_path).replace('\\', '/')

        # Add the entry
        lines.append(f"{indent}* [{title}]({link_path})")

    return lines

def main():
    docs_dir = Path('docs')

    if not docs_dir.exists():
        print(f"Error: {docs_dir} directory not found")
        return

    print("Scanning documentation files...")
    files = collect_all_files(docs_dir)
    print(f"Found {len(files)} markdown files")

    print("Generating sidebar...")
    sidebar_lines = generate_sidebar(files)

    # Write to _sidebar.md in docs directory
    output_file = docs_dir / '_sidebar.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sidebar_lines))

    print(f"[OK] Sidebar generated: {output_file}")
    print(f"  Total lines: {len(sidebar_lines)}")
    print(f"  Total entries: {len(files)}")

if __name__ == '__main__':
    main()
