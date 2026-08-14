<!--
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

-->
# Julia – Histórico de versões e evolução
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| 0,1 | 2013 | Lançamento inicial (Bezanson, Karpinski, Viral Shah, Jeff Bezanson) |
| 0,2 | 2013 | Gerenciador de pacotes, melhorias no REPL |
| 0,3 | 2014 | Matrizes, álgebra linear,`Nullable`|
| 0,4 | 2015 | **Programação funcional**: fechamentos, compreensões, tipos complexos |
| 0,5 | 2016 | **Principal**: paridade de desempenho com C para muitos benchmarks |
| 0,6 | 2017 |  Tipos `Union`, sintaxe `where`, sistema de tipos aprimorado |
| 0,7 | 2018 | **Limpeza massiva**: descontinuações, tipo `Missing`,`nothing`,`stderr`|
| 1,0 | 2018 | **Primeira versão estável**: API estável, início do suporte de longo prazo |
| 1.1 | 2019 |  Melhorias em`adjoint`,`copy!`,`LinearAlgebra`|
| 1.2 | 2019 | Tuplas nomeadas, melhorias em argumentos de palavras-chave |
| 1.3 | 2019 | **Servidor de pacotes**, bases`async`/`await`|
| 1.4 | 2020 |  Melhorias `import`,`LazyModule`|
| 1,5 | 2020 | **Principal**: inicialização mais rápida,`--compiled-modules`, compilação em duas fases |
| 1.6 | 2021 | **Lançamento LTS**: inicialização mais rápida, novo REPL,`Base64`|
| 1.7 | 2021 |  Blocos `let`, melhorias`@kwdef`|
| 1.8 | 2022 | **Threads de tarefas** (tarefas paralelas),`@constprop`|
| 1,9 | 2023 | **`@threads` nativo **, pré-compilação de pacote,`@assume_effects`|
| 1.10 | 2023 | **Principal**:`@ccallable`, inferência de tipo aprimorada,`@constprop :aggressive`|
| 1.11 | 2024 | Outras melhorias de desempenho,`@assume_effects`|
| 2.0 | A definir | (futuro) Mudanças significativas esperadas |
## Marcos importantes
### Julia 0.x — O Protótipo (2012–2018)
- **2012**: Jeff Bezanson, Stefan Karpinski, Viral Shah e Alan Edelman iniciam Julia no MIT
- **Objetivo**: "Ande como Python, execute como C" — sintaxe de alto nível com desempenho de baixo nível
- **0.1 (2013)**: Primeiro lançamento público — despacho múltiplo, JIT baseado em LLVM
- **0.4 (2015)**: Recursos de programação funcional — fechamentos, compreensões
- **0,5 (2016)**: marco de desempenho — corresponde a C em muitos benchmarks
- **0.6 (2017)**: tipos `Union`, sintaxe `where`
- **0.7 (2018)**: Limpeza massiva — tipo `Missing`,`nothing`substitui`nothing`, remoção de descontinuação
### Julia 1.0 – Estabilidade (2018)
- **Primeira API estável** — compatibilidade com versões anteriores garantida na versão 1.x
- Despacho múltiplo, tipos paramétricos, metaprogramação, corrotinas
- Gerenciador de pacotes integrado (Pkg)
- Tópicos verdes (tarefas)
### Julia 1.x - Desempenho e paralelismo (2019-presente)
- **1.5 (2020)**: Tempo de inicialização mais rápido (crítico para uso CLI)
- **1.6 (2021)**: LTS — novo REPL, inicialização mais rápida, sistema de artefatos
- **1.8 (2022)**: **Threads de tarefas** — execute tarefas em vários threads de sistema operacional
- **1.9 (2023)**:`@threads`nativo com agendamento`:static`e `:dynamic`
- **1.10 (2023)**: Grandes melhorias de desempenho, melhor inferência de tipo
- **1.11 (2024)**: Otimização contínua
## Evolução de despacho múltiplo
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

## Evolução do desempenho
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

## Simultaneidade e paralelismo
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

## Princípios-chave de design
```
1. "Walk like Python, run like C" — high-level syntax, low-level speed
2. "Multiple dispatch is king" — functions dispatch on all argument types
3. "No performance cliffs" — generic code should be fast
4. "Composable" — small primitives, compose freely
5. "Interactive" — REPL-first, notebook-friendly
6. "Scientific" — built for numerical/scientific computing
```

## Crescimento do Ecossistema
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
