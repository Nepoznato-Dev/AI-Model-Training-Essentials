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
# C# - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | .NET | ธีมหลัก |
|---------|--------|-----------|
| 1.0 | 2545 | 1.0 | คลาส, อินเทอร์เฟซ, ผู้รับมอบสิทธิ์, กิจกรรม |
| 1.2 | 2546 | 1.1 | `foreach`กับ`IDisposable`|
| 2.0 | 2548 | 2.0 | **ทั่วไป**, ประเภทที่เป็นโมฆะ, วิธีการที่ไม่ระบุชื่อ, ตัววนซ้ำ |
| 3.0 | 2550 | 3.5 | **LINQ**, นิพจน์แลมบ์ดา, วิธีการขยาย,`var`, ประเภทที่ไม่ระบุชื่อ |
| 4.0 | 2010 | 4.0 | `dynamic`อาร์กิวเมนต์ที่มีชื่อ/เป็นทางเลือก,`Tuple<T>`|
| 5.0 | 2555 | 4.5 | **`async/await`** |
| 6.0 | 2558 | 4.6 |`?.`แบบมีเงื่อนไข Null, การประมาณค่าสตริง, สมาชิกแบบ expression-bodied |
| 7.0 | 2017 | คอร์ 2.0 | สิ่งอันดับ, การรื้อโครงสร้าง, การจับคู่รูปแบบ,`out var`, การส่งคืนการอ้างอิง |
| 7.3 | 2018 | คอร์ 2.1 | `Span<T>`,`stackalloc`ในนิพจน์ |
| 8.0 | 2019 | คอร์ 3.0 | **ประเภทการอ้างอิงที่เป็น Nullable**, สลับนิพจน์, ช่วง`..`|
| 9.0 | 2020 | 5.0 | **`record`** คุณสมบัติ`init`การปรับปรุงการจับคู่รูปแบบ |
| 10.0 | 2021 | 6.0 | **`record struct`**, การใช้งานทั่วโลก, เนมสเปซที่กำหนดขอบเขตไฟล์, การปรับปรุงแลมบ์ดา |
| 11.0 | 2022 | 7.0 | **`required`**,`raw string literals`,`file`ประเภท,`ref`ฟิลด์ |
| 12.0 | 2023 | 8.0 | **ตัวสร้างหลัก** นิพจน์คอลเลกชัน`[]`อาร์เรย์อินไลน์ |
| 13.0 | 2024 | 9.0 |  คอลเลกชัน `params`,`Lock<T>`ใหม่ ,`field`คำหลัก |
## เหตุการณ์สำคัญที่สำคัญ
### ภาษา C# ยุคแรก (พ.ศ. 2545–2550)
- **1.0 (2002)**: โค้ดที่ได้รับการจัดการบน .NET; การเก็บขยะ คุณสมบัติ, กิจกรรม, ผู้ได้รับมอบหมาย
- **2.0 (2005)**: ข้อมูลทั่วไป —`List<T>`,`Dictionary<K,V>`; ประเภทที่เป็นโมฆะ`int?`; ตัววนซ้ำ`yield return`
- **3.0 (2007)**: LINQ — ไวยากรณ์คิวรี, นิพจน์แลมบ์ดา, วิธีการขยาย,`var`, ประเภทที่ไม่ระบุชื่อ, ต้นไม้นิพจน์
### ยุคสมัยใหม่ (2555–2560)
- **5.0 (2012)**:`async/await`— การปฏิวัติการเขียนโปรแกรมแบบอะซิงโครนัส
- **6.0 (2015)**:`?.`ที่ไม่มีเงื่อนไข , การแก้ไขสตริง`$""`, การกำหนดค่าเริ่มต้นคุณสมบัติอัตโนมัติ
- **7.0 (2017)**: Tuples`(int, string)`, การจับคู่รูปแบบ,`out var`, ฟังก์ชันในตัวเครื่อง
### วิวัฒนาการที่รวดเร็ว (2019–ปัจจุบัน)
- **8.0 (2019)**: ประเภทการอ้างอิงที่เป็น Nullable — ความปลอดภัยที่เป็นโมฆะในเวลาคอมไพล์
- **9.0 (2020)**: ประเภท`record`— ผู้ให้บริการข้อมูลที่ไม่เปลี่ยนรูป
- **10.0 (2021)**:`record struct`การใช้งานทั่วโลก เนมสเปซที่กำหนดขอบเขตไฟล์
- **11.0 (2022)**: คีย์เวิร์ด `required`, ตัวอักษรสตริงดิบ`"""..."""`
- **12.0 (2023)**: ตัวสร้างหลักสำหรับทุกคลาส นิพจน์คอลเลกชัน`[1, 2, 3]`
- **13.0 (2024)**:`params`สำหรับคอลเลกชันทุกประเภท
## วิวัฒนาการคุณสมบัติ
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

## วิวัฒนาการแพลตฟอร์ม .NET
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

## ปรัชญาการออกแบบภาษา
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## การเติบโตของระบบนิเวศ
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
