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
# শেল এবং পাওয়ারশেল — সংস্করণ ইতিহাস এবং বিবর্তন
## ইউনিক্স শেল টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| থম্পসন শ | 1971 | প্রথম ইউনিক্স শেল (কেন থম্পসন) |
| বোর্ন শ | 1977 | **`sh`** — স্ক্রিপ্টিং, ভেরিয়েবল, নিয়ন্ত্রণ প্রবাহ |
| csh | 1978 | সি-এর মতো সিনট্যাক্স, কাজ নিয়ন্ত্রণ, উপনাম |
| ksh | 1983 | কর্ন শেল —`sh`+`csh`বৈশিষ্ট্য |
| বাশ | 1989 | **বোর্ন এগেইন শেল** — GNU`sh`প্রতিস্থাপন |
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash 3.0 | 2004 | `=~`regex,`|&`|
| bash 4.0 | 2009 | **অ্যাসোসিয়েটিভ অ্যারে**,`mapfile`,`declare -g`|
| bash 4.3 | 2014 | শেলশক দুর্বলতা আবিষ্কৃত |
| bash 5.0 | 2019 | `declare -n`namerefs,`printf %q`|
| bash 5.1 | 2020 | `wait -n`,`shopt`উন্নতি |
| bash 5.2 | 2022 | `${var@U}`(বড় হাতের অক্ষর),`shopt -s compat`|
| zsh | 1990 | বর্ধিত ব্যাশ — সমাপ্তি, থিম |
| মাছ | 2005 | **ব্যবহারকারী-বান্ধব** — অটো সাজেশন, সিনট্যাক্স হাইলাইটিং |
| nushell | 2019 | স্ট্রাকচার্ড ডেটা, টেবিলের পাইপলাইন |
| তেল/ওশ | 2020 | বাশ-সামঞ্জস্যপূর্ণ শব্দার্থবিদ্যার সাথে |
## পাওয়ারশেল টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| 1.0 | 2006 | প্রাথমিক প্রকাশ (Microsoft, Jeffrey Snover) |
| 2.0 | 2009 | **মডিউল**, রিমোটিং, ব্যাকগ্রাউন্ড জব, লেনদেন |
| 3.0 | 2012 | কর্মপ্রবাহ,`Invoke-RestMethod`, নির্ধারিত কাজ |
| 4.0 | 2013 | **কাঙ্ক্ষিত স্টেট কনফিগারেশন (DSC)**,`if`/`switch`উন্নতি |
| 5.0 | 2016 | **ক্লাস**,`enum`,`using`,`using module`|
| 5.1 | 2017 | শুধুমাত্র উইন্ডোজের শেষ সংস্করণ |
| 6.0 | 2018 | **পাওয়ারশেল কোর** — ক্রস-প্ল্যাটফর্ম (উইন্ডোজ, লিনাক্স, ম্যাকোস) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(পরীক্ষামূলক) |
| 6.2 | 2019 | `&&`/`||`পাইপলাইন চেইন অপারেটর |
| 7.0 | 2020 | **মেজর**:`?.`নাল-কন্ডিশনাল,`??`নাল-কোলেসিং,`using assembly`|
| 7.1 | 2020 | টারনারি অপারেটর`? :`,`using module`উন্নতি |
| 7.2 | 2021 | **LTS রিলিজ**,`using namespace`উন্নতি |
| 7.3 | 2022 | `switch`উন্নতি,`ErrorView`বিকল্পগুলি |
| 7.4 | 2023 | `using module`উন্নতি,`Get-Error`|
| 7.5 | 2024 | কর্মক্ষমতা উন্নতি,`PSResourceGet`|
| 7.6 | 2025 | চলমান উন্নয়ন |
## প্রধান মাইলফলক
### ইউনিক্স শেল হেরিটেজ (1971-1989)
- **1971**: থম্পসন শেল — প্রথম ইউনিক্স শেল, সাধারণ কমান্ড এক্সিকিউশন
- **1977**: বোর্ন শেল (`sh`) — ভেরিয়েবল, নিয়ন্ত্রণ প্রবাহ (`if`,`while`), এখানে-নথিপত্র
- **1978**: সি শেল (`csh`) — সি-এর মতো সিনট্যাক্স, কাজের নিয়ন্ত্রণ, উপনাম, ইতিহাস
- **1983**: কর্ন শেল (`ksh`) —`sh`+`csh`এর সেরা
### ব্যাশ — দ্য স্ট্যান্ডার্ড (1989-বর্তমান)
- **1989**: ব্রায়ান ফক্স GNU প্রজেক্টের জন্য ব্যাশ তৈরি করেছে — বোর্ন এগেইন শেল
- **2.0 (1996):`[[ ]]`পরীক্ষা,`(( ))`পাটিগণিত,`+=`
- **4.0 (2009): অ্যাসোসিয়েটিভ অ্যারে (`declare -A`),`mapfile`
- **5.0 (2019): Namerefs,`printf %q`
- **5.2 (2022): স্ট্রিং কেস ম্যানিপুলেশন
### zsh — পাওয়ার ইউজারের শেল (1990-বর্তমান)
- **1990**: পল ফালস্ট্যাড zsh তৈরি করেছেন — bash, ksh, tcsh বৈশিষ্ট্যগুলিকে একত্রিত করে
- **2000s**: oh-my-zsh ফ্রেমওয়ার্ক — থিম, প্লাগইন, সমাপ্তি
- **2019**: macOS ডিফল্ট শেল (ব্যাশ প্রতিস্থাপন করে)
### মাছ — দ্য ফ্রেন্ডলি শেল (2005-বর্তমান)
- **2005**: অ্যাক্সেল লিলজানক্রান্টজ মাছ তৈরি করেন - "অবশেষে, একটি ইন্টারেক্টিভ শেল"
- অটোসাজেশন, সিনট্যাক্স হাইলাইটিং, ওয়েব-ভিত্তিক কনফিগারেশন
- ব্যাশ-সামঞ্জস্যপূর্ণ নয় — ভিন্ন স্ক্রিপ্টিং ভাষা
### পাওয়ারশেল — মাইক্রোসফটের শেল (2006-বর্তমান)
- **2006**: PowerShell 1.0 — .NET-ভিত্তিক, অবজেক্ট পাইপলাইন, cmdlets
- **2.0 (2009): মডিউল, রিমোটিং, ব্যাকগ্রাউন্ড জব
- **5.0 (2016): ক্লাস, গণনা
- **6.0 (2018): **ক্রস-প্ল্যাটফর্ম** — পাওয়ারশেল কোর (.NET কোরে নির্মিত)
- **7.0 (2020): শূন্য-শর্তযুক্ত`?.`, নাল-কোলেসিং`??`, তৃতীয় `?:`
## সিনট্যাক্স বিবর্তন
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

## মূল ডিজাইনের নীতি
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

## ইকোসিস্টেম বৃদ্ধি
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
