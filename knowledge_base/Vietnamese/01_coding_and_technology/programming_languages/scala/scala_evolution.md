---
# Metadata
title: "Scala — Version History & Evolution"
description: "Comprehensive version history and evolution of Scala from 1.0 to modern Scala."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [scala, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Scala — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| 1.0 | 2004 | Bản phát hành lần đầu (Martin Odersky, EPFL) |
| 2.0 | 2006 | Các loại cấu trúc, cải tiến khớp mẫu |
| 2.7 | 2009 | Thư viện diễn viên, suy luận kiểu cải tiến |
| 2,8 | 2010 | **Đối số được đặt tên/mặc định**, đối tượng gói, thiết kế lại bộ sưu tập |
| 2.9 | 2011 | Bộ sưu tập song song, nội suy chuỗi |
| 2.10 | 2013 | **Các lớp giá trị**, cải tiến tiềm ẩn, nội suy chuỗi |
| 2.11 | 2014 | Nội suy chuỗi, bộ sưu tập được cải tiến |
| 2.12 | 2016 | **Các loại SAM** (Java 8 lambdas), bộ sưu tập trên Strawman |
| 2.13 | 2019 | **Thiết kế lại bộ sưu tập**, các tham số ngầm định theo tên |
| 3.0 | 2021 | **Chính**: Trình biên dịch mới (Dotty),`enum`,`given`/`using`, các phương thức mở rộng |
| 3.1 | 2022 | Mệnh đề xuất, bí danh loại`opaque`|
| 3.2 | 2022 | `inline`cải tiến, từ khóa`erased`|
| 3.3 | 2023 | **Bản phát hành LTS** — giá trị rỗng rõ ràng, mệnh đề`derives`|
| 3,4 | 2024 | Đối số loại được đặt tên, chú thích`@experimental`|
| 3,5 | 2024 | Trình kiểm tra nắm bắt, thông báo lỗi được cải thiện |
| 3.6 | 2025 | Cải tiến thêm, cải tiến hiệu suất |
## Các cột mốc quan trọng
### Scala thời kỳ đầu (2004–2010)
- **2004**: Martin Odersky phát hành Scala — kết hợp OOP và FP trên JVM
- **2.0–2.7**: Kiểu cấu trúc, tác nhân, suy luận kiểu cải tiến
- **2.8 (2010)**: Đối số được đặt tên/mặc định, đối tượng gói, thiết kế lại bộ sưu tập — "Scala hiện đại bắt đầu"
### Thời gian trưởng thành của Scala 2.x (2011–2020)
- **2.9**: Bộ sưu tập song song
- **2.10**: Lớp giá trị, nội suy chuỗi, cải tiến tiềm ẩn
- **2.12**: Các loại SAM — tương tác Java 8 liền mạch
- **2.13**: Thiết kế lại thư viện các bộ sưu tập chính (mặc định không thay đổi)
### Scala 3 — Thời kỳ Phục hưng (2021–nay)
- **3.0 (2021)**: Viết lại trình biên dịch hoàn chỉnh (Dotty → Scala 3)
  -`enum`thay thế bản tóm tắt đặc điểm kín + lớp trường hợp
  - `given`/`using` thay thế các tham số ngầm định
  - Các phương thức mở rộng thay thế các lớp ẩn
  - Các loại `match`, các loại liên kết, các loại giao lộ
  - Cú pháp đơn giản hóa (dấu ngoặc nhọn tùy chọn, ít từ khóa hơn)
- **3.3 (2023)**: LTS đầu tiên — giá trị rỗng rõ ràng, mệnh đề `derives`
- **3,4–3,6**: Đối số loại được đặt tên, trình kiểm tra chụp, hiệu suất
## Tiến hóa cú pháp
```scala
// Scala 2: Implicit class for extension methods
implicit class StringOps(val s: String) extends AnyVal {
  def shout: String = s.toUpperCase + "!"
}

// Scala 3: Extension methods
extension (s: String)
  def shout: String = s.toUpperCase + "!"

// Scala 2: Sealed trait + case class (ADT)
sealed trait Color
case object Red extends Color
case object Blue extends Color

// Scala 3: enum
enum Color:
  case Red, Blue, Green

// Scala 2: Implicit parameters
def greet(implicit ctx: Context): String = ctx.name

// Scala 3: given/using
given ctx: Context = Context("Alice")
def greet(using ctx: Context): String = ctx.name

// Scala 3: Union types
def process(input: String | Int): String = input.toString

// Scala 3: Match types
type Elem[X] = X match
  case String => Char
  case List[t] => t
  case _ => X
```

## Loại tiến hóa hệ thống
```
Scala 2.0:  Structural types, refinements
Scala 2.7:  Existential types
Scala 2.8:  Implicit resolution rules
Scala 2.10: Value classes, macro annotations
Scala 2.12: SAM conversion, Java 8 interop
Scala 2.13: Implicit by-name, literal types
Scala 3.0:  Union types, intersection types, match types,
            opaque types, enum, given/using, extension methods
Scala 3.3:  Explicit nulls, derives clause
Scala 3.4:  Named type arguments
Scala 3.5:  Capture checker (experimental)
```

## Tiến hóa đồng thời
```
2009: Scala Actors library (green threads)
2011: Akka library (Actor model, JVM-based)
2013: Scala Futures + Promises (standard library)
2018: Cats Effect (functional effect system)
2020: ZIO (functional effect system, high performance)
2025: Scala 3 + virtual threads (Java 21 Loom integration)
```

## Nguyên tắc thiết kế chính
```
1. "Scalable language" — from scripts to large systems
2. "Unify OOP and FP" — everything is an object, everything is a function
3. "Type safety" — leverage the type system for correctness
4. "Interoperability" — seamless Java interop
5. "Expressiveness" — concise, elegant syntax
6. "Evidence-based" — type classes via given/using (Scala 3)
```

## Tăng trưởng hệ sinh thái
```
2004: Scala released by Martin Odersky (EPFL)
2009: Twitter adopts Scala — puts Scala on the map
2011: Akka framework — distributed computing
2012: Play Framework 2.0 — web development
2014: Apache Spark — big data processing in Scala
2016: sbt becomes standard build tool
2021: Scala 3 — modernized language
2025: Scala powers LinkedIn, Twitter, Netflix, The Guardian, Stripe
       sbt, Mill build tools; Akka, ZIO, Cats Effect ecosystems
```
