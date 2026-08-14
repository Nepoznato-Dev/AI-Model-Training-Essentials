---
# Metadata
title: "C# — Version History & Evolution"
description: "Comprehensive version history and evolution of C# from 1.0 to modern C#."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# C# – Versionsverlauf und Entwicklung
## Zeitleiste
| Version | Jahr | .NET | Schlüsselthema |
|---------|------|------|-----------|
| 1,0 | 2002 | 1,0 | Klassen, Schnittstellen, Delegaten, Ereignisse |
| 1.2 | 2003 | 1.1 | `foreach`mit`IDisposable`|
| 2,0 | 2005 | 2,0 | **Generika**, nullfähige Typen, anonyme Methoden, Iteratoren |
| 3,0 | 2007 | 3,5 | **LINQ**, Lambda-Ausdrücke, Erweiterungsmethoden, `var`, anonyme Typen |
| 4,0 | 2010 | 4,0 | `dynamic`, benannte/optionale Argumente,`Tuple<T>`|
| 5,0 | 2012 | 4,5 | **`async/await`** |
| 6,0 | 2015 | 4,6 | NULL-bedingtes`?.`, Zeichenfolgeninterpolation, Mitglieder mit Ausdruckskörper |
| 7,0 | 2017 | Kern 2.0 | Tupel, Dekonstruktion, Mustervergleich,`out var`, ref gibt | zurück
| 7,3 | 2018 | Kern 2.1 | `Span<T>`,`stackalloc`in Ausdrücken |
| 8,0 | 2019 | Kern 3.0 | **Nullable-Referenztypen**, Switch-Ausdrücke, Bereiche`..`|
| 9,0 | 2020 | 5,0 | **`record`**, `init`-Eigenschaften, Verbesserungen beim Mustervergleich |
| 10,0 | 2021 | 6,0 | **`record struct`**, globale Verwendungen, dateibezogene Namespaces, Lambda-Verbesserungen |
| 11,0 | 2022 | 7,0 | **`required`**,`raw string literals`, `file`-Typen, `ref`-Felder |
| 12,0 | 2023 | 8,0 | **Primäre Konstruktoren**, Sammlungsausdrücke`[]`, Inline-Arrays |
| 13,0 | 2024 | 9,0 |  `params`-Sammlungen, neue `Lock<T>`-, `field`-Schlüsselwörter |
## Wichtige Meilensteine
### Frühes C# (2002–2007)
- **1.0 (2002)**: Verwalteter Code auf .NET; Müllabfuhr; Eigenschaften, Ereignisse, Delegierte
- **2.0 (2005)**: Generics –`List<T>`,`Dictionary<K,V>`; nullfähige Typen`int?`; Iteratoren`yield return`
- **3.0 (2007)**: LINQ – Abfragesyntax, Lambda-Ausdrücke, Erweiterungsmethoden, `var`, anonyme Typen, Ausdrucksbäume
### Die Moderne (2012–2017)
- **5.0 (2012)**:`async/await`– Revolution der asynchronen Programmierung
- **6.0 (2015)**: NULL-Bedingung `?.`, String-Interpolation `$""`, automatische Eigenschaftsinitialisierer
- **7.0 (2017)**: Tupel `(int, string)`, Mustervergleich, `out var`, lokale Funktionen
### Die schnelle Entwicklung (2019–heute)
- **8.0 (2019)**: Nullable-Referenztypen – Nullsicherheit zur Kompilierungszeit
- **9.0 (2020)**: `record`-Typen – unveränderliche Datenträger
– **10.0 (2021)**: `record struct`, globale Verwendung, dateibezogene Namespaces
– **11.0 (2022)**: Schlüsselwort `required`, rohe String-Literale`"""..."""`
– **12.0 (2023)**: Primärkonstruktoren für alle Klassen, Sammlungsausdrücke`[1, 2, 3]`
- **13.0 (2024)**:`params`für jeden Sammlungstyp
## Feature-Entwicklung
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

## .NET-Plattformentwicklung
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

## Philosophie des Sprachdesigns
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Ökosystemwachstum
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
