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
# Java — ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | วันที่วางจำหน่าย | ธีมหลัก |
|---------|-------------|-----------|
| JDK 1.0 | ม.ค. 2539 | การเปิดตัวครั้งแรก ("โอ๊ค") |
| JDK 1.1 | ก.พ. 2540 | คลาสภายใน, JDBC, RMI |
| J2SE 1.2 | ธ.ค. 2541 | กรอบคอลเลกชัน, สวิง,`strictfp`|
| J2SE 1.3 | พฤษภาคม 2543 | ฮอตสปอต JVM,`assert`|
| J2SE 1.4 | ก.พ. 2545 | `assert`, NIO, regex,`java.net`|
| J2SE 5.0 | ก.ย. 2547 | **หลัก**: ข้อมูลทั่วไป, enums, คำอธิบายประกอบ, autoboxing, varargs |
| ชวา SE 6 | ธ.ค. 2549 | การเขียนสคริปต์, คอมไพเลอร์ API,`@Override`บนอินเทอร์เฟซ |
| ชวา SE 7 | ก.ค. 2554 | `try-with-resources`,`switch`บนสตริง, NIO.2 |
| ชวา SE 8 | มี.ค. 2557 | **หลัก**: Lambdas, Streams,`Optional`,`java.time`, วิธีการเริ่มต้น |
| ชวา 9 | ก.ย. 2560 | โมดูล (JPMS),`var`,`jshell`, วิธีการอินเทอร์เฟซส่วนตัว |
| ชวา 10 | มี.ค. 2561 | `var`สำหรับตัวแปรโลคัล |
| ชวา 11 | ก.ย. 2561 | **LTS**: วิธี `String`,`HttpClient`, การเรียกใช้ไฟล์เดียว |
| ชวา 12 | มี.ค. 2562 | สลับนิพจน์ (ดูตัวอย่าง) |
| ชวา 13 | ก.ย. 2562 | บล็อกข้อความ (ตัวอย่าง) |
| ชวา 14 | มี.ค. 2563 | `record`(ดูตัวอย่าง), สลับนิพจน์, รูปแบบ`instanceof`|
| ชวา 15 | ก.ย. 2563 | บล็อกข้อความ คลาสที่ปิดผนึก (ตัวอย่าง) |
| ชวา 16 | มี.ค. 2564 | `record`,`instanceof`การจับคู่รูปแบบ |
| ชวา 17 | ก.ย. 2564 | **LTS**: คลาสที่ปิดผนึก การจับคู่รูปแบบสำหรับ`switch`|
| ชวา 18 | มี.ค. 2565 | เว็บเซิร์ฟเวอร์ธรรมดา ค่าเริ่มต้น UTF-8 |
| ชวา 19 | ก.ย. 2565 | เธรดเสมือน (ดูตัวอย่าง) การจับคู่รูปแบบ |
| ชวา 20 | มี.ค. 2566 | ค่าที่กำหนดขอบเขต (ตู้ฟัก) รูปแบบการบันทึก |
| ชวา 21 | ก.ย. 2566 | **LTS**: **เธรดเสมือน**, การจับคู่รูปแบบ, รูปแบบ `switch`, คอลเลกชันที่เรียงลำดับ |
| ชวา 22 | มี.ค. 2567 | เทมเพลตสตริง (ตัวอย่าง), API หน่วยความจำต่างประเทศ |
| ชวา 23 | ก.ย. 2567 | ประเภทดั้งเดิมในรูปแบบ (ตัวอย่าง) |
| ชวา 24 | มี.ค. 2568 | เห็นพ้องกันอย่างมีโครงสร้าง (ตัวอย่าง) |
| ชวา 25 | ก.ย. 2568 | **LTS**: (คาดไว้) |
## เหตุการณ์สำคัญที่สำคัญ
### ยุคคลาสสิก (พ.ศ. 2539–2547)
- **1.0 (1996)**: "เขียนครั้งเดียว เรียกใช้ได้ทุกที่" — แอพเพล็ต, AWT
- **1.2 (1998)**: กรอบงานคอลเลกชัน (รากฐานของคอลเลกชัน Java)
- **1.4 (2002)**: NIO, การบันทึก, regex, การยืนยัน
- **5.0 (2004)**: การอัปเดตที่ใหญ่ที่สุด — generics, enums, annotation, autoboxing, for-loop ที่ปรับปรุงแล้ว, varargs, `static import`
### ยุคองค์กร (พ.ศ. 2549–2557)
- **6 (2006)**: รองรับการเขียนสคริปต์, คอมไพลเลอร์ API
- **7 (2011)**:`try-with-resources`ตัวดำเนินการเพชร`switch`บน String, NIO.2
- **8 (2014)**: "บิ๊กแบง" อื่น ๆ — lambdas, สตรีม,`Optional`,`java.time`, วิธีการเริ่มต้น, `CompletableFuture`
### ยุคสมัยใหม่ (พ.ศ. 2560–ปัจจุบัน)
- **9 (2017)**: ระบบโมดูล (JPMS),`var`,`jshell`REPL
- **11 (2018)**: LTS แรกต่ำกว่าจังหวะการเผยแพร่ 6 เดือน `HttpClient`; การเปลี่ยนแปลงสิทธิ์การใช้งาน Oracle JDK
- **17 (2021)**: LTS — คลาสที่ปิดผนึก การจับคู่รูปแบบ
- **21 (2023)**: LTS — **virtual threads** (Project Loom), การจับคู่รูปแบบ, รูปแบบการบันทึก
## จังหวะการเปิดตัว 6 เดือน
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## การเดินทางทั่วไป
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## วิวัฒนาการการเขียนโปรแกรมเชิงฟังก์ชัน
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## วิวัฒนาการพร้อมกัน
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## วิวัฒนาการคุณสมบัติภาษา
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

## วิวัฒนาการ JVM
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## การเติบโตของระบบนิเวศ
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
