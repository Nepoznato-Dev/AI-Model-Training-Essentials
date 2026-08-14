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

# ব্যাশ এবং শেল স্ক্রিপ্টিং চিট শীট
Bash-এ শেল স্ক্রিপ্ট লেখার জন্য একটি ব্যবহারিক রেফারেন্স — বেশিরভাগ Linux এবং macOS সিস্টেমে ডিফল্ট শেল। সিনট্যাক্স, সাধারণ নিদর্শন, পাঠ্য প্রক্রিয়াকরণ এবং দরকারী ওয়ান-লাইনার কভার করে।
---

## স্ক্রিপ্ট স্ট্রাকচার
প্রতিটি ব্যাশ স্ক্রিপ্ট একটি **শেবাং** লাইন দিয়ে শুরু হয়:
```bash
#!/usr/bin/env bash
set -euo pipefail   # Safe defaults
```

| পতাকা | প্রভাব |
|------|---------|
| `set -e`| একটি কমান্ড ব্যর্থ হলে অবিলম্বে প্রস্থান করুন |
| `set -u`| আনসেট ভেরিয়েবলকে ত্রুটি হিসাবে বিবেচনা করুন |
| `set -o pipefail`| এতে কোনো কমান্ড ব্যর্থ হলে পাইপলাইন ব্যর্থ হয় |
| `set -x`| এক্সিকিউট করার আগে প্রতিটি কমান্ড প্রিন্ট করুন (ডিবাগ মোড) |
একটি স্ক্রিপ্ট চালান:`chmod +x script.sh && ./script.sh`বা `bash script.sh`৷
---

## ভেরিয়েবল
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

## বিশেষ ভেরিয়েবল
| পরিবর্তনশীল | অর্থ |
|----------|---------|
| `$0`| স্ক্রিপ্ট নাম |
| `$1`,`$2`, ... | অবস্থানগত যুক্তি |
| `$#`| অবস্থানগত আর্গুমেন্টের সংখ্যা |
| `$@`| সমস্ত অবস্থানগত যুক্তি (আলাদা শব্দ হিসাবে) |
| `$*`| সমস্ত অবস্থানগত আর্গুমেন্ট (একটি স্ট্রিং হিসাবে) |
| `$?`| শেষ কমান্ডের প্রস্থান অবস্থা (0 = সাফল্য) |
| `$$`| বর্তমান প্রক্রিয়ার PID |
| `$!`| শেষ পটভূমি প্রক্রিয়ার PID |
| `$_`| পূর্ববর্তী কমান্ডের শেষ যুক্তি |
---

## শর্তাবলী
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

### টেস্ট অপারেটর
| পরীক্ষা | অর্থ |
|------|---------|
| `[[ -f "$x" ]]`| ফাইল বিদ্যমান এবং একটি নিয়মিত ফাইল |
| `[[ -d "$x" ]]`| ডিরেক্টরি বিদ্যমান |
| `[[ -e "$x" ]]`| ফাইল/ডিরেক্টরি বিদ্যমান (যেকোনো কিছু) |
| `[[ -r "$x" ]]`| পঠনযোগ্য |
| `[[ -w "$x" ]]`| লেখার যোগ্য |
| `[[ -x "$x" ]]`| এক্সিকিউটেবল |
| `[[ -z "$x" ]]`| স্ট্রিং খালি |
| `[[ -n "$x" ]]`| স্ট্রিং খালি নয় |
| `[[ "$a" == "$b" ]]`| স্ট্রিং সমতা |
| `[[ "$a" != "$b" ]]`| স্ট্রিং অসমতা |
| `[[ "$a" =~ regex ]]`| Regex ম্যাচ |
| `[[ $a -eq $b ]]`| পূর্ণসংখ্যা সমতা |
| `[[ $a -ne $b ]]`| পূর্ণসংখ্যা অসমতা |
| `[[ $a -gt $b ]]`| এর চেয়ে বড় |
| `[[ $a -lt $b ]]`| কম |
| `[[ $a -ge $b ]]`| এর চেয়ে বড় বা সমান |
| `[[ $a -le $b ]]`| কম বা সমান |
### লজিক্যাল অপারেটর
```bash
[[ -f "$a" && -f "$b" ]]   # AND
[[ -f "$a" || -f "$b" ]]   # OR
[[ ! -f "$a" ]]             # NOT
```

