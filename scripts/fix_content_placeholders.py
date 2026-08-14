"""
Fix remaining placeholder corruption in content files.
Restores inline code that was protected by placeholders during translation
but never restored. Uses English originals as reference.
"""
import re
from pathlib import Path

KB_ROOT = Path(__file__).parent.parent / "knowledge_base"


def fix_arabic_terraform():
    """Fix __محمي_X__ in Arabic terraform_quick_ref.md"""
    fp = KB_ROOT / "Arabic" / "10_quick_reference" / "infrastructure" / "terraform_quick_ref.md"
    lines = fp.read_text(encoding="utf-8").splitlines()

    # Workflow table: placeholders replace terraform commands (lines ~56-64)
    workflow_map = {
        "1": "`terraform init`",
        "2": "`terraform fmt`",
        "3": "`terraform validate`",
        "4": "`terraform plan`",
        "5": "`terraform apply`",
        "6": "`terraform destroy`",
    }

    # Commands table: different mapping (lines ~67-83)
    commands_map = {
        "0": "`terraform init`",
        "1": "`terraform plan`",
        "2": "`terraform apply`",
        "3": "`-auto-approve`",
        "4": "`terraform destroy`",
        "5": "`terraform fmt`",
        "6": "`terraform validate`",
        "7": "`terraform output`",
        "8": "`terraform state list`",
        "9": "`terraform state show <resource>`",
        "10": "`terraform import <resource> <id>`",
        "11": "`terraform taint <resource>`",
        "12": "`terraform refresh`",
        "13": "`terraform graph`",
        "14": "`terraform console`",
    }

    pat = re.compile(r'__محمي_(\d+)__')
    in_commands = False
    new_lines = []

    for line in lines:
        if "الأوامر المشتركة" in line:
            in_commands = True

        def replacer(m):
            idx = m.group(1)
            if in_commands:
                return commands_map.get(idx, m.group(0))
            else:
                return workflow_map.get(idx, m.group(0))

        new_lines.append(pat.sub(replacer, line))

    fp.write_text("\n".join(new_lines), encoding="utf-8")
    print(f"  Fixed: {fp.relative_to(KB_ROOT.parent)}")


