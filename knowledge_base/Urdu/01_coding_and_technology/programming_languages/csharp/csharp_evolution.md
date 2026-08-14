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
# C# - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | .NET | کلیدی تھیم |
|---------|------|------|------------|
| 1.0 | 2002 | 1.0 | کلاسز، انٹرفیس، مندوبین، واقعات |
| 1.2 | 2003 | 1.1 | `foreach``IDisposable` کے ساتھ |
| 2.0 | 2005 | 2.0 | **Generics**، کالعدم اقسام، گمنام طریقے، تکرار کرنے والے |
| 3.0 | 2007 | 3.5 | **LINQ**، لیمبڈا ایکسپریشنز، ایکسٹینشن کے طریقے،`var`, گمنام اقسام |
| 4.0 | 2010 | 4.0 |  `dynamic`، نامزد/اختیاری دلائل،`Tuple<T>`|
| 5.0 | 2012 | 4.5 | **`async/await`** |
| 6.0 | 2015 | 4.6 | غیر مشروط`?.`, سٹرنگ انٹرپولیشن، اظہار جسم والے ارکان |
| 7.0 | 2017 | کور 2.0 | ٹیپلز، ڈی کنسٹرکشن، پیٹرن میچنگ،`out var`, ref ریٹرن |
| 7.3 | 2018 | کور 2.1 | `Span<T>`,`stackalloc`اظہار میں |
| 8.0 | 2019 | کور 3.0 | **منسوخ حوالہ کی اقسام**، ایکسپریشنز کو تبدیل کریں، رینجز`..`|
| 9.0 | 2020 | 5.0 | **`record`**،`init`کی خصوصیات، پیٹرن کی مماثلت میں بہتری |
| 10.0 | 2021 | 6.0 | **`record struct`**، عالمی استعمال، فائل کے دائرہ کار والے نام کی جگہیں، لیمبڈا میں بہتری |
| 11.0 | 2022 | 7.0 | **`required`**, `raw string literals`,`file`اقسام,`ref`فیلڈز |
| 12.0 | 2023 | 8.0 | **بنیادی تعمیر کنندگان**، مجموعہ اظہار`[]`, ان لائن صفوں |
| 13.0 | 2024 | 9.0 | `params`مجموعہ، نیا`Lock<T>`,`field`کلیدی لفظ |
## اہم سنگ میل
### ابتدائی C# (2002–2007)
- **1.0 (2002): .NET پر منظم کوڈ؛ کچرا جمع کرنا؛ خصوصیات، واقعات، مندوبین
- **2.0 (2005)**: جنرک —`List<T>`,`Dictionary<K,V>`; کالعدم اقسام`int?`; تکرار کرنے والے`yield return`
- **3.0 (2007)**: LINQ — استفسار کا نحو، لیمبڈا اظہار، توسیع کے طریقے، `var`، گمنام اقسام، اظہار کے درخت
### جدید دور (2012–2017)
- **5.0 (2012)**:`async/await`— غیر مطابقت پذیر پروگرامنگ انقلاب
- **6.0 (2015)**: غیر مشروط`?.`, سٹرنگ انٹرپولیشن`$""`, آٹو پراپرٹی انیشیلائزرز
- **7.0 (2017): Tuples `(int, string)`، پیٹرن میچنگ، `out var`، مقامی فنکشنز
### تیز ارتقاء (2019–موجودہ)
- **8.0 (2019)**: کالعدم حوالہ جات کی قسمیں - مرتب وقت کی کالعدم حفاظت
- **9.0 (2020)**:`record`اقسام — ناقابل تبدیل ڈیٹا کیریئرز
- **10.0 (2021)**: `record struct`، عالمی استعمال، فائل کے دائرہ کار والے نام کی جگہیں
- **11.0 (2022)**:`required`کلیدی لفظ، خام سٹرنگ لٹریلز`"""..."""`
- **12.0 (2023)**: تمام کلاسز کے لیے پرائمری کنسٹرکٹرز، مجموعہ اظہار`[1, 2, 3]`
- **13.0 (2024)**: کسی بھی قسم کے مجموعہ کے لیے `params`
## فیچر ارتقاء
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

## .NET پلیٹ فارم ارتقاء
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

## زبان کا ڈیزائن فلسفہ
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## ماحولیاتی نظام کی نمو
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
