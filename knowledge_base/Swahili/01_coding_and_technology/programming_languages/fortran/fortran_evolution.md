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
# Fortran - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| Fortran I | 1957 | **Lugha ya kwanza ya kiwango cha juu** (John Backus, IBM) |
| Fortran II | 1958 | Subroutines, kazi |
| Fortran IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| FORTRAN 66 | 1966 | **Kiwango cha kwanza cha ANSI** (X3.4-1966) |
| FORTRAN 77 | 1977 | **Utengenezaji wa programu**:`IF`/`THEN`/`ELSE`,`CHARACTER`, iliyoelekezwa kwenye orodha I/O |
| Fortran 90 | 1991 | **Meja**: chanzo cha umbo lisilolipishwa, moduli, safu,`ALLOCATABLE`,`SELECT CASE`|
| Fortran 95 | 1997 | `FORALL`,`WHERE`, taratibu safi/kimsingi |
| Fortran 2003 | 2004 | **OOP**: madarasa, urithi, upolimishaji, viashiria vya `PROCEDURE`, hesabu ya`IEEE`|
| Fortran 2008 | 2010 | **Mipangilio ya safu** (programu sambamba),`SUBMODULE`,`DO CONCURRENT`|
| Fortran 2018 | 2018 | **Nuru zilizoimarishwa**,`ASSOCIATE`,`TYPE IS`maboresho |
| Fortran 2023 | 2024 | **`BLOCK`**,`ALLOCATE`maboresho,`SELECT RANK`, nambari kamili ambazo hazijasainiwa |
## Mafanikio Makuu
### Fortran I–IV: Kuzaliwa kwa Utayarishaji wa Kiwango cha Juu (1957–1965)
- **1957**: John Backus na timu katika IBM wanaunda Fortran (Tafsiri ya Mfumo)
- **Lugha ya programu ya kiwango cha juu inayotumiwa sana**
- **Fortran I**: Imeanzisha vitanzi vya `DO`,`IF`,`GO TO`, vielezi vya hesabu
- **Fortran II (1958)**: Njia ndogo na utendaji (mkusanyiko tofauti)
- **Fortran IV (1962)**:`DATA`,`EQUIVALENCE`,`COMMON`vitalu
- Chanzo cha fomu isiyobadilika: safu wima 1-6 za lebo, 7-72 za msimbo
### FORTRAN 66 & 77: Kusawazisha (1966–1990)
- **FORTRAN 66**: Kiwango cha kwanza cha ANSI - Fortran inayobebeka
- **FORTRAN 77 (1977)**: Ya classic
  - Utengenezaji wa programu:`IF`/`THEN`/`ELSE`/`ENDIF`
  -`CHARACTER`aina (ushughulikiaji wa kamba)
  - I/O iliyoelekezwa kwenye orodha (umbizo la `*`)
 `PARAMETER`(viunga vilivyopewa jina)
  -`ENTRY`(viingilio vingi)
  - Bado inatumika sana katika kompyuta ya kisayansi
### Fortran 90: Mapinduzi ya Kisasa (1991)
- **Chanzo cha fomu isiyolipishwa** - hakuna vizuizi zaidi vya safu wima
- **Moduli ** - encapsulation,`USE`
- **Safu zenye nguvu** —`ALLOCATABLE`,`ALLOCATE`
- **Operesheni za mkusanyiko** — sintaksia ya safu nzima`a = b + c`
-`SELECT CASE`- muundo wa matawi
-`IMPLICIT NONE`- zinahitaji matamko tofauti
- Taratibu za kujirudia
- Viashiria
- Opereta inapakia kupita kiasi
- Aina zinazotokana (miundo)
### Fortran 95–2003: OOP Inawasili (1997–2004)
- **Fortran 95**:`FORALL`,`WHERE`, taratibu safi/msingi
- **Fortran 2003**: **OOP Kamili**
  - Madarasa (aina zinazotokana na taratibu zilizofungwa na aina)
  - Urithi (`EXTENDS`)
  - Polymorphism (`CLASS`,`SELECT TYPE`)
  - Viashiria vya utaratibu
  - Udhibiti wa uhakika wa IEEE
  - Taarifa ya `FLUSH`
  -`NEWUNIT`kwa I/O
### Fortran 2008–2023: Parallel & Modern (2010–sasa)
- **Fortran 2008**: **Coarrays** — programu sambamba iliyojengwa katika lugha
  -`DO CONCURRENT`- ujenzi wa kitanzi sambamba
  -`SUBMODULE`- upangaji wa kawaida
  - Sifa ya `CONTIGUOUS`
- **Fortran 2018**: safu zilizoimarishwa, maboresho ya `ASSOCIATE`, timu
- **Fortran 2023**:`BLOCK`kujenga maboresho,`ALLOCATE`maboresho,`SELECT RANK`, nambari kamili ambazo hazijasainiwa
## Mageuzi ya Sintaksia
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

## Mageuzi ya Kipengele
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

## Kanuni Muhimu za Usanifu
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## Ukuaji wa Mfumo ikolojia
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
