---
# Metadata
title: "C# — Version History & Evolution"
description: "Comprehensive version history and evolution of C# from 1.0 to modern C#."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [csharp, dotnet, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C# — Version History & Evolution

## Timeline

| Version | Year | .NET | Key Theme |
|---------|------|------|-----------|
| 1.0     | 2002 | 1.0  | Classes, interfaces, delegates, events |
| 1.2     | 2003 | 1.1  | `foreach` with `IDisposable` |
| 2.0     | 2005 | 2.0  | **Generics**, nullable types, anonymous methods, iterators |
| 3.0     | 2007 | 3.5  | **LINQ**, lambda expressions, extension methods, `var`, anonymous types |
| 4.0     | 2010 | 4.0  | `dynamic`, named/optional arguments, `Tuple<T>` |
| 5.0     | 2012 | 4.5  | **`async/await`** |
| 6.0     | 2015 | 4.6  | Null-conditional `?.`, string interpolation, expression-bodied members |
| 7.0     | 2017 | Core 2.0 | Tuples, deconstruction, pattern matching, `out var`, ref returns |
| 7.3     | 2018 | Core 2.1 | `Span<T>`, `stackalloc` in expressions |
| 8.0     | 2019 | Core 3.0 | **Nullable reference types**, switch expressions, ranges `..` |
| 9.0     | 2020 | 5.0  | **`record`**, `init` properties, pattern matching improvements |
| 10.0    | 2021 | 6.0  | **`record struct`**, global usings, file-scoped namespaces, lambda improvements |
| 11.0    | 2022 | 7.0  | **`required`**, `raw string literals`, `file` types, `ref` fields |
| 12.0    | 2023 | 8.0  | **Primary constructors**, collection expressions `[]`, inline arrays |
| 13.0    | 2024 | 9.0  | `params` collections, new `Lock<T>`, `field` keyword |

## Major Milestones

### Early C# (2002–2007)
- **1.0 (2002)**: Managed code on .NET; garbage collection; properties, events, delegates
- **2.0 (2005)**: Generics — `List<T>`, `Dictionary<K,V>`; nullable types `int?`; iterators `yield return`
- **3.0 (2007)**: LINQ — query syntax, lambda expressions, extension methods, `var`, anonymous types, expression trees

### The Modern Era (2012–2017)
- **5.0 (2012)**: `async/await` — asynchronous programming revolution
- **6.0 (2015)**: Null-conditional `?.`, string interpolation `$""`, auto-property initializers
- **7.0 (2017)**: Tuples `(int, string)`, pattern matching, `out var`, local functions

### The Rapid Evolution (2019–present)
- **8.0 (2019)**: Nullable reference types — compile-time null safety
- **9.0 (2020)**: `record` types — immutable data carriers
- **10.0 (2021)**: `record struct`, global usings, file-scoped namespaces
- **11.0 (2022)**: `required` keyword, raw string literals `"""..."""`
- **12.0 (2023)**: Primary constructors for all classes, collection expressions `[1, 2, 3]`
- **13.0 (2024)**: `params` for any collection type

## Feature Evolution

```
Null Safety:
  2002: Reference types always nullable
  2005: Nullable value types (int?)
  2019: Nullable reference types (string?)
  2022: Required members

Pattern Matching:
  2017: Basic type/is patterns
  2019: Switch expressions, property patterns
  2020: Relational patterns, combinator patterns
  2021: List patterns, type patterns

Async:
  2012: async/await (Task-based)
  2017: async Main, async streams (IAsyncEnumerable)
  2020: Top-level statements
  2023: async disposables

Data Types:
  2002: Classes, structs, enums
  2005: Generics
  2020: record (class)
  2021: record struct
  2023: Primary constructors for all types
```

## .NET Platform Evolution

```
2002: .NET Framework 1.0 (Windows only)
2005: .NET Framework 2.0 (generics)
2012: .NET Framework 4.5 (async)
2016: .NET Core 1.0 (cross-platform!)
2019: .NET Core 3.0 (Windows desktop)
2020: .NET 5 (unified platform)
2021: .NET 6 (LTS, minimal APIs)
2022: .NET 7 (performance)
2023: .NET 8 (LTS, native AOT)
2024: .NET 9 (performance, hybridization)
2025: .NET 10 (LTS expected)
```

## Language Design Philosophy

```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Ecosystem Growth

```
2002: .NET Framework, Windows Forms, ASP.NET Web Forms
2005: LINQ, Entity Framework
2010: MVVM, WPF, Silverlight
2016: .NET Core — cross-platform
2018: Blazor — C# in the browser (WebAssembly)
2020: .NET 5 — unified platform
2023: .NET 8 — native AOT, minimal APIs
2025: C# — top 5 most used language; dominant in enterprise, games (Unity), cloud (Azure)
```
