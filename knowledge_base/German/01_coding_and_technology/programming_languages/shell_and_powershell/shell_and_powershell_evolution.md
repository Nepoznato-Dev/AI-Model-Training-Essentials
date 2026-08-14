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
# Shell & PowerShell – Versionsverlauf und Entwicklung
## Unix-Shell-Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| Thompson sh | 1971 | Erste Unix-Shell (Ken Thompson) |
| Bourne sh | 1977 | **`sh`** – Skripterstellung, Variablen, Kontrollfluss |
| csh | 1978 | C-ähnliche Syntax, Jobsteuerung, Aliase |
| ksh | 1983 | Korn-Shell –`sh`+ `csh`-Funktionen |
| bash | 1989 | **Bourne Again Shell** – GNU `sh`-Ersatz |
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash 3.0 | 2004 | `=~`regulärer Ausdruck,`|&`|
| bash 4.0 | 2009 | **Assoziative Arrays**,`mapfile`,`declare -g`|
| bash 4.3 | 2014 | Shellshock-Sicherheitslücke entdeckt |
| bash 5.0 | 2019 | `declare -n`Namensreferenzen,`printf %q`|
| bash 5.1 | 2020 | `wait -n`,`shopt`Verbesserungen |
| bash 5.2 | 2022 | `${var@U}`(Großbuchstaben),`shopt -s compat`|
| zsh | 1990 | Erweiterte Bash – Vervollständigungen, Themen |
| Fisch | 2005 | **Benutzerfreundlich** – automatische Vorschläge, Syntaxhervorhebung |
| nushell | 2019 | Strukturierte Daten, Pipelines von Tabellen |
| Öl/Osche | 2020 | Bash-kompatibel mit besserer Semantik |
## PowerShell-Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| 1,0 | 2006 | Erstveröffentlichung (Microsoft, Jeffrey Snover) |
| 2,0 | 2009 | **Module**, Remoting, Hintergrundjobs, Transaktionen |
| 3,0 | 2012 | Workflows,`Invoke-RestMethod`, geplante Jobs |
| 4,0 | 2013 | **Desired State Configuration (DSC)**,`if`/`switch`Verbesserungen |
| 5,0 | 2016 | **Klassen**,`enum`,`using`,`using module`|
| 5.1 | 2017 | Letzte reine Windows-Version |
| 6,0 | 2018 | **PowerShell Core** – plattformübergreifend (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(experimentell) |
| 6.2 | 2019 | `&&`/`||`Pipeline-Kettenbetreiber |
| 7,0 | 2020 | **Major**:`?.`null-bedingt,`??`null-koaleszierend,`using assembly`|
| 7.1 | 2020 | Ternärer Operator`? :`,`using module`Verbesserungen |
| 7.2 | 2021 | **LTS-Version**, `using namespace`-Verbesserungen |
| 7,3 | 2022 | `switch`Verbesserungen,`ErrorView`Optionen |
| 7,4 | 2023 | `using module`Verbesserungen,`Get-Error`|
| 7,5 | 2024 | Leistungsverbesserungen,`PSResourceGet`|
| 7,6 | 2025 | Kontinuierliche Entwicklung |
## Wichtige Meilensteine
### Unix-Shell-Erbe (1971–1989)
- **1971**: Thompson-Shell – erste Unix-Shell, einfache Befehlsausführung
- **1977**: Bourne-Shell (`sh`) – Variablen, Kontrollfluss (`if`,`while`), Here-Dokumente
- **1978**: C-Shell (`csh`) – C-ähnliche Syntax, Jobsteuerung, Aliase, Verlauf
- **1983**: Korn-Shell (`ksh`) – das Beste aus`sh`+ `csh`
### bash – The Standard (1989–heute)
- **1989**: Brian Fox erstellt Bash für das GNU-Projekt – Bourne Again Shell
- **2.0 (1996)**: `[[ ]]`-Test, `(( ))`-Arithmetik,`+=`
- **4.0 (2009)**: Assoziative Arrays (`declare -A`),`mapfile`
- **5.0 (2019)**: Namerefs,`printf %q`
- **5.2 (2022)**: String-Fallmanipulation
### zsh – The Power User's Shell (1990–heute)
- **1990**: Paul Falstad erstellt zsh – kombiniert Bash-, ksh- und tcsh-Funktionen
- **2000er Jahre**: oh-my-zsh-Framework – Themen, Plugins, Vervollständigungen
- **2019**: macOS-Standard-Shell (ersetzt Bash)
### Fisch – The Friendly Shell (2005–heute)
- **2005**: Axel Liljankrantz kreiert Fische – „Endlich eine interaktive Muschel“
- Autosuggestions, Syntaxhervorhebung, webbasierte Konfiguration
– Nicht Bash-kompatibel – andere Skriptsprache
### PowerShell – Microsofts Shell (2006–heute)
- **2006**: PowerShell 1.0 – .NET-basiert, Objektpipeline, Cmdlets
- **2.0 (2009)**: Module, Remoting, Hintergrundjobs
- **5.0 (2016)**: Klassen, Aufzählungen
- **6.0 (2018)**: **Plattformübergreifend** – PowerShell Core (basiert auf .NET Core)
- **7.0 (2020)**: Null-bedingter `?.`, null-koaleszierender `??`, ternärer `?:`
## Syntaxentwicklung
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

## Wichtige Designprinzipien
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

## Ökosystemwachstum
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
