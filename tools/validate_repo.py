#!/usr/bin/env python3
"""Lightweight repository QA checks for AI-Model-Training-Essentials.

The validator checks high-signal repository failures without pretending to
replace real execution tests. It is intentionally dependency-light; PyYAML is
part of the repository's base validation environment.
"""
from __future__ import annotations

import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []

SUSPICIOUS = ("Ã", "Â", "â€", "â€™", "â€œ", "â€”", "ï»¿")
MD_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


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
            match = FRONTMATTER.match(text)
            if not match:
                ERRORS.append(f"Malformed YAML frontmatter: {path}")
            else:
                check_agent_metadata(path, match.group(1)) if path.parts[0] == "agent_modes" else None


def check_agent_metadata(path: pathlib.Path, raw: str) -> None:
    """Validate the stable metadata contract used by agent modes."""
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        ERRORS.append(f"Invalid agent-mode YAML: {path}: {exc}")
        return
    if not isinstance(data, dict):
        ERRORS.append(f"Agent-mode frontmatter must be a mapping: {path}")
        return

    required = {"name", "description", "argument-hint", "tools", "agents", "handoffs"}
    missing = sorted(required - set(data))
    if missing:
        ERRORS.append(f"Agent-mode metadata missing {missing}: {path}")

    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        ERRORS.append(f"Agent-mode name must be a non-empty string: {path}")
    elif path.stem != name:
        ERRORS.append(f"Agent-mode filename/name mismatch: {path} declares {name!r}")

    for key in ("description", "argument-hint"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            ERRORS.append(f"Agent-mode {key!r} must be a non-empty string: {path}")

    tools = data.get("tools")
    if not isinstance(tools, list) or not all(isinstance(item, str) and item.strip() for item in tools):
        ERRORS.append(f"Agent-mode tools must be a list of non-empty strings: {path}")

    agents = data.get("agents")
    if not isinstance(agents, list) or not all(isinstance(item, str) and item.strip() for item in agents):
        ERRORS.append(f"Agent-mode agents must be a list of non-empty strings: {path}")

    handoffs = data.get("handoffs")
    if not isinstance(handoffs, list):
        ERRORS.append(f"Agent-mode handoffs must be a list: {path}")
    else:
        for index, handoff in enumerate(handoffs):
            if not isinstance(handoff, dict):
                ERRORS.append(f"Agent-mode handoff #{index + 1} must be a mapping: {path}")
                continue
            for key in ("label", "agent", "prompt", "send"):
                if key not in handoff:
                    ERRORS.append(f"Agent-mode handoff #{index + 1} missing {key!r}: {path}")
            if "label" in handoff and not isinstance(handoff["label"], str):
                ERRORS.append(f"Agent-mode handoff #{index + 1} label must be a string: {path}")
            if "agent" in handoff and not isinstance(handoff["agent"], str):
                ERRORS.append(f"Agent-mode handoff #{index + 1} agent must be a string: {path}")
            if "prompt" in handoff and not isinstance(handoff["prompt"], str):
                ERRORS.append(f"Agent-mode handoff #{index + 1} prompt must be a string: {path}")
            if "send" in handoff and not isinstance(handoff["send"], bool):
                ERRORS.append(f"Agent-mode handoff #{index + 1} send must be boolean: {path}")


def check_agent_references() -> None:
    """Catch handoffs/agent lists that point to modes that do not exist."""
    available = {p.stem for p in (ROOT / "agent_modes").glob("*.md")}
    for path in (ROOT / "agent_modes").glob("*.md"):
        match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
        if not match:
            continue
        try:
            data = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError:
            continue
        refs = list(data.get("agents", []) or [])
        refs.extend(
            handoff.get("agent")
            for handoff in (data.get("handoffs", []) or [])
            if isinstance(handoff, dict) and isinstance(handoff.get("agent"), str)
        )
        for ref in refs:
            if ref not in available:
                ERRORS.append(f"Agent-mode reference {ref!r} does not exist: {path}")


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
    check_agent_references()
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
