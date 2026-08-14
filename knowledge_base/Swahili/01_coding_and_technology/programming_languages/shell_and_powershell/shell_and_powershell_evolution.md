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
# Shell & PowerShell - Historia ya Toleo & Mageuzi
## Rekodi ya Unix Shell
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| Thompson sh | 1971 | Kwanza Unix shell (Ken Thompson) |
| Bourne sh | 1977 | **`sh`** — uandishi, vigezo, mtiririko wa udhibiti |
| csh | 1978 | Sintaksia-kama C, udhibiti wa kazi, lakabu |
| ksh | 1983 | Kon shell —`sh`+`csh`vipengele |
| bash | 1989 | **Bourne Again Shell** — GNU`sh`badala |
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash 3.0 | 2004 | `=~`regex,`|&`|
| bash 4.0 | 2009 | **Safu shirikishi**,`mapfile`,`declare -g`|
| bash 4.3 | 2014 | Athari ya Shellshock imegunduliwa |
| bash 5.0 | 2019 | `declare -n`namerefs,`printf %q`|
| bash 5.1 | 2020 | `wait -n`,`shopt`maboresho |
| bash 5.2 | 2022 | `${var@U}`(herufi kubwa),`shopt -s compat`|
| zsh | 1990 | Bash iliyopanuliwa - ukamilishaji, mada |
| samaki | 2005 | **Inafaa kwa mtumiaji** — mapendekezo otomatiki, uangaziaji wa sintaksia |
| nuksi | 2019 | Data iliyopangwa, mabomba ya meza |
| mafuta/osh | 2020 | Bash-inayoendana na semantiki bora |
## Rekodi ya Muda ya PowerShell
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| 1.0 | 2006 | Toleo la awali (Microsoft, Jeffrey Snover) |
| 2.0 | 2009 | **Moduli**, uondoaji, kazi za usuli, miamala |
| 3.0 | 2012 | Mtiririko wa kazi,`Invoke-RestMethod`, kazi zilizopangwa |
| 4.0 | 2013 | **Usanidi Unaohitajika wa Jimbo (DSC)**,`if`/`switch`maboresho |
| 5.0 | 2016 | **Madarasa**,`enum`,`using`,`using module`|
| 5.1 | 2017 | Toleo la mwisho la Windows pekee |
| 6.0 | 2018 | **PowerShell Core** — jukwaa-msingi (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(majaribio) |
| 6.2 | 2019 |  waendeshaji mnyororo wa bomba`&&`/`||`|
| 7.0 | 2020 | **Kubwa**:`?.`null-conditional,`??`null-coalescing,`using assembly`|
| 7.1 | 2020 | Opereta wa Ternary`? :`,`using module`maboresho |
| 7.2 | 2021 | **Toleo la LTS**, maboresho ya`using namespace`|
| 7.3 | 2022 |  Maboresho ya `switch`, chaguzi za`ErrorView`|
| 7.4 | 2023 |  Maboresho ya `using module`,`Get-Error`|
| 7.5 | 2024 | Maboresho ya utendaji,`PSResourceGet`|
| 7.6 | 2025 | Maendeleo yanayoendelea |
## Mafanikio Makuu
### Unix Shell Heritage (1971–1989)
- **1971**: ganda la Thompson - ganda la kwanza la Unix, utekelezaji rahisi wa amri
- **1977**: Gamba la Bourne (`sh`) - vigezo, mtiririko wa udhibiti (`if`,`while`), hati-hapa
- **1978**: C shell (`csh`) - Sintaksia inayofanana na C, udhibiti wa kazi, lakabu, historia
- **1983**: ganda la Korn (`ksh`) - bora zaidi ya`sh`+ `csh`
### bash — The Standard (1989–sasa)
- **1989**: Brian Fox anaunda bash kwa mradi wa GNU - Bourne Again Shell
- **2.0 (1996)**: mtihani wa `[[ ]]`, hesabu ya `(( ))`,`+=`
- **4.0 (2009)**: Safu shirikishi (`declare -A`),`mapfile`
- **5.0 (2019)**: Namerefs,`printf %q`
- **5.2 (2022)**: Udanganyifu wa kesi ya kamba
### zsh — Shell ya Mtumiaji Nguvu (1990–sasa)
- **1990**: Paul Falstad huunda zsh - unachanganya vipengele vya bash, ksh, tcsh
- **2000**: mfumo wa oh-my-zsh - mandhari, programu-jalizi, ukamilishaji
- **2019**: ganda chaguo-msingi la macOS (inachukua nafasi ya bash)
### samaki — The Friendly Shell (2005–sasa)
- **2005**: Axel Liljankrantz huunda samaki — "Mwishowe, ganda linaloingiliana"
- Mapendekezo ya kiotomatiki, mwangaza wa syntax, usanidi wa msingi wa wavuti
- Haiendani na bash - lugha tofauti ya uandishi
### PowerShell — Shell ya Microsoft (2006–sasa)
- **2006**: PowerShell 1.0 — .Inayotokana na NET, bomba la kifaa, cmdlets
- **2.0 (2009)**: Moduli, uondoaji, kazi za nyuma
- **5.0 (2016)**: Madarasa, enum
- **6.0 (2018)**: **Mtandao-jukwaa** — PowerShell Core (imejengwa kwa .NET Core)
- **7.0 (2020)**: Null-conditional`?.`, null-coalescing`??`, ternary `?:`
## Mageuzi ya Sintaksia
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

## Kanuni Muhimu za Usanifu
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

## Ukuaji wa Mfumo ikolojia
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
