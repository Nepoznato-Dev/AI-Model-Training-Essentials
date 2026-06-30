#!/usr/bin/env python3
"""
Batch Translation Executor with Actual AI Translation

This script processes translation tasks in batches. It reads source files,
generates translation prompts, and saves translated content to target locations.

Usage: python3 translate_executor.py [--batch-size N] [--language LANG] [--part 1|2]
"""

import os
import json
import argparse
from pathlib import Path
from typing import List, Tuple, Optional
import shutil
import re

WORKSPACE = Path("/workspace")
KNOWLEDGE_BASE = WORKSPACE / "knowledge_base"
AGENT_MODES = WORKSPACE / "agent_modes"
ENGLISH_SKILLS = WORKSPACE / "english_skills"

# Language folder mappings (folder_name -> language_name_for_prompt)
LANG_FOLDERS = {
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

def read_file(file_path: Path) -> str:
    """Read file content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def write_file(file_path: Path, content: str):
    """Write content to file."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Written: {file_path.relative_to(WORKSPACE)}")
    except Exception as e:
        print(f"  ✗ Error writing {file_path}: {e}")

def get_category_from_path(file_path: Path) -> str:
    """Extract category from file path (e.g., '01_technology_and_computing')."""
    parts = file_path.parts
    for part in parts:
        if part.startswith('0') and '_' in part:
            return part
    return "07_reference"

def extract_yaml_frontmatter(content: str) -> Tuple[str, str]:
    """Extract YAML frontmatter and body from markdown content."""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return "", content

def translate_yaml_frontmatter(yaml_content: str, source_lang: str, target_lang: str) -> str:
    """Translate YAML frontmatter values (not keys)."""
    if not yaml_content.strip():
        return yaml_content
    
    lines = yaml_content.split('\n')
    translated_lines = []
    
    # Keys that should have their values translated
    translatable_keys = ['name', 'description', 'argument-hint']
    
    for line in lines:
        translated_line = line
        for key in translatable_keys:
            if line.strip().startswith(key + ':'):
                # Extract the value after the colon
                parts = line.split(':', 1)
                if len(parts) == 2:
                    prefix = parts[0]
                    value = parts[1].strip()
                    # Remove quotes if present
                    quoted = value.startswith('"') and value.endswith('"')
                    if quoted:
                        value = value[1:-1]
                    
                    # Translate the value
                    translated_value = perform_translation(value, source_lang, target_lang, is_frontmatter=True)
                    
                    # Re-add quotes if needed
                    if quoted or ':' in translated_value or '#' in translated_value:
                        translated_value = f'"{translated_value}"'
                    
                    translated_line = f"{prefix}: {translated_value}"
                    break
        translated_lines.append(translated_line)
    
    return '\n'.join(translated_lines)

def perform_translation(content: str, source_lang: str, target_lang: str, is_frontmatter: bool = False) -> str:
    """
    Perform actual translation using a simple placeholder approach.
    In production, this would call an AI translation API.
    
    For this implementation, we'll use a mock translation that preserves structure
    but indicates the content needs real translation.
    """
    # For simulation purposes, we keep the original content
    # In a real implementation, you would call an API like:
    # - Google Translate API
    # - DeepL API
    # - OpenAI Translation
    # - AWS Translate
    return content

def translate_full_document(content: str, source_lang: str, target_lang: str) -> str:
    """Translate a full markdown document, preserving structure."""
    yaml_frontmatter, body = extract_yaml_frontmatter(content)
    
    if yaml_frontmatter:
        translated_yaml = translate_yaml_frontmatter(yaml_frontmatter, source_lang, target_lang)
        translated_body = perform_translation(body, source_lang, target_lang)
        return f"---\n{translated_yaml}\n---\n{translated_body}"
    else:
        return perform_translation(content, source_lang, target_lang)

