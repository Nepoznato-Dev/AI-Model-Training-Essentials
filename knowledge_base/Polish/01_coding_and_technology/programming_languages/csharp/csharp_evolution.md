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

# C# — Historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | .NET | Kluczowy motyw |
|--------|------|------|----------|
| 1,0 | 2002 | 1,0 | Klasy, interfejsy, delegaci, zdarzenia |
| 1.2 | 2003 | 1.1 | `foreach`z`IDisposable`|
| 2,0 | 2005 | 2,0 | **Generyczne**, typy dopuszczające wartość null, metody anonimowe, iteratory |
| 3,0 | 2007 | 3,5 | **LINQ**, wyrażenia lambda, metody rozszerzające,`var`, typy anonimowe |
| 4,0 | 2010 | 4,0 | `dynamic`, nazwane/opcjonalne argumenty,`Tuple<T>`|
| 5,0 | 2012 | 4,5 | **`async/await`** |
| 6,0 | 2015 | 4,6 | Warunek zerowy`?.`, interpolacja ciągów znaków, elementy członkowskie zawierające wyrażenie |
| 7,0 | 2017 | Rdzeń 2.0 | Krotki, dekonstrukcja, dopasowywanie wzorców, `out var`, ref zwraca |
| 7.3 | 2018 | Rdzeń 2.1 | `Span<T>`,`stackalloc`w wyrażeniach |
| 8,0 | 2019 | Rdzeń 3.0 | **Typy referencyjne dopuszczające wartość null**, wyrażenia przełączające, zakresy`..`|
| 9,0 | 2020 | 5,0 | **`record`**, właściwości `init`, ulepszenia dopasowywania wzorców |
| 10,0 | 2021 | 6,0 | **`record struct`**, zastosowania globalne, przestrzenie nazw ograniczone do plików, ulepszenia lambda |
| 11,0 | 2022 | 7,0 | ** Typy`required`**,`raw string literals`, `file`, pola`ref`|
| 12,0 | 2023 | 8,0 | **Konstruktory podstawowe**, wyrażenia kolekcji`[]`, tablice wbudowane |
| 13,0 | 2024 | 9,0 |  kolekcje `params`, nowości`Lock<T>`,`field`słowo kluczowe |
## Główne kamienie milowe
### Wczesny C# (2002–2007)
- **1.0 (2002)**: Kod zarządzany w .NET; zbieranie śmieci; właściwości, zdarzenia, delegaci
- **2.0 (2005)**: Ogólne —`List<T>`,`Dictionary<K,V>`; typy dopuszczające wartość null`int?`; iteratory`yield return`
- **3.0 (2007)**: LINQ — składnia zapytań, wyrażenia lambda, metody rozszerzające,`var`, typy anonimowe, drzewa wyrażeń
### Era nowożytna (2012–2017)
- **5.0 (2012)**:`async/await`— rewolucja w programowaniu asynchronicznym
- **6.0 (2015)**: Warunek zerowy `?.`, interpolacja ciągów `$""`, inicjalizatory automatycznych właściwości
- **7.0 (2017)**: Krotki`(int, string)`, dopasowywanie wzorców,`out var`, funkcje lokalne
### Szybka ewolucja (od 2019 r.)
- **8.0 (2019)**: Typy referencyjne dopuszczające wartość null — bezpieczeństwo zerowe w czasie kompilacji
- **9.0 (2020)**: typy`record`— niezmienne nośniki danych
- **10.0 (2021)**: `record struct`, zastosowania globalne, przestrzenie nazw ograniczone do plików
- **11.0 (2022)**: słowo kluczowe `required`, surowe literały łańcuchowe`"""..."""`
- **12.0 (2023)**: Konstruktory podstawowe dla wszystkich klas, wyrażenia kolekcji`[1, 2, 3]`
- **13.0 (2024)**:`params`dla dowolnego typu kolekcji
## Ewolucja funkcji
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

## Ewolucja platformy .NET
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

## Filozofia projektowania języka
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Rozwój ekosystemu
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
