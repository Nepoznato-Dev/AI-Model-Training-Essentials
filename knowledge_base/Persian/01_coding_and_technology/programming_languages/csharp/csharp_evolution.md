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
# سی شارپ - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | دات نت | تم کلید |
|---------|------|------|-----------|
| 1.0 | 2002 | 1.0 | کلاس ها، رابط ها، نمایندگان، رویدادها |
| 1.2 | 2003 | 1.1 | `foreach`با`IDisposable`|
| 2.0 | 2005 | 2.0 | **عمومی**، انواع nullable، روش های ناشناس، تکرار کننده |
| 3.0 | 2007 | 3.5 | **LINQ**، عبارات لامبدا، روش های گسترش، `var`، انواع ناشناس |
| 4.0 | 2010 | 4.0 |  `dynamic`، آرگومان های نامگذاری شده/اختیاری،`Tuple<T>`|
| 5.0 | 2012 | 4.5 | **`async/await`** |
| 6.0 | 2015 | 4.6 |`?.`شرطی تهی، درون یابی رشته ای، اعضای بیانی |
| 7.0 | 2017 | Core 2.0 | تاپل ها، ساختارشکنی، تطبیق الگو، `out var`، بازگشت رف |
| 7.3 | 2018 | هسته 2.1 | `Span<T>`,`stackalloc`در عبارات |
| 8.0 | 2019 | هسته 3.0 | **انواع مرجع نال پذیر**، عبارات سوئیچ، محدوده`..`|
| 9.0 | 2020 | 5.0 | **`record`**، ویژگی های `init`، بهبود تطبیق الگو |
| 10.0 | 2021 | 6.0 | **`record struct`**، کاربردهای جهانی، فضاهای نام با دامنه فایل، بهبود لامبدا |
| 11.0 | 2022 | 7.0 | ** انواع`required`**,`raw string literals`, `file`, فیلدهای`ref`|
| 12.0 | 2023 | 8.0 | **سازندگان اولیه**، مجموعه عبارات `[]`، آرایه های درون خطی |
| 13.0 | 2024 | 9.0 |  مجموعه های `params`، کلمه کلیدی`Lock<T>`جدید،`field`|
## نقاط عطف اصلی
### C# اولیه (2002–2007)
- **1.0 (2002)**: کد مدیریت شده در NET. جمع آوری زباله؛ خواص، رویدادها، نمایندگان
- **2.0 (2005)**: Generics — `List<T>`، `Dictionary<K,V>`؛ انواع nullable`int?`; تکرار کننده`yield return`
- **3.0 (2007)**: LINQ - نحو پرس و جو، عبارات لامبدا، روش های توسعه، `var`، انواع ناشناس، درخت های عبارت
### عصر مدرن (2012–2017)
- **5.0 (2012)**:`async/await`- انقلاب برنامه نویسی ناهمزمان
- **6.0 (2015)**:`?.`شرطی تهی، درون یابی رشته ای `$""`، اولیه سازهای ویژگی خودکار
- **7.0 (2017)**: تاپلی `(int, string)`، تطبیق الگو، `out var`، توابع محلی
### تکامل سریع (2019–اکنون)
- **8.0 (2019)**: انواع مرجع تهی - ایمنی تهی زمان کامپایل
- **9.0 (2020)**: انواع`record`- حامل های داده غیرقابل تغییر
- **10.0 (2021)**: `record struct`، کاربردهای جهانی، فضاهای نام با دامنه فایل
- **11.0 (2022)**: کلمه کلیدی `required`، کلمات رشته ای خام`"""..."""`
- **12.0 (2023)**: سازنده های اولیه برای همه کلاس ها، عبارات مجموعه`[1, 2, 3]`
- **13.0 (2024)**:`params`برای هر نوع مجموعه
## تکامل ویژگی
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

## تکامل پلتفرم دات نت
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

## فلسفه طراحی زبان
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## رشد اکوسیستم
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
