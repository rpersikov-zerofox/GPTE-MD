#!/usr/bin/env python3
"""
Fix all broken links in GPTE documentation markdown files.

This script fixes:
1. Asset paths: ../assets/ -> /assets/
2. Absolute paths: /docs/assets/ -> /assets/
3. Windows backslashes: \ -> /
4. Internal markdown links to use proper relative paths from docs root
"""

import os
import re
from pathlib import Path

# Statistics counters
stats = {
    'files_processed': 0,
    'files_modified': 0,
    'relative_assets_fixed': 0,
    'absolute_assets_fixed': 0,
    'backslashes_fixed': 0,
    'internal_links_checked': 0,
}

def fix_asset_links(content):
    """Fix asset link paths to be relative to docs root."""
    modified = False

    # Fix relative asset paths (../assets/ or ../../assets/ etc) -> /assets/
    pattern1 = r'(\!\[.*?\]\()(?:\.\.\/)+assets\/'
    if re.search(pattern1, content):
        content = re.sub(pattern1, r'\1/assets/', content)
        stats['relative_assets_fixed'] += len(re.findall(pattern1, content))
        modified = True

    # Fix absolute paths /docs/assets/ -> /assets/
    pattern2 = r'(\!\[.*?\]\()\/docs\/assets\/'
    if re.search(pattern2, content):
        count = len(re.findall(pattern2, content))
        content = re.sub(pattern2, r'\1/assets/', content)
        stats['absolute_assets_fixed'] += count
        modified = True

    return content, modified

def fix_backslashes(content):
    """Fix Windows backslashes in links."""
    modified = False

    # Find markdown links with backslashes
    pattern = r'(\[.*?\]\([^)]*)(\\)([^)]*\))'
    matches = list(re.finditer(pattern, content))

    if matches:
        # Replace all backslashes with forward slashes in links
        for match in reversed(matches):  # Reverse to maintain positions
            original = match.group(0)
            fixed = original.replace('\\', '/')
            content = content[:match.start()] + fixed + content[match.end():]
            stats['backslashes_fixed'] += original.count('\\')
            modified = True

    return content, modified

def normalize_internal_links(content, current_file_path, docs_root):
    """
    Normalize internal markdown links to be relative to docs root.
    MkDocs prefers links relative to the docs folder.
    """
    modified = False

    # Pattern to find markdown links (not images)
    pattern = r'\[([^\]]+)\]\(([^)]+\.md[^)]*)\)'

    def replace_link(match):
        nonlocal modified
        link_text = match.group(1)
        link_path = match.group(2)

        stats['internal_links_checked'] += 1

        # Skip absolute URLs
        if link_path.startswith('http://') or link_path.startswith('https://'):
            return match.group(0)

        # Skip anchor-only links
        if link_path.startswith('#'):
            return match.group(0)

        # If link already starts with /, it's relative to docs root - keep it
        if link_path.startswith('/'):
            return match.group(0)

        # Convert backslashes to forward slashes
        link_path = link_path.replace('\\', '/')

        # Resolve the link relative to current file
        current_dir = current_file_path.parent

        try:
            # Resolve the target file
            target_path = (current_dir / link_path).resolve()

            # Make it relative to docs root
            rel_path = target_path.relative_to(docs_root)

            # Convert to forward slashes and prepend /
            new_link = '/' + str(rel_path).replace('\\', '/')

            if new_link != '/' + link_path:
                modified = True
                return f'[{link_text}]({new_link})'

        except (ValueError, FileNotFoundError):
            # If we can't resolve, keep original
            pass

        return match.group(0)

    content = re.sub(pattern, replace_link, content)

    return content, modified

def process_file(file_path, docs_root):
    """Process a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        file_modified = False

        # Fix asset links
        content, mod1 = fix_asset_links(content)
        file_modified = file_modified or mod1

        # Fix backslashes
        content, mod2 = fix_backslashes(content)
        file_modified = file_modified or mod2

        # Normalize internal links
        content, mod3 = normalize_internal_links(content, file_path, docs_root)
        file_modified = file_modified or mod3

        # Write back if modified
        if file_modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            stats['files_modified'] += 1
            return True

        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to process all markdown files."""
    script_dir = Path(__file__).parent
    docs_root = script_dir / 'docs'

    if not docs_root.exists():
        print(f"Error: docs directory not found at {docs_root}")
        return

    print("=" * 60)
    print("GPTE Documentation Link Fixer")
    print("=" * 60)
    print(f"Docs root: {docs_root}")
    print()

    # Find all markdown files
    md_files = list(docs_root.rglob('*.md'))
    total_files = len(md_files)

    print(f"Found {total_files} markdown files")
    print()
    print("Processing files...")
    print("-" * 60)

    # Process each file
    for i, md_file in enumerate(md_files, 1):
        stats['files_processed'] += 1

        # Show progress
        if i % 50 == 0 or i == total_files:
            print(f"Progress: {i}/{total_files} files processed...")

        process_file(md_file, docs_root)

    # Print results
    print()
    print("=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Files processed:           {stats['files_processed']}")
    print(f"Files modified:            {stats['files_modified']}")
    print()
    print("Fixes applied:")
    print(f"  Relative asset paths:    {stats['relative_assets_fixed']}")
    print(f"  Absolute asset paths:    {stats['absolute_assets_fixed']}")
    print(f"  Backslashes in links:    {stats['backslashes_fixed']}")
    print(f"  Internal links checked:  {stats['internal_links_checked']}")
    print()

    total_fixes = (stats['relative_assets_fixed'] +
                   stats['absolute_assets_fixed'] +
                   stats['backslashes_fixed'])

    print(f"Total link fixes: {total_fixes}")
    print("=" * 60)

    if total_fixes > 0:
        print()
        print("✓ Links have been fixed!")
        print("  Next steps:")
        print("  1. Run: mkdocs build")
        print("  2. Run: mkdocs serve")
        print("  3. Check http://127.0.0.1:8000")
    else:
        print()
        print("✓ No issues found - all links are already correct!")

if __name__ == '__main__':
    main()