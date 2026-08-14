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

# C# — 版本历史和演变
## 时间轴
|版本 |年份| .NET |关键主题 |
|--------|------|------|------------|
| 1.0 | 2002 | 1.0 |类、接口、委托、事件 |
| 1.2 | 1.2 2003 | 1.1| `foreach`与`IDisposable`|
| 2.0 | 2005 | 2.0 | **泛型**、可空类型、匿名方法、迭代器 |
| 3.0 | 2007 | 3.5 | 3.5 **LINQ**、lambda 表达式、扩展方法、`var` 、匿名类型 |
| 4.0 | 2010 | 4.0 | `dynamic`，命名/可选参数，`Tuple<T>` |
| 5.0 | 2012 | 4.5 | 4.5 **`async/await`** |
| 6.0 | 2015 | 2015 4.6 |空条件`?.`、字符串插值、表达式主体成员 |
| 7.0 | 2017 | 2017核心2.0 |元组、解构、模式匹配、`out var`、 ref 返回 |
| 7.3 | 7.3 2018 |核心2.1 |  表达式中的`Span<T>`、`stackalloc`|
| 8.0 | 2019 | 2019核心3.0 | **可空引用类型**、开关表达式、范围`..`|
| 9.0 | 2020 | 5.0 | **`record`**、`init` 属性、模式匹配改进 |
| 10.0 | 2021 | 6.0 | **`record struct`**、全局使用、文件范围的命名空间、lambda 改进 |
| 11.0 | 11.0 2022 | 2022 7.0 | **`required`**、`raw string literals`、`file` 类型、`ref` 字段 |
| 12.0 | 2023 | 8.0 | **主构造函数**、集合表达式`[]`、内联数组 |
| 13.0 | 2024 | 2024 9.0 | `params`系列，新`Lock<T>`、`field`关键字 |
## 主要里程碑
### 早期 C# (2002–2007)
- **1.0 (2002)**：.NET 上的托管代码；垃圾收集；属性、事件、代表
- **2.0 (2005)**：泛型 —`List<T>`、`Dictionary<K,V>`；可空类型`int?`；迭代器`yield return`
- **3.0 (2007)**：LINQ — 查询语法、lambda 表达式、扩展方法、`var`、匿名类型、表达式树
### 现代时代（2012–2017）
- **5.0 (2012)**：`async/await` — 异步编程革命
- **6.0 (2015)**：空条件`?.`、字符串插值`$""`、自动属性初始值设定项
- **7.0 (2017)**：元组`(int, string)`、模式匹配、`out var`、局部函数
### 快速演变（2019 年至今）
- **8.0 (2019)**：可为 Null 的引用类型 — 编译时 null 安全
- **9.0 (2020)**：`record` 类型 — 不可变数据载体
- **10.0 (2021)**：`record struct`、全局使用、文件范围的命名空间
- **11.0 (2022)**：`required` 关键字，原始字符串文字`"""..."""`
- **12.0 (2023)**：所有类的主构造函数、集合表达式`[1, 2, 3]`
- **13.0 (2024)**：`params` 适用于任何集合类型
## 功能演变
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

## .NET 平台演变
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

## 语言设计理念
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## 生态系统增长
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
