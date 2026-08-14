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
# Shell y PowerShell: historial de versiones y evolución
## Cronología del shell de Unix
| Versión | Año | Tema clave |
|---------|------|-----------|
| Thompson sh | 1971 | Primer shell Unix (Ken Thompson) |
| Bourne sh | 1977 | **`sh`** — secuencias de comandos, variables, flujo de control |
| cs | 1978 | Sintaxis similar a C, control de trabajos, alias |
| ksh | 1983 | Cáscara de Korn —`sh`+`csh`características |
| fiesta | 1989 | **Bourne Again Shell** — Reemplazo de GNU`sh`|
| fiesta 2.0 | 1996 |  `[[ ]]`, `(( ))`,`+=`|
| fiesta 3.0 | 2004 | `=~`expresión regular,`|&`|
| fiesta 4.0 | 2009 | **Matrices asociativas**, `mapfile`,`declare -g`|
| fiesta 4.3 | 2014 | Vulnerabilidad Shellshock descubierta |
| fiesta 5.0 | 2019 | `declare -n`referencias de nombre,`printf %q`|
| fiesta 5.1 | 2020 |  Mejoras en `wait -n`,`shopt`|
| fiesta 5.2 | 2022 | `${var@U}`(mayúscula),`shopt -s compat`|
| zsh | 1990 | Fiesta extendida: finalizaciones, temas |
| pescado | 2005 | **Fácil de usar**: sugerencias automáticas, resaltado de sintaxis |
| cáscara nula | 2019 | Datos estructurados, canalizaciones de tablas |
| aceite/sst | 2020 | Compatible con Bash con mejor semántica |
## Línea de tiempo de PowerShell
| Versión | Año | Tema clave |
|---------|------|-----------|
| 1.0 | 2006 | Lanzamiento inicial (Microsoft, Jeffrey Snover) |
| 2.0 | 2009 | **Módulos**, comunicación remota, trabajos en segundo plano, transacciones |
| 3.0 | 2012 | Flujos de trabajo, `Invoke-RestMethod`, trabajos programados |
| 4.0 | 2013 | **Configuración de estado deseado (DSC)**, mejoras en`if`/`switch`|
| 5.0 | 2016 | **Clases**, `enum`, `using`,`using module`|
| 5.1 | 2017 | Última versión sólo para Windows |
| 6.0 | 2018 | **PowerShell Core**: multiplataforma (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(experimental) |
| 6.2 | 2019 |  Operadores de cadena de tuberías`&&`/`||`|
| 7.0 | 2020 | **Principal**:`?.`condicional nulo,`??`fusionado nulo,`using assembly`|
| 7.1 | 2020 | Mejoras del operador ternario `? :`,`using module`|
| 7.2 | 2021 | **Lanzamiento LTS**, mejoras en`using namespace`|
| 7.3 | 2022 |  Mejoras `switch`, opciones`ErrorView`|
| 7.4 | 2023 |  Mejoras en `using module`,`Get-Error`|
| 7.5 | 2024 | Mejoras de rendimiento,`PSResourceGet`|
| 7.6 | 2025 | Desarrollo continuo |
## Hitos importantes
### Herencia de Unix Shell (1971–1989)
- **1971**: Thompson shell: primer shell de Unix, ejecución sencilla de comandos
- **1977**: Bourne Shell (`sh`) — variables, flujo de control (`if`,`while`), documentos aquí
- **1978**: C shell (`csh`) — Sintaxis similar a C, control de trabajos, alias, historial
- **1983**: Concha Korn (`ksh`) — lo mejor de`sh`+ `csh`
### bash - El estándar (1989-presente)
- **1989**: Brian Fox crea bash para el proyecto GNU — Bourne Again Shell
- **2.0 (1996)**: prueba `[[ ]]`, aritmética `(( ))`,`+=`
- **4.0 (2009)**: matrices asociativas (`declare -A`),`mapfile`
- **5.0 (2019)**: Referencias de nombre,`printf %q`
- **5.2 (2022)**: Manipulación de mayúsculas y minúsculas en cadenas
### zsh — El Shell del usuario avanzado (1990-presente)
- **1990**: Paul Falstad crea zsh: combina funciones de bash, ksh y tcsh
- **Década de 2000**: marco oh-my-zsh: temas, complementos, finalizaciones
- **2019**: shell predeterminado de macOS (reemplaza a bash)
### pez - The Friendly Shell (2005-presente)
- **2005**: Axel Liljankrantz crea peces — "Por fin, una concha interactiva"
- Autosugerencias, resaltado de sintaxis, configuración basada en web
- No compatible con bash: lenguaje de programación diferente
### PowerShell: Shell de Microsoft (2006-presente)
- **2006**: PowerShell 1.0: canalización de objetos, cmdlets, basados en .NET
- **2.0 (2009)**: Módulos, comunicación remota, trabajos en segundo plano
- **5.0 (2016)**: Clases, enumeraciones
- **6.0 (2018)**: **Multiplataforma**: PowerShell Core (basado en .NET Core)
- **7.0 (2020)**:`?.`condicional nulo,`??`fusionado nulo,`?:`ternario
## Evolución de la sintaxis
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

## Principios clave de diseño
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

## Crecimiento del ecosistema
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
