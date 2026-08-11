#!/usr/bin/env python3
"""Lightweight repository QA checks for AI-Model-Training-Essentials.

This validator checks high-signal repository failures without pretending to
replace real execution tests. Existing content-quality findings are reported
as warnings until the V2 migration has cleaned the repository baseline.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []

SUSPICIOUS = ("Ã", "Â", "â€", "â€™", "â€œ", "â€”", "ï»¿")
MD_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FRONTMATTER = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


def text_files() -> list[pathlib.Path]:
    return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def check_encoding_and_frontmatter() -> None:
    for path in text_files():
        try:
            raw = path.read_bytes()
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            ERRORS.append(f"Non-UTF-8 file: {path}: {exc}")
            continue
        if raw.startswith(b"\xef\xbb\xbf"):
            WARNINGS.append(f"UTF-8 BOM before content: {path}")
        if any(token in text for token in SUSPICIOUS):
            WARNINGS.append(f"Possible mojibake: {path}")
        if path.parts[0] in {"skills", "agent_modes"} and text.startswith("---"):
            if not FRONTMATTER.match(text):
                ERRORS.append(f"Malformed YAML frontmatter: {path}")


def check_markdown_links() -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for target in MD_LINK.findall(text):
            target = target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            candidate = (path.parent / target).resolve()
            if not candidate.exists():
                WARNINGS.append(f"Broken Markdown link: {path} -> {target}")


def check_python_source() -> None:
    for path in ROOT.rglob("*.py"):
        if ".git" in path.parts:
            continue
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as exc:
            ERRORS.append(f"Python syntax error: {path}: {exc}")


def main() -> int:
    check_encoding_and_frontmatter()
    check_markdown_links()
    check_python_source()

    for warning in WARNINGS:
        print(f"WARNING: {warning}")
    for error in ERRORS:
        print(f"ERROR: {error}")

    print(f"\nValidation complete: {len(ERRORS)} errors, {len(WARNINGS)} warnings")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
