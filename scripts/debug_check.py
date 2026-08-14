"""Debug script - writes output to file to avoid encoding issues."""
import re
from pathlib import Path

KB_ROOT = Path(__file__).parent.parent / "knowledge_base"
readme = KB_ROOT / "Arabic" / "README.md"
content = readme.read_text(encoding="utf-8")
lines = content.split("\n")

pat = re.compile(r'__محمي_(\d+)__')
sec_pat = re.compile(r'###\s*(\d{2})\s*[—\-–]')

output = []

current_section = None
for i, line in enumerate(lines):
    sm = sec_pat.match(line)
    if sm:
        current_section = sm.group(1)
    
    if pat.search(line) and 48 <= i <= 56:
        starts_pipe = line.strip().startswith("|")
        m = pat.search(line)
        idx = int(m.group(1)) if m else -1
        output.append(f"Line {i}: section={current_section}, starts_pipe={starts_pipe}, placeholder_idx={idx}")

# Parse English section 01 files
BROKEN_FILES = {
    "web_development.md", "security_best_practices.md",
    "software_architecture_patterns.md", "technology_glossary.md",
    "tool_usage.md", "testing_methodologies.md",
}

en_readme = KB_ROOT / "English" / "README.md"
en_content = en_readme.read_text(encoding="utf-8")
en_lines = en_content.split("\n")

section_01_files = []
in_section_01 = False
link_re = re.compile(r'\[([^\]]+\.md)\]\(([^)]+)\)')
for line in en_lines:
    if re.match(r'###\s*01\s*[—-]', line):
        in_section_01 = True
        continue
    if in_section_01 and re.match(r'###\s*\d{2}', line):
        break
    if in_section_01:
        m = link_re.search(line)
        if m and "programming_languages/" not in m.group(2):
            section_01_files.append((m.group(1), m.group(2)))

broken_idx = set()
for idx, (fn, fp) in enumerate(section_01_files):
    is_broken = fn in BROKEN_FILES
    if is_broken:
        broken_idx.add(idx)
    output.append(f"  [{idx}] {fn} {'BROKEN' if is_broken else 'OK'}")

output.append(f"\nTotal section 01 files: {len(section_01_files)}")
output.append(f"Broken indices: {broken_idx}")

# Write output to file
out_path = Path(__file__).parent / "debug_output.txt"
out_path.write_text("\n".join(output), encoding="utf-8")
