---
# Metadata
title: "Shell & PowerShell"
description: "Comprehensive reference for the Shell and PowerShell programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "AI Model Training Team"
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
# 쉘 및 파워셸
쉘 스크립팅은 명령줄 해석기용 스크립트 작성을 의미합니다. 가장 중요한 두 가지 셸은 Linux 및 macOS의 기본값인 **Bash**(Bourne Again Shell)와 Microsoft의 최신 크로스 플랫폼 셸 및 스크립팅 언어인 **PowerShell**입니다. 셸 스크립트는 시스템 관리 작업, 빌드 파이프라인, 파일 처리 및 배포 워크플로를 자동화합니다.
모든 개발자, DevOps 엔지니어 및 시스템 관리자는 셸 스크립팅 기술이 필요합니다. 웹 서버 배포, 로그 파일 처리, CI/CD 파이프라인 설정, 백업 자동화 등 어떤 작업을 하든 셸 스크립팅은 작업을 위한 도구입니다.
---

## 쉘/PowerShell이 ​​중요한 이유
- **자동화**: 파일 관리, 배포, 시스템 구성 등 반복적인 작업을 자동화합니다.
- **DevOps 필수**: CI/CD 파이프라인(GitHub Actions, Jenkins), Docker, Kubernetes는 모두 셸 스크립트를 사용합니다.
- **범용**: 모든 서버, 클라우드 인스턴스 및 컨테이너에는 셸이 있습니다.
- **PowerShell의 개체 파이프라인**: Bash와 달리 PowerShell은 텍스트가 아닌 개체를 전달하므로 복잡한 작업이 더 쉬워집니다.
- **크로스 플랫폼(PowerShell)**: PowerShell 7+는 Windows, macOS 및 Linux에서 실행됩니다.
- **빠르고 더러운**: 명령줄에서 일회성 문제를 해결하는 가장 빠른 방법입니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **Bash의 단점** | 일관성 없는 구문, 깨지기 쉬운 문자열 처리 |`set -euo pipefail`사용; 인용 변수; 복잡한 스크립트에는 PowerShell을 선호합니다 |
| **복잡한 프로그램에는 적합하지 않음** | 열악한 데이터 구조, OOP 없음, 테스트하기 어려움 | 복잡한 논리에 Python, Go 또는 기타 언어 사용 |
| **오류 처리** | Bash 오류 처리는 기본적입니다 |`set -e`사용; 종료 코드를 확인하세요. PowerShell의 try/catch 사용 |
| **이식성** | Bash 스크립트가 모든 시스템에서 작동하지 않을 수 있음 | 이식성을 극대화하려면 POSIX sh를 사용하십시오. 크로스 플랫폼용 PowerShell |
| **디버깅** | 제한된 디버깅 도구 | Bash에는 `set -x`를 사용하세요. PowerShell에는 적절한 디버거가 있습니다 |
---

## 배시 구문
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

## 파워셸 구문
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

## 고급 구문 및 패턴
### 고급 Bash 파이핑 및 리디렉션
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

### 고급 PowerShell 패턴
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

### 셸의 정규식
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

### PowerShell 정규식 및 텍스트 처리
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

## 핵심 기능 심층 분석
### 파이프라인 패턴
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
### 모듈 시스템
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

## 프로젝트 구성 및 빌드 시스템
### 스크립트 구조 모범 사례
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

### PowerShell 프로필
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

## 테스트
### 박쥐를 이용한 Bash 테스트
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

### Pester를 사용한 PowerShell 테스트
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

### shunit2를 사용한 쉘 테스트
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

## 상호 운용성
### 외부 프로그램 호출
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

### 파워셸 .NET 상호 운용성
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

## 디자인 패턴
### 패턴 1: 백오프로 재시도(Bash)
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

### 패턴 2: 구성 관리(PowerShell)
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

### 패턴 3: 안전한 파일 처리(Bash)
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

### 패턴 4: 트랩 기반 오류 처리(Bash)
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

### 패턴 5: 동적 파이프라인 빌더(PowerShell)
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

## 성능 및 최적화
### 파이프라인 최적화
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

## 배포
### 스크립트 배포
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

## 쉘/PowerShell을 사용해야 하는 경우
| 시나리오 | 쉘/PowerShell을 선택해야 하는 이유 | 더 나은 대안 |
|----------|---------|------|
| 시스템 관리 | 표준 도구 | 복잡한 자동화를 위한 Python |
| CI/CD 파이프라인 | DevOps의 범용 | --- |
| 파일 처리 | 간단한 작업을 빠르게 수행 | 복잡한 변환을 위한 Python |
| 서버 배포 | 모든 서버에는 쉘이 있습니다 | 복잡한 인프라를 위한 Ansible/Terraform |
| 로그 분석 | 빠른 grep/awk 한 줄짜리 | 복잡한 분석을 위한 Python, SQL |
| 복잡한 애플리케이션 | 적합하지 않음 | 파이썬, 바둑, 자바 |
| 크로스 플랫폼 스크립트 | PowerShell 7+는 어디에서나 작동합니다 | 진정한 이식성 스크립트를 위한 Python |
---

## 요약
쉘 스크립팅(Bash 및 PowerShell)은 컴퓨터를 사용하는 모든 사람에게 필수적인 기술입니다. Bash는 Linux/macOS 환경과 DevOps를 지배합니다. PowerShell은 보다 현대적인 개체 지향 접근 방식을 제공하며 Windows 관리에 필수적입니다. 현대 기술 스택에는 둘 다 필요합니다. 쉘 스크립트는 시스템을 연결하고, 워크플로우를 자동화하고, 작업을 신속하게 완료하는 접착제입니다.