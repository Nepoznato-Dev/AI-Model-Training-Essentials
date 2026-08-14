"""Re-translate only files that have placeholder corruption.

Uses the existing translation infrastructure (translate_knowledge_base.py)
but targets only files that still have leaked placeholders from a previous
translation run.
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

# Import translation functions from the existing script
sys.path.insert(0, str(Path(__file__).parent))
from translate_knowledge_base import (
    LANGUAGES,
    translate_markdown,
)

KB_ROOT = Path(__file__).parent.parent / "knowledge_base"

# All known placeholder patterns (from any language)
PLACEHOLDER_PATTERNS = {
    "Arabic": re.compile(r"__محمي_\d+__"),
    "Persian": re.compile(r"__محافظت شده_\d+__"),
    "French": re.compile(r"__PROTÉGÉ_\d+__"),
}


def find_affected_files(language: str) -> list[Path]:
    """Find English source files whose translations have placeholders."""
    pattern = PLACEHOLDER_PATTERNS.get(language)
    if not pattern:
        return []

    lang_root = KB_ROOT / language
    eng_root = KB_ROOT / "English"
    affected = []

    for trans_file in sorted(lang_root.rglob("*.md")):
        if trans_file.name == "README.md":
            continue
        content = trans_file.read_text(encoding="utf-8")
        if pattern.search(content):
            rel = trans_file.relative_to(lang_root)
            eng_file = eng_root / rel
            if eng_file.exists():
                affected.append(eng_file)

    return affected


def retranslate_file(eng_file: Path, language: str, delay: float = 0.5) -> bool:
    """Re-translate a single file and check if placeholders are resolved."""
    lang_root = KB_ROOT / language
    dest = lang_root / eng_file.relative_to(KB_ROOT / "English")

    source_content = eng_file.read_text(encoding="utf-8")
    try:
        result = translate_markdown(source_content, LANGUAGES[language], delay)
        if not result.strip():
            print(f"    ERROR: empty translation for {eng_file.name}")
            return False

        # Check if result still has placeholders
        pattern = PLACEHOLDER_PATTERNS.get(language)
        if pattern and pattern.search(result):
            count = len(pattern.findall(result))
            print(f"    WARNING: {count} placeholders remain after re-translation")

        # Write the result
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_suffix(dest.suffix + ".tmp")
        tmp.write_text(result, encoding="utf-8", newline="")
        tmp.replace(dest)
        return True
    except Exception as e:
        print(f"    ERROR: {e}")
        return False


def main():
    print("=" * 60)
    print("Targeted Re-translation of Placeholder-Corrupted Files")
    print("=" * 60)

    languages_to_fix = ["Arabic", "Persian"]
    total_fixed = 0
    total_failed = 0

    for language in languages_to_fix:
        pattern = PLACEHOLDER_PATTERNS.get(language)
        if not pattern:
            continue

        affected = find_affected_files(language)
        if not affected:
            print(f"\n[{language}] No files need re-translation")
            continue

        print(f"\n[{language}] {len(affected)} files to re-translate")

        for i, eng_file in enumerate(affected):
            rel = eng_file.relative_to(KB_ROOT / "English")
            print(f"  [{i+1}/{len(affected)}] {rel}...", end=" ", flush=True)

            ok = retranslate_file(eng_file, language, delay=0.5)
            if ok:
                total_fixed += 1
                print("OK")
            else:
                total_failed += 1
                print("FAILED")

            # Small delay to avoid rate limiting
            time.sleep(0.3)

    # Verification
    print(f"\n{'=' * 60}")
    print("Verification sweep...")
    remaining = 0
    for language, pattern in PLACEHOLDER_PATTERNS.items():
        lang_root = KB_ROOT / language
        if not lang_root.exists():
            continue
        for md_file in lang_root.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            count = len(pattern.findall(content))
            if count > 0:
                remaining += count
                print(f"  REMAINING: {md_file.relative_to(KB_ROOT)} — {count}")

    print(f"\n{'=' * 60}")
    print(f"Re-translated: {total_fixed} files OK, {total_failed} failed")
    if remaining == 0:
        print("ALL CLEAR — zero placeholder corruption!")
    else:
        print(f"WARNING: {remaining} placeholders still remain")
    print("=" * 60)


if __name__ == "__main__":
    main()
