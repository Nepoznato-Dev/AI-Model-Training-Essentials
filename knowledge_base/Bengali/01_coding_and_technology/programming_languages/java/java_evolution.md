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
# জাভা — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | মুক্তির তারিখ | মূল থিম |
|---------|---------------|------------|
| JDK 1.0 | জানুয়ারী 1996 | প্রাথমিক প্রকাশ ("ওক") |
| JDK 1.1 | ফেব্রুয়ারী 1997 | ইনার ক্লাস, JDBC, RMI |
| J2SE 1.2 | ডিসেম্বর 1998 | সংগ্রহ কাঠামো, সুইং,`strictfp`|
| J2SE 1.3 | মে 2000 | হটস্পট JVM,`assert`|
| J2SE 1.4 | ফেব্রুয়ারী 2002 | `assert`, NIO, regex,`java.net`|
| J2SE 5.0 | সেপ্টেম্বর 2004 | **মেজর**: জেনেরিক, এনাম, টীকা, অটোবক্সিং, ভারার্গস |
| জাভা এসই 6 | ডিসেম্বর 2006 | স্ক্রিপ্টিং, কম্পাইলার API, ইন্টারফেসে`@Override`|
| জাভা এসই 7 | জুলাই 2011 | `try-with-resources`,`switch`অন স্ট্রিং, NIO.2 |
| জাভা এসই 8 | মার্চ 2014 | **মেজর**: ল্যাম্বডাস, স্ট্রীমস,`Optional`,`java.time`, ডিফল্ট পদ্ধতি |
| জাভা 9 | সেপ্টেম্বর 2017 | মডিউল (JPMS),`var`,`jshell`, ব্যক্তিগত ইন্টারফেস পদ্ধতি |
| জাভা 10 | মার্চ 2018 |  স্থানীয় ভেরিয়েবলের জন্য`var`|
| জাভা 11 | সেপ্টেম্বর 2018 | **LTS**:`String`পদ্ধতি,`HttpClient`, একক-ফাইল লঞ্চ |
| জাভা 12 | মার্চ 2019 | এক্সপ্রেশন পরিবর্তন করুন (প্রিভিউ) |
| জাভা 13 | সেপ্টেম্বর 2019 | টেক্সট ব্লক (প্রিভিউ) |
| জাভা 14 | মার্চ 2020 | `record`(প্রিভিউ), সুইচ এক্সপ্রেশন,`instanceof`প্যাটার্ন |
| জাভা 15 | সেপ্টেম্বর 2020 | টেক্সট ব্লক, সিল করা ক্লাস (প্রিভিউ) |
| জাভা 16 | মার্চ 2021 | `record`,`instanceof`প্যাটার্ন ম্যাচিং |
| জাভা 17 | সেপ্টেম্বর 2021 | **LTS**: সিল করা ক্লাস,`switch`এর জন্য প্যাটার্ন ম্যাচিং |
| জাভা 18 | মার্চ 2022 | সাধারণ ওয়েব সার্ভার, UTF-8 ডিফল্ট |
| জাভা 19 | সেপ্টেম্বর 2022 | ভার্চুয়াল থ্রেড (প্রিভিউ), প্যাটার্ন ম্যাচিং |
| জাভা 20 | মার্চ 2023 | স্কোপড মান (ইনকিউবেটর), রেকর্ড প্যাটার্ন |
| জাভা 21 | সেপ্টেম্বর 2023 | **LTS**: **ভার্চুয়াল থ্রেড**, প্যাটার্ন ম্যাচিং,`switch`প্যাটার্ন, সিকোয়েন্সড কালেকশন |
| জাভা 22 | মার্চ 2024 | স্ট্রিং টেমপ্লেট (প্রিভিউ), বিদেশী মেমরি API |
| জাভা 23 | সেপ্টেম্বর 2024 | প্যাটার্নে আদিম প্রকার (প্রিভিউ) |
| জাভা 24 | মার্চ 2025 | স্ট্রাকচার্ড কনকারেন্সি (প্রিভিউ) |
| জাভা 25 | সেপ্টেম্বর 2025 | **LTS**: (প্রত্যাশিত) |
## প্রধান মাইলফলক
### দ্য ক্লাসিক এরা (1996-2004)
- **1.0 (1996): "একবার লিখুন, যে কোনো জায়গায় চালান" — অ্যাপলেট, AWT
- **1.2 (1998): সংগ্রহ কাঠামো (জাভা সংগ্রহের ভিত্তি)
- **1.4 (2002): এনআইও, লগিং, রেজেক্স, দাবী
- **5.0 (2004)**: সবচেয়ে বড় আপডেট — জেনেরিক, এনাম, টীকা, অটোবক্সিং, বর্ধিত ফর-লুপ, ভারার্গস, `static import`
### এন্টারপ্রাইজ যুগ (2006-2014)
- **6 (2006): স্ক্রিপ্টিং সমর্থন, কম্পাইলার API
- **7 (2011):`try-with-resources`, ডায়মন্ড অপারেটর,`switch`অন স্ট্রিং, NIO.2
- **8 (2014): অন্য "বিগ ব্যাং" — ল্যাম্বডাস, স্ট্রিম,`Optional`,`java.time`, ডিফল্ট পদ্ধতি, `CompletableFuture`
### আধুনিক যুগ (2017-বর্তমান)
- **9 (2017): মডিউল সিস্টেম (JPMS),`var`,`jshell`REPL
- **11 (2018): 6 মাসের রিলিজ ক্যাডেন্সের অধীনে প্রথম LTS; `HttpClient`; ওরাকল জেডিকে লাইসেন্সিং পরিবর্তন
- **17 (2021): LTS — সিল করা ক্লাস, প্যাটার্ন ম্যাচিং
- **21 (2023): LTS — **ভার্চুয়াল থ্রেড** (প্রজেক্ট লুম), প্যাটার্ন ম্যাচিং, রেকর্ড প্যাটার্ন
## ৬ মাসের রিলিজ ক্যাডেন্স
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## জেনেরিক জার্নি
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## কার্যকরী প্রোগ্রামিং বিবর্তন
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## কনকারেন্সি বিবর্তন
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## ভাষার বৈশিষ্ট্য বিবর্তন
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

## জেভিএম বিবর্তন
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## ইকোসিস্টেম বৃদ্ধি
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
