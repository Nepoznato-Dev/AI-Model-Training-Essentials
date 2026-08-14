---
# Metadata
title: "Java — Version History & Evolution"
description: "Comprehensive version history and evolution of Java from 1.0 to modern Java."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [java, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Java — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Ngày phát hành | Chủ đề chính |
|----------|-------------|----------|
| JDK 1.0 | Tháng 1 năm 1996 | Bản phát hành đầu tiên ("Oak") |
| JDK 1.1 | Tháng 2 năm 1997 | Các lớp bên trong, JDBC, RMI |
| J2SE 1.2 | Tháng 12 năm 1998 | Khung bộ sưu tập, Swing,`strictfp`|
| J2SE 1.3 | Tháng 5 năm 2000 | HotSpot JVM,`assert`|
| J2SE 1.4 | Tháng 2 năm 2002 | `assert`, NIO, biểu thức chính quy,`java.net`|
| J2SE 5.0 | Tháng 9 năm 2004 | **Chính**: Generics, enums, chú thích, autoboxing, varargs |
| Java SE 6 | Tháng 12 năm 2006 | Viết kịch bản, API trình biên dịch,`@Override`trên giao diện |
| Java SE 7 | Tháng 7 năm 2011 | `try-with-resources`,`switch`trên chuỗi, NIO.2 |
| Java SE 8 | Tháng 3 năm 2014 | **Chính**: Lambdas, Streams,`Optional`,`java.time`, các phương thức mặc định |
| Java 9 | Tháng 9 năm 2017 | Mô-đun (JPMS),`var`,`jshell`, phương thức giao diện riêng |
| Java 10 | Tháng 3 năm 2018 | `var`cho các biến cục bộ |
| Java 11 | Tháng 9 năm 2018 | **LTS**: Phương pháp `String`, `HttpClient`, khởi chạy một tệp |
| Java 12 | Tháng 3 năm 2019 | Chuyển đổi biểu thức (xem trước) |
| Java 13 | Tháng 9 năm 2019 | Khối văn bản (xem trước) |
| Java 14 | Tháng 3 năm 2020 | `record`(xem trước), biểu thức chuyển đổi, mẫu`instanceof`|
| Java 15 | Tháng 9 năm 2020 | Khối văn bản, lớp kín (xem trước) |
| Java 16 | Tháng 3 năm 2021 | `record`,`instanceof`khớp mẫu |
| Java 17 | Tháng 9 năm 2021 | **LTS**: Các lớp kín, khớp mẫu cho`switch`|
| Java 18 | Tháng 3 năm 2022 | Máy chủ web đơn giản, mặc định UTF-8 |
| Java 19 | Tháng 9 năm 2022 | Chủ đề ảo (xem trước), khớp mẫu |
| Java 20 | Tháng 3 năm 2023 | Giá trị phạm vi (vườn ươm), mẫu bản ghi |
| Java 21 | Tháng 9 năm 2023 | **LTS**: **Chủ đề ảo**, khớp mẫu, mẫu `switch`, bộ sưu tập được giải trình tự |
| Java 22 | Tháng 3 năm 2024 | Mẫu chuỗi (xem trước), API bộ nhớ ngoài |
| Java 23 | Tháng 9 năm 2024 | Các kiểu nguyên thủy trong mẫu (xem trước) |
| Java 24 | Tháng 3 năm 2025 | Đồng thời có cấu trúc (xem trước) |
| Java 25 | Tháng 9 năm 2025 | **LTS**: (dự kiến) |
## Các cột mốc quan trọng
### Kỷ nguyên cổ điển (1996–2004)
- **1.0 (1996)**: "Viết một lần, chạy mọi nơi" — applet, AWT
- **1.2 (1998)**: Khung bộ sưu tập (nền tảng của bộ sưu tập Java)
- **1.4 (2002)**: NIO, ghi nhật ký, biểu thức chính quy, xác nhận
- **5.0 (2004)**: Bản cập nhật lớn nhất — generic, enum, chú thích, autoboxing, for-loop nâng cao, varargs, `static import`
### Kỷ nguyên Doanh nghiệp (2006–2014)
- **6 (2006)**: Hỗ trợ tập lệnh, API trình biên dịch
- **7 (2011)**:`try-with-resources`, toán tử kim cương,`switch`trên chuỗi, NIO.2
- **8 (2014)**: "vụ nổ lớn" khác — lambdas, luồng,`Optional`,`java.time`, phương thức mặc định, `CompletableFuture`
### Thời Hiện Đại (2017–nay)
- **9 (2017)**: Hệ thống mô-đun (JPMS),`var`,`jshell`REPL
- **11 (2018)**: LTS đầu tiên có nhịp phát hành dưới 6 tháng; `HttpClient`; Thay đổi cấp phép Oracle JDK
- **17 (2021)**: LTS — các lớp kín, khớp mẫu
- **21 (2023)**: LTS — **luồng ảo** (Project Loom), khớp mẫu, ghi mẫu
## Nhịp phát hành 6 tháng
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## Hành trình Generics
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## Tiến hóa lập trình chức năng
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## Tiến hóa đồng thời
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## Tiến hóa tính năng ngôn ngữ
```
Java 5:   Generics, enums, annotations, autoboxing, varargs
Java 7:   try-with-resources, diamond <>, switch on String
Java 8:   Lambdas, streams, default methods, Optional
Java 9:   var (local), modules, jshell
Java 14:  record (preview), switch expressions
Java 16:  record, instanceof pattern
Java 17:  sealed classes, switch pattern matching
Java 21:  virtual threads, pattern matching, record patterns
```

## Tiến hóa JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## Tăng trưởng hệ sinh thái
```
1998: J2EE — enterprise Java begins
2001: Spring Framework
2004: Hibernate, Maven
2006: Java on Android (modified Java)
2010: Oracle acquires Sun (Java)
2014: Java 8 — Spring Boot era
2018: Java 11 — modular JDK, GraalVM
2023: Java 21 — virtual threads, Spring Boot 3
2025: Java remains #1 enterprise language
```
