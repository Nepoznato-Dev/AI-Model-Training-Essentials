---
# Metadata
title: "Shell & PowerShell — Version History & Evolution"
description: "Comprehensive version history and evolution of Unix Shell and PowerShell from sh to modern shells."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [shell, powershell, bash, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# شیل اور پاور شیل - ورژن کی تاریخ اور ارتقاء
## یونکس شیل ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| تھامسن ش | 1971 | پہلا یونکس شیل (کین تھامسن) |
| بورن ش | 1977 | **`sh`** - سکرپٹ، متغیرات، کنٹرول بہاؤ |
| csh | 1978 | سی کی طرح نحو، جاب کنٹرول، عرفی نام |
| ksh | 1983 | کارن شیل —`sh`+`csh`خصوصیات |
| bash | 1989 | **بورن اگین شیل** — GNU`sh`متبادل |
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash 3.0 | 2004 | `=~`regex,`|&`|
| bash 4.0 | 2009 | **ایسوسی ایٹیو ارے**،`mapfile`,`declare -g`|
| bash 4.3 | 2014 | شیل شاک کا خطرہ دریافت ہوا |
| bash 5.0 | 2019 | `declare -n`namerefs,`printf %q`|
| bash 5.1 | 2020 | `wait -n`,`shopt`بہتری |
| bash 5.2 | 2022 | `${var@U}`(بڑے حروف میں)،`shopt -s compat`|
| zsh | 1990 | توسیعی باش - تکمیلات، تھیمز |
| مچھلی | 2005 | **صارف کے موافق** — خودکار تجاویز، نحو کو نمایاں کرنا |
| nushell | 2019 | سٹرکچرڈ ڈیٹا، ٹیبلز کی پائپ لائنز |
| تیل/اوش | 2020 | بہتر سیمنٹکس کے ساتھ باش ہم آہنگ |
## پاور شیل ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| 1.0 | 2006 | ابتدائی ریلیز (Microsoft, Jeffrey Snover) |
| 2.0 | 2009 | **ماڈیول**، ریموٹنگ، بیک گراؤنڈ جابز، لین دین |
| 3.0 | 2012 | ورک فلوز،`Invoke-RestMethod`, طے شدہ ملازمتیں |
| 4.0 | 2013 | **مطلوبہ اسٹیٹ کنفیگریشن (DSC)**،`if`/`switch`بہتری |
| 5.0 | 2016 | **کلاسز**, `enum`, `using`,`using module`|
| 5.1 | 2017 | آخری ونڈوز صرف ورژن |
| 6.0 | 2018 | **پاور شیل کور** — کراس پلیٹ فارم (ونڈوز، لینکس، میک او ایس) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(تجرباتی) |
| 6.2 | 2019 | `&&`/`||`پائپ لائن چین آپریٹرز |
| 7.0 | 2020 | **میجر**:`?.`null-conditional,`??`null coalescing,`using assembly`|
| 7.1 | 2020 | ٹرنری آپریٹر`? :`,`using module`بہتری |
| 7.2 | 2021 | **LTS ریلیز**،`using namespace`بہتری |
| 7.3 | 2022 | `switch`بہتری،`ErrorView`اختیارات |
| 7.4 | 2023 | `using module`بہتری،`Get-Error`|
| 7.5 | 2024 | کارکردگی میں بہتری،`PSResourceGet`|
| 7.6 | 2025 | جاری ترقی |
## اہم سنگ میل
### یونکس شیل ہیریٹیج (1971–1989)
- **1971**: تھامسن شیل - پہلا یونکس شیل، سادہ کمانڈ پر عمل درآمد
- **1977**: بورن شیل (`sh`) - متغیرات، کنٹرول کا بہاؤ ( `if`،`while`)، یہاں-دستاویزات
- **1978**: C شیل (`csh`) - C جیسا نحو، جاب کنٹرول، عرفی نام، تاریخ
- **1983**: کارن شیل (`ksh`) — بہترین`sh`+ `csh`
### bash — دی اسٹینڈرڈ (1989–موجودہ)
- **1989**: برائن فاکس نے GNU پروجیکٹ کے لیے bash بنایا - Bourne Again Shell
- **2.0 (1996)**:`[[ ]]`ٹیسٹ،`(( ))`ریاضی،`+=`
- **4.0 (2009)**: ایسوسی ایٹیو صفوں (`declare -A`),`mapfile`
- **5.0 (2019)**: Namerefs,`printf %q`
- **5.2 (2022): سٹرنگ کیس میں ہیرا پھیری
### zsh — پاور یوزر شیل (1990–موجودہ)
- **1990**: پال Falstad نے zsh تخلیق کیا - bash، ksh، tcsh خصوصیات کو یکجا کرتا ہے
- **2000s**: oh-my-zsh فریم ورک — تھیمز، پلگ انز، تکمیلات
- **2019**: macOS ڈیفالٹ شیل (bash کی جگہ لے لیتا ہے)
### مچھلی - دوستانہ شیل (2005–موجودہ)
- **2005**: ایکسل لِلجنکرانٹز مچھلی بناتا ہے - "آخر میں، ایک انٹرایکٹو شیل"
- خودکار تجاویز، نحو کو نمایاں کرنا، ویب پر مبنی تشکیل
- bash کے موافق نہیں - مختلف اسکرپٹنگ زبان
### پاور شیل — مائیکروسافٹ کا شیل (2006–موجودہ)
- **2006**: پاور شیل 1.0 — NET پر مبنی، آبجیکٹ پائپ لائن، cmdlets
- **2.0 (2009): ماڈیولز، ریموٹنگ، بیک گراؤنڈ جابز
- **5.0 (2016): کلاسز، شماریات
- **6.0 (2018)**: **کراس پلیٹ فارم** — پاور شیل کور (.NET کور پر بنایا گیا)
- **7.0 (2020)**: غیر مشروط`?.`, null-coalescing`??`, ٹرنری `?:`
## نحوی ارتقاء
```bash
# Bourne shell (1977): Basic scripting
#!/bin/sh
name="World"
echo "Hello, $name"
for file in *.txt; do
  echo "Processing $file"
done

# bash 4.0: Associative arrays
declare -A colors
colors[red]="#FF0000"
colors[green]="#00FF00"
echo "${colors[red]}"

# bash 5.0+: Modern bash
mapfile -t lines < input.txt
for line in "${lines[@]}"; do
  echo "${line^^}"  # uppercase
done

# zsh + oh-my-zsh: Enhanced interactive
# Autosuggestions, syntax highlighting, git aliases

# fish: Modern interactive
# Autosuggestions, web config, not bash-compatible
function greet
    echo "Hello, $argv"
end
```

```powershell
# PowerShell 1.0: Basic cmdlets
Get-Process | Where-Object { $_.CPU -gt 100 }

# PowerShell 5.0: Classes
class Person {
    [string]$Name
    [int]$Age
    Person([string]$n, [int]$a) { $this.Name = $n; $this.Age = $a }
}

# PowerShell 7.0+: Modern syntax
$person = [Person]::new("Alice", 30)
$name = $person?.Name ?? "Unknown"  # null-conditional, null-coalescing
$result = $x -gt 0 ? "positive" : "non-positive"  # ternary

# PowerShell: Object pipeline (unique feature)
Get-ChildItem |
  Where-Object { $_.Extension -eq ".md" } |
  ForEach-Object { $_.FullName }
```

## ڈیزائن کے کلیدی اصول
```
Shell (bash/zsh):
1. "Text is the universal interface" — pipes connect everything
2. "Do one thing well" — small tools, compose via pipes
3. "Everything is a file" — Unix philosophy
4. "Backward compatible" — 40-year-old scripts still work

PowerShell:
1. "Objects, not text" — pipeline passes .NET objects
2. "Consistent" — Verb-Noun naming (Get-Process, Set-Location)
3. "Extensible" — modules, providers, remoting
4. "Cross-platform" — PowerShell 7+ runs everywhere
```

## ماحولیاتی نظام کی نمو
```
1971: Thompson shell — first Unix shell
1977: Bourne shell (sh) — scripting begins
1989: bash — GNU shell, becomes Linux default
1990: zsh — power user shell
2005: fish — user-friendly shell
2006: PowerShell 1.0 — Microsoft's object shell
2010: oh-my-zsh — zsh framework (themes, plugins)
2018: PowerShell 6.0 — cross-platform
2019: nushell — structured data shell
2020: PowerShell 7.0 — modern syntax
2025: bash remains the default on Linux/macOS
       PowerShell dominates Windows administration
       zsh is macOS default; fish gaining popularity
```
