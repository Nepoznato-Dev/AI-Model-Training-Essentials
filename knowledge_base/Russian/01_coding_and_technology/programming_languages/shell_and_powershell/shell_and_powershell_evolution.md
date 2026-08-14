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
# Shell и PowerShell — история версий и эволюция
## Временная шкала оболочки Unix
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| Томпсон ш | 1971 | Первая оболочка Unix (Кен Томпсон) |
| Борн ш | 1977 | **`sh`** — сценарии, переменные, поток управления |
| КШ | 1978 | C-подобный синтаксис, управление заданиями, псевдонимы |
| кш | 1983 | Оболочка Korn — возможности`sh`+`csh`|
| баш | 1989 | **Bourne Again Shell** — замена GNU`sh`|
| Баш 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| Баш 3.0 | 2004 |  регулярное выражение `=~`,`|&`|
| Баш 4.0 | 2009 | **Ассоциативные массивы**,`mapfile`,`declare -g`|
| Баш 4.3 | 2014 | Обнаружена уязвимость Shellshock |
| Баш 5.0 | 2019 | `declare -n`namerefs,`printf %q`|
| Баш 5.1 | 2020 |  Улучшения `wait -n`,`shopt`|
| Баш 5.2 | 2022 | `${var@U}`(прописные),`shopt -s compat`|
| зш | 1990 | Extended bash — доработки, темы |
| рыба | 2005 | **Удобство** — автопредложения, подсветка синтаксиса |
| нушелл | 2019 | Структурированные данные, конвейеры таблиц |
| нефть/Ош | 2020 | Bash-совместимость с лучшей семантикой |
## Временная шкала PowerShell
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| 1.0 | 2006 | Первоначальный выпуск (Microsoft, Джеффри Сновер) |
| 2.0 | 2009 | **Модули**, удаленное взаимодействие, фоновые задания, транзакции |
| 3.0 | 2012 | Рабочие процессы, `Invoke-RestMethod`, запланированные задания |
| 4.0 | 2013 | **Конфигурация желаемого состояния (DSC)**, улучшения `if`/`switch` |
| 5.0 | 2016 | **Классы**,`enum`,`using`,`using module`|
| 5.1 | 2017 | Последняя версия только для Windows |
| 6.0 | 2018 | **PowerShell Core** — кроссплатформенность (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(экспериментальный) |
| 6.2 | 2019 |  Операторы трубопроводной цепи`&&`/`||`|
| 7.0 | 2020 | **Основные**:`?.`с нулевым условием,`??`с нулевым объединением,`using assembly`|
| 7.1 | 2020 | Тернарный оператор `? :`, улучшения`using module`|
| 7.2 | 2021 | **LTS-релиз**, улучшения`using namespace`|
| 7.3 | 2022 |  Улучшения `switch`, опции`ErrorView`|
| 7.4 | 2023 |  Улучшения `using module`,`Get-Error`|
| 7,5 | 2024 | Улучшения производительности,`PSResourceGet`|
| 7,6 | 2025 | Постоянное развитие |
## Основные вехи
### Наследие оболочки Unix (1971–1989)
- **1971**: оболочка Thompson — первая оболочка Unix, простое выполнение команд.
- **1977**: оболочка Bourne (`sh`) — переменные, поток управления (`if`,`while`), здесь-документы
- **1978**: оболочка C (`csh`) — синтаксис C-подобного типа, управление заданиями, псевдонимы, история.
- **1983**: оболочка Korn (`ksh`) — лучшее из`sh`+ `csh`
### bash — Стандарт (1989 – настоящее время)
- **1989**: Брайан Фокс создает bash для проекта GNU — Bourne Again Shell
- **2.0 (1996 г.)**: тест `[[ ]]`, арифметика `(( ))`,`+=`
- **4.0 (2009 г.)**: Ассоциативные массивы (`declare -A`), `mapfile`. 
- **5.0 (2019 г.)**: Namerefs,`printf %q`
- **5.2 (2022 г.)**: Манипулирование регистром строк.
### zsh — Оболочка опытного пользователя (1990 – настоящее время)
- **1990**: Пол Фалстад создает zsh — сочетает в себе функции bash, ksh и tcsh.
- **2000-е**: фреймворк oh-my-zsh — темы, плагины, дополнения.
- **2019**: оболочка macOS по умолчанию (заменяет bash).
### рыба — The Friendly Shell (2005 – настоящее время)
- **2005**: Аксель Лильянкранц создает рыбу — «Наконец-то интерактивная оболочка».
- Автопредложения, подсветка синтаксиса, веб-конфигурация
- Несовместим с bash — другой язык сценариев.
### PowerShell — оболочка Microsoft (2006 – настоящее время)
- **2006**: PowerShell 1.0 — конвейер объектов, командлеты на основе .NET.
- **2.0 (2009 г.)**: Модули, удаленное взаимодействие, фоновые задания.
- **5.0 (2016 г.)**: Классы, перечисления.
- **6.0 (2018 г.)**: **Кроссплатформенность** — PowerShell Core (на базе .NET Core).
- **7.0 (2020 г.)**:`?.`с нулевым условием,`??`с нулевым объединением, троичный `?:`
## Эволюция синтаксиса
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

## Ключевые принципы проектирования
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

## Рост экосистемы
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
