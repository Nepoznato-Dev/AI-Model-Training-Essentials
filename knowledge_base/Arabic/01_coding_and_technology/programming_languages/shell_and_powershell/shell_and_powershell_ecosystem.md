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
# Shell وPowerShell — دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والأطر والبنية الأساسية الأساسية للبرمجة النصية لـ Shell (Bash/Zsh) وPowerShell.
---

## تطبيقات شل
| شل | منصة | ملاحظات |
|-------|----------|-------|
| **باش** | يونيكس/لينكس/ماك | الأكثر استخدامًا |
| **زش** | نظام التشغيل MacOS الافتراضي | تعزيز باش |
| **السمك** | عبر منصة | سهل الاستخدام |
| **شرطة** | ديبيان/أوبونتو | سريع ومتوافق مع POSIX |
| **كش** | يونكس | قشرة الذرة |
| **بوويرشيل** | عبر منصة | كائنية التوجه (pwsh) |
| **نوشيل** | عبر منصة | قذيفة البيانات المنظمة |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## مديرو الحزم (أدوات Shell)
| أداة | الغرض |
|------|---------|
| ** البيرة ** | مدير حزم ماك/لينكس |
| **مناسبة/يم/dnf** | مديرو حزم لينكس |
| **حزمة** | مدير حزمة FreeBSD |
| **مغرفة** | مثبت Windows CLI |
| **الشوكولاته** | مدير حزم ويندوز |
| **وينجيت** | مدير حزم ويندوز |
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

## أدوات CLI الأساسية
| أداة | الغرض |
|------|---------|
| **جق** | معالجة JSON |
| **yq** | معالجة YAML |
| **ريبجرب (رغ)** | grep سريع |
| **فد** | البحث السريع |
| **بات** | القط المحسن |
| **إكسا/إيزا** | تعزيز ليرة سورية |
| **فزف** | مكتشف غامض |
| **هتوب** | عارض العملية |
| ** تموكس ** | معدد الإرسال الطرفي |
| ** الضفيرة / wget ** | طلبات HTTP |
| **السيد / أوك** | معالجة النصوص |
| **xargs** | بناء الأوامر من الإدخال |
| **اصنع** | عداء المهمة |
| **أدخل** | تشغيل الأوامر على تغييرات الملف |
| ** الموازي ** | التنفيذ الموازي |
| **فحص الصدف** | شل النصي linter |
---

## أطر عمل شركة شل وتحسيناتها
| أداة | الغرض |
|------|---------|
| **يا زش** | إطار Zsh (الموضوعات والإضافات) |
| **بريزتو** | إطار عمل Zsh (أسرع) |
| **المركبة الفضائية** | موجه عبر الصدفة |
| **zsh-الاقتراحات التلقائية** | اقتراحات تلقائية |
| **تسليط الضوء على بناء جملة zsh** | تسليط الضوء على بناء الجملة |
| **باش-ات** | إطار باش |
| **اتوين** | تاريخ شل (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## وحدات PowerShell
| الوحدة | الغرض |
|--------|---------|
| **PSReadLine** | تحرير سطر الأوامر المحسن |
| ** بيستر ** | إطار الاختبار |
| **PSScriptAnalyzer** | البطانة |
| ** الفاخرة بوابة ** | تكامل بوابة |
| **أيقونات المحطة** | أيقونات الملفات |
| **PSWindowsUpdate** | تحديثات ويندوز |
| **من الألف إلى الياء** | إدارة أزور |
| **AWSPowerShell** | إدارة AWS |
| ** SQLServer ** | إدارة SQL Server |
| **بود** | إطار الويب |
| **لوحة القيادة العالمية** | لوحات تحكم الويب |
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

## الاختبار
| الإطار | شل | الغرض |
|-----------|-------|---------|
| **الخفافيش** | باش | اختبار باش الآلي |
| **شونيت2** | شل | اختبار نمط xUnit |
| ** بيستر ** | بوويرشيل | اختبار واستهزاء |
| **assert.sh** | باش | مكتبة التوكيد |
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

## جودة الكود
| أداة | شل | الغرض |
|------|-------|---------|
| **فحص الشل** | باش/زش | البطانة والتحليل الساكن |
| **شفمت** | باش/زش | تنسيق الكود |
| **PSScriptAnalyzer** | بوويرشيل | البطانة |
| **إعدادات PSScript** | بوويرشيل | التنسيق |
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

## المكتبات والأنماط الرئيسية
### باش
| نمط | الغرض |
|---------|--------|
| ** مجموعة -euo Pipefail ** | الوضع الصارم |
| **فخ** | التعامل مع الإشارات |
| **المصدر / .** | تضمين الملفات |
| **جيتوبتس** | تحليل الوسيطة |
| **هيريدوك** | سلاسل متعددة الأسطر |
| ** استبدال العملية ** | `<()`و`>()` |
| **المصفوفات** | مفهرسة والترابطي |
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

### باورشيل
| نمط | الغرض |
|---------|--------|
| ** أمر CmdletBinding ** | وظيفة متقدمة |
| **المعلمة** | سمات المعلمة |
| **خط الأنابيب** | خط أنابيب الكائن |
| ** حاول / التقط ** | معالجة الأخطاء |
| **الفصول** | OOP |
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

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **رمز VS** | دعم شل/PowerShell |
| **نيوفيم** | القائم على المحطة الطرفية |
| **محطة ويندوز** | المحطة الحديثة (PowerShell) |
| **iTerm2** | محطة ماك |
| **الاعوجاج** | محطة تعمل بالذكاء الاصطناعي |
| **النشاط** | محطة تسريع GPU |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **كرون** | المهام المجدولة (يونكس) |
| **سيستمد** | إدارة الخدمات (لينكس) |
| ** جدولة المهام ** | المهام المجدولة في Windows |
| **نقطة دخول عامل الميناء** | مخطوطات الحاوية |
| ** خطوط أنابيب CI/CD ** | إجراءات جيثب، GitLab CI |
| ** غير مقبول ** | إدارة التكوين |
| **تيرافورم** | البنية التحتية كرمز |
---

## ملخص
يتنوع النظام البيئي لبرمجة Shell النصية: يظل **Bash** هو المعيار العالمي، و**Zsh** هو الإعداد الافتراضي الحديث للاستخدام التفاعلي، و**PowerShell** الذي يهيمن على إدارة Windows. المكدس القياسي هو: **Bash/Zsh** للبرمجة النصية، **ShellCheck** للفحص، **shfmt** للتنسيق، **Bats** للاختبار، **jq** لـ JSON، **ripgrep** للبحث، و **tmux** لتعدد الإرسال الطرفي. بالنسبة إلى PowerShell: **Pester** للاختبار، و**PSScriptAnalyzer** للفحص، و**PSReadLine** للتحرير المحسّن. تعد البرمجة النصية لـ Shell ضرورية للأتمتة وCI/CD وإدارة النظام وسير عمل DevOps.