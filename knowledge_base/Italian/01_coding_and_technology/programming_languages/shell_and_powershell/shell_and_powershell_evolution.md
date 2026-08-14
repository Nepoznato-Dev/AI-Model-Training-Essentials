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
# Shell e PowerShell: cronologia ed evoluzione delle versioni
## Cronologia della shell Unix
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| Thompson sh | 1971 | Prima shell Unix (Ken Thompson) |
| Bourne sh | 1977 | **`sh`** — scripting, variabili, flusso di controllo |
| csh | 1978 | Sintassi tipo C, controllo dei lavori, alias |
| ksh | 1983 | Guscio Korn — Caratteristiche`sh`+`csh`|
| bash | 1989 | **Bourne Again Shell** — Sostituzione GNU`sh`|
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash 3.0 | 2004| `=~`espressione regolare,`|&`|
| bash 4.0 | 2009| **Array associativi**,`mapfile`,`declare -g`|
| bash4.3 | 2014| Scoperta la vulnerabilità Shellshock |
| bash 5.0 | 2019 | `declare -n`riferimento nome,`printf %q`|
| bash 5.1 | 2020 | `wait -n`,`shopt`miglioramenti |
| bash 5.2 | 2022 | `${var@U}`(maiuscolo),`shopt -s compat`|
| zsh | 1990 | Bash estesa: completamenti, temi |
| pesce | 2005| **Facile da usare**: suggerimenti automatici, evidenziazione della sintassi |
| poche parole | 2019 | Dati strutturati, pipeline di tabelle |
| petrolio/ssl | 2020 | Compatibile con Bash con semantica migliore |
## Cronologia di PowerShell
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| 1.0 | 2006| Versione iniziale (Microsoft, Jeffrey Snover) |
| 2.0 | 2009| **Moduli**, remoting, lavori in background, transazioni |
| 3.0 | 2012| Flussi di lavoro,`Invoke-RestMethod`, lavori pianificati |
| 4.0 | 2013| **Configurazione dello stato desiderato (DSC)**, miglioramenti`if`/`switch`|
| 5.0 | 2016| **Classi**,`enum`,`using`,`using module`|
| 5.1 | 2017 | Ultima versione solo per Windows |
| 6.0 | 2018 | **PowerShell Core**: multipiattaforma (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(sperimentale) |
| 6.2 | 2019 | `&&`/`||`operatori di catene di condutture |
| 7.0| 2020 | **Maggiore**:`?.`nullo condizionale,`??`nullo a coalescenza,`using assembly`|
| 7.1 | 2020 | Miglioramenti all'operatore ternario`? :`,`using module`|
| 7.2 | 2021 | **Versione LTS**, miglioramenti`using namespace`|
| 7.3| 2022 |  Miglioramenti `switch`, opzioni`ErrorView`|
| 7.4| 2023 |  Miglioramenti `using module`,`Get-Error`|
| 7,5 | 2024 | Miglioramenti delle prestazioni,`PSResourceGet`|
| 7.6| 2025 | Sviluppo continuo |
## Traguardi importanti
### Eredità Unix Shell (1971–1989)
- **1971**: Thompson shell: prima shell Unix, semplice esecuzione di comandi
- **1977**: Bourne shell (`sh`) — variabili, flusso di controllo (`if`,`while`), qui-documenti
- **1978**: C shell (`csh`) — sintassi simile a C, controllo dei lavori, alias, cronologia
- **1983**: Conchiglia Korn (`ksh`) — il meglio di`sh`+ `csh`
### bash - The Standard (1989-oggi)
- **1989**: Brian Fox crea bash per il progetto GNU — Bourne Again Shell
- **2.0 (1996)**: test `[[ ]]`, aritmetica `(( ))`,`+=`
- **4.0 (2009)**: array associativi (`declare -A`),`mapfile`
- **5.0 (2019)**: Riferimenti nome,`printf %q`
- **5.2 (2022)**: manipolazione di maiuscole e minuscole
### zsh - La shell dell'utente esperto (1990-oggi)
- **1990**: Paul Falstad crea zsh: combina le funzionalità bash, ksh e tcsh
- **Anni 2000**: framework oh-my-zsh: temi, plugin, completamenti
- **2019**: shell predefinita di macOS (sostituisce bash)
### pesce - The Friendly Shell (2005-oggi)
- **2005**: Axel Liljankrantz crea il pesce — "Finalmente una conchiglia interattiva"
- Suggerimenti automatici, evidenziazione della sintassi, configurazione basata sul web
- Non compatibile con bash: linguaggio di scripting diverso
### PowerShell: Shell di Microsoft (2006-oggi)
- **2006**: PowerShell 1.0: pipeline di oggetti, cmdlet basati su .NET
- **2.0 (2009)**: Moduli, servizi remoti, lavori in background
- **5.0 (2016)**: classi, enumerazioni
- **6.0 (2018)**: **Multipiattaforma**: PowerShell Core (basato su .NET Core)
- **7.0 (2020)**:`?.`condizionale nullo,`??`a coalescenza nulla,`?:`ternario
## Evoluzione della sintassi
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

## Principi chiave di progettazione
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

## Crescita dell'ecosistema
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
