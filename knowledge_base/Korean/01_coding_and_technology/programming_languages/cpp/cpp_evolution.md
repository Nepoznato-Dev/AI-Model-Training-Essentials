<!--
---
# Metadata
title: "C++ — Version History & Evolution"
description: "Comprehensive version history and evolution of C++ from C with Classes to C++26."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [cpp, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# C++ — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 정면 | 1983년 | "C with Classes" — 클래스, 상속 |
| C++98 | 1998 | 최초의 ISO 표준; STL, 템플릿, 예외 |
| C++03 | 2003년 | 결함 수정 |
| C++11 | 2011 | **주요**: 이동 의미 체계, 람다, `auto`, 스마트 포인터,`nullptr`|
| C++14 | 2014 | 일반 람다,`auto`반환,`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, 구조화된 바인딩 |
| C++20 | 2020 | **주요**: 개념, 범위, 코루틴, 모듈, `std::span`, 3방향 비교 |
| C++23 | 2024년 | `std::expected`,`std::print`,`std::flat_map`,`this`추론 |
| C++26 | ~2026 | `std::execution`, 반영(예상), 계약 |
## 주요 이정표
### 표준 이전 시대(1983~1998)
- **1983**: Bjarne Stroustrup이 Bell Labs에서 "C with Classes"를 만듭니다.
- **1985**: C++로 이름이 변경되었습니다. "C++ 프로그래밍 언어" 초판
- **1989**: 템플릿, 예외, 네임스페이스 제안
- **1990**: Alexander Stepanov의 STL(표준 템플릿 라이브러리)
- **1991**: 템플릿 표준화; "주석이 달린 C++ 참조 매뉴얼"
### C++98 — 재단(1998)
- 클래스, 상속, 가상 함수
- 템플릿(함수, 클래스, 전문화)
- STL:`vector`,`map`,`set`,`algorithm`,`iterator`
- 예외(`try/catch/throw`)
-`namespace`,`bool`,`const_cast`,`dynamic_cast`
-`explicit`생성자,`mutable`멤버
- RTTI (`typeid`,`dynamic_cast`)
### C++11 — 르네상스(2011)
- **이동 의미**:`&&`rvalue 참조,`std::move`
- **스마트 포인터**:`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`**: 유형 추론
- **`nullptr`**: `NULL`를 대체합니다. 
- **람다**:`[](int x) { return x * 2; }`
- **범위**:`for (auto& x : container)`
- **`constexpr`**: 컴파일 타임 계산
- **`static_assert`**: 컴파일 타임 어설션
- **`using`**: 유형 별칭(`typedef`대체)
- **가변 템플릿**:`template<typename... Args>`
- **`enum class`**: 강력한 형식의 열거형
- **`override`/`final`**: 가상 기능 제어
- **`std::thread`**: 기본 스레딩
- **`std::atomic`**: 잠금 없는 프로그래밍
- **`std::function`/`std::bind`**: 일급 기능
### C++17 — 개선(2017)
- `std::optional<T>`, `std::variant<T...>`,`std::any`
-`if constexpr`— 컴파일 타임 분기
- 구조화된 바인딩:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- 병렬 알고리즘:`std::execution::par`
- 중첩된 네임스페이스:`namespace A::B::C {}`
- `[[nodiscard]]`, `[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — 현대 언어(2020)
- **개념**:`template<std::integral T>`— 제한된 템플릿
- **범위**:`views::filter`,`views::transform`— 지연 파이프라인
- **코루틴**:`co_await`,`co_yield`,`co_return`
- **모듈**:`import`/`export`— 더 빠른 컴파일
- **`std::span`**: 연속 데이터의 비소유 뷰
- **3자 비교**: `<=>`(우주선 운영자)
- **`std::format`**: Python 스타일 형식
- **`consteval`/`constinit`**: 컴파일 타임 적용
- **지정된 초기화 프로그램**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: 중지 토큰이 있는 자동 조인 스레드
### C++23 — 실용적인 개선(2024)
-`std::expected<T, E>`— Rust에서 영감을 받은 오류 처리
-`std::print`/`std::println`— 빠른 형식의 출력
- `std::flat_map`,`std::flat_set`
-`this`추론 — 명시적 객체 매개변수
-`std::mdspan`— 다차원 범위
-`std::generator`— 동기 발전기
-`#include <debugging>`— 중단점, 덤프
## 핵심 패턴의 진화
```
Memory Management:
  1998: Raw pointers, manual new/delete
  2011: Smart pointers (unique_ptr, shared_ptr)
  2020: std::span, views (zero-copy abstractions)
  2023: std::expected (error without exceptions)

Error Handling:
  1998: Exceptions (try/catch)
  2011: noexcept, error codes
  2023: std::expected (Rust-inspired)
  2026: Contracts (expected)

Concurrency:
  1998: None (OS threads)
  2011: std::thread, std::mutex, std::atomic
  2017: Parallel algorithms
  2020: Coroutines, std::jthread

Abstraction:
  1998: Templates (unconstrained)
  2011: Move semantics, perfect forwarding
  2020: Concepts (constrained templates)
```

## 표준 프로세스
```
1998: C++98 (ISO/IEC 14882:1998)
2003: C++03 (defect fixes)
2011: C++11 — "modern C++" begins
2014: C++14 — incremental
2017: C++17 — incremental
2020: C++20 — another revolution
2024: C++23 — practical improvements
2026: C++26 — reflection, contracts (expected)

3-year release cycle since C++11
```

## 생태계 영향
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
