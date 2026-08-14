"""Restructure non-English knowledge-base directories to mirror the English hierarchy.

This script:
1. Creates subdirectories in each language to match the English structure
2. Moves existing flat files into the correct subdirectories
3. Handles filename mismatches between English and non-English languages
4. Reports files that need to be translated (exist in English but not in target language)

Usage:
    python scripts/restructure_and_translate.py --root . --restructure
    python scripts/restructure_and_translate.py --root . --translate --languages Arabic French
    python scripts/restructure_and_translate.py --root . --translate --all-languages
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

# ── Configuration ──────────────────────────────────────────────────────────

LANGUAGES = {
    "Arabic": "ar", "Spanish": "es", "French": "fr", "German": "de",
    "Japanese": "ja", "Korean": "ko", "Mandarin_Simplified": "zh-CN",
    "Mandarin_Traditional": "zh-TW", "Portuguese": "pt",
    "Russian": "ru", "Italian": "it", "Polish": "pl", "Turkish": "tr",
    "Vietnamese": "vi", "Indonesian": "id", "Hindi": "hi", "Persian": "fa",
    "Thai": "th", "Bengali": "bn", "Urdu": "ur", "Filipino": "tl",
    "Swahili": "sw",
}

# Files with different names in non-English vs English.
# Key = non-English filename, Value = (english_filename, target_subdir)
FILENAME_OVERRIDES: dict[str, tuple[str, str] | None] = {
    "science_and_nature.md": None,  # orphaned - no English equivalent
    "math_and_logic.md": ("mathematics.md", "03_data_science_and_analytics/mathematics"),
    "arts_and_literature.md": None,  # orphaned - split into multiple arts/ files
    "dictionary.md": None,  # orphaned - no English equivalent
}

# Where each file should live in the English hierarchy (relative to knowledge_base/{lang}/)
# Built from the English directory structure.
FILE_TO_SUBDIR: dict[str, str] = {
    # 02_ai_and_machine_learning subdirs
    "federated_learning_and_privacy.md": "02_ai_and_machine_learning/architectures",
    "generative_ai_deep_dive.md": "02_ai_and_machine_learning/architectures",
    "graph_neural_networks.md": "02_ai_and_machine_learning/architectures",
    "recommendation_systems.md": "02_ai_and_machine_learning/architectures",
    "reinforcement_learning.md": "02_ai_and_machine_learning/architectures",
    "data_engineering_and_pipelines.md": "02_ai_and_machine_learning/engineering",
    "local_ai_architecture.md": "02_ai_and_machine_learning/engineering",
    "ml_engineering_and_mlops.md": "02_ai_and_machine_learning/engineering",
    "model_optimization_and_deployment.md": "02_ai_and_machine_learning/engineering",
    "phi3_and_local_models.md": "02_ai_and_machine_learning/engineering",
    "ai_ethics_and_governance.md": "02_ai_and_machine_learning/ethics_and_safety",
    "ai_safety_and_alignment.md": "02_ai_and_machine_learning/ethics_and_safety",
    "artificial_intelligence.md": "02_ai_and_machine_learning/foundations",
    "ml_evaluation_and_workflow.md": "02_ai_and_machine_learning/foundations",
    "prompt_engineering.md": "02_ai_and_machine_learning/foundations",
    "computer_vision_fundamentals.md": "02_ai_and_machine_learning/nlp_and_speech",
    "multimodal_ai.md": "02_ai_and_machine_learning/nlp_and_speech",
    "nlp_fundamentals.md": "02_ai_and_machine_learning/nlp_and_speech",
    "speech_and_audio_processing.md": "02_ai_and_machine_learning/nlp_and_speech",
    "time_series_and_forecasting.md": "02_ai_and_machine_learning/nlp_and_speech",
    # 03_data_science_and_analytics subdirs
    "logic_and_critical_thinking.md": "03_data_science_and_analytics/mathematics",
    "mathematics.md": "03_data_science_and_analytics/mathematics",
    "statistics_and_probability.md": "03_data_science_and_analytics/mathematics",
    # 04_natural_sciences subdirs
    "astronomy_and_cosmology.md": "04_natural_sciences/earth_and_environment",
    "earth_science.md": "04_natural_sciences/earth_and_environment",
    "environmental_science_and_sustainability.md": "04_natural_sciences/earth_and_environment",
    "biology_fundamentals.md": "04_natural_sciences/life_sciences",
    "food_agriculture_and_nutrition.md": "04_natural_sciences/life_sciences",
    "genetics_and_genomics.md": "04_natural_sciences/life_sciences",
    "medicine_and_healthcare.md": "04_natural_sciences/life_sciences",
    "neuroscience.md": "04_natural_sciences/life_sciences",
    "chemistry.md": "04_natural_sciences/physical_sciences",
    "materials_science.md": "04_natural_sciences/physical_sciences",
    "physics.md": "04_natural_sciences/physical_sciences",
    # 06_humanities_and_arts subdirs
    "literature.md": "06_humanities_and_arts/arts",
    "music_theory_and_acoustics.md": "06_humanities_and_arts/arts",
    "performing_arts.md": "06_humanities_and_arts/arts",
    "visual_arts.md": "06_humanities_and_arts/arts",
    "geography_and_geopolitics.md": "06_humanities_and_arts/history",
    "history_and_culture.md": "06_humanities_and_arts/history",
    "language_and_english.md": "06_humanities_and_arts/language",
    "linguistics_and_language_science.md": "06_humanities_and_arts/language",
    "philosophy_and_critical_thinking.md": "06_humanities_and_arts/philosophy_and_mind",
    "psychology_and_human_behavior.md": "06_humanities_and_arts/philosophy_and_mind",
    "world_religions_and_comparative_mythology.md": "06_humanities_and_arts/religion_and_mythology",
    # 08_future_and_trends subdirs
    "demographic_shifts.md": "08_future_and_trends/society_and_domains",
    "education_transformation.md": "08_future_and_trends/society_and_domains",
    "future_healthcare.md": "08_future_and_trends/society_and_domains",
    "future_of_work.md": "08_future_and_trends/society_and_domains",
    "future_transportation.md": "08_future_and_trends/society_and_domains",
    "sustainable_future.md": "08_future_and_trends/society_and_domains",
    "2026_and_future_events.md": "08_future_and_trends/strategy",
    "geostrategic_futures.md": "08_future_and_trends/strategy",
    "scenario_planning.md": "08_future_and_trends/strategy",
    "ai_in_everyday_life.md": "08_future_and_trends/technology",
    "climate_technology_and_green_innovation.md": "08_future_and_trends/technology",
    "emerging_technologies.md": "08_future_and_trends/technology",
    "future_of_computing.md": "08_future_and_trends/technology",
    "space_exploration_roadmap.md": "08_future_and_trends/technology",
    # 10_quick_reference subdirs
    "ansible_quick_ref.md": "10_quick_reference/infrastructure",
    "bash_and_shell_scripting.md": "10_quick_reference/infrastructure",
    "cicd_pipeline_config.md": "10_quick_reference/infrastructure",
    "cloud_services_comparison.md": "10_quick_reference/infrastructure",
    "docker_and_kubernetes.md": "10_quick_reference/infrastructure",
    "linux_commands.md": "10_quick_reference/infrastructure",
    "prometheus_and_grafana.md": "10_quick_reference/infrastructure",
    "terraform_quick_ref.md": "10_quick_reference/infrastructure",
    "git_commands.md": "10_quick_reference/programming",
    "python_syntax.md": "10_quick_reference/programming",
    "regular_expressions.md": "10_quick_reference/programming",
    "sql_quick_ref.md": "10_quick_reference/programming",
}


# ── Translation helpers (reuses logic from translate_knowledge_base.py) ────

FENCE = re.compile(r"^\s*(```|~~~)")
INLINE = re.compile(r"(`[^`]*`|<[^>]+>|https?://[^\s)]+|\[[^]]*\]\([^)]*\))")


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


def translate_markdown(source: str, target: str, delay: float = 0.15) -> str:
    frontmatter_end = find_frontmatter_end(source)
    if frontmatter_end is not None:
        return source[:frontmatter_end] + translate_markdown(
            source[frontmatter_end:], target, delay
        )
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


# ── Phase 1: Restructure ──────────────────────────────────────────────────

def restructure_language(root: Path, language: str, dry_run: bool = False) -> dict:
    """Move flat files into the correct subdirectories for one language."""
    lang_dir = root / "knowledge_base" / language
    stats = {"moved": 0, "skipped": 0, "orphans": [], "errors": []}

    # Collect all non-README .md files that are directly inside numbered dirs
    for numbered_dir in sorted(lang_dir.iterdir()):
        if not numbered_dir.is_dir():
            continue
        for md_file in sorted(numbered_dir.glob("*.md")):
            if md_file.name == "README.md":
                continue

            filename = md_file.name
            target_subdir = FILE_TO_SUBDIR.get(filename)

            if target_subdir is None:
                # Check overrides for renamed files
                if filename in FILENAME_OVERRIDES:
                    override = FILENAME_OVERRIDES[filename]
                    if override is None:
                        stats["orphans"].append(str(md_file.relative_to(lang_dir)))
                        continue
                    # Override provides (english_name, target_subdir)
                    eng_name, target_subdir = override
                    dest_dir = lang_dir / target_subdir
                    dest_file = dest_dir / eng_name
                    if dry_run:
                        print(f"  [DRY-RUN] {md_file.relative_to(lang_dir)} -> {dest_file.relative_to(lang_dir)} (renamed)")
                        stats["moved"] += 1
                        continue
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    if dest_file.exists():
                        md_file.unlink()
                        stats["skipped"] += 1
                        continue
                    md_file.rename(dest_file)
                    stats["moved"] += 1
                    continue

                # File doesn't need moving or is unknown
                if "programming_languages" in str(md_file):
                    stats["skipped"] += 1
                    continue

                stats["skipped"] += 1
                continue

            # We need to move this file
            dest_dir = lang_dir / target_subdir
            dest_file = dest_dir / filename

            if dry_run:
                print(f"  [DRY-RUN] {md_file.relative_to(lang_dir)} -> {dest_file.relative_to(lang_dir)}")
                stats["moved"] += 1
                continue

            dest_dir.mkdir(parents=True, exist_ok=True)
            if dest_file.exists():
                # Already exists at destination – remove the flat copy
                md_file.unlink()
                stats["skipped"] += 1
                continue

            md_file.rename(dest_file)
            stats["moved"] += 1

    return stats


def restructure_all(root: Path, languages: list[str], dry_run: bool = False) -> None:
    """Restructure all specified languages."""
    print("\n=== PHASE 1: RESTRUCTURE ===\n")
    for language in languages:
        lang_dir = root / "knowledge_base" / language
        if not lang_dir.is_dir():
            print(f"  [{language}] SKIP – directory not found")
            continue

        print(f"  [{language}] restructuring...")
        stats = restructure_language(root, language, dry_run)
        print(f"    moved: {stats['moved']}, skipped: {stats['skipped']}, orphans: {len(stats['orphans'])}")
        if stats["orphans"]:
            for orphan in stats["orphans"]:
                print(f"      orphan: {orphan}")


# ── Phase 2: Translate missing files ──────────────────────────────────────

def find_missing_files(root: Path, language: str) -> list[Path]:
    """Find English files that don't have a corresponding translation."""
    english_dir = root / "knowledge_base" / "English"
    lang_dir = root / "knowledge_base" / language
    missing: list[Path] = []

    for eng_file in sorted(english_dir.rglob("*.md")):
        if eng_file.name == "README.md":
            continue
        rel = eng_file.relative_to(english_dir)
        target_file = lang_dir / rel
        if not target_file.exists():
            missing.append(eng_file)

    return missing


def _translate_one_file(args: tuple) -> tuple[str, bool]:
    """Translate a single file. Returns (language, success)."""
    root, language, eng_file, overwrite, delay = args
    english_dir = root / "knowledge_base" / "English"
    lang_dir = root / "knowledge_base" / language
    lang_code = LANGUAGES[language]
    rel = eng_file.relative_to(english_dir)
    dest = lang_dir / rel
    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists() and not overwrite:
        return (language, False)

    source_content = eng_file.read_text(encoding="utf-8")
    try:
        result = translate_markdown(source_content, lang_code, delay)
        if not result.strip():
            print(f"    [{language}] ERROR empty translation: {rel}", flush=True)
            return (language, False)
        tmp = dest.with_suffix(dest.suffix + ".tmp")
        tmp.write_text(result, encoding="utf-8", newline="")
        tmp.replace(dest)
        print(f"    [{language}] {rel}", flush=True)
        return (language, True)
    except Exception as e:
        print(f"    [{language}] ERROR {rel}: {e}", flush=True)
        return (language, False)


def translate_missing_files(
    root: Path,
    language: str,
    limit: int = 0,
    delay: float = 0.15,
    overwrite: bool = False,
    file_workers: int = 1,
) -> int:
    """Translate missing English files into the target language."""
    missing = find_missing_files(root, language)

    if limit:
        missing = missing[:limit]

    if not missing:
        print(f"  [{language}] No missing files to translate", flush=True)
        return 0

    print(f"  [{language}] {len(missing)} files to translate", flush=True)

    args_list = [(root, language, eng_file, overwrite, delay) for eng_file in missing]

    if file_workers <= 1:
        translated = sum(1 for _, ok in map(_translate_one_file, args_list) if ok)
    else:
        with ThreadPoolExecutor(max_workers=file_workers) as executor:
            translated = sum(1 for _, ok in executor.map(_translate_one_file, args_list) if ok)

    print(f"  [{language}] Translated {translated}/{len(missing)} files", flush=True)
    return translated


def translate_all(root: Path, languages: list[str], limit: int = 0, delay: float = 0.15, overwrite: bool = False, workers: int = 1, file_workers: int = 1) -> None:
    """Translate missing files for all specified languages."""
    print("\n=== PHASE 2: TRANSLATE MISSING FILES ===\n", flush=True)
    if workers <= 1:
        for language in languages:
            lang_dir = root / "knowledge_base" / language
            if not lang_dir.is_dir():
                print(f"  [{language}] SKIP - directory not found")
                continue
            translate_missing_files(root, language, limit, delay, overwrite, file_workers)
    else:
        def _worker(lang: str) -> tuple[str, int]:
            lang_dir = root / "knowledge_base" / lang
            if not lang_dir.is_dir():
                return (lang, 0)
            count = translate_missing_files(root, lang, limit, delay, overwrite, file_workers)
            return (lang, count)

        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_worker, lang): lang for lang in languages}
            for future in as_completed(futures):
                lang, count = future.result()
                print(f"  [{lang}] Done: {count} files translated", flush=True)


# ── Phase 3: Verify ───────────────────────────────────────────────────────

def verify_structure(root: Path, languages: list[str]) -> None:
    """Verify all language directories match the English structure."""
    print("\n=== VERIFICATION ===\n")
    english_dir = root / "knowledge_base" / "English"
    eng_files = set()
    for f in english_dir.rglob("*.md"):
        if f.name != "README.md":
            eng_files.add(str(f.relative_to(english_dir)))

    print(f"  English: {len(eng_files)} files\n")

    all_match = True
    for language in languages:
        lang_dir = root / "knowledge_base" / language
        if not lang_dir.is_dir():
            print(f"  [{language}] SKIP – directory not found")
            continue

        lang_files = set()
        for f in lang_dir.rglob("*.md"):
            if f.name != "README.md":
                lang_files.add(str(f.relative_to(lang_dir)))

        missing = eng_files - lang_files
        extra = lang_files - eng_files

        status = "OK" if not missing and not extra else "MISMATCH"
        if status == "MISMATCH":
            all_match = False

        print(f"  [{language}] {len(lang_files)}/{len(eng_files)} files – {status}")
        if missing:
            print(f"    Missing ({len(missing)}):")
            for m in sorted(missing)[:10]:
                print(f"      - {m}")
            if len(missing) > 10:
                print(f"      ... and {len(missing) - 10} more")
        if extra:
            print(f"    Extra ({len(extra)}):")
            for e in sorted(extra)[:5]:
                print(f"      + {e}")

    if all_match:
        print("\n  All languages match the English structure!")
    else:
        print("\n  Some languages still need work.")


