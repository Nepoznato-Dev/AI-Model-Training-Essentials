#!/usr/bin/env python3
"""
Knowledge Base Translator Script v2
Translates markdown files from English to multiple target languages while preserving:
- Code blocks (``` fenced and `inline`) - completely untranslated
- Markdown structure (headers, lists, etc.)

Usage: python3 translate_kb_v2.py
"""

import os
import re
import sys
import time
import random
from pathlib import Path
from deep_translator import GoogleTranslator

# Configuration
SOURCE_DIR = Path("/workspace/knowledge_base/English")
OUTPUT_BASE = Path("/workspace")
TARGET_LANGUAGES = {
    "Thai": "th",
    "Persian": "fa",
    "Polish": "pl",
    "Indonesian": "id",
    "Vietnamese": "vi",
    "Italian": "it",
}

# Folders to translate (starting with 01)
FOLDERS_TO_TRANSLATE = ["01_technology_and_computing"]

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
BATCH_SIZE = 4000  # characters per batch for translation (reduced for safety)

# Placeholder markers for code blocks - use unique markers unlikely to appear in text
CODE_BLOCK_MARKER_START = "\x00CODEBLOCK_"
CODE_BLOCK_MARKER_END = "_END\x00"
INLINE_CODE_MARKER_START = "\x00INLINECODE_"
INLINE_CODE_MARKER_END = "_END\x00"


def extract_code_blocks(text):
    """Extract code blocks and inline code, replacing with null-byte placeholders."""
    code_blocks = []
    inline_codes = []

    # Extract fenced code blocks first (``` ... ```)
    def replace_code_block(match):
        code_blocks.append(match.group(0))
        return f"{CODE_BLOCK_MARKER_START}{len(code_blocks)-1}{CODE_BLOCK_MARKER_END}"

    # Match ``` followed by optional language identifier, newline, content, then closing ```
    text = re.sub(r'```([^\n]*)\n(.*?)```', replace_code_block, text, flags=re.DOTALL)

    # Extract inline code (` ... `)
    def replace_inline_code(match):
        inline_codes.append(match.group(0))
        return f"{INLINE_CODE_MARKER_START}{len(inline_codes)-1}{INLINE_CODE_MARKER_END}"

    # Match inline code - single backticks with non-empty content
    text = re.sub(r'`([^`]+)`', replace_inline_code, text)

    return text, code_blocks, inline_codes


def restore_code_blocks(text, code_blocks, inline_codes):
    """Restore code blocks and inline code from placeholders."""
    # Restore fenced code blocks
    for i, original in enumerate(code_blocks):
        placeholder = f"{CODE_BLOCK_MARKER_START}{i}{CODE_BLOCK_MARKER_END}"
        text = text.replace(placeholder, original)

    # Restore inline code
    for i, original in enumerate(inline_codes):
        placeholder = f"{INLINE_CODE_MARKER_START}{i}{INLINE_CODE_MARKER_END}"
        text = text.replace(placeholder, original)

    return text


def split_into_paragraphs(text):
    """Split text into paragraphs for batch translation."""
    # Split by double newlines (paragraph boundaries)
    paragraphs = re.split(r'(\n\n+)', text)
    return paragraphs


def translate_batch(translator, text, max_retries=MAX_RETRIES):
    """Translate a batch of text with retry logic."""
    if not text.strip():
        return text
    
    for attempt in range(max_retries):
        try:
            result = translator.translate(text)
            if result and result.strip():
                return result
            else:
                print(f"  Warning: Empty translation result, retrying... (attempt {attempt + 1}/{max_retries})")
        except Exception as e:
            print(f"  Error during translation (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                delay = RETRY_DELAY * (2 ** attempt) + random.uniform(0.5, 1.5)
                print(f"  Retrying in {delay:.1f} seconds...")
                time.sleep(delay)
            else:
                raise
    return None


def translate_markdown_content(text, target_lang_code):
    """Translate markdown content while preserving code blocks."""
    # Extract code blocks FIRST (before any processing)
    text_no_code, code_blocks, inline_codes = extract_code_blocks(text)

    # Create translator
    translator = GoogleTranslator(source='en', target=target_lang_code)

    # Split remaining text into paragraphs
    paragraphs = split_into_paragraphs(text_no_code)
    
    # Translate each paragraph separately
    translated_paragraphs = []
    for i, para in enumerate(paragraphs):
        if para.strip() and not para.isspace():
            # This is actual content, translate it
            translated = translate_batch(translator, para)
            if translated:
                translated_paragraphs.append(translated)
            else:
                print(f"    Warning: Failed to translate paragraph {i}, keeping original")
                translated_paragraphs.append(para)
        else:
            # This is just whitespace/newlines, keep as-is
            translated_paragraphs.append(para)

    # Join translated paragraphs
    translated_text = ''.join(translated_paragraphs)

    # Restore code blocks EXACTLY as they were
    translated_text = restore_code_blocks(translated_text, code_blocks, inline_codes)

    return translated_text


def process_file(source_path, output_path, target_lang_name, target_lang_code):
    """Process a single file for translation."""
    print(f"  Processing: {source_path.name} -> {target_lang_name}")

    # Read source file
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ERROR: Could not read {source_path}: {e}")
        return False

    if not content.strip():
        print(f"  WARNING: Source file is empty: {source_path}")
        # Create empty output file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("")
        return True

    # Translate content
    try:
        translated_content = translate_markdown_content(content, target_lang_code)
    except Exception as e:
        print(f"  ERROR: Translation failed for {source_path}: {e}")
        return False

    # Write output file
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        print(f"  SUCCESS: Written to {output_path}")
        return True
    except Exception as e:
        print(f"  ERROR: Could not write {output_path}: {e}")
        return False


def verify_output_file(output_path, source_path, target_lang_name):
    """Verify that an output file exists and is valid."""
    errors = []

    # Check file exists
    if not output_path.exists():
        errors.append("File does not exist")
        return False, errors

    # Check file is not empty
    try:
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        errors.append(f"Could not read file: {e}")
        return False, errors

    if not content.strip():
        errors.append("File is empty")
        return False, errors

    # Check it's not just the untranslated English text
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            source_content = f.read()
    except:
        source_content = ""

    if content == source_content:
        errors.append("File appears to be untranslated (identical to source)")
        return False, errors

    # Basic check: if target language uses non-Latin script, verify some chars changed
    # This is a simple heuristic
    if target_lang_name in ["Thai", "Persian"]:
        # These should have non-ASCII characters
        ascii_ratio = sum(1 for c in content if ord(c) < 128) / len(content) if content else 1
        if ascii_ratio > 0.9:
            errors.append(f"Suspicious: Too many ASCII characters ({ascii_ratio:.2%}) for {target_lang_name}")
            return False, errors

    # Check code blocks are preserved (basic check)
    source_code_blocks = len(re.findall(r'```', source_content))
    output_code_blocks = len(re.findall(r'```', content))
    if source_code_blocks != output_code_blocks:
        errors.append(f"Code block count mismatch: source={source_code_blocks}, output={output_code_blocks}")
        return False, errors

    # Check inline code preservation (sample check)
    source_inline = len(re.findall(r'`[^`]+`', source_content))
    output_inline = len(re.findall(r'`[^`]+`', content))
    if source_inline != output_inline:
        errors.append(f"Inline code count mismatch: source={source_inline}, output={output_inline}")
        return False, errors

    return True, errors


def main():
    print("=" * 60)
    print("Knowledge Base Translation Script v2")
    print("=" * 60)

    # Verify source directory exists
    if not SOURCE_DIR.exists():
        print(f"FATAL: Source directory does not exist: {SOURCE_DIR}")
        sys.exit(1)

    # Count files per folder
    print("\nSource file counts:")
    total_files = 0
    for folder in FOLDERS_TO_TRANSLATE:
        folder_path = SOURCE_DIR / folder
        if folder_path.exists():
            files = list(folder_path.glob("*.md"))
            print(f"  {folder}: {len(files)} files")
            total_files += len(files)
        else:
            print(f"  {folder}: NOT FOUND")

    if total_files == 0:
        print("FATAL: No source files found!")
        sys.exit(1)

    print(f"\nTotal source files: {total_files}")
    print(f"Target languages: {list(TARGET_LANGUAGES.keys())}")

    # Process each folder
    results = {}
    for folder in FOLDERS_TO_TRANSLATE:
        folder_path = SOURCE_DIR / folder
        if not folder_path.exists():
            print(f"\nSkipping missing folder: {folder}")
            continue

        print(f"\n{'='*60}")
        print(f"Processing folder: {folder}")
        print(f"{'='*60}")

        source_files = list(folder_path.glob("*.md"))

        for lang_name, lang_code in TARGET_LANGUAGES.items():
            print(f"\n--- Translating to {lang_name} ---")

            # Create output directory
            output_folder = OUTPUT_BASE / lang_name / folder
            output_folder.mkdir(parents=True, exist_ok=True)

            results.setdefault(lang_name, {}).setdefault(folder, {})

            for source_file in source_files:
                output_file = output_folder / source_file.name
                success = process_file(source_file, output_file, lang_name, lang_code)
                results[lang_name][folder][source_file.name] = "PASS" if success else "FAIL"

    # Verification phase
    print("\n" + "=" * 60)
    print("VERIFICATION PHASE")
    print("=" * 60)

    verification_results = {}
    all_passed = True

    for lang_name, lang_code in TARGET_LANGUAGES.items():
        print(f"\n--- Verifying {lang_name} ---")
        verification_results[lang_name] = {}

        for folder in FOLDERS_TO_TRANSLATE:
            output_folder = OUTPUT_BASE / lang_name / folder
            source_folder = SOURCE_DIR / folder

            if not output_folder.exists():
                print(f"  Folder missing: {output_folder}")
                verification_results[lang_name][folder] = {"ERROR": "Folder not created"}
                all_passed = False
                continue

            verification_results[lang_name][folder] = {}

            for source_file in source_folder.glob("*.md"):
                output_file = output_folder / source_file.name
                passed, errors = verify_output_file(output_file, source_file, lang_name)

                status = "PASS" if passed else "FAIL"
                verification_results[lang_name][folder][source_file.name] = status

                if not passed:
                    all_passed = False
                    print(f"  {source_file.name}: {status}")
                    for err in errors:
                        print(f"    - {err}")
                else:
                    print(f"  {source_file.name}: {status}")

    # Summary report
    print("\n" + "=" * 60)
    print("SUMMARY REPORT")
    print("=" * 60)

    for lang_name in TARGET_LANGUAGES.keys():
        print(f"\n{lang_name}:")
        for folder in FOLDERS_TO_TRANSLATE:
            if folder in verification_results.get(lang_name, {}):
                print(f"  {folder}:")
                for filename, status in verification_results[lang_name][folder].items():
                    print(f"    {filename}: {status}")

    if all_passed:
        print("\n✓ All files translated and verified successfully!")
    else:
        print("\n✗ Some files failed verification. Review the errors above.")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
