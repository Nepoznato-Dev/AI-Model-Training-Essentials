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
# Go — Version History & Evolution

## Timeline

| Version | Release Date | Key Theme |
|---------|-------------|-----------|
| 1.0     | Mar 2012    | First stable release |
| 1.1     | May 2013    | Performance, race detector |
| 1.3     | Jun 2014    | Network polling, crypto/tls |
| 1.4     | Dec 2014    | Bootstrap with Go (self-hosting) |
| 1.5     | Aug 2015    | **Concurrent GC**, write barriers |
| 1.7     | Aug 2016    | `context` package, `testing` subtests |
| 1.8     | Feb 2017    | `http.Server.Shutdown`, plugins |
| 1.9     | Aug 2017    | Type aliases, parallel `make` |
| 1.10    | Feb 2018    | `database/sql` connection pool |
| 1.11    | Aug 2018    | **Go modules**, `go mod` |
| 1.12    | Feb 2019    | TLS 1.3, module versioning |
| 1.13    | Sep 2019    | `errors.Is/As`, number literals `0b`, `0o` |
| 1.14    | Feb 2020    | **Overlapped I/O on Windows**, goroutine preemption |
| 1.15    | Aug 2020    | `time.Ticker`/`Timer` reset, module proxy |
| 1.16    | Feb 2021    | `embed` package, `io/fs`, module-aware by default |
| 1.17    | Aug 2021    | Slice-to-array conversion, `unsafe.Slice` |
| 1.18    | Mar 2022    | **Generics**, fuzzing, workspaces |
| 1.19    | Aug 2022    | Doc comments, memory model revision |
| 1.20    | Feb 2023    | `errors.Join`, profile-guided optimization |
| 1.21    | Aug 2023    | **`slog`**, `min/max` builtins, `maps/slices` |
| 1.22    | Feb 2024    | Range over integers, enhanced routing |
| 1.23    | Aug 2024    | Iterator (`iter`) package, timer changes |
| 1.24    | Feb 2025    | `weak` package, improved maps |

## Major Milestones

### The Beginning (2009–2012)
- **2009**: Go announced by Google (Robert Griesemer, Rob Pike, Ken Thompson)
- **2012**: **Go 1.0** — "The Go 1 compatibility promise"

### Performance & Tooling (2012–2018)
- **1.1**: 30%+ performance improvement; race detector
- **1.5**: Concurrent garbage collector (GC pauses drop from milliseconds to microseconds)
- **1.5**: Go compiler bootstrapped — written in Go (no more C)
- **1.7**: `context` package becomes standard

### Modules & Ecosystem (2018–2021)
- **1.11**: **Go modules** — official dependency management
- **1.13**: `errors.Is/As` — error wrapping becomes idiomatic
- **1.16**: `embed` package — embed files at compile time

### Modern Go (2022–present)
- **1.18**: **Generics** — type parameters with constraints
- **1.21**: `slog` — structured logging in stdlib; `min/max` builtins
- **1.22**: Range over integers (`for i := range 10`)
- **1.23**: Iterator package — lazy evaluation in stdlib

## Generics Journey

```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## Error Handling Philosophy

```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## Concurrency Evolution

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

## Ecosystem Growth

```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## Performance Evolution

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
