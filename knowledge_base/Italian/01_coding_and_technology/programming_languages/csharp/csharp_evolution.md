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

# C#: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | .NET | Tema chiave |
|---------|------|------|-----------|
| 1.0 | 2002| 1.0 | Classi, interfacce, delegati, eventi |
| 1.2 | 2003| 1.1 | `foreach`con`IDisposable`|
| 2.0 | 2005| 2.0 | **Generici**, tipi nullable, metodi anonimi, iteratori |
| 3.0 | 2007| 3,5 | **LINQ**, espressioni lambda, metodi di estensione,`var`, tipi anonimi |
| 4.0 | 2010| 4.0 | `dynamic`, argomenti denominati/facoltativi,`Tuple<T>`|
| 5.0 | 2012| 4.5| **`async/await`** |
| 6.0 | 2015| 4.6|`?.`condizionale nullo, interpolazione di stringhe, membri con corpo di espressione |
| 7.0| 2017 | Nucleo 2.0 | Tuple, decostruzione, corrispondenza di modelli,`out var`, ref return |
| 7.3| 2018 | Nucleo 2.1 | `Span<T>`,`stackalloc`nelle espressioni |
| 8.0 | 2019 | Nucleo 3.0 | **Tipi di riferimento nullable**, espressioni di commutazione, intervalli`..`|
| 9.0 | 2020 | 5.0 | **`record`**, proprietà `init`, miglioramenti alla corrispondenza dei modelli |
| 10.0 | 2021 | 6.0 | **`record struct`**, utilizzi globali, spazi dei nomi con ambito file, miglioramenti lambda |
| 11.0 | 2022 | 7.0| **`required`**,`raw string literals`, tipi `file`, campi`ref`|
| 12.0| 2023 | 8.0 | **Costruttori primari**, espressioni di raccolta`[]`, array inline |
| 13.0| 2024 | 9.0 |  Collezioni `params`, nuova parola chiave`Lock<T>`,`field`|
## Traguardi importanti
### Inizio do# (2002-2007)
- **1.0 (2002)**: codice gestito su .NET; raccolta dei rifiuti; proprietà, eventi, delegati
- **2.0 (2005)**: Generici — `List<T>`, `Dictionary<K,V>`; tipi nullable`int?`; iteratori`yield return`
- **3.0 (2007)**: LINQ: sintassi delle query, espressioni lambda, metodi di estensione, `var`, tipi anonimi, alberi delle espressioni
### L'era moderna (2012–2017)
- **5.0 (2012)**:`async/await`— rivoluzione della programmazione asincrona
- **6.0 (2015)**:`?.`condizionale Null, interpolazione di stringhe `$""`, inizializzatori di proprietà automatica
- **7.0 (2017)**: Tuple `(int, string)`, corrispondenza di modelli, `out var`, funzioni locali
### La rapida evoluzione (2019-oggi)
- **8.0 (2019)**: tipi di riferimento nullable: sicurezza null in fase di compilazione
- **9.0 (2020)**: tipi`record`- supporti dati immutabili
- **10.0 (2021)**: `record struct`, utilizzi globali, spazi dei nomi con ambito file
- **11.0 (2022)**: parola chiave `required`, valori letterali stringa grezzi`"""..."""`
- **12.0 (2023)**: costruttori primari per tutte le classi, espressioni di raccolta`[1, 2, 3]`
- **13.0 (2024)**:`params`per qualsiasi tipo di raccolta
## Evoluzione delle funzionalità
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

## Evoluzione della piattaforma .NET
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

## Filosofia del design del linguaggio
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Crescita dell'ecosistema
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
