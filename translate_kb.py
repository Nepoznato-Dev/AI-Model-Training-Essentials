#!/usr/bin/env python3
"""
Translate knowledge base folder 02 from English to multiple languages.
- Batches translation requests (translates whole paragraphs at once)
- Preserves code blocks (``` fenced and `inline`) untranslated
- Preserves markdown structure
- Has retry logic with delays
- Uses googletrans library (more reliable than deep-translator)
"""

import os
import re
import time
from pathlib import Path
from googletrans import Translator

# Configuration
SOURCE_FOLDER = "/workspace/knowledge_base/English/02_artificial_intelligence"
BASE_KB_FOLDER = "/workspace/knowledge_base"

# Target languages with their language codes for googletrans
TARGET_LANGUAGES = {
    "Thai": "th",
    "Persian": "fa",
    "Polish": "pl",
    "Indonesian": "id",
    "Vietnamese": "vi",
    "Italian": "it",
}

# Retry configuration
MAX_RETRIES = 5
RETRY_DELAY = 1  # seconds

# Code block placeholder patterns
FENCED_CODE_PLACEHOLDER = "%%%FENCED_CODE_BLOCK_{idx}%%%"
INLINE_CODE_PLACEHOLDER = "%%%INLINE_CODE_{idx}%%%"


def extract_code_blocks(text):
    """Extract code blocks and replace with placeholders, return text and mapping."""
    fenced_codes = {}
    inline_codes = {}
    fenced_idx = 0
    inline_idx = 0
    
    # First, extract fenced code blocks (``` ... ```)
    def replace_fenced(match):
        nonlocal fenced_idx
        placeholder = FENCED_CODE_PLACEHOLDER.format(idx=fenced_idx)
        fenced_codes[placeholder] = match.group(0)
        fenced_idx += 1
        return placeholder
    
    text = re.sub(r'```[\s\S]*?```', replace_fenced, text)
    
    # Then extract inline code (` ... `) but not inside already replaced fenced blocks
    def replace_inline(match):
        nonlocal inline_idx
        placeholder = INLINE_CODE_PLACEHOLDER.format(idx=inline_idx)
        inline_codes[placeholder] = match.group(0)
        inline_idx += 1
        return placeholder
    
    text = re.sub(r'`[^`]+`', replace_inline, text)
    
    return text, fenced_codes, inline_codes


def restore_code_blocks(text, fenced_codes, inline_codes):
    """Restore code blocks from placeholders."""
    # Restore fenced code blocks first
    for placeholder, code in fenced_codes.items():
        text = text.replace(placeholder, code)
    
    # Restore inline code
    for placeholder, code in inline_codes.items():
        text = text.replace(placeholder, code)
    
    return text


def split_into_paragraphs(text):
    """Split text into paragraphs for batched translation."""
    # Split by double newlines (paragraph breaks)
    paragraphs = re.split(r'\n\n+', text)
    return [p.strip() for p in paragraphs if p.strip()]


def translate_with_retry(translator, text, target_lang, max_retries=MAX_RETRIES):
    """Translate text with retry logic."""
    if not text.strip():
        return text
    
    for attempt in range(max_retries):
        try:
            result = translator.translate(text, dest=target_lang)
            if result and result.text:
                return result.text
            else:
                print(f"  Empty result on attempt {attempt + 1}")
        except Exception as e:
            print(f"  Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(RETRY_DELAY * (attempt + 1))  # Exponential backoff
    
    print(f"  WARNING: Translation failed after {max_retries} attempts, returning original")
    return text  # Return original if all attempts fail


def translate_file(source_path, dest_path, lang_name, lang_code):
    """Translate a single markdown file, preserving code blocks."""
    print(f"Translating: {source_path} -> {dest_path}")
    
    # Read source file
    with open(source_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    if not original_content.strip():
        print(f"  WARNING: Source file is empty!")
        return False
    
    # Extract code blocks
    processed_text, fenced_codes, inline_codes = extract_code_blocks(original_content)
    
    print(f"  Extracted {len(fenced_codes)} fenced code blocks and {len(inline_codes)} inline code blocks")
    
    # Split into paragraphs for batched translation
    paragraphs = split_into_paragraphs(processed_text)
    print(f"  Split into {len(paragraphs)} paragraphs for translation")
    
    # Create translator
    translator = Translator()
    
    # Translate each paragraph (batch within paragraph)
    translated_paragraphs = []
    for i, para in enumerate(paragraphs):
        if i % 10 == 0:
            print(f"  Translating paragraph {i+1}/{len(paragraphs)}...")
        
        translated = translate_with_retry(translator, para, lang_code)
        translated_paragraphs.append(translated)
    
    # Rejoin paragraphs
    translated_text = '\n\n'.join(translated_paragraphs)
    
    # Restore code blocks
    final_text = restore_code_blocks(translated_text, fenced_codes, inline_codes)
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write translated file
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(final_text)
    
    print(f"  Written to {dest_path}")
    return True


def verify_translation(source_path, dest_path, lang_name):
    """Verify the translated file."""
    errors = []
    
    # Check file exists
    if not os.path.exists(dest_path):
        return False, ["File does not exist"]
    
    # Check file is not empty
    with open(dest_path, 'r', encoding='utf-8') as f:
        translated_content = f.read()
    
    if not translated_content.strip():
        errors.append("File is empty")
        return False, errors
    
    with open(source_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Check it's not just the untranslated text (simple heuristic)
    if translated_content.strip() == original_content.strip():
        errors.append("File appears to be untranslated (identical to source)")
        return False, errors
    
    # Check code blocks are preserved (count should match)
    orig_fenced = len(re.findall(r'```[\s\S]*?```', original_content))
    trans_fenced = len(re.findall(r'```[\s\S]*?```', translated_content))
    if orig_fenced != trans_fenced:
        errors.append(f"Fenced code block count mismatch: original={orig_fenced}, translated={trans_fenced}")
    
    orig_inline = len(re.findall(r'`[^`]+`', original_content))
    trans_inline = len(re.findall(r'`[^`]+`', translated_content))
    if orig_inline != trans_inline:
        errors.append(f"Inline code count mismatch: original={orig_inline}, translated={trans_inline}")
    
    # Check markdown headers are preserved (at least some # should exist if original had them)
    orig_headers = len(re.findall(r'^#+\s', original_content, re.MULTILINE))
    trans_headers = len(re.findall(r'^#+\s', translated_content, re.MULTILINE))
    if orig_headers > 0 and trans_headers == 0:
        errors.append("Markdown headers appear to be lost")
    
    if errors:
        return False, errors
    
    return True, ["OK"]


def main():
    print("=" * 60)
    print("Knowledge Base Translation Script - Folder 02")
    print("=" * 60)
    
    # Confirm source files are readable
    print("\n[1] Checking source files...")
    if not os.path.isdir(SOURCE_FOLDER):
        print(f"ERROR: Source folder does not exist: {SOURCE_FOLDER}")
        return 1
    
    source_files = list(Path(SOURCE_FOLDER).glob("*.md"))
    print(f"Found {len(source_files)} markdown files in {SOURCE_FOLDER}")
    
    for sf in source_files:
        if not os.access(sf, os.R_OK):
            print(f"ERROR: Cannot read source file: {sf}")
            return 1
    print("All source files are readable.")
    
    # Print file counts per target folder
    print("\n[2] Target folder status:")
    for lang_name in TARGET_LANGUAGES:
        target_folder = os.path.join(BASE_KB_FOLDER, lang_name, "02_artificial_intelligence")
        existing_files = list(Path(target_folder).glob("*.md")) if os.path.isdir(target_folder) else []
        print(f"  {lang_name}: {len(existing_files)} existing files in 02 folder")
    
    # Process each language
    results = {}
    for lang_name, lang_code in TARGET_LANGUAGES.items():
        print(f"\n{'='*60}")
        print(f"[3] Translating to {lang_name} ({lang_code})")
        print(f"{'='*60}")
        
        target_folder = os.path.join(BASE_KB_FOLDER, lang_name, "02_artificial_intelligence")
        os.makedirs(target_folder, exist_ok=True)
        
        lang_results = {}
        for source_file in source_files:
            filename = source_file.name
            dest_file = os.path.join(target_folder, filename)
            
            success = translate_file(str(source_file), dest_file, lang_name, lang_code)
            
            if success:
                verified, messages = verify_translation(str(source_file), dest_file, lang_name)
                if verified:
                    lang_results[filename] = "PASS"
                    print(f"  ✓ {filename}: PASS")
                else:
                    lang_results[filename] = f"FAIL: {', '.join(messages)}"
                    print(f"  ✗ {filename}: FAIL - {', '.join(messages)}")
            else:
                lang_results[filename] = "FAIL: Translation failed"
                print(f"  ✗ {filename}: FAIL - Translation failed")
        
        results[lang_name] = lang_results
    
    # Summary report
    print(f"\n{'='*60}")
    print("[4] VERIFICATION SUMMARY")
    print(f"{'='*60}")
    
    all_passed = True
    for lang_name, lang_results in results.items():
        print(f"\n{lang_name}:")
        for filename, status in lang_results.items():
            if status == "PASS":
                print(f"  ✓ {filename}: {status}")
            else:
                print(f"  ✗ {filename}: {status}")
                all_passed = False
    
    print(f"\n{'='*60}")
    if all_passed:
        print("ALL FILES PASSED VERIFICATION")
    else:
        print("SOME FILES FAILED VERIFICATION - REVIEW ABOVE")
    print(f"{'='*60}")
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
