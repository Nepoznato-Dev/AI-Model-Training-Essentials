<!--
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

-->
# C# - Historia ya Toleo & Mageuzi
## Rekodi ya matukio
| Toleo | Mwaka | .NET | Mandhari Muhimu |
|---------|------|------|-----------|
| 1.0 | 2002 | 1.0 | Madarasa, violesura, wajumbe, matukio |
| 1.2 | 2003 | 1.1 | `foreach`pamoja na`IDisposable`|
| 2.0 | 2005 | 2.0 | **Jeneriki**, aina zisizoweza kubatilishwa, mbinu zisizojulikana, viboreshaji |
| 3.0 | 2007 | 3.5 | **LINQ**, misemo ya lambda, mbinu za upanuzi,`var`, aina zisizojulikana |
| 4.0 | 2010 | 4.0 | `dynamic`, hoja zenye majina/sio lazima,`Tuple<T>`|
| 5.0 | 2012 | 4.5 | **`async/await`** |
| 6.0 | 2015 | 4.6 | Null-conditional`?.`, tafsiri ya kamba, wanachama walio na hisia-mwili |
| 7.0 | 2017 | Msingi 2.0 | Tuples, deconstruction, muundo vinavyolingana,`out var`, rejeleo anarudi |
| 7.3 | 2018 | Msingi 2.1 | `Span<T>`,`stackalloc`katika misemo |
| 8.0 | 2019 | Msingi 3.0 | **Aina za marejeleo zinazoweza kubatilishwa**, badilisha vielezi, safu`..`|
| 9.0 | 2020 | 5.0 | **`record`**,`init`mali, uboreshaji unaolingana na muundo |
| 10.0 | 2021 | 6.0 | **`record struct`**, matumizi ya kimataifa, nafasi za majina zilizo na faili, maboresho ya lambda |
| 11.0 | 2022 | 7.0 | **`required`**,`raw string literals`,`file`aina,`ref`mashamba |
| 12.0 | 2023 | 8.0 | **Wajenzi wa msingi**, maneno ya mkusanyiko`[]`, safu za ndani |
| 13.0 | 2024 | 9.0 |  Mikusanyiko ya `params`, neno kuu la`Lock<T>`,`field`|
## Mafanikio Makuu
### C# ya Mapema (2002–2007)
- **1.0 (2002)**: Msimbo unaosimamiwa kwenye .NET; ukusanyaji wa takataka; mali, matukio, wajumbe
- **2.0 (2005)**: Jenerali —`List<T>`,`Dictionary<K,V>`; aina zisizoweza kubatilishwa`int?`; iterators`yield return`
- **3.0 (2007)**: LINQ — sintaksia ya hoja, misemo ya lambda, mbinu za upanuzi,`var`, aina zisizojulikana, miti ya kujieleza
### Enzi ya Kisasa (2012–2017)
- **5.0 (2012)**:`async/await`- mapinduzi ya programu ya asynchronous
- **6.0 (2015)**: Null-conditional`?.`, tafsiri ya kamba`$""`, vianzilishi vya mali kiotomatiki
- **7.0 (2017)**: Tuples`(int, string)`, muundo unaolingana,`out var`, utendakazi wa ndani
### Mageuzi ya Haraka (2019–sasa)
- **8.0 (2019)**: Aina za marejeleo zinazoweza kubatilishwa — kukusanya usalama batili wa muda
- **9.0 (2020)**: aina za`record`— vibeba data visivyoweza kubadilika
- **10.0 (2021)**:`record struct`, matumizi ya kimataifa, nafasi za majina zilizo na faili
- **11.0 (2022)**:`required`neno kuu, kamba mbichi halisi`"""..."""`
- **12.0 (2023)**: Wajenzi wa msingi kwa madarasa yote, maneno ya mkusanyiko`[1, 2, 3]`
- **13.0 (2024)**:`params`kwa aina yoyote ya mkusanyiko
## Mageuzi ya Kipengele
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

## Falsafa ya Usanifu wa Lugha
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Ukuaji wa Mfumo ikolojia
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
