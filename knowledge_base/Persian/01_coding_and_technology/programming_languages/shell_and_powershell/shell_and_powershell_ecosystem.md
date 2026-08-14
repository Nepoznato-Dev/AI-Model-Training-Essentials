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
# Shell & PowerShell - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری برای برنامه‌نویسی پوسته (Bash/Zsh) و PowerShell را پوشش می‌دهد.
---

## پیاده سازی شل
| پوسته | پلت فرم | یادداشت ها |
|-------|----------|-------|
| **باش** | یونیکس / لینوکس / macOS | پرکاربردترین |
| **زش** | macOS پیش فرض | Bash پیشرفته |
| **ماهی** | کراس پلتفرم | کاربر پسند |
| **داش** | دبیان/اوبونتو | سریع، سازگار با POSIX |
| **ksh** | یونیکس | پوسته کورن |
| **PowerShell** | کراس پلتفرم | شی گرا (pwsh) |
| **نوشل** | کراس پلتفرم | پوسته داده های ساخت یافته |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## مدیران بسته (ابزار شل)
| ابزار | هدف |
|------|---------|
| **هومبرو** | مدیر بسته macOS/Linux |
| **apt / yum / dnf ** | مدیران بسته لینوکس |
| **pkg** | مدیریت بسته های FreeBSD |
| **اسکوپ** | نصب کننده ویندوز CLI |
| **شکلاتی** | مدیر بسته ویندوز |
| **winget** | مدیر بسته ویندوز |
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

## ابزارهای ضروری CLI
| ابزار | هدف |
|------|---------|
| **jq** | پردازش JSON |
| **yq** | پردازش YAML |
| **ripgrep (rg)** | grep سریع |
| **fd** | یافتن سریع |
| **خفاش** | گربه تقویت شده |
| **exa / eza** | ls پیشرفته |
| **fzf** | فازی یاب |
| **htop** | نمایشگر فرآیند |
| **tmux** | مالتی پلکسر ترمینال |
| **curl / wget** | درخواست های HTTP |
| **sed / awk** | پردازش متن |
| **xargs** | ساخت دستورات از ورودی |
| **ساخت** | Task runner |
| **ورود** | اجرای دستورات روی تغییرات فایل |
| **موازی** | اجرای موازی |
| **shellcheck** | لیتر اسکریپت پوسته |
---

## چارچوب‌ها و پیشرفت‌های پوسته
| ابزار | هدف |
|------|---------|
| **اوه من زش** | فریمورک Zsh (تم ها، پلاگین ها) |
| **پرزتو** | فریمورک Zsh (سریعتر) |
| **سفینه فضایی** | درخواست متقاطع پوسته |
| **zsh-autosuggestions** | پیشنهادات خودکار |
| **zsh-syntax-highlighting** | برجسته سازی نحو |
| **باش آن** | چارچوب Bash |
| **آتوین** | تاریخچه پوسته (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## ماژول های PowerShell
| ماژول | هدف |
|--------|---------|
| **PSReadLine** | ویرایش خط فرمان پیشرفته |
| **پستر** | چارچوب تست |
| **PSScriptAnalyzer** | پرز زدن |
| **posh-git** | یکپارچه سازی Git |
| **آیکون های ترمینال** | نمادهای فایل |
| **PSWindowsUpdate** | به روز رسانی ویندوز |
| **از** | مدیریت لاجوردی |
| **AWSPowerShell** | مدیریت AWS |
| **SqlServer** | مدیریت SQL Server |
| **پود** | چارچوب وب |
| **داشبورد جهانی** | داشبوردهای وب |
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

## تست
| چارچوب | پوسته | هدف |
|-----------|-------|---------|
| **خفاش** | باش | تست خودکار Bash |
| **شونیت2** | پوسته | تست xUnit-style |
| **پستر** | پاورشل | تست و تمسخر |
| **اظهار.ش** | باش | کتابخانه ادعا |
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

## کیفیت کد
| ابزار | پوسته | هدف |
|------|-------|---------|
| **ShellCheck** | Bash/Zsh | لینتینگ و آنالیز استاتیک |
| **shfmt** | Bash/Zsh | قالب بندی کد |
| **PSScriptAnalyzer** | پاورشل | پرز زدن |
| **تنظیمات PScript** | پاورشل | قالب بندی |
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

## کتابخانه ها و الگوهای کلیدی
### ضربه شدید
| الگو | هدف |
|---------|---------|
| **set -euo pipefail** | حالت سختگیرانه |
| **تله** | کنترل سیگنال |
| **منبع / .** | شامل فایل ها |
| **getopts** | تجزیه آرگومان |
| **heredoc** | رشته های چند خطی |
| **جایگزینی فرآیند** | `<()`و`>()`|
| **آرایه** | نمایه شده و انجمنی |
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

### PowerShell
| الگو | هدف |
|---------|---------|
| **CmdletBinding** | عملکرد پیشرفته |
| **پارامتر** | ویژگی های پارامتر |
| **خط لوله** | خط لوله آبجکت |
| **امتحان/گرفتن** | رسیدگی به خطا |
| **کلاس** | OOP |
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

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| ** کد VS ** | پشتیبانی از Shell/PowerShell |
| **Neovim** | مبتنی بر ترمینال |
| **ترمینال ویندوز** | ترمینال مدرن (PowerShell) |
| **iTerm2** | ترمینال macOS |
| **Warp** | ترمینال مجهز به هوش مصنوعی |
| **Alacritty** | ترمینال با شتاب GPU |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **کرون** | وظایف برنامه ریزی شده (یونیکس) |
| **سیستم** | مدیریت خدمات (لینوکس) |
| **زمانبندی وظایف** | وظایف برنامه ریزی شده ویندوز |
| **داکر ENTRYPOINT** | اسکریپت کانتینر |
| **خطوط لوله CI/CD** | GitHub Actions، GitLab CI |
| **آنسیبل** | مدیریت پیکربندی |
| **Terraform** | زیرساخت به عنوان کد |
---

## خلاصه
اکوسیستم اسکریپت نویسی شل متنوع است: **Bash** استاندارد جهانی باقی می ماند، **Zsh** پیش فرض مدرن برای استفاده تعاملی است و **PowerShell** بر مدیریت ویندوز تسلط دارد. پشته استاندارد عبارتند از: **Bash/Zsh** برای اسکریپت، **ShellCheck** برای linting، **shfmt** برای قالب بندی، **Bats** برای تست، **jq** برای JSON، **ripgrep** برای جستجو، و **tmux** برای مالتی پلکس شدن ترمینال. برای PowerShell: **Pester** برای آزمایش، **PSScriptAnalyzer** برای linting و **PSReadLine** برای ویرایش پیشرفته. برنامه نویسی پوسته برای اتوماسیون، CI/CD، مدیریت سیستم و گردش کار DevOps ضروری است.