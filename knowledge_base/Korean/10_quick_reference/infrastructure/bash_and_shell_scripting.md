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

# Bash 및 쉘 스크립팅 치트 시트
대부분의 Linux 및 macOS 시스템의 기본 셸인 Bash에서 셸 스크립트를 작성하기 위한 실용적인 참조입니다. 구문, 일반적인 패턴, 텍스트 처리 및 유용한 한 줄짜리 내용을 다룹니다.
---

## 스크립트 구조
모든 Bash 스크립트는 **shebang** 줄로 시작합니다.
```bash
#!/usr/bin/env bash
set -euo pipefail   # Safe defaults
```

| 플래그 | 효과 |
|------|---------|
| `set -e`| 명령이 실패하면 즉시 종료 |
| `set -u`| 설정되지 않은 변수를 오류로 처리 |
| `set -o pipefail`| 파이프라인의 명령이 실패하면 파이프라인이 실패합니다. |
| `set -x`| 실행하기 전에 각 명령을 인쇄합니다(디버그 모드) |
스크립트 실행:`chmod +x script.sh && ./script.sh`또는 `bash script.sh`
---

## 변수
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

## 특수 변수
| 변수 | 의미 |
|------------|---------|
| `$0`| 스크립트 이름 |
| `$1`,`$2`, ... | 위치 인수 |
| `$#`| 위치 인수 수 |
| `$@`| 모든 위치 인수(별도의 단어로) |
| `$*`| 모든 위치 인수(단일 문자열) |
| `$?`| 마지막 명령의 종료 상태(0 = 성공) |
| `$$`| 현재 프로세스의 PID |
| `$!`| 마지막 백그라운드 프로세스의 PID |
| `$_`| 이전 명령의 마지막 인수 |
---

## 조건부
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

### 테스트 연산자
| 테스트 | 의미 |
|------|---------|
| `[[ -f "$x" ]]`| 파일이 존재하며 일반 파일입니다 |
| `[[ -d "$x" ]]`| 디렉토리가 존재합니다 |
| `[[ -e "$x" ]]`| 파일/디렉토리가 존재합니다(무엇이든) |
| `[[ -r "$x" ]]`| 읽기 가능 |
| `[[ -w "$x" ]]`| 쓰기 가능 |
| `[[ -x "$x" ]]`| 실행 가능 |
| `[[ -z "$x" ]]`| 문자열이 비어 있습니다 |
| `[[ -n "$x" ]]`| 문자열이 비어 있지 않습니다 |
| `[[ "$a" == "$b" ]]`| 문자열 평등 |
| `[[ "$a" != "$b" ]]`| 문자열 불평등 |
| `[[ "$a" =~ regex ]]`| 정규식 일치 |
| `[[ $a -eq $b ]]`| 정수 평등 |
| `[[ $a -ne $b ]]`| 정수 부등식 |
| `[[ $a -gt $b ]]`| 보다 큼 |
| `[[ $a -lt $b ]]`| 미만 |
| `[[ $a -ge $b ]]`| 이상 |
| `[[ $a -le $b ]]`| 작거나 같음 |
### 논리 연산자
```bash
[[ -f "$a" && -f "$b" ]]   # AND
[[ -f "$a" || -f "$b" ]]   # OR
[[ ! -f "$a" ]]             # NOT
```

---

## 루프
### 루프용
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

### while 루프
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

### 루프까지
```bash
until [[ -f /tmp/ready ]]; do
    echo "Waiting..."
    sleep 1
done
```

---

## 기능
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

## 문자열 작업
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

## 배열
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

## 파이핑 및 리디렉션
| 구문 | 의미 |
|---------|---------|
| `cmd > file`| stdout을 파일로 리디렉션(덮어쓰기) |
| `cmd >> file`| stdout을 파일로 리디렉션(추가) |
| `cmd 2> errors.log`| 표준 오류 리디렉션 |
| `cmd &> all.log`| stdout 및 stderr 모두 리디렉션 |
| `cmd1 \| cmd2`| cmd1의 stdout을 cmd2의 stdin으로 파이프 |
| `cmd1 \|& cmd2`| stdout과 stderr 모두 파이프 |
| `cmd < file`| 파일을 stdin으로 리디렉션 |
| `cmd <<EOF ... EOF`| 여기 문서(여러 줄 입력) |
| `cmd <<< "string"`| Here-string(한 줄 입력) |
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

## 텍스트 처리
### 자르다
```bash
echo "a,b,c" | cut -d',' -f2        # b (field 2, comma-delimited)
echo "hello world" | cut -c1-5      # hello (characters 1-5)
cut -d':' -f1 /etc/passwd           # First field (usernames)
```

### 종류
```bash
sort file.txt                       # Alphabetical sort
sort -n numbers.txt                 # Numeric sort
sort -r file.txt                    # Reverse sort
sort -t',' -k2 file.csv             # Sort by 2nd field, comma-delimited
sort -u file.txt                    # Sort and remove duplicates
```

### 유니크
```bash
sort names.txt | uniq               # Remove consecutive duplicates (sort first!)
sort names.txt | uniq -c            # Count occurrences
sort names.txt | uniq -d            # Show only duplicated lines
```

### 어이
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

## 유용한 한 줄짜리 설명
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

## 스크립팅 패턴
### 인수 구문 분석
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

### 오류 처리
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

### 종속성 확인
```bash
for cmd in git docker python3; do
    if ! command -v "$cmd" &>/dev/null; then
        echo "Error: $cmd is not installed" >&2
        exit 1
    fi
done
```

### 임시 파일
```bash
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
echo "working..." > "$TMPFILE"
```

---

## 요약
Bash 스크립팅은 컴퓨터로 작업하는 모든 사람의 생산성을 높여줍니다. 모든 플래그를 외울 필요는 없습니다. 무엇이 가능한지, 어디서 문서를 찾을 수 있는지 아는 것만으로도 충분합니다. 변수, 조건부, 루프, 파이프 등 기본 사항부터 시작하세요. 그런 다음 필요에 따라 텍스트 처리 도구(grep, sed, awk)를 추가합니다. 강력한 스크립트를 작성하려면 `set -euo pipefail`를 사용하는 것이 좋습니다.