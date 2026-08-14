---
# Metadata
title: "Shell & PowerShell — Syntax Reference"
description: "Detailed syntax reference for Bash and PowerShell covering scripting, pipelines, process management, automation, and system administration patterns."
category: "Coding and Technology"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
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

# Shell & PowerShell — Tham khảo cú pháp
Tài liệu này cung cấp tài liệu tham khảo cú pháp có cấu trúc, toàn diện cho Bash và PowerShell. Nó bổ sung cho tham chiếu Shell chính bằng cách tập trung vào các mẫu kịch bản, quy trình, quản lý quy trình và thành ngữ tự động hóa đầy đủ cho cả hai shell.
---

## Bash — Toán tử & Biến
### Toán tử cốt lõi
| Nhà điều hành | Tên | Ví dụ | Ghi chú |
|----------|------|----------|-------|
| `=`| Bài tập | `x=10`| Không còn khoảng trống xung quanh`=`|
| `$var`| Mở rộng biến | `echo $HOME`| |
| `${var}`| Mở rộng giằng | `${HOME}/docs`| Định hướng |
| `$(cmd)`| Thay thế lệnh | `$(date +%Y)`| Được ưu tiên hơn backticks |
| `$((expr))`| Số học | `$((2 + 3))`| |
| `${var:-default}`| Giá trị mặc định | `${PORT:-8080}`| Nếu không được đặt hoặc trống |
| `${var:=default}`| Chỉ định mặc định | `${count:=0}`| |
| `${#var}`| Độ dài chuỗi | `${#name}`| |
| `${var%%pattern}`| Xóa hậu tố dài nhất | `${file%%.*}`| Xóa tiện ích mở rộng |
| `${var##pattern}`| Xóa tiền tố dài nhất | `${path##*/}`| Lấy tên tập tin |
| `"``"` | Dấu ngoặc kép | `"$var"`| Cho phép mở rộng |
| `'``'` | Dấu ngoặc đơn | `'$var'`| Chuỗi chữ |
### Người vận hành thử nghiệm
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

## Bash — Luồng điều khiển
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

## Bash — Chức năng & Đường dẫn
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

## PowerShell — Lệnh ghép ngắn & Đường dẫn
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

## PowerShell — Luồng điều khiển
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

## PowerShell — Hàm & Mẫu nâng cao
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

## Bản tóm tắt
Bash và PowerShell đại diện cho hai mô hình kịch bản shell. Văn bản ống Bash - mọi lệnh đều biến đổi chuỗi. Đối tượng đường ống PowerShell - mọi lệnh đều tạo ra dữ liệu có cấu trúc với các thuộc tính và phương thức. Bash thống trị Linux/macOS và DevOps. PowerShell rất cần thiết cho quản trị Windows và ngày càng đa nền tảng. Cả hai đều là những công cụ thiết yếu trong kho công nghệ hiện đại. Tập lệnh Shell là chất keo kết nối các hệ thống, tự động hóa quy trình làm việc và hoàn thành công việc.