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

# C# — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | .NET | মূল থিম |
|---------|------|------|------------|
| 1.0 | 2002 | 1.0 | ক্লাস, ইন্টারফেস, প্রতিনিধি, ইভেন্ট |
| 1.2 | 2003 | 1.1 | `foreach`সঙ্গে`IDisposable`|
| 2.0 | 2005 | 2.0 | **জেনারিক**, বাতিলযোগ্য প্রকার, বেনামী পদ্ধতি, পুনরাবৃত্তিকারী |
| 3.0 | 2007 | 3.5 | **LINQ**, ল্যাম্বডা এক্সপ্রেশন, এক্সটেনশন পদ্ধতি,`var`, বেনামী প্রকার |
| 4.0 | 2010 | 4.0 | `dynamic`, নাম/ঐচ্ছিক আর্গুমেন্ট,`Tuple<T>`|
| 5.0 | 2012 | 4.5 | **`async/await`** |
| 6.0 | 2015 | 4.6 | নাল-শর্ত`?.`, স্ট্রিং ইন্টারপোলেশন, এক্সপ্রেশন-বডিড সদস্য |
| 7.0 | 2017 | কোর 2.0 | Tuples, deconstruction, প্যাটার্ন ম্যাচিং,`out var`, রেফ রিটার্ন |
| 7.3 | 2018 | কোর 2.1 |  এক্সপ্রেশনে`Span<T>`,`stackalloc`|
| 8.0 | 2019 | কোর 3.0 | **অন্যস্তযোগ্য রেফারেন্স প্রকার**, এক্সপ্রেশন পরিবর্তন করুন, রেঞ্জ`..`|
| 9.0 | 2020 | 5.0 | **`record`**,`init`বৈশিষ্ট্য, প্যাটার্ন ম্যাচিং উন্নতি |
| 10.0 | 2021 | 6.0 | **`record struct`**, বিশ্বব্যাপী ব্যবহার, ফাইল-স্কোপড নেমস্পেস, ল্যাম্বডা উন্নতি |
| 11.0 | 2022 | 7.0 | **`required`**,`raw string literals`,`file`প্রকার,`ref`ক্ষেত্র |
| 12.0 | 2023 | 8.0 | **প্রাথমিক কনস্ট্রাক্টর**, সংগ্রহ এক্সপ্রেশন`[]`, ইনলাইন অ্যারে |
| 13.0 | 2024 | 9.0 | `params`সংগ্রহ, নতুন`Lock<T>`,`field`কীওয়ার্ড |
## প্রধান মাইলফলক
### প্রারম্ভিক C# (2002-2007)
- **1.0 (2002): .NET-এ পরিচালিত কোড; আবর্জনা সংগ্রহ; বৈশিষ্ট্য, ঘটনা, প্রতিনিধি
- **2.0 (2005): জেনেরিক —`List<T>`,`Dictionary<K,V>`; বাতিলযোগ্য প্রকারগুলি`int?`; পুনরাবৃত্তিকারী`yield return`
- **3.0 (2007)**: LINQ — ক্যোয়ারী সিনট্যাক্স, ল্যাম্বডা এক্সপ্রেশন, এক্সটেনশন পদ্ধতি,`var`, বেনামী প্রকার, এক্সপ্রেশন ট্রি
### আধুনিক যুগ (2012-2017)
- **5.0 (2012):`async/await`— অ্যাসিঙ্ক্রোনাস প্রোগ্রামিং বিপ্লব
- **6.0 (2015): নাল-শর্তযুক্ত`?.`, স্ট্রিং ইন্টারপোলেশন`$""`, স্বয়ংক্রিয়-সম্পত্তি ইনিশিয়ালাইজার
- **7.0 (2017): Tuples`(int, string)`, প্যাটার্ন ম্যাচিং,`out var`, স্থানীয় ফাংশন
### দ্রুত বিবর্তন (2019-বর্তমান)
- **8.0 (2019)**: বাতিলযোগ্য রেফারেন্স প্রকার — কম্পাইল-টাইম নাল নিরাপত্তা
- **9.0 (2020)**:`record`প্রকারগুলি — অপরিবর্তনীয় ডেটা ক্যারিয়ার
- **10.0 (2021):`record struct`, বিশ্বব্যাপী ব্যবহার, ফাইল-স্কোপড নেমস্পেস
- **11.0 (2022):`required`কীওয়ার্ড, কাঁচা স্ট্রিং লিটারেল`"""..."""`
- **12.0 (2023): সকল শ্রেণীর জন্য প্রাথমিক নির্মাণকারী, সংগ্রহের অভিব্যক্তি`[1, 2, 3]`
- **13.0 (2024): যেকোন প্রকার সংগ্রহের জন্য `params`
## বৈশিষ্ট্য বিবর্তন
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

## .NET প্ল্যাটফর্ম বিবর্তন
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

## ভাষা নকশা দর্শন
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## ইকোসিস্টেম বৃদ্ধি
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
