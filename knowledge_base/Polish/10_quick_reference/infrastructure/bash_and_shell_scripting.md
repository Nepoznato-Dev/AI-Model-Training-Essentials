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
# Ściągawka dotycząca skryptów Bash i Shell
Praktyczny podręcznik dotyczący pisania skryptów powłoki w języku Bash — domyślnej powłoce w większości systemów Linux i macOS. Obejmuje składnię, typowe wzorce, przetwarzanie tekstu i przydatne jednoliniowe.
---

## Struktura skryptu
Każdy skrypt Bash zaczyna się od linii **shebang**:
```bash
#!/usr/bin/env bash
set -euo pipefail   # Safe defaults
```

| Flaga | Efekt |
|------|------------|
| `set -e`| Wyjdź natychmiast, jeśli polecenie nie powiedzie się |
| `set -u`| Traktuj nieustawione zmienne jako błędy |
| `set -o pipefail`| Potok nie działa, jeśli jakiekolwiek polecenie w nim nie powiedzie się |
| `set -x`| Wydrukuj każde polecenie przed wykonaniem (tryb debugowania) |
Uruchom skrypt:`chmod +x script.sh && ./script.sh`lub `bash script.sh`
---

## Zmienne
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

## Zmienne specjalne
| Zmienna | Znaczenie |
|--------------|--------|
| `$0`| Nazwa skryptu |
| `$1`,`$2`, ... | Argumenty pozycyjne |
| `$#`| Liczba argumentów pozycyjnych |
| `$@`| Wszystkie argumenty pozycyjne (jako osobne słowa) |
| `$*`| Wszystkie argumenty pozycyjne (jako pojedynczy ciąg znaków) |
| `$?`| Status wyjścia ostatniego polecenia (0 = sukces) |
| `$$`| PID bieżącego procesu |
| `$!`| PID ostatniego procesu w tle |
| `$_`| Ostatni argument poprzedniego polecenia |
---

## Warunki warunkowe
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

### Operatorzy testowi
| Testuj | Znaczenie |
|------|-------------|
| `[[ -f "$x" ]]`| Plik istnieje i jest zwykłym plikiem |
| `[[ -d "$x" ]]`| Katalog istnieje |
| `[[ -e "$x" ]]`| Plik/katalog istnieje (cokolwiek) |
| `[[ -r "$x" ]]`| Czytelne |
| `[[ -w "$x" ]]`| Zapisywalny |
| `[[ -x "$x" ]]`| Plik wykonywalny |
| `[[ -z "$x" ]]`| Ciąg jest pusty |
| `[[ -n "$x" ]]`| Łańcuch nie jest pusty |
| `[[ "$a" == "$b" ]]`| Równość ciągów |
| `[[ "$a" != "$b" ]]`| Nierówność ciągów |
| `[[ "$a" =~ regex ]]`| Dopasowanie wyrażeń regularnych |
| `[[ $a -eq $b ]]`| Równość całkowita |
| `[[ $a -ne $b ]]`| Nierówność całkowita |
| `[[ $a -gt $b ]]`| Większe niż |
| `[[ $a -lt $b ]]`| Mniej niż |
| `[[ $a -ge $b ]]`| Większe lub równe |
| `[[ $a -le $b ]]`| Mniejsze lub równe |
### Operatory logiczne
```bash
[[ -f "$a" && -f "$b" ]]   # AND
[[ -f "$a" || -f "$b" ]]   # OR
[[ ! -f "$a" ]]             # NOT
```

---

## Pętle
### dla pętli
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

### podczas pętli
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

### aż do pętli
```bash
until [[ -f /tmp/ready ]]; do
    echo "Waiting..."
    sleep 1
done
```

---

## Funkcje
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

## Operacje na ciągach
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

## Tablice
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

## Rurociągi i przekierowania
| Składnia | Znaczenie |
|------------|--------|
| `cmd > file`| Przekieruj standardowe wyjście do pliku (nadpisz) |
| `cmd >> file`| Przekieruj standardowe wyjście do pliku (dołącz) |
| `cmd 2> errors.log`| Przekieruj stderr |
| `cmd &> all.log`| Przekieruj zarówno stdout, jak i stderr |
| `cmd1 \| cmd2`| Potokuj standardowe wyjście z cmd1 do stdin z cmd2 |
| `cmd1 \|& cmd2`| Potok zarówno stdout, jak i stderr |
| `cmd < file`| Przekieruj plik na stdin |
| `cmd <<EOF ... EOF`| Dokument tutaj (wprowadzanie wielowierszowe) |
| `cmd <<< "string"`| Here-string (wejście jednowierszowe) |
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

## Przetwarzanie tekstu
### cięcie
```bash
echo "a,b,c" | cut -d',' -f2        # b (field 2, comma-delimited)
echo "hello world" | cut -c1-5      # hello (characters 1-5)
cut -d':' -f1 /etc/passwd           # First field (usernames)
```

### sortowanie
```bash
sort file.txt                       # Alphabetical sort
sort -n numbers.txt                 # Numeric sort
sort -r file.txt                    # Reverse sort
sort -t',' -k2 file.csv             # Sort by 2nd field, comma-delimited
sort -u file.txt                    # Sort and remove duplicates
```

### wyjątkowy
```bash
sort names.txt | uniq               # Remove consecutive duplicates (sort first!)
sort names.txt | uniq -c            # Count occurrences
sort names.txt | uniq -d            # Show only duplicated lines
```

### ok
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

## Przydatne jednowierszowe
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

## Wzorce skryptowe
### Analiza argumentów
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

### Obsługa błędów
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

### Sprawdzanie zależności
```bash
for cmd in git docker python3; do
    if ! command -v "$cmd" &>/dev/null; then
        echo "Error: $cmd is not installed" >&2
        exit 1
    fi
done
```

### Pliki tymczasowe
```bash
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
echo "working..." > "$TMPFILE"
```

---

## Streszczenie
Skrypty Bash zwiększają produktywność każdego, kto pracuje z komputerami. Nie trzeba zapamiętywać wszystkich flag – wystarczy wiedzieć, co jest możliwe i gdzie znaleźć dokumentację. Zacznij od podstaw: zmienne, warunki, pętle, potoki. Następnie dodaj narzędzia do przetwarzania tekstu (grep, sed, awk) według potrzeb. Do pisania solidnych skryptów zaleca się używanie `set -euo pipefail`.