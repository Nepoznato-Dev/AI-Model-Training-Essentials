#!/usr/bin/env python3
"""Validate multilingual knowledge-base structure and protected year metadata."""
from __future__ import annotations

import pathlib
import re
import sys
from collections import Counter

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
    return {path.relative_to(root) for path in root.rglob("*.md") if path.is_file()}


def check_language_parity() -> None:
    if not SOURCE.exists():
        ERRORS.append(f"English knowledge-base source directory is missing: {SOURCE}")
        return

    source_files = relative_files(SOURCE)
    languages = sorted(path for path in KB.iterdir() if path.is_dir() and path.name != "English")

    for language in languages:
        files = relative_files(language)
        for path in sorted(source_files - files):
            WARNINGS.append(f"{language.name}: missing translation for {path}")
        for path in sorted(files - source_files):
            WARNINGS.append(f"{language.name}: extra translation file not in English source: {path}")


def check_protected_years() -> None:
    """Catch translated files that introduce too many occurrences of a year."""
    if not SOURCE.exists():
        return

    source_files = relative_files(SOURCE)
    source_years = {
        path: Counter(YEAR.findall(read(SOURCE / path)))
        for path in source_files
    }

    for language in sorted(path for path in KB.iterdir() if path.is_dir() and path.name != "English"):
        for relative in source_files:
            translated = language / relative
            if not translated.exists():
                continue

            observed = Counter(YEAR.findall(read(translated)))
            expected = source_years[relative]
            excessive = {
                year: count
                for year, count in observed.items()
                if count > expected.get(year, 0)
            }
            if excessive:
                ERRORS.append(
                    f"{language.name}/{relative}: year occurrence(s) exceed English source: "
                    f"{dict(sorted(excessive.items()))}; source counts={dict(sorted(expected.items()))}"
                )


def check_empty_files() -> None:
    if not KB.exists():
        return
    for path in KB.rglob("*.md"):
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
