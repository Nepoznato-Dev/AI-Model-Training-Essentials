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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# Bash at Shell Scripting Cheat Sheet
Isang praktikal na sanggunian para sa pagsusulat ng mga script ng shell sa Bash — ang default na shell sa karamihan ng mga Linux at macOS system. Sinasaklaw ang syntax, karaniwang mga pattern, pagpoproseso ng text, at mga kapaki-pakinabang na one-liner.
---

## Istraktura ng Script
Ang bawat Bash script ay nagsisimula sa isang **shebang** na linya:
```bash
#!/usr/bin/env bash
set -euo pipefail   # Safe defaults
```

| Bandila | Epekto |
|------|--------|
| `set -e`| Lumabas kaagad kung ang isang utos ay nabigo |
| `set -u`| Tratuhin ang mga hindi nakatakdang variable bilang mga error |
| `set -o pipefail`| Nabigo ang pipeline kung ang anumang utos dito ay nabigo |
| `set -x`| I-print ang bawat command bago isagawa (debug mode) |
Magpatakbo ng script:`chmod +x script.sh && ./script.sh`o `bash script.sh`
---

## Mga variable
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

## Mga Espesyal na Variable
| Variable | Ibig sabihin |
|----------|---------|
| `$0`| Pangalan ng script |
| `$1`,`$2`, ... | Mga posisyong argumento |
| `$#`| Bilang ng mga positional na argumento |
| `$@`| Lahat ng positional na argumento (bilang magkahiwalay na salita) |
| `$*`| Lahat ng positional na argumento (bilang isang string) |
| `$?`| Exit status ng huling command (0 = success) |
| `$$`| PID ng kasalukuyang proseso |
| `$!`| PID ng huling proseso sa background |
| `$_`| Huling argumento ng nakaraang utos |
---

## Mga kondisyon
### kung / elif / iba pa
```bash
if [[ -f "$FILE" ]]; then
    echo "File exists"
elif [[ -d "$FILE" ]]; then
    echo "It's a directory"
else
    echo "Not found"
fi
```

### Mga Operator ng Pagsubok
| Pagsubok | Ibig sabihin |
|------|---------|
| `[[ -f "$x" ]]`| Ang file ay umiiral at ito ay isang regular na file |
| `[[ -d "$x" ]]`| Mayroong direktoryo |
| `[[ -e "$x" ]]`| Umiiral ang file/direktoryo (kahit ano) |
| `[[ -r "$x" ]]`| Nababasa |
| `[[ -w "$x" ]]`| Naisusulat |
| `[[ -x "$x" ]]`| Maipapatupad |
| `[[ -z "$x" ]]`| Walang laman ang string |
| `[[ -n "$x" ]]`| Walang laman ang string |
| `[[ "$a" == "$b" ]]`| Pagkakapantay-pantay ng string |
| `[[ "$a" != "$b" ]]`| Hindi pagkakapantay-pantay ng string |
| `[[ "$a" =~ regex ]]`| Regex match |
| `[[ $a -eq $b ]]`| Integer equality |
| `[[ $a -ne $b ]]`| Integer inequality |
| `[[ $a -gt $b ]]`| Higit sa |
| `[[ $a -lt $b ]]`| Mas mababa sa |
| `[[ $a -ge $b ]]`| Higit sa o katumbas ng |
| `[[ $a -le $b ]]`| Mas mababa sa o katumbas |
### Mga Lohikal na Operator
```bash
[[ -f "$a" && -f "$b" ]]   # AND
[[ -f "$a" || -f "$b" ]]   # OR
[[ ! -f "$a" ]]             # NOT
```

---

## Mga loop
### para sa Loop
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

### habang Loop
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

### hanggang Loop
```bash
until [[ -f /tmp/ready ]]; do
    echo "Waiting..."
    sleep 1
done
```

---

## Mga Pag-andar
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

## Mga Pagpapatakbo ng String
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

## Mga array
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

## Piping at Pag-redirect
| Syntax | Ibig sabihin |
|--------|---------|
| `cmd > file`| I-redirect ang stdout sa file (overwrite) |
| `cmd >> file`| I-redirect ang stdout sa file (idagdag) |
| `cmd 2> errors.log`| I-redirect ang stderr |
| `cmd &> all.log`| I-redirect ang parehong stdout at stderr |
| `cmd1 \| cmd2`| Pipe stdout ng cmd1 hanggang stdin ng cmd2 |
| `cmd1 \|& cmd2`| Pipe ang parehong stdout at stderr |
| `cmd < file`| I-redirect ang file sa stdin |
| `cmd <<EOF ... EOF`| Dito-dokumento (multi-line input) |
| `cmd <<< "string"`| Here-string (single-line input) |
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

## Pagproseso ng Teksto
### hiwa
```bash
echo "a,b,c" | cut -d',' -f2        # b (field 2, comma-delimited)
echo "hello world" | cut -c1-5      # hello (characters 1-5)
cut -d':' -f1 /etc/passwd           # First field (usernames)
```

### uri
```bash
sort file.txt                       # Alphabetical sort
sort -n numbers.txt                 # Numeric sort
sort -r file.txt                    # Reverse sort
sort -t',' -k2 file.csv             # Sort by 2nd field, comma-delimited
sort -u file.txt                    # Sort and remove duplicates
```

### uniq
```bash
sort names.txt | uniq               # Remove consecutive duplicates (sort first!)
sort names.txt | uniq -c            # Count occurrences
sort names.txt | uniq -d            # Show only duplicated lines
```

### awk
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

## Mga Kapaki-pakinabang na One-Liner
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

## Mga Pattern ng Scripting
### Pag-parse ng Argumento
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

### Error sa Paghawak
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

### Sinusuri ang Dependencies
```bash
for cmd in git docker python3; do
    if ! command -v "$cmd" &>/dev/null; then
        echo "Error: $cmd is not installed" >&2
        exit 1
    fi
done
```

### Mga Pansamantalang File
```bash
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
echo "working..." > "$TMPFILE"
```

---

## Buod
Ang Bash scripting ay nagpapataas ng pagiging produktibo para sa sinumang nagtatrabaho sa mga computer. Hindi kailangang isaulo ang bawat bandila — sapat na ang pag-alam kung ano ang posible at kung saan mahahanap ang dokumentasyon. Magsimula sa mga pangunahing kaalaman: mga variable, conditional, loops, pipes. Pagkatapos ay magdagdag ng mga tool sa pagpoproseso ng teksto (grep, sed, awk) kung kinakailangan. Ang paggamit ng`set -euo pipefail`ay inirerekomenda para sa pagsusulat ng matatag na mga script.