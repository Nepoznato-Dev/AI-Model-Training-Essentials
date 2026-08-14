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
# Shell & PowerShell
Tập lệnh Shell đề cập đến việc viết tập lệnh cho trình thông dịch dòng lệnh. Hai shell quan trọng nhất là **Bash** (Bourne Again Shell) — mặc định trên Linux và macOS — và **PowerShell** — shell và ngôn ngữ kịch bản đa nền tảng hiện đại của Microsoft. Các tập lệnh Shell tự động hóa các tác vụ quản trị hệ thống, xây dựng quy trình, xử lý tệp và quy trình triển khai.
Mọi nhà phát triển, kỹ sư DevOps và quản trị viên hệ thống đều cần có kỹ năng viết kịch bản shell. Cho dù bạn đang triển khai máy chủ web, xử lý tệp nhật ký, thiết lập đường dẫn CI/CD hay tự động sao lưu, tập lệnh shell là công cụ dành cho công việc đó.
---

## Tại sao Shell/PowerShell lại quan trọng
- **Tự động hóa**: Tự động hóa các tác vụ lặp đi lặp lại — quản lý tệp, triển khai, cấu hình hệ thống.
- **DevOps thiết yếu**: Quy trình CI/CD (GitHub Actions, Jenkins), Docker, Kubernetes đều sử dụng tập lệnh shell.
- **Universal**: Mọi máy chủ, phiên bản đám mây và vùng chứa đều có shell.
- **Đường dẫn đối tượng của PowerShell**: Không giống như Bash, PowerShell truyền đối tượng chứ không phải văn bản — giúp các thao tác phức tạp trở nên dễ dàng hơn.
- **Đa nền tảng (PowerShell)**: PowerShell 7+ chạy trên Windows, macOS và Linux.
- **Nhanh và bẩn**: Cách nhanh nhất để giải quyết vấn đề xảy ra một lần trên dòng lệnh.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Những điều kỳ quặc về Bash** | Cú pháp không nhất quán, xử lý chuỗi dễ vỡ | Sử dụng `set -euo pipefail`; trích dẫn các biến; thích PowerShell hơn cho các tập lệnh phức tạp |
| **Không dành cho các chương trình phức tạp** | Cấu trúc dữ liệu kém, không có OOP, khó kiểm tra | Sử dụng Python, Go hoặc các ngôn ngữ khác để xử lý logic phức tạp |
| **Xử lý lỗi** | Xử lý lỗi Bash còn nguyên thủy | Sử dụng `set -e`; kiểm tra mã thoát; sử dụng thử/bắt |
| **Tính di động** | Tập lệnh Bash có thể không hoạt động trên tất cả các hệ thống | Sử dụng POSIX sh để có tính di động tối đa; PowerShell cho đa nền tảng |
| **Gỡ lỗi** | Công cụ gỡ lỗi hạn chế | Sử dụng`set -x`cho Bash; PowerShell có trình gỡ lỗi thích hợp |
---

## Cú pháp Bash
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

## Cú pháp PowerShell
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

## Cú pháp và mẫu nâng cao
### Đường ống và chuyển hướng Bash nâng cao
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

### Mẫu PowerShell nâng cao
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

### Biểu thức chính quy trong Shell
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

### PowerShell Regex và xử lý văn bản
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

## Đi sâu vào các tính năng cốt lõi
### Mẫu đường ống
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
### Hệ thống mô-đun
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

## Cấu hình dự án & xây dựng hệ thống
### Các phương pháp hay nhất về cấu trúc tập lệnh
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

### Cấu hình PowerShell
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

##Thử nghiệm
### Thử nghiệm Bash với dơi
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

### Kiểm tra PowerShell bằng Pester
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

### Kiểm tra Shell với shunit2
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

## Khả năng tương tác
### Gọi các chương trình bên ngoài
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

### PowerShell .NET Interop
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

## Mẫu thiết kế
### Mẫu 1: Thử lại với Backoff (Bash)
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

### Mẫu 2: Quản lý cấu hình (PowerShell)
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

### Mẫu 3: Xử lý tệp an toàn (Bash)
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

### Mẫu 4: Xử lý lỗi dựa trên bẫy (Bash)
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

### Mẫu 5: Trình tạo đường ống động (PowerShell)
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

## Hiệu suất & Tối ưu hóa
### Tối ưu hóa đường ống
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

## Triển khai
### Phân phối tập lệnh
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

## Khi nào nên sử dụng Shell/PowerShell
| Kịch bản | Tại sao Shell/PowerShell | Thay thế tốt hơn |
|----------|----------------------|-------------------|
| Quản trị hệ thống | Công cụ tiêu chuẩn | Python cho tự động hóa phức tạp |
| Đường ống CI/CD | Phổ biến trong DevOps | --- |
| Xử lý tập tin | Nhanh chóng cho các tác vụ đơn giản | Python cho các phép biến đổi phức tạp |
| Triển khai máy chủ | Mỗi máy chủ đều có shell | Ansible/Terraform cho cơ sở hạ tầng phức tạp |
| Phân tích nhật ký | Nhanh chóng grep/awk one-liners | Python, SQL để phân tích phức tạp |
| Ứng dụng phức tạp | Không phù hợp | Python, Go, Java |
| Tập lệnh đa nền tảng | PowerShell 7+ hoạt động ở mọi nơi | Python cho các tập lệnh thực sự di động |
---

## Hỏi đáp tổng hợp
### Q1: Sự khác biệt giữa dấu ngoặc đơn và dấu ngoặc kép trong Bash là gì?
**A:** Dấu ngoặc kép cho phép mở rộng biến; dấu ngoặc đơn là theo nghĩa đen:
```bash
name="World"
echo "Hello, $name"   # Hello, World
echo 'Hello, $name'   # Hello, $name

# Backticks vs $() for command substitution
echo "Today is $(date +%A)"   # preferred
echo "Today is `date +%A`"    # older syntax, avoid
```

### Câu 2: Làm cách nào để xử lý lỗi trong tập lệnh shell?
**A:** Sử dụng`set -e`để thoát khỏi lỗi và bẫy để dọn dẹp:
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

### Câu hỏi 3: Làm cách nào để xử lý các đối số dòng lệnh đúng cách?
**A:** Sử dụng`getopts`cho cờ và tham số vị trí:
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

### Câu hỏi 4: Đường dẫn PowerShell là gì và nó khác với Bash như thế nào?
**A:** PowerShell dẫn đối tượng chứ không phải văn bản. Mỗi đối tượng giữ lại các thuộc tính của nó:
```powershell
# Bash: text-based pipeline
ps aux | grep chrome | awk '{print $2}'

# PowerShell: object-based pipeline
Get-Process chrome | Select-Object Id, WorkingSet64

# Each object has properties and methods
(Get-Process chrome).GetType()  # System.Diagnostics.Process
```

### Câu 5: Làm cách nào để viết tập lệnh đa nền tảng?
**A:** Đối với Bash: sử dụng`#!/usr/bin/env bash`, tránh các cờ dành riêng cho GNU. Đối với PowerShell: sử dụng`pwsh`(PowerShell Core) chạy trên Linux/macOS/Windows.
---

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Tập lệnh xử lý ảnh hàng loạt (Bash)
**Bước 1: Tìm hiểu vấn đề**
Thay đổi kích thước tất cả hình ảnh PNG trong một thư mục thành chiều rộng tối đa 800px.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng`find`để định vị tệp và`convert`(ImageMagick) để thay đổi kích thước.
**Bước 3: Thực hiện**```bash
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

**Bước 4: Gia hạn**
Thêm thanh tiến trình, xử lý lỗi đối với hình ảnh bị hỏng và xử lý song song với `xargs -P`.
### Vấn đề 2: Tự động xoay vòng nhật ký (Bash)
**Bước 1: Tìm hiểu vấn đề**
Xoay tệp nhật ký hàng ngày, nén nhật ký cũ và xóa nhật ký cũ hơn 30 ngày.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng`find`với các bộ lọc dựa trên thời gian và`gzip`để nén.
**Bước 3: Thực hiện**```bash
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

**Bước 4: Lên lịch**
Thêm vào crontab: `0 2 * * * /usr/local/bin/log-rotate.sh`
### Vấn đề 3: Kiểm tra tình trạng dịch vụ Windows (PowerShell)
**Bước 1: Tìm hiểu vấn đề**
Kiểm tra xem các dịch vụ quan trọng có đang chạy hay không và gửi cảnh báo nếu có dịch vụ nào bị dừng.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng`Get-Service`và lọc các dịch vụ đã dừng.
**Bước 3: Thực hiện**```powershell
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

**Bước 4: Tự động hóa**
Lập lịch dưới dạng công việc Lập lịch tác vụ Windows chạy 5 phút một lần.
---

## Bản tóm tắt
Viết kịch bản Shell (Bash và PowerShell) là một kỹ năng cần thiết cho bất kỳ ai làm việc với máy tính. Bash thống trị môi trường Linux/macOS và DevOps. PowerShell cung cấp một cách tiếp cận hướng đối tượng, hiện đại hơn và rất cần thiết cho việc quản trị Windows. Cả hai đều cần thiết trong nền tảng công nghệ hiện đại. Tập lệnh Shell là chất keo kết nối các hệ thống, tự động hóa quy trình làm việc và hoàn thành công việc một cách nhanh chóng.