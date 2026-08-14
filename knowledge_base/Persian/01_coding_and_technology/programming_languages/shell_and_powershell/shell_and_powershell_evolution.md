<!--
---
# Metadata
title: "Shell & PowerShell — Version History & Evolution"
description: "Comprehensive version history and evolution of Unix Shell and PowerShell from sh to modern shells."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Shell & PowerShell - تاریخچه نسخه و تکامل
## جدول زمانی یونیکس شل
| نسخه | سال | تم کلید |
|---------|------|-----------|
| تامپسون ش | 1971 | اولین پوسته یونیکس (کن تامپسون) |
| بورن ش | 1977 | **`sh`** — برنامه نویسی، متغیرها، جریان کنترل |
| csh | 1978 | نحو شبیه C، کنترل شغل، نام مستعار |
| ksh | 1983 | پوسته کورن — ویژگی های`sh`+`csh`|
| بش | 1989 | **Bourne Again Shell** — جایگزینی GNU`sh`|
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash 3.0 | 2004 | `=~`regex،`|&`|
| bash 4.0 | 2009 | **آرایه های انجمنی**، `mapfile`،`declare -g`|
| bash 4.3 | 2014 | آسیب پذیری Shellshock کشف شد |
| bash 5.0 | 2019 | `declare -n`namerefs،`printf %q`|
| bash 5.1 | 2020 |  بهبودهای `wait -n`،`shopt`|
| bash 5.2 | 2022 | `${var@U}`(بزرگ)،`shopt -s compat`|
| zsh | 1990 | Bash گسترده — تکمیل، مضامین |
| ماهی | 2005 | **کاربر پسند** — پیشنهادات خودکار، برجسته سازی نحو |
| خلاصه | 2019 | داده های ساخت یافته، خطوط لوله جداول |
| روغن / اوش | 2020 | Bash سازگار با معناشناسی بهتر |
## جدول زمانی PowerShell
| نسخه | سال | تم کلید |
|---------|------|-----------|
| 1.0 | 2006 | انتشار اولیه (مایکروسافت، جفری اسنوور) |
| 2.0 | 2009 | ** ماژول ها **، از راه دور، مشاغل پس زمینه، معاملات |
| 3.0 | 2012 | گردش کار، `Invoke-RestMethod`، کارهای برنامه ریزی شده |
| 4.0 | 2013 | **پیکربندی حالت مطلوب (DSC)**، بهبودهای`if`/`switch`|
| 5.0 | 2016 | **کلاس**,`enum`,`using`,`using module`|
| 5.1 | 2017 | آخرین نسخه فقط ویندوز |
| 6.0 | 2018 | **PowerShell Core** — کراس پلتفرم (ویندوز، لینوکس، macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(تجربی) |
| 6.2 | 2019 |  اپراتورهای زنجیره ای خط لوله`&&`/`||`|
| 7.0 | 2020 | **عمده**:`?.`null-conditional،`??`null-Coalescing،`using assembly`|
| 7.1 | 2020 | اپراتور سه تایی `? :`، بهبود`using module`|
| 7.2 | 2021 | **نسخه LTS**، بهبودهای`using namespace`|
| 7.3 | 2022 |  بهبودهای `switch`، گزینه های`ErrorView`|
| 7.4 | 2023 |  بهبودهای `using module`،`Get-Error`|
| 7.5 | 2024 | بهبود عملکرد،`PSResourceGet`|
| 7.6 | 2025 | توسعه در حال انجام |
## نقاط عطف اصلی
### Unix Shell Heritage (1971-1989)
- **1971**: پوسته تامپسون - اولین پوسته یونیکس، اجرای دستور ساده
- **1977**: پوسته بورن (`sh`) - متغیرها، جریان کنترل (`if`، `while`)، اسناد اینجا
- **1978**: پوسته C (`csh`) - نحو شبیه به C، کنترل کار، نام مستعار، تاریخچه
- **1983**: پوسته کورن (`ksh`) - بهترین`sh`+ `csh`
### bash - The Standard (1989–اکنون)
- **1989**: برایان فاکس bash را برای پروژه گنو ایجاد می کند - Bourne Again Shell
- **2.0 (1996)**: تست `[[ ]]`، محاسبات `(( ))`،`+=`
- **4.0 (2009)**: آرایه های انجمنی (`declare -A`)،`mapfile`
- **5.0 (2019)**: Namerefs،`printf %q`
- **5.2 (2022)**: دستکاری مورد رشته
### zsh - پوسته کاربران قدرتمند (1990–اکنون)
- **1990**: پل فالستاد zsh را ایجاد می کند - ویژگی های bash، ksh، tcsh را ترکیب می کند.
- ** دهه 2000 **: چارچوب oh-my-zsh - تم ها، پلاگین ها، تکمیل ها
- **2019**: پوسته پیش فرض macOS (جایگزین bash)
### ماهی - پوسته دوستانه (2005–اکنون)
- **2005**: Axel Liljankrantz ماهی می‌سازد - "در نهایت، یک پوسته تعاملی"
- پیشنهادات خودکار، برجسته سازی نحو، پیکربندی مبتنی بر وب
- سازگار با bash نیست - زبان برنامه نویسی مختلف
### PowerShell - مایکروسافت شل (2006–اکنون)
- **2006**: PowerShell 1.0 - مبتنی بر NET، خط لوله آبجکت، cmdlets
- **2.0 (2009)**: ماژول ها، از راه دور، کارهای پس زمینه
- **5.0 (2016)**: کلاس ها، تعداد
- **6.0 (2018)**: **کراس پلتفرم** — PowerShell Core (ساخته شده بر روی NET Core)
- **7.0 (2020)**:`?.`تهی شرطی،`??`تهی،`?:`سه تایی
## تکامل نحو
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

## اصول کلیدی طراحی
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

## رشد اکوسیستم
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
