<!--
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

-->
# শেল এবং পাওয়ারশেল — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্ন
এই ডকুমেন্টটি শেল/ব্যাশ এবং পাওয়ারশেলের সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্ন সংশোধন সহ ক্যাটালগ করে।
---

## 1. উদ্ধৃতিহীন ভেরিয়েবল (ব্যাশ)
```bash
# ❌ WRONG — word splitting and globbing
file="my file.txt"
cat $file  # tries: cat "my" "file.txt"

# ✅ CORRECT — always quote variables
cat "$file"
```

---

## 2.`[ ]`বনাম`[[ ]]`(ব্যাশ)
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

## 3.`=`বনাম`-eq`(ব্যাশ)
```bash
# ❌ WRONG — string comparison for numbers
if [ $x = 5 ]; then  # works but semantically wrong

# ✅ CORRECT — numeric comparison
if [[ $x -eq 5 ]]; then
    echo "x is 5"
fi
```

---

## 4. এক্সিট কোড চেক করা হচ্ছে না (ব্যাশ)
```bash
# ❌ WRONG — ignoring failures
rm /important/file
cp backup /important/file  # runs even if rm failed!

# ✅ CORRECT — check exit codes
set -euo pipefail  # exit on error, undefined vars, pipe failures
rm /important/file || { echo "Failed"; exit 1; }
```

---

## 5. পাওয়ারশেল: স্ট্রিং ইন্টারপোলেশন
```powershell
# ❌ WRONG — single quotes don't interpolate
$name = "Alice"
Write-Host 'Hello $name'  # prints: Hello $name

# ✅ CORRECT — double quotes for interpolation
Write-Host "Hello $name"  # prints: Hello Alice
```

---

## 6. পাওয়ারশেল:`==`বনাম `-eq`
```powershell
# ❌ WRONG — == is not PowerShell comparison
if ($x == 5) { }  # syntax error!

# ✅ CORRECT — use -eq, -ne, -gt, -lt
if ($x -eq 5) { Write-Host "x is 5" }
```

---

## 7. সাবশেল ভেরিয়েবল স্কোপ (ব্যাশ)
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

## 8. পাওয়ারশেল: পাইপলাইন অবজেক্ট বনাম স্ট্রিংস
```powershell
# ❌ WRONG — treating pipeline objects as strings
Get-Process | Where-Object { $_ -match "chrome" }
# $_ is a Process object, not string

# ✅ CORRECT — access properties
Get-Process | Where-Object { $_.ProcessName -match "chrome" }
```

---

## সারাংশ
শেল স্ক্রিপ্টিং ফাঁদ: সর্বদা ব্যাশে ভেরিয়েবল উদ্ধৃত করুন,`[ ]`এর উপর`[[ ]]`ব্যবহার করুন,`set -euo pipefail`ব্যবহার করুন, প্রস্থান কোড পরীক্ষা করুন এবং সাবশেল স্কোপিং বোঝুন। পাওয়ারশেল ফাঁদ: ইন্টারপোলেশনের জন্য ডবল উদ্ধৃতি ব্যবহার করুন,`-eq`ব্যবহার করুন`==`নয়, এবং মনে রাখবেন পাইপলাইন বস্তুর বৈশিষ্ট্য রয়েছে। সাবধানে উদ্ধৃতি এবং স্পষ্ট ত্রুটি পরিচালনা উভয়ই পুরস্কৃত করে।