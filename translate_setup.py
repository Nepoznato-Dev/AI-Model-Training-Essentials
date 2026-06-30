#!/usr/bin/env python3
"""
Translation Script for Knowledge Base and Agent Modes

This script:
1. Creates english_skills folder with English translations of all non-English knowledge_base files
2. Translates all agent_modes files to all supported languages

Note: This script generates translation requests that can be processed by an AI assistant.
Since actual translation requires AI model calls, this script creates a structured workflow.
"""

import os
import json
from pathlib import Path
from typing import List, Tuple

# Configuration
WORKSPACE = Path("/workspace")
KNOWLEDGE_BASE = WORKSPACE / "knowledge_base"
AGENT_MODES = WORKSPACE / "agent_modes"
ENGLISH_SKILLS = WORKSPACE / "english_skills"

# Language mappings (folder name -> language name for translation prompts)
LANGUAGE_MAP = {
    "Arabic": "Arabic",
    "French": "French", 
    "German": "German",
    "Japanese": "Japanese",
    "Korean": "Korean",
    "Mandarin (Simplified Chinese)": "Simplified Chinese",
    "Mandarin (Traditional Chinese)": "Traditional Chinese",
    "Portuguese": "Portuguese",
    "Russian": "Russian",
    "Spanish": "Spanish",
    "Turkish": "Turkish",
}

def get_all_md_files(directory: Path) -> List[Path]:
    """Get all markdown files recursively."""
    return list(directory.rglob("*.md"))

def get_non_english_files() -> List[Tuple[Path, str]]:
    """Get all non-English markdown files with their source language."""
    non_english_files = []
    
    for lang_folder in KNOWLEDGE_BASE.iterdir():
        if lang_folder.is_dir() and lang_folder.name != "English":
            lang_name = LANGUAGE_MAP.get(lang_folder.name, lang_folder.name)
            for md_file in get_all_md_files(lang_folder):
                non_english_files.append((md_file, lang_name))
    
    return non_english_files

def get_agent_mode_files() -> List[Path]:
    """Get all agent mode markdown files."""
    return get_all_md_files(AGENT_MODES)

def create_translation_prompt(source_file: Path, source_lang: str, target_lang: str = "English") -> str:
    """Create a translation prompt for a single file."""
    return f"""
Translate the following content from {source_lang} to {target_lang}:

Source file: {source_file.relative_to(WORKSPACE)}

[FILE CONTENT TO BE READ AND TRANSLATED]

Preserve:
- Markdown structure (headers, lists, code blocks)
- Technical terms in English where appropriate
- File paths and code examples
- YAML frontmatter structure (translate only human-readable values)

Output path: {ENGLISH_SKILLS.relative_to(WORKSPACE)}/{source_file.relative_to(lang_folder) if 'lang_folder' in dir() else source_file.relative_to(KNOWLEDGE_BASE)}
""".strip()

def generate_batch_translation_plan():
    """Generate a comprehensive translation plan."""
    
    print("=" * 80)
    print("TRANSLATION TASK PLAN")
    print("=" * 80)
    
    # Part 1: Non-English to English (english_skills)
    print("\n## PART 1: Create english_skills with English translations\n")
    
    non_english_files = get_non_english_files()
    print(f"Found {len(non_english_files)} non-English markdown files to translate to English\n")
    
    # Group by source language
    by_language = {}
    for file_path, lang in non_english_files:
        if lang not in by_language:
            by_language[lang] = []
        by_language[lang].append(file_path)
    
    for lang, files in sorted(by_language.items()):
        print(f"  {lang}: {len(files)} files")
    
    # Part 2: Agent Modes to all languages
    print("\n## PART 2: Translate agent_modes to all languages\n")
    
    agent_files = get_agent_mode_files()
    print(f"Found {len(agent_files)} agent mode files\n")
    print(f"Target languages: {', '.join(LANGUAGE_MAP.values())}")
    print(f"Total translations needed: {len(agent_files) * len(LANGUAGE_MAP)}\n")
    
    # Show sample files
    print("Agent files to translate:")
    for f in agent_files:
        print(f"  - {f.name}")
    
    print("\n" + "=" * 80)
    print("SCRIPT GENERATION COMPLETE")
    print("=" * 80)
    
    return non_english_files, agent_files

def create_directory_structure():
    """Create the directory structure for english_skills."""
    ENGLISH_SKILLS.mkdir(parents=True, exist_ok=True)
    
    # Mirror the structure from knowledge_base (excluding English folder)
    template_dirs = [
        "01_technology_and_computing",
        "02_artificial_intelligence", 
        "03_data_science",
        "04_science",
        "05_business_and_finance",
        "06_humanities",
        "07_reference",
        "08_future",
        "10_cheat_sheets"
    ]
    
    for dir_name in template_dirs:
        (ENGLISH_SKILLS / dir_name).mkdir(parents=True, exist_ok=True)
    
    print(f"Created directory structure at {ENGLISH_SKILLS}")

if __name__ == "__main__":
    # Create directory structure
    create_directory_structure()
    
    # Generate translation plan
    non_english_files, agent_files = generate_batch_translation_plan()
    
    # Save manifest files
    manifest = {
        "non_english_files_count": len(non_english_files),
        "agent_files_count": len(agent_files),
        "languages": list(LANGUAGE_MAP.keys()),
        "non_english_files": [str(f.relative_to(WORKSPACE)) for f, _ in non_english_files],
        "agent_files": [str(f.relative_to(WORKSPACE)) for f in agent_files]
    }
    
    with open(WORKSPACE / "translation_manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\nManifest saved to: {WORKSPACE / 'translation_manifest.json'}")