# ── Main ──────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="Restructure and translate knowledge base")
    parser.add_argument("--root", type=Path, required=True, help="Repository root")
    parser.add_argument(
        "--languages", nargs="+", choices=sorted(LANGUAGES),
        help="Specific languages to process (default: all)",
    )
    parser.add_argument("--restructure", action="store_true", help="Phase 1: restructure directories")
    parser.add_argument("--translate", action="store_true", help="Phase 2: translate missing files")
    parser.add_argument("--verify", action="store_true", help="Phase 3: verify structure matches English")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be moved without moving")
    parser.add_argument("--limit", type=int, default=0, help="Limit files per language for translation")
    parser.add_argument("--delay", type=float, default=0.15, help="Delay between translation requests")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing translations")
    parser.add_argument("--workers", type=int, default=4, help="Parallel language workers (default: 4)")
    parser.add_argument("--file-workers", type=int, default=1, help="Parallel file workers per language (default: 1)")
    parser.add_argument("--all", action="store_true", help="Run all phases")
    args = parser.parse_args()

    languages = args.languages or list(LANGUAGES)

    if not args.restructure and not args.translate and not args.verify and not args.all:
        parser.print_help()
        return 1

    if args.all:
        args.restructure = True
        args.translate = True
        args.verify = True

    if args.restructure:
        restructure_all(args.root, languages, args.dry_run)

    if args.translate:
        translate_all(args.root, languages, args.limit, args.delay, args.overwrite, args.workers, args.file_workers)

    if args.verify:
        verify_structure(args.root, languages)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
