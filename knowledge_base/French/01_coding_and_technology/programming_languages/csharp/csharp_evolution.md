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

# C# — Historique et évolution des versions
## Chronologie
| Version | Année | .NET | Thème clé |
|---------|------|------|---------------|
| 1.0 | 2002 | 1.0 | Cours, interfaces, délégués, événements |
| 1.2 | 2003 | 1.1 | `foreach`avec`IDisposable`|
| 2.0 | 2005 | 2.0 | **Génériques**, types nullables, méthodes anonymes, itérateurs |
| 3.0 | 2007 | 3.5 | **LINQ**, expressions lambda, méthodes d'extension,`var`, types anonymes |
| 4.0 | 2010 | 4.0 | `dynamic`, arguments nommés/facultatifs,`Tuple<T>`|
| 5.0 | 2012 | 4.5 | **`async/await`** |
| 6.0 | 2015 | 4.6 | Null-conditionnel`?.`, interpolation de chaîne, membres avec corps d'expression |
| 7.0 | 2017 | Noyau 2.0 | Tuples, déconstruction, correspondance de modèles,`out var`, retours de référence |
| 7.3 | 2018 | Noyau 2.1 | `Span<T>`,`stackalloc`dans les expressions |
| 8.0 | 2019 | Noyau 3.0 | **Types de référence nullables**, expressions de commutation, plages`..`|
| 9.0 | 2020 | 5.0 | **`record`**, propriétés `init`, améliorations de la correspondance de modèles |
| 10,0 | 2021 | 6.0 | **`record struct`**, utilisations globales, espaces de noms limités aux fichiers, améliorations lambda |
| 11.0 | 2022 | 7.0 | **`required`**,`raw string literals`, types `file`, champs`ref`|
| 12.0 | 2023 | 8.0 | **Constructeurs principaux**, expressions de collection`[]`, tableaux en ligne |
| 13.0 | 2024 | 9.0 |  Collections `params`, nouveau`Lock<T>`, mot-clé`field`|
## Étapes majeures
### Début C# (2002-2007)
- **1.0 (2002)** : Code managé sur .NET ; collecte des ordures; propriétés, événements, délégués
- **2.0 (2005)** : Génériques —`List<T>`,`Dictionary<K,V>`; types nullables`int?`; itérateurs`yield return`
- **3.0 (2007)** : LINQ — syntaxe de requête, expressions lambda, méthodes d'extension,`var`, types anonymes, arbres d'expression
### L'ère moderne (2012-2017)
- **5.0 (2012)** :`async/await`— révolution de la programmation asynchrone
- **6.0 (2015)** :`?.`conditionnel nul, interpolation de chaîne `$""`, initialiseurs de propriétés automatiques
- **7.0 (2017)** : Tuples`(int, string)`, correspondance de modèles,`out var`, fonctions locales
### L'évolution rapide (2019-présent)
- **8.0 (2019)** : types de référence nullables — sécurité nulle au moment de la compilation
- **9.0 (2020)** : types`record`— supports de données immuables
- **10.0 (2021)** : `record struct`, utilisations globales, espaces de noms à l'échelle des fichiers
- **11.0 (2022)** : mot-clé `required`, littéraux de chaîne brute`"""..."""`
- **12.0 (2023)** : Constructeurs principaux pour toutes les classes, expressions de collection`[1, 2, 3]`
- **13.0 (2024)** :`params`pour tout type de collection
## Évolution des fonctionnalités
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

## Évolution de la plateforme .NET
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

## Philosophie de conception du langage
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Croissance de l'écosystème
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
