---
# Metadata
title: "Fortran — Version History & Evolution"
description: "Comprehensive version history and evolution of Fortran from Fortran I to modern Fortran."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [fortran, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Fortran — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 포트란 I | 1957 | **최초의 고급 언어**(John Backus, IBM) |
| 포트란 II | 1958 | 서브루틴, 함수 |
| 포트란 IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| 포트란 66 | 1966 | **최초의 ANSI 표준**(X3.4-1966) |
| 포트란 77 | 1977 | **구조적 프로그래밍**:`IF`/`THEN`/`ELSE`,`CHARACTER`, 목록 지향 I/O |
| 포트란 90 | 1991 | **주요**: 자유 형식 소스, 모듈, 배열,`ALLOCATABLE`,`SELECT CASE`|
| 포트란 95 | 1997 | `FORALL`,`WHERE`, 순수/요소 프로시저 |
| 포트란 2003 | 2004년 | **OOP**: 클래스, 상속, 다형성,`PROCEDURE`포인터,`IEEE`산술 |
| 포트란 2008 | 2010 | **Coarrays** (병렬 프로그래밍),`SUBMODULE`,`DO CONCURRENT`|
| 포트란 2018 | 2018 | **향상된 공동 배열**,`ASSOCIATE`,`TYPE IS`개선 |
| 포트란 2023 | 2024 | **`BLOCK`**,`ALLOCATE`개선,`SELECT RANK`, 부호 없는 정수 |
## 주요 이정표
### 포트란 I~IV: 고급 프로그래밍의 탄생(1957~1965)
- **1957**: John Backus와 IBM 팀이 Fortran(공식 번역)을 만듭니다.
- **최초로 널리 사용되는 고급 프로그래밍 언어**
- **Fortran I**:`DO`루프,`IF`,`GO TO`, 산술 표현식 도입
- **Fortran II(1958)**: 서브루틴 및 함수(별도 컴파일)
- **포트란 IV(1962)**:`DATA`,`EQUIVALENCE`,`COMMON`블록
- 고정 형식 소스: 라벨의 경우 1~6열, 코드의 경우 7~72열
### FORTRAN 66 및 77: 표준화(1966~1990)
- **FORTRAN 66**: 최초의 ANSI 표준 — 휴대용 포트란
- **FORTRAN 77(1977)**: 고전
  - 구조적 프로그래밍:`IF`/`THEN`/`ELSE`/`ENDIF`
  -`CHARACTER`유형(문자열 처리)
  - 목록 지향 I/O(`*`형식)
  - `PARAMETER`(명명된 상수)
  - `ENTRY`(다중 진입점)
  - 여전히 과학 컴퓨팅에 널리 사용됨
### 포트란 90: 현대 혁명(1991)
- **자유 형식 소스** — 더 이상 열 제한이 없습니다.
- **모듈** — 캡슐화,`USE`
- **동적 배열** —`ALLOCATABLE`,`ALLOCATE`
- **배열 작업** — 전체 배열 구문`a = b + c`
-`SELECT CASE`— 구조화된 분기
-`IMPLICIT NONE`— 변수 선언이 필요합니다.
- 재귀 프로시저
- 포인터
- 연산자 과부하
- 파생 유형(구조체)
### 포트란 95–2003: OOP 도착(1997–2004)
- **Fortran 95**:`FORALL`,`WHERE`, 순수/요소 프로시저
- **포트란 2003**: **전체 OOP**
  - 클래스(유형 바인딩 프로시저가 있는 파생 유형)
  - 상속(`EXTENDS`)
  - 다형성 (`CLASS`,`SELECT TYPE`)
  - 절차 지침
  - IEEE 부동 소수점 제어
  -`FLUSH`문
  - I/O용 `NEWUNIT`
### Fortran 2008–2023: 병렬 및 현대(2010–현재)
- **Fortran 2008**: **Coarrays** — 언어에 내장된 병렬 프로그래밍
  -`DO CONCURRENT`— 병렬 루프 구성
  -`SUBMODULE`— 모듈형 프로그래밍
  -`CONTIGUOUS`속성
- **Fortran 2018**: 향상된 공동 배열,`ASSOCIATE`개선, 팀
- **Fortran 2023**:`BLOCK`구성 개선,`ALLOCATE`개선,`SELECT RANK`, 부호 없는 정수
## 구문 진화
```fortran
C     FORTRAN 77: Fixed-form, structured programming
      PROGRAM HELLO
      INTEGER I
      DO 10 I = 1, 10
         PRINT *, 'Iteration: ', I
   10 CONTINUE
      END

! Fortran 90: Free-form, modules, arrays
program hello
  implicit none
  integer :: i
  real, dimension(10) :: values
  do i = 1, 10
    values(i) = real(i) * 2.0
  end do
  print *, sum(values)
end program hello

! Fortran 90: Array operations (no loops needed!)
program array_ops
  implicit none
  real :: a(100), b(100), c(100)
  a = [(real(i), i=1,100)]  ! array constructor
  b = sin(a)
  c = a + b                  ! whole-array operation
  print *, sum(c)
end program array_ops

! Fortran 2003: Object-oriented
module shapes
  implicit none
  type :: shape
    character(len=20) :: name
  contains
    procedure :: area => shape_area
  end type

  type, extends(shape) :: circle
    real :: radius
  contains
    procedure :: area => circle_area
  end type
contains
  function shape_area(self) result(a)
    class(shape), intent(in) :: self
    real :: a
    a = 0.0
  end function
  function circle_area(self) result(a)
    class(circle), intent(in) :: self
    real :: a
    a = 3.14159 * self%radius**2
  end function
end module

! Fortran 2008: Coarrays (parallel)
program parallel_example
  implicit none
  real :: data[*]  ! coarray — one element per image
  data = real(this_image())  ! each image gets its number
  sync all
  if (this_image() == 1) then
    print *, 'Image 2 has:', data[2]
  end if
end program

! Fortran 2008: DO CONCURRENT
program concurrent_loop
  implicit none
  real :: a(1000)
  integer :: i
  do concurrent (i = 1:1000)
    a(i) = sin(real(i)) * cos(real(i))
  end do
end program
```

## 기능 진화
```
Fortran I (1957):   DO loops, IF, GO TO, arithmetic expressions
Fortran II (1958):  Subroutines, functions
Fortran IV (1962):  DATA, EQUIVALENCE, COMMON
FORTRAN 66 (1966):  First standard
FORTRAN 77 (1977):  IF/THEN/ELSE, CHARACTER, list-directed I/O
Fortran 90 (1991):  Free-form, modules, arrays, ALLOCATABLE, SELECT CASE
Fortran 95 (1997):  FORALL, WHERE, pure/elemental
Fortran 2003 (2004): OOP, IEEE arithmetic, procedure pointers
Fortran 2008 (2010): Coarrays, DO CONCURRENT, SUBMODULE
Fortran 2018 (2018): Enhanced coarrays, teams
Fortran 2023 (2024): BLOCK, SELECT RANK, unsigned integers
```

## 주요 디자인 원칙
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## 생태계 성장
```
1957: Fortran I — first high-level language (IBM 704)
1966: FORTRAN 66 — first standard
1977: FORTRAN 77 — the classic (still used in legacy code)
1991: Fortran 90 — modern Fortran begins
2003: Fortran 2003 — OOP
2008: Fortran 2008 — parallel programming (coarrays)
2018: Fortran 2018 — enhanced parallelism
2024: Fortran 2023 — continued modernization
2025: Fortran powers:
       - Weather/climate modeling (WRF, CESM)
       - Computational fluid dynamics
       - Quantum chemistry (Gaussian, GAMESS)
       - Nuclear physics simulations
       - Financial modeling (legacy systems)
       Compilers: gfortran, ifx (Intel), nvfortran (NVIDIA), flang
```
