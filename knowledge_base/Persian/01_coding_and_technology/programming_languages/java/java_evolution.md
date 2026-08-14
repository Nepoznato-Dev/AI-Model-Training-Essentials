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
# جاوا - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | تاریخ انتشار | تم کلید |
|---------|-------------|-----------|
| JDK 1.0 | ژانویه 1996 | انتشار اولیه ("بلوط") |
| JDK 1.1 | فوریه 1997 | کلاس های داخلی، JDBC، RMI |
| J2SE 1.2 | دسامبر 1998 | چارچوب مجموعه، Swing،`strictfp`|
| J2SE 1.3 | می 2000 | HotSpot JVM،`assert`|
| J2SE 1.4 | فوریه 2002 | `assert`, NIO, regex,`java.net`|
| J2SE 5.0 | سپتامبر 2004 | ** عمده **: ژنریک، فهرست، حاشیه نویسی، اتوباکسینگ، varargs |
| جاوا SE 6 | دسامبر 2006 | اسکریپت، API کامپایلر،`@Override`در رابط ها |
| جاوا SE 7 | جولای 2011 | `try-with-resources`,`switch`در String, NIO.2 |
| Java SE 8 | مارس 2014 | **عمده**: Lambdas، Streams، `Optional`، `java.time`، روش های پیش فرض |
| جاوا 9 | سپتامبر 2017 | ماژول ها (JPMS)، `var`، `jshell`، روش های رابط خصوصی |
| جاوا 10 | مارس 2018 | `var`برای متغیرهای محلی |
| جاوا 11 | سپتامبر 2018 | **LTS**: روش های `String`، `HttpClient`، راه اندازی تک فایل |
| جاوا 12 | مارس 2019 | تغییر عبارات (پیش نمایش) |
| جاوا 13 | سپتامبر 2019 | بلوک های متن (پیش نمایش) |
| جاوا 14 | مارس 2020 | `record`(پیش نمایش)، عبارات سوئیچ، الگوی`instanceof`|
| جاوا 15 | سپتامبر 2020 | بلوک های متنی، کلاس های مهر و موم شده (پیش نمایش) |
| جاوا 16 | مارس 2021 |  تطبیق الگوی`record`,`instanceof`|
| جاوا 17 | سپتامبر 2021 | **LTS**: کلاس های مهر و موم شده، تطبیق الگو برای`switch`|
| جاوا 18 | مارس 2022 | وب سرور ساده، پیش فرض UTF-8 |
| جاوا 19 | سپتامبر 2022 | موضوعات مجازی (پیش نمایش)، تطبیق الگو |
| جاوا 20 | مارس 2023 | مقادیر محدوده (انکوباتور)، الگوهای ثبت |
| جاوا 21 | سپتامبر 2023 | **LTS**: **رشته های مجازی**، تطبیق الگو، الگوهای `switch`، مجموعه های متوالی |
| جاوا 22 | مارس 2024 | قالب های رشته ای (پیش نمایش)، API حافظه خارجی |
| جاوا 23 | سپتامبر 2024 | انواع اولیه در الگوها (پیش نمایش) |
| جاوا 24 | مارس 2025 | همزمانی ساختاریافته (پیش نمایش) |
| جاوا 25 | سپتامبر 2025 | **LTS**: (مورد انتظار) |
## نقاط عطف اصلی
### دوران کلاسیک (1996-2004)
- **1.0 (1996)**: "یک بار بنویس، هر جا اجرا کن" - اپلت ها، AWT
- **1.2 (1998)**: چارچوب مجموعه ها (بنیاد مجموعه های جاوا)
- **1.4 (2002)**: NIO، ورود به سیستم، regex، ادعاها
- **5.0 (2004)**: بزرگترین به روز رسانی - ژنریک، فهرست، حاشیه نویسی، جعبه خودکار، حلقه تقویت شده، varargs، `static import`
### عصر سازمانی (2006-2014)
- **6 (2006)**: پشتیبانی از اسکریپت، API کامپایلر
- **7 (2011)**: `try-with-resources`، اپراتور الماس،`switch`در رشته، NIO.2
- **8 (2014)**: «بیگ بنگ» دیگر - لامبدا، جریان، `Optional`، `java.time`، روش های پیش فرض، `CompletableFuture`
### عصر مدرن (2017–اکنون)
- **9 (2017)**: سیستم ماژول (JPMS)، `var`،`jshell`REPL
- **11 (2018)**: اولین LTS زیر آهنگ انتشار 6 ماهه؛ `HttpClient`; تغییر مجوز Oracle JDK
- **17 (2021)**: LTS - کلاس های مهر و موم شده، تطبیق الگو
- **21 (2023)**: LTS — **رشته های مجازی** (Project Loom)، تطبیق الگو، الگوهای ضبط
## آهنگ انتشار 6 ماهه
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## سفر ژنریک
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## تکامل برنامه نویسی تابعی
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## تکامل همزمان
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## تکامل ویژگی زبان
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

## تکامل JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## رشد اکوسیستم
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
