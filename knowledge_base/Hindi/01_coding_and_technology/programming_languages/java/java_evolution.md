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
# जावा - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | रिलीज की तारीख | मुख्य विषय |
|--|----|----|
| जेडीके 1.0 | जनवरी 1996 | आरंभिक रिलीज़ ("ओक") |
| जेडीके 1.1 | फरवरी 1997 | आंतरिक कक्षाएं, जेडीबीसी, आरएमआई |
| जे2एसई 1.2 | दिसंबर 1998 | संग्रह ढांचा, स्विंग,`strictfp`|
| जे2एसई 1.3 | मई 2000 | हॉटस्पॉट JVM,`assert`|
| जे2एसई 1.4 | फरवरी 2002 | `assert`, NIO, regex,`java.net`|
| जे2एसई 5.0 | सितम्बर 2004 | **प्रमुख**: जेनरिक, एनम्स, एनोटेशन, ऑटोबॉक्सिंग, वेरार्ग्स |
| जावा एसई 6 | दिसम्बर 2006 | स्क्रिप्टिंग, कंपाइलर एपीआई, इंटरफेस पर`@Override`|
| जावा एसई 7 | जुलाई 2011 | `try-with-resources`,`switch`स्ट्रिंग पर, NIO.2 |
| जावा एसई 8 | मार्च 2014 | **प्रमुख**: लैम्ब्डा, स्ट्रीम, `Optional`, `java.time`, डिफ़ॉल्ट विधियाँ |
| जावा 9 | सितंबर 2017 | मॉड्यूल (JPMS),`var`,`jshell`, निजी इंटरफ़ेस विधियाँ |
| जावा 10 | मार्च 2018 |  स्थानीय चर के लिए`var`|
| जावा 11 | सितंबर 2018 | **LTS**:`String`विधियाँ, `HttpClient`, एकल-फ़ाइल लॉन्च |
| जावा 12 | मार्च 2019 | भाव बदलें (पूर्वावलोकन) |
| जावा 13 | सितंबर 2019 | टेक्स्ट ब्लॉक (पूर्वावलोकन) |
| जावा 14 | मार्च 2020 | `record`(पूर्वावलोकन), स्विच एक्सप्रेशन,`instanceof`पैटर्न |
| जावा 15 | सितंबर 2020 | टेक्स्ट ब्लॉक, सीलबंद कक्षाएं (पूर्वावलोकन) |
| जावा 16 | मार्च 2021 | `record`,`instanceof`पैटर्न मिलान |
| जावा 17 | सितंबर 2021 | **एलटीएस**: सीलबंद कक्षाएं,`switch`के लिए पैटर्न मिलान |
| जावा 18 | मार्च 2022 | सरल वेब सर्वर, UTF-8 डिफ़ॉल्ट |
| जावा 19 | सितंबर 2022 | आभासी धागे (पूर्वावलोकन), पैटर्न मिलान |
| जावा 20 | मार्च 2023 | स्कोप्ड मान (इनक्यूबेटर), रिकॉर्ड पैटर्न |
| जावा 21 | सितम्बर 2023 | **एलटीएस**: **आभासी धागे**, पैटर्न मिलान,`switch`पैटर्न, अनुक्रमित संग्रह |
| जावा 22 | मार्च 2024 | स्ट्रिंग टेम्प्लेट (पूर्वावलोकन), विदेशी मेमोरी एपीआई |
| जावा 23 | सितंबर 2024 | पैटर्न में आदिम प्रकार (पूर्वावलोकन) |
| जावा 24 | मार्च 2025 | संरचित समवर्ती (पूर्वावलोकन) |
| जावा 25 | सितम्बर 2025 | **एलटीएस**: (अपेक्षित) |
## प्रमुख मील के पत्थर
### द क्लासिक एरा (1996-2004)
- **1.0 (1996)**: "एक बार लिखें, कहीं भी चलाएं" - एप्लेट्स, एडब्ल्यूटी
- **1.2 (1998)**: संग्रह ढांचा (जावा संग्रह की नींव)
- **1.4 (2002)**: एनआईओ, लॉगिंग, रेगेक्स, अभिकथन
- **5.0 (2004)**: सबसे बड़ा अपडेट - जेनेरिक, एनम, एनोटेशन, ऑटोबॉक्सिंग, एन्हांस्ड फॉर-लूप, वेरार्ग, `static import`
### द एंटरप्राइज एरा (2006-2014)
- **6 (2006)**: स्क्रिप्टिंग समर्थन, कंपाइलर एपीआई
- **7 (2011)**: `try-with-resources`, हीरा संचालक, स्ट्रिंग पर `switch`, NIO.2
- **8 (2014)**: अन्य "बड़ा धमाका" - लैम्ब्डा, स्ट्रीम, `Optional`, `java.time`, डिफ़ॉल्ट तरीके, `CompletableFuture`
### आधुनिक युग (2017–मौजूदा)
- **9 (2017)**: मॉड्यूल सिस्टम (जेपीएमएस), `var`,`jshell`REPL
- **11 (2018)**: 6 महीने की रिलीज़ ताल के तहत पहला एलटीएस; `HttpClient`; Oracle JDK लाइसेंसिंग परिवर्तन
- **17 (2021)**: एलटीएस - सीलबंद कक्षाएं, पैटर्न मिलान
- **21 (2023)**: एलटीएस - **वर्चुअल थ्रेड्स** (प्रोजेक्ट लूम), पैटर्न मिलान, रिकॉर्ड पैटर्न
## 6 महीने की रिलीज़ ताल
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## जेनेरिक यात्रा
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## कार्यात्मक प्रोग्रामिंग विकास
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## समवर्ती विकास
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## भाषा सुविधा विकास
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

## जेवीएम इवोल्यूशन
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## पारिस्थितिकी तंत्र का विकास
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
