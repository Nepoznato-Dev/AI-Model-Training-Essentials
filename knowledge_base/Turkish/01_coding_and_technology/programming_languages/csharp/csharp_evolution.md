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
# C# — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | .NET | Anahtar Tema |
|-----------|------|------|-----------|
| 1.0 | 2002 | 1.0 | Sınıflar, arayüzler, delegeler, etkinlikler |
| 1.2 | 2003 | 1.1 | `foreach`ile`IDisposable`|
| 2.0 | 2005 | 2.0 | **Geneller**, null olabilen türler, anonim yöntemler, yineleyiciler |
| 3.0 | 2007 | 3.5 | **LINQ**, lambda ifadeleri, uzantı yöntemleri, `var`, anonim türler |
| 4.0 | 2010 | 4.0 | `dynamic`, adlandırılmış/isteğe bağlı bağımsız değişkenler,`Tuple<T>`|
| 5.0 | 2012 | 4.5 | **`async/await`** |
| 6.0 | 2015 | 4.6 | Boş koşullu`?.`, dize enterpolasyonu, ifade gövdeli üyeler |
| 7.0 | 2017 | Çekirdek 2.0 | Demetler, yapısöküm, desen eşleştirme, `out var`, ref dönüşleri |
| 7.3 | 2018 | Çekirdek 2.1 |  İfadelerde `Span<T>`,`stackalloc`|
| 8.0 | 2019 | Çekirdek 3.0 | **Null yapılabilir başvuru türleri**, anahtar ifadeleri, aralıklar`..`|
| 9.0 | 2020 | 5.0 | **`record`**,`init`özellikleri, desen eşleştirme iyileştirmeleri |
| 10.0 | 2021 | 6.0 | **`record struct`**, genel kullanımlar, dosya kapsamlı ad alanları, lambda iyileştirmeleri |
| 11.0 | 2022 | 7.0 | **`required`**,`raw string literals`,`file`türleri,`ref`alanları |
| 12.0 | 2023 | 8.0 | **Birincil oluşturucular**, koleksiyon ifadeleri `[]`, satır içi diziler |
| 13.0 | 2024 | 9.0 | `params`koleksiyonları, yeni `Lock<T>`,`field`anahtar kelime |
## Önemli Kilometre Taşları
### Erken C# (2002–2007)
- **1.0 (2002)**: .NET'te yönetilen kod; çöp toplama; özellikler, etkinlikler, delegeler
- **2.0 (2005)**: Jenerikler —`List<T>`,`Dictionary<K,V>`; null olabilen türler`int?`; yineleyiciler`yield return`
- **3.0 (2007)**: LINQ — sorgu sözdizimi, lambda ifadeleri, uzantı yöntemleri, `var`, anonim türler, ifade ağaçları
### Modern Çağ (2012–2017)
- **5.0 (2012)**:`async/await`— eşzamansız programlama devrimi
- **6.0 (2015)**: Boş koşullu `?.`, dize enterpolasyonu `$""`, otomatik özellik başlatıcıları
- **7.0 (2017)**: Tuples `(int, string)`, desen eşleştirme, `out var`, yerel işlevler
### Hızlı Evrim (2019 – günümüz)
- **8.0 (2019)**: Null yapılabilir referans türleri — derleme zamanı null güvenliği
- **9.0 (2020)**:`record`türleri — değişmez veri taşıyıcıları
- **10.0 (2021)**:`record struct`, genel kullanımlar, dosya kapsamlı ad alanları
- **11.0 (2022)**:`required`anahtar kelime, ham dize değişmez değerleri`"""..."""`
- **12.0 (2023)**: Tüm sınıflar için birincil oluşturucular, koleksiyon ifadeleri`[1, 2, 3]`
- **13.0 (2024)**: Tüm koleksiyon türleri için `params`
## Özellik Gelişimi
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

## .NET Platformunun Gelişimi
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

## Dil Tasarım Felsefesi
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Ekosistem Büyümesi
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
