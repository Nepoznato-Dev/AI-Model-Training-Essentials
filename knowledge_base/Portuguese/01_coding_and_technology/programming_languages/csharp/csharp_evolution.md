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
# C# — Histórico e evolução da versão
## Linha do tempo
| Versão | Ano | .NET | Tema principal |
|--------|------|------|-----------|
| 1,0 | 2002 | 1,0 | Classes, interfaces, delegados, eventos |
| 1.2 | 2003 | 1.1 | `foreach`com`IDisposable`|
| 2.0 | 2005 | 2.0 | **Genéricos**, tipos anuláveis, métodos anônimos, iteradores |
| 3.0 | 2007 | 3.5 | **LINQ**, expressões lambda, métodos de extensão,`var`, tipos anônimos |
| 4,0 | 2010 | 4,0 | `dynamic`, argumentos nomeados/opcionais,`Tuple<T>`|
| 5,0 | 2012 | 4,5 | **`async/await`** |
| 6,0 | 2015 | 4.6 |`?.`condicional nulo, interpolação de string, membros com corpo de expressão |
| 7,0 | 2017 | Núcleo 2.0 | Tuplas, desconstrução, correspondência de padrões,`out var`, retornos de referência |
| 7.3 | 2018 | Núcleo 2.1 | `Span<T>`,`stackalloc`em expressões |
| 8,0 | 2019 | Núcleo 3.0 | **Tipos de referência anuláveis**, expressões de alternância, intervalos`..`|
| 9,0 | 2020 | 5,0 | **`record`**, propriedades `init`, melhorias na correspondência de padrões |
| 10,0 | 2021 | 6,0 | **`record struct`**, usos globais, namespaces com escopo de arquivo, melhorias lambda |
| 11,0 | 2022 | 7,0 | **`required`**,`raw string literals`, tipos `file`, campos`ref`|
| 12,0 | 2023 | 8,0 | **Construtores primários**, expressões de coleção`[]`, matrizes embutidas |
| 13,0 | 2024 | 9,0 |  Coleções `params`, nova palavra-chave`Lock<T>`,`field`|
## Marcos importantes
### C# inicial (2002–2007)
- **1.0 (2002)**: Código gerenciado em .NET; coleta de lixo; propriedades, eventos, delegados
- **2.0 (2005)**: Genéricos —`List<T>`,`Dictionary<K,V>`; tipos anuláveis ​​`int?` ; iteradores`yield return`
- **3.0 (2007)**: LINQ — sintaxe de consulta, expressões lambda, métodos de extensão,`var`, tipos anônimos, árvores de expressão
### A Era Moderna (2012–2017)
- **5.0 (2012)**:`async/await`— revolução da programação assíncrona
- **6.0 (2015)**:`?.`condicional nulo, interpolação de string `$""`, inicializadores de propriedade automática
- **7.0 (2017)**: Tuplas`(int, string)`, correspondência de padrões,`out var`, funções locais
### A Evolução Rápida (2019-presente)
- **8.0 (2019)**: Tipos de referência anuláveis — segurança nula em tempo de compilação
- **9.0 (2020)**: tipos`record`— suportes de dados imutáveis
- **10.0 (2021)**:`record struct`, usos globais, namespaces com escopo de arquivo
- **11.0 (2022)**: palavra-chave `required`, literais de string brutos`"""..."""`
- **12.0 (2023)**: Construtores primários para todas as classes, expressões de coleção`[1, 2, 3]`
- **13.0 (2024)**:`params`para qualquer tipo de coleção
## Evolução de recursos
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

## Evolução da plataforma .NET
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

## Filosofia de Design de Linguagem
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Crescimento do Ecossistema
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
