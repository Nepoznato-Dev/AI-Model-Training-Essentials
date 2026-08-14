---
# Metadata
title: "C — Version History & Evolution"
description: "Comprehensive version history and evolution of C from K&R to C23."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [c, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# C — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| K&R C | 1972~78 | 오리지널 C(커니건 & 리치) |
| C89/C90 | 1989/90 | 최초의 ANSI/ISO 표준 |
| C95 | 1995 | 수정안 1:`wchar.h`, 이중 그래프 |
| C99 | 1999 | `//`주석,`inline`,`bool`, VLA, 지정된 이니셜라이저 |
| C11 | 2011 | 원자, 스레드, `_Static_assert`, 익명 구조체/공용체 |
| C17 | 2018 | 결함 수정(새로운 기능 없음) |
| C23 | 2024년 | `nullptr`,`typeof`,`constexpr`,`#embed`, 속성 |
## 주요 이정표
### K&R C(1972~1989)
- **1972**: Dennis Ritchie가 Bell Labs에서 Unix용 C를 만듭니다.
- **1978**: Kernighan & Ritchie가 "C 프로그래밍 언어" 출판
- 주요 기능:`struct`,`int`,`char`, 포인터, 기능,`#include`
-`void`없음,`enum`없음,`unsigned`없음,`const`없음
### C89/C90 - 표준(1989)
- 최초의 ANSI 표준(ANSI X3.159-1989)
- 추가됨:`void`,`enum`,`const`,`volatile`, 함수 프로토타입,`signed`
- "황금 시대" — 휴대 가능, 널리 채택됨
- 여전히 많은 임베디드 시스템의 기준선
### C99 — 모던 C(1999)
-`//`한줄 주석
-`inline`기능
- `<stdbool.h>`를 통한`bool`
- 가변 길이 배열(VLA)
- 지정 초기화 프로그램:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— 루프 선언
-`<stdint.h>`:`int32_t`,`uint64_t`등
-`restrict`키워드
- 가변 매크로
- 복합 리터럴
### C11 — 안전 및 동시성(2011)
-`<stdatomic.h>`— 원자적 연산
-`<threads.h>`— 스레드 지원
-`_Static_assert`— 컴파일 타임 어설션
- 중첩된 구조체의 익명 구조체/공용체
-`_Alignof`,`_Alignas`— 정렬 제어
- 일반 선택:`_Generic(x, int: ..., default: ...)`
- 유니코드 지원:`<uchar.h>`
- 선택적 VLA 지원(내재된 문제로 인해 선택적으로 만들어짐)
### C23 — 르네상스(2024)
-`nullptr`— 널 포인터 상수(`NULL` 매크로 대체)
-`typeof`— 유형 추론
-`constexpr`— 상수 표현식
-`#embed`— 컴파일 타임에 바이너리 데이터 포함
-`[[attribute]]`구문(C23 스타일 속성)
- 키워드로`true`/`false`(더 이상 `<stdbool.h>`가 필요하지 않음)
-`auto`유형 추론
-`static_assert`(밑줄 없음)
-`alignof`(밑줄 없음)
- 기본`int`반환이 제거되었습니다.
## 표준 프로세스
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## 호환성 철학
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## 전처리기의 진화
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## 유형 시스템 진화
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## 생태계 영향
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
