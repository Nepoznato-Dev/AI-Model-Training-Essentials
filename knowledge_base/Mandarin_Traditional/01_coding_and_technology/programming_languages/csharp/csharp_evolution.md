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

# C# — 版本歷史與演變
## 時間軸
|版本 |年份| .NET |關鍵主題 |
|--------|------|------|------------|
| 1.0 | 2002 | 1.0 |類別、介面、委託、事件 |
| 1.2 | 1.2 2003 | 1.1|`foreach`與`IDisposable`|
| 2.0 | 2005 | 2.0 | **泛型**、可空型別、匿名方法、迭代器 |
| 3.0 | 2007 | 3.5 | 3.5 **LINQ**、lambda 表達式、擴充方法、`var` 、匿名型別 |
| 4.0 | 2010 | 4.0 |`dynamic`，命名/可選參數，`Tuple<T>` |
| 5.0 | 2012 | 4.5 | 4.5 **`async/await`** |
| 6.0 | 2015 | 2015 4.6 |空條件`?.`、字串插值、表達式主體成員 |
| 7.0 | 2017 | 2017核心2.0 |元組、解構、模式比對、`out var`、 ref 回傳 |
| 7.3 | 7.3 2018 |核心2.1 | 表達式中的`Span<T>`、`stackalloc`|
| 8.0 | 2019 | 2019核心3.0 | **可空引用型別**、開關表達式、範圍`..`|
| 9.0 | 2020 | 5.0 | **`record`**、`init` 屬性、模式匹配改進 |
| 10.0 | 2021 | 6.0 | **`record struct`**、全域使用、檔案範圍的命名空間、lambda 改進 |
| 11.0 | 11.0 2022 | 2022 7.0 | **`required`**、`raw string literals`、`file` 類型、`ref` 欄位 |
| 12.0 | 2023 | 8.0 | **主建構子**、集合表達式`[]`、內聯陣列 |
| 13.0 | 2024 | 2024 9.0 |`params`系列，新`Lock<T>`、`field`關鍵字 |
## 主要里程碑
### 早期 C# (2002–2007)
- **1.0 (2002)**：.NET 上的託管程式碼；垃圾收集；屬性、事件、代表
- **2.0 (2005)**：泛型 —`List<T>`、`Dictionary<K,V>`；可空型別`int?`；迭代器 `yield return`
- **3.0 (2007)**：LINQ — 查詢語法、lambda 運算式、擴充方法、`var`、匿名型別、表達式樹
### 現代時代（2012–2017）
- **5.0 (2012)**：`async/await` — 非同步程式設計革命
- **6.0 (2015)**：空條件`?.`、字串插值`$""`、自動屬性初始值設定項
- **7.0 (2017)**：元組`(int, string)`、模式匹配、`out var`、局部函數
### 快速演進（2019 年至今）
- **8.0 (2019)**：可為 Null 的引用型 — 編譯時 null 安全
- **9.0 (2020)**：`record` 型態 — 非可變資料載體
- **10.0 (2021)**：`record struct`、全域使用、檔案範圍的命名空間
- **11.0 (2022)**：`required` 關鍵字，原始字串文字 `"""..."""`
- **12.0 (2023)**：所有類別的主建構子、集合表達式 `[1, 2, 3]`
- **13.0 (2024)**：`params` 適用於任何集合類型
## 功能演變
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

## .NET 平台演變
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

## 語言設計理念
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## 生態系成長
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
