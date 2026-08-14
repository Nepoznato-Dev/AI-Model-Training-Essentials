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
#C# — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | صافي | الموضوع الرئيسي |
|---------|------|-----|-----------|
| 1.0 | 2002 | 1.0 | فصول، واجهات، مندوبين، أحداث |
| 1.2 | 2003 | 1.1 | `foreach`مع`IDisposable`|
| 2.0 | 2005 | 2.0 | **الأنواع العامة**، الأنواع الخالية، الأساليب المجهولة، التكرارات |
| 3.0 | 2007 | 3.5 | **LINQ**، تعبيرات لامدا، طرق الامتداد، `var`، الأنواع المجهولة |
| 4.0 | 2010 | 4.0 |  `dynamic`، الوسائط المسماة/الاختيارية،`Tuple<T>`|
| 5.0 | 2012 | 4.5 | **`async/await`** |
| 6.0 | 2015 | 4.6 |`?.`خالية مشروطة، استيفاء سلسلة، أعضاء ذات أجسام تعبيرية |
| 7.0 | 2017 | كور 2.0 | الصفوف، التفكيك، مطابقة الأنماط، `out var`، إرجاع المرجع |
| 7.3 | 2018 | كور 2.1 | `Span<T>`,`stackalloc`في التعبيرات |
| 8.0 | 2019 | كور 3.0 | **أنواع المراجع الخالية**، تعبيرات التبديل، النطاقات`..`|
| 9.0 | 2020 | 5.0 | **`record`**، خصائص `init`، تحسينات مطابقة الأنماط |
| 10.0 | 2021 | 6.0 | **`record struct`**، الاستخدامات العالمية، مساحات الأسماء على نطاق الملف، تحسينات لامدا |
| 11.0 | 2022 | 7.0 | **`required`**، أنواع `raw string literals`، `file`، حقول`ref`|
| 12.0 | 2023 | 8.0 | **المنشئات الأولية**، تعبيرات المجموعة `[]`، المصفوفات المضمنة |
| 13.0 | 2024 | 9.0 |  مجموعات `params`،`Lock<T>`الجديدة، الكلمة الرئيسية`field`|
## المعالم الرئيسية
### أوائل لغة C# (2002-2007)
- **1.0 (2002)**: تعليمات برمجية مُدارة على .NET؛ جمع القمامة؛ خصائص، أحداث، مندوبين
- **2.0 (2005)**: الأدوية العامة —`List<T>`,`Dictionary<K,V>`; الأنواع الخالية`int?`؛ التكرارات`yield return`
- **3.0 (2007)**: LINQ — بناء جملة الاستعلام، وتعبيرات لامدا، وطرق الامتداد، `var`، والأنواع المجهولة، وأشجار التعبير
### العصر الحديث (2012-2017)
- **5.0 (2012)**:`async/await`— ثورة البرمجة غير المتزامنة
- **6.0 (2015)**:`?.`المشروط، واستيفاء السلسلة `$""`، ومهيئات الخصائص التلقائية
- **7.0 (2017)**: Tuples `(int, string)`، مطابقة الأنماط، `out var`، الوظائف المحلية
### التطور السريع (2019 إلى الوقت الحاضر)
- **8.0 (2019)**: أنواع المراجع الخالية - أمان فارغ في وقت الترجمة
- **9.0 (2020)**: أنواع`record`— ناقلات البيانات غير القابلة للتغيير
- **10.0 (2021)**: `record struct`، الاستخدامات العالمية، مساحات الأسماء ذات نطاق الملف
- **11.0 (2022)**: الكلمة الأساسية `required`، سلسلة حرفية أولية`"""..."""`
- **12.0 (2023)**: المُنشئون الأساسيون لجميع الفئات، وتعبيرات المجموعة`[1, 2, 3]`
- **13.0 (2024)**:`params`لأي نوع مجموعة
## تطور الميزة
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

## تطور منصة .NET
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

## فلسفة تصميم اللغة
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## نمو النظام البيئي
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
