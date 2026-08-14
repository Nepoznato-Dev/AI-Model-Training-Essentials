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

# Shell & PowerShell — Version History & Evolution

## Unix Shell Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| Thompson sh | 1971 | First Unix shell (Ken Thompson) |
| Bourne sh   | 1977 | **`sh`** — scripting, variables, control flow |
| csh         | 1978 | C-like syntax, job control, aliases |
| ksh         | 1983 | Korn shell — `sh` + `csh` features |
| bash        | 1989 | **Bourne Again Shell** — GNU `sh` replacement |
| bash 2.0    | 1996 | `[[ ]]`, `(( ))`, `+=` |
| bash 3.0    | 2004 | `=~` regex, `|&` |
| bash 4.0    | 2009 | **Associative arrays**, `mapfile`, `declare -g` |
| bash 4.3    | 2014 | Shellshock vulnerability discovered |
| bash 5.0    | 2019 | `declare -n` namerefs, `printf %q` |
| bash 5.1    | 2020 | `wait -n`, `shopt` improvements |
| bash 5.2    | 2022 | `${var@U}` (uppercase), `shopt -s compat` |
| zsh         | 1990 | Extended bash — completions, themes |
| fish        | 2005 | **User-friendly** — autosuggestions, syntax highlighting |
| nushell     | 2019 | Structured data, pipelines of tables |
| oil/osh     | 2020 | Bash-compatible with better semantics |

## PowerShell Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| 1.0     | 2006 | Initial release (Microsoft, Jeffrey Snover) |
| 2.0     | 2009 | **Modules**, remoting, background jobs, transactions |
| 3.0     | 2012 | Workflows, `Invoke-RestMethod`, scheduled jobs |
| 4.0     | 2013 | **Desired State Configuration (DSC)**, `if`/`switch` improvements |
| 5.0     | 2016 | **Classes**, `enum`, `using`, `using module` |
| 5.1     | 2017 | Last Windows-only version |
| 6.0     | 2018 | **PowerShell Core** — cross-platform (Windows, Linux, macOS) |
| 6.1     | 2018 | `ForEach-Object -Parallel` (experimental) |
| 6.2     | 2019 | `&&`/`||` pipeline chain operators |
| 7.0     | 2020 | **Major**: `?.` null-conditional, `??` null-coalescing, `using assembly` |
| 7.1     | 2020 | Ternary operator `? :`, `using module` improvements |
| 7.2     | 2021 | **LTS release**, `using namespace` improvements |
| 7.3     | 2022 | `switch` improvements, `ErrorView` options |
| 7.4     | 2023 | `using module` improvements, `Get-Error` |
| 7.5     | 2024 | Performance improvements, `PSResourceGet` |
| 7.6     | 2025 | Ongoing development |

## Major Milestones

### Unix Shell Heritage (1971–1989)
- **1971**: Thompson shell — first Unix shell, simple command execution
- **1977**: Bourne shell (`sh`) — variables, control flow (`if`, `while`), here-documents
- **1978**: C shell (`csh`) — C-like syntax, job control, aliases, history
- **1983**: Korn shell (`ksh`) — best of `sh` + `csh`

### bash — The Standard (1989–present)
- **1989**: Brian Fox creates bash for GNU project — Bourne Again Shell
- **2.0 (1996)**: `[[ ]]` test, `(( ))` arithmetic, `+=`
- **4.0 (2009)**: Associative arrays (`declare -A`), `mapfile`
- **5.0 (2019)**: Namerefs, `printf %q`
- **5.2 (2022)**: String case manipulation

### zsh — The Power User's Shell (1990–present)
- **1990**: Paul Falstad creates zsh — combines bash, ksh, tcsh features
- **2000s**: oh-my-zsh framework — themes, plugins, completions
- **2019**: macOS default shell (replaces bash)

### fish — The Friendly Shell (2005–present)
- **2005**: Axel Liljankrantz creates fish — "Finally, an interactive shell"
- Autosuggestions, syntax highlighting, web-based config
- Not bash-compatible — different scripting language

### PowerShell — Microsoft's Shell (2006–present)
- **2006**: PowerShell 1.0 — .NET-based, object pipeline, cmdlets
- **2.0 (2009)**: Modules, remoting, background jobs
- **5.0 (2016)**: Classes, enums
- **6.0 (2018)**: **Cross-platform** — PowerShell Core (built on .NET Core)
- **7.0 (2020)**: Null-conditional `?.`, null-coalescing `??`, ternary `?:`

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

## Key Design Principles

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

## Ecosystem Growth

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
