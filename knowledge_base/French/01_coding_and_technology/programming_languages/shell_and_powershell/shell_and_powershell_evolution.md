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
# Shell & PowerShell — Historique et évolution des versions
## Chronologie du shell Unix
| Version | Année | Thème clé |
|---------|------|-----------|
| Thompson sh | 1971 | Premier shell Unix (Ken Thompson) |
| Bourne sh | 1977 | **`sh`** — scripts, variables, flux de contrôle |
| csh | 1978 | Syntaxe de type C, contrôle des tâches, alias |
| ksh | 1983 | Coque Korn — Fonctionnalités`sh`+`csh`|
| coup | 1989 | **Bourne Again Shell** — Remplacement de GNU`sh`|
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash 3.0 | 2004 |  Expression régulière `=~`,`|&`|
| bash 4.0 | 2009 | **Tableaux associatifs**,`mapfile`,`declare -g`|
| bash 4.3 | 2014 | Vulnérabilité Shellshock découverte |
| bash 5.0 | 2019 | `declare -n`références de nom,`printf %q`|
| bash 5.1 | 2020 |  Améliorations`wait -n`,`shopt`|
| bash 5.2 | 2022 | `${var@U}`(majuscule),`shopt -s compat`|
| zsh | 1990 | Bash étendu – achèvements, thèmes |
| poisson | 2005 | **Convivial** — suggestions automatiques, coloration syntaxique |
| Nushell | 2019 | Données structurées, pipelines de tables |
| huile/CST | 2020 | Compatible avec Bash avec une meilleure sémantique |
## Chronologie PowerShell
| Version | Année | Thème clé |
|---------|------|-----------|
| 1.0 | 2006 | Version initiale (Microsoft, Jeffrey Snover) |
| 2.0 | 2009 | **Modules**, communication à distance, tâches en arrière-plan, transactions |
| 3.0 | 2012 | Flux de travail,`Invoke-RestMethod`, tâches planifiées |
| 4.0 | 2013 | **Configuration de l'état souhaité (DSC)**, améliorations`if`/`switch`|
| 5.0 | 2016 | **Classes**,`enum`,`using`,`using module`|
| 5.1 | 2017 | Dernière version Windows uniquement |
| 6.0 | 2018 | **PowerShell Core** — multiplateforme (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(expérimental) |
| 6.2 | 2019 |  Opérateurs de chaînes de pipelines`&&`/`||`|
| 7.0 | 2020 | **Majeur** : `?.` à condition nulle,`??`à fusion nulle,`using assembly`|
| 7.1 | 2020 | Opérateur ternaire`? :`, améliorations`using module`|
| 7.2 | 2021 | **Version LTS**, améliorations`using namespace`|
| 7.3 | 2022 |  Améliorations du `switch`, options du`ErrorView`|
| 7.4 | 2023 |  Améliorations du `using module`,`Get-Error`|
| 7.5 | 2024 | Améliorations des performances,`PSResourceGet`|
| 7.6 | 2025 | Développement en cours |
## Étapes majeures
### Héritage du shell Unix (1971-1989)
- **1971** : Shell Thompson — premier shell Unix, exécution simple de commandes
- **1977** : Bourne shell (`sh`) — variables, flux de contrôle (`if`,`while`), ici-documents
- **1978** : Shell C (`csh`) — Syntaxe de type C, contrôle des tâches, alias, historique
- **1983** : coque Korn (`ksh`) — le meilleur de`sh`+ `csh`
### bash — Le standard (depuis 1989)
- **1989** : Brian Fox crée bash pour le projet GNU — Bourne Again Shell
- **2.0 (1996)** : test `[[ ]]`, arithmétique `(( ))`,`+=`
- **4.0 (2009)** : tableaux associatifs (`declare -A`),`mapfile`
- **5.0 (2019)** : références de nom,`printf %q`
- **5.2 (2022)** : Manipulation de la casse des chaînes
### zsh — Le shell de l'utilisateur expérimenté (depuis 1990)
- **1990** : Paul Falstad crée zsh — combine les fonctionnalités bash, ksh et tcsh
- **Années 2000** : framework oh-my-zsh — thèmes, plugins, complétions
- **2019** : shell par défaut de macOS (remplace bash)
### poisson - The Friendly Shell (2005-présent)
- **2005** : Axel Liljankrantz crée un poisson — "Enfin un coquillage interactif"
- Suggestions automatiques, coloration syntaxique, configuration basée sur le Web
- Non compatible avec bash - langage de script différent
### PowerShell — Shell de Microsoft (depuis 2006)
- **2006** : PowerShell 1.0 – pipeline d'objets, applets de commande basés sur .NET
- **2.0 (2009)** : Modules, remoting, tâches en arrière-plan
- **5.0 (2016)** : Classes, énumérations
- **6.0 (2018)** : **Multiplateforme** — PowerShell Core (construit sur .NET Core)
- **7.0 (2020)** :`?.`conditionnel nul,`??`à fusion nulle,`?:`ternaire
## Évolution de la syntaxe
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

## Principes de conception clés
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

## Croissance de l'écosystème
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
