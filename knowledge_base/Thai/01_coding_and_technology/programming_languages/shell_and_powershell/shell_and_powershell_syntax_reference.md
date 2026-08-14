<!--
---
# Metadata
title: "Shell & PowerShell — Syntax Reference"
description: "Detailed syntax reference for Bash and PowerShell covering scripting, pipelines, process management, automation, and system administration patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [shell, bash, powershell, syntax-reference, scripting, automation, pipelines, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Shell & PowerShell - การอ้างอิงไวยากรณ์
เอกสารนี้ให้การอ้างอิงไวยากรณ์ที่มีโครงสร้างและครอบคลุมสำหรับ Bash และ PowerShell ช่วยเสริมการอ้างอิงเชลล์หลักโดยมุ่งเน้นไปที่รูปแบบสคริปต์ที่ละเอียดถี่ถ้วน ไปป์ไลน์ การจัดการกระบวนการ และสำนวนอัตโนมัติสำหรับเชลล์ทั้งสอง
---

## Bash - ตัวดำเนินการและตัวแปร
### ผู้ประกอบการหลัก
| ตัวดำเนินการ | ชื่อ | ตัวอย่าง | หมายเหตุ |
|----------|-|---------|-------|
| `=`| การมอบหมายงาน | `x=10`| ไม่มีการเว้นวรรครอบ`=`|
| `$var`| การขยายตัวแปร | `echo $HOME`| |
| `${var}`| การขยายตัวแบบค้ำยัน | `${HOME}/docs`| แก้ความกำกวม |
| `$(cmd)`| การทดแทนคำสั่ง | `$(date +%Y)`| เป็นที่ต้องการมากกว่า backticks |
| `$((expr))`| เลขคณิต | `$((2 + 3))`| |
| `${var:-default}`| ค่าเริ่มต้น | `${PORT:-8080}`| หากไม่ได้ตั้งค่าหรือว่างเปล่า |
| `${var:=default}`| กำหนดค่าเริ่มต้น | `${count:=0}`| |
| `${#var}`| ความยาวสตริง | `${#name}`| |
| `${var%%pattern}`| ลบคำต่อท้ายที่ยาวที่สุด | `${file%%.*}`| ลบส่วนขยาย |
| `${var##pattern}`| ลบคำนำหน้าที่ยาวที่สุด | `${path##*/}`| รับชื่อไฟล์ |
| `"``"` | เครื่องหมายคำพูดคู่ | `"$var"`| อนุญาตให้ขยาย |
| `'``'` | เครื่องหมายคำพูดเดี่ยว | `'$var'`| สตริงตัวอักษร |
### ผู้ดำเนินการทดสอบ
```bash
# File tests
[ -f "$file" ]    # is a regular file
[ -d "$dir" ]     # is a directory
[ -e "$path" ]    # exists
[ -r "$file" ]    # readable
[ -w "$file" ]    # writable
[ -x "$file" ]    # executable
[ -s "$file" ]    # non-empty

# String tests
[ -z "$str" ]     # empty string
[ -n "$str" ]     # non-empty string
[ "$a" = "$b" ]   # equal
[ "$a" != "$b" ]  # not equal

# Numeric tests
[ "$a" -eq "$b" ] # equal
[ "$a" -ne "$b" ] # not equal
[ "$a" -lt "$b" ] # less than
[ "$a" -ge "$b" ] # greater or equal

# Compound
[[ "$a" == pattern* ]]   # pattern matching (bash)
[[ "$a" =~ regex ]]       # regex matching (bash)
[ "$a" -gt 0 ] && [ "$b" -lt 10 ]   # AND
[ "$a" -gt 0 ] || [ "$b" -lt 10 ]   # OR
```

---

## Bash - โฟลว์ควบคุม
```bash
# if / elif / else
if [ -f "$file" ]; then
    echo "File exists"
elif [ -d "$file" ]; then
    echo "Is a directory"
else
    echo "Not found"
fi

# case
case "$action" in
    start)
        start_service ;;
    stop)
        stop_service ;;
    restart)
        stop_service
        start_service ;;
    *)
        echo "Unknown action: $action" ;;
esac

# for loop
for file in *.txt; do
    echo "Processing: $file"
done

# C-style for
for ((i = 0; i < 10; i++)); do
    echo "$i"
done

# while
while IFS= read -r line; do
    process "$line"
done < input.txt

# until
until [ "$count" -ge 10 ]; do
    count=$((count + 1))
done

# Select (interactive menu)
select choice in "Option 1" "Option 2" "Quit"; do
    case $choice in
        "Option 1") do_something ;;
        "Option 2") do_other ;;
        "Quit") break ;;
    esac
done
```

---

## Bash - ฟังก์ชั่นและไปป์ไลน์
```bash
# Function definition
greet() {
    local name="${1:-World}"
    echo "Hello, $name!"
}

# Return values (via stdout)
get_count() {
    find . -name "*.txt" | wc -l
}
count=$(get_count)

# Pipes
cat access.log | grep "ERROR" | awk '{print $4}' | sort | uniq -c | sort -rn | head -20

# xargs
find . -name "*.log" -mtime +30 | xargs rm
echo "file1 file2 file3" | xargs -I {} cp {} /backup/

# Process substitution
diff <(sort file1) <(sort file2)

# Here documents
cat <<EOF
Hello, $USER
Today is $(date)
EOF

# Here string
grep "pattern" <<< "some input string"
```

---

## PowerShell — Cmdlets & ไปป์ไลน์
```powershell
# Cmdlet syntax (Verb-Noun)
Get-Process
Get-Service -Name wuauserv
Set-Location -Path C:\Users

# Pipeline — objects, not text
Get-Process | Where-Object { $_.WorkingSet64 -gt 100MB } | Sort-Object CPU -Descending | Select-Object -First 10 Name, CPU, WorkingSet64

# Variables
$name = "Alice"
$count = 42
$items = @(1, 2, 3, 4, 5)
$hash = @{ Name = "Alice"; Age = 30 }

# String interpolation
"Hello, $name!"
"Path: $($env:USERPROFILE)\Documents"
'This is literal: $not_expanded'

# Array operations
$items.Count              # 5
$items[0]                 # 1
$items[-1]                # 5 (last element)
$items += 6               # append
$filtered = $items | Where-Object { $_ -gt 3 }
```

---

## PowerShell - โฟลว์การควบคุม
```powershell
# if / elseif / else
if ($age -ge 18) {
    "Adult"
} elseif ($age -ge 13) {
    "Teenager"
} else {
    "Child"
}

# Comparison operators
# -eq  -ne  -lt  -le  -gt  -ge
# -like (wildcard)   -match (regex)
# -contains           -in
# -and  -or  -not  -xor

# switch
switch ($status) {
    'active'   { "Currently active" }
    'pending'  { "Awaiting activation" }
    default    { "Unknown status" }
}

# switch with conditions
switch -Regex ($input) {
    '^\d+$'     { "Number: $_" }
    '^[a-z]+$'  { "Word: $_" }
    default     { "Other: $_" }
}

# foreach
foreach ($item in $collection) {
    Process-Item $item
}

# ForEach-Object (pipeline)
1..10 | ForEach-Object { $_ * 2 }

# while / do-while
while ($condition) { Do-Something }
do { Do-Something } while ($condition)

# for
for ($i = 0; $i -lt 10; $i++) {
    Write-Host $i
}
```

---

## PowerShell - ฟังก์ชั่นและรูปแบบขั้นสูง
```powershell
# Basic function
function Get-Greeting {
    param(
        [Parameter(Mandatory)]
        [string]$Name,

        [string]$Greeting = "Hello"
    )
    "$Greeting, $Name!"
}

# Pipeline input
function Convert-ToUpperCase {
    process {
        $_.ToUpper()
    }
}
"hello", "world" | Convert-ToUpperCase

# Advanced function with begin/process/end
function Measure-Pipeline {
    begin   { $count = 0; $start = Get-Date }
    process { $count++; $_ }
    end     { $elapsed = (Get-Date) - $start; Write-Host "Processed $count items in $elapsed" }
}

# Error handling
try {
    $result = Get-Content "nonexistent.txt" -ErrorAction Stop
} catch [System.IO.FileNotFoundException] {
    Write-Warning "File not found"
} catch {
    Write-Error "Unexpected: $_"
} finally {
    # cleanup
}

# Custom objects
[PSCustomObject]@{
    Name = "Alice"
    Age = 30
    Department = "Engineering"
}

# Modules
Import-Module ActiveDirectory
Get-Command -Module ActiveDirectory
```

---

## สรุป
Bash และ PowerShell เป็นตัวแทนของสองกระบวนทัศน์ของการเขียนสคริปต์เชลล์ ข้อความ Bash Pipes — ทุกคำสั่งจะแปลงสตริง ไปป์ออบเจ็กต์ PowerShell — ทุกคำสั่งจะสร้างข้อมูลที่มีโครงสร้างพร้อมคุณสมบัติและวิธีการ Bash ครอบงำ Linux/macOS และ DevOps PowerShell เป็นสิ่งจำเป็นสำหรับการดูแลระบบ Windows และข้ามแพลตฟอร์มที่เพิ่มมากขึ้น ทั้งสองอย่างเป็นเครื่องมือสำคัญในกลุ่มเทคโนโลยีสมัยใหม่ เชลล์สคริปต์คือกาวที่เชื่อมโยงระบบ ทำให้เวิร์กโฟลว์เป็นอัตโนมัติ และทำงานต่างๆ ให้เสร็จสิ้น