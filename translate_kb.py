#!/usr/bin/env python3
"""
Knowledge Base Translator Script
Translates markdown files from English to multiple target languages while preserving:
- Code blocks (``` fenced and `inline`)
- Markdown structure (headers, lists, etc.)

Usage: python3 translate_kb.py
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

# Folders to translate (starting with 04)
FOLDERS_TO_TRANSLATE = ["04_science"]

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
BATCH_SIZE = 5000  # characters per batch for translation

# Placeholder markers for code blocks
CODE_BLOCK_PLACEHOLDER = "<<<CODE_BLOCK_{idx}>>>"
INLINE_CODE_PLACEHOLDER = "<<<INLINE_CODE_{idx}>>>"


def extract_code_blocks(text):
    """Extract code blocks and inline code, replacing with placeholders."""
    code_blocks = {}
    inline_codes = {}
    
    # Extract fenced code blocks first (``` ... ```)
    # Use a more robust pattern that handles any characters including newlines
    idx = 0
    def replace_code_block(match):
        nonlocal idx
        placeholder = CODE_BLOCK_PLACEHOLDER.format(idx=idx)
        code_blocks[placeholder] = match.group(0)
        idx += 1
        return placeholder
    
    # Match ``` followed by optional language identifier, newline, content, then closing ```
    # The (?s) flag makes . match newlines
    text = re.sub(r'```([^\n]*)\n(.*?)```', replace_code_block, text, flags=re.DOTALL)
    
    # Extract inline code (` ... `) - must be careful not to match inside already-extracted code
    # Only match single backticks that are NOT part of triple backticks
    idx = 0
    def replace_inline_code(match):
        nonlocal idx
        # Check if this is actually inside a code block placeholder (shouldn't happen, but safety check)
        matched = match.group(0)
        # Skip if it looks like it could be part of markdown formatting artifacts
        placeholder = INLINE_CODE_PLACEHOLDER.format(idx=idx)
        inline_codes[placeholder] = matched
        idx += 1
        return placeholder
    
    # More careful inline code matching - avoid matching empty or whitespace-only
    text = re.sub(r'`([^`\s][^`]*[^`\s]|[^`\s])`', replace_inline_code, text)
    
    return text, code_blocks, inline_codes


def restore_code_blocks(text, code_blocks, inline_codes):
    """Restore code blocks and inline code from placeholders."""
    # Restore fenced code blocks
    for placeholder, original in code_blocks.items():
        text = text.replace(placeholder, original)
    
    # Restore inline code
    for placeholder, original in inline_codes.items():
        text = text.replace(placeholder, original)
    
    return text


def split_into_batches(text, max_size=BATCH_SIZE):
    """Split text into batches for translation, trying to break at paragraph boundaries."""
    if len(text) <= max_size:
        return [text]
    
    batches = []
    current_batch = ""
    
    # Split by paragraphs (double newlines)
    paragraphs = re.split(r'(\n\n+)', text)
    
    for para in paragraphs:
        if len(current_batch) + len(para) <= max_size:
            current_batch += para
        else:
            if current_batch:
                batches.append(current_batch)
            # If single paragraph is too long, split by sentences
            if len(para) > max_size:
                sentences = re.split(r'([.!?]+\s+|\n)', para)
                current_batch = ""
                for sent in sentences:
                    if len(current_batch) + len(sent) <= max_size:
                        current_batch += sent
                    else:
                        if current_batch:
                            batches.append(current_batch)
                        current_batch = sent
            else:
                current_batch = para
    
    if current_batch:
        batches.append(current_batch)
    
    return batches


def translate_batch(translator, text, max_retries=MAX_RETRIES):
    """Translate a batch of text with retry logic."""
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
    # Extract code blocks
    text_no_code, code_blocks, inline_codes = extract_code_blocks(text)
    
    # Split into batches
    batches = split_into_batches(text_no_code)
    
    # Create translator
    translator = GoogleTranslator(source='en', target=target_lang_code)
    
    # Translate each batch
    translated_batches = []
    for i, batch in enumerate(batches):
        print(f"    Translating batch {i+1}/{len(batches)}...")
        translated = translate_batch(translator, batch)
        if translated:
            translated_batches.append(translated)
        else:
            print(f"    Warning: Failed to translate batch {i+1}, keeping original")
            translated_batches.append(batch)
    
    # Join translated batches
    translated_text = ''.join(translated_batches)
    
    # Restore code blocks
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
    print("Knowledge Base Translation Script")
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
