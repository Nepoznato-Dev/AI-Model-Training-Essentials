<!--
---
# Metadata
title: "Rust — Version History & Evolution"
description: "Comprehensive version history and evolution of Rust from early development to modern Rust."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [rust, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Rust — 버전 기록 및 진화
## 타임라인
| 버전 | 출시일 | 주요 테마 |
|---------|-------------|------------|
| 0.1 | 2012년 1월 | 최초의 컴파일러(rustc), 작업 기반 동시성 |
| 0.5 | 2012 | 특성 기반 유형 시스템이 구체화됩니다 |
| 0.6 | 2012 |`@`관리 상자 제거 |
| 0.7 | 2013 |  `@`가 제거되었습니다. 소유한 상자의 경우`~`|
| 0.8 | 2013 | 평생 주석,`&mut`|
| 0.9 | 2014년 1월 | 1.0 이전 최종 정리 |
| 0.10 | 2014년 2월 | 1.0 이전 마지막 릴리스 |
| 0.11 | 2014년 4월 |  `Box<T>`가 `~T`를 대체합니다 |
| 0.12 | 2014년 5월 | `io`모듈 재작성 시작 |
| 1.0 | 2015년 5월 15일 | **안정적인 릴리스** — "Rust 1.0" |
| 1.10 | 2016년 8월 | `?`오류 전파(`try!` →`?`) |
| 1.15 | 2017년 2월 |`impl Trait`준비를 통해 안정적인 첫 Rust |
| 1.18 | 2017년 6월 |  `pub(crate)`, 증분 컴파일 |
| 1.20 | 2017년 10월 | 관련 상수 |
| 1.26 | 2018년 5월 |  인수/반환 위치의`impl Trait`|
| 1.28 | 2018년 9월 | 글로벌 할당자 |
| 1.31 | 2018년 12월 | **Rust 2018 에디션** — 모듈,`dyn Trait`|
| 1.34 | 2019년 4월 | 대체 레지스트리 |
| 1.39 | 2019년 11월 |  안정적인`async/await`|
| 1.44 | 2020년 7월 | 진단 개선 |
| 1.51 | 2021년 4월 | `const`제네릭(MVP) |
| 1.56 | 2021년 10월 | **Rust 2021 에디션** — 클로저, IntoIterator |
| 1.59 | 2022년 2월 | 인라인 조립 |
| 1.62 | 2022년 6월 |  열거형용`#[default]`|
| 1.65 | 2022년 12월 | `let else`|
| 1.68 | 2023년 3월 |  `#[ffi_pure]`, 프로필 기반 최적화 |
| 1.70 | 2023년 6월 | 격리된`crates.io`종속성 |
| 1.74 | 2023년 11월 | 화물 오프라인 모드 |
| 1.76 | 2024년 2월 | **Rust 2024 에디션** —`gen`블록,`unsafe extern`|
| 1.79 | 2024년 6월 | `LazyCell`,`LazyLock`|
| 1.82 | 2024년 10월 | `extern`블록의`unsafe`필요 |
| 1.85 | 2025년 2월 | Rust 2024 에디션 안정화 |
## 주요 이정표
### 1.0 이전(2010~2015)
- **2010**: Mozilla에서 Graydon Hoare의 사이드 프로젝트가 주목을 받았습니다.
- **2012**: 최초의 공개 컴파일러; 유형 시스템이 대대적으로 재설계되었습니다.
- **2013**: 소유권 모델이 구체화됩니다. `@`상자가 제거되었습니다.
- **2014**: Rust RFC 프로세스가 공식화되었습니다. 커뮤니티가 성장하다
- **2015**: **1.0** — 안정성 보장; "비용이 들지 않는 추상화"
### 성장의 해(2015~2019)
- **2015년**: Cargo가 표준 패키지 관리자가 됨
- **2018**: **Rust 2018 에디션** — 모듈 시스템 점검,`dyn Trait`,`impl Trait`
- **2019**: `async/await`가 안정적으로 출시됨 — 비동기 생태계가 시작됩니다.
### 성숙도(2020~현재)
- **2021**: **Rust 2021 에디션** — 클로저의 필드 명확화, 배열의 경우 `IntoIterator`
- **2024**: **Rust 2024 에디션** —`gen`블록,`unsafe extern`요구 사항
- **2025**: Linux 커널, Android, Windows, AWS 인프라의 Rust
## 에디션 시스템
```
Rust 2015:  The baseline (1.0)
Rust 2018:  Module system, async/await prep, dyn Trait
Rust 2021:  Closure changes, IntoIterator, panic macros
Rust 2024:  gen blocks, unsafe extern, tail expressions

Key principle: Editions are opt-in, never break existing code.
Old editions always compile. New editions add features.
```

## 소유권 진화
```
2010: GC-based, like Erlang
2011: Region-based lifetimes proposed
2012: Ownership model emerges (unique, shared, owned)
2013: Simplified to &T / &mut T / Box<T>
2014: Box<T> replaces ~T; Rc<T> for shared ownership
2015: 1.0 — ownership model finalized
2018: Non-Lexical Lifetimes (NLL) in Rust 2018
2021: IntoIterator for arrays (was blocked by edition concerns)
2024: Further NLL improvements
```

## 비동기 진화
```
2018: futures 0.1 — early async with manual polling
2019: async/await syntax (Rust 1.39)
2019: tokio 0.2 — async runtime
2020: async-std — std-like async API
2021: tokio 1.0 — stable async runtime
2023: async fn in traits (Rust 1.75)
2024: async closures, improved Send bounds
```

## 생태계 성장
```
2015: crates.io launches (~2,000 crates)
2018: Rust most loved language (Stack Overflow survey)
2019: 30,000 crates on crates.io
2021: Most admired language (6th consecutive year)
2023: 130,000+ crates
2025: Used in Linux kernel, Android, Windows, Chromium, AWS, Cloudflare, Discord, Dropbox
```

## 주요 RFC
| RFC | 연도 | 기능 |
|------|------|---------|
| 25 | 2013 | 패턴 매칭 |
| 153 | 2014 | `Result`유형 |
| 217 | 2014 |  `?`(시도) 연산자 |
| 460 | 2016 |  `?`가 `try!`를 대체합니다 |
| 1210 | 2015 | `impl Trait`|
| 1414 | 2016 | 러스트 2018 에디션 |
| 2394 | 2018 | `async/await`|
| 2515 | 2018 | `const`제네릭 |
| 3013 | 2020 | 조건부 컴파일 확인 |
| 3517 | 2023년 | `gen`블록 |