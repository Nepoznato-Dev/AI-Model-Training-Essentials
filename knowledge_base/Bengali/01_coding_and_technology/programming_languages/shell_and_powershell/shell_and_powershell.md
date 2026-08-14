<!--
---
# Metadata
title: "Shell & PowerShell"
description: "Comprehensive reference for the Shell and PowerShell programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [shell-and-powershell, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# শেল এবং পাওয়ারশেল
শেল স্ক্রিপ্টিং কমান্ড-লাইন ইন্টারপ্রেটারদের জন্য স্ক্রিপ্ট লেখাকে বোঝায়। দুটি সবচেয়ে গুরুত্বপূর্ণ শেল হল **ব্যাশ** (বোর্ন অ্যাগেইন শেল) — লিনাক্স এবং ম্যাকওএস-এ ডিফল্ট — এবং **পাওয়ারশেল** — মাইক্রোসফটের আধুনিক ক্রস-প্ল্যাটফর্ম শেল এবং স্ক্রিপ্টিং ভাষা। শেল স্ক্রিপ্টগুলি সিস্টেম প্রশাসনের কাজগুলিকে স্বয়ংক্রিয় করে, পাইপলাইন তৈরি করে, ফাইল প্রক্রিয়াকরণ, এবং স্থাপনার কর্মপ্রবাহ।
প্রত্যেক ডেভেলপার, DevOps ইঞ্জিনিয়ার এবং সিস্টেম অ্যাডমিনিস্ট্রেটরের শেল স্ক্রিপ্টিং দক্ষতা প্রয়োজন। আপনি একটি ওয়েব সার্ভার স্থাপন করছেন, লগ ফাইল প্রসেস করছেন, সিআই/সিডি পাইপলাইন সেট আপ করছেন বা ব্যাকআপ স্বয়ংক্রিয় করছেন, শেল স্ক্রিপ্টিং হল কাজের হাতিয়ার।
---

## কেন শেল/পাওয়ারশেল গুরুত্বপূর্ণ
- **অটোমেশন**: পুনরাবৃত্তিমূলক কাজগুলি স্বয়ংক্রিয় করুন — ফাইল পরিচালনা, স্থাপনা, সিস্টেম কনফিগারেশন।
- **DevOps অপরিহার্য**: CI/CD পাইপলাইন (GitHub Actions, Jenkins), Docker, Kubernetes সবাই শেল স্ক্রিপ্ট ব্যবহার করে।
- **ইউনিভার্সাল**: প্রতিটি সার্ভার, ক্লাউড ইনস্ট্যান্স এবং কন্টেইনারের একটি শেল থাকে।
- **পাওয়ারশেলের অবজেক্ট পাইপলাইন**: ব্যাশের বিপরীতে, পাওয়ারশেল অবজেক্ট পাস করে, টেক্সট নয় — জটিল অপারেশনগুলিকে সহজ করে তোলে।
- **ক্রস-প্ল্যাটফর্ম (পাওয়ারশেল): PowerShell 7+ Windows, macOS এবং Linux-এ চলে।
- **দ্রুত এবং নোংরা**: কমান্ড লাইনে এককালীন সমস্যা সমাধানের দ্রুততম উপায়।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **ব্যাশ quirks** | অসামঞ্জস্যপূর্ণ সিনট্যাক্স, ভঙ্গুর স্ট্রিং পরিচালনা |`set -euo pipefail`ব্যবহার করুন; উদ্ধৃতি ভেরিয়েবল; জটিল স্ক্রিপ্টের জন্য PowerShell পছন্দ করুন |
| **জটিল প্রোগ্রামের জন্য নয়** | দুর্বল ডেটা স্ট্রাকচার, OOP নেই, পরীক্ষা করা কঠিন | জটিল যুক্তির জন্য পাইথন, গো বা অন্যান্য ভাষা ব্যবহার করুন |
| **ত্রুটি পরিচালনা** | ব্যাশ ত্রুটি হ্যান্ডলিং আদিম |`set -e`ব্যবহার করুন; প্রস্থান কোড চেক করুন; PowerShell এর চেষ্টা/ক্যাচ | ব্যবহার করুন
| ** বহনযোগ্যতা** | ব্যাশ স্ক্রিপ্ট সব সিস্টেমে কাজ নাও করতে পারে | সর্বাধিক বহনযোগ্যতার জন্য POSIX sh ব্যবহার করুন; ক্রস-প্ল্যাটফর্মের জন্য PowerShell |
| **ডিবাগিং** | সীমিত ডিবাগিং টুল | ব্যাশের জন্য`set -x`ব্যবহার করুন; পাওয়ারশেলের একটি সঠিক ডিবাগার আছে |
---

## ব্যাশ সিনট্যাক্স
```bash
#!/bin/bash
set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Variables
NAME="Alice"
AGE=30
echo "Hello, $NAME! Age: $AGE"

# Conditionals
if [ "$AGE" -ge 18 ]; then
    echo "Adult"
elif [ "$AGE" -ge 13 ]; then
    echo "Teenager"
else
    echo "Child"
fi

# Loops
for file in *.txt; do
    echo "Processing: $file"
done

for i in {1..10}; do
    echo "Count: $i"
done

while read -r line; do
    echo "Line: $line"
done < input.txt

# Functions
greet() {
    local name="$1"
    local greeting="${2:-Hello}"  # Default value
    echo "$greeting, $name!"
}

greet "Alice" "Hi"

# Command substitution
FILE_COUNT=$(find . -name "*.md" | wc -l)
echo "Found $FILE_COUNT markdown files"

# Pipes and text processing
cat access.log | grep "ERROR" | awk '{print $1, $4}' | sort | uniq -c | sort -rn | head -10
```

## পাওয়ারশেল সিনট্যাক্স
```powershell
# Variables
$Name = "Alice"
$Age = 30
Write-Host "Hello, $Name! Age: $Age"

# Objects (PowerShell passes objects, not text)
Get-Process | Where-Object { $_.CPU -gt 100 } | Sort-Object CPU -Descending | Select-Object -First 5

# Conditionals
if ($Age -ge 18) {
    Write-Host "Adult"
} elseif ($Age -ge 13) {
    Write-Host "Teenager"
} else {
    Write-Host "Child"
}

# Loops
foreach ($file in Get-ChildItem -Filter "*.txt") {
    Write-Host "Processing: $($file.Name)"
}

1..10 | ForEach-Object { Write-Host "Count: $_" }

# Functions
function Greet {
    param(
        [string]$Name,
        [string]$Greeting = "Hello"
    )
    "$Greeting, $Name!"
}

Greet -Name "Alice" -Greeting "Hi"

# Error handling
try {
    $result = 10 / 0
} catch {
    Write-Error "Division failed: $_"
} finally {
    Write-Host "Cleanup complete"
}

# File operations
Get-Content "data.csv" | ConvertFrom-Csv | Where-Object { $_.Age -gt 25 }

# Pipeline (object-based — much more powerful than text pipes)
Get-Service | 
    Where-Object Status -eq "Running" | 
    Select-Object Name, DisplayName, Status |
    Format-Table -AutoSize
```

---

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### উন্নত ব্যাশ পাইপিং এবং পুনঃনির্দেশ
```bash
# Process substitution: treat command output as a file
diff <(sort file1.txt) <(sort file2.txt)

# Here-strings (Bash 3+)
grep "pattern" <<< "search in this string directly"

# Here-documents for multi-line input
cat << 'ENDCONF' > config.yaml
database:
  host: localhost
  port: 5432
  name: myapp
ENDCONF

# Named pipes (FIFOs)
mkfifo /tmp/mypipe
echo "data" > /tmp/mypipe &
cat /tmp/mypipe
```
```bash
# xargs: convert stdin into command arguments
find . -name "*.log" -mtime +30 -exec gzip {} \;
find . -name "*.txt" -print0 | xargs -0 wc -l  # Handle filenames with spaces
```

### উন্নত পাওয়ারশেল প্যাটার্নস
```powershell
# Here-strings for multi-line text
$query = @"
SELECT name, email
FROM users
WHERE created_at > '2024-01-01'
ORDER BY name
"@

# Splatting: pass parameters as a hashtable
$params = @{
    Path        = "C:\Logs"
    Filter      = "*.log"
    Recurse     = $true
    ErrorAction = "SilentlyContinue"
}
Get-ChildItem @params
```
```powershell
# Advanced function with parameter validation
function Deploy-Application {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$AppName,

        [Parameter(Mandatory = $true)]
        [ValidateSet("dev", "staging", "production")]
        [string]$Environment,

        [ValidateRange(1, 65535)]
        [int]$Port = 8080,

        [switch]$DryRun
    )
    begin { Write-Verbose "Starting deployment of $AppName to $Environment" }
    process {
        if ($DryRun) {
            Write-Host "[DRY RUN] Would deploy $AppName to $Environment on port $Port"
        } else {
            Write-Host "Deploying $AppName to $Environment..."
        }
    }
    end { Write-Verbose "Deployment complete" }
}

# PowerShell classes (PS 5.0+)
class ServerConfig {
    [string]$Name
    [string]$Environment
    [int]$Port
    [bool]$IsHealthy

    ServerConfig([string]$name, [string]$env, [int]$port) {
        $this.Name = $name
        $this.Environment = $env
        $this.Port = $port
        $this.IsHealthy = $false
    }

    [string] GetUrl() {
        return "https://$($this.Name).$($this.Environment):$($this.Port)"
    }

    [void] MarkHealthy() { $this.IsHealthy = $true }
}

$server = [ServerConfig]::new("web01", "production", 443)
$server.MarkHealthy()
Write-Host $server.GetUrl()
```
```powershell
# Error handling patterns
$ErrorActionPreference = "Stop"

try {
    $response = Invoke-WebRequest -Uri "https://api.example.com/data" -TimeoutSec 10
    $data = $response.Content | ConvertFrom-Json
} catch [System.Net.WebException] {
    Write-Warning "Web request failed: $($_.Exception.Message)"
} catch {
    Write-Error "Unexpected error: $($_.Exception.GetType().FullName)"
} finally {
    Write-Verbose "Cleanup complete"
}
```

### শেলে রেগুলার এক্সপ্রেশন
```bash
# Bash regex matching
email="user@example.com"
if [[ "$email" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
    echo "Valid email: ${BASH_REMATCH[0]}"
fi

# grep with extended regex
grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}' access.log       # Lines starting with dates
grep -c 'ERROR' /var/log/syslog                           # Count error lines

# sed: stream editing
sed 's/old/new/g' file.txt                          # Global replacement
sed -n '/ERROR/,/END/p' log.txt                     # Print range between patterns

# awk: field processing
awk -F',' '{print $1, $3}' data.csv                 # Print columns 1 and 3
awk '{sum += $1} END {print "Total:", sum}' numbers.txt  # Sum first column
awk 'NR==1 || $3 > 100' data.txt                    # Header + filtered rows
awk '/ERROR/ {count++} END {print count+0}' log     # Count error lines
```

### পাওয়ারশেল রেজেক্স এবং টেক্সট প্রসেসিং
```powershell
# PowerShell regex
$email = "user@example.com"
if ($email -match '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$') {
    Write-Host "Valid email: $($Matches[0])"
}

# Named capture groups
$logLine = "2024-01-15 ERROR Connection timeout after 30s"
if ($logLine -match '^(?<date>\d{4}-\d{2}-\d{2})\s+(?<level>\w+)\s+(?<message>.+)$') {
    Write-Host "Date: $($Matches.date), Level: $($Matches.level), Message: $($Matches.message)"
}

# Select-String: PowerShell's grep
Select-String -Path "*.log" -Pattern "ERROR" -Context 2, 3

# String manipulation
$text = "Hello, World!"
$text.ToUpper()
$text -replace 'World', 'PowerShell'
$text.Split(',')
"  padded  ".Trim()
```
---

## মূল বৈশিষ্ট্যগুলিতে গভীরভাবে ডুব দিন
### পাইপলাইন প্যাটার্নস
```bash
# Bash: log analysis pipeline
awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -rn | head -20

# Find and process files by date
find /data -name "*.csv" -mtime -7 -exec gzip {} \;

# Parallel execution with xargs
cat urls.txt | xargs -P 8 -I {} curl -s -o /dev/null -w "%{http_code} {}" {}

# Monitor and alert
tail -f /var/log/syslog | grep --line-buffered "CRITICAL" | while read -r line; do
    echo "ALERT: $line"
done
```

```powershell
# PowerShell: object pipeline for system analysis
Get-Process |
    Group-Object Company |
    Where-Object { $_.Count -gt 5 } |
    Sort-Object Count -Descending |
    Select-Object @{N='Company';E={$_.Name}}, Count |
    Format-Table -AutoSize

# PowerShell: parallel processing (PS 7+)
$urls = Get-Content urls.txt
$urls | ForEach-Object -Parallel -ThrottleLimit 8 {
    try {
        $response = Invoke-WebRequest -Uri $_ -TimeoutSec 10
        "$_ : $($response.StatusCode)"
    } catch { "$_ : FAILED" }
}

# Pipeline to CSV to JSON
Get-Process |
    Select-Object Name, Id, CPU, WorkingSet64 |
    ConvertTo-Csv -NoTypeInformation |
    Out-File processes.csv

Import-Csv data.csv | ConvertTo-Json -Depth 5 | Out-File data.json
```
### মডিউল সিস্টেম
```bash
# Bash: sourcing functions from external files
# lib/utils.sh
log_info()  { echo "[INFO]  $(date '+%Y-%m-%d %H:%M:%S') $*"; }
log_error() { echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') $*" >&2; }
require_var() {
    local var_name="$1"
    if [[ -z "${!var_name:-}" ]]; then
        log_error "Required variable $var_name is not set"
        exit 1
    fi
}

# main.sh
#!/bin/bash
source "$(dirname "$0")/lib/utils.sh"
require_var "DATABASE_URL"
log_info "Starting application..."
```

