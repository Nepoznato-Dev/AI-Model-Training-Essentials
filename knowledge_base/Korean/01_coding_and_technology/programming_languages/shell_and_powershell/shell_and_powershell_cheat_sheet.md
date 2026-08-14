---
# Metadata
title: "Shell & PowerShell — Cheat Sheet"
description: "Quick-reference cheat sheet for Bash and PowerShell syntax and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [bash, powershell, shell, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# 셸 및 PowerShell — 치트 시트
## 배쉬 기본
```bash
# Variables
name="Alice"
age=30
readonly PI=3.14159

# Use variables
echo "Hello, $name!"
echo "Age: ${age}"
echo "Home: $HOME"
echo "Args: $1 $2 $@"
echo "Count: $#"
echo "Exit code: $?"
echo "PID: $$"

# Command substitution
today=$(date +%Y-%m-%d)
files=$(ls -la)

# Arithmetic
echo $((2 + 3))
echo $((age + 1))
let "x = 5 + 3"

# String operations
echo ${#name}              # length
echo ${name^^}             # uppercase
echo ${name,,}             # lowercase
echo ${name:0:3}           # substring
echo ${name/Alice/Bob}     # replace
echo ${name:-default}      # default if empty
echo ${name:=default}      # set default
```

## Bash 배열
```bash
# Indexed array
arr=(one two three four)
echo ${arr[0]}
echo ${arr[@]}             # all elements
echo ${#arr[@]}            # length
arr+=(five)                # append

# Associative array (Bash 4+)
declare -A map
map[name]="Alice"
map[age]=30
echo ${map[name]}
echo ${!map[@]}            # keys
echo ${map[@]}             # values
```

## Bash 제어 흐름
```bash
# If
if [[ -f "file.txt" ]]; then
    echo "exists"
elif [[ -d "dir" ]]; then
    echo "directory"
else
    echo "other"
fi

# Test conditions
[[ -f file ]]       # file exists
[[ -d dir ]]        # directory exists
[[ -z "$var" ]]     # empty string
[[ -n "$var" ]]     # non-empty string
[[ "$a" == "$b" ]]  # string equal
[[ "$a" -eq "$b" ]] # numeric equal
[[ "$a" -gt "$b" ]] # numeric greater
[[ "$str" =~ regex ]] # regex match

# Case
case "$action" in
    start) echo "starting" ;;
    stop)  echo "stopping" ;;
    *)     echo "unknown" ;;
esac

# Loops
for item in "${arr[@]}"; do
    echo "$item"
done

for i in $(seq 1 10); do
    echo "$i"
done

for ((i=0; i<10; i++)); do
    echo "$i"
done

while read -r line; do
    echo "$line"
done < file.txt

until [[ $count -gt 10 ]]; do
    ((count++))
done
```

## Bash 함수 및 패턴
```bash
# Function
greet() {
    local name="$1"
    local greeting="${2:-Hello}"
    echo "$greeting, $name!"
}
greet "Alice" "Hi"

# Error handling
set -euo pipefail
trap 'echo "Error on line $LINENO"' ERR

# Read input
read -p "Enter name: " name
read -r -a array   # read into array

# Here document
cat <<EOF
Hello, $name!
Today is $(date).
EOF

# Process substitution
diff <(sort file1) <(sort file2)

# Common patterns
x="${1:-default}"       # default value
: "${var:=default}"     # set if unset
"${var:?error msg}"     # error if unset
```

## 파워셸 기본 사항
```powershell
# Variables
$name = "Alice"
$age = 30
$PI = 3.14159
[int]$count = 42
[string]$text = "hello"

# String interpolation
"Hello, $name!"
"Age: $($age + 1)"
"Pi: $([math]::Round($PI, 2))"

# String methods
$name.Length
$name.ToUpper()
$name.ToLower()
$name.Trim()
$name.Contains("lic")
$name.Replace("Alice", "Bob")
$name.Substring(0, 3)
$name -split ""
[string]::Join(", ", $items)

# Operators
$x -eq 42         # equal
$x -ne 0          # not equal
$x -gt 10         # greater
$x -lt 100        # less
$x -ge 0          # greater or equal
$name -like "A*"  # wildcard match
$name -match "lic" # regex match
$name -in @("Alice","Bob")
$name -contains "lic"
```

## PowerShell 컬렉션
```powershell
# Array
$arr = @(1, 2, 3)
$arr[0]
$arr.Count
$arr += 4
$arr | Where-Object { $_ -gt 2 }
$arr | ForEach-Object { $_ * 2 }
$arr | Sort-Object
$arr | Select-Object -First 3

# Hashtable
$map = @{ name = "Alice"; age = 30 }
$map["email"] = "a@b.com"
$map["name"]
$map.Keys
$map.Values
$map.ContainsKey("name")

# PSCustomObject
$obj = [PSCustomObject]@{
    Name = "Alice"
    Age = 30
    Email = "a@b.com"
}
$obj.Name
```

## 파워셸 제어 흐름
```powershell
# If
if ($age -ge 18) {
    "adult"
} elseif ($age -ge 13) {
    "teen"
} else {
    "child"
}

# Switch
switch ($day) {
    "Monday" { "early week"; break }
    { $_ -match "day$" } { "weekday"; break }
    default { "other" }
}

# Loops
foreach ($item in $collection) { $item }
for ($i = 0; $i -lt 10; $i++) { $i }
while ($condition) { ... }
do { ... } until ($condition)
1..10 | ForEach-Object { $_ }
```

## 파워셸 함수
```powershell
# Advanced function
function Get-User {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Name,

        [int]$Age = 0,

        [switch]$Verbose
    )

    process {
        "Hello, $Name! Age: $Age"
    }
}

# Pipeline function
function Convert-ToUpper {
    process { $_.ToUpper() }
}
"hello", "world" | Convert-ToUpper
```

## 파워셸 오류 처리
```powershell
try {
    $result = Get-Content "file.txt" -ErrorAction Stop
} catch [System.IO.FileNotFoundException] {
    Write-Warning "File not found"
} catch {
    Write-Error "Error: $_"
} finally {
    # cleanup
}

# Error preference
$ErrorActionPreference = "Stop"

# Throw
throw "Something failed"
```
