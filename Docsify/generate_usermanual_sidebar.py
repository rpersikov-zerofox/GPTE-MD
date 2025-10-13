#!/usr/bin/env python3
"""
Generate Docsify sidebar from user-manual-files.txt with exact nesting structure.
"""

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

def main():
    # Read the file list
    with open('user-manual-files.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Process each line and convert to relative path from docs/
    files = []
    for line in lines:
        # Extract path after 'docs/'
        if '/docs/' in line:
            rel_path = line.split('/docs/', 1)[1]
            files.append(rel_path)

    # Build sidebar structure
    sidebar_lines = ['<!-- User Manual Sidebar -->', '', '* [Home](/)']

    for filepath in files:
        # Split path into parts
        parts = filepath.split('/')

        # Calculate depth (number of directories before the file)
        depth = len(parts) - 1

        # Get title from actual file
        full_path = Path('docs') / filepath
        title = get_title_from_file(full_path)

        # Create the sidebar entry
        indent = '  ' * depth
        sidebar_lines.append(f"{indent}* [{title}]({filepath})")

    # Write sidebar
    output_file = Path('docs') / '_sidebar.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sidebar_lines))

    print(f"[OK] Sidebar generated: {output_file}")
    print(f"  Total entries: {len(files)}")

if __name__ == '__main__':
    main()
