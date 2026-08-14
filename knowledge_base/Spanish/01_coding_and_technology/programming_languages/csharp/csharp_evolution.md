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

# C# — Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | .NET | Tema clave |
|---------|------|------|-----------|
| 1.0 | 2002 | 1.0 | Clases, interfaces, delegados, eventos |
| 1.2 | 2003 | 1.1 | `foreach`con`IDisposable`|
| 2.0 | 2005 | 2.0 | **Genéricos**, tipos que aceptan valores NULL, métodos anónimos, iteradores |
| 3.0 | 2007 | 3.5 | **LINQ**, expresiones lambda, métodos de extensión, `var`, tipos anónimos |
| 4.0 | 2010 | 4.0 | `dynamic`, argumentos con nombre/opcionales,`Tuple<T>`|
| 5.0 | 2012 | 4.5 | **`async/await`** |
| 6.0 | 2015 | 4.6 |`?.`condicional nulo, interpolación de cadenas, miembros con cuerpo de expresión |
| 7.0 | 2017 | Núcleo 2.0 | Tuplas, deconstrucción, coincidencia de patrones, `out var`, retornos de referencia |
| 7.3 | 2018 | Núcleo 2.1 |  `Span<T>`,`stackalloc`en expresiones |
| 8.0 | 2019 | Núcleo 3.0 | **Tipos de referencia que admiten valores NULL**, expresiones de cambio, rangos`..`|
| 9.0 | 2020 | 5.0 | **`record`**, propiedades `init`, mejoras en la coincidencia de patrones |
| 10.0 | 2021 | 6.0 | **`record struct`**, usos globales, espacios de nombres con ámbito de archivo, mejoras lambda |
| 11.0 | 2022 | 7.0 | **`required`**, `raw string literals`, tipos `file`, campos`ref`|
| 12.0 | 2023 | 8.0 | **Constructores primarios**, expresiones de colección `[]`, matrices en línea |
| 13.0 | 2024 | 9.0 |  Colecciones `params`, nueva palabra clave `Lock<T>`,`field`|
## Hitos importantes
### Principios de C# (2002–2007)
- **1.0 (2002)**: Código administrado en .NET; recolección de basura; propiedades, eventos, delegados
- **2.0 (2005)**: Genéricos: `List<T>`, `Dictionary<K,V>`; tipos que aceptan valores NULL `int?`; iteradores`yield return`
- **3.0 (2007)**: LINQ: sintaxis de consulta, expresiones lambda, métodos de extensión, `var`, tipos anónimos, árboles de expresión
### La era moderna (2012-2017)
- **5.0 (2012)**: `async/await`: revolución de la programación asincrónica
- **6.0 (2015)**:`?.`con condición nula, interpolación de cadenas `$""`, inicializadores de propiedad automática
- **7.0 (2017)**: Tuplas `(int, string)`, coincidencia de patrones, `out var`, funciones locales
### La rápida evolución (2019-presente)
- **8.0 (2019)**: tipos de referencia que admiten valores NULL: seguridad nula en tiempo de compilación
- **9.0 (2020)**: tipos `record`: soportes de datos inmutables
- **10.0 (2021)**: `record struct`, usos globales, espacios de nombres con ámbito de archivo
- **11.0 (2022)**: palabra clave `required`, literales de cadena sin formato`"""..."""`
- **12.0 (2023)**: constructores primarios para todas las clases, expresiones de colección`[1, 2, 3]`
- **13.0 (2024)**:`params`para cualquier tipo de colección
## Evolución de funciones
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

## Evolución de la plataforma .NET
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

## Filosofía del diseño del lenguaje
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Crecimiento del ecosistema
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