def fix_arabic_sql():
    """Fix __محمي_X__ in Arabic sql_quick_ref.md"""
    fp = KB_ROOT / "Arabic" / "10_quick_reference" / "programming" / "sql_quick_ref.md"
    content = fp.read_text(encoding="utf-8")

    # Each subsection restarts the counter from 0
    # Numeric: 0=INT, 1=BIGINT, 3=FLOAT, 4=DOUBLE
    # String: 0=CHAR(n), 2=TEXT, 3=ENUM
    # Date/Time: 0=DATE, 1=TIME, 2=DATETIME, 3=TIMESTAMP, 4=YEAR
    # Boolean: 0=BOOLEAN, 1=BOOL
    # Binary: 0=BLOB, 1=BINARY, 2=VARBINARY

    replacements = [
        # Numeric section
        ("__محمي_0__ - عدد صحيح", "`INT` - عدد صحيح"),
        ("__محمي_1__ - عدد صحيح كبير", "`BIGINT` - عدد صحيح كبير"),
        ("__محمي_3__ - نقطة عائمة تقريبية", "`FLOAT` - نقطة عائمة تقريبية"),
        ("__محمي_4__ - تعويم مزدوج الدقة", "`DOUBLE` - تعويم مزدوج الدقة"),
        # String section
        ("__محمي_0__ - سلسلة ذات طول ثابت", "`CHAR(n)` - سلسلة ذات طول ثابت"),
        ("__محمي_2__ - نص كبير", "`TEXT` - نص كبير"),
        ("__محمي_3__ - القيم المذكورة", "`ENUM` - القيم المذكورة"),
        # Date/Time section
        ("__محمي_0__ - التاريخ", "`DATE` - التاريخ"),
        ("__محمي_1__ - الوقت", "`TIME` - الوقت"),
        ("__محمي_2__ - التاريخ والوقت", "`DATETIME` - التاريخ والوقت"),
        ("__محمي_3__ - الطابع الزمني", "`TIMESTAMP` - الطابع الزمني"),
        ("__محمي_4__ - قيمة السنة", "`YEAR` - قيمة السنة"),
        # Boolean section
        ("__محمي_0__ أو __محمي_1__ - صواب/خطأ", "`BOOLEAN` أو `BOOL` - صواب/خطأ"),
        # Binary section
        ("__محمي_0__ - كائن ثنائي كبير", "`BLOB` - كائن ثنائي كبير"),
        ("__محمي_1__ - ثنائي ثابت", "`BINARY` - ثنائي ثابت"),
        ("__محمي_2__ - ثنائي متغير", "`VARBINARY` - ثنائي متغير"),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    fp.write_text(content, encoding="utf-8")
    print(f"  Fixed: {fp.relative_to(KB_ROOT.parent)}")


def fix_persian_terraform():
    """Fix __محافظت شده_X__ in Persian terraform_quick_ref.md"""
    fp = KB_ROOT / "Persian" / "10_quick_reference" / "infrastructure" / "terraform_quick_ref.md"
    lines = fp.read_text(encoding="utf-8").splitlines()

    # Workflow table: placeholders replace terraform commands
    workflow_map = {
        "1": "`terraform init`",
        "3": "`terraform validate`",
        "6": "`terraform destroy`",
    }

    # Commands table: different mapping
    commands_map = {
        "1": "`terraform plan`",
        "6": "`terraform validate`",
        "9": "`terraform state show <resource>`",
    }

    # Variable Types table: counter restarts from 0
    # 0=string (already has backticks), 1=number, 2=bool (has backticks), 3=list, 4=map (has backticks), 5=object (has backticks)
    var_types_map = {
        "1": "`variable \"count\" { type = number }`",
        "3": "`variable \"zones\" { type = list(string) }`",
    }

    pat = re.compile(r'__محافظت شده_(\d+)__')
    section = None
    new_lines = []

    for line in lines:
        if "گردش کار" in line or "Workflow" in line:
            section = "workflow"
        elif "دستورات رایج" in line or "Common Commands" in line:
            section = "commands"
        elif "انواع متغیر" in line or "Variable Types" in line:
            section = "var_types"

        def replacer(m):
            idx = m.group(1)
            if section == "commands":
                return commands_map.get(idx, m.group(0))
            elif section == "var_types":
                return var_types_map.get(idx, m.group(0))
            else:
                return workflow_map.get(idx, m.group(0))

        new_lines.append(pat.sub(replacer, line))

    fp.write_text("\n".join(new_lines), encoding="utf-8")
    print(f"  Fixed: {fp.relative_to(KB_ROOT.parent)}")


def fix_persian_regex():
    """Fix __محافظت شده_X__ in Persian regular_expressions.md"""
    fp = KB_ROOT / "Persian" / "10_quick_reference" / "programming" / "regular_expressions.md"
    content = fp.read_text(encoding="utf-8")

    # Each table section restarts counter from 0
    # Core Syntax table: 1=^, 3=*, 9=()
    # Character Classes: 1=[a-z], 3=[0-9], 6=[a-z0-9_]
    # Shorthand Classes: 1=[0-9], 3=[^0-9], 6=[^a-zA-Z0-9_], 9=[ \t\n\r\f]  (but \W is [^a-zA-Z0-9_])
    # Quantifiers: 1=ab*c, 3=ab+c, 6={n}, 9=a{2,}
    # Greedy: 1=<b>hi</b>, 6=<b>hi</b>

    # Since each section restarts, and the placeholders are in different table contexts,
    # we need context-aware replacement. Let's do line-by-line.

    lines = content.splitlines()
    pat = re.compile(r'__محافظت شده_(\d+)__')

    # Track which section we're in
    section = None
    new_lines = []

    for line in lines:
        # Detect section boundaries
        if "هسته" in line or "Core" in line:
            section = "core_syntax"
        elif "کلاس های شخصیت" in line or "Character Classes" in line:
            section = "char_classes"
        elif "کلاس های کوتاه" in line or "Shorthand" in line:
            section = "shorthand"
        elif "کمیت کننده" in line or "Quantifier" in line:
            section = "quantifiers"
        elif "حریص" in line or "Greedy" in line:
            section = "greedy"

        def replacer(m):
            idx = m.group(1)
            if section == "core_syntax":
                return {"1": "`^`", "3": "`*`", "9": "`()`"}.get(idx, m.group(0))
            elif section == "char_classes":
                return {"1": "`[a-z]`", "3": "`[0-9]`", "6": "`[a-z0-9_]`"}.get(idx, m.group(0))
            elif section == "shorthand":
                return {"1": "`[0-9]`", "3": "`[^0-9]`", "6": "`\\W`", "9": "`[ \\t\\n\\r\\f]`"}.get(idx, m.group(0))
            elif section == "quantifiers":
                return {"1": "`ab*c`", "3": "`ab+c`", "6": "`{n}`", "9": "`a{2,}`"}.get(idx, m.group(0))
            elif section == "greedy":
                return {"1": "`<b>hi</b>`", "6": "`<b>hi</b>`"}.get(idx, m.group(0))
            return m.group(0)

        new_lines.append(pat.sub(replacer, line))

    fp.write_text("\n".join(new_lines), encoding="utf-8")
    print(f"  Fixed: {fp.relative_to(KB_ROOT.parent)}")


def fix_persian_linux():
    """Fix __محافظت شده_X__ in Persian linux_commands.md"""
    fp = KB_ROOT / "Persian" / "10_quick_reference" / "infrastructure" / "linux_commands.md"
    content = fp.read_text(encoding="utf-8")

    # Keyboard shortcuts section: 1=Ctrl+C, 3=Ctrl+D, 6=Ctrl+E, 9=Ctrl+R
    replacements = [
        ("__محافظت شده_1__", "`Ctrl+C`"),
        ("__محافظت شده_3__", "`Ctrl+D`"),
        ("__محافظت شده_6__", "`Ctrl+E`"),
        ("__محافظت شده_9__", "`Ctrl+R`"),
    ]

    for old, new in replacements:
        content = content.replace(old, new)

    fp.write_text(content, encoding="utf-8")
    print(f"  Fixed: {fp.relative_to(KB_ROOT.parent)}")


def check_persian_terraform_core_concepts():
    """Also fix the core concepts table in Persian terraform if it has placeholders"""
    fp = KB_ROOT / "Persian" / "10_quick_reference" / "infrastructure" / "terraform_quick_ref.md"
    content = fp.read_text(encoding="utf-8")
    # Check if there are still any remaining placeholders
    remaining = re.findall(r'__محافظت شده_\d+__', content)
    if remaining:
        print(f"  WARNING: {len(remaining)} placeholders still remain in Persian terraform: {remaining}")
    else:
        print(f"  OK: Persian terraform clean")


if __name__ == "__main__":
    print("Fixing remaining content file placeholders...\n")

    print("[1/5] Arabic terraform_quick_ref.md")
    fix_arabic_terraform()

    print("[2/5] Arabic sql_quick_ref.md")
    fix_arabic_sql()

    print("[3/5] Persian terraform_quick_ref.md")
    fix_persian_terraform()

    print("[4/5] Persian regular_expressions.md")
    fix_persian_regex()

    print("[5/5] Persian linux_commands.md")
    fix_persian_linux()

    print("\n--- Verification ---")
    check_persian_terraform_core_concepts()

    # Final sweep
    print("\n--- Final placeholder sweep ---")
    for lang_dir in KB_ROOT.iterdir():
        if not lang_dir.is_dir():
            continue
        for md_file in lang_dir.rglob("*.md"):
            content = md_file.read_text(encoding="utf-8")
            arabic = re.findall(r'__محمي_\d+__', content)
            persian = re.findall(r'__محافظت شده_\d+__', content)
            french = re.findall(r'__PROTÉGÉ_\d+__', content)
            total = len(arabic) + len(persian) + len(french)
            if total > 0:
                rel = md_file.relative_to(KB_ROOT)
                print(f"  REMAINING: {rel} — Arabic:{len(arabic)} Persian:{len(persian)} French:{len(french)}")

    print("\nDone!")
