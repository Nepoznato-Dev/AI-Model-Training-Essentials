<!--
---
# Metadata
title: "Shell & PowerShell — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Shell and PowerShell ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [shell, powershell, bash, ecosystem, tooling, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# شیل اور پاور شیل - ایکو سسٹم اور ٹولنگ گائیڈ
اس گائیڈ میں شیل اسکرپٹنگ (Bash/Zsh) اور PowerShell کے لیے ضروری ٹولز، فریم ورک، اور انفراسٹرکچر کا احاطہ کیا گیا ہے۔
---

## شیل کے نفاذ
| شیل | پلیٹ فارم | نوٹس |
|---------|------------|------|
| **بش** | Unix/Linux/macOS | سب سے زیادہ استعمال کیا جاتا ہے |
| **Zsh** | macOS ڈیفالٹ | بہتر Bash |
| **مچھلی** | کراس پلیٹ فارم | صارف دوست |
| **ڈیش** | Debian/Ubuntu | تیز، POSIX کے مطابق |
| **ksh** | یونیکس | کارن شیل |
| **پاور شیل** | کراس پلیٹ فارم | آبجیکٹ پر مبنی (pwsh) |
| **نشیل** | کراس پلیٹ فارم | سٹرکچرڈ ڈیٹا شیل |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## پیکیج مینیجرز (شیل ٹولز)
| ٹول | مقصد |
|------|---------|
| **ہومبریو** | macOS/Linux پیکیج مینیجر |
| **apt/yum/dnf** | لینکس پیکیج مینیجر |
| **pkg** | فری بی ایس ڈی پیکیج مینیجر |
| **سکوپ** | ونڈوز CLI انسٹالر |
| **چاکلیٹی** | ونڈوز پیکج مینیجر |
| **ونگیٹ** | ونڈوز پیکج مینیجر |
```bash
# Homebrew
brew install jq ripgrep fd bat    # install tools
brew upgrade                      # upgrade all

# apt (Debian/Ubuntu)
sudo apt update && sudo apt install -y jq curl

# PowerShell
Install-Module -Name PSReadLine -Force
```

---

## ضروری CLI ٹولز
| ٹول | مقصد |
|------|---------|
| **jq** | JSON پروسیسنگ |
| **yq** | YAML پروسیسنگ |
| **ripgrep (rg)** | فاسٹ گریپ |
| **fd** | تیزی سے تلاش |
| **بلے* | بہتر بلی |
| **exa/eza** | بہتر ls |
| **fzf** | فجی فائنڈر |
| **htop** | عمل ناظر |
| **tmux** | ٹرمینل ملٹی پلیکسر |
| **curl/wget** | HTTP درخواستیں |
| **sed/awk** | ٹیکسٹ پروسیسنگ |
| **xargs** | ان پٹ سے کمانڈز بنائیں |
| **بناؤ** | ٹاسک رنر |
| **داخلہ** | فائل کی تبدیلیوں پر کمانڈ چلائیں |
| **متوازی** | متوازی عملدرآمد |
| **شیل چیک** | شیل اسکرپٹ لنٹر |
---

## شیل فریم ورک اور اضافہ
| ٹول | مقصد |
|------|---------|
| **Oh My Zsh** | Zsh فریم ورک (تھیمز، پلگ ان) |
| **پریزٹو** | Zsh فریم ورک (تیز) |
| **اسٹار شپ** | کراس شیل پرامپٹ |
| **zsh-خودکار تجاویز** | خودکار تجاویز |
| **zsh-نحو-ہائی لائٹنگ** | نحو کو نمایاں کرنا |
| **بش-اٹ** | باش فریم ورک |
| **atuin** | شیل کی تاریخ (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## پاور شیل ماڈیولز
| ماڈیول | مقصد |
|---------|---------|
| **PSReadLine** | بہتر کمانڈ لائن ایڈیٹنگ |
| **پیسٹر** | جانچ کا فریم ورک |
| **PSScriptAnalyzer** | لنٹنگ |
| **پاش گٹ** | گٹ انضمام |
| **ٹرمینل شبیہیں** | فائل شبیہیں |
| **PSWindows Update** | ونڈوز اپ ڈیٹس |
| **Az** | Azure مینجمنٹ |
| **AWSPowerShell** | AWS مینجمنٹ |
| **SqlServer** | ایس کیو ایل سرور مینجمنٹ |
| **پوڈ** | ویب فریم ورک |
| **یونیورسل ڈیش بورڈ** | ویب ڈیش بورڈز |
```powershell
# Install modules
Install-Module -Name PSReadLine -Force
Install-Module -Name Pester -Force
Install-Module -Name PSScriptAnalyzer -Force
Install-Module -Name Az -Force

# Import module
Import-Module Az
```

---

## ٹیسٹنگ
| فریم ورک | شیل | مقصد |
|------------|-------|---------|
| ** چمگادڑ** | باش | باش خودکار ٹیسٹنگ |
| **شونیٹ2** | شیل | xUnit طرز کی جانچ |
| **پیسٹر** | پاور شیل | جانچ اور مذاق |
| **assert.sh** | باش | دعویٰ لائبریری |
```bash
# Bats example
#!/usr/bin/env bats

@test "addition" {
  result=$((2 + 3))
  [ "$result" -eq 5 ]
}

@test "file exists" {
  [ -f "/etc/passwd" ]
}

@test "command succeeds" {
  run echo "hello"
  [ "$status" -eq 0 ]
  [ "$output" = "hello" ]
}
```

```powershell
# Pester example
Describe "UserService" {
    It "finds user by id" {
        $user = Get-User -Id 1
        $user.Name | Should -Be "Alice"
    }
    
    It "throws when user not found" {
        { Get-User -Id 999 } | Should -Throw
    }
}
```

---

## کوڈ کا معیار
| ٹول | شیل | مقصد |
|------|------|---------|
| **شیل چیک** | Bash/Zsh | لنٹنگ اور جامد تجزیہ |
| **shfmt** | Bash/Zsh | کوڈ فارمیٹنگ |
| **PSScriptAnalyzer** | پاور شیل | لنٹنگ |
| **PSScriptSettings** | پاور شیل | فارمیٹنگ |
```bash
# ShellCheck
shellcheck script.sh        # lint
shellcheck -s bash script.sh  # specify shell

# shfmt
shfmt -w script.sh          # format
shfmt -d script.sh          # diff (check only)
```

```powershell
# PSScriptAnalyzer
Invoke-ScriptAnalyzer -Path .\script.ps1
Invoke-ScriptAnalyzer -Path .\script.ps1 -Fix  # auto-fix
```

---

## کلیدی لائبریریاں اور پیٹرن
### باش
| پیٹرن | مقصد |
|---------|---------|
| **سیٹ -euo پائپ فیل** | سخت موڈ |
| **ٹریپ** | سگنل ہینڈلنگ |
| **ذریعہ / .** | فائلیں شامل کریں |
| **getopts** | دلیل کی تجزیہ |
| **ہریڈوک** | ملٹی لائن سٹرنگز |
| **عمل کا متبادل** | `<()`اور`>()`|
| **ارے** | انڈیکسڈ اور ایسوسی ایٹیو |
```bash
#!/usr/bin/env bash
set -euo pipefail

# Functions
log() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"; }

# Argument parsing
while getopts "hn:v" opt; do
  case $opt in
    h) echo "Usage: $0 [-h] [-n name] [-v]"; exit 0 ;;
    n) NAME="$OPTARG" ;;
    v) VERBOSE=true ;;
  esac
done

# Cleanup trap
cleanup() { rm -rf "$TMPDIR"; }
trap cleanup EXIT
```

### پاور شیل
| پیٹرن | مقصد |
|---------|---------|
| **Cmdlet بائنڈنگ** | اعلی درجے کی تقریب |
| **پیرامیٹر** | پیرامیٹر کی خصوصیات |
| **پائپ لائن** | آبجیکٹ پائپ لائن |
| **کوشش/پکڑو** | خرابی سے نمٹنے |
| **کلاسز** | OOP |
```powershell
function Get-User {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [int]$Id,
        
        [ValidateSet("json", "xml")]
        [string]$Format = "json"
    )
    
    try {
        $user = Invoke-RestMethod -Uri "https://api.example.com/users/$Id"
        return $user
    }
    catch {
        Write-Error "Failed to get user: $_"
    }
}
```

---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| ** VS کوڈ** | شیل/پاور شیل سپورٹ |
| **نیوم** | ٹرمینل پر مبنی |
| **ونڈوز ٹرمینل** | جدید ٹرمینل (PowerShell) |
| **iTerm2** | macOS ٹرمینل |
| **وارپ** | اے آئی سے چلنے والا ٹرمینل |
| **الکرٹی** | GPU- ایکسلریٹڈ ٹرمینل |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **کرون** | طے شدہ کام (یونکس) |
| **سسٹم ڈی** | سروس مینجمنٹ (لینکس) |
| **ٹاسک شیڈولر** | ونڈوز کے طے شدہ کام |
| **ڈوکر انٹری پوائنٹ** | کنٹینر اسکرپٹس |
| **CI/CD پائپ لائنز** | GitHub ایکشنز، GitLab CI |
| **جواب ** | کنفیگریشن مینجمنٹ |
| **ٹیرافارم** | بنیادی ڈھانچہ بطور کوڈ |
---

## خلاصہ
شیل اسکرپٹنگ کا ماحولیاتی نظام متنوع ہے: **باش** یونیورسل اسٹینڈرڈ ہے، **Zsh** انٹرایکٹو استعمال کے لیے جدید ڈیفالٹ ہے، اور **PowerShell** ونڈوز ایڈمنسٹریشن پر حاوی ہے۔ معیاری اسٹیک یہ ہے: سکرپٹ کے لیے **Bash/Zsh**، linting کے لیے **ShellCheck**، فارمیٹنگ کے لیے **shfmt**، ٹیسٹنگ کے لیے **Bats**، JSON کے لیے **jq**، تلاش کے لیے **ripgrep**، اور ٹرمینل ملٹی پلیکسنگ کے لیے **tmux**۔ پاور شیل کے لیے: **پیسٹر** ٹیسٹنگ کے لیے، **PSScriptAnalyzer** linting کے لیے، اور **PSReadLine** بہتر ایڈیٹنگ کے لیے۔ شیل اسکرپٹنگ آٹومیشن، CI/CD، سسٹم ایڈمنسٹریشن، اور DevOps ورک فلو کے لیے ضروری ہے۔