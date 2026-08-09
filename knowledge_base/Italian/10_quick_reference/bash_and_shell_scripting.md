---
# Metadata
title: "Bash and Shell Scripting Cheat Sheet"
description: "Bash scripting, text processing, useful one-liners"
category: "Quick Reference"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
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

# Foglio informativo di Bash e Shell Scripting
Un riferimento pratico per scrivere script di shell in Bash, la shell predefinita sulla maggior parte dei sistemi Linux e macOS. Copre la sintassi, i modelli comuni, l'elaborazione del testo e le battute utili.
---

## Struttura dello script
Ogni script Bash inizia con una riga **shebang**:
```bash
#!/usr/bin/env bash
set -euo pipefail   # Safe defaults
```

| Bandiera | Effetto |
|------|--------|
| `set -e`| Esce immediatamente se un comando fallisce |
| `set -u`| Tratta le variabili non impostate come errori |
| `set -o pipefail`| La pipeline fallisce se qualsiasi comando al suo interno fallisce |
| `set -x`| Stampa ogni comando prima di eseguirlo (modalità debug) |
Esegui uno script:`chmod +x script.sh && ./script.sh`o `bash script.sh`
---

## Variabili
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

## Variabili speciali
| Variabile | Significato |
|----------|---------|
| `$0`| Nome dello script |
| `$1`,`$2`, ... | Argomenti posizionali |
| `$#`| Numero di argomenti posizionali |
| `$@`| Tutti gli argomenti posizionali (come parole separate) |
| `$*`| Tutti gli argomenti posizionali (come una singola stringa) |
| `$?`| Stato di uscita dell'ultimo comando (0 = successo) |
| `$$`| PID del processo corrente |
| `$!`| PID dell'ultimo processo in background |
| `$_`| Ultimo argomento del comando precedente |
---

## Condizionali
### if /elif/else
```bash
if [[ -f "$FILE" ]]; then
    echo "File exists"
elif [[ -d "$FILE" ]]; then
    echo "It's a directory"
else
    echo "Not found"
fi
```

### Operatori di prova
| Prova | Significato |
|------|---------|
| `[[ -f "$x" ]]`| Il file esiste ed è un file normale |
| `[[ -d "$x" ]]`| La directory esiste |
| `[[ -e "$x" ]]`| Il file/directory esiste (qualsiasi cosa) |
| `[[ -r "$x" ]]`| Leggibile |
| `[[ -w "$x" ]]`| Scrivibile |
| `[[ -x "$x" ]]`| Eseguibile |
| `[[ -z "$x" ]]`| La stringa è vuota |
| `[[ -n "$x" ]]`| La stringa non è vuota |
| `[[ "$a" == "$b" ]]`| Uguaglianza delle stringhe |
| `[[ "$a" != "$b" ]]`| Disuguaglianza delle stringhe |
| `[[ "$a" =~ regex ]]`| Corrispondenza regex |
| `[[ $a -eq $b ]]`| Uguaglianza intera |
| `[[ $a -ne $b ]]`| Disuguaglianza intera |
| `[[ $a -gt $b ]]`| Maggiore di |
| `[[ $a -lt $b ]]`| Meno di |
| `[[ $a -ge $b ]]`| Maggiore o uguale |
| `[[ $a -le $b ]]`| Minore o uguale |
### Operatori logici
```bash
[[ -f "$a" && -f "$b" ]]   # AND
[[ -f "$a" || -f "$b" ]]   # OR
[[ ! -f "$a" ]]             # NOT
```

---

## Loop
### per Ciclo
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

### mentre Ciclo
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

### fino al ciclo
```bash
until [[ -f /tmp/ready ]]; do
    echo "Waiting..."
    sleep 1
done
```

---

## Funzioni
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

## Operazioni sulle stringhe
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

## Array
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

## Tubazioni e reindirizzamento
| Sintassi | Significato |
|--------|---------|
| `cmd > file`| Reindirizzare stdout al file (sovrascrivere) |
| `cmd >> file`| Reindirizzare stdout al file (aggiungere) |
| `cmd 2> errors.log`| Reindirizzare stderr |
| `cmd &> all.log`| Reindirizza sia stdout che stderr |
| `cmd1 \| cmd2`| Invia lo stdout di cmd1 allo stdin di cmd2 |
| `cmd1 \|& cmd2`| Pipe sia stdout che stderr |
| `cmd < file`| Reindirizzare il file su stdin |
| `cmd <<EOF ... EOF`| Here-document (input su più righe) |
| `cmd <<< "string"`| Here-string (input su riga singola) |
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

## Elaborazione del testo
### taglio
```bash
echo "a,b,c" | cut -d',' -f2        # b (field 2, comma-delimited)
echo "hello world" | cut -c1-5      # hello (characters 1-5)
cut -d':' -f1 /etc/passwd           # First field (usernames)
```

### ordinare
```bash
sort file.txt                       # Alphabetical sort
sort -n numbers.txt                 # Numeric sort
sort -r file.txt                    # Reverse sort
sort -t',' -k2 file.csv             # Sort by 2nd field, comma-delimited
sort -u file.txt                    # Sort and remove duplicates
```

### unico
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

###sed
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

###grep
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

## Linee guida utili
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

## Modelli di script
### Analisi degli argomenti
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

### Gestione degli errori
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

### Controllo delle dipendenze
```bash
for cmd in git docker python3; do
    if ! command -v "$cmd" &>/dev/null; then
        echo "Error: $cmd is not installed" >&2
        exit 1
    fi
done
```

### File temporanei
```bash
TMPFILE=$(mktemp)
trap 'rm -f "$TMPFILE"' EXIT
echo "working..." > "$TMPFILE"
```

---

## Riepilogo
Lo scripting Bash è un moltiplicatore di forza per chiunque lavori con i computer. Non è necessario memorizzare ogni flag: è necessario sapere cosa è possibile fare e dove cercarlo. Inizia dalle basi: variabili, condizionali, loop, pipe. Quindi sovrapponi gli strumenti di elaborazione del testo (grep, sed, awk) quando ne hai bisogno. E usa sempre `set -euo pipefail`: in futuro te ne sarai grato.