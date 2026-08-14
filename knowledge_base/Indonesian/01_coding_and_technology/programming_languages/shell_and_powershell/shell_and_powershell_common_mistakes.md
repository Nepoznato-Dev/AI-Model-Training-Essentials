---
# Metadata
title: "Shell & PowerShell — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Shell/Bash and PowerShell with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Shell & PowerShell — Kesalahan Umum & Anti-Pola
Dokumen ini mengkatalogkan kesalahan, jebakan, dan anti-pola paling umum di Shell/Bash dan PowerShell beserta koreksinya.
---

## 1. Variabel Tanpa Kutipan (Bash)
```bash
# ❌ WRONG — word splitting and globbing
file="my file.txt"
cat $file  # tries: cat "my" "file.txt"

# ✅ CORRECT — always quote variables
cat "$file"
```

---

## 2.`[ ]`vs`[[ ]]`(Bash)
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

## 3.`=`vs`-eq`(Bash)
```bash
# ❌ WRONG — string comparison for numbers
if [ $x = 5 ]; then  # works but semantically wrong

# ✅ CORRECT — numeric comparison
if [[ $x -eq 5 ]]; then
    echo "x is 5"
fi
```

---

## 4. Tidak Memeriksa Kode Keluar (Bash)
```bash
# ❌ WRONG — ignoring failures
rm /important/file
cp backup /important/file  # runs even if rm failed!

# ✅ CORRECT — check exit codes
set -euo pipefail  # exit on error, undefined vars, pipe failures
rm /important/file || { echo "Failed"; exit 1; }
```

---

## 5. PowerShell: Interpolasi String
```powershell
# ❌ WRONG — single quotes don't interpolate
$name = "Alice"
Write-Host 'Hello $name'  # prints: Hello $name

# ✅ CORRECT — double quotes for interpolation
Write-Host "Hello $name"  # prints: Hello Alice
```

---

## 6. PowerShell:`==`vs `-eq`
```powershell
# ❌ WRONG — == is not PowerShell comparison
if ($x == 5) { }  # syntax error!

# ✅ CORRECT — use -eq, -ne, -gt, -lt
if ($x -eq 5) { Write-Host "x is 5" }
```

---

## 7. Lingkup Variabel Subkulit (Bash)
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

## 8. PowerShell: Objek Pipa vs String
```powershell
# ❌ WRONG — treating pipeline objects as strings
Get-Process | Where-Object { $_ -match "chrome" }
# $_ is a Process object, not string

# ✅ CORRECT — access properties
Get-Process | Where-Object { $_.ProcessName -match "chrome" }
```

---

## Ringkasan
Perangkap skrip shell: selalu mengutip variabel di Bash, gunakan`[[ ]]`di atas`[ ]`, gunakan`set -euo pipefail`, periksa kode keluar, dan pahami pelingkupan subkulit. Perangkap PowerShell: gunakan tanda kutip ganda untuk interpolasi, gunakan`-eq`bukan`==`, dan ingat objek pipa memiliki properti. Keduanya menghargai kutipan yang cermat dan penanganan kesalahan yang eksplisit.