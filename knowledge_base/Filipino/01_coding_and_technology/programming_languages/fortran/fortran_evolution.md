<!--
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

-->
# Fortran — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| Fortran I | 1957 | **Unang mataas na antas ng wika** (John Backus, IBM) |
| Fortran II | 1958 | Mga subroutine, function |
| Fortran IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| FORTRAN 66 | 1966 | **Unang pamantayan ng ANSI** (X3.4-1966) |
| FORTRAN 77 | 1977 | **Structured programming**:`IF`/`THEN`/`ELSE`,`CHARACTER`, list-directed I/O |
| Fortran 90 | 1991 | **Major**: free-form source, modules, arrays,`ALLOCATABLE`,`SELECT CASE`|
| Fortran 95 | 1997 | `FORALL`,`WHERE`, dalisay/elemental na pamamaraan |
| Fortran 2003 | 2004 | **OOP**: mga klase, inheritance, polymorphism,`PROCEDURE`pointer,`IEEE`arithmetic |
| Fortran 2008 | 2010 | **Coarrays** (parallel programming),`SUBMODULE`,`DO CONCURRENT`|
| Fortran 2018 | 2018 | **Mga pinahusay na coarray**,`ASSOCIATE`,`TYPE IS`mga pagpapabuti |
| Fortran 2023 | 2024 | **`BLOCK`**,`ALLOCATE`mga pagpapabuti,`SELECT RANK`, unsigned integers |
## Mga Pangunahing Milestone
### Fortran I–IV: Ang Kapanganakan ng High-Level Programming (1957–1965)
- **1957**: Si John Backus at ang koponan sa IBM ay lumikha ng Fortran (Formula Translation)
- **Ang unang malawakang ginagamit na high-level na programming language**
- **Fortran I**: Ipinakilala ang`DO`loops,`IF`,`GO TO`, mga arithmetic expression
- **Fortran II (1958)**: Mga subroutine at function (hiwalay na compilation)
- **Fortran IV (1962)**:`DATA`,`EQUIVALENCE`,`COMMON`block
- Fixed-form source: column 1-6 para sa mga label, 7-72 para sa code
### FORTRAN 66 & 77: Standardisasyon (1966–1990)
- **FORTRAN 66**: Unang pamantayan ng ANSI — portable Fortran
- **FORTRAN 77 (1977)**: Ang classic
  - Structured programming:`IF`/`THEN`/`ELSE`/`ENDIF`
  - Uri ng`CHARACTER`(paghawak ng string)
  - I/O na nakadirekta sa listahan (`*`na format)
  -`PARAMETER`(pinangalanang mga constant)
  -`ENTRY`(maraming entry point)
  - Malawak pa ring ginagamit sa scientific computing
### Fortran 90: The Modern Revolution (1991)
- **Free-form source** — wala nang mga paghihigpit sa column
- **Mga Module** — encapsulation,`USE`
- **Dynamic na array** —`ALLOCATABLE`,`ALLOCATE`
- **Mga operasyon ng array** — whole-array syntax`a = b + c`
-`SELECT CASE`— structured branching
-`IMPLICIT NONE`— nangangailangan ng mga variable na deklarasyon
- Mga recursive na pamamaraan
- Mga payo
- Overloading ng operator
- Mga nagmula na uri (mga istruktura)
### Fortran 95–2003: Dumating ang OOP (1997–2004)
- **Fortran 95**:`FORALL`,`WHERE`, mga pure/elemental na pamamaraan
- **Fortran 2003**: **Buong OOP**
  - Mga klase (mga hinangong uri na may mga pamamaraang nakatali sa uri)
  - Pamana (`EXTENDS`)
  - Polymorphism (`CLASS`,`SELECT TYPE`)
  - Mga payo ng pamamaraan
  - IEEE floating-point control
  -`FLUSH`na pahayag
  -`NEWUNIT`para sa I/O
### Fortran 2008–2023: Parallel & Modern (2010–kasalukuyan)
- **Fortran 2008**: **Coarrays** — parallel programming na binuo sa wika
  -`DO CONCURRENT`— parallel loop construct
  -`SUBMODULE`— modular programming
  -`CONTIGUOUS`attribute
- **Fortran 2018**: Mga pinahusay na coarray, mga pagpapahusay ng `ASSOCIATE`, mga koponan
- **Fortran 2023**:`BLOCK`construct improvements,`ALLOCATE`enhancement,`SELECT RANK`, unsigned integers
## Syntax Evolution
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

## Ebolusyon ng Tampok
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

## Pangunahing Prinsipyo ng Disenyo
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## Paglago ng Ecosystem
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
