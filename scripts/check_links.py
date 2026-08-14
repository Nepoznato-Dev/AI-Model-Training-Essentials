import re
import urllib.parse
from pathlib import Path

root = Path(r"c:\Users\PC\Downloads\AI-Model-Training-Essentials-main")
link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
# Inline code spans are literal code, never links — strip before scanning so
# snippets like `[](int x){...}` or regex examples aren't misreported.
inline_re = re.compile(r"`[^`]*`")

broken = []
for md in sorted(root.rglob("*.md")):
    text = md.read_text(encoding="utf-8", errors="ignore")
    in_code = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        scan_line = inline_re.sub("", line)
        for target in link_re.findall(scan_line):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target = urllib.parse.unquote(target)
            if target.startswith(("data:", "javascript:")):
                continue
            candidate = target.split("#", 1)[0].strip()
            if not candidate:
                continue
            if candidate.startswith(("http://", "https://", "mailto:", "data:", "javascript:")):
                continue
            if candidate.startswith("/"):
                continue
            resolved = (md.parent / candidate).resolve()
            if not resolved.exists() and not candidate.endswith("/"):
                broken.append((str(md.relative_to(root)).replace("\\", "/"), target))

seen = set()
uniq = []
for item in broken:
    if item not in seen:
        seen.add(item)
        uniq.append(item)

print(f"UNIQUE_BROKEN {len(uniq)}")
for file_path, target in uniq[:200]:
    print(f"{file_path} -> {target}")
