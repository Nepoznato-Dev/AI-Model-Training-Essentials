<!--
---
# Metadata
title: "Go — Version History & Evolution"
description: "Comprehensive version history and evolution of Go from 1.0 to modern Go."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [go, golang, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Go — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Petsa ng Paglabas | Pangunahing Tema |
|---------|-------------|-----------|
| 1.0 | Mar 2012 | Unang matatag na release |
| 1.1 | Mayo 2013 | Pagganap, race detector |
| 1.3 | Hun 2014 | Network polling, crypto/tls |
| 1.4 | Dis 2014 | Bootstrap na may Go (self-hosting) |
| 1.5 | Ago 2015 | **Kasabay na GC**, sumulat ng mga hadlang |
| 1.7 | Ago 2016 | `context`package,`testing`subtest |
| 1.8 | Peb 2017 | `http.Server.Shutdown`, mga plugin |
| 1.9 | Ago 2017 | Mag-type ng mga alias, parallel`make`|
| 1.10 | Peb 2018 | `database/sql`connection pool |
| 1.11 | Ago 2018 | **Go modules**,`go mod`|
| 1.12 | Peb 2019 | TLS 1.3, bersyon ng module |
| 1.13 | Set 2019 | `errors.Is/As`, mga literal na numero`0b`,`0o`|
| 1.14 | Peb 2020 | **Nag-overlap na I/O sa Windows**, goroutine preemption |
| 1.15 | Ago 2020 | `time.Ticker`/`Timer`reset, module proxy |
| 1.16 | Peb 2021 | `embed`package,`io/fs`, module-aware bilang default |
| 1.17 | Ago 2021 | Slice-to-array na conversion,`unsafe.Slice`|
| 1.18 | Mar 2022 | **Generics**, fuzzing, workspaces |
| 1.19 | Ago 2022 | Mga komento ng doc, rebisyon ng modelo ng memorya |
| 1.20 | Peb 2023 | `errors.Join`, pag-optimize na ginagabayan ng profile |
| 1.21 | Ago 2023 | **`slog`**,`min/max`builtin,`maps/slices`|
| 1.22 | Peb 2024 | Saklaw sa mga integer, pinahusay na pagruruta |
| 1.23 | Ago 2024 | Iterator (`iter`) package, pagbabago ng timer |
| 1.24 | Peb 2025 | `weak`package, pinahusay na mga mapa |
## Mga Pangunahing Milestone
### Ang Simula (2009–2012)
- **2009**: Go inihayag ng Google (Robert Griesemer, Rob Pike, Ken Thompson)
- **2012**: **Go 1.0** — "The Go 1 compatibility promise"
### Pagganap at Tooling (2012–2018)
- **1.1**: 30%+ pagpapabuti ng pagganap; detektor ng lahi
- **1.5**: Kasabay na kolektor ng basura (Ang mga pag-pause ng GC ay bumaba mula millisecond hanggang microseconds)
- **1.5**: Go compiler bootstrapped — nakasulat sa Go (wala nang C)
- **1.7**: Nagiging standard ang`context`package
### Mga Module at Ecosystem (2018–2021)
- **1.11**: **Go modules** — opisyal na pamamahala ng dependency
- **1.13**:`errors.Is/As`— nagiging idiomatic ang error wrapping
- **1.16**:`embed`package — mag-embed ng mga file sa oras ng pag-compile
### Modern Go (2022–kasalukuyan)
- **1.18**: **Generics** — uri ng mga parameter na may mga hadlang
- **1.21**:`slog`— structured logging in stdlib; `min/max`builtin
- **1.22**: Range over integer (`for i := range 10`)
- **1.23**: Iterator package — tamad na pagsusuri sa stdlib
## Generics na Paglalakbay
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## Error sa Paghawak ng Pilosopiya
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## Ebolusyon ng Concurrency
```
1.0:  Goroutines + channels — CSP-inspired
1.1:  Race detector
1.4:  Non-blocking syscalls (net poller)
1.5:  Concurrent GC
1.7:  context package for cancellation
1.14: Cooperative goroutine preemption (signals)
1.21: Synchronization improvements
1.23: iter package — iterator pattern
```

## Go Compatibility Promise
```
Go 1.0 (2012): "Go 1 will be available for a long time.
  Compatibility is important. Programs that work at Go 1
  will continue to work at every subsequent Go 1 release."

This means:
- No breaking changes to the language spec
- No breaking changes to the standard library
- Only additive changes
- Forward compatibility guaranteed
```

## Paglago ng Ecosystem
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## Ebolusyon ng Pagganap
```
Go 1.0:  Baseline
Go 1.1:  ~30% faster (register-based calling prep)
Go 1.5:  Concurrent GC (pause time: ms → μs)
Go 1.7:  SSA backend (15-30% faster)
Go 1.11: PGO experiments
Go 1.13: Faster map operations
Go 1.18: Generics (initial overhead, optimized in 1.19+)
Go 1.20: Profile-guided optimization
Go 1.22: Faster crypto, improved compiler
```