```powershell
# PowerShell module structure:
# MyModule/
#   MyModule.psd1    (module manifest)
#   MyModule.psm1    (module script)
#   Public/
#     Get-ServerStatus.ps1
#   Private/
#     Invoke-InternalApi.ps1

# MyModule.psd1 (manifest)
@{
    ModuleVersion     = '1.0.0'
    RootModule        = 'MyModule.psm1'
    FunctionsToExport = @('Get-ServerStatus')
    Author            = 'Dev Team'
    Description       = 'Server management utilities'
    PowerShellVersion = '5.1'
}

# MyModule.psm1 (auto-load public and private functions)
$Public  = @(Get-ChildItem -Path "$PSScriptRoot\Public\*.ps1" -ErrorAction SilentlyContinue)
$Private = @(Get-ChildItem -Path "$PSScriptRoot\Private\*.ps1" -ErrorAction SilentlyContinue)
($Public + $Private) | ForEach-Object { . $_.FullName }
Export-ModuleMember -Function $Public.BaseName

# Install and use module
Install-Module -Name MyModule -Scope CurrentUser
Import-Module MyModule
Get-ServerStatus -Name "web01"
```
---

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### স্ক্রিপ্ট স্ট্রাকচার সেরা অনুশীলন
```bash
#!/bin/bash
# ============================================================================
# deploy.sh - Application deployment script
# Usage: ./deploy.sh --env production --version 2.1.0
# ============================================================================
set -euo pipefail
IFS=$'\n\t'

# Constants
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_NAME="$(basename "$0")"
readonly LOG_FILE="/var/log/deploy.log"

# Defaults
ENVIRONMENT="staging"
VERSION=""
DRY_RUN=false

usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS]
Options:
    --env ENV         Target environment (dev|staging|production)
    --version VER     Version to deploy
    --dry-run         Show what would be done
    -h, --help        Show this help message
EOF
}

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"; }

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --env)      ENVIRONMENT="$2"; shift 2 ;;
        --version)  VERSION="$2"; shift 2 ;;
        --dry-run)  DRY_RUN=true; shift ;;
        -h|--help)  usage; exit 0 ;;
        *)          echo "Unknown option: $1"; usage; exit 1 ;;
    esac
done

# Validation
if [[ -z "$VERSION" ]]; then
    echo "Error: --version is required"; usage; exit 1
fi

main() {
    log "Deploying version $VERSION to $ENVIRONMENT"
    if $DRY_RUN; then
        log "[DRY RUN] Would deploy $VERSION to $ENVIRONMENT"
    else
        log "Deployment complete"
    fi
}

main "$@"
```

### পাওয়ারশেল প্রোফাইল
```powershell
# Profile locations (run $PROFILE to see current):
# Current User, All Hosts: $HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
# Current User, VS Code:   $HOME\Documents\PowerShell\Microsoft.VSCode_profile.ps1

# Example profile content:
function prompt {
    $status = if ($?) { "+" } else { "-" }
    $path = Split-Path -Leaf -Path (Get-Location)
    "[$status] PS $path> "
}

Set-Alias -Name ll -Value Get-ChildItem
Set-Alias -Name grep -Value Select-String

Import-Module PSReadLine
Set-PSReadLineOption -PredictionSource History

function mkcd($dir) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    Set-Location $dir
}
```
---

## পরীক্ষা
### ব্যাট দিয়ে ব্যাশ টেস্টিং
```bash
#!/usr/bin/env bats
# test/utils.bats - test utility functions

setup() {
    source "$BATS_TEST_DIRNAME/../lib/utils.sh"
    export TEST_DIR="$(mktemp -d)"
}

teardown() {
    find "$TEST_DIR" -type f -delete 2>/dev/null || true
    rmdir "$TEST_DIR" 2>/dev/null || true
}

@test "log_info outputs formatted message" {
    run log_info "test message"
    [ "$status" -eq 0 ]
    [[ "$output" =~ "\[INFO\]" ]]
    [[ "$output" =~ "test message" ]]
}

@test "require_var fails on empty variable" {
    export MY_VAR=""
    run require_var "MY_VAR"
    [ "$status" -eq 1 ]
    [[ "$output" =~ "Required variable" ]]
}

@test "file_exists returns 0 for existing file" {
    touch "$TEST_DIR/test.txt"
    run file_exists "$TEST_DIR/test.txt"
    [ "$status" -eq 0 ]
}
```

