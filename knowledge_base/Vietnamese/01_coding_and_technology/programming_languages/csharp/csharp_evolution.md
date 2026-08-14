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

# C# — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | .NET | Chủ đề chính |
|----------|------|------|----------|
| 1.0 | 2002 | 1.0 | Lớp học, giao diện, đại biểu, sự kiện |
| 1.2 | 2003 | 1.1 | `foreach`với`IDisposable`|
| 2.0 | 2005 | 2.0 | **Generics**, kiểu nullable, phương thức ẩn danh, trình vòng lặp |
| 3.0 | 2007 | 3,5 | **LINQ**, biểu thức lambda, phương thức mở rộng, `var`, loại ẩn danh |
| 4.0 | 2010 | 4.0 | `dynamic`, đối số được đặt tên/tùy chọn,`Tuple<T>`|
| 5.0 | 2012 | 4,5 | **`async/await`** |
| 6.0 | 2015 | 4.6 |`?.`không có điều kiện, nội suy chuỗi, các thành viên có biểu thức |
| 7.0 | 2017 | Cốt lõi 2.0 | Bộ dữ liệu, giải cấu trúc, khớp mẫu, `out var`, trả về ref |
| 7.3 | 2018 | Cốt lõi 2.1 | `Span<T>`,`stackalloc`trong biểu thức |
| 8.0 | 2019 | Cốt lõi 3.0 | **Các loại tham chiếu có thể rỗng**, biểu thức chuyển đổi, phạm vi`..`|
| 9,0 | 2020 | 5.0 | **`record`**, thuộc tính `init`, cải tiến so khớp mẫu |
| 10.0 | 2021 | 6.0 | **`record struct`**, cách sử dụng toàn cầu, không gian tên trong phạm vi tệp, cải tiến lambda |
| 11.0 | 2022 | 7.0 | **`required`**, các loại `raw string literals`, `file`, các trường`ref`|
| 12.0 | 2023 | 8.0 | **Hàm tạo chính**, biểu thức bộ sưu tập `[]`, mảng nội tuyến |
| 13.0 | 2024 | 9,0 |  Bộ sưu tập `params`, từ khóa`Lock<T>`mới,`field`|
## Các cột mốc quan trọng
### C# thời kỳ đầu (2002–2007)
- **1.0 (2002)**: Mã được quản lý trên .NET; thu gom rác; thuộc tính, sự kiện, đại biểu
- **2.0 (2005)**: Thuốc gốc —`List<T>`,`Dictionary<K,V>`; các loại có thể vô hiệu `int?`; vòng lặp`yield return`
- **3.0 (2007)**: LINQ — cú pháp truy vấn, biểu thức lambda, phương thức mở rộng,`var`, kiểu ẩn danh, cây biểu thức
### Thời Hiện Đại (2012–2017)
- **5.0 (2012)**:`async/await`— cuộc cách mạng lập trình không đồng bộ
- **6.0 (2015)**:`?.`không có điều kiện, nội suy chuỗi `$""`, trình khởi tạo thuộc tính tự động
- **7.0 (2017)**: Bộ dữ liệu`(int, string)`, khớp mẫu,`out var`, hàm cục bộ
### Sự tiến hóa nhanh chóng (2019–nay)
- **8.0 (2019)**: Các loại tham chiếu có thể vô hiệu — an toàn vô hiệu trong thời gian biên dịch
- **9.0 (2020)**: Loại`record`— vật mang dữ liệu bất biến
- **10.0 (2021)**:`record struct`, cách sử dụng chung, không gian tên trong phạm vi tệp
- **11.0 (2022)**: Từ khóa `required`, chuỗi ký tự thô`"""..."""`
- **12.0 (2023)**: Hàm tạo chính cho tất cả các lớp, biểu thức tập hợp`[1, 2, 3]`
- **13.0 (2024)**:`params`cho mọi loại bộ sưu tập
## Tiến hóa tính năng
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

## Sự phát triển của nền tảng .NET
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

## Triết lý thiết kế ngôn ngữ
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## Tăng trưởng hệ sinh thái
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
