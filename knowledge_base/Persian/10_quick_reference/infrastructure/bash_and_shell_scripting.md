<!--
---
# Metadata
title: "Bash and Shell Scripting Cheat Sheet"
description: "Bash scripting, text processing, useful one-liners"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [bash, shell, scripting, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "19 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# برگه تقلب اسکریپت Bash و Shell
یک مرجع عملی برای نوشتن اسکریپت های پوسته در Bash - پوسته پیش فرض در اکثر سیستم های لینوکس و macOS. سینتکس، الگوهای رایج، پردازش متن و تک خط های مفید را پوشش می دهد.
---

## ساختار اسکریپت
هر اسکریپت Bash با یک خط **shebang** شروع می شود:
```bash
#!/usr/bin/env bash
set -euo pipefail   # Safe defaults
```

| پرچم | اثر |
|------|--------|
| `set -e`| در صورت شکست دستوری فوراً خارج شوید |
| `set -u`| متغیرهای تنظیم نشده را به عنوان خطا در نظر بگیرید |
| `set -o pipefail`| خط لوله در صورت عدم موفقیت در هر دستوری از کار می افتد |
| `set -x`| هر دستور را قبل از اجرا چاپ کنید (حالت اشکال زدایی) |
یک اسکریپت را اجرا کنید:`chmod +x script.sh && ./script.sh`یا `bash script.sh`
---

## متغیرها
```bash
# Assignment (no spaces around =)
NAME="Alice"
COUNT=42

# Usage
echo "$NAME"          # Alice
echo "${NAME}"        # Alice (explicit delimiter)
echo "Hello, $NAME!"  # Hello, Alice!

# Read-only
readonly PI=3.14159

# Command substitution
TODAY=$(date +%Y-%m-%d)
FILES=$(ls -1 | wc -l)

# Default values
echo "${UNSET_VAR:-default}"   # Prints "default" if UNSET_VAR is empty/unset
: "${REQUIRED_VAR:?Error: REQUIRED_VAR is not set}"  # Exit with error if unset

# Arithmetic
echo $((2 + 3))        # 5
echo $((COUNT * 2))    # 84
((COUNT++))            # Increment
```

---

## متغیرهای ویژه
| متغیر | معنی |
|----------|---------|
| `$0`| نام اسکریپت |
| `$1`,`$2`, ... | آرگومان های موضعی |
| `$#`| تعداد آرگومان های موضعی |
| `$@`| همه آرگومان های موضعی (به عنوان کلمات جداگانه) |
| `$*`| همه آرگومان های موقعیتی (به عنوان یک رشته) |
| `$?`| وضعیت خروج از آخرین فرمان (0 = موفقیت) |
| `$$`| PID فرآیند جاری |
| `$!`| PID آخرین فرآیند پس زمینه |
| `$_`| آخرین آرگومان دستور قبلی |
---

## شرایط
### if / elif / else
```bash
if [[ -f "$FILE" ]]; then
    echo "File exists"
elif [[ -d "$FILE" ]]; then
    echo "It's a directory"
else
    echo "Not found"
fi
```

### اپراتورهای تست
| تست | معنی |
|------|---------|
| `[[ -f "$x" ]]`| فایل موجود است و یک فایل معمولی است |
| `[[ -d "$x" ]]`| دایرکتوری وجود دارد |
| `[[ -e "$x" ]]`| فایل/دایرکتوری وجود دارد (هر چیزی) |
| `[[ -r "$x" ]]`| خواندنی |
| `[[ -w "$x" ]]`| قابل نوشتن |
| `[[ -x "$x" ]]`| قابل اجرا |
| `[[ -z "$x" ]]`| رشته خالی است |
| `[[ -n "$x" ]]`| رشته خالی نیست |
| `[[ "$a" == "$b" ]]`| برابری رشته |
| `[[ "$a" != "$b" ]]`| نابرابری رشته |
| `[[ "$a" =~ regex ]]`| بازی Regex |
| `[[ $a -eq $b ]]`| برابری عدد صحیح |
| `[[ $a -ne $b ]]`| نابرابری عدد صحیح |
| `[[ $a -gt $b ]]`| بزرگتر از |
| `[[ $a -lt $b ]]`| کمتر از |
| `[[ $a -ge $b ]]`| بزرگتر یا مساوی |
| `[[ $a -le $b ]]`| کمتر یا مساوی |
### عملگرهای منطقی
```bash
[[ -f "$a" && -f "$b" ]]   # AND
[[ -f "$a" || -f "$b" ]]   # OR
[[ ! -f "$a" ]]             # NOT
```

---

## حلقه ها
### برای حلقه
```bash
# C-style
for ((i = 0; i < 10; i++)); do
    echo "$i"
done

# Over a list
for item in apple banana cherry; do
    echo "$item"
done

# Over files
for file in *.txt; do
    echo "Processing $file"
done

# Over command output
for line in $(cat list.txt); do
    echo "$line"
done
```

### while حلقه
```bash
while [[ $COUNT -gt 0 ]]; do
    echo "$COUNT"
    ((COUNT--))
done

# Read file line by line
while IFS= read -r line; do
    echo "$line"
done < input.txt
```

### تا حلقه
```bash
until [[ -f /tmp/ready ]]; do
    echo "Waiting..."
    sleep 1
done
```

---

## توابع
```bash
# Define
greet() {
    local name="$1"          # local variable
    echo "Hello, ${name}!"
}

# Call
greet "Alice"               # Hello, Alice!

# Return values (use echo + command substitution)
add() {
    echo $(( $1 + $2 ))
}
RESULT=$(add 3 5)           # 8
```

---

## عملیات رشته
```bash
STR="Hello, World!"

echo "${#STR}"              # Length: 13
echo "${STR:0:5}"           # Substring: "Hello"
echo "${STR,,}"             # Lowercase: "hello, world!"
echo "${STR^^}"             # Uppercase: "HELLO, WORLD!"
echo "${STR/World/Bash}"    # Replace first: "Hello, Bash!"
echo "${STR//l/L}"          # Replace all: "HeLLo, WorLd!"
echo "${STR#*,}"            # Remove shortest prefix matching ,: " World!"
echo "${STR%,*}"            # Remove shortest suffix matching ,: "Hello"
```

---

## آرایه ها
```bash
# Indexed array
FRUITS=("apple" "banana" "cherry")
echo "${FRUITS[0]}"         # apple
echo "${FRUITS[@]}"         # all elements
echo "${#FRUITS[@]}"        # length: 3

# Append
FRUITS+=("date")

# Associative array (Bash 4+)
declare -A AGES
AGES[Alice]=30
AGES[Bob]=25
echo "${AGES[Alice]}"       # 30
echo "${!AGES[@]}"          # keys: Alice Bob
```

---

## لوله کشی و تغییر مسیر
| نحو | معنی |
|--------|---------|
| `cmd > file`| تغییر مسیر stdout به فایل (بازنویسی) |
| `cmd >> file`| تغییر مسیر stdout به فایل (پیوست) |
| `cmd 2> errors.log`| تغییر مسیر stderr |
| `cmd &> all.log`| تغییر مسیر هر دو stdout و stderr |
| `cmd1 \| cmd2`| لوله stdout از cmd1 به stdin از cmd2 |
| `cmd1 \|& cmd2`| هم stdout و هم stderr |
| `cmd < file`| تغییر مسیر فایل به stdin |
| `cmd <<EOF ... EOF`| در اینجا سند (ورودی چند خطی) |
| `cmd <<< "string"`| Here-string (ورودی تک خطی) |
```bash
# Here-document
cat <<EOF
Name: $NAME
Date: $(date)
EOF

# Process substitution
diff <(sort file1.txt) <(sort file2.txt)
```

---

## پردازش متن
### برش
```bash
echo "a,b,c" | cut -d',' -f2        # b (field 2, comma-delimited)
echo "hello world" | cut -c1-5      # hello (characters 1-5)
cut -d':' -f1 /etc/passwd           # First field (usernames)
```

### مرتب سازی
```bash
sort file.txt                       # Alphabetical sort
sort -n numbers.txt                 # Numeric sort
sort -r file.txt                    # Reverse sort
sort -t',' -k2 file.csv             # Sort by 2nd field, comma-delimited
sort -u file.txt                    # Sort and remove duplicates
```

### یونیک
```bash
sort names.txt | uniq               # Remove consecutive duplicates (sort first!)
sort names.txt | uniq -c            # Count occurrences
sort names.txt | uniq -d            # Show only duplicated lines
```

### عجب
```bash
awk '{print $1, $3}' file.txt              # Print columns 1 and 3
awk -F',' '{print $2}' data.csv            # CSV: print 2nd column
awk '/ERROR/ {print NR": "$0}' log.txt     # Print ERROR lines with line numbers
awk '{sum += $1} END {print sum}' nums.txt # Sum first column
awk 'length($0) > 80' file.txt             # Lines longer than 80 chars
awk '{print toupper($0)}' file.txt         # Uppercase every line
awk -F: '{print $1}' /etc/passwd           # Usernames from passwd file
```

### sed
```bash
sed 's/old/new/' file.txt           # Replace first occurrence per line
sed 's/old/new/g' file.txt          # Replace all occurrences
sed 's/old/new/gi' file.txt         # Case-insensitive replace all
sed '/pattern/d' file.txt           # Delete lines matching pattern
sed -n '5,10p' file.txt             # Print lines 5-10
sed 's/^/# /' file.txt              # Prepend "# " to every line
sed 's/[[:space:]]\+$//' file.txt   # Remove trailing whitespace
sed '10,20d' file.txt               # Delete lines 10-20
sed -i 's/old/new/g' file.txt       # Edit in place (macOS: sed -i '' ...)
```

### grep
```bash
grep "pattern" file.txt             # Basic search
grep -i "pattern" file.txt          # Case-insensitive
grep -r "pattern" directory/        # Recursive search
grep -rn "pattern" src/             # Recursive with line numbers
grep -c "ERROR" log.txt             # Count matching lines
grep -v "pattern" file.txt          # Invert match (exclude)
grep -E "regex" file.txt            # Extended regex
grep -l "pattern" *.txt             # List files containing match
grep -w "word" file.txt             # Match whole word only
grep -A 3 "pattern" file.txt        # Show 3 lines after match
grep -B 2 "pattern" file.txt        # Show 2 lines before match
grep -C 2 "pattern" file.txt        # Show 2 lines of context
```

---

## تک لاینرهای مفید
```bash
# Find largest files
find / -type f -exec du -h {} + 2>/dev/null | sort -rh | head -20

# Count lines of code in a directory
find . -name "*.py" | xargs wc -l | tail -1

# Monitor a log file in real time
tail -f /var/log/syslog | grep --line-buffered "ERROR"

# Find and replace in all files
find . -name "*.txt" -exec sed -i 's/old/new/g' {} +

# Check which process is using a port
lsof -i :8080          # macOS/Linux
ss -tlnp | grep 8080   # Linux

# Compress a directory
tar -czf archive.tar.gz directory/

# Extract a tarball
tar -xzf archive.tar.gz

# Download a file
curl -O https://example.com/file.zip      # Save with original name
wget https://example.com/file.zip          # Alternative

# Generate a random password
openssl rand -base64 24
# or
tr -dc 'A-Za-z0-9!@#$%' < /dev/urandom | head -c 20

# JSON pretty-print
cat data.json | python3 -m json.tool
# or
cat data.json | jq .

# CSV to TSV
tr ',' '\t' < data.csv

# Remove duplicate lines (preserving order)
awk '!seen[$0]++' file.txt

# Find files modified in the last 24 hours
find . -type f -mtime -1

# Kill all processes matching a name
pkill -f "python app.py"

# Disk usage summary
du -sh */ | sort -rh | head -10

# System info one-liner
uname -a; echo "---"; uptime; echo "---"; df -h; echo "---"; free -h
```

---

## الگوهای اسکریپت
### تجزیه آرگومان
```bash
#!/usr/bin/env bash
set -euo pipefail

usage() {
    echo "Usage: $0 [-n NAME] [-v] FILE"
    exit 1
}

VERBOSE=false
while getopts "n:v" opt; do
    case $opt in
        n) NAME="$OPTARG" ;;
        v) VERBOSE=true ;;
        *) usage ;;
    esac
done
shift $((OPTIND - 1))

FILE="${1:?Error: FILE argument required}"
echo "Name: ${NAME:-not set}, Verbose: $VERBOSE, File: $FILE"
```

### رسیدگی به خطا
```bash
#!/usr/bin/env bash
set -euo pipefail

cleanup() {
    echo "Cleaning up..."
    rm -f /tmp/tempfile
}
trap cleanup EXIT

error_handler() {
    echo "Error on line $1, exit code $2" >&2
}
trap 'error_handler ${LINENO} $?' ERR
```

### بررسی وابستگی ها
```bash
for cmd in git docker python3; do
    if ! command -v "$cmd" &>/dev/null; then
        echo "Error: $cmd is not installed" >&2
        exit 1
    fi
done
```

### فایل های موقت
```bash
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
echo "working..." > "$TMPFILE"
```

---

## خلاصه
برنامه نویسی Bash بهره وری را برای هر کسی که با رایانه کار می کند افزایش می دهد. لازم نیست همه پرچم ها را به خاطر بسپارید - دانستن اینکه چه چیزی ممکن است و کجا می توانید اسناد را پیدا کنید کافی است. با اصول اولیه شروع کنید: متغیرها، شرطی ها، حلقه ها، لوله ها. سپس ابزارهای پردازش متن (grep، sed، awk) را در صورت نیاز اضافه کنید. استفاده از`set -euo pipefail`برای نوشتن اسکریپت های قوی توصیه می شود.