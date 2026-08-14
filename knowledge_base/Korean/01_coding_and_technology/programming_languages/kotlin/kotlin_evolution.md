---
# Metadata
title: "Kotlin — Version History & Evolution"
description: "Comprehensive version history and evolution of Kotlin from 1.0 to modern Kotlin."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [kotlin, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Kotlin — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 1.0 | 2016 | 첫 번째 안정 릴리스(JetBrains) |
| 1.1 | 2017 | 코루틴, 유형 별칭, 람다 구조 분해 |
| 1.2 | 2017 | 배열 확산,`lateinit`최상위 수준, 후행 쉼표 |
| 1.3 | 2018 | `inline class`,`contracts`(실험적) |
| 1.4 | 2020 |  `@JvmDefault`, Kotlin 인터페이스용 SAM 변환 |
| 1.5 | 2021 | `value class`,`OptIn`주석, 정규식 리터럴 |
| 1.6 | 2021 | `when`완전성,`Unit`반환 최적화 |
| 1.7 | 2022 | `enum`항목,`@JvmInline`값 클래스 |
| 1.8 | 2022 |  `@SubclassOptInRequired`, K2 컴파일러 미리보기 |
| 1.9 | 2023년 | **K2 컴파일러**,`@ConsistentCopyVisibility`,`data`개체 |
| 2.0 | 2024 | **K2 컴파일러 안정**, `@SubclassOptInRequired`, 스마트 캐스트 개선 |
| 2.1 | 2024 | `when`주제, 속성 위임 개선 |
| 2.2 | 2025 | (예상) K2 추가 개선 |
## 주요 이정표
### 시작(2011~2016)
- **2011**: JetBrains에서 Kotlin 발표(상트페테르부르크 근처 Kotlin Island의 이름을 따서 명명)
- **2012**: Kotlin 오픈소스
- **2016**: **Kotlin 1.0** — JVM 및 Android용 프로덕션 준비 완료
### Android 채택(2017~2019)
- **2017**: Google은 Google I/O에서 최고 수준의 Kotlin 지원을 발표했습니다.
- **1.1 (2017)**: **코루틴** — 경량 비동기 프로그래밍
- **1.2(2017)**: 멀티플랫폼 프로젝트(Kotlin/Native, Kotlin/JS)
- **1.3 (2018)**:`inline class`, 계약
### 성장 연도(2020~2023)
- **1.5 (2021)**:`value class`,`OptIn`주석, 부호 없는 정수 유형
- **1.7(2022)**:`enum`항목, K2 컴파일러 미리보기
- **1.9(2023)**: K2 컴파일러(새로운 프런트엔드, 30% 더 빠른 컴파일),`data`개체
### 최신 Kotlin(2024~현재)
- **2.0(2024)**: **K2 컴파일러 안정** — 주요 성능 개선, 더 나은 분석
- **2.1(2024)**:`when`강화, 속성 위임
## 코루틴 진화
```
1.1:  Experimental coroutines (suspend functions, launch, async)
1.2:  Coroutine builder improvements
1.3:  Coroutine scope, structured concurrency, Dispatchers
1.5:  Flow API (cold async streams), StateFlow, SharedFlow
1.6:  Flow improvements, structured concurrency enforcement
1.9:  Coroutine debugging improvements
2.0:  Stable coroutine API
```

## 멀티플랫폼의 진화
```
1.2:  Kotlin Multiplatform (experimental)
1.3:  Kotlin/Native (iOS support)
1.4:  expect/actual mechanism
1.5:  Hierarchical multiplatform structure
1.9:  K2 with multiplatform support
2.0:  Compose Multiplatform (Jetpack Compose on iOS)
```

## 언어 기능의 진화
```
Null Safety:
  1.0:  Nullable types (String?), safe calls (?.), Elvis (?:)
  1.5:  OptIn annotation for experimental APIs
  2.0:  Smart cast improvements

Pattern Matching:
  1.0:  when expression, is/as operators
  1.7:  when exhaustiveness checking
  2.1:  Enhanced when subjects

Data Classes:
  1.0:  data class (equals, hashCode, toString, copy, componentN)
  1.9:  data object
  2.0:  @ConsistentCopyVisibility

Value Classes:
  1.3:  inline class (experimental)
  1.5:  value class (renamed)
  1.7:  @JvmInline value class
```

## 다양한 플랫폼의 Kotlin
```
2016: Kotlin/JVM (Android, server)
2017: Kotlin/JS (JavaScript)
2017: Kotlin/Native (iOS, macOS, Linux, Windows)
2018: Kotlin Multiplatform Mobile (KMM)
2021: Compose Multiplatform (desktop)
2023: Compose Multiplatform (iOS)
2025: Kotlin — official Android language; used server-side, iOS, web, embedded
```

## 생태계 성장
```
2016: Kotlin 1.0 — JetBrains IDE plugin
2017: Google I/O — first-class Android support
2018: Android KTX, Spring Framework 5 Kotlin support
2019: Kotlin 1.3 — coroutines stable
2021: Kotlin 1.5 — multiplatform matures
2023: Kotlin 1.9 — K2 compiler
2024: Kotlin 2.0 — K2 stable, Compose Multiplatform
2025: Kotlin — top 15 most used language; dominant in Android
```

## 주요 디자인 원칙
```
1. Pragmatism — solve real problems
2. Conciseness — less boilerplate than Java
3. Safety — null safety at compile time
4. Interoperability — 100% Java compatible
5. Tooling — IntelliJ IDEA first-class support
6. Multiplatform — one language, many targets
```
