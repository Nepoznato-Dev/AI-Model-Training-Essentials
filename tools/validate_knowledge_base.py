#!/usr/bin/env python3
"""Validate multilingual knowledge-base structure and protected year metadata.

This intentionally checks conservative invariants rather than trying to prove
that translations are semantically identical. In particular, four-digit years
found in a translated file must match the English source at the same relative
path. This catches accidental bulk date rewrites (for example, changing every
historical year to the current year) without attempting to normalize locale-
specific date formatting.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge_base"
SOURCE = KB / "English"
ERRORS: list[str] = []
WARNINGS: list[str] = []
YEAR = re.compile(r"(?<!\d)(?:1[0-9]{3}|20[0-9]{2}|21[0-9]{2})(?!\d)")


def read(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        ERRORS.append(f"Non-UTF-8 knowledge-base file: {path}: {exc}")
        return ""


def relative_files(root: pathlib.Path) -> set[pathlib.Path]:
    return {
        path.relative_to(root)
        for path in root.rglob("*.md")
        if path.is_file()
    }


def check_language_parity() -> None:
    if not SOURCE.exists():
        ERRORS.append(f"English knowledge-base source directory is missing: {SOURCE}")
        return

    source_files = relative_files(SOURCE)
    languages = sorted(
        path for path in KB.iterdir()
        if path.is_dir() and path.name != "English"
    )

    for language in languages:
        files = relative_files(language)
        missing = sorted(source_files - files)
        extra = sorted(files - source_files)
        for path in missing:
            WARNINGS.append(f"{language.name}: missing translation for {path}")
        for path in extra:
            WARNINGS.append(f"{language.name}: extra translation file not in English source: {path}")


def check_protected_years() -> None:
    """Ensure translations do not silently change source years."""
    if not SOURCE.exists():
        return

    source_files = relative_files(SOURCE)
    source_years = {
        path: set(YEAR.findall(read(SOURCE / path)))
        for path in source_files
    }

    for language in sorted(
        path for path in KB.iterdir()
        if path.is_dir() and path.name != "English"
    ):
        for relative in source_files:
            translated = language / relative
            if not translated.exists():
                continue
            years = set(YEAR.findall(read(translated)))
            expected = source_years[relative]
            # Only flag years that appear in the translation but not the source.
            # Missing years can be legitimate when a translation paraphrases text.
            unexpected = sorted(years - expected)
            if unexpected:
                ERRORS.append(
                    f"{language.name}/{relative}: unexpected year(s) {unexpected}; "
                    f"English source years are {sorted(expected)}"
                )


def check_empty_files() -> None:
    for path in KB.rglob("*.md") if KB.exists() else []:
        if path.is_file() and not read(path).strip():
            WARNINGS.append(f"Empty knowledge-base file: {path}")


def main() -> int:
    if not KB.exists():
        print("knowledge_base/ does not exist; skipping knowledge-base validation")
        return 0

    check_language_parity()
    check_protected_years()
    check_empty_files()

    for warning in WARNINGS:
        print(f"WARNING: {warning}")
    for error in ERRORS:
        print(f"ERROR: {error}")

    print(f"\nKnowledge-base validation complete: {len(ERRORS)} errors, {len(WARNINGS)} warnings")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