### পেস্টারের সাথে পাওয়ারশেল টেস্টিং
```powershell
# tests/Deploy.Tests.ps1
BeforeAll {
    . "$PSScriptRoot/../scripts/Deploy.ps1"
}

Describe "Deploy-Application" {
    Context "Parameter validation" {
        It "Should throw when AppName is empty" {
            { Deploy-Application -AppName "" -Environment "dev" } | Should -Throw
        }

        It "Should reject invalid environment" {
            { Deploy-Application -AppName "myapp" -Environment "invalid" } | Should -Throw
        }

        It "Should accept valid parameters" {
            { Deploy-Application -AppName "myapp" -Environment "dev" -DryRun } |
                Should -Not -Throw
        }
    }

    Context "Deployment logic" {
        BeforeEach {
            Mock Invoke-Deployment { return $true } -ModuleName Deploy
            Mock Write-Host { } -ModuleName Deploy
        }

        It "Should call deployment for staging" {
            Deploy-Application -AppName "myapp" -Environment "staging"
            Should -Invoke Invoke-Deployment -Times 1
        }

        It "Should not deploy in dry-run mode" {
            Deploy-Application -AppName "myapp" -Environment "staging" -DryRun
            Should -Invoke Invoke-Deployment -Times 0
        }
    }
}

# Run tests:
# Invoke-Pester -Path ./tests -Output Detailed
```

### shunit2 দিয়ে শেল টেস্টিং
```bash
#!/bin/bash
# test/test_utils.sh
source "$(dirname "$0")/../lib/utils.sh"

test_log_info_outputs_message() {
    result=$(log_info "hello world" 2>&1)
    assertContains "$result" "[INFO]"
    assertContains "$result" "hello world"
}

test_require_var_fails_on_empty() {
    MY_VAR=""
    require_var "MY_VAR" 2>/dev/null
    assertEquals 1 $?
}

# Load and run shunit2
. shunit2
```
---

## ইন্টারঅপারেবিলিটি
### বহিরাগত প্রোগ্রাম কল করা
```bash
# Bash: calling external programs and capturing output
json_output=$(curl -s https://api.github.com/users/octocat)
name=$(echo "$json_output" | jq -r '.name')

# Capture exit code
curl -s -o /dev/null -w "%{http_code}" https://example.com
http_code=$?
if [[ $http_code -ne 0 ]]; then
    echo "Request failed with code $http_code"
fi

# Background processes and waiting
long_task &
pid=$!
echo "Started background task with PID $pid"
wait $pid
echo "Task completed with exit code $?"
```

### PowerShell .NET ইন্টারপ
```powershell
# Access any .NET class directly
[System.IO.File]::ReadAllText("config.json")
[System.Net.Dns]::GetHostAddresses("google.com")
[Math]::Round(3.14159, 2)

# Load and use a .NET assembly
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show("Hello from PowerShell!", "Title")

# COM interop (Windows-specific)
$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
$workbook = $excel.Workbooks.Open("C:\Reports\data.xlsx")
$sheet = $workbook.Sheets.Item(1)
$value = $sheet.Cells.Item(1, 1).Text
$workbook.Close($false)
$excel.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null

# REST API calls
$headers = @{ "Authorization" = "Bearer $token"; "Content-Type" = "application/json" }
$body = @{ name = "test"; value = 42 } | ConvertTo-Json

$response = Invoke-RestMethod -Uri "https://api.example.com/items" `
    -Method Post -Headers $headers -Body $body
$response | ConvertTo-Json -Depth 5
```
---

## ডিজাইন প্যাটার্ন
### প্যাটার্ন 1: ব্যাকঅফের সাথে পুনরায় চেষ্টা করুন (ব্যাশ)
```bash
#!/bin/bash
retry_with_backoff() {
    local max_attempts="${1}"
    local cmd="${2}"
    local attempt=1
    local delay=1

    while [[ $attempt -le $max_attempts ]]; do
        echo "Attempt $attempt/$max_attempts: $cmd"
        if eval "$cmd"; then
            echo "Success on attempt $attempt"
            return 0
        fi
        echo "Failed. Waiting ${delay}s before retry..."
        sleep "$delay"
        delay=$((delay * 2))  # Exponential backoff
        attempt=$((attempt + 1))
    done
    echo "All $max_attempts attempts failed"
    return 1
}

retry_with_backoff 5 "curl -sf https://api.example.com/health"
```

### প্যাটার্ন 2: কনফিগারেশন ম্যানেজমেন্ট (পাওয়ারশেল)
```powershell
class AppConfig {
    [string]$Environment
    [string]$DatabaseHost
    [int]$DatabasePort
    [string]$LogLevel

    static [AppConfig] Load([string]$path) {
        $raw = Get-Content $path -Raw | ConvertFrom-Json
        $config = [AppConfig]::new()
        $config.Environment = $raw.environment
        $config.DatabaseHost = $raw.database.host
        $config.DatabasePort = $raw.database.port
        $config.LogLevel = $raw.logLevel
        return $config
    }
}

$config = [AppConfig]::Load("./config.json")
```

### প্যাটার্ন 3: নিরাপদ ফাইল প্রসেসিং (ব্যাশ)
```bash
#!/bin/bash
# Process files safely, handling spaces and special characters
process_files() {
    local dir="${1:-.}"
    local count=0

    while IFS= read -r -d '' file; do
        echo "Processing: $(basename "$file")"
        count=$((count + 1))
    done < <(find "$dir" -name "*.txt" -print0)

    echo "Processed $count files"
}
```

### প্যাটার্ন 4: ট্র্যাপ-ভিত্তিক ত্রুটি হ্যান্ডলিং (ব্যাশ)
```bash
#!/bin/bash
set -euo pipefail

cleanup() {
    echo "Cleaning up temporary files..."
    # Cleanup logic here
}
trap cleanup EXIT

error_handler() {
    local line_no=$1
    local exit_code=$2
    echo "ERROR: Script failed at line $line_no with exit code $exit_code" >&2
    exit "$exit_code"
}
trap 'error_handler ${LINENO} $?' ERR

TEMP_DIR=$(mktemp -d)
echo "Working in $TEMP_DIR"
```

### প্যাটার্ন ৫: ডায়নামিক পাইপলাইন বিল্ডার (পাওয়ারশেল)
```powershell
function Build-Report {
    param([string]$DataSource, [switch]$IncludeInactive, [string]$SortBy = "Name")

    $pipeline = Get-Content $DataSource | ConvertFrom-Csv

    if (-not $IncludeInactive) {
        $pipeline = $pipeline | Where-Object { $_.Status -eq "Active" }
    }

    $pipeline | Sort-Object $SortBy | Format-Table -AutoSize
}
```
---

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### পাইপলাইন অপ্টিমাইজেশান
```bash
# BAD: unnecessary use of cat (UUOC)
cat file.txt | grep "pattern" | wc -l

# GOOD: let grep read the file directly
grep -c "pattern" file.txt

# Use LC_ALL=C for faster text processing (byte-level comparison)
LC_ALL=C sort large_file.txt
LC_ALL=C grep "pattern" large_file.txt

# Avoid subshells when possible (use built-in string operations)
# SLOW: count=$(echo "$string" | wc -c)
# FAST: count=${#string}
```

```powershell
# BAD: string concatenation in a loop
$result = ""
foreach ($i in 1..10000) { $result += "line $i`n" }

# GOOD: use StringBuilder
$sb = [System.Text.StringBuilder]::new()
foreach ($i in 1..10000) { [void]$sb.AppendLine("line $i") }
$result = $sb.ToString()

# Use .NET methods for file I/O (faster than cmdlets)
$lines = [System.IO.File]::ReadAllLines("large_file.txt")

# Measure performance
Measure-Command { Get-ChildItem -Recurse -Path "C:\Windows" } | Select-Object TotalSeconds
```
---

## স্থাপনা
### স্ক্রিপ্ট বিতরণ
```bash
# install.sh - Make scripts installable
#!/bin/bash
set -euo pipefail

INSTALL_DIR="/usr/local/bin"
SCRIPT_NAME="mytool"

echo "Installing $SCRIPT_NAME to $INSTALL_DIR..."
cp "$SCRIPT_NAME.sh" "$INSTALL_DIR/$SCRIPT_NAME"
chmod +x "$INSTALL_DIR/$SCRIPT_NAME"
echo "Installed successfully."
```

```powershell
# Publish PowerShell module to PSGallery
$publishParams = @{
    Path       = "./MyModule"
    NuGetApiKey = $env:NUGET_API_KEY
    Repository = "PSGallery"
}
Publish-Module @publishParams
```

---

## কখন শেল/পাওয়ারশেল ব্যবহার করবেন
| দৃশ্যকল্প | কেন শেল/পাওয়ারশেল | ভাল বিকল্প |
|------------|--------------------------------------------|
| সিস্টেম প্রশাসন | আদর্শ টুল | জটিল অটোমেশনের জন্য পাইথন |
| CI/CD পাইপলাইন | DevOps-এ ইউনিভার্সাল | --- |
| ফাইল প্রসেসিং | সহজ কাজের জন্য দ্রুত | জটিল রূপান্তরের জন্য পাইথন |
| সার্ভার স্থাপনা | প্রতিটি সার্ভারের একটি শেল আছে | জটিল ইনফ্রার জন্য উত্তরযোগ্য/টেরাফর্ম |
| লগ বিশ্লেষণ | দ্রুত গ্রেপ/ওক ওয়ান-লাইনার | পাইথন, জটিল বিশ্লেষণের জন্য এসকিউএল |
| জটিল অ্যাপ্লিকেশন | উপযুক্ত নয় | পাইথন, গো, জাভা |
| ক্রস-প্ল্যাটফর্ম স্ক্রিপ্ট | PowerShell 7+ সর্বত্র কাজ করে | সত্যিই পোর্টেবল স্ক্রিপ্টের জন্য পাইথন |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: ব্যাশে একক এবং ডবল উদ্ধৃতির মধ্যে পার্থক্য কী?
**A:** ডবল উদ্ধৃতি পরিবর্তনশীল সম্প্রসারণের অনুমতি দেয়; একক উদ্ধৃতি আক্ষরিক:
```bash
name="World"
echo "Hello, $name"   # Hello, World
echo 'Hello, $name'   # Hello, $name

# Backticks vs $() for command substitution
echo "Today is $(date +%A)"   # preferred
echo "Today is `date +%A`"    # older syntax, avoid
```

### প্রশ্ন 2: শেল স্ক্রিপ্টে আমি কীভাবে ত্রুটিগুলি পরিচালনা করব?
**A:** ত্রুটি থেকে প্রস্থান করতে`set -e`ব্যবহার করুন এবং পরিষ্কারের জন্য ফাঁদ:
```bash
#!/bin/bash
set -euo pipefail   # exit on error, undefined vars, pipe failures

cleanup() {
    rm -f "$tmpfile"
}
trap cleanup EXIT

tmpfile=$(mktemp)
echo "Working..."
# Script exits on any error, cleanup runs on exit
```

### প্রশ্ন 3: আমি কিভাবে কমান্ড-লাইন আর্গুমেন্ট সঠিকভাবে প্রক্রিয়া করব?
**A:** পতাকা এবং অবস্থানগত প্যারামিটারের জন্য`getopts`ব্যবহার করুন:
```bash
#!/bin/bash
usage() { echo "Usage: $0 [-v] [-o output] <input>"; exit 1; }

verbose=false
output="default.txt"

while getopts "vo:h" opt; do
    case $opt in
        v) verbose=true ;;
        o) output="$OPTARG" ;;
        h) usage ;;
        *) usage ;;
    esac
done
shift $((OPTIND - 1))
input="${1:?Input file required}"
```

### প্রশ্ন 4: পাওয়ারশেল পাইপলাইন কী এবং এটি ব্যাশ থেকে কীভাবে আলাদা?
**A:** PowerShell বস্তুকে পাইপ করে, পাঠ্য নয়। প্রতিটি বস্তু তার বৈশিষ্ট্য বজায় রাখে:
```powershell
# Bash: text-based pipeline
ps aux | grep chrome | awk '{print $2}'

# PowerShell: object-based pipeline
Get-Process chrome | Select-Object Id, WorkingSet64

# Each object has properties and methods
(Get-Process chrome).GetType()  # System.Diagnostics.Process
```

### প্রশ্ন 5: আমি কিভাবে ক্রস-প্ল্যাটফর্ম স্ক্রিপ্ট লিখব?
**A:** Bash এর জন্য:`#!/usr/bin/env bash`ব্যবহার করুন, GNU-নির্দিষ্ট পতাকা এড়িয়ে চলুন। পাওয়ারশেলের জন্য:`pwsh`(PowerShell Core) ব্যবহার করুন যা Linux/macOS/Windows-এ চলে।
---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: ব্যাচ ইমেজ প্রসেসিং স্ক্রিপ্ট (ব্যাশ)
**ধাপ 1: সমস্যাটি বুঝুন**
একটি ডিরেক্টরিতে থাকা সমস্ত PNG চিত্রের সর্বোচ্চ 800px প্রস্থে আকার পরিবর্তন করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
ফাইলগুলি সনাক্ত করতে`find`এবং আকার পরিবর্তন করতে`convert`(ImageMagick) ব্যবহার করুন৷
**ধাপ 3: প্রয়োগ করুন**```bash
#!/bin/bash
set -euo pipefail

input_dir="${1:-.}"
output_dir="${2:-./resized}"
mkdir -p "$output_dir"

find "$input_dir" -maxdepth 1 -name '*.png' -type f | while read -r file; do
    filename=$(basename "$file")
    echo "Processing: $filename"
    convert "$file" -resize '800x800>' "$output_dir/$filename"
done

echo "Done. Resized $(ls "$output_dir"/*.png 2>/dev/null | wc -l) images."
```

**ধাপ 4: প্রসারিত করুন**
অগ্রগতি বার, দূষিত চিত্রগুলির জন্য ত্রুটি পরিচালনা এবং`xargs -P`এর সাথে সমান্তরাল প্রক্রিয়াকরণ যোগ করুন।
### সমস্যা 2: স্বয়ংক্রিয় লগ ঘূর্ণন (ব্যাশ)
**ধাপ 1: সমস্যাটি বুঝুন**
লগ ফাইলগুলি প্রতিদিন ঘোরান, পুরানো লগগুলি সংকুচিত করুন এবং 30 দিনের বেশি পুরানো লগগুলি মুছুন৷
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
সময়-ভিত্তিক ফিল্টার সহ`find`এবং কম্প্রেশনের জন্য`gzip`ব্যবহার করুন৷
**ধাপ 3: প্রয়োগ করুন**```bash
#!/bin/bash
set -euo pipefail

LOG_DIR="/var/log/myapp"
RETENTION_DAYS=30

# Compress logs older than 1 day
find "$LOG_DIR" -name '*.log' -mtime +1 -exec gzip {} \;

# Delete compressed logs older than retention period
find "$LOG_DIR" -name '*.log.gz' -mtime +$RETENTION_DAYS -delete

# Report
compressed=$(find "$LOG_DIR" -name '*.log.gz' | wc -l)
echo "Active logs: $(find "$LOG_DIR" -name '*.log' | wc -l)"
echo "Compressed: $compressed"
```

**ধাপ 4: সময়সূচী**
ক্রনট্যাবে যোগ করুন: `0 2 * * * /usr/local/bin/log-rotate.sh`
### সমস্যা 3: উইন্ডোজ সার্ভিস হেলথ চেক (পাওয়ারশেল)
**ধাপ 1: সমস্যাটি বুঝুন**
গুরুত্বপূর্ণ পরিষেবাগুলি চলছে কিনা তা পরীক্ষা করুন এবং কোনও বন্ধ হয়ে গেলে একটি সতর্কতা পাঠান৷
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
`Get-Service` ব্যবহার করুন এবং বন্ধ পরিষেবাগুলির জন্য ফিল্টার করুন৷
**ধাপ 3: প্রয়োগ করুন**```powershell
$criticalServices = @('wuauserv', 'BITS', 'WinRM', 'Spooler')

$results = foreach ($svc in $criticalServices) {
    $service = Get-Service -Name $svc -ErrorAction SilentlyContinue
    [PSCustomObject]@{
        Name   = $svc
        Status = if ($service) { $service.Status } else { 'NotFound' }
    }
}

$stopped = $results | Where-Object { $_.Status -ne 'Running' }
if ($stopped) {
    Write-Warning "Services not running:"
    $stopped | Format-Table -AutoSize
    # Send-MailMessage or webhook alert here
}
```

**ধাপ 4: স্বয়ংক্রিয়**
প্রতি 5 মিনিটে চলমান একটি উইন্ডোজ টাস্ক শিডিউলারের কাজ হিসাবে সময়সূচী করুন।
---

## সারাংশ
শেল স্ক্রিপ্টিং (ব্যাশ এবং পাওয়ারশেল) কম্পিউটারের সাথে কাজ করে এমন প্রত্যেকের জন্য একটি অপরিহার্য দক্ষতা। ব্যাশ লিনাক্স/ম্যাকওএস পরিবেশ এবং ডিওঅপস-এ আধিপত্য বিস্তার করে। PowerShell একটি আরো আধুনিক, অবজেক্ট-ভিত্তিক পদ্ধতির অফার করে এবং এটি উইন্ডোজ প্রশাসনের জন্য অপরিহার্য। উভয়ই একটি আধুনিক প্রযুক্তির স্ট্যাকে প্রয়োজন। শেল স্ক্রিপ্টগুলি হল আঠা যা সিস্টেমগুলিকে সংযুক্ত করে, কর্মপ্রবাহকে স্বয়ংক্রিয় করে এবং কাজগুলি দ্রুত সম্পন্ন করে।