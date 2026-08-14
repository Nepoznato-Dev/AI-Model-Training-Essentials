---
# Metadata
title: "Julia — Version History & Evolution"
description: "Comprehensive version history and evolution of Julia from 0.1 to modern Julia."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [julia, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Julia - Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| 0,1 | 2013 | Lanzamiento inicial (Bezanson, Karpinski, Viral Shah, Jeff Bezanson) |
| 0,2 | 2013 | Administrador de paquetes, mejoras REPL |
| 0,3 | 2014 | Matrices, álgebra lineal,`Nullable`|
| 0,4 | 2015 | **Programación funcional**: cierres, comprensiones, tipos complejos |
| 0,5 | 2016 | **Principal**: paridad de rendimiento con C para muchos puntos de referencia |
| 0,6 | 2017 |  Tipos `Union`, sintaxis `where`, sistema de tipos mejorado |
| 0,7 | 2018 | **Limpieza masiva**: obsolescencias, tipo `Missing`, `nothing`,`stderr`|
| 1.0 | 2018 | **Primera versión estable**: API estable, comienza el soporte a largo plazo |
| 1.1 | 2019 |  Mejoras `adjoint`, `copy!`,`LinearAlgebra`|
| 1.2 | 2019 | Tuplas con nombre, mejoras en los argumentos de palabras clave |
| 1.3 | 2019 | **Servidor de paquetes**, bases`async`/`await`|
| 1.4 | 2020 |  Mejoras en `import`,`LazyModule`|
| 1.5 | 2020 | **Principal**: inicio más rápido, `--compiled-modules`, compilación en dos fases |
| 1.6 | 2021 | **Lanzamiento LTS**: inicio más rápido, nuevo REPL,`Base64`|
| 1.7 | 2021 |  Bloques `let`, mejoras`@kwdef`|
| 1.8 | 2022 | **Subprocesos de tareas** (tareas paralelas),`@constprop`|
| 1.9 | 2023 | **`@threads` nativo**, precompilación del paquete,`@assume_effects`|
| 1.10 | 2023 | **Principal**: `@ccallable`, inferencia de tipos mejorada,`@constprop :aggressive`|
| 1.11 | 2024 | Otras mejoras de rendimiento,`@assume_effects`|
| 2.0 | Por determinar | (futuro) Se esperan cambios importantes |
## Hitos importantes
### Julia 0.x — El prototipo (2012-2018)
- **2012**: Jeff Bezanson, Stefan Karpinski, Viral Shah y Alan Edelman comienzan con Julia en el MIT
- **Objetivo**: "Camina como Python, ejecuta como C": sintaxis de alto nivel con rendimiento de bajo nivel.
- **0.1 (2013)**: primer lanzamiento público: envío múltiple, JIT basado en LLVM
- **0.4 (2015)**: Funciones de programación funcional: cierres, comprensiones
- **0,5 (2016)**: hito de rendimiento: coincide con C en muchos puntos de referencia
- **0.6 (2017)**: tipos `Union`, sintaxis `where`
- **0.7 (2018)**: Limpieza masiva: tipo `Missing`,`nothing`reemplaza a `nothing`, eliminación de obsolescencia
### Julia 1.0 — Estabilidad (2018)
- **Primera API estable**: compatibilidad con versiones anteriores garantizada en 1.x
- Despacho múltiple, tipos paramétricos, metaprogramación, corrutinas.
- Administrador de paquetes incorporado (Pkg)
- Hilos verdes (Tareas)
### Julia 1.x: rendimiento y paralelismo (2019-presente)
- **1.5 (2020)**: tiempo de inicio más rápido (crítico para el uso de CLI)
- **1.6 (2021)**: LTS: nuevo REPL, inicio más rápido, sistema de artefactos
- **1.8 (2022)**: **Subprocesos de tareas**: ejecuta tareas en varios subprocesos del sistema operativo
- **1.9 (2023)**:`@threads`nativo con programación`:static`y `:dynamic`
- **1.10 (2023)**: importantes mejoras de rendimiento, mejor inferencia de tipos
- **1.11 (2024)**: optimización continua
## Evolución del envío múltiple
```julia
# Julia's core feature: multiple dispatch
# Method selection based on ALL argument types

# Basic methods
function area(shape)
    error("Unknown shape")
end

area(c::Circle) = π * c.r^2
area(r::Rectangle) = r.w * r.h

# Parametric types
struct Point{T <: Real}
    x::T
    y::T
end

# Dispatch on type parameters
distance(p1::Point{T}, p2::Point{T}) where {T} =
    sqrt((p1.x - p2.x)^2 + (p1.y - p2.y)^2)

# Union types (0.6+)
process(x::Union{Int, Float64}) = x * 2

# Julia 1.0+: Clean type system
function solve(A::AbstractMatrix{T}, b::AbstractVector{T}) where {T <: Number}
    # Works for any numeric type
    A \ b
end
```

## Evolución del rendimiento
```
Julia 0.1:  JIT via LLVM — promising but inconsistent
Julia 0.5:  "C-competitive" on many benchmarks (177 benchmarks)
Julia 1.0:  Stable, fast startup
Julia 1.5:  Faster startup (critical for CLI tools)
Julia 1.8:  Task threads — multi-core parallelism
Julia 1.9:  Native @threads, package precompilation
Julia 1.10: Major type inference improvements
Julia 1.11: Further optimizations
Target:     Sub-millisecond startup, C-competitive throughput
```

## Concurrencia y paralelismo
```
0.1:  Tasks (green threads, cooperative)
0.5:  Channel (producer-consumer)
1.0:  Distributed computing (Distributed stdlib)
1.3:  Package server, async foundations
1.8:  Task threads — Tasks run on OS threads
1.9:  @threads :static / :dynamic
1.10: Improved thread safety
2.0+: (planned) Better async/await, effect handlers
```

## Principios clave de diseño
```
1. "Walk like Python, run like C" — high-level syntax, low-level speed
2. "Multiple dispatch is king" — functions dispatch on all argument types
3. "No performance cliffs" — generic code should be fast
4. "Composable" — small primitives, compose freely
5. "Interactive" — REPL-first, notebook-friendly
6. "Scientific" — built for numerical/scientific computing
```

## Crecimiento del ecosistema
```
2012: Julia development begins at MIT
2013: Julia 0.1 released publicly
2014: JuliaCon first held
2016: Julia 0.5 — performance milestone
2017: Julia 0.6 — type system improvements
2018: Julia 1.0 — first stable release
2019: JuliaHub founded — commercial support
2020: Julia 1.5 — faster startup
2021: Julia 1.6 — LTS release
2022: Julia 1.8 — task threads
2025: Julia powers scientific computing, climate modeling (CliMA),
       astronomy (Celeste), bioinformatics, quantitative finance
       10,000+ registered packages
       Used by: NASA, MIT, Stanford, Pfizer, Aviva, Federal Reserve
```
