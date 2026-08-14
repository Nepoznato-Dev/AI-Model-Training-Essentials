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
# Shell وPowerShell — تاريخ الإصدار وتطوره
## الجدول الزمني ليونكس شل
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| طومسون ش | 1971 | أول قذيفة يونكس (كين طومسون) |
| بورن ش | 1977 | **`sh`** — البرمجة النصية والمتغيرات وتدفق التحكم |
| كش | 1978 | بناء جملة يشبه لغة C، والتحكم في الوظيفة، والأسماء المستعارة |
| شلن كيني | 1983 | قذيفة كورن - ميزات`sh`+`csh`|
| باش | 1989 | **Bourne Again Shell** — استبدال GNU`sh`|
| باش 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| باش 3.0 | 2004 |  التعبير العادي `=~`،`|&`|
| باش 4.0 | 2009 | ** المصفوفات الترابطية **,`mapfile`,`declare -g`|
| باش 4.3 | 2014 | اكتشاف ثغرة أمنية في Shellshock |
| باش 5.0 | 2019 | `declare -n`namerefs،`printf %q`|
| باش 5.1 | 2020 |  تحسينات`wait -n`,`shopt`|
| باش 5.2 | 2022 | `${var@U}`(أحرف كبيرة)،`shopt -s compat`|
| زش | 1990 | باش ممتد - الإكمالات والموضوعات |
| سمك | 2005 | **سهل الاستخدام** — اقتراحات تلقائية، وتسليط الضوء على بناء الجملة |
| نشل | 2019 | البيانات المنظمة، خطوط أنابيب الجداول |
| زيت/أوش | 2020 | باش متوافق مع دلالات أفضل |
## الجدول الزمني باورشيل
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| 1.0 | 2006 | الإصدار الأولي (مايكروسوفت، جيفري سنوفر) |
| 2.0 | 2009 | **الوحدات**، العمل عن بعد، وظائف الخلفية، المعاملات |
| 3.0 | 2012 | سير العمل، `Invoke-RestMethod`، الوظائف المجدولة |
| 4.0 | 2013 | **تكوين الحالة المرغوبة (DSC)**، تحسينات`if`/`switch`|
| 5.0 | 2016 | **الفصول**,`enum`,`using`,`using module`|
| 5.1 | 2017 | الإصدار الأخير لنظام التشغيل Windows فقط |
| 6.0 | 2018 | **PowerShell Core** — متعدد الأنظمة الأساسية (Windows وLinux وmacOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(تجريبي) |
| 6.2 | 2019 | `&&`/`||`مشغلي سلسلة خطوط الأنابيب |
| 7.0 | 2020 | **التخصص**:`?.`خالي مشروط،`??`اندماج فارغ،`using assembly`|
| 7.1 | 2020 | تحسينات المشغل الثلاثي`? :`,`using module`|
| 7.2 | 2021 | **إصدار LTS**، تحسينات`using namespace`|
| 7.3 | 2022 |  تحسينات `switch`، خيارات`ErrorView`|
| 7.4 | 2023 |  تحسينات `using module`،`Get-Error`|
| 7.5 | 2024 | تحسينات الأداء،`PSResourceGet`|
| 7.6 | 2025 | التطوير المستمر |
## المعالم الرئيسية
### تراث يونكس شل (1971-1989)
- **1971**: Thompson Shell — أول قذيفة Unix، تنفيذ بسيط للأوامر
- **1977**: Bourne Shell (`sh`) — متغيرات، تدفق التحكم (`if`,`while`) ، هنا المستندات
- **1978**: C shell (`csh`) — بناء جملة يشبه لغة C، والتحكم في الوظائف، والأسماء المستعارة، والتاريخ
- **1983**: Korn Shell (`ksh`) — الأفضل في`sh`+ `csh`
### باش — المعيار (1989 إلى الوقت الحاضر)
- **1989**: قام بريان فوكس بإنشاء باش لمشروع GNU — Bourne Again Shell
- **2.0 (1996)**: اختبار `[[ ]]`، الحساب `(( ))`،`+=`
- **4.0 (2009)**: المصفوفات الترابطية (`declare -A`)،`mapfile`
- **5.0 (2019)**: Namerefs,`printf %q`
- **5.2 (2022)**: معالجة حالة السلسلة
### zsh — غلاف المستخدم القوي (1990 إلى الوقت الحاضر)
- **1990**: قام بول فالستاد بإنشاء zsh — يجمع بين ميزات bash وksh وtcsh
- **العقد الأول من القرن الحادي والعشرين**: إطار عمل oh-my-zsh — السمات، والمكونات الإضافية، والإكمالات
- **2019**: غلاف macOS الافتراضي (يستبدل bash)
### الأسماك — الصدفة الصديقة (2005 إلى الوقت الحاضر)
- **2005**: أكسل ليلجانكرانتز يصنع سمكة - "أخيرًا، صدفة تفاعلية"
- الاقتراحات التلقائية، وتسليط الضوء على بناء الجملة، والتكوين على شبكة الإنترنت
- غير متوافق مع bash — لغة برمجة نصية مختلفة
### PowerShell — شركة Microsoft Shell (2006 إلى الوقت الحاضر)
- **2006**: PowerShell 1.0 — مستند إلى .NET، مسار الكائنات، أوامر cmdlets
- **2.0 (2009)**: الوحدات، والعمل عن بعد، والمهام الخلفية
- **5.0 (2016)**: الفئات، التعدادات
- **6.0 (2018)**: **عبر الأنظمة الأساسية** — PowerShell Core (مبني على .NET Core)
- **7.0 (2020)**:`?.`شرطي فارغ، اندماج فارغ `??`، ثلاثي `?:`
## تطور بناء الجملة
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

## مبادئ التصميم الرئيسية
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

## نمو النظام البيئي
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
