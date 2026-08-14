---
# Metadata
title: "Dart — Version History & Evolution"
description: "Comprehensive version history and evolution of Dart from 1.0 to modern Dart."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [dart, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# 다트 — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 1.0 | 2013 | 최초 출시(Google, Lars Bak 및 Kasper Lund) |
| 1.2 | 2014 | Dart2JS 컴파일러 개선 |
| 1.3 | 2014 | `async`/`await`지원 |
| 1.4 | 2014 |  `enum`, 믹스인 개선 |
| 1.5 | 2014 | 생성기(`sync*`,`async*`) |
| 1.6 | 2014 | `Future`개선 |
| 1.8 | 2014 | `dart:io`개선 |
| 1.9 | 2015 | 강력 모드(선택) |
| 1.11 | 2015 | `Future.then`개선 |
| 1.12 | 2015 | **강력 모드** 시행 |
| 2.0 | 2018 | **Major**: 사운드 유형 시스템,`null`안전 준비, 컬렉션 재작성 |
| 2.1 | 2018 | `int`/`double`통합,`await for`|
| 2.2 | 2019 | `Set`리터럴,`const`컬렉션 개선 |
| 2.3 | 2019 | 컬렉션`if`, 컬렉션`for`, 스프레드 연산자`...`|
| 2.6 | 2019 | 확장 방법 |
| 2.7 | 2020 | 기본 명명된 매개변수 |
| 2.10 | 2020 | **사운드 널 안전**(선택) |
| 2.12 | 2021 | **기본적으로 Null 안전이 활성화됨** |
| 2.13 | 2021 | 생성자 분리 |
| 2.14 | 2021 | `late`개선, 부호 없는 정수 |
| 2.15 | 2021 | 생성자가 안정적이고 일반적인 함수 유형을 분리합니다 |
| 2.17 | 2022 | **수퍼 매개변수**, 향상된 열거형 |
| 2.18 | 2022 | 향상된 유형 추론 |
| 2.19 | 2023년 | 기록과 패턴(미리보기) |
| 3.0 | 2023년 | **주요**: 레코드, 패턴, 클래스 한정자,`switch`표현식 |
| 3.1 | 2023년 | 패턴 개선, 봉인된 클래스 |
| 3.2 | 2023년 | 정적 분석 개선 |
| 3.3 | 2024 | 확장 유형,`switch`표현식 개선 |
| 3.4 | 2024 | `if`요소,`case`개선 |
| 3.5 | 2024 | 매크로(미리보기), 추가 언어 개선 |
| 3.6 | 2025 | 지속적인 개발 |
## 주요 이정표
### Dart 1.x — 초기(2013~2017)
- **2013**: Google, 구조화된 웹 프로그래밍용으로 설계된 Dart 출시
- **목표**: 웹 개발을 위한 JavaScript 대체(야심은 나중에 조정됨)
- **1.0**: 클래스, 인터페이스, 격리, 선택적 입력
- **1.3**:`async`/`await`지원
- **1.9**: 강력 모드(엄격한 입력 선택)
- Chromium에서 Dart VM이 잠시 사용되었다가 제거되었습니다.
### Flutter Pivot(2017~2018)
- **2017**: Flutter 프레임워크 발표 — Dart가 UI 언어가 됨
- Dart는 자신의 목적을 찾았습니다: 크로스 플랫폼 모바일/데스크톱/웹 개발
- **2.0 (2018)**: 완전 재작성 — 사운드 유형 시스템, 현대적인 컬렉션
### 다트 2.x — 모던 다트(2018~2023)
- **2.0**: 사운드 유형 시스템, 기본적으로 `dynamic`가 더 이상 없음
- **2.3**: 컬렉션`if`/`for`, 스프레드 연산자 — Flutter 위젯 트리에 적합
- **2.6**: 확장 방법
- **2.10**: 사운드 널 안전(선택)
- **2.12**: **기본적으로 Null 안전이 활성화됨** —`?`nullable 유형
- **2.17**: 슈퍼 매개변수(`super.x`), 향상된 열거형
### Dart 3.x — 기록 및 패턴(2023~현재)
- **3.0(2023)**: **레코드**(익명 데이터 매체), **패턴**(구조 분해), **클래스 수정자**(`sealed`,`final`,`interface`,`base`),`switch`표현식
- **3.3(2024)**: 확장 유형(무료 래퍼)
- **3.5(2024)**: 매크로 미리보기 — 컴파일 타임 메타프로그래밍
## 구문 진화
```dart
// Dart 1.x: Verbose, JavaScript-like
class Person {
  String name;
  int age;
  Person(this.name, this.age);
}

// Dart 2.0: Sound types
Person createPerson(String name, int age) {
  return Person(name, age);
}

// Dart 2.3: Collection if/for, spread
var widgets = [
  if (showHeader) HeaderWidget(),
  for (var item in items) ItemWidget(item),
  ...otherWidgets,
];

// Dart 2.6: Extension methods
extension StringX on String {
  String get shout => toUpperCase() + '!';
}

// Dart 2.12: Null safety
String? nullable;     // can be null
String nonNullable;   // cannot be null (enforced)

// Dart 2.17: Super parameters, enhanced enums
class NamedPerson extends Person {
  NamedPerson({super.name, super.age});  // pass to super constructor
}

enum Status {
  active('Active'),
  inactive('Inactive');
  final String label;
  const Status(this.label);
}

// Dart 3.0: Records and patterns
(String, int) getNameAndAge() => ('Alice', 30);

sealed class Shape {}
class Circle extends Shape { final double radius; Circle(this.radius); }
class Rect extends Shape { final double w, h; Rect(this.w, this.h); }

String describe(Shape s) => switch (s) {
  Circle(radius: var r) => 'Circle($r)',
  Rect(w: var w, h: var h) => 'Rect(${w}x${h})',
};
```

## 유형 시스템 진화
```
Dart 1.0:  Optional types (annotations only)
Dart 1.9:  Strong mode (opt-in)
Dart 2.0:  Sound type system (enforced)
Dart 2.10: Sound null safety (opt-in)
Dart 2.12: Null safety by default (? nullable, ! assert)
Dart 2.15: Generic function types
Dart 3.0:  Records, sealed classes, patterns, class modifiers
Dart 3.3:  Extension types (zero-cost wrappers)
Dart 3.5:  Macros (compile-time metaprogramming)
```

## 주요 디자인 원칙
```
1. "Productive" — fast iteration, hot reload (Flutter)
2. "Safe" — sound type system, null safety
3. "Portable" — runs on mobile, web, desktop, server
4. "Approachable" — familiar syntax (C/Java/JS background)
5. "Fast" — AOT compilation (Flutter), JIT (development)
6. "Structured" — classes, interfaces, mixins, extensions
```

## 생태계 성장
```
2013: Dart 1.0 released by Google
2015: AngularDart — Google uses Dart internally
2017: Flutter announced — Dart finds its purpose
2018: Dart 2.0 — sound type system
2021: Dart 2.12 — null safety
2022: Flutter 3 — iOS, Android, Web, Desktop, Embedded
2023: Dart 3.0 — records, patterns, sealed classes
2025: Flutter + Dart power apps from BMW, Alibaba, Google Pay, Toyota
       pub.dev hosts 30,000+ packages
       Dart runs on: mobile (Flutter), web (dart2wasm), server (dart:io), embedded
```
