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

# C# — История версий и эволюция
## Временная шкала
| Версия | Год | .NET | Ключевая тема |
|---------|------|------|-----------|
| 1.0 | 2002 | 1.0 | Классы, интерфейсы, делегаты, события |
| 1,2 | 2003 | 1.1 | `foreach`с`IDisposable`|
| 2.0 | 2005 | 2.0 | **Обобщенные**, типы, допускающие значение NULL, анонимные методы, итераторы |
| 3.0 | 2007 | 3,5 | **LINQ**, лямбда-выражения, методы расширения, `var`, анонимные типы |
| 4.0 | 2010 | 4.0 | `dynamic`, именованные/необязательные аргументы,`Tuple<T>`|
| 5.0 | 2012 | 4,5 | **`async/await`** |
| 6.0 | 2015 | 4,6 | Условное значение NULL`?.`, строковая интерполяция, члены с телом выражения |
| 7.0 | 2017 | Ядро 2.0 | Кортежи, деконструкция, сопоставление с образцом, `out var`, возврат ref |
| 7.3 | 2018 | Ядро 2.1 | `Span<T>`,`stackalloc`в выражениях |
| 8.0 | 2019 | Ядро 3.0 | **Ссылочные типы, допускающие значение NULL**, выражения переключения, диапазоны`..`|
| 9.0 | 2020 | 5.0 | **`record`**, свойства `init`, улучшения сопоставления с образцом |
| 10,0 | 2021 | 6.0 | **`record struct`**, глобальное использование, пространства имен на уровне файла, улучшения лямбда |
| 11,0 | 2022 | 7.0 | ** Типы`required`**,`raw string literals`, `file`, поля`ref`|
| 12,0 | 2023 | 8.0 | **Основные конструкторы**, выражения коллекций `[]`, встроенные массивы |
| 13,0 | 2024 | 9.0 |  Коллекции `params`, новое ключевое слово `Lock<T>`,`field`|
## Основные вехи
### Ранний C# (2002–2007)
- **1.0 (2002 г.)**: Управляемый код на .NET; сбор мусора; свойства, события, делегаты
- **2.0 (2005 г.)**: Универсальные шаблоны —`List<T>`,`Dictionary<K,V>`; типы, допускающие значение NULL`int?`; итераторы`yield return`
- **3.0 (2007 г.)**: LINQ — синтаксис запросов, лямбда-выражения, методы расширения, `var`, анонимные типы, деревья выражений.
### Современная эпоха (2012–2017)
- **5.0 (2012 г.)**:`async/await`— революция в асинхронном программировании.
- **6.0 (2015 г.)**:`?.`с нулевым условием, строковая интерполяция `$""`, автоматические инициализаторы свойств.
- **7.0 (2017 г.)**: кортежи `(int, string)`, сопоставление с образцом, `out var`, локальные функции.
### Быстрая эволюция (2019 – настоящее время)
- **8.0 (2019 г.)**: ссылочные типы, допускающие значение NULL, — нулевая безопасность во время компиляции.
- **9.0 (2020 г.)**: типы`record`— неизменяемые носители данных.
- **10.0 (2021 г.)**:`record struct`, глобальное использование, пространства имен на уровне файла.
- **11.0 (2022 г.)**: ключевое слово `required`, необработанные строковые литералы `"""..."""`. 
- **12.0 (2023 г.)**: основные конструкторы для всех классов, выражения коллекций `[1, 2, 3]`. 
- **13.0 (2024 г.)**:`params`для любого типа коллекции.
## Эволюция функций
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

## Эволюция платформы .NET
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

## Философия языкового дизайна
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Рост экосистемы
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
