---
# Metadata
title: "C# — Version History & Evolution"
description: "Comprehensive version history and evolution of C# from 1.0 to modern C#."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [csharp, dotnet, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# C# — 버전 기록 및 발전
## 타임라인
| 버전 | 연도 | .NET | 주요 테마 |
|---------|------|------|-----------|
| 1.0 | 2002 | 1.0 | 클래스, 인터페이스, 대리자, 이벤트 |
| 1.2 | 2003년 | 1.1 | `foreach`및`IDisposable`|
| 2.0 | 2005년 | 2.0 | **제네릭**, null 허용 유형, 익명 메서드, 반복자 |
| 3.0 | 2007년 | 3.5 | **LINQ**, 람다 식, 확장 메서드, `var`, 익명 유형 |
| 4.0 | 2010 | 4.0 | `dynamic`, 명명된/선택적 인수,`Tuple<T>`|
| 5.0 | 2012 | 4.5 | **`async/await`** |
| 6.0 | 2015 | 4.6 | Null 조건부`?.`, 문자열 보간, 표현식 본문 멤버 |
| 7.0 | 2017 | 코어 2.0 | 튜플, 분해, 패턴 일치,`out var`, ref 반환 |
| 7.3 | 2018 | 코어 2.1 |  표현식의`Span<T>`,`stackalloc`|
| 8.0 | 2019 | 코어 3.0 | **Nullable 참조 유형**, 스위치 표현식, 범위`..`|
| 9.0 | 2020 | 5.0 | **`record`**,`init`속성, 패턴 일치 개선 |
| 10.0 | 2021 | 6.0 | **`record struct`**, 전역 사용, 파일 범위 네임스페이스, 람다 개선 |
| 11.0 | 2022 | 7.0 | **`required`**,`raw string literals`,`file`유형,`ref`필드 |
| 12.0 | 2023년 | 8.0 | **기본 생성자**, 컬렉션 표현식 `[]`, 인라인 배열 |
| 13.0 | 2024 | 9.0 | `params`컬렉션, 새로운`Lock<T>`,`field`키워드 |
## 주요 이정표
### 초기 C#(2002~2007)
- **1.0(2002)**: .NET의 관리 코드; 쓰레기 수거; 속성, 이벤트, 대리자
- **2.0 (2005)**: 제네릭 —`List<T>`,`Dictionary<K,V>`; 널 입력 가능 유형`int?`; 반복자`yield return`
- **3.0 (2007)**: LINQ — 쿼리 구문, 람다 식, 확장 메서드, `var`, 익명 형식, 식 트리
### 현대 시대(2012~2017)
- **5.0 (2012)**:`async/await`— 비동기 프로그래밍 혁명
- **6.0 (2015)**: Null 조건부`?.`, 문자열 보간`$""`, 자동 속성 초기화 프로그램
- **7.0 (2017)**: 튜플`(int, string)`, 패턴 일치,`out var`, 로컬 함수
### 급속한 진화(2019~현재)
- **8.0(2019)**: Null 허용 참조 유형 — 컴파일 시간 Null 안전성
- **9.0(2020)**:`record`유형 — 불변 데이터 매체
- **10.0 (2021)**:`record struct`, 전역 사용, 파일 범위 네임스페이스
- **11.0(2022)**:`required`키워드, 원시 문자열 리터럴`"""..."""`
- **12.0 (2023)**: 모든 클래스의 기본 생성자, 컬렉션 표현식`[1, 2, 3]`
- **13.0(2024)**: 모든 컬렉션 유형에 대한 `params`
## 기능 진화
```
Null Safety:
  2002: Reference types always nullable
  2005: Nullable value types (int?)
  2019: Nullable reference types (string?)
  2022: Required members

Pattern Matching:
  2017: Basic type/is patterns
  2019: Switch expressions, property patterns
  2020: Relational patterns, combinator patterns
  2021: List patterns, type patterns

Async:
  2012: async/await (Task-based)
  2017: async Main, async streams (IAsyncEnumerable)
  2020: Top-level statements
  2023: async disposables

Data Types:
  2002: Classes, structs, enums
  2005: Generics
  2020: record (class)
  2021: record struct
  2023: Primary constructors for all types
```

## .NET 플랫폼의 진화
```
2002: .NET Framework 1.0 (Windows only)
2005: .NET Framework 2.0 (generics)
2012: .NET Framework 4.5 (async)
2016: .NET Core 1.0 (cross-platform!)
2019: .NET Core 3.0 (Windows desktop)
2020: .NET 5 (unified platform)
2021: .NET 6 (LTS, minimal APIs)
2022: .NET 7 (performance)
2023: .NET 8 (LTS, native AOT)
2024: .NET 9 (performance, hybridization)
2025: .NET 10 (LTS expected)
```

## 언어 디자인 철학
```
1. "The component-oriented language" — properties, events
2. "Type safety first" — generics, nullable references
3. "Expressiveness" — LINQ, pattern matching
4. "Async by default" — async/await, async streams
5. "Less ceremony" — var, global usings, primary constructors
6. "Interoperability" — P/Invoke, Span<T>, source generators
```

## 생태계 성장
```
2002: .NET Framework, Windows Forms, ASP.NET Web Forms
2005: LINQ, Entity Framework
2010: MVVM, WPF, Silverlight
2016: .NET Core — cross-platform
2018: Blazor — C# in the browser (WebAssembly)
2020: .NET 5 — unified platform
2023: .NET 8 — native AOT, minimal APIs
2025: C# — top 5 most used language; dominant in enterprise, games (Unity), cloud (Azure)
```
