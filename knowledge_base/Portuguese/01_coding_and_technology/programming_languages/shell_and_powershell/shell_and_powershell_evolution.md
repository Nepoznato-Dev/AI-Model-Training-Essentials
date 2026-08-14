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
# Shell e PowerShell – Histórico de versões e evolução
## Linha do tempo do shell Unix
| Versão | Ano | Tema principal |
|--------|------|-----------|
| Thompson | 1971 | Primeiro shell Unix (Ken Thompson) |
| Bourne sh | 1977 | **`sh`** — scripts, variáveis, fluxo de controle |
| csh | 1978 | Sintaxe semelhante a C, controle de tarefas, aliases |
| ksh | 1983 | Concha Korn - recursos`sh`+`csh`|
| festa | 1989 | **Bourne Again Shell** — Substituição do GNU`sh`|
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash 3.0 | 2004 |  Regex `=~`,`|&`|
| bash 4.0 | 2009 | **Matrizes associativas**,`mapfile`,`declare -g`|
| bash 4.3 | 2014 | Vulnerabilidade Shellshock descoberta |
| bash 5.0 | 2019 |  Referências de nomes `declare -n`,`printf %q`|
| bash 5.1 | 2020 |  Melhorias`wait -n`,`shopt`|
| bash 5.2 | 2022 | `${var@U}`(maiúsculas),`shopt -s compat`|
| zsh | 1990 | Bash estendido – conclusões, temas |
| peixe | 2005 | **Fácil de usar** — sugestões automáticas, realce de sintaxe |
| nada | 2019 | Dados estruturados, pipelines de tabelas |
| óleo/osh | 2020 | Compatível com Bash com melhor semântica |
## Linha do tempo do PowerShell
| Versão | Ano | Tema principal |
|--------|------|-----------|
| 1,0 | 2006 | Versão inicial (Microsoft, Jeffrey Snover) |
| 2.0 | 2009 | **Módulos**, comunicação remota, trabalhos em segundo plano, transações |
| 3.0 | 2012 | Fluxos de trabalho, `Invoke-RestMethod`, trabalhos agendados |
| 4,0 | 2013 | **Configuração do estado desejado (DSC)**, melhorias em `if`/`switch` |
| 5,0 | 2016 | **Aulas**,`enum`,`using`,`using module`|
| 5.1 | 2017 | Última versão somente para Windows |
| 6,0 | 2018 | **PowerShell Core** — plataforma cruzada (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(experimental) |
| 6.2 | 2019 |  Operadores de cadeia de pipeline`&&`/`||`|
| 7,0 | 2020 | **Principal**:`?.`condicional nulo, coalescência nula `??`,`using assembly`|
| 7.1 | 2020 | Melhorias do operador ternário`? :`,`using module`|
| 7.2 | 2021 | **Lançamento LTS**, melhorias no`using namespace`|
| 7.3 | 2022 |  Melhorias `switch`, opções`ErrorView`|
| 7.4 | 2023 |  Melhorias `using module`,`Get-Error`|
| 7,5 | 2024 | Melhorias de desempenho,`PSResourceGet`|
| 7.6 | 2025 | Desenvolvimento contínuo |
## Marcos importantes
### Herança Unix Shell (1971–1989)
- **1971**: Thompson shell — primeiro shell Unix, execução simples de comandos
- **1977**: Bourne shell (`sh`) — variáveis, fluxo de controle (`if`,`while`), documentos aqui
- **1978**: C shell (`csh`) — Sintaxe semelhante a C, controle de trabalho, aliases, histórico
- **1983**: Concha Korn (`ksh`) — melhor de`sh`+ `csh`
### bash — O Padrão (1989-presente)
- **1989**: Brian Fox cria bash para o projeto GNU — Bourne Again Shell
- **2.0 (1996)**: teste `[[ ]]`, aritmética `(( ))`,`+=`
- **4.0 (2009)**: Matrizes associativas (`declare -A`),`mapfile`
- **5.0 (2019)**: Namerefs,`printf %q`
- **5.2 (2022)**: Manipulação de maiúsculas e minúsculas de string
### zsh — O Shell do usuário avançado (1990-presente)
- **1990**: Paul Falstad cria zsh — combina recursos bash, ksh, tcsh
- **Anos 2000**: estrutura oh-my-zsh — temas, plug-ins, conclusões
- **2019**: shell padrão do macOS (substitui o bash)
### peixe — The Friendly Shell (2005-presente)
- **2005**: Axel Liljankrantz cria peixes — "Finalmente, uma concha interativa"
- Sugestões automáticas, destaque de sintaxe, configuração baseada na web
- Não compatível com bash — linguagem de script diferente
### PowerShell — Shell da Microsoft (2006-presente)
- **2006**: PowerShell 1.0 — baseado em .NET, pipeline de objetos, cmdlets
- **2.0 (2009)**: Módulos, comunicação remota, trabalhos em segundo plano
- **5.0 (2016)**: Classes, enumerações
- **6.0 (2018)**: **Plataforma cruzada** — PowerShell Core (construído em .NET Core)
- **7.0 (2020)**:`?.`condicional nulo,`??`coalescente nulo,`?:`ternário
## Evolução da Sintaxe
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

## Princípios-chave de design
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

## Crescimento do Ecossistema
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