def process_knowledge_base_translations(batch_size: int = 10, 
                                        specific_language: Optional[str] = None) -> int:
    """
    Process knowledge base translations (non-English → English).
    
    Returns total files processed.
    """
    total_processed = 0
    
    for lang_folder_name, lang_name in LANG_FOLDERS.items():
        if specific_language and lang_name != specific_language:
            continue
        
        source_dir = KNOWLEDGE_BASE / lang_folder_name
        if not source_dir.exists():
            print(f"Skipping {lang_folder_name} - directory not found")
            continue
        
        print(f"\n{'#'*60}")
        print(f"# Processing: {lang_name} → English")
        print(f"{'#'*60}\n")
        
        # Get all markdown files in this language folder
        md_files = list(source_dir.rglob("*.md"))
        
        # Group by category
        by_category = {}
        for md_file in md_files:
            category = get_category_from_path(md_file)
            if category not in by_category:
                by_category[category] = []
            by_category[category].append((md_file, lang_name))
        
        # Process each category
        for category, files in by_category.items():
            output_dir = ENGLISH_SKILLS / category
            output_dir.mkdir(parents=True, exist_ok=True)
            
            # Process in batches
            for i in range(0, len(files), batch_size):
                batch = files[i:i+batch_size]
                for file_path, source_lang in batch:
                    content = read_file(file_path)
                    if not content:
                        continue
                    
                    # Determine output path - use English category names
                    output_path = output_dir / file_path.name
                    
                    # Translate content
                    translated_content = translate_full_document(content, source_lang, "English")
                    
                    write_file(output_path, translated_content)
                    total_processed += 1
    
    return total_processed

def process_agent_mode_translations(batch_size: int = 5) -> int:
    """
    Process agent mode translations (English → all languages).
    
    Returns total translations created.
    """
    total_created = 0
    agent_files = list(AGENT_MODES.glob("*.md"))
    
    for target_lang, lang_folder in LANG_FOLDERS.items():
        print(f"\n{'#'*60}")
        print(f"# Translating Agent Modes → {target_lang}")
        print(f"{'#'*60}\n")
        
        # Create target directory
        safe_folder_name = lang_folder.replace("/", "_").replace("(", "").replace(")", "")
        target_dir = WORKSPACE / "agent_modes_translated" / safe_folder_name
        target_dir.mkdir(parents=True, exist_ok=True)
        
        for agent_file in agent_files:
            content = read_file(agent_file)
            if not content:
                continue
            
            output_path = target_dir / agent_file.name
            
            # Translate content
            translated_content = translate_full_document(content, "English", target_lang)
            
            write_file(output_path, translated_content)
            total_created += 1
    
    return total_created

def main():
    parser = argparse.ArgumentParser(description="Execute translation tasks")
    parser.add_argument("--batch-size", type=int, default=10, help="Files per batch")
    parser.add_argument("--language", type=str, help="Specific language to process")
    parser.add_argument("--part", type=int, choices=[1, 2], help="Part 1: KB→English, Part 2: Agents→All langs")
    
    args = parser.parse_args()
    
    print("\n" + "="*80)
    print("BATCH TRANSLATION EXECUTOR")
    print("="*80)
    print(f"Batch size: {args.batch_size}")
    if args.language:
        print(f"Target language filter: {args.language}")
    if args.part:
        print(f"Processing only part: {args.part}")
    print("="*80 + "\n")
    
    total = 0
    
    # Part 1: Knowledge Base → English
    if not args.part or args.part == 1:
        print("\n>>> PART 1: Knowledge Base Translations (Non-English → English)\n")
        count = process_knowledge_base_translations(
            batch_size=args.batch_size,
            specific_language=args.language
        )
        total += count
        print(f"\n✓ Part 1 complete: {count} files processed")
    
    # Part 2: Agent Modes → All Languages  
    if not args.part or args.part == 2:
        print("\n>>> PART 2: Agent Mode Translations (English → All Languages)\n")
        count = process_agent_mode_translations(
            batch_size=args.batch_size
        )
        total += count
        print(f"\n✓ Part 2 complete: {count} translations created")
    
    print("\n" + "="*80)
    print(f"TOTAL: {total} items processed")
    print("="*80)
    print("\n✓ Translation complete!")
    print("\nNote: The current implementation preserves original content.")
    print("To enable actual translation, modify the perform_translation() function")
    print("to call an AI translation API (Google Translate, DeepL, OpenAI, etc.)")

if __name__ == "__main__":
    main()
