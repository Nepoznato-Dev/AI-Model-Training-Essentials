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
# جافا — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | تاريخ الإصدار | الموضوع الرئيسي |
|---------|------------|-----------|
| جدك 1.0 | يناير 1996 | الإصدار الأولي ("أوك") |
| جدك 1.1 | فبراير 1997 | الطبقات الداخلية، JDBC، RMI |
| J2SE 1.2 | ديسمبر 1998 | إطار المجموعات، سوينغ،`strictfp`|
| J2SE 1.3 | مايو 2000 | هوت سبوت JVM،`assert`|
| J2SE 1.4 | فبراير 2002 |  `assert`، NIO، regex،`java.net`|
| J2SE 5.0 | سبتمبر 2004 | ** التخصص **: الأدوية العامة، التعدادات، التعليقات التوضيحية، autoboxing، varargs |
| جافا سي 6 | ديسمبر 2006 | البرمجة النصية، API المترجم،`@Override`على الواجهات |
| جافا سي 7 | يوليو 2011 | `try-with-resources`،`switch`على السلسلة، NIO.2 |
| جافا سي 8 | مارس 2014 | **التخصص**: Lambdas، Streams، `Optional`، `java.time`، الطرق الافتراضية |
| جافا 9 | سبتمبر 2017 | وحدات (JPMS)، `var`، `jshell`، طرق الواجهة الخاصة |
| جافا 10 | مارس 2018 | `var`للمتغيرات المحلية |
| جافا 11 | سبتمبر 2018 | **LTS**: طرق `String`، `HttpClient`، إطلاق ملف واحد |
| جافا 12 | مارس 2019 | تبديل التعبيرات (معاينة) |
| جافا 13 | سبتمبر 2019 | كتل نصية (معاينة) |
| جافا 14 | مارس 2020 | `record`(معاينة)، تعبيرات التبديل، نمط`instanceof`|
| جافا 15 | سبتمبر 2020 | الكتل النصية الطبقات المختومة (معاينة) |
| جافا 16 | مارس 2021 |  مطابقة الأنماط `record`،`instanceof`|
| جافا 17 | سبتمبر 2021 | **LTS**: فئات مختومة، مطابقة النمط لـ`switch`|
| جافا 18 | مارس 2022 | خادم ويب بسيط، UTF-8 الافتراضي |
| جافا 19 | سبتمبر 2022 | المواضيع الافتراضية (المعاينة)، مطابقة الأنماط |
| جافا 20 | مارس 2023 | القيم النطاقية (الحاضنة)، أنماط التسجيل |
| جافا 21 | سبتمبر 2023 | **LTS**: **خيوط افتراضية**، مطابقة الأنماط، أنماط `switch`، مجموعات متسلسلة |
| جافا 22 | مارس 2024 | قوالب السلسلة (معاينة)، API للذاكرة الخارجية |
| جافا 23 | سبتمبر 2024 | الأنواع البدائية في الأنماط (معاينة) |
| جافا 24 | مارس 2025 | التزامن المنظم (معاينة) |
| جافا 25 | سبتمبر 2025 | **LTS**: (متوقع) |
## المعالم الرئيسية
### العصر الكلاسيكي (1996-2004)
- **1.0 (1996)**: "الكتابة مرة واحدة، والتشغيل في أي مكان" — التطبيقات الصغيرة، AWT
- **1.2 (1998)**: إطار عمل المجموعات (أساس مجموعات Java)
- **1.4 (2002)**: NIO، التسجيل، التعبير العادي، التأكيدات
- **5.0 (2004)**: أكبر تحديث — الأدوية العامة، والتعدادات، والتعليقات التوضيحية، والعلبة التلقائية، والحلقة المحسّنة، والفارارجس، و`static import`
### عصر المشاريع (2006-2014)
- **6 (2006)**: دعم البرمجة النصية، واجهة برمجة تطبيقات المترجم
- **7 (2011)**: `try-with-resources`، عامل الماس،`switch`on String، NIO.2
- **8 (2014)**: "الانفجار الكبير" الآخر - لامداس، التدفقات، `Optional`، `java.time`، الأساليب الافتراضية، `CompletableFuture`
### العصر الحديث (2017–الآن)
- **9 (2017)**: نظام الوحدة (JPMS)،`var`،`jshell`REPL
- **11 (2018)**: أول إصدار LTS في أقل من 6 أشهر؛ `HttpClient`; تغيير ترخيص Oracle JDK
- **17 (2021)**: LTS — فئات مختومة، مطابقة الأنماط
- **21 (2023)**: LTS — **خيوط افتراضية** (Project Loom)، مطابقة الأنماط، أنماط التسجيل
## إيقاع الإصدار لمدة 6 أشهر
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## رحلة الأدوية الجنيسة
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## تطور البرمجة الوظيفية
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## تطور التزامن
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## تطور ميزة اللغة
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

## تطور JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## نمو النظام البيئي
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
