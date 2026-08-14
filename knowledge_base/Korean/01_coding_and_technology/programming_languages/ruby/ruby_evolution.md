---
# Metadata
title: "Ruby — Version History & Evolution"
description: "Comprehensive version history and evolution of Ruby from 1.0 to modern Ruby."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ruby, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ruby — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 0.95 | 1995 | 최초 출시("Matz" 마츠모토 유키히로) |
| 1.0 | 1996 | 첫 번째 안정 릴리스 |
| 1.2 | 1998 | 최초의 영어 문서 |
| 1.4 | 1999 | `BEGIN`/`END`,`String#unpack`|
| 1.6 | 2000 | 가비지 수집 개선 |
| 1.8 | 2003년 | $KCODE, 오니구루마 정규식 엔진 |
| 1.9 | 2007년 | **주요**: M17N(다국어), 새로운 해시 구문, 파이버 |
| 2.0 | 2013 | 키워드 인수,`Enumerator::Lazy`,`Module#prepend`|
| 2.1 | 2013 | 개선된 메소드 호출,`frozen_string_literal`|
| 2.2 | 2014 | 심볼 GC, 증분 GC |
| 2.3 | 2015 | 고정된 문자열 리터럴 pragma,`&.`안전 탐색 |
| 2.4 | 2016 | `Integer`통합,`String`유니코드 대소문자 매핑 |
| 2.5 | 2017 | `yield_self`,`rescue`/ `ensure`의 블록 |
| 2.6 | 2018 | **JIT 컴파일러(MJIT)**, 무한 범위`1..`|
| 2.7 | 2019 | 패턴 일치(실험적), 번호가 매겨진 블록 매개변수 |
| 3.0 | 2020 | **주요**: Ractor(동시성), Fiber Scheduler, RBS 유형 |
| 3.1 | 2021 | `Anonymous`블록 전달,`Hash#compact`|
| 3.2 | 2022 | `Data`클래스,`File.realpath`개선, YJIT 제작 |
| 3.3 | 2023년 | **YJIT** 주요 개선,`it`블록 매개변수 |
| 3.4 | 2024 | 프리즘 파서 기본값, 기본 블록 매개변수로`it`|
## 주요 이정표
### 초기 루비(1995~2003)
- **1995**: Matz는 Perl, Smalltalk, Lisp를 혼합하여 Ruby를 만듭니다.
- **1.0(1996)**: 첫 번째 안정 릴리스
- **1.8 (2003)**: "클래식" Ruby — 빠르고 안정적이며 널리 채택됨
### 레일스 시대(2004~2013)
- **2004**: Ruby on Rails 출시 — 웹 개발 혁명
- **1.9 (2007)**: M17N (다국어 문자열), 새로운 해시 구문 `{key: value}`, 섬유
- **2.0 (2013)**: 키워드 인수, 게으른 열거자, `Module#prepend`
### 모던 루비(2015~현재)
- **2.6(2018)**: JIT 컴파일러(MJIT) — 첫 번째 성능 푸시
- **2.7(2019)**: 패턴 일치(실험적), 번호가 매겨진 블록 매개변수`_1`
- **3.0(2020)**: **Ractor**(액터-모델 동시성), **Fiber Scheduler**(비동기 I/O), **RBS**(유형 서명)
- **3.2(2022)**:`Data`클래스(불변 값 객체), YJIT 프로덕션 지원
- **3.3(2023)**: YJIT 주요 속도 향상(최대 3배 빠름),`it`블록 매개변수
- **3.4(2024)**: 프리즘 파서가 기본으로 설정됨
## 성능의 진화
```
Ruby 1.8:  Baseline (interpreted)
Ruby 1.9:  ~1.5x faster (YARV bytecode)
Ruby 2.0:  ~1x (focus on features)
Ruby 2.6:  MJIT (experimental JIT)
Ruby 3.0:  Fiber Scheduler (async I/O)
Ruby 3.2:  YJIT (production JIT)
Ruby 3.3:  YJIT 3x faster (Rails benchmarks)
Ruby 3.4:  Prism parser (faster parsing)
Target:    3x faster than Ruby 2.5 (Ruby 3x3 goal)
```

## 동시성 진화
```
1.8:  Green threads (GIL)
1.9:  Native threads (still GIL)
2.0:  Fiber (cooperative)
2.6:  Fiber Scheduler proposal
3.0:  Ractor (Actor model, no GIL sharing)
3.0:  Fiber Scheduler (async I/O without threads)
3.3:  Improved Fiber Scheduler
```

## 패턴 매칭의 진화
```
2.7:  Experimental — case/in
3.0:  Improved — pin operator, find pattern
3.1:  One-line pattern matching
3.2:  Shortcut syntax, infinite patterns
3.4:  Pattern matching stabilized
```

## 주요 디자인 원칙
```
1. "MINASWAN" — Matz is nice and so we are nice
2. "Programmer happiness" — surprising is bad
3. "Everything is an object" — even numbers, nil, true
4. "Blocks are fundamental" — closures as first-class
5. "Duck typing" — behavior over type
6. "Convention over configuration" — Rails philosophy
```

## 생태계 성장
```
2004: Rails launches — Ruby enters mainstream
2005: RubyGems package manager
2006: Ruby wins "Language of the Year" (TIOBE)
2008: Bundler (dependency management)
2010: Ruby 1.9 adoption accelerates
2013: Ruby 2.0 — enterprise adoption
2020: Ruby 3.0 — concurrency revolution
2023: YJIT makes Ruby fast again
2025: Ruby remains top 10; Rails powers GitHub, Shopify, Basecamp, Stripe
```
