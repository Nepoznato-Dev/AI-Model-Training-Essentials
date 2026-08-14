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

# Shell & PowerShell — Các lỗi thường gặp & Mẫu chống đối
Tài liệu này liệt kê các lỗi, bẫy và mô hình chống phổ biến nhất trong Shell/Bash và PowerShell kèm theo các bản sửa lỗi.
---

## 1. Biến không trích dẫn (Bash)
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

## 4. Không kiểm tra mã thoát (Bash)
```bash
# ❌ WRONG — ignoring failures
rm /important/file
cp backup /important/file  # runs even if rm failed!

# ✅ CORRECT — check exit codes
set -euo pipefail  # exit on error, undefined vars, pipe failures
rm /important/file || { echo "Failed"; exit 1; }
```

---

## 5. PowerShell: Nội suy chuỗi
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

## 7. Phạm vi biến Subshell (Bash)
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

## 8. PowerShell: Đối tượng đường ống và chuỗi
```powershell
# ❌ WRONG — treating pipeline objects as strings
Get-Process | Where-Object { $_ -match "chrome" }
# $_ is a Process object, not string

# ✅ CORRECT — access properties
Get-Process | Where-Object { $_.ProcessName -match "chrome" }
```

---

## Bản tóm tắt
Bẫy kịch bản shell: luôn trích dẫn các biến trong Bash, sử dụng`[[ ]]`trên`[ ]`, sử dụng`set -euo pipefail`, kiểm tra mã thoát và hiểu phạm vi của shell con. Bẫy PowerShell: sử dụng dấu ngoặc kép để nội suy, sử dụng`-eq`không phải`==`và nhớ các đối tượng đường ống có thuộc tính. Cả hai đều khen thưởng việc trích dẫn cẩn thận và xử lý lỗi rõ ràng.