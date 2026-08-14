---
# Metadata
title: "Julia — Version History & Evolution"
description: "Comprehensive version history and evolution of Julia from 0.1 to modern Julia."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# Julia — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| 0.1 | 2013 | Paunang release (Bezanson, Karpinski, Viral Shah, Jeff Bezanson) |
| 0.2 | 2013 | Package manager, REPL improvements |
| 0.3 | 2014 | Mga array, linear algebra,`Nullable`|
| 0.4 | 2015 | **Functional programming**: mga pagsasara, pag-unawa, kumplikadong mga uri |
| 0.5 | 2016 | **Major**: pagkakapare-pareho ng pagganap sa C para sa maraming mga benchmark |
| 0.6 | 2017 |  Mga uri ng `Union`, syntax ng `where`, pinahusay na sistema ng uri |
| 0.7 | 2018 | **Malaking paglilinis**: mga paghinto, uri ng `Missing`,`nothing`,`stderr`|
| 1.0 | 2018 | **Unang stable na release**: stable na API, magsisimula ang pangmatagalang suporta |
| 1.1 | 2019 | `adjoint`,`copy!`,`LinearAlgebra`mga pagpapabuti |
| 1.2 | 2019 | Pinangalanang tuple, mga pagpapahusay sa argumento ng keyword |
| 1.3 | 2019 | **Package server**,`async`/`await`foundations |
| 1.4 | 2020 | `import`mga pagpapabuti,`LazyModule`|
| 1.5 | 2020 | **Major**: mas mabilis na pagsisimula,`--compiled-modules`, two-phase compilation |
| 1.6 | 2021 | **LTS release**: mas mabilis na startup, bagong REPL,`Base64`|
| 1.7 | 2021 | `let`block,`@kwdef`mga pagpapabuti |
| 1.8 | 2022 | **Mga thread ng gawain** (mga parallel na gawain),`@constprop`|
| 1.9 | 2023 | **Native`@threads`**, package precompilation,`@assume_effects`|
| 1.10 | 2023 | **Major**:`@ccallable`, pinahusay na uri ng inference,`@constprop :aggressive`|
| 1.11 | 2024 | Mga karagdagang pagpapahusay sa pagganap,`@assume_effects`|
| 2.0 | TBD | (hinaharap) Inaasahan ang mga breaking na pagbabago |
## Mga Pangunahing Milestone
### Julia 0.x — The Prototype (2012–2018)
- **2012**: Sina Jeff Bezanson, Stefan Karpinski, Viral Shah, at Alan Edelman ay nagsimula kay Julia sa MIT
- **Layunin**: "Maglakad tulad ng Python, tumakbo tulad ng C" — mataas na antas na syntax na may mababang antas ng pagganap
- **0.1 (2013)**: Unang pampublikong release — maramihang dispatch, LLVM-based na JIT
- **0.4 (2015)**: Mga functional na feature ng programming — mga pagsasara, pag-unawa
- **0.5 (2016)**: Performance milestone — tumutugma sa C sa maraming benchmark
- **0.6 (2017)**: Mga uri ng `Union`, syntax ng `where`
- **0.7 (2018)**: Napakalaking paglilinis — Uri ng `Missing`, pinapalitan ng`nothing`ang`nothing`, pag-alis ng paghinto
### Julia 1.0 — Katatagan (2018)
- **Unang stable na API** — garantisadong backward compatibility sa loob ng 1.x
- Maramihang dispatch, mga uri ng parametric, metaprogramming, coroutine
- Built-in na manager ng package (Pkg)
- Mga berdeng thread (Mga Gawain)
### Julia 1.x — Pagganap at Paralelismo (2019–kasalukuyan)
- **1.5 (2020)**: Mas mabilis na oras ng pagsisimula (kritikal para sa paggamit ng CLI)
- **1.6 (2021)**: LTS — bagong REPL, mas mabilis na startup, artifact system
- **1.8 (2022)**: **Task thread** — magpatakbo ng Tasks sa maraming OS thread
- **1.9 (2023)**: Native`@threads`na may`:static`at`:dynamic`na pag-iskedyul
- **1.10 (2023)**: Mga pangunahing pagpapahusay sa pagganap, mas mahusay na uri ng hinuha
- **1.11 (2024)**: Patuloy na pag-optimize
## Maramihang Dispatch Evolution
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

## Ebolusyon ng Pagganap
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

## Concurrency at Paralelismo
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

## Pangunahing Prinsipyo ng Disenyo
```
1. "Walk like Python, run like C" — high-level syntax, low-level speed
2. "Multiple dispatch is king" — functions dispatch on all argument types
3. "No performance cliffs" — generic code should be fast
4. "Composable" — small primitives, compose freely
5. "Interactive" — REPL-first, notebook-friendly
6. "Scientific" — built for numerical/scientific computing
```

## Paglago ng Ecosystem
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
