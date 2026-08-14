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
# شیل اور پاور شیل
شیل اسکرپٹنگ سے مراد کمانڈ لائن ترجمانوں کے لیے اسکرپٹ لکھنا ہے۔ دو اہم ترین شیل ہیں **باش** (بورن اگین شیل) — لینکس اور میک او ایس پر ڈیفالٹ — اور ** پاور شیل** — مائیکروسافٹ کا جدید کراس پلیٹ فارم شیل اور اسکرپٹنگ لینگویج۔ شیل اسکرپٹس سسٹم ایڈمنسٹریشن کے کاموں کو خودکار بناتی ہیں، پائپ لائنیں بناتی ہیں، فائل پروسیسنگ، اور تعیناتی ورک فلو کرتی ہیں۔
ہر ڈویلپر، DevOps انجینئر، اور سسٹم ایڈمنسٹریٹر کو شیل اسکرپٹنگ کی مہارتوں کی ضرورت ہوتی ہے۔ چاہے آپ ویب سرور تعینات کر رہے ہوں، لاگ فائلوں پر کارروائی کر رہے ہوں، CI/CD پائپ لائنیں ترتیب دے رہے ہوں، یا بیک اپ کو خودکار کر رہے ہوں، شیل اسکرپٹنگ اس کام کا ٹول ہے۔
---

## شیل/پاور شیل کیوں اہمیت رکھتا ہے۔
- **آٹومیشن**: دہرائے جانے والے کاموں کو خودکار بنائیں — فائل کا انتظام، تعیناتیاں، سسٹم کنفیگریشن۔
- **DevOps ضروری**: CI/CD پائپ لائنز (GitHub ایکشنز، Jenkins)، Docker، Kubernetes سبھی شیل اسکرپٹ استعمال کرتے ہیں۔
- **یونیورسل**: ہر سرور، کلاؤڈ مثال، اور کنٹینر میں ایک شیل ہوتا ہے۔
- **PowerShell کی آبجیکٹ پائپ لائن**: Bash کے برعکس، PowerShell اشیاء کو پاس کرتا ہے، ٹیکسٹ نہیں - پیچیدہ آپریشنز کو آسان بناتا ہے۔
- **کراس پلیٹ فارم (پاور شیل)**: پاور شیل 7+ ونڈوز، میک او ایس اور لینکس پر چلتا ہے۔
- **فوری اور گندا**: کمانڈ لائن پر یک طرفہ مسئلہ حل کرنے کا تیز ترین طریقہ۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **بش کی باتیں** | متضاد نحو، نازک سٹرنگ ہینڈلنگ |`set -euo pipefail`استعمال کریں؛ اقتباس متغیر؛ پیچیدہ اسکرپٹس کے لیے پاور شیل کو ترجیح دیں |
| ** پیچیدہ پروگراموں کے لیے نہیں** | ناقص ڈیٹا سٹرکچر، کوئی OOP نہیں، جانچنا مشکل | پیچیدہ منطق کے لیے Python، Go، یا دوسری زبانیں استعمال کریں۔
| **خرابی کو سنبھالنا** | Bash ایرر ہینڈلنگ قدیم ہے |`set -e`استعمال کریں؛ باہر نکلنے کے کوڈ چیک کریں؛ پاور شیل کی کوشش/کیچ | استعمال کریں۔
| **پورٹیبلٹی** | باش اسکرپٹس تمام سسٹمز پر کام نہیں کر سکتے ہیں | زیادہ سے زیادہ پورٹیبلٹی کے لیے POSIX sh استعمال کریں۔ کراس پلیٹ فارم کے لیے پاور شیل |
| **ڈیبگنگ** | محدود ڈیبگنگ ٹولز | Bash کے لیے`set -x`استعمال کریں۔ پاور شیل کے پاس مناسب ڈیبگر ہے۔
---

## باش نحو
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

## پاور شیل نحو
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

## اعلی درجے کی نحو اور نمونے۔
### ایڈوانسڈ باش پائپنگ اور ری ڈائریکشن
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

### اعلی درجے کی پاور شیل پیٹرنز
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

### شیل میں باقاعدہ اظہار
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

### پاور شیل ریجیکس اور ٹیکسٹ پروسیسنگ
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

## بنیادی خصوصیات میں گہرا غوطہ لگائیں۔
### پائپ لائن پیٹرن
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
### ماڈیول سسٹمز
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### اسکرپٹ کی ساخت کے بہترین طریقے
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

### پاور شیل پروفائلز
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

## ٹیسٹنگ
### چمگادڑوں کے ساتھ بیش ٹیسٹنگ
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

### پیسٹر کے ساتھ پاور شیل ٹیسٹنگ
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

### shunit2 کے ساتھ شیل ٹیسٹنگ
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

## انٹرآپریبلٹی
### بیرونی پروگراموں کو کال کرنا
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

### پاور شیل .NET انٹراپ
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

## ڈیزائن پیٹرن
### پیٹرن 1: بیک آف کے ساتھ دوبارہ کوشش کریں (باش)
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

### پیٹرن 2: کنفیگریشن مینجمنٹ (PowerShell)
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

### پیٹرن 3: محفوظ فائل پروسیسنگ (باش)
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

### پیٹرن 4: ٹریپ پر مبنی ایرر ہینڈلنگ (باش)
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

### پیٹرن 5: ڈائنامک پائپ لائن بلڈر (پاور شیل)
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

## کارکردگی اور اصلاح
### پائپ لائن کی اصلاح
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

## تعیناتی۔
### اسکرپٹ کی تقسیم
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

## شیل/پاور شیل کب استعمال کریں۔
| منظر نامہ | کیوں شیل/پاور شیل | بہتر متبادل |
|------------|--------------------------------------------|
| سسٹم ایڈمنسٹریشن | معیاری ٹول | پیچیدہ آٹومیشن کے لیے ازگر |
| CI/CD پائپ لائنز | DevOps میں یونیورسل | --- |
| فائل پروسیسنگ | آسان کاموں کے لیے تیز | پیچیدہ تبدیلیوں کے لیے ازگر |
| سرور کی تعیناتی | ہر سرور کا ایک شیل ہوتا ہے | پیچیدہ انفرا کے لیے قابل جواب/ٹیرافارم |
| لاگ تجزیہ | فوری گریپ/اوک ون لائنرز | Python، SQL پیچیدہ تجزیہ کے لیے |
| پیچیدہ ایپلی کیشنز | مناسب نہیں | ازگر، گو، جاوا |
| کراس پلیٹ فارم اسکرپٹس | PowerShell 7+ ہر جگہ کام کرتا ہے | صحیح معنوں میں پورٹیبل اسکرپٹس کے لیے ازگر |
---

## مصنوعی سوال و جواب
### Q1: Bash میں سنگل اور ڈبل کوٹس میں کیا فرق ہے؟
**A:** دوہری قیمتیں متغیر کی توسیع کی اجازت دیتی ہیں۔ واحد اقتباسات لفظی ہیں:
```bash
name="World"
echo "Hello, $name"   # Hello, World
echo 'Hello, $name'   # Hello, $name

# Backticks vs $() for command substitution
echo "Today is $(date +%A)"   # preferred
echo "Today is `date +%A`"    # older syntax, avoid
```

### Q2: میں شیل اسکرپٹ میں غلطیوں کو کیسے ہینڈل کروں؟
**A:** غلطیوں سے باہر نکلنے کے لیے`set -e`استعمال کریں، اور صفائی کے لیے ٹریپ:
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

### Q3: میں کمانڈ لائن آرگیومنٹ کو صحیح طریقے سے کیسے پروسیس کروں؟
**A:** جھنڈوں اور پوزیشنی پیرامیٹرز کے لیے`getopts`استعمال کریں:
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

### Q4: PowerShell پائپ لائن کیا ہے اور یہ Bash سے کیسے مختلف ہے؟
**A:** PowerShell اشیاء کو پائپ کرتا ہے، ٹیکسٹ نہیں۔ ہر چیز اپنی خصوصیات کو برقرار رکھتی ہے:
```powershell
# Bash: text-based pipeline
ps aux | grep chrome | awk '{print $2}'

# PowerShell: object-based pipeline
Get-Process chrome | Select-Object Id, WorkingSet64

# Each object has properties and methods
(Get-Process chrome).GetType()  # System.Diagnostics.Process
```

### Q5: میں کراس پلیٹ فارم اسکرپٹ کیسے لکھ سکتا ہوں؟
**A:** Bash کے لیے:`#!/usr/bin/env bash`استعمال کریں، GNU مخصوص جھنڈوں سے بچیں۔ پاور شیل کے لیے:`pwsh`(PowerShell Core) استعمال کریں جو Linux/macOS/Windows پر چلتا ہے۔
---

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: بیچ امیج پروسیسنگ اسکرپٹ (باش)
**مرحلہ 1: مسئلہ کو سمجھیں**
ڈائرکٹری میں تمام PNG امیجز کا سائز 800px کی زیادہ سے زیادہ چوڑائی تک تبدیل کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
فائلوں کو تلاش کرنے کے لیے`find`اور سائز تبدیل کرنے کے لیے`convert`(ImageMagick) کا استعمال کریں۔
**مرحلہ 3: نافذ کریں**```bash
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

**مرحلہ 4: توسیع کریں**
`xargs -P` کے ساتھ پروگریس بار، کرپٹ امیجز کے لیے ایرر ہینڈلنگ، اور متوازی پروسیسنگ شامل کریں۔
### مسئلہ 2: خودکار لاگ گردش (باش)
**مرحلہ 1: مسئلہ کو سمجھیں**
لاگ فائلوں کو روزانہ گھمائیں، پرانے لاگز کو کمپریس کریں، اور 30 دن سے زیادہ پرانے لاگز کو حذف کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
وقت پر مبنی فلٹرز کے ساتھ`find`اور کمپریشن کے لیے`gzip`استعمال کریں۔
**مرحلہ 3: نافذ کریں**```bash
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

**مرحلہ 4: شیڈول**
کرونٹاب میں شامل کریں: `0 2 * * * /usr/local/bin/log-rotate.sh`
### مسئلہ 3: ونڈوز سروس ہیلتھ چیک (پاور شیل)
**مرحلہ 1: مسئلہ کو سمجھیں**
چیک کریں کہ کیا اہم خدمات چل رہی ہیں اور اگر کوئی بند ہو تو الرٹ بھیجیں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
`Get-Service` استعمال کریں اور روکی ہوئی خدمات کے لیے فلٹر کریں۔
**مرحلہ 3: نافذ کریں**```powershell
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

**مرحلہ 4: خودکار**
ہر 5 منٹ میں ونڈوز ٹاسک شیڈیولر کام کے طور پر شیڈول کریں۔
---

## خلاصہ
شیل اسکرپٹنگ (باش اور پاور شیل) کمپیوٹر کے ساتھ کام کرنے والے ہر فرد کے لیے ایک ضروری مہارت ہے۔ Bash Linux/macOS ماحول اور DevOps پر حاوی ہے۔ PowerShell ایک زیادہ جدید، آبجیکٹ پر مبنی نقطہ نظر پیش کرتا ہے اور یہ ونڈوز انتظامیہ کے لیے ضروری ہے۔ جدید ٹیک اسٹیک میں دونوں کی ضرورت ہے۔ شیل اسکرپٹ وہ گلو ہے جو سسٹم کو جوڑتا ہے، ورک فلو کو خودکار کرتا ہے، اور کام کو تیزی سے انجام دیتا ہے۔