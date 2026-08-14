"""Bulk repair placeholder corruption in translated knowledge-base content files.

The translation script protects inline code/links/URLs by replacing them with
numbered markers before sending to Google Translate, then restores them after.
When restoration fails, the translated marker text remains as a placeholder
(e.g. __محمي_X__ in Arabic, __محافظت شده_X__ in Persian).

This script repairs those files by:
1. Splitting both English and translated files into paragraphs (separated by blank lines)
2. Extracting inline code from each English paragraph (same regex as the translator)
3. Mapping placeholders in each translated paragraph to English code by position
4. Replacing placeholders with the correct inline code

Usage:
    python scripts/fix_all_placeholders.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

KB_ROOT = Path(__file__).parent.parent / "knowledge_base"

# Same regex the translation script uses to protect inline content
INLINE = re.compile(r"(`[^`]*`|<[^>]+>|https?://[^\s)]+|\[[^]]*\]\([^)]*\))")
FENCE = re.compile(r"^\s*(```|~~~)")

# Placeholder patterns for each affected language
PLACEHOLDER_PATTERNS = {
    "Arabic": re.compile(r"__محمي_(\d+)__"),
    "Persian": re.compile(r"__محافظت شده_(\d+)__"),
}


def split_paragraphs(text: str) -> list[str]:
    """Split text into paragraph blocks, matching the translation script's logic.

    The translation script accumulates consecutive non-empty, non-fence lines
    into paragraphs. Empty lines, fence lines, and in-fence lines trigger a flush.
    We replicate this to ensure paragraph alignment.
    """
    paragraphs: list[str] = []
    current: list[str] = []
    in_fence = False

    for line in text.splitlines(keepends=True):
        if FENCE.match(line):
            if current:
                paragraphs.append("".join(current))
                current = []
            in_fence = not in_fence
            paragraphs.append(line)
        elif in_fence or not line.strip():
            if current:
                paragraphs.append("".join(current))
                current = []
            paragraphs.append(line)
        else:
            current.append(line)

    if current:
        paragraphs.append("".join(current))

    return paragraphs


def extract_code_items(text: str) -> list[str]:
    """Extract inline code/links/URLs from text (same as translator)."""
    return INLINE.findall(text)


def count_placeholders(text: str, pattern: re.Pattern) -> int:
    return len(pattern.findall(text))


def find_frontmatter_end(source: str) -> int | None:
    """Find the end of YAML frontmatter (delimited by ---)."""
    if not source.startswith("---\n"):
        return None
    closing = source.find("\n---", 4)
    if closing == -1:
        return None
    end = closing + len("\n---")
    if end < len(source) and source[end] == "\n":
        return end + 1
    return end


def fix_file(eng_path: Path, trans_path: Path, lang: str) -> tuple[int, bool]:
    """Fix placeholders in a single translated file.

    Returns (placeholders_fixed, had_placeholders).
    """
    pattern = PLACEHOLDER_PATTERNS[lang]

    trans_content = trans_path.read_text(encoding="utf-8")
    total_placeholders = count_placeholders(trans_content, pattern)

    if total_placeholders == 0:
        return (0, False)

    eng_content = eng_path.read_text(encoding="utf-8")

    # Skip frontmatter in both files (frontmatter may have been translated
    # by an older script, causing paragraph misalignment)
    eng_fm_end = find_frontmatter_end(eng_content)
    trans_fm_end = find_frontmatter_end(trans_content)

    eng_body = eng_content[eng_fm_end:] if eng_fm_end else eng_content
    trans_body = trans_content[trans_fm_end:] if trans_fm_end else trans_content
    trans_prefix = trans_content[:trans_fm_end] if trans_fm_end else ""

    # Split both bodies into paragraphs using the same logic as the translator
    eng_paras = split_paragraphs(eng_body)
    trans_paras = split_paragraphs(trans_body)

    fixed_count = 0
    new_trans_paras = []

    # Track paragraph indices (only count non-blank, non-fence paragraphs)
    eng_para_indices = [i for i, p in enumerate(eng_paras) if p.strip() and not FENCE.match(p)]
    trans_para_indices = [i for i, p in enumerate(trans_paras) if p.strip() and not FENCE.match(p)]

    # Build mapping: for each trans paragraph with placeholders, find corresponding eng paragraph
    eng_pi = 0  # index into eng_para_indices

    for ti, trans_para in enumerate(trans_paras):
        ph_count = count_placeholders(trans_para, pattern)

        if ph_count == 0 or not trans_para.strip() or FENCE.match(trans_para):
            new_trans_paras.append(trans_para)
            # Advance eng index for non-blank non-fence paragraphs
            if trans_para.strip() and not FENCE.match(trans_para):
                eng_pi += 1
            continue

        # Find corresponding English paragraph
        max_idx = max(int(m) for m in pattern.findall(trans_para))
        eng_code_items = None

        # Try current eng paragraph first
        if eng_pi < len(eng_para_indices):
            ei = eng_para_indices[eng_pi]
            code_items = extract_code_items(eng_paras[ei])
            if len(code_items) > max_idx:
                eng_code_items = code_items

        # If that didn't work, search nearby
        if eng_code_items is None:
            for offset in range(-3, 6):
                check_pi = eng_pi + offset
                if 0 <= check_pi < len(eng_para_indices):
                    ei = eng_para_indices[check_pi]
                    code_items = extract_code_items(eng_paras[ei])
                    if len(code_items) > max_idx:
                        eng_code_items = code_items
                        break

        if eng_code_items is None:
            # Can't find matching paragraph, keep as-is
            new_trans_paras.append(trans_para)
            if trans_para.strip() and not FENCE.match(trans_para):
                eng_pi += 1
            continue

        def replace_placeholder(match):
            nonlocal fixed_count
            idx = int(match.group(1))
            if idx < len(eng_code_items):
                fixed_count += 1
                return eng_code_items[idx]
            return match.group(0)

        new_para = pattern.sub(replace_placeholder, trans_para)
        new_trans_paras.append(new_para)
        if trans_para.strip() and not FENCE.match(trans_para):
            eng_pi += 1

    new_content = trans_prefix + "".join(new_trans_paras)

    if fixed_count > 0:
        trans_path.write_text(new_content, encoding="utf-8")

    return (fixed_count, True)


def scan_for_affected_files(lang: str) -> list[tuple[Path, Path]]:
    """Find all files in a language that have placeholders."""
    pattern = PLACEHOLDER_PATTERNS[lang]
    eng_root = KB_ROOT / "English"
    lang_root = KB_ROOT / lang
    pairs = []

    for trans_file in sorted(lang_root.rglob("*.md")):
        if trans_file.name == "README.md":
            continue
        content = trans_file.read_text(encoding="utf-8")
        if count_placeholders(content, pattern) > 0:
            rel = trans_file.relative_to(lang_root)
            eng_file = eng_root / rel
            if eng_file.exists():
                pairs.append((eng_file, trans_file))
            else:
                print(f"  WARNING: No English equivalent for {trans_file.relative_to(KB_ROOT)}")

    return pairs


def main():
    print("=" * 60)
    print("Bulk Placeholder Repair")
    print("=" * 60)

    total_fixed = 0
    total_files = 0

    for lang, pattern in PLACEHOLDER_PATTERNS.items():
        print(f"\n--- {lang} ---")
        pairs = scan_for_affected_files(lang)
        print(f"  Found {len(pairs)} files with placeholders")

        for eng_path, trans_path in pairs:
            fixed, had = fix_file(eng_path, trans_path, lang)
            rel = trans_path.relative_to(KB_ROOT)
            if had:
                total_files += 1
                total_fixed += fixed
                print(f"  [{rel}] fixed {fixed} placeholders")

    # Verification sweep
    print(f"\n{'=' * 60}")
    print("Verification sweep...")
    remaining = 0
    for lang, pattern in PLACEHOLDER_PATTERNS.items():
        lang_root = KB_ROOT / lang
        for md_file in lang_root.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            count = count_placeholders(content, pattern)
            if count > 0:
                remaining += count
                print(f"  REMAINING: {md_file.relative_to(KB_ROOT)} — {count} placeholders")

    print(f"\n{'=' * 60}")
    print(f"Summary: fixed {total_fixed} placeholders across {total_files} files")
    if remaining == 0:
        print("ALL CLEAR — zero placeholders corruption remaining!")
    else:
        print(f"WARNING: {remaining} placeholders still remain (see above)")
    print("=" * 60)


if __name__ == "__main__":
    main()
