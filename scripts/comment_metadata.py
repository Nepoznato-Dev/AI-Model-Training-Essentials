"""
Script to:
1. Replace author/contributor names with 'Nepoznato-Dev' in YAML frontmatter
2. Wrap the entire YAML frontmatter block in HTML comments so it's hidden in plain Markdown
"""

import os
import re

KB_ROOT = os.path.join(os.path.dirname(__file__), "..", "knowledge_base")

def process_file(filepath):
    """Process a single markdown file."""
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

    # Wrap frontmatter in HTML comments
    # Remove the --- delimiters and wrap content
    # Original: ---\n...content...\n---
    # Result:   <!-- \n---\n...content...\n---\n -->
    new_frontmatter = "<!--\n" + frontmatter + "\n-->"

    # Ensure there's a newline between the comment close and the rest
    if rest and not rest.startswith("\n"):
        new_frontmatter += "\n"

    new_content = new_frontmatter + rest

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def main():
    processed = 0
    skipped = 0
    errors = []

    for root, dirs, files in os.walk(KB_ROOT):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            filepath = os.path.join(root, fname)
            try:
                result = process_file(filepath)
                if result:
                    processed += 1
                else:
                    skipped += 1
            except Exception as e:
                errors.append((filepath, str(e)))

    print(f"Processed: {processed}")
    print(f"Skipped (no frontmatter): {skipped}")
    if errors:
        print(f"Errors ({len(errors)}):")
        for fp, err in errors:
            print(f"  {fp}: {err}")


if __name__ == "__main__":
    main()
