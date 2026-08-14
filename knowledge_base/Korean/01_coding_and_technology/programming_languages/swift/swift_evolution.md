<!--
---
# Metadata
title: "Swift — Version History & Evolution"
description: "Comprehensive version history and evolution of Swift from 1.0 to modern Swift."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [swift, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Swift — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 1.0 | 2014 | 최초 출시(Chris Lattner, Apple) |
| 1.1 | 2014 | 실패한 초기화 프로그램,`@autoclosure`|
| 1.2 | 2015 | `as?`/`as!`,`Set`유형, 튜플 비교 |
| 2.0 | 2015 | 프로토콜 확장,`defer`,`guard`,`errortype`|
| 2.1 | 2015 | `try?`, 리터럴의 문자열 보간 |
| 2.2 | 2016 | `#selector`,`defer`, 튜플 반환 |
| 3.0 | 2016 | **주요**: API 재설계 — 명명 규칙,`@discardableResult`|
| 4.0 | 2017 | `Codable`,`String`다시 쓰기, 여러 줄 리터럴 |
| 5.0 | 2019 | **주요**:`async/await`준비, ABI 안정성,`Result`유형 |
| 5.1 | 2019 |  `some`(불투명 유형), 속성 래퍼,`@resultBuilder`|
| 5.2 | 2020 | 함수로 호출, 함수로`KeyPath`|
| 5.3 | 2020 | `@MainActor`, 다중 후행 클로저,`enum`개선 |
| 5.4 | 2021 | 다중 가변 매개변수,`@resultBuilder`개선 |
| 5.5 | 2021 | **`async/await`**, 배우,`Sendable`|
| 5.6 | 2022 | `any`키워드,`Clock`,`Duration`|
| 5.7 | 2022 | `if let`약어,`Regex`리터럴,`Clock`프로토콜 |
| 5.8 | 2023년 | 기능백 탑재,`Clock`개선 |
| 5.9 | 2023년 | **매크로**, 매개변수 팩,`consume`/`discard`|
| 5.10 | 2024 | 완전한 동시성 검사, 엄격한 데이터 경쟁 안전 |
| 6.0 | 2024 | **주요**: 기본적으로 엄격한 동시성, 입력된 throw |
| 6.1 | 2025 | (예상) 동시성 개선 |
## 주요 이정표
### Swift 1.x — 탄생(2014~2015)
- **2014**: WWDC에서 발표됨; Apple 개발을 위해 Objective-C를 대체합니다.
- **1.0**: 옵션, 제네릭, 클로저, 유형 추론, 프로토콜
- **1.2**:`as?`/`as!`패턴,`Set`유형
### Swift 2.x — 오류 처리(2015~2016)
- **2.0**: 프로토콜 확장(프로토콜 지향 프로그래밍),`guard`,`defer`,`do/try/catch`
- **2.1**: 선택적 오류 처리를 위한 `try?`
### Swift 3.x — 뛰어난 API 이름 변경(2016)
- **3.0**: 대규모 API 재설계 — "대규모 통합 이름 변경"
- 명명 규칙:`stringByAppendingString`→`appending`
- C 스타일`for`루프,`++`/`--`연산자를 제거했습니다.
- 기본적으로 첫 번째 매개변수 라벨
### Swift 4.x — 코딩 가능(2017)
- **4.0**:`Codable`프로토콜(JSON 인코딩/디코딩),`String`재작성, 여러 줄 문자열 리터럴
### Swift 5.x — 안정성(2019~2024)
- **5.0**: ABI 안정성(앱이 작아짐),`Result`유형, 원시 문자열
- **5.1**: 불투명 유형(`some View`), 속성 래퍼(`@State`,`@Binding`)
- **5.5**: **`async/await`**, 액터,`Sendable`프로토콜
- **5.9**: 매크로(컴파일 타임 코드 생성), 매개변수 팩
### Swift 6.x — 동시성 안전성(2024년~현재)
- **6.0**: 기본적으로 엄격한 동시성 검사, 입력된 throw
## 동시성 진화
```
1.0:  GCD (Grand Central Dispatch) — Objective-C pattern
2.0:  Protocol extensions for async patterns
5.5:  async/await, actors, Sendable
5.10: Complete concurrency checking
6.0:  Strict concurrency by default (data race safety)
```

## 유형 시스템 진화
```
1.0:  Optionals, generics, protocols
2.0:  Protocol extensions, protocol composition
4.0:  Codable, associated type constraints
5.1:  Opaque types (some), property wrappers
5.9:  Macros, parameter packs (variadic generics)
6.0:  Typed throws, strict Sendable
```

## 다른 플랫폼의 Swift
```
2015: Swift open-sourced (Apache 2.0)
2015: Swift on Linux (Ubuntu)
2016: Swift on ARM (Raspberry Pi)
2017: Swift on Windows (experimental)
2019: TensorFlow Swift (later discontinued)
2020: Swift on AWS Lambda
2021: Vapor (server-side Swift framework)
2023: Swift on embedded systems (embedded Swift)
2025: Swift — cross-platform systems language
```

## 신속한 진화 과정
```
SE-0001 (2015): First proposal
Over 400 proposals accepted by 2025
Key proposals:
  SE-0044: Import as member
  SE-0110: Distributed actors
  SE-0295: Codable improvements
  SE-0302: Sendable and @Sendable closures
  SE-0335: Introduce existential any
  SE-0346: Lightweight same-type requirements (some)
  SE-0401: Remove Actor Isolation Inference
  SE-0413: Typed throws
```

## 생태계 성장
```
2014: Swift announced — replaces Objective-C
2015: Open source; Swift Package Manager
2016: Swift 3 — API redesign
2017: Swift 4 — Codable
2019: Swift 5 — ABI stability
2021: SwiftUI matures
2023: Swift 5.9 — macros
2025: Swift 6 — data race safety; used in iOS, macOS, server, embedded
```
