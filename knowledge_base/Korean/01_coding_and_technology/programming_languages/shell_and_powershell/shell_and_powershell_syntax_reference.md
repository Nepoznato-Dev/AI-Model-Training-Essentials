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
# 셸 및 PowerShell - 구문 참조
이 문서는 Bash 및 PowerShell에 대한 포괄적이고 구조화된 구문 참조를 제공합니다. 두 셸 모두에 대한 철저한 스크립팅 패턴, 파이프라인, 프로세스 관리 및 자동화 관용어에 중점을 두어 기본 셸 참조를 보완합니다.
---

## Bash — 연산자 및 변수
### 핵심 운영자
| 운영자 | 이름 | 예 | 메모 |
|------------|------|---------|-------|
| `=`| 과제 | `x=10`|`=`주위에 공백이 없습니다 |
| `$var`| 변수 확장 | `echo $HOME`| |
| `${var}`| 보강된 확장 | `${HOME}/docs`| 명확성 |
| `$(cmd)`| 명령 대체 | `$(date +%Y)`| 백틱보다 선호됨 |
| `$((expr))`| 산술 | `$((2 + 3))`| |
| `${var:-default}`| 기본값 | `${PORT:-8080}`| 설정되지 않았거나 비어 있는 경우 |
| `${var:=default}`| 기본값 할당 | `${count:=0}`| |
| `${#var}`| 문자열 길이 | `${#name}`| |
| `${var%%pattern}`| 가장 긴 접미사 제거 | `${file%%.*}`| 확장 프로그램 제거 |
| `${var##pattern}`| 가장 긴 접두사 제거 | `${path##*/}`| 파일 이름 가져오기 |
| `"``"` | 큰따옴표 | `"$var"`| 확장 가능 |
| `'``'` | 작은따옴표 | `'$var'`| 리터럴 문자열 |
### 테스트 연산자
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

## Bash — 제어 흐름
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

## Bash — 함수 및 파이프라인
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

## PowerShell — cmdlet 및 파이프라인
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

## 파워셸 — 제어 흐름
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

## PowerShell — 기능 및 고급 패턴
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

## 요약
Bash와 PowerShell은 셸 스크립팅의 두 가지 패러다임을 나타냅니다. Bash 파이프 텍스트 — 모든 명령은 문자열을 변환합니다. PowerShell 파이프 개체 - 모든 명령은 속성과 메서드가 포함된 구조화된 데이터를 생성합니다. Bash는 Linux/macOS 및 DevOps를 지배합니다. PowerShell은 Windows 관리 및 점점 더 많은 크로스 플랫폼에 필수적입니다. 둘 다 현대 기술 스택의 필수 도구입니다. 쉘 스크립트는 시스템을 연결하고, 워크플로우를 자동화하고, 작업을 완료하는 접착제입니다.