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

# C# — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | .NET | Tema Utama |
|---------|------|------|-----------|
| 1.0 | 2002 | 1.0 | Kelas, antarmuka, delegasi, acara |
| 1.2 | 2003 | 1.1 | `foreach`dengan`IDisposable`|
| 2.0 | 2005 | 2.0 | **Generik**, tipe nullable, metode anonim, iterator |
| 3.0 | 2007 | 3,5 | **LINQ**, ekspresi lambda, metode ekstensi,`var`, tipe anonim |
| 4.0 | 2010 | 4.0 | `dynamic`, argumen bernama/opsional,`Tuple<T>`|
| 5.0 | 2012 | 4.5 | **`async/await`**|
| 6.0 | 2015 | 4.6 |`?.`bersyarat nol, interpolasi string, anggota bertubuh ekspresi |
| 7.0 | 2017 | Inti 2.0 | Tupel, dekonstruksi, pencocokan pola,`out var`, pengembalian ref |
| 7.3 | 2018 | Inti 2.1 | `Span<T>`,`stackalloc`dalam ekspresi |
| 8.0 | 2019 | Inti 3.0 | **Jenis referensi nullable**, ekspresi peralihan, rentang`..`|
| 9.0 | 2020 | 5.0 | **`record`**, properti `init`, peningkatan pencocokan pola |
| 10.0 | 2021 | 6.0 | **`record struct`**, penggunaan global, ruang nama cakupan file, peningkatan lambda |
| 11.0 | 2022 | 7.0 | ** Jenis`required`**,`raw string literals`, `file`, bidang`ref`|
| 12.0 | 2023 | 8.0 | **Konstruktor utama**, ekspresi kumpulan`[]`, array inline |
| 13.0 | 2024 | 9.0 |  Koleksi `params`, kata kunci`Lock<T>`baru,`field`|
## Tonggak Penting
### Awal C# (2002–2007)
- **1.0 (2002)**: Kode terkelola di .NET; pengumpulan sampah; properti, acara, delegasi
- **2.0 (2005)**: Generik —`List<T>`,`Dictionary<K,V>`; tipe yang dapat dibatalkan`int?`; iterator`yield return`
- **3.0 (2007)**: LINQ — sintaksis kueri, ekspresi lambda, metode ekstensi,`var`, tipe anonim, pohon ekspresi
### Era Modern (2012–2017)
- **5.0 (2012)**:`async/await`— revolusi pemrograman asinkron
- **6.0 (2015)**:`?.`bersyarat nol, interpolasi string`$""`, inisialisasi properti otomatis
- **7.0 (2017)**: Tupel`(int, string)`, pencocokan pola,`out var`, fungsi lokal
### Evolusi Pesat (2019–sekarang)
- **8.0 (2019)**: Tipe referensi yang dapat dibatalkan — keamanan null pada waktu kompilasi
- **9.0 (2020)**: Tipe`record`— operator data yang tidak dapat diubah
- **10.0 (2021)**:`record struct`, penggunaan global, namespace cakupan file
- **11.0 (2022)**: kata kunci `required`, literal string mentah`"""..."""`
- **12.0 (2023)**: Konstruktor utama untuk semua kelas, ekspresi kumpulan`[1, 2, 3]`
- **13.0 (2024)**:`params`untuk semua jenis koleksi
## Evolusi Fitur
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

## Evolusi Platform .NET
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

## Filosofi Desain Bahasa
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Pertumbuhan Ekosistem
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
