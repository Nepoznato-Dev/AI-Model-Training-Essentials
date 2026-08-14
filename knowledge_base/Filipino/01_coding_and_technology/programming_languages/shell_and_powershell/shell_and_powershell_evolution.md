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
# Shell at PowerShell — Kasaysayan ng Bersyon at Ebolusyon
## Unix Shell Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| Thompson sh | 1971 | Unang Unix shell (Ken Thompson) |
| Bourne sh | 1977 | **`sh`** — scripting, variable, control flow |
| csh | 1978 | C-like syntax, kontrol sa trabaho, mga alias |
| ksh | 1983 | Korn shell —`sh`+`csh`feature |
| bash | 1989 | **Bourne Again Shell** — GNU`sh`kapalit |
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash 3.0 | 2004 | `=~`regex,`|&`|
| bash 4.0 | 2009 | **Associative arrays**,`mapfile`,`declare -g`|
| bash 4.3 | 2014 | Natuklasan ang kahinaan ng Shellshock |
| bash 5.0 | 2019 | `declare -n`namerefs,`printf %q`|
| bash 5.1 | 2020 | `wait -n`,`shopt`mga pagpapabuti |
| bash 5.2 | 2022 | `${var@U}`(uppercase),`shopt -s compat`|
| zsh | 1990 | Extended bash — mga pagkumpleto, mga tema |
| isda | 2005 | **User-friendly** — mga autosuggestion, syntax highlighting |
| kaunti | 2019 | Structured data, pipelines ng mga talahanayan |
| langis/osh | 2020 | Bash-compatible sa mas magandang semantics |
## Timeline ng PowerShell
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| 1.0 | 2006 | Paunang release (Microsoft, Jeffrey Snover) |
| 2.0 | 2009 | **Mga Module**, pag-remote, mga trabaho sa background, mga transaksyon |
| 3.0 | 2012 | Mga Daloy ng Trabaho,`Invoke-RestMethod`, mga nakaiskedyul na trabaho |
| 4.0 | 2013 | **Desired State Configuration (DSC)**,`if`/`switch`mga pagpapabuti |
| 5.0 | 2016 | **Mga Klase**,`enum`,`using`,`using module`|
| 5.1 | 2017 | Huling bersyon na Windows-only |
| 6.0 | 2018 | **PowerShell Core** — cross-platform (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(pang-eksperimento) |
| 6.2 | 2019 | `&&`/`||`pipeline chain operator |
| 7.0 | 2020 | **Major**:`?.`null-conditional,`??`null-coalescing,`using assembly`|
| 7.1 | 2020 | Ternary operator`? :`,`using module`mga pagpapabuti |
| 7.2 | 2021 | **LTS release**,`using namespace`improvements |
| 7.3 | 2022 | `switch`mga pagpapabuti,`ErrorView`opsyon |
| 7.4 | 2023 | `using module`mga pagpapabuti,`Get-Error`|
| 7.5 | 2024 | Mga pagpapahusay sa pagganap,`PSResourceGet`|
| 7.6 | 2025 | Patuloy na pag-unlad |
## Mga Pangunahing Milestone
### Unix Shell Heritage (1971–1989)
- **1971**: Thompson shell — unang Unix shell, simpleng command execution
- **1977**: Bourne shell (`sh`) — mga variable, control flow (`if`,`while`), dito-mga dokumento
- **1978**: C shell (`csh`) — C-like syntax, kontrol sa trabaho, mga alias, kasaysayan
- **1983**: Korn shell (`ksh`) — pinakamahusay sa`sh`+ `csh`
### bash — The Standard (1989–kasalukuyan)
- **1989**: Lumilikha si Brian Fox ng bash para sa proyekto ng GNU — Bourne Again Shell
- **2.0 (1996)**:`[[ ]]`test,`(( ))`arithmetic,`+=`
- **4.0 (2009)**: Mga magkakaugnay na array (`declare -A`),`mapfile`
- **5.0 (2019)**: Namerefs,`printf %q`
- **5.2 (2022)**: Pagmamanipula ng string case
### zsh — The Power User's Shell (1990–kasalukuyan)
- **1990**: Lumilikha si Paul Falstad ng zsh — pinagsasama ang bash, ksh, tcsh na mga feature
- **2000s**: oh-my-zsh framework — mga tema, plugin, pagkumpleto
- **2019**: macOS default na shell (pinapalitan ang bash)
### isda — The Friendly Shell (2005–kasalukuyan)
- **2005**: Lumilikha si Axel Liljankrantz ng isda — "Sa wakas, isang interactive na shell"
- Autosuggestions, syntax highlighting, web-based na config
- Hindi bash-compatible — ibang scripting language
### PowerShell — Microsoft's Shell (2006–kasalukuyan)
- **2006**: PowerShell 1.0 — .NET-based, object pipeline, cmdlet
- **2.0 (2009)**: Mga module, pag-remote, mga trabaho sa background
- **5.0 (2016)**: Mga klase, enum
- **6.0 (2018)**: **Cross-platform** — PowerShell Core (built on .NET Core)
- **7.0 (2020)**: Null-conditional`?.`, null-coalescing`??`, ternary `?:`
## Syntax Evolution
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

## Pangunahing Prinsipyo ng Disenyo
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

## Paglago ng Ecosystem
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
