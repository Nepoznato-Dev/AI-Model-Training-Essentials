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
# शैल और पावरशेल - सिंटैक्स संदर्भ
यह दस्तावेज़ बैश और पॉवरशेल के लिए एक व्यापक, संरचित सिंटैक्स संदर्भ प्रदान करता है। यह दोनों शेल के लिए संपूर्ण स्क्रिप्टिंग पैटर्न, पाइपलाइन, प्रक्रिया प्रबंधन और स्वचालन मुहावरों पर ध्यान केंद्रित करके मुख्य शेल संदर्भ को पूरक करता है।
---

## बैश - ऑपरेटर्स और वेरिएबल्स
### कोर ऑपरेटर्स
| ऑपरेटर | नाम | उदाहरण | नोट्स |
|-------|------|------|-------|
| `=`| असाइनमेंट | `x=10`|`=`के आसपास कोई स्थान नहीं |
| `$var`| परिवर्तनशील विस्तार | `echo $HOME`| |
| `${var}`| ब्रेस्ड विस्तार | `${HOME}/docs`| असंबद्ध |
| `$(cmd)`| कमांड प्रतिस्थापन | `$(date +%Y)`| बैकटिक्स पर पसंदीदा |
| `$((expr))`| अंकगणित | `$((2 + 3))`| |
| `${var:-default}`| डिफ़ॉल्ट मान | `${PORT:-8080}`| यदि असेट या खाली है |
| `${var:=default}`| डिफ़ॉल्ट असाइन करें | `${count:=0}`| |
| `${#var}`| स्ट्रिंग की लंबाई | `${#name}`| |
| `${var%%pattern}`| सबसे लंबा प्रत्यय हटाएँ | `${file%%.*}`| एक्सटेंशन हटाएं |
| `${var##pattern}`| सबसे लंबा उपसर्ग हटाएँ | `${path##*/}`| फ़ाइल नाम प्राप्त करें |
| `"``"` | दोहरे उद्धरण | `"$var"`| विस्तार की अनुमति देता है |
| `'``'` | एकल उद्धरण | `'$var'`| शाब्दिक स्ट्रिंग |
### परीक्षण संचालक
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

## बैश - नियंत्रण प्रवाह
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

## बैश - कार्य और पाइपलाइन
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

## पावरशेल - सीएमडीलेट्स और पाइपलाइन
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

## पॉवरशेल - नियंत्रण प्रवाह
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

## पावरशेल - फ़ंक्शन और उन्नत पैटर्न
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

## सारांश
बैश और पॉवरशेल शेल स्क्रिप्टिंग के दो प्रतिमानों का प्रतिनिधित्व करते हैं। बैश पाइप टेक्स्ट - प्रत्येक कमांड स्ट्रिंग्स को बदल देता है। पॉवरशेल पाइप ऑब्जेक्ट्स - प्रत्येक कमांड गुणों और विधियों के साथ संरचित डेटा उत्पन्न करता है। बैश Linux/macOS और DevOps पर हावी है। विंडोज़ प्रशासन और तेजी से क्रॉस-प्लेटफ़ॉर्म के लिए पावरशेल आवश्यक है। आधुनिक तकनीकी स्टैक में दोनों आवश्यक उपकरण हैं। शेल स्क्रिप्ट वह गोंद है जो सिस्टम को जोड़ती है, वर्कफ़्लो को स्वचालित करती है और काम पूरा करती है।