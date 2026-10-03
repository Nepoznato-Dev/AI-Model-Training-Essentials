"""Create and validate the repository's translation file layout."""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGUAGE_FILE = ROOT / "languages" / "languages.txt"
SOURCE_ROOT = ROOT / "languages" / "english"
COLLECTIONS = ("skills", "wiki", "guides", "agent_modes")
PLACEHOLDER = """---
translation_status: pending
source: {source}
language: {language}
---

# Translation pending

This file is reserved for the {language} translation of `{source}`.
"""


def languages() -> list[str]:
    return [
        line.strip()
        for line in LANGUAGE_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]


def source_documents() -> list[tuple[str, Path]]:
    documents = []
    for collection in COLLECTIONS:
        source_root = SOURCE_ROOT / collection
        documents.extend(
            (collection, path.relative_to(source_root))
            for path in source_root.rglob("*.md")
            if "translations" not in path.parts
        )
    return sorted(documents)


def expected_files() -> list[tuple[Path, str, str]]:
    return [
        (
            ROOT / "languages" / language.lower() / collection / relative_path,
            language,
            f"{collection}/{relative_path.as_posix()}",
        )
        for language in languages()
        for collection, relative_path in source_documents()
    ]


def create() -> int:
    created = 0
    for destination, language, source in expected_files():
        if destination.exists():
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            PLACEHOLDER.format(language=language, source=source),
            encoding="utf-8",
        )
        created += 1
    print(f"Created {created} translation placeholders.")
    return 0


def check() -> int:
    missing = [
        destination
        for destination, _, _ in expected_files()
        if not destination.exists()
    ]
    if missing:
        print(f"Missing {len(missing)} translation files; run with --create.")
        for path in missing[:10]:
            print(f"  {path.relative_to(ROOT)}")
        return 1
    print(f"Validated {len(expected_files())} translation files.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--create", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    return create() if args.create else check()


if __name__ == "__main__":
    raise SystemExit(main())
