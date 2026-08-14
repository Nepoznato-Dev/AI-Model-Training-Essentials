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
# Powłoka i PowerShell
Skrypty powłoki odnoszą się do pisania skryptów dla interpreterów wiersza poleceń. Dwie najważniejsze powłoki to **Bash** (Bourne Again Shell) — domyślna w systemach Linux i macOS — oraz **PowerShell** — nowoczesna wieloplatformowa powłoka i język skryptowy firmy Microsoft. Skrypty powłoki automatyzują zadania administracyjne systemu, tworzą potoki, przetwarzają pliki i przepływy pracy związane z wdrażaniem.
Każdy programista, inżynier DevOps i administrator systemu potrzebuje umiejętności pisania skryptów powłoki. Niezależnie od tego, czy wdrażasz serwer WWW, przetwarzasz pliki dziennika, konfigurujesz potoki CI/CD, czy automatyzujesz kopie zapasowe, skrypty powłoki są narzędziem do tego zadania.
---

## Dlaczego Shell/PowerShell ma znaczenie
- **Automatyzacja**: Automatyzuj powtarzalne zadania — zarządzanie plikami, wdrożenia, konfiguracja systemu.
- **Niezbędne DevOps**: Potoki CI/CD (GitHub Actions, Jenkins), Docker, Kubernetes używają skryptów powłoki.
- **Uniwersalny**: każdy serwer, instancja w chmurze i kontener ma powłokę.
- **Potok obiektowy PowerShell**: W przeciwieństwie do Bash, PowerShell przekazuje obiekty, a nie tekst, co ułatwia złożone operacje.
- ** Wieloplatformowy (PowerShell)**: PowerShell 7+ działa w systemach Windows, macOS i Linux.
- **Szybko i brudno**: Najszybszy sposób rozwiązania jednorazowego problemu w wierszu poleceń.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Dziwactwa Basha** | Niespójna składnia, delikatna obsługa ciągów | Użyj`set -euo pipefail`; cytować zmienne; preferuj PowerShell dla złożonych skryptów |
| **Nie dla skomplikowanych programów** | Słabe struktury danych, brak OOP, trudne do przetestowania | Używaj Pythona, Go lub innych języków do obsługi złożonej logiki |
| **Obsługa błędów** | Obsługa błędów Bash jest prymitywna | Użyj`set -e`; sprawdź kody wyjścia; użyj try/catch | programu PowerShell
| **Przenośność** | Skrypty Bash mogą nie działać na wszystkich systemach | Użyj POSIX sh, aby uzyskać maksymalną przenośność; PowerShell dla wielu platform |
| **Debugowanie** | Ograniczone narzędzia do debugowania | Użyj`set -x`dla Bash; PowerShell ma odpowiedni debuger |
---

## Składnia Basha
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

## Składnia programu PowerShell
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

## Zaawansowana składnia i wzorce
### Zaawansowane potokowanie i przekierowanie Bash
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

### Zaawansowane wzorce PowerShell
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

### Wyrażenia regularne w powłoce
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

### PowerShell Regex i przetwarzanie tekstu
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

## Zagłęb się w podstawowe funkcje
### Wzory rurociągów
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
### Systemy modułowe
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

## Konfiguracja projektu i budowanie systemu
### Najlepsze praktyki dotyczące struktury skryptu
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

### Profile programu PowerShell
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

## Testowanie
### Testowanie Bash z nietoperzami
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

### Testowanie programu PowerShell za pomocą szkodnika
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

### Testowanie powłoki za pomocą shunit2
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

## Interoperacyjność
### Wywoływanie programów zewnętrznych
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

### Współpraca programu PowerShell z platformą .NET
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

## Wzorce projektowe
### Wzorzec 1: Ponów próbę z wycofaniem (Bash)
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

### Wzorzec 2: Zarządzanie konfiguracją (PowerShell)
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

### Wzorzec 3: Bezpieczne przetwarzanie plików (Bash)
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

### Wzorzec 4: Obsługa błędów oparta na pułapkach (Bash)
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

### Wzorzec 5: Dynamiczny kreator potoków (PowerShell)
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

## Wydajność i optymalizacja
### Optymalizacja rurociągu
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

## Zastosowanie
### Dystrybucja skryptów
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

## Kiedy używać powłoki/PowerShell
| Scenariusz | Dlaczego Shell/PowerShell | Lepsza alternatywa |
|---------|---------------------|--------------------------------|
| Administracja systemem | Standardowe narzędzie | Python do złożonej automatyzacji |
| Rurociągi CI/CD | Uniwersalny w DevOps | --- |
| Przetwarzanie plików | Szybki do prostych zadań | Python do złożonych przekształceń |
| Wdrożenie serwera | Każdy serwer ma powłokę | Ansible/Terraform dla złożonej infrastruktury |
| Analiza dziennika | Szybkie jednowierszowe grep/awk | Python, SQL do kompleksowej analizy |
| Złożone aplikacje | Nie nadaje się | Python, Go, Java |
| Skrypty wieloplatformowe | PowerShell 7+ działa wszędzie | Python dla prawdziwie przenośnych skryptów |
---

## Syntetyczne pytania i odpowiedzi
### P1: Jaka jest różnica między cudzysłowami pojedynczymi i podwójnymi w języku Bash?
**A:** Podwójne cudzysłowy umożliwiają zmienne rozwinięcie; pojedyncze cudzysłowy są dosłowne:
```bash
name="World"
echo "Hello, $name"   # Hello, World
echo 'Hello, $name'   # Hello, $name

# Backticks vs $() for command substitution
echo "Today is $(date +%A)"   # preferred
echo "Today is `date +%A`"    # older syntax, avoid
```

### P2: Jak radzić sobie z błędami w skryptach powłoki?
**A:** Użyj `set -e`, aby wyjść w przypadku błędów i zastosować pułapkę w celu oczyszczenia:
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

### P3: Jak prawidłowo przetwarzać argumenty wiersza poleceń?
**A:** Użyj`getopts`dla flag i parametrów pozycyjnych:
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

### P4: Co to jest potok PowerShell i czym różni się od Bash?
**O:** PowerShell przesyła obiekty, a nie tekst. Każdy obiekt zachowuje swoje właściwości:
```powershell
# Bash: text-based pipeline
ps aux | grep chrome | awk '{print $2}'

# PowerShell: object-based pipeline
Get-Process chrome | Select-Object Id, WorkingSet64

# Each object has properties and methods
(Get-Process chrome).GetType()  # System.Diagnostics.Process
```

### P5: Jak pisać skrypty wieloplatformowe?
**A:** Dla Bash: użyj`#!/usr/bin/env bash`, unikaj flag specyficznych dla GNU. W przypadku PowerShell: użyj`pwsh`(PowerShell Core), który działa w systemie Linux/macOS/Windows.
---

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Skrypt przetwarzania wsadowego obrazu (Bash)
**Krok 1: Zrozum problem**
Zmień rozmiar wszystkich obrazów PNG w katalogu na maksymalną szerokość 800 pikseli.
**Krok 2: Zidentyfikuj podejście**
Użyj `find`, aby zlokalizować pliki i`convert`(ImageMagick), aby zmienić rozmiar.
**Krok 3: Wdróż**```bash
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

**Krok 4: Przedłuż**
Dodaj pasek postępu, obsługę błędów w przypadku uszkodzonych obrazów i przetwarzanie równoległe za pomocą`xargs -P`.
### Problem 2: Automatyczna rotacja logów (Bash)
**Krok 1: Zrozum problem**
Codziennie zmieniaj pliki dziennika, kompresuj stare dzienniki i usuwaj dzienniki starsze niż 30 dni.
**Krok 2: Zidentyfikuj podejście**
Użyj`find`z filtrami opartymi na czasie i`gzip`do kompresji.
**Krok 3: Wdróż**```bash
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

**Krok 4: Harmonogram**
Dodaj do crontaba: `0 2 * * * /usr/local/bin/log-rotate.sh`
### Problem 3: Sprawdzanie stanu usług Windows (PowerShell)
**Krok 1: Zrozum problem**
Sprawdź, czy działają krytyczne usługi i wyślij alert, jeśli jakiekolwiek zostaną zatrzymane.
**Krok 2: Zidentyfikuj podejście**
Użyj`Get-Service`i filtruj zatrzymane usługi.
**Krok 3: Wdróż**```powershell
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

**Krok 4: Automatyzuj**
Zaplanuj jako zadanie Harmonogramu zadań systemu Windows uruchamiane co 5 minut.
---

## Streszczenie
Obsługa skryptów powłoki (Bash i PowerShell) jest niezbędną umiejętnością każdego, kto pracuje z komputerami. Bash dominuje w środowiskach Linux/macOS i DevOps. PowerShell oferuje bardziej nowoczesne, obiektowe podejście i jest niezbędny do administrowania systemem Windows. Obydwa są potrzebne w nowoczesnym stosie technologii. Skrypty powłoki to spoiwo łączące systemy, automatyzujące przepływy pracy i umożliwiające szybkie wykonywanie zadań.