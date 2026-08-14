---
# Metadata
title: "Java — Version History & Evolution"
description: "Comprehensive version history and evolution of Java from 1.0 to modern Java."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Java — 버전 기록 및 진화
## 타임라인
| 버전 | 출시일 | 주요 테마 |
|---------|-------------|------------|
| JDK 1.0 | 1996년 1월 | 최초 릴리스("Oak") |
| JDK 1.1 | 1997년 2월 | 내부 클래스, JDBC, RMI |
| J2SE 1.2 | 1998년 12월 | 컬렉션 프레임워크, Swing,`strictfp`|
| J2SE 1.3 | 2000년 5월 | 핫스팟 JVM,`assert`|
| J2SE 1.4 | 2002년 2월 | `assert`, NIO, 정규식,`java.net`|
| J2SE 5.0 | 2004년 9월 | **주요**: 제네릭, 열거형, 주석, 오토박싱, 가변 인수 |
| 자바 SE 6 | 2006년 12월 | 인터페이스의 스크립팅, 컴파일러 API,`@Override`|
| 자바 SE 7 | 2011년 7월 | `try-with-resources`, 문자열의 `switch`, NIO.2 |
| 자바 SE 8 | 2014년 3월 | **주요**: Lambdas, Streams,`Optional`,`java.time`, 기본 메서드 |
| 자바 9 | 2017년 9월 | 모듈(JPMS),`var`,`jshell`, 개인 인터페이스 메소드 |
| 자바 10 | 2018년 3월 |  지역 변수용`var`|
| 자바 11 | 2018년 9월 | **LTS**:`String`메서드, `HttpClient`, 단일 파일 실행 |
| 자바 12 | 2019년 3월 | 표현식 전환(미리보기) |
| 자바 13 | 2019년 9월 | 텍스트 블록(미리보기) |
| 자바 14 | 2020년 3월 |  `record`(미리보기), 스위치 표현식,`instanceof`패턴 |
| 자바 15 | 2020년 9월 | 텍스트 블록, 봉인된 클래스(미리보기) |
| 자바 16 | 2021년 3월 | `record`,`instanceof`패턴 일치 |
| 자바 17 | 2021년 9월 | **LTS**: 봉인된 클래스, `switch`에 대한 패턴 일치 |
| 자바 18 | 2022년 3월 | 간단한 웹 서버, UTF-8 기본값 |
| 자바 19 | 2022년 9월 | 가상 스레드(미리보기), 패턴 일치 |
| 자바 20 | 2023년 3월 | 범위 값(인큐베이터), 기록 패턴 |
| 자바 21 | 2023년 9월 | **LTS**: **가상 스레드**, 패턴 일치,`switch`패턴, 시퀀스 컬렉션 |
| 자바 22 | 2024년 3월 | 문자열 템플릿(미리보기), 외부 메모리 API |
| 자바 23 | 2024년 9월 | 패턴의 기본 유형(미리보기) |
| 자바 24 | 2025년 3월 | 구조적 동시성(미리보기) |
| 자바 25 | 2025년 9월 | **LTS**: (예상) |
## 주요 이정표
### 고전 시대(1996~2004)
- **1.0 (1996)**: "한 번 작성하면 어디서나 실행 가능" — 애플릿, AWT
- **1.2(1998)**: 컬렉션 프레임워크(Java 컬렉션의 기초)
- **1.4 (2002)**: NIO, 로깅, 정규식, 어설션
- **5.0(2004)**: 최대 업데이트 — 제네릭, 열거형, 주석, 오토박싱, 향상된 for-loop, varargs, `static import`
### 엔터프라이즈 시대(2006~2014)
- **6 (2006)**: 스크립팅 지원, 컴파일러 API
- **7 (2011)**:`try-with-resources`, 다이아몬드 연산자, 문자열의 `switch`, NIO.2
- **8 (2014)**: 또 다른 "빅뱅" — 람다, 스트림,`Optional`,`java.time`, 기본 메서드 `CompletableFuture`
### 현대 시대(2017~현재)
- **9(2017)**: 모듈 시스템(JPMS),`var`,`jshell`REPL
- **11(2018)**: 6개월 릴리스 주기에 따른 첫 번째 LTS;  `HttpClient`; Oracle JDK 라이선스 변경
- **17(2021)**: LTS — 봉인된 클래스, 패턴 일치
- **21(2023)**: LTS — **가상 스레드**(Project Loom), 패턴 매칭, 레코드 패턴
## 6개월 출시 주기
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## 제네릭 여정
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## 함수형 프로그래밍의 진화
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## 동시성 진화
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## 언어 기능의 진화
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

## JVM의 진화
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## 생태계 성장
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
