---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Rust — Version History & Evolution

## Timeline

| Version | Release Date | Key Theme |
|---------|-------------|-----------|
| 0.1     | Jan 2012    | First compiler (rustc), task-based concurrency |
| 0.5     | 2012        | Trait-based type system takes shape |
| 0.6     | 2012        | Removal of `@` managed boxes |
| 0.7     | 2013        | `@` removed, `~` for owned boxes |
| 0.8     | 2013        | Lifetime annotations, `&mut` |
| 0.9     | Jan 2014    | Final pre-1.0 cleanup |
| 0.10    | Feb 2014    | Last pre-1.0 release |
| 0.11    | Apr 2014    | `Box<T>` replaces `~T` |
| 0.12    | May 2014    | `io` module rewrite begins |
| 1.0     | May 15, 2015 | **Stable release** — "Rust 1.0" |
| 1.10    | Aug 2016    | `?` error propagation (as `try!` → `?`) |
| 1.15    | Feb 2017    | First Rust on stable with `impl Trait` prep |
| 1.18    | Jun 2017    | `pub(crate)`, incremental compilation |
| 1.20    | Oct 2017    | Associated constants |
| 1.26    | May 2018    | `impl Trait` in argument/return position |
| 1.28    | Sep 2018    | Global allocators |
| 1.31    | Dec 2018    | **Rust 2018 Edition** — modules, `dyn Trait` |
| 1.34    | Apr 2019    | Alternative registries |
| 1.39    | Nov 2019    | `async/await` on stable |
| 1.44    | Jul 2020    | Diagnostics improvements |
| 1.51    | Apr 2021    | `const` generics (MVP) |
| 1.56    | Oct 2021    | **Rust 2021 Edition** — closures, IntoIterator |
| 1.59    | Feb 2022    | Inline assembly |
| 1.62    | Jun 2022    | `#[default]` for enums |
| 1.65    | Dec 2022    | `let else` |
| 1.68    | Mar 2023    | `#[ffi_pure]`, profile-guided optimization |
| 1.70    | Jun 2023    | Isolated `crates.io` dependencies |
| 1.74    | Nov 2023    | Cargo offline mode |
| 1.76    | Feb 2024    | **Rust 2024 Edition** — `gen` blocks, `unsafe extern` |
| 1.79    | Jun 2024    | `LazyCell`, `LazyLock` |
| 1.82    | Oct 2024    | `unsafe` in `extern` blocks required |
| 1.85    | Feb 2025    | Rust 2024 edition stabilized |

## Major Milestones

### Pre-1.0 (2010–2015)
- **2010**: Graydon Hoare's side project at Mozilla gains traction
- **2012**: First public compiler; type system undergoes major redesign
- **2013**: Ownership model crystallizes; `@` boxes removed
- **2014**: Rust RFC process formalized; community grows
- **2015**: **1.0** — stability guarantee; "zero-cost abstractions"

### The Growth Years (2015–2019)
- **2015**: Cargo becomes the standard package manager
- **2018**: **Rust 2018 Edition** — module system overhaul, `dyn Trait`, `impl Trait`
- **2019**: `async/await` lands on stable — async ecosystem begins

### Maturity (2020–present)
- **2021**: **Rust 2021 Edition** — disambiguate fields in closures, `IntoIterator` for arrays
- **2024**: **Rust 2024 Edition** — `gen` blocks, `unsafe extern` requirements
- **2025**: Rust in Linux kernel, Android, Windows, AWS infrastructure

## Edition System

```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## Ownership Evolution

```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## Async Evolution

```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## Ecosystem Growth

```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## Key RFCs

| RFC  | Year | Feature |
|------|------|---------|
| 25   | 2013 | Pattern matching |
| 153  | 2014 | `Result` type |
| 217  | 2014 | `?` (try) operator |
| 460  | 2016 | `?` replaces `try!` |
| 1210 | 2015 | `impl Trait` |
| 1414 | 2016 | Rust 2018 edition |
| 2394 | 2018 | `async/await` |
| 2515 | 2018 | `const` generics |
| 3013 | 2020 | Checking conditional compilation |
| 3517 | 2023 | `gen` blocks |