---

## লুপ
### লুপের জন্য
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

### যখন লুপ
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

### লুপ পর্যন্ত
```bash
until [[ -f /tmp/ready ]]; do
    echo "Waiting..."
    sleep 1
done
```

---

## ফাংশন
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

## স্ট্রিং অপারেশন
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

## অ্যারে
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

## পাইপিং এবং পুনঃনির্দেশ
| সিনট্যাক্স | অর্থ |
|---------|---------|
| `cmd > file`| stdout ফাইলে পুনঃনির্দেশিত করুন (ওভাররাইট) |
| `cmd >> file`| stdout ফাইলে পুনঃনির্দেশিত (সংযোজন) |
| `cmd 2> errors.log`| পুনঃনির্দেশ stderr |
| `cmd &> all.log`| stdout এবং stderr | উভয়ই রিডাইরেক্ট করুন
| `cmd1 \| cmd2`| cmd1 এর পাইপ stdout থেকে cmd2 এর stdin |
| `cmd1 \|& cmd2`| stdout এবং stderr উভয়ই পাইপ |
| `cmd < file`| ফাইলকে stdin এ রিডাইরেক্ট করুন |
| `cmd <<EOF ... EOF`| এখানে-নথি (মাল্টি-লাইন ইনপুট) |
| `cmd <<< "string"`| এখানে-স্ট্রিং (একক-লাইন ইনপুট) |
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

## টেক্সট প্রসেসিং
### কাটা
```bash
echo "a,b,c" | cut -d',' -f2        # b (field 2, comma-delimited)
echo "hello world" | cut -c1-5      # hello (characters 1-5)
cut -d':' -f1 /etc/passwd           # First field (usernames)
```

### সাজান
```bash
sort file.txt                       # Alphabetical sort
sort -n numbers.txt                 # Numeric sort
sort -r file.txt                    # Reverse sort
sort -t',' -k2 file.csv             # Sort by 2nd field, comma-delimited
sort -u file.txt                    # Sort and remove duplicates
```

### ইউনিক
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

### সেড
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

### গ্রেপ
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

## দরকারী ওয়ান-লাইনার
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

## স্ক্রিপ্টিং প্যাটার্ন
### আর্গুমেন্ট পার্সিং
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

### ত্রুটি হ্যান্ডলিং
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

### নির্ভরতা পরীক্ষা করা হচ্ছে
```bash
for cmd in git docker python3; do
    if ! command -v "$cmd" &>/dev/null; then
        echo "Error: $cmd is not installed" >&2
        exit 1
    fi
done
```

### অস্থায়ী ফাইল
```bash
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
echo "working..." > "$TMPFILE"
```

---

## সারাংশ
ব্যাশ স্ক্রিপ্টিং যারা কম্পিউটারের সাথে কাজ করে তাদের জন্য উত্পাদনশীলতা বাড়ায়। প্রতিটি পতাকা মুখস্থ করার প্রয়োজন নেই - কী সম্ভব এবং কোথায় ডকুমেন্টেশন খুঁজে পাওয়া যায় তা জানা যথেষ্ট। বেসিক দিয়ে শুরু করুন: ভেরিয়েবল, কন্ডিশনাল, লুপ, পাইপ। তারপর প্রয়োজন অনুযায়ী টেক্সট প্রসেসিং টুলস (grep, sed, awk) যোগ করুন। শক্তিশালী স্ক্রিপ্ট লেখার জন্য`set -euo pipefail`ব্যবহার করার পরামর্শ দেওয়া হয়।