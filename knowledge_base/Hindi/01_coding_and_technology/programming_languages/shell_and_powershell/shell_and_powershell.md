---
# मेटाडेटा
शीर्षक: "शेल और पॉवरशेल"
विवरण: "शेल और पॉवरशेल प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स फंडामेंटल, इकोसिस्टम और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [शेल-एंड-पॉवरशेल, प्रोग्रामिंग-लैंग्वेज, सिंटैक्स, इकोसिस्टम, कोडिंग-एंड-टेक्नोलॉजी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का समय: "35 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# शैल और पॉवरशेल
शेल स्क्रिप्टिंग से तात्पर्य कमांड-लाइन दुभाषियों के लिए स्क्रिप्ट लिखने से है। दो सबसे महत्वपूर्ण शेल हैं **बैश** (बॉर्न अगेन शेल) - लिनक्स और मैकओएस पर डिफ़ॉल्ट - और **पॉवरशेल** - माइक्रोसॉफ्ट का आधुनिक क्रॉस-प्लेटफ़ॉर्म शेल और स्क्रिप्टिंग भाषा। शेल स्क्रिप्ट सिस्टम प्रशासन कार्यों को स्वचालित करती है, पाइपलाइनों का निर्माण करती है, फ़ाइल प्रोसेसिंग और परिनियोजन वर्कफ़्लोज़ का निर्माण करती है।
प्रत्येक डेवलपर, DevOps इंजीनियर और सिस्टम प्रशासक को शेल स्क्रिप्टिंग कौशल की आवश्यकता होती है। चाहे आप एक वेब सर्वर तैनात कर रहे हों, लॉग फ़ाइलों को संसाधित कर रहे हों, सीआई/सीडी पाइपलाइन स्थापित कर रहे हों, या बैकअप स्वचालित कर रहे हों, शेल स्क्रिप्टिंग इस काम के लिए उपकरण है।
---

## शेल/पावरशेल क्यों मायने रखता है
- **स्वचालन**: दोहराए जाने वाले कार्यों को स्वचालित करें - फ़ाइल प्रबंधन, परिनियोजन, सिस्टम कॉन्फ़िगरेशन।
- **डेवऑप्स आवश्यक**: सीआई/सीडी पाइपलाइन (गिटहब एक्शन, जेनकिंस), डॉकर, कुबेरनेट्स सभी शेल स्क्रिप्ट का उपयोग करते हैं।
- **यूनिवर्सल**: प्रत्येक सर्वर, क्लाउड इंस्टेंस और कंटेनर में एक शेल होता है।
- **पावरशेल की ऑब्जेक्ट पाइपलाइन**: बैश के विपरीत, पॉवरशेल ऑब्जेक्ट को पास करता है, टेक्स्ट को नहीं - जिससे जटिल संचालन आसान हो जाता है।
- **क्रॉस-प्लेटफ़ॉर्म (पावरशेल)**: पॉवरशेल 7+ विंडोज़, मैकओएस और लिनक्स पर चलता है।
- **त्वरित और गंदा**: कमांड लाइन पर एकबारगी समस्या को हल करने का सबसे तेज़ तरीका।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **बैश विचित्रताएँ** | असंगत वाक्यविन्यास, नाजुक स्ट्रिंग हैंडलिंग |`set -euo pipefail`का प्रयोग करें; उद्धरण चर; जटिल स्क्रिप्ट के लिए PowerShell को प्राथमिकता दें |
| **जटिल कार्यक्रमों के लिए नहीं** | ख़राब डेटा संरचनाएँ, कोई OOP नहीं, परीक्षण करना कठिन | जटिल तर्क के लिए पायथन, गो या अन्य भाषाओं का उपयोग करें |
| **त्रुटि प्रबंधन** | बैश त्रुटि प्रबंधन आदिम है |`set -e`का प्रयोग करें; निकास कोड की जाँच करें; PowerShell के प्रयास/पकड़ का उपयोग करें |
| **पोर्टेबिलिटी** | बैश स्क्रिप्ट सभी सिस्टम पर काम नहीं कर सकती | अधिकतम पोर्टेबिलिटी के लिए POSIX sh का उपयोग करें; क्रॉस-प्लेटफ़ॉर्म के लिए पॉवरशेल |
| **डिबगिंग** | सीमित डिबगिंग उपकरण | बैश के लिए`set -x`का उपयोग करें; पॉवरशेल में एक उचित डिबगर है |
---

## बैश सिंटैक्स
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

## पॉवरशेल सिंटैक्स
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

## उन्नत सिंटैक्स और पैटर्न
### उन्नत बैश पाइपिंग और पुनर्निर्देशन
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

### उन्नत पावरशेल पैटर्न
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

### शैल में नियमित अभिव्यक्तियाँ
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

### पॉवरशेल रेगेक्स और टेक्स्ट प्रोसेसिंग
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

## मुख्य विशेषताओं में गहराई से उतरें
### पाइपलाइन पैटर्न
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
### मॉड्यूल सिस्टम
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### स्क्रिप्ट संरचना सर्वोत्तम अभ्यास
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

### पावरशेल प्रोफाइल
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

## परीक्षण
### बल्ले से बैश परीक्षण
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

### पेस्टर के साथ पावरशेल परीक्षण
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

### shunit2 के साथ शैल परीक्षण
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

## अंतरसंचालनीयता
### बाहरी प्रोग्राम को कॉल करना
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

### पॉवरशेल .NET इंटरऑप
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

## डिज़ाइन पैटर्न
### पैटर्न 1: बैकऑफ़ (बैश) के साथ पुनः प्रयास करें
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

### पैटर्न 2: कॉन्फ़िगरेशन प्रबंधन (पॉवरशेल)
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

### पैटर्न 3: सुरक्षित फ़ाइल प्रोसेसिंग (बैश)
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

### पैटर्न 4: ट्रैप-आधारित त्रुटि प्रबंधन (बैश)
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

### पैटर्न 5: डायनेमिक पाइपलाइन बिल्डर (पॉवरशेल)
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

## प्रदर्शन एवं अनुकूलन
### पाइपलाइन अनुकूलन
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

## तैनाती
### स्क्रिप्ट वितरण
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

## शेल/पॉवरशेल का उपयोग कब करें
| परिदृश्य | शेल/पॉवरशेल क्यों | बेहतर विकल्प |
|---|-----|-----|
| सिस्टम प्रशासन | मानक उपकरण | जटिल स्वचालन के लिए पायथन |
| सीआई/सीडी पाइपलाइन | DevOps में सार्वभौमिक | --- |
| फ़ाइल प्रोसेसिंग | सरल कार्यों के लिए तेज़ | जटिल परिवर्तनों के लिए पायथन |
| सर्वर परिनियोजन | प्रत्येक सर्वर में एक शेल होता है | जटिल इन्फ्रा के लिए अन्सिबल/टेराफॉर्म |
| लॉग विश्लेषण | त्वरित grep/awk वन-लाइनर्स | जटिल विश्लेषण के लिए पायथन, एसक्यूएल |
| जटिल अनुप्रयोग | अनुकूल नहीं | पायथन, गो, जावा |
| क्रॉस-प्लेटफ़ॉर्म स्क्रिप्ट | पॉवरशेल 7+ हर जगह काम करता है | वास्तव में पोर्टेबल स्क्रिप्ट के लिए पायथन |
---

## सारांश
शेल स्क्रिप्टिंग (बैश और पॉवरशेल) कंप्यूटर के साथ काम करने वाले किसी भी व्यक्ति के लिए एक आवश्यक कौशल है। बैश Linux/macOS परिवेश और DevOps पर हावी है। पॉवरशेल अधिक आधुनिक, ऑब्जेक्ट-ओरिएंटेड दृष्टिकोण प्रदान करता है और विंडोज़ प्रशासन के लिए आवश्यक है। आधुनिक तकनीकी स्टैक में दोनों की आवश्यकता है। शेल स्क्रिप्ट वह गोंद है जो सिस्टम को जोड़ती है, वर्कफ़्लो को स्वचालित करती है, और काम जल्दी पूरा करती है।