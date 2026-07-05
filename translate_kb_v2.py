#!/usr/bin/env python3
"""
Knowledge Base Translator Script v2
Fixed: Preserve code block language identifiers untranslated
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

FOLDERS_TO_TRANSLATE = ["01_technology_and_computing"]

MAX_RETRIES = 3
RETRY_DELAY = 2
BATCH_SIZE = 5000

CODE_BLOCK_PLACEHOLDER = "<<<CODE_BLOCK_{idx}>>>"
INLINE_CODE_PLACEHOLDER = "<<<INLINE_CODE_{idx}>>>"


def extract_code_blocks(text):
    """Extract code blocks preserving exact content including language tag."""
    code_blocks = {}
    inline_codes = {}
    
    idx = 0
    def replace_code_block(match):
        nonlocal idx
        placeholder = CODE_BLOCK_PLACEHOLDER.format(idx=idx)
        # Store the ENTIRE code block including opening/closing ``` and lang tag
        code_blocks[placeholder] = match.group(0)
        idx += 1
        return placeholder
    
    # Match ``` + optional lang + newline + content + closing ```
    text = re.sub(r'```([^\n]*)\n(.*?)```', replace_code_block, text, flags=re.DOTALL)
    
    # Extract inline code
    idx = 0
    def replace_inline_code(match):
        nonlocal idx
        placeholder = INLINE_CODE_PLACEHOLDER.format(idx=idx)
        inline_codes[placeholder] = match.group(0)
        idx += 1
        return placeholder
    
    text = re.sub(r'`([^`\s][^`]*[^`\s]|[^`\s])`', replace_inline_code, text)
    
    return text, code_blocks, inline_codes


def restore_code_blocks(text, code_blocks, inline_codes):
    """Restore code blocks exactly as they were."""
    for placeholder, original in code_blocks.items():
        text = text.replace(placeholder, original)
    for placeholder, original in inline_codes.items():
        text = text.replace(placeholder, original)
    return text


def split_into_batches(text, max_size=BATCH_SIZE):
    if len(text) <= max_size:
        return [text]
    
    batches = []
    current_batch = ""
    paragraphs = re.split(r'(\n\n+)', text)
    
    for para in paragraphs:
        if len(current_batch) + len(para) <= max_size:
            current_batch += para
        else:
            if current_batch:
                batches.append(current_batch)
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
    for attempt in range(max_retries):
        try:
            result = translator.translate(text)
            if result and result.strip():
                return result
            else:
                print(f"  Warning: Empty translation, retrying... ({attempt + 1}/{max_retries})")
        except Exception as e:
            print(f"  Error ({attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                delay = RETRY_DELAY * (2 ** attempt) + random.uniform(0.5, 1.5)
                print(f"  Retrying in {delay:.1f}s...")
                time.sleep(delay)
            else:
                raise
    return None


def translate_markdown_content(text, target_lang_code):
    text_no_code, code_blocks, inline_codes = extract_code_blocks(text)
    batches = split_into_batches(text_no_code)
    translator = GoogleTranslator(source='en', target=target_lang_code)
    
    translated_batches = []
    for i, batch in enumerate(batches):
        print(f"    Batch {i+1}/{len(batches)}...")
        translated = translate_batch(translator, batch)
        if translated:
            translated_batches.append(translated)
        else:
            print(f"    Warning: Keeping original batch {i+1}")
            translated_batches.append(batch)
    
    translated_text = ''.join(translated_batches)
    translated_text = restore_code_blocks(translated_text, code_blocks, inline_codes)
    
    return translated_text


def process_file(source_path, output_path, target_lang_name, target_lang_code):
    print(f"  {source_path.name} -> {target_lang_name}")
    
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ERROR reading {source_path}: {e}")
        return False
    
    if not content.strip():
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("")
        return True
    
    try:
        translated_content = translate_markdown_content(content, target_lang_code)
    except Exception as e:
        print(f"  ERROR translating {source_path}: {e}")
        return False
    
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        print(f"  OK: {output_path}")
        return True
    except Exception as e:
        print(f"  ERROR writing {output_path}: {e}")
        return False


def verify_output_file(output_path, source_path, target_lang_name):
    errors = []
    
    if not output_path.exists():
        errors.append("File does not exist")
        return False, errors
    
    try:
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        errors.append(f"Could not read: {e}")
        return False, errors
    
    if not content.strip():
        errors.append("File is empty")
        return False, errors
    
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            source_content = f.read()
    except:
        source_content = ""
    
    if content == source_content:
        errors.append("Untranslated (identical to source)")
        return False, errors
    
    if target_lang_name in ["Thai", "Persian"]:
        ascii_ratio = sum(1 for c in content if ord(c) < 128) / len(content) if content else 1
        if ascii_ratio > 0.9:
            errors.append(f"Too many ASCII chars ({ascii_ratio:.2%})")
            return False, errors
    
    source_code_blocks = len(re.findall(r'```', source_content))
    output_code_blocks = len(re.findall(r'```', content))
    if source_code_blocks != output_code_blocks:
        errors.append(f"Code block mismatch: src={source_code_blocks}, out={output_code_blocks}")
        return False, errors
    
    source_inline = len(re.findall(r'`[^`]+`', source_content))
    output_inline = len(re.findall(r'`[^`]+`', content))
    if source_inline != output_inline:
        errors.append(f"Inline code mismatch: src={source_inline}, out={output_inline}")
        return False, errors
    
    return True, errors


def main():
    print("=" * 60)
    print("KB Translator v2")
    print("=" * 60)
    
    if not SOURCE_DIR.exists():
        print(f"FATAL: {SOURCE_DIR} not found")
        sys.exit(1)
    
    print("\nSource files:")
    total_files = 0
    for folder in FOLDERS_TO_TRANSLATE:
        folder_path = SOURCE_DIR / folder
        if folder_path.exists():
            files = list(folder_path.glob("*.md"))
            print(f"  {folder}: {len(files)}")
            total_files += len(files)
        else:
            print(f"  {folder}: NOT FOUND")
    
    if total_files == 0:
        print("FATAL: No files!")
        sys.exit(1)
    
    print(f"\nTotal: {total_files} files")
    print(f"Languages: {list(TARGET_LANGUAGES.keys())}")
    
    results = {}
    for folder in FOLDERS_TO_TRANSLATE:
        folder_path = SOURCE_DIR / folder
        if not folder_path.exists():
            continue
        
        print(f"\n{'='*60}\n{folder}\n{'='*60}")
        source_files = list(folder_path.glob("*.md"))
        
        for lang_name, lang_code in TARGET_LANGUAGES.items():
            print(f"\n--- {lang_name} ---")
            output_folder = OUTPUT_BASE / lang_name / folder
            output_folder.mkdir(parents=True, exist_ok=True)
            results.setdefault(lang_name, {}).setdefault(folder, {})
            
            for source_file in source_files:
                output_file = output_folder / source_file.name
                success = process_file(source_file, output_file, lang_name, lang_code)
                results[lang_name][folder][source_file.name] = "PASS" if success else "FAIL"
    
    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)
    
    verification_results = {}
    all_passed = True
    
    for lang_name, lang_code in TARGET_LANGUAGES.items():
        print(f"\n--- {lang_name} ---")
        verification_results[lang_name] = {}
        
        for folder in FOLDERS_TO_TRANSLATE:
            output_folder = OUTPUT_BASE / lang_name / folder
            source_folder = SOURCE_DIR / folder
            
            if not output_folder.exists():
                print(f"  Folder missing: {output_folder}")
                verification_results[lang_name][folder] = {"ERROR": "Not created"}
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
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    for lang_name in TARGET_LANGUAGES.keys():
        print(f"\n{lang_name}:")
        for folder in FOLDERS_TO_TRANSLATE:
            if folder in verification_results.get(lang_name, {}):
                print(f"  {folder}:")
                for filename, status in verification_results[lang_name][folder].items():
                    print(f"    {filename}: {status}")
    
    if all_passed:
        print("\n✓ All PASS!")
    else:
        print("\n✗ Some FAIL - see above")
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
