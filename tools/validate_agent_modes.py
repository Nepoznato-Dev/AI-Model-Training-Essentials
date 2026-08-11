#!/usr/bin/env python3
"""Validate the lightweight frontmatter contract used by agent modes.

This intentionally avoids a YAML dependency: the repository only needs to
validate the small metadata subset shared by its mode files. Full YAML parsing
can be introduced later if the schema grows beyond this contract.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODE_DIR = ROOT / "agent_modes"
ERRORS: list[str] = []

FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
REQUIRED = {"name", "description", "argument-hint", "tools", "agents"}


def parse_frontmatter(path: pathlib.Path) -> dict[str, object] | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        ERRORS.append(f"{path}: missing or malformed frontmatter")
        return None

    body = match.group("body")
    result: dict[str, object] = {}
    current_list: str | None = None
    list_items: list[str] = []

    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if current_list:
            if line == "]":
                result[current_list] = list_items
                current_list = None
                list_items = []
                continue
            if line.startswith("'") and line.endswith("',"):
                list_items.append(line[1:-2])
                continue
            if line.startswith("'") and line.endswith("'"):
                list_items.append(line[1:-1])
                continue
            ERRORS.append(f"{path}: invalid list item in {current_list!r}: {line}")
            continue

        if ":" not in line:
            ERRORS.append(f"{path}: invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "[":
            current_list = key
            list_items = []
        else:
            result[key] = value

    if current_list:
        ERRORS.append(f"{path}: unterminated list for {current_list!r}")
    return result


def main() -> int:
    if not MODE_DIR.exists():
        ERRORS.append("agent_modes directory does not exist")
    else:
        for path in sorted(MODE_DIR.glob("*.md")):
            if path.name.lower() == "readme.md":
                continue
            data = parse_frontmatter(path)
            if data is None:
                continue

            missing = REQUIRED - data.keys()
            for key in sorted(missing):
                ERRORS.append(f"{path}: missing required field {key!r}")

            if data.get("name") != path.stem:
                ERRORS.append(
                    f"{path}: frontmatter name {data.get('name')!r} does not match filename {path.stem!r}"
                )

            for field in ("tools", "agents"):
                value = data.get(field)
                if not isinstance(value, list):
                    ERRORS.append(f"{path}: {field!r} must be a list")

            tools = data.get("tools")
            if isinstance(tools, list) and not tools:
                ERRORS.append(f"{path}: tools list must not be empty")

    for error in ERRORS:
        print(f"ERROR: {error}")
    print(f"Agent-mode validation complete: {len(ERRORS)} errors")
    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
