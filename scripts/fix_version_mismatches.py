"""Fix metadata version mismatches in knowledge base files.

Many files have version: "1.0.0" in their frontmatter but a changelog entry
for "1.0.1" (from subfolder moves). This script updates the frontmatter
version to match the latest changelog entry.
"""
import os
import re

KB_ROOT = os.path.join(os.path.dirname(__file__), '..', 'knowledge_base', 'English')

fixed = 0
scanned = 0

for dirpath, _, filenames in os.walk(KB_ROOT):
    for fname in filenames:
        if not fname.endswith('.md') or fname == 'README.md':
            continue
        fpath = os.path.join(dirpath, fname)
        scanned += 1
        
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if frontmatter says version: "1.0.0" but changelog has 1.0.1
        if 'version: "1.0.0"' not in content:
            continue
        if 'version: "1.0.1"' not in content:
            continue
        
        # Verify the 1.0.1 is in the changelog section (indented) and 1.0.0 is the frontmatter version
        # Replace only the first occurrence (the frontmatter version field)
        new_content = content.replace('version: "1.0.0"', 'version: "1.0.1"', 1)
        
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed += 1
            rel = os.path.relpath(fpath, KB_ROOT)
            print(f"  Fixed: {rel}")

print(f"\nScanned {scanned} files, fixed {fixed} version mismatches.")
