"""
Repair script for knowledge base translation errors.
Fixes: broken links, placeholder corruption, wrong titles, wrong directories.
"""
import re
import os
from pathlib import Path

KB_ROOT = Path(__file__).parent.parent / "knowledge_base"
ENGLISH_README = KB_ROOT / "English" / "README.md"

LANGUAGES = [
    "Arabic", "French", "German", "Spanish", "Japanese", "Russian",
    "Thai", "Vietnamese", "Turkish", "Polish", "Portuguese", "Persian",
    "Indonesian", "Italian", "Mandarin_Simplified", "Mandarin_Traditional",
    "Hindi", "Korean", "Bengali", "Urdu", "Filipino", "Swahili",
]

# 6 files that don't exist in any language directory
BROKEN_FILES = {
    "web_development.md",
    "security_best_practices.md",
    "software_architecture_patterns.md",
    "technology_glossary.md",
    "tool_usage.md",
    "testing_methodologies.md",
}

# Correct titles for each language (what the H1 should say)
CORRECT_TITLES = {
    "Arabic": "قاعدة المعرفة",
    "Bengali": "জ্ঞান ভাণ্ডার",
    "Filipino": "Base ng Kaalaman",
    "French": "Base de connaissances",
    "German": "Wissensdatenbank",
    "Spanish": "Base de conocimientos",
    "Japanese": "ナレッジベース",
    "Russian": "База знаний",
    "Swahili": "Hazina ya Maarifa",
    "Thai": "ฐานความรู้",
    "Urdu": "علمی ذخیرہ",
    "Vietnamese": "Kho kiến thức",
    "Turkish": "Bilgi Bankası",
    "Polish": "Baza wiedzy",
    "Portuguese": "Base de conhecimento",
    "Persian": "پایگاه دانش",
    "Indonesian": "Basis Pengetahuan",
    "Italian": "Base di conoscenza",
    "Mandarin_Simplified": "知识库",
    "Mandarin_Traditional": "知識庫",
    "Hindi": "नॉलेज बेस",
    "Korean": "지식 베이스",
}

# Placeholder patterns per language
PLACEHOLDER_PATTERNS = {
    "Arabic": re.compile(r'__محمي_(\d+)__'),
    "French": re.compile(r'__PROTÉGÉ_(\d+)__'),
    "Persian": re.compile(r'__محافظت شده_(\d+)__'),
}

# Original English section 01 files (before broken rows were removed)
# Needed for mapping placeholders in corrupted READMEs
ORIGINAL_SECTION_01_FILES = [
    ("web_development.md", "01_coding_and_technology/web_development.md"),
    ("database_systems.md", "01_coding_and_technology/database_systems.md"),
    ("cloud_architecture.md", "01_coding_and_technology/cloud_architecture.md"),
    ("networking_basics.md", "01_coding_and_technology/networking_basics.md"),
    ("devops_sysadmin.md", "01_coding_and_technology/devops_sysadmin.md"),
    ("security_best_practices.md", "01_coding_and_technology/security_best_practices.md"),
    ("devops_and_cicd.md", "01_coding_and_technology/devops_and_cicd.md"),
    ("cybersecurity_fundamentals.md", "01_coding_and_technology/cybersecurity_fundamentals.md"),
    ("api_design_and_architecture.md", "01_coding_and_technology/api_design_and_architecture.md"),
    ("software_architecture_patterns.md", "01_coding_and_technology/software_architecture_patterns.md"),
    ("technology_glossary.md", "01_coding_and_technology/technology_glossary.md"),
    ("tool_usage.md", "01_coding_and_technology/tool_usage.md"),
    ("accessibility_and_inclusive_design.md", "01_coding_and_technology/accessibility_and_inclusive_design.md"),
    ("blockchain_and_distributed_systems.md", "01_coding_and_technology/blockchain_and_distributed_systems.md"),
    ("data_structures_and_algorithms.md", "01_coding_and_technology/data_structures_and_algorithms.md"),
    ("embedded_systems_and_iot.md", "01_coding_and_technology/embedded_systems_and_iot.md"),
    ("low_code_and_platform_engineering.md", "01_coding_and_technology/low_code_and_platform_engineering.md"),
    ("mobile_development.md", "01_coding_and_technology/mobile_development.md"),
    ("performance_optimization.md", "01_coding_and_technology/performance_optimization.md"),
    ("testing_methodologies.md", "01_coding_and_technology/testing_methodologies.md"),
]

# Programming language directory paths (ordered, matches placeholder indices 0-33)
PROG_LANG_PATHS = [
    ("`programming_languages/python/`", ""),
    ("`programming_languages/javascript/`", ""),
    ("`programming_languages/c/`", ""),
    ("`programming_languages/cpp/`", ""),
    ("`programming_languages/java/`", ""),
    ("`programming_languages/csharp/`", ""),
    ("`programming_languages/go/`", ""),
    ("`programming_languages/rust/`", ""),
    ("`programming_languages/typescript/`", ""),
    ("`programming_languages/sql/`", ""),
    ("`programming_languages/ruby/`", ""),
    ("`programming_languages/php/`", ""),
    ("`programming_languages/swift/`", ""),
    ("`programming_languages/kotlin/`", ""),
    ("`programming_languages/r/`", ""),
    ("`programming_languages/visual_basic/`", ""),
    ("`programming_languages/dart/`", ""),
    ("`programming_languages/scala/`", ""),
    ("`programming_languages/haskell/`", ""),
    ("`programming_languages/julia/`", ""),
    ("`programming_languages/lua/`", ""),
    ("`programming_languages/perl/`", ""),
    ("`programming_languages/erlang_and_elixir/`", ""),
    ("`programming_languages/ocaml/`", ""),
    ("`programming_languages/prolog/`", ""),
    ("`programming_languages/lisp_and_clojure/`", ""),
    ("`programming_languages/ada/`", ""),
    ("`programming_languages/assembly/`", ""),
    ("`programming_languages/matlab/`", ""),
    ("`programming_languages/fortran/`", ""),
    ("`programming_languages/cobol/`", ""),
    ("`programming_languages/shell_and_powershell/`", ""),
    ("`programming_languages/delphi_object_pascal/`", ""),
    ("`programming_languages/scratch/`", ""),
]

# Hindi/Korean native-script directory names → English
NATIVE_DIR_FIXES = {
    "Hindi": [
        ("01_कोडिंग_और_तकनीक", "01_coding_and_technology"),
        ("02_कृत्रिम_बुद्धिमत्ता_और_मशीन_लर्निंग", "02_ai_and_machine_learning"),
        ("03_डेटा_विज्ञान_और_एनालिटिक्स", "03_data_science_and_analytics"),
        ("04_प्राकृतिक_विज्ञान", "04_natural_sciences"),
        ("05_व्यवसाय_और_अर्थव्यवस्था", "05_business_and_economics"),
        ("06_मानविकी_और_कला", "06_humanities_and_arts"),
        ("07_सामान्य_संदर्भ", "07_general_reference"),
        ("08_भविष्य_और_रुझान", "08_future_and_trends"),
        ("09_असफलताओं_से_सीख", "09_lessons_from_failures"),
        ("10_त्वरित_संदर्भ", "10_quick_reference"),
    ],
    "Korean": [
        ("01_코딩_및_기술", "01_coding_and_technology"),
        ("02_인공지능_및_머신러닝", "02_ai_and_machine_learning"),
        ("03_데이터_과학_및_분석", "03_data_science_and_analytics"),
        ("04_자연과학", "04_natural_sciences"),
        ("05_비즈니스_및_경제", "05_business_and_economics"),
        ("06_인문학_및_예술", "06_humanities_and_arts"),
        ("07_일반_참조", "07_general_reference"),
        ("08_미래_및_트렌드", "08_future_and_trends"),
        ("09_실패에서_배우는_교훈", "09_lessons_from_failures"),
        ("10_빠른_참조", "10_quick_reference"),
    ],
}


def parse_english_section_files():
    """Parse the English README to get ordered file links per section."""
    content = ENGLISH_README.read_text(encoding="utf-8")
    lines = content.split("\n")

    sections = {}
    current_section = None
    link_re = re.compile(r'\[([^\]]+\.md)\]\(([^)]+)\)')

    for line in lines:
        # Detect section headers like "### 01 —" or "### 02 —"
        section_match = re.match(r'###\s*(\d{2})\s*[—-]', line)
        if section_match:
            current_section = section_match.group(1)
            if current_section not in sections:
                sections[current_section] = []
            continue

        # Detect subcategory headers (like "**Foundations**", "**Life Sciences**")
        # These indicate sub-sections within 02, 03, 04, 06, 08, 10
        # For the flat READMEs (non-English), these are flattened, so we just
        # track ALL file links within each numbered section

        if current_section:
            match = link_re.search(line)
            if match:
                filename = match.group(1)
                filepath = match.group(2)
                # Only include files from 01_coding section (the main table)
                # Skip programming_languages subdirectory links
                if "programming_languages/" not in filepath:
                    sections[current_section].append((filename, filepath))

    return sections


def has_placeholder_corruption(lang, line):
    """Check if a line has placeholder corruption."""
    if lang in PLACEHOLDER_PATTERNS:
        return bool(PLACEHOLDER_PATTERNS[lang].search(line))
    return False


def fix_placeholder_in_line(lang, line, file_list, section_counter):
    """Replace a placeholder with the correct markdown link or path."""
    pattern = PLACEHOLDER_PATTERNS.get(lang)
    if not pattern:
        return line

    def replacer(match):
        idx = int(match.group(1))
        if idx < len(file_list):
            name, path = file_list[idx]
            if path:  # Has a link path — create markdown link
                return f"[{name}]({path})"
            else:  # No path — just display text (e.g., programming language paths)
                return name
        return match.group(0)  # Keep placeholder if no mapping

    return pattern.sub(replacer, line)


def fix_readme(lang):
    """Fix a single language README."""
    readme_path = KB_ROOT / lang / "README.md"
    if not readme_path.exists():
        print(f"  SKIP: {readme_path} does not exist")
        return

    content = readme_path.read_text(encoding="utf-8")
    original = content
    lines = content.split("\n")

    # Get English section files for placeholder restoration
    en_sections = parse_english_section_files()
    is_corrupted = lang in PLACEHOLDER_PATTERNS

    # === FIX 1: Title ===
    correct_title = CORRECT_TITLES.get(lang, "Knowledge Base")
    # Replace the first H1 line
    for i, line in enumerate(lines):
        if line.startswith("# "):
            lines[i] = f"# {correct_title}"
            break

    # === FIX 2: Code block directory reference ===
    # Replace knowledge_base/English/ with knowledge_base/{lang}/ in code blocks
    in_code_block = False
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
        if in_code_block and "knowledge_base/English/" in line:
            lines[i] = line.replace("knowledge_base/English/", f"knowledge_base/{lang}/")

    # === FIX 3: Hindi/Korean native-script directory names ===
    if lang in NATIVE_DIR_FIXES:
        for native, english in NATIVE_DIR_FIXES[lang]:
            for i, line in enumerate(lines):
                if native in line:
                    lines[i] = line.replace(native, english)

    # Build broken file index sets per section (for corrupted READMEs)
    broken_indices = {}
    if is_corrupted:
        # Use original file lists (before broken rows were removed from English)
        original_sections = {"01": ORIGINAL_SECTION_01_FILES}
        # For other sections, the parsed English list should still be correct
        # (broken files only exist in section 01)
        for sec_id, files in en_sections.items():
            if sec_id != "01":
                original_sections[sec_id] = files
        for sec_id, files in original_sections.items():
            broken_indices[sec_id] = {
                idx for idx, (fn, fp) in enumerate(files) if fn in BROKEN_FILES
            }

    # === Process line by line for remaining fixes ===
    result = []
    current_section = None
    section_counter = 0  # Counter for placeholder mapping within section
    in_prog_lang_table = False  # Track if we're in the programming languages table

    for i, line in enumerate(lines):
        # Track current section
        section_match = re.match(r'###\s*(\d{2})\s*[—\-–]', line)
        if section_match:
            current_section = section_match.group(1)
            section_counter = 0
            in_prog_lang_table = False
            result.append(line)
            continue

        # Detect programming languages sub-table — placeholders restart from 0
        if is_corrupted and re.match(r'.*34.*', line) and any(c in line for c in [
            'لغات البرمجة', 'Langages de programmation', 'Programmiersprachen',
            'لغات برنامه نویسی', 'programming_languages', '34 لغة', '34 langues',
            '34 Sprachen', '34 زبان', '34 言語', '34 языка', '34 भाषा',
        ]):
            section_counter = 0
            in_prog_lang_table = True
            result.append(line)
            continue

        # For corrupted READMEs: check if this placeholder row maps to a broken file
        if is_corrupted and current_section and line.strip().startswith("|"):
            pat = PLACEHOLDER_PATTERNS.get(lang)
            if pat and pat.search(line):
                # Use programming language paths if in that table
                if in_prog_lang_table:
                    file_list = PROG_LANG_PATHS
                elif current_section == "01":
                    # Use original (pre-fix) file list for section 01
                    # since the parsed English list has broken rows removed
                    file_list = ORIGINAL_SECTION_01_FILES
                else:
                    file_list = en_sections.get(current_section, [])

                m = pat.search(line)
                idx = int(m.group(1))

                # Check if this maps to a broken file (only for main section tables)
                if not in_prog_lang_table and idx in broken_indices.get(current_section, set()):
                    continue  # Skip broken file rows

                # Map placeholder to correct file
                new_line = fix_placeholder_in_line(lang, line, file_list, section_counter)
                section_counter += 1
                result.append(new_line)
                continue

        # For corrupted READMEs: fix learning path placeholders
        if is_corrupted and current_section and re.match(r'\s*\d+\.', line):
            pat = PLACEHOLDER_PATTERNS.get(lang)
            if pat and pat.search(line):
                full_sec_files = en_sections.get(current_section, [])
                new_line = fix_placeholder_in_line(lang, line, full_sec_files, section_counter)
                matches = list(pat.finditer(line))
                if matches:
                    section_counter += len(matches)
                result.append(new_line)
                continue

        # Skip table rows referencing non-existent files (non-corrupted READMEs)
        is_broken_row = False
        for bf in BROKEN_FILES:
            if bf in line and line.strip().startswith("|"):
                # Check it's a table data row (not header/separator)
                stripped = line.strip()
                is_header = any(stripped.startswith(p) for p in [
                    "|---", "| File", "| Archivo", "| Datei", "| Fichier",
                    "| ファイル", "| Файл", "| फ़ाइल", "| 파일", "| ملف",
                    "| 文件", "| Файл"
                ])
                if not is_header:
                    is_broken_row = True
                    break
        if is_broken_row:
            continue

        # Fix learning path references to non-existent files (non-corrupted)
        is_broken_learning_path = False
        for bf in BROKEN_FILES:
            if bf in line and re.match(r'\s*\d+\.', line):
                is_broken_learning_path = True
                break
        if is_broken_learning_path:
            continue

        result.append(line)

    new_content = "\n".join(result)

    if new_content != original:
        readme_path.write_text(new_content, encoding="utf-8")
        print(f"  FIXED: {readme_path}")
    else:
        print(f"  NO CHANGE: {readme_path}")


def fix_technology_and_computing(lang):
    """Fix broken cross-references in technology_and_computing.md."""
    filepath = KB_ROOT / lang / "07_general_reference" / "technology_and_computing.md"
    if not filepath.exists():
        return

    content = filepath.read_text(encoding="utf-8")
    original = content

    # Fix: Remove references to web_development.md and security_best_practices.md
    # These appear in "go deeper" paragraphs as markdown links

    # Pattern 1: [web development](../01_coding_and_technology/web_development.md)
    # These appear inline in a paragraph, so we remove the link text
    # The paragraph lists files: "including [web development](...), [database systems](...), ..."
    # We need to remove just the web development and security references

    # Remove web development link and surrounding comma/space
    content = re.sub(
        r'\[web development\]\(\.\./01_coding_and_technology/web_development\.md\),?\s*',
        '', content
    )
    # Also handle non-relative links
    content = re.sub(
        r'\[web development\]\(01_coding_and_technology/web_development\.md\),?\s*',
        '', content
    )

    # Remove security best practices link (appears twice - in overview and cybersecurity section)
    content = re.sub(
        r',?\s*\[security\]\(\.\./01_coding_and_technology/security_best_practices\.md\)',
        '', content
    )
    content = re.sub(
        r',?\s*\[security best practices\]\(\.\./01_coding_and_technology/security_best_practices\.md\)',
        '', content
    )
    content = re.sub(
        r',?\s*\[security\]\(01_coding_and_technology/security_best_practices\.md\)',
        '', content
    )
    content = re.sub(
        r',?\s*\[security best practices\]\(01_coding_and_technology/security_best_practices\.md\)',
        '', content
    )

    # Fix the cybersecurity paragraph that says "see [security best practices](...)"
    # Replace with a generic reference since the file doesn't exist
    # Look for the sentence pattern and replace it
    content = re.sub(
        r'For a full guide covering OWASP Top 10, secure development lifecycle, and secrets management, see \.',
        'For a full guide covering OWASP Top 10, secure development lifecycle, and secrets management, see the cybersecurity fundamentals reference.',
        content
    )
    # Similar patterns in other languages
    # Since the sentence structure varies, we'll use a broader approach:
    # If the line still has a dangling "see ." or "see ,", fix it
    content = re.sub(r'see\s+\.\s*$', 'see the cybersecurity fundamentals reference.', content, flags=re.MULTILINE)
    content = re.sub(r'see\s+\.,', 'see the cybersecurity fundamentals reference,', content)

    if content != original:
        filepath.write_text(content, encoding="utf-8")
        print(f"  FIXED: {filepath}")


def fix_english_readme():
    """Fix the English README specifically."""
    filepath = KB_ROOT / "English" / "README.md"
    content = filepath.read_text(encoding="utf-8")
    original = content
    lines = content.split("\n")

    result = []
    for line in lines:
        # Skip table rows referencing non-existent files
        is_broken = False
        for bf in BROKEN_FILES:
            if bf in line and line.strip().startswith("| ["):
                is_broken = True
                break
        if is_broken:
            continue

        # Skip learning path references to non-existent files
        is_broken_lp = False
        for bf in BROKEN_FILES:
            if bf in line and re.match(r'\s*\d+\.\s*`', line):
                is_broken_lp = True
                break
        if is_broken_lp:
            continue

        result.append(line)

    new_content = "\n".join(result)
    if new_content != original:
        filepath.write_text(new_content, encoding="utf-8")
        print(f"  FIXED: {filepath}")


def main():
    print("=== Knowledge Base README Repair Script ===\n")

    # Fix English README first
    print("Fixing English README...")
    fix_english_readme()

    # Fix all non-English READMEs
    print("\nFixing non-English READMEs...")
    for lang in LANGUAGES:
        fix_readme(lang)

    # Fix technology_and_computing.md files
    print("\nFixing technology_and_computing.md cross-references...")
    all_langs = ["English"] + LANGUAGES
    for lang in all_langs:
        fix_technology_and_computing(lang)

    print("\n=== Repair complete ===")


if __name__ == "__main__":
    main()
