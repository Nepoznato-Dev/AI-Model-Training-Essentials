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
# শেল এবং পাওয়ারশেল — সিনট্যাক্স রেফারেন্স
এই নথিটি Bash এবং PowerShell-এর জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি উভয় শেলের জন্য সম্পূর্ণ স্ক্রিপ্টিং প্যাটার্ন, পাইপলাইন, প্রক্রিয়া পরিচালনা এবং অটোমেশন ইডিয়মগুলিতে ফোকাস করে প্রধান শেল রেফারেন্সের পরিপূরক।
---

## ব্যাশ — অপারেটর এবং ভেরিয়েবল
### মূল অপারেটর
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `=`| অ্যাসাইনমেন্ট | `x=10`|`=`এর আশেপাশে কোন স্পেস নেই |
| `$var`| পরিবর্তনশীল সম্প্রসারণ | `echo $HOME`| |
| `${var}`| বন্ধনী সম্প্রসারণ | `${HOME}/docs`| অস্পষ্ট করে |
| `$(cmd)`| কমান্ড প্রতিস্থাপন | `$(date +%Y)`| ব্যাকটিক্সের চেয়ে পছন্দ |
| `$((expr))`| পাটিগণিত | `$((2 + 3))`| |
| `${var:-default}`| ডিফল্ট মান | `${PORT:-8080}`| সেট না থাকলে বা খালি থাকলে |
| `${var:=default}`| ডিফল্ট বরাদ্দ করুন | `${count:=0}`| |
| `${#var}`| স্ট্রিং দৈর্ঘ্য | `${#name}`| |
| `${var%%pattern}`| দীর্ঘতম প্রত্যয় সরান | `${file%%.*}`| এক্সটেনশন সরান |
| `${var##pattern}`| দীর্ঘতম উপসর্গ সরান | `${path##*/}`| ফাইলের নাম পান |
| `"``"` | ডবল উদ্ধৃতি | `"$var"`| সম্প্রসারণের অনুমতি দেয় |
| `'``'` | একক উদ্ধৃতি | `'$var'`| আক্ষরিক স্ট্রিং |
### টেস্ট অপারেটর
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

## ব্যাশ — নিয়ন্ত্রণ প্রবাহ
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

## ব্যাশ — ফাংশন এবং পাইপলাইন
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

## পাওয়ারশেল — Cmdlets এবং পাইপলাইন
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

## পাওয়ারশেল — নিয়ন্ত্রণ প্রবাহ
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

## পাওয়ারশেল — ফাংশন এবং উন্নত প্যাটার্ন
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

## সারাংশ
Bash এবং PowerShell শেল স্ক্রিপ্টিংয়ের দুটি দৃষ্টান্ত উপস্থাপন করে। ব্যাশ পাইপ টেক্সট — প্রতিটি কমান্ড স্ট্রিং রূপান্তরিত করে। PowerShell পাইপ অবজেক্ট - প্রতিটি কমান্ড বৈশিষ্ট্য এবং পদ্ধতি সহ কাঠামোগত ডেটা তৈরি করে। ব্যাশ লিনাক্স/ম্যাকওএস এবং ডিওঅপসকে প্রাধান্য দেয়। Windows প্রশাসন এবং ক্রমবর্ধমান ক্রস-প্ল্যাটফর্মের জন্য PowerShell অপরিহার্য। উভয়ই একটি আধুনিক প্রযুক্তির স্ট্যাকের অপরিহার্য সরঞ্জাম। শেল স্ক্রিপ্টগুলি হল আঠা যা সিস্টেমগুলিকে সংযুক্ত করে, কর্মপ্রবাহকে স্বয়ংক্রিয় করে এবং কাজগুলি সম্পন্ন করে।