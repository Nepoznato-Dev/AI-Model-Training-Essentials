---
# Metadata
title: "Shell & PowerShell — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Shell/Bash and PowerShell with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [shell, bash, powershell, common-mistakes, anti-patterns, pitfalls, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Shell e PowerShell: errori comuni e anti-pattern
Questo documento cataloga gli errori, le trappole e gli anti-pattern più comuni in Shell/Bash e PowerShell con le correzioni.
---

## 1. Variabili senza virgolette (Bash)
```bash
# ❌ WRONG — word splitting and globbing
file="my file.txt"
cat $file  # tries: cat "my" "file.txt"

# ✅ CORRECT — always quote variables
cat "$file"
```

---

## 2.`[ ]`contro`[[ ]]`(Bash)
```bash
# ❌ WRONG — [ ] doesn't handle empty variables
name=""
if [ $name = "Alice" ]; then  # syntax error!
    echo "Hello"
fi

# ✅ CORRECT — [[ ]] is safer
if [[ $name = "Alice" ]]; then
    echo "Hello"
fi
```

---

## 3.`=`contro`-eq`(Bash)
```bash
# ❌ WRONG — string comparison for numbers
if [ $x = 5 ]; then  # works but semantically wrong

# ✅ CORRECT — numeric comparison
if [[ $x -eq 5 ]]; then
    echo "x is 5"
fi
```

---

## 4. Non controllare i codici di uscita (Bash)
```bash
# ❌ WRONG — ignoring failures
rm /important/file
cp backup /important/file  # runs even if rm failed!

# ✅ CORRECT — check exit codes
set -euo pipefail  # exit on error, undefined vars, pipe failures
rm /important/file || { echo "Failed"; exit 1; }
```

---

## 5. PowerShell: interpolazione di stringhe
```powershell
# ❌ WRONG — single quotes don't interpolate
$name = "Alice"
Write-Host 'Hello $name'  # prints: Hello $name

# ✅ CORRECT — double quotes for interpolation
Write-Host "Hello $name"  # prints: Hello Alice
```

---

## 6. PowerShell:`==`contro `-eq`
```powershell
# ❌ WRONG — == is not PowerShell comparison
if ($x == 5) { }  # syntax error!

# ✅ CORRECT — use -eq, -ne, -gt, -lt
if ($x -eq 5) { Write-Host "x is 5" }
```

---

## 7. Ambito variabile della subshell (Bash)
```bash
# ❌ WRONG — pipe creates subshell
count=0
echo "hello" | while read line; do
    count=$((count + 1))
done
echo $count  # still 0! (subshell modification lost)

# ✅ CORRECT — use process substitution
count=0
while read line; do
    count=$((count + 1))
done < <(echo "hello")
echo $count  # 1
```

---

## 8. PowerShell: oggetti pipeline e stringhe
```powershell
# ❌ WRONG — treating pipeline objects as strings
Get-Process | Where-Object { $_ -match "chrome" }
# $_ is a Process object, not string

# ✅ CORRECT — access properties
Get-Process | Where-Object { $_.ProcessName -match "chrome" }
```

---

## Riepilogo
Trappole nello scripting della shell: citare sempre le variabili in Bash, utilizzare`[[ ]]`su`[ ]`, utilizzare`set -euo pipefail`, controllare i codici di uscita e comprendere l'ambito della subshell. Trappole di PowerShell: utilizzare virgolette doppie per l'interpolazione, utilizzare`-eq`non`==`e ricordare che gli oggetti pipeline hanno proprietà. Entrambi premiano la citazione attenta e la gestione esplicita degli errori.