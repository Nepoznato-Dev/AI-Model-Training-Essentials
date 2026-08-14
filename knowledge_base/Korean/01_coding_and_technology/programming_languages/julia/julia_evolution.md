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
# Julia — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 0.1 | 2013 | 최초 릴리스(Bezanson, Karpinski, Viral Shah, Jeff Bezanson) |
| 0.2 | 2013 | 패키지 관리자, REPL 개선 |
| 0.3 | 2014 | 배열, 선형 대수,`Nullable`|
| 0.4 | 2015 | **함수형 프로그래밍**: 클로저, 컴프리헨션, 복합 유형 |
| 0.5 | 2016 | **주요**: 많은 벤치마크에서 C와 성능 동등 |
| 0.6 | 2017 | `Union`유형,`where`구문, 향상된 유형 시스템 |
| 0.7 | 2018 | **대규모 정리**: 지원 중단,`Missing`유형,`nothing`,`stderr`|
| 1.0 | 2018 | **첫 번째 안정적인 릴리스**: 안정적인 API, 장기 지원 시작 |
| 1.1 | 2019 | `adjoint`,`copy!`,`LinearAlgebra`개선 |
| 1.2 | 2019 | 명명된 튜플, 키워드 인수 개선 |
| 1.3 | 2019 | **패키지 서버**,`async`/`await`기반 |
| 1.4 | 2020 | `import`개선,`LazyModule`|
| 1.5 | 2020 | **주요**: 빠른 시작, `--compiled-modules`, 2단계 컴파일 |
| 1.6 | 2021 | **LTS 릴리스**: 더 빠른 시작, 새로운 REPL,`Base64`|
| 1.7 | 2021 | `let`블록,`@kwdef`개선 |
| 1.8 | 2022 | **작업 스레드**(병렬 작업),`@constprop`|
| 1.9 | 2023년 | **네이티브`@threads`**, 패키지 사전 컴파일,`@assume_effects`|
| 1.10 | 2023년 | **주요**:`@ccallable`, 향상된 유형 추론,`@constprop :aggressive`|
| 1.11 | 2024 | 더욱 향상된 성능,`@assume_effects`|
| 2.0 | 미정 | (향후) 획기적인 변화가 예상됨 |
## 주요 이정표
### Julia 0.x — 프로토타입(2012~2018)
- **2012**: Jeff Bezanson, Stefan Karpinski, Viral Shah 및 Alan Edelman이 MIT에서 Julia 시작
- **목표**: "Python처럼 걷고 C처럼 실행" — 낮은 수준의 성능을 갖춘 높은 수준의 구문
- **0.1(2013)**: 최초 공개 릴리스 — 다중 디스패치, LLVM 기반 JIT
- **0.4 (2015)**: 함수형 프로그래밍 기능 — 클로저, 컴프리헨션
- **0.5(2016)**: 성능 이정표 — 여러 벤치마크에서 C와 일치
- **0.6 (2017)**:`Union`유형,`where`구문
- **0.7(2018)**: 대규모 정리 —`Missing`유형, `nothing`가 `nothing`를 대체하고 지원 중단 제거
### Julia 1.0 — 안정성(2018)
- **최초의 안정적인 API** — 1.x 내에서 이전 버전과의 호환성 보장
- 다중 디스패치, 파라메트릭 유형, 메타프로그래밍, 코루틴
- 패키지 관리자(Pkg) 내장
- 녹색 스레드(작업)
### Julia 1.x — 성능 및 병렬성(2019~현재)
- **1.5(2020)**: 더 빠른 시작 시간(CLI 사용에 중요)
- **1.6(2021)**: LTS — 새로운 REPL, 더 빠른 시작, 아티팩트 시스템
- **1.8(2022)**: **작업 스레드** — 여러 OS 스레드에서 작업 실행
- **1.9(2023)**:`:static`및`:dynamic`예약 기능을 갖춘 네이티브 `@threads`
- **1.10(2023)**: 주요 성능 개선, 유형 추론 개선
- **1.11(2024)**: 지속적인 최적화
## 다중 디스패치의 진화
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

## 성능의 진화
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

## 동시성 및 병렬성
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

## 주요 디자인 원칙
```
1. "Walk like Python, run like C" — high-level syntax, low-level speed
2. "Multiple dispatch is king" — functions dispatch on all argument types
3. "No performance cliffs" — generic code should be fast
4. "Composable" — small primitives, compose freely
5. "Interactive" — REPL-first, notebook-friendly
6. "Scientific" — built for numerical/scientific computing
```

## 생태계 성장
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
