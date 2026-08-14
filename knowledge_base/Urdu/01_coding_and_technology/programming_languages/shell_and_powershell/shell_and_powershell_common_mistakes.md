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

# شیل اور پاور شیل - عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز شیل/باش اور پاور شیل میں سب سے عام غلطیوں، ٹریپس، اور اینٹی پیٹرن کو تصحیح کے ساتھ کیٹلاگ کرتا ہے۔
---

## 1. غیر نقل شدہ متغیرات (بش)
```bash
# ❌ WRONG — word splitting and globbing
file="my file.txt"
cat $file  # tries: cat "my" "file.txt"

# ✅ CORRECT — always quote variables
cat "$file"
```

---

## 2.`[ ]`بمقابلہ`[[ ]]`(باش)
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

## 3.`=`بمقابلہ`-eq`(باش)
```bash
# ❌ WRONG — string comparison for numbers
if [ $x = 5 ]; then  # works but semantically wrong

# ✅ CORRECT — numeric comparison
if [[ $x -eq 5 ]]; then
    echo "x is 5"
fi
```

---

## 4. ایگزٹ کوڈز کی جانچ نہیں کرنا (باش)
```bash
# ❌ WRONG — ignoring failures
rm /important/file
cp backup /important/file  # runs even if rm failed!

# ✅ CORRECT — check exit codes
set -euo pipefail  # exit on error, undefined vars, pipe failures
rm /important/file || { echo "Failed"; exit 1; }
```

---

## 5. پاور شیل: سٹرنگ انٹرپولیشن
```powershell
# ❌ WRONG — single quotes don't interpolate
$name = "Alice"
Write-Host 'Hello $name'  # prints: Hello $name

# ✅ CORRECT — double quotes for interpolation
Write-Host "Hello $name"  # prints: Hello Alice
```

---

## 6. پاور شیل:`==`بمقابلہ `-eq`
```powershell
# ❌ WRONG — == is not PowerShell comparison
if ($x == 5) { }  # syntax error!

# ✅ CORRECT — use -eq, -ne, -gt, -lt
if ($x -eq 5) { Write-Host "x is 5" }
```

---

## 7. سب شیل ویری ایبل اسکوپ (باش)
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

## 8. پاور شیل: پائپ لائن آبجیکٹ بمقابلہ سٹرنگز
```powershell
# ❌ WRONG — treating pipeline objects as strings
Get-Process | Where-Object { $_ -match "chrome" }
# $_ is a Process object, not string

# ✅ CORRECT — access properties
Get-Process | Where-Object { $_.ProcessName -match "chrome" }
```

---

## خلاصہ
شیل اسکرپٹنگ ٹریپس: ہمیشہ باش میں متغیرات کا حوالہ دیں،`[[ ]]`پر`[ ]`استعمال کریں،`set -euo pipefail`استعمال کریں، ایگزٹ کوڈز چیک کریں، اور سب شیل اسکوپنگ کو سمجھیں۔ پاور شیل ٹریپس: انٹرپولیشن کے لیے ڈبل کوٹس استعمال کریں،`-eq`استعمال کریں`==`نہیں، اور یاد رکھیں پائپ لائن اشیاء کی خصوصیات ہیں۔ احتیاط سے حوالہ دینے اور واضح غلطی سے نمٹنے دونوں کو انعام دیتے ہیں۔