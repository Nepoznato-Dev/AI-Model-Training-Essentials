"""
Script to:
1. Replace author/contributor names with 'Nepoznato-Dev' in YAML frontmatter
2. Keep the YAML frontmatter block as active (uncommented) frontmatter

Usage:
    python comment_metadata.py           # Process files with active frontmatter
    python comment_metadata.py --migrate # One-time: unwrap HTML-commented frontmatter
"""

import os
import re
import sys

KB_ROOT = os.path.join(os.path.dirname(__file__), "..", "knowledge_base")

def process_file(filepath):
    """Process a single markdown file with active YAML frontmatter."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Only process files that start with ---
    if not content.startswith("---"):
        return False

    # Find the closing --- (second occurrence)
    # Start searching after the first ---
    second_delim = content.find("\n---", 3)
    if second_delim == -1:
        return False

    # Extract frontmatter (including the delimiters)
    frontmatter = content[:second_delim + 5]  # +5 for "\n---"
    rest = content[second_delim + 5:]

    # Replace author names with Nepoznato-Dev
    frontmatter = frontmatter.replace(
        'name: "AI Model Training Team"',
        'name: "Nepoznato-Dev"'
    )
    frontmatter = frontmatter.replace(
        'author: "AI Model Training Team"',
        'author: "Nepoznato-Dev"'
    )

    # Keep frontmatter as active YAML (no HTML-comment wrapping)
    new_frontmatter = frontmatter

    # Ensure there's a newline between the comment close and the rest
    if rest and not rest.startswith("\n"):
        new_frontmatter += "\n"

    new_content = new_frontmatter + rest

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def migrate_file(filepath):
    """Unwrap HTML-commented frontmatter in a single markdown file.

    Converts:
        <!--
        ---
        title: ...
        ---
        -->
    To:
        ---
        title: ...
        ---
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Only process files that start with the HTML comment wrapper
    if not content.startswith("<!--\n---"):
        return False

    # Find the closing -->
    close_idx = content.find("-->")
    if close_idx == -1:
        return False

    # Extract the YAML frontmatter (strip <!--\n prefix and \n--> suffix)
    frontmatter = content[4:close_idx].strip("\n")
    rest = content[close_idx + 3:]

    # Basic YAML validation: must contain at least one key: value pair
    if ":" not in frontmatter:
        return False

    # Ensure clean separation between frontmatter and body
    if rest and not rest.startswith("\n"):
        rest = "\n" + rest

    new_content = frontmatter + rest

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    migrate = "--migrate" in sys.argv

    processed = 0
    skipped = 0
    errors = []

    for root, dirs, files in os.walk(KB_ROOT):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            filepath = os.path.join(root, fname)
            try:
                if migrate:
                    result = migrate_file(filepath)
                else:
                    result = process_file(filepath)
                if result:
                    processed += 1
                else:
                    skipped += 1
            except Exception as e:
                errors.append((filepath, str(e)))

    mode = "Migrated" if migrate else "Processed"
    print(f"{mode}: {processed}")
    print(f"Skipped (no frontmatter): {skipped}")
    if errors:
        print(f"Errors ({len(errors)}):")
        for fp, err in errors:
            print(f"  {fp}: {err}")


if __name__ == "__main__":
    main()
