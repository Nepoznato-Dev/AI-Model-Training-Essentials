<!--
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

-->
# Java — 版本歷史與演變
## 時間軸
|版本 |發佈日期 |關鍵主題 |
|--------|-------------|------------|
| JDK 1.0 | 1996 年 1 月 |初始版本（“Oak”）|
| JDK 1.1 | 1997 年 2 月 |內部類別、JDBC、RMI |
| J2SE 1.2 | J2SE 1.2 1998 年 12 月 |集合架構、Swing、`strictfp` |
| J2SE 1.3 | J2SE 1.3 2000 年 5 月 |熱點 JVM，`assert` |
| J2SE 1.4 | J2SE 1.4 2002 年 2 月 |`assert`、NIO、正規表示式、`java.net` |
| J2SE 5.0 | 2004 年 9 月 | **主要**：泛型、枚舉、註釋、自動裝箱、可變參數 |
| Java SE 6 | 2006 年 12 月 |介面上的腳本、編譯器 API、`@Override` |
| Java SE 7 | 2011 年 7 月 |`try-with-resources`、`switch`字串，NIO.2 |
| Java SE 8 | 2014 年 3 月 | **主要**：Lambdas、Streams、`Optional`、`java.time`、預設方法 |
| Java 9 | 2017 年 9 月 |模組 (JPMS)、`var` 、`jshell` 、私有介面方法 |
| Java 10 | 2018 年 3 月 |`var`用於局部變數 |
| Java 11 | 2018 年 9 月 | **LTS**：`String` 方法、`HttpClient` 、單一檔案啟動 |
| Java 12 | 2019 年 3 月 |開關表達式（預覽）|
| Java 13 | 2019 年 9 月 |文字區塊（預覽）|
| Java 14 | 2020 年 3 月 | `record`（預覽）、開關表達式、`instanceof` 模式 |
| Java 15 | 2020 年 9 月 |文字區塊、密封類別（預覽）|
| Java 16 | 2021 年 3 月 |`record`、`instanceof`模式比對 |
| Java 17 | 2021 年 9 月 | **LTS**：密封類，`switch` 的模式匹配 |
| Java 18 | 2022 年 3 月 |簡單的Web伺服器，預設UTF-8 |
| Java 19 | 2022 年 9 月 |虛擬執行緒（預覽）、模式比對 |
| Java 20 | 2023 年 3 月 |範圍值（孵化器），記錄模式 |
| Java 21 | 2023 年 9 月 | **LTS**：**虛擬執行緒**、模式比對、`switch` 模式、排序集合 |
| Java 22 | 2024 年 3 月 |字串模板（預覽）、外部記憶體 API |
| Java 23 | 2024 年 9 月 |模式中的原始類型（預覽） |
| Java 24 | 2025 年 3 月 |結構化並發（預覽）|
| Java 25 | 2025 年 9 月 | **LTS**：（預期）|
## 主要里程碑
### 經典時代（1996–2004）
- **1.0 (1996)**：「一次編寫，隨處運行」——小程式、AWT
- **1.2 (1998)**：集合架構（Java 集合的基礎）
- **1.4 (2002)**：NIO、日誌記錄、正規表示式、斷言
- **5.0 (2004)**：最大的更新 — 泛型、枚舉、註釋、自動裝箱、增強的 for 循環、可變參數、`static import`
### 企業時代（2006-2014）
- **6 (2006)**：腳本支援、編譯器 API
- **7 (2011)**：`try-with-resources`，鑽石運算符，字串上的 `switch`，NIO.2
- **8 (2014)**：其他「大爆炸」 — lambda、串流、`Optional`、`java.time`、預設方法、 `CompletableFuture`
### 現代時代（2017 年至今）
- **9 (2017)**：模組系統 (JPMS)、`var`、`jshell` REPL
- **11 (2018)**：第一個 LTS 以 6 個月的發布週期發布； `HttpClient`; Oracle JDK 許可變更
- **17 (2021)**：LTS — 密封類別、模式匹配
- **21 (2023)**：LTS — **虛擬執行緒**（Project Loom）、模式比對、記錄模式
## 6 個月的發布節奏
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## 泛型之旅
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## 函數式程式設計的演變
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## 並發演進
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## 語言特徵演化
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

## JVM 演變
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## 生態系成長
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
