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
# Java — 版本历史和演变
## 时间轴
|版本 |发布日期 |关键主题 |
|--------|-------------|------------|
| JDK 1.0 | 1996 年 1 月 |初始版本（“Oak”）|
| JDK 1.1 | 1997 年 2 月 |内部类、JDBC、RMI |
| J2SE 1.2 | J2SE 1.2 1998 年 12 月 |集合框架、Swing、`strictfp` |
| J2SE 1.3 | J2SE 1.3 2000 年 5 月 |热点 JVM，`assert` |
| J2SE 1.4 | J2SE 1.4 2002 年 2 月 | `assert`、NIO、正则表达式、`java.net` |
| J2SE 5.0 | 2004 年 9 月 | **主要**：泛型、枚举、注释、自动装箱、可变参数 |
| Java SE 6 | 2006 年 12 月 |接口上的脚本、编译器 API、`@Override` |
| Java SE 7 | 2011 年 7 月 | `try-with-resources`、`switch`字符串，NIO.2 |
| Java SE 8 | 2014 年 3 月 | **主要**：Lambdas、Streams、`Optional`、`java.time`、默认方法 |
| Java 9 | 2017 年 9 月 |模块 (JPMS)、`var` 、`jshell` 、私有接口方法 |
| Java 10 | 2018 年 3 月 | `var`用于局部变量 |
| Java 11 | 2018 年 9 月 | **LTS**：`String` 方法、`HttpClient` 、单文件启动 |
| Java 12 | 2019 年 3 月 |开关表达式（预览）|
| Java 13 | 2019 年 9 月 |文本块（预览）|
| Java 14 | 2020 年 3 月 |  `record`（预览）、开关表达式、`instanceof` 模式 |
| Java 15 | 2020 年 9 月 |文本块、密封类（预览）|
| Java 16 | 2021 年 3 月 | `record`、`instanceof`模式匹配 |
| Java 17 | 2021 年 9 月 | **LTS**：密封类，`switch` 的模式匹配 |
| Java 18 | 2022 年 3 月 |简单的Web服务器，默认UTF-8 |
| Java 19 | 2022 年 9 月 |虚拟线程（预览）、模式匹配 |
| Java 20 | 2023 年 3 月 |范围值（孵化器），记录模式 |
| Java 21 | 2023 年 9 月 | **LTS**：**虚拟线程**、模式匹配、`switch` 模式、排序集合 |
| Java 22 | 2024 年 3 月 |字符串模板（预览）、外部内存 API |
| Java 23 | 2024 年 9 月 |模式中的原始类型（预览） |
| Java 24 | 2025 年 3 月 |结构化并发（预览）|
| Java 25 | 2025 年 9 月 | **LTS**：（预期）|
## 主要里程碑
### 经典时代（1996–2004）
- **1.0 (1996)**：“一次编写，随处运行”——小程序、AWT
- **1.2 (1998)**：集合框架（Java 集合的基础）
- **1.4 (2002)**：NIO、日志记录、正则表达式、断言
- **5.0 (2004)**：最大的更新 — 泛型、枚举、注释、自动装箱、增强的 for 循环、可变参数、`static import`
### 企业时代（2006-2014）
- **6 (2006)**：脚本支持、编译器 API
- **7 (2011)**：`try-with-resources`，钻石运算符，字符串上的 `switch`，NIO.2
- **8 (2014)**：其他“大爆炸” — lambda、流、`Optional`、`java.time`、默认方法、 `CompletableFuture`
### 现代时代（2017 年至今）
- **9 (2017)**：模块系统 (JPMS)、`var`、`jshell` REPL
- **11 (2018)**：第一个 LTS 以 6 个月的发布周期发布；  `HttpClient`; Oracle JDK 许可变更
- **17 (2021)**：LTS — 密封类、模式匹配
- **21 (2023)**：LTS — **虚拟线程**（Project Loom）、模式匹配、记录模式
## 6 个月的发布节奏
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

## 函数式编程的演变
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## 并发演进
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## 语言特征演化
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

## JVM 演变
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## 生态系统增长
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
