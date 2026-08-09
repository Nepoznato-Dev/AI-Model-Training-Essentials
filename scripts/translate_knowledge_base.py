"""Translate Markdown knowledge-base files through the public Google endpoint.

The script is resumable: existing files are left untouched by default. It keeps
fenced code blocks, inline code, links, URLs, and HTML comments unchanged.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

LANGUAGES = {
    "Arabic": "ar", "Spanish": "es", "French": "fr", "German": "de",
    "Japanese": "ja", "Korean": "ko", "Mandarin_Simplified": "zh-CN",
    "Mandarin_Traditional": "zh-TW", "Portuguese": "pt",
    "Russian": "ru", "Italian": "it", "Polish": "pl", "Turkish": "tr",
    "Vietnamese": "vi", "Indonesian": "id", "Hindi": "hi", "Persian": "fa",
    "Thai": "th",
}
LANGUAGE_DIRECTORIES = {
    "Mandarin_Simplified": "Mandarin_Simplified",
    "Mandarin_Traditional": "Mandarin_Traditional",
}
FENCE = re.compile(r"^\s*(```|~~~)")
INLINE = re.compile(r"(`[^`]*`|<[^>]+>|https?://[^\s)]+|\[[^]]*\]\([^)]*\))")
LEAKED_PLACEHOLDER = re.compile(
    r"(?:XQZMARKER\d+XQZ|__(?:PROTECTED|PROTEGIDO|PROTEGE|PROTÉGÉ|[A-Z]+)_\d+__)",
    re.IGNORECASE,
)


def translate_text(text: str, target: str) -> str:
    if not text.strip() or not re.search(r"[A-Za-z]", text):
        return text
    protected: list[str] = []

    def hold(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f" XQZMARKER{len(protected) - 1}XQZ "

    query = INLINE.sub(hold, text)
    url = (
        "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en"
        f"&tl={quote(target)}&dt=t&q={quote(query)}"
    )
    request = Request(url, headers={"User-Agent": "knowledge-base-translator/1.0"})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
            break
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    result = "".join(part[0] for part in payload[0] if part and part[0])
    for index, original in enumerate(protected):
        result = result.replace(f" XQZMARKER{index}XQZ ", original)
        result = result.replace(f"XQZMARKER{index}XQZ", original)
    return result


def translate_markdown(source: str, target: str, delay: float) -> str:
    frontmatter_end = find_frontmatter_end(source)
    if frontmatter_end is not None:
        return source[:frontmatter_end] + translate_markdown(source[frontmatter_end:], target, delay)
    output: list[str] = []
    in_fence = False
    paragraph: list[str] = []

    def flush() -> None:
        if paragraph:
            block = "".join(paragraph)
            output.append(translate_text(block, target))
            paragraph.clear()

    for line in source.splitlines(keepends=True):
        if FENCE.match(line):
            flush()
            in_fence = not in_fence
            output.append(line)
        elif in_fence or not line.strip():
            flush()
            output.append(line)
        else:
            paragraph.append(line)
    flush()
    time.sleep(delay)
    return "".join(output)


def find_frontmatter_end(source: str) -> int | None:
    if not source.startswith("---\n"):
        return None
    closing = source.find("\n---", 4)
    if closing == -1:
        return None
    end = closing + len("\n---")
    if end < len(source) and source[end] == "\n":
        return end + 1
    return None


def translate_single_file(args: tuple) -> tuple[str, int]:
    """Translate a single file. Returns (language, processed_count)."""
    root, language, source_path, overwrite, delay = args
    source_root = root / "knowledge_base" / "English"
    target_root = root / "knowledge_base" / LANGUAGE_DIRECTORIES.get(language, language)
    destination = target_root / source_path.relative_to(source_root)
    source_content = source_path.read_text(encoding="utf-8")
    existing_content = destination.read_text(encoding="utf-8") if destination.exists() else ""
    if (
        destination.exists()
        and not overwrite
        and destination.stat().st_mtime_ns >= source_path.stat().st_mtime_ns
        and not LEAKED_PLACEHOLDER.search(existing_content)
    ):
        source_frontmatter_end = find_frontmatter_end(source_content)
        destination_frontmatter_end = find_frontmatter_end(existing_content)
        if (
            source_frontmatter_end is not None
            and destination_frontmatter_end is not None
            and source_content[:source_frontmatter_end] != existing_content[:destination_frontmatter_end]
        ):
            temporary = destination.with_suffix(destination.suffix + ".tmp")
            temporary.write_text(
                source_content[:source_frontmatter_end] + existing_content[destination_frontmatter_end:],
                encoding="utf-8",
                newline="",
            )
            temporary.replace(destination)
            print(f"[{language}] repaired metadata {destination.relative_to(root)}", flush=True)
            return (language, 1)
        return (language, 0)
    destination.parent.mkdir(parents=True, exist_ok=True)
    translated = translate_markdown(source_content, LANGUAGES[language], delay)
    if not translated.strip():
        raise ValueError(f"translation returned empty content for {source_path}")
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.write_text(translated, encoding="utf-8", newline="")
    temporary.replace(destination)
    print(f"[{language}] {destination.relative_to(root)}", flush=True)
    return (language, 1)


def translate_language(root: Path, language: str, limit: int, overwrite: bool, delay: float, file_workers: int = 1) -> int:
    source_root = root / "knowledge_base" / "English"
    target_root = root / "knowledge_base" / LANGUAGE_DIRECTORIES.get(language, language)
    files = sorted(source_root.rglob("*.md"))
    if limit:
        files = files[:limit]
    
    if file_workers <= 1:
        # Sequential processing
        processed = 0
        for source_path in files:
            _, count = translate_single_file((root, language, source_path, overwrite, delay))
            processed += count
    else:
        # Parallel file processing
        args_list = [(root, language, source_path, overwrite, delay) for source_path in files]
        with ThreadPoolExecutor(max_workers=file_workers) as executor:
            results = executor.map(translate_single_file, args_list)
            processed = sum(count for _, count in results)
    
    print(f"Completed {processed} files for {language}")
    return processed


def repair_metadata(root: Path, language: str) -> int:
    source_root = root / "knowledge_base" / "English"
    target_root = root / "knowledge_base" / LANGUAGE_DIRECTORIES.get(language, language)
    repaired = 0
    for source_path in source_root.rglob("*.md"):
        destination = target_root / source_path.relative_to(source_root)
        if not destination.exists():
            continue
        source_content = source_path.read_text(encoding="utf-8")
        destination_content = destination.read_text(encoding="utf-8")
        source_end = find_frontmatter_end(source_content)
        destination_end = find_frontmatter_end(destination_content)
        if source_end is None or destination_end is None:
            continue
        if source_content[:source_end] == destination_content[:destination_end]:
            continue
        temporary = destination.with_suffix(destination.suffix + ".tmp")
        temporary.write_text(
            source_content[:source_end] + destination_content[destination_end:],
            encoding="utf-8",
            newline="",
        )
        temporary.replace(destination)
        repaired += 1
        print(f"[{language} metadata {repaired}] {destination.relative_to(root)}", flush=True)
    print(f"Repaired metadata in {repaired} files for {language}")
    return repaired


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument(
        "--language",
        choices=sorted(LANGUAGES),
        nargs="+",
        dest="languages",
        help="languages to update (default: every configured language)",
    )
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--metadata-only", action="store_true")
    parser.add_argument("--delay", type=float, default=0.15)
    parser.add_argument("--workers", type=int, default=0, help="parallel languages (default: up to 4)")
    parser.add_argument("--file-workers", type=int, default=1, help="parallel files per language (default: 1)")
    args = parser.parse_args()
    source_root = args.root / "knowledge_base" / "English"
    if not source_root.is_dir():
        print(f"Source directory not found: {source_root}", file=sys.stderr)
        return 2
    if args.workers < 0:
        parser.error("--workers must be zero or greater")
    languages = args.languages or list(LANGUAGES)
    if args.metadata_only:
        for language in languages:
            repair_metadata(args.root, language)
        return 0
    workers = min(args.workers or 4, len(languages))
    try:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            jobs = [
                executor.submit(translate_language, args.root, language, args.limit, args.overwrite, args.delay, args.file_workers)
                for language in languages
            ]
            for job in jobs:
                job.result()
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())