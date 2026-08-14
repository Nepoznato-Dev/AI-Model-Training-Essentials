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
# Shell i PowerShell — historia wersji i ewolucja
## Oś czasu powłoki Uniksa
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| Thompson sh | 1971 | Pierwsza powłoka Uniksa (Ken Thompson) |
| Bourne sh | 1977 | **`sh`** — skrypty, zmienne, przepływ sterowania |
| csh | 1978 | Składnia podobna do języka C, kontrola zadań, aliasy |
| ksz | 1983 | Powłoka Korna — funkcje`sh`+`csh`|
| bash | 1989 | **Bourne Again Shell** — zamiennik GNU`sh`|
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash 3.0 | 2004 |  Wyrażenie regularne `=~`,`|&`|
| bash 4.0 | 2009 | **Tablice asocjacyjne**,`mapfile`,`declare -g`|
| bash 4.3 | 2014 | Odkryto lukę w Shellshock |
| bash 5.0 | 2019 |  Referencje nazw `declare -n`,`printf %q`|
| bash 5.1 | 2020 |  Ulepszenia`wait -n`,`shopt`|
| bash 5.2 | 2022 | `${var@U}`(wielkie litery),`shopt -s compat`|
| zsh | 1990 | Rozszerzony bash — uzupełnienia, motywy |
| ryba | 2005 | **Przyjazny dla użytkownika** — autosugestie, podświetlanie składni |
| nushell | 2019 | Dane strukturalne, potoki tabel |
| olej/bhp | 2020 | Kompatybilny z Bashem i lepszą semantyką |
## Oś czasu programu PowerShell
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| 1,0 | 2006 | Wersja pierwsza (Microsoft, Jeffrey Snover) |
| 2,0 | 2009 | **Moduły**, zdalne, zadania w tle, transakcje |
| 3,0 | 2012 | Przepływy pracy,`Invoke-RestMethod`, zaplanowane zadania |
| 4,0 | 2013 | **Konfiguracja żądanego stanu (DSC)**, ulepszenia`if`/`switch`|
| 5,0 | 2016 | **Klasy**,`enum`,`using`,`using module`|
| 5.1 | 2017 | Ostatnia wersja tylko dla systemu Windows |
| 6,0 | 2018 | **PowerShell Core** — wieloplatformowy (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(eksperymentalny) |
| 6.2 | 2019 |  Operatorzy łańcucha rurociągów`&&`/`||`|
| 7,0 | 2020 | **Główne**:`?.`warunek zerowy,`??`łączenie wartości zerowej,`using assembly`|
| 7.1 | 2020 | Ulepszenia operatora trójskładnikowego`? :`,`using module`|
| 7.2 | 2021 | **Wersja LTS**, ulepszenia`using namespace`|
| 7.3 | 2022 |  Ulepszenia `switch`, opcje`ErrorView`|
| 7,4 | 2023 |  Ulepszenia `using module`,`Get-Error`|
| 7,5 | 2024 | Ulepszenia wydajności,`PSResourceGet`|
| 7,6 | 2025 | Ciągły rozwój |
## Główne kamienie milowe
### Dziedzictwo powłoki Uniksa (1971–1989)
- **1971**: Powłoka Thompsona — pierwsza powłoka Uniksa, proste wykonywanie poleceń
- **1977**: Powłoka Bourne'a (`sh`) — zmienne, przepływ sterowania (`if`,`while`), dokumenty tutaj
- **1978**: Powłoka C (`csh`) — składnia podobna do C, kontrola zadań, aliasy, historia
- **1983**: Korn Shell (`ksh`) — najlepszy z`sh`+ `csh`
### bash — Standard (1989 – obecnie)
- **1989**: Brian Fox tworzy basha dla projektu GNU — Bourne Again Shell
- **2.0 (1996)**: test `[[ ]]`, arytmetyka `(( ))`,`+=`
- **4.0 (2009)**: Tablice asocjacyjne (`declare -A`),`mapfile`
- **5.0 (2019)**: Namerefs,`printf %q`
- **5.2 (2022)**: Manipulacja wielkością liter
### zsh — Powłoka zaawansowanego użytkownika (1990 – obecnie)
- **1990**: Paul Falstad tworzy zsh — łączy funkcje bash, ksh, tcsh
- **2000s**: framework oh-my-zsh — motywy, wtyczki, uzupełnienia
- **2019**: domyślna powłoka macOS (zastępuje bash)
### ryba — Przyjazna muszla (2005 – obecnie)
- **2005**: Axel Liljankrantz tworzy ryby — „Wreszcie interaktywna muszla”
- Autosugestie, podświetlanie składni, konfiguracja internetowa
- Nie jest kompatybilny z bashem - inny język skryptowy
### PowerShell — powłoka Microsoftu (2006 – obecnie)
- **2006**: PowerShell 1.0 — oparty na .NET, potok obiektowy, polecenia cmdlet
- **2.0 (2009)**: Moduły, zdalne, zadania w tle
- **5.0 (2016)**: Klasy, wyliczenia
- **6.0 (2018)**: **Wiele platform** — PowerShell Core (zbudowany na platformie .NET Core)
- **7,0 (2020)**: Warunek zerowy`?.`, łączenie wartości zerowej`??`, trójskładnikowy `?:`
## Ewolucja składni
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

## Kluczowe zasady projektowania
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

## Rozwój ekosystemu
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
