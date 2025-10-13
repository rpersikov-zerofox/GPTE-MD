#!/usr/bin/env python3
"""
Fix sidebar structure - put main section files at correct level.
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
        return filepath.stem.replace('-', ' ').title()
    except Exception:
        return filepath.stem.replace('-', ' ').title()

def is_section_file(path):
    """Check if a file is a section header (folder name matches file name)."""
    parts = path.split('/')
    if len(parts) < 2:
        return False

    filename = parts[-1].replace('.md', '')
    folder_name = parts[-2]

    return filename == folder_name

def main():
    # Read the file list
    with open('user-manual-files.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    # Process and sort files
    files_data = []
    for line in lines:
        if '/docs/' in line:
            rel_path = line.split('/docs/', 1)[1]
            full_path = Path('docs') / rel_path
            title = get_title_from_file(full_path)
            is_section = is_section_file(rel_path)
            depth = len(rel_path.split('/')) - 1

            # Adjust depth for section files - they should be at their folder level
            if is_section:
                depth -= 1

            files_data.append((rel_path, title, depth, is_section))

    # Sort files to put section files before their contents
    def sort_key(item):
        path, title, depth, is_section = item
        parts = path.split('/')
        # Create a sort key that puts section files first in their directory
        key = []
        for i, part in enumerate(parts):
            if i == len(parts) - 1 and is_section:
                key.append((i, '0' + part))  # Section file comes first
            else:
                key.append((i, '1' + part))  # Regular files come after
        return key

    files_data.sort(key=sort_key)

    # Build sidebar
    sidebar_lines = ['<!-- User Manual Sidebar -->', '', '* [Home](/)']

    for rel_path, title, depth, is_section in files_data:
        indent = '  ' * depth
        sidebar_lines.append(f"{indent}* [{title}]({rel_path})")

    # Write sidebar
    output_file = Path('docs') / '_sidebar.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sidebar_lines))

    print(f"[OK] Sidebar generated: {output_file}")
    print(f"  Total entries: {len(files_data)}")
    section_count = sum(1 for _, _, _, is_sec in files_data if is_sec)
    print(f"  Section files: {section_count}")

if __name__ == '__main__':
    main()
