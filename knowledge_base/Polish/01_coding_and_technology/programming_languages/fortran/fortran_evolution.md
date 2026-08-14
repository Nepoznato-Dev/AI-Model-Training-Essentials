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
# Fortran — historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| Fortran I | 1957 | **Pierwszy język wysokiego poziomu** (John Backus, IBM) |
| Fortran II | 1958 | Podprogramy, funkcje |
| Fortran IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| FORTRAN 66 | 1966 | **Pierwszy standard ANSI** (X3.4-1966) |
| FORTRAN 77 | 1977 | **Programowanie strukturalne**:`IF`/`THEN`/`ELSE`,`CHARACTER`, we/wy kierowane na listę |
| Fortran 90 | 1991 | **Główne**: źródła dowolne, moduły, tablice,`ALLOCATABLE`,`SELECT CASE`|
| Fortran 95 | 1997 | `FORALL`,`WHERE`, procedury czyste/elementarne |
| Fortran 2003 | 2004 | **OOP**: klasy, dziedziczenie, polimorfizm, wskaźniki `PROCEDURE`, arytmetyka`IEEE`|
| Fortran 2008 | 2010 | **Wspólne tablice** (programowanie równoległe),`SUBMODULE`,`DO CONCURRENT`|
| Fortran 2018 | 2018 | **Ulepszone współrzędne**, ulepszenia `ASSOCIATE`,`TYPE IS`|
| Fortran 2023 | 2024 | **`BLOCK`**, ulepszenia `ALLOCATE`,`SELECT RANK`, liczby całkowite bez znaku |
## Główne kamienie milowe
### Fortran I–IV: Narodziny programowania wysokiego poziomu (1957–1965)
- **1957**: John Backus i zespół IBM tworzą Fortran (tłumaczenie formuł)
- **Pierwszy powszechnie używany język programowania wysokiego poziomu**
- **Fortran I**: Wprowadzono pętle `DO`,`IF`,`GO TO`, wyrażenia arytmetyczne
- **Fortran II (1958)**: Podprogramy i funkcje (osobna kompilacja)
- **Fortran IV (1962)**: bloki`DATA`,`EQUIVALENCE`, `COMMON`
- Źródło o ustalonej formie: kolumny 1-6 dla etykiet, 7-72 dla kodu
### FORTRAN 66 i 77: Standaryzacja (1966–1990)
- **FORTRAN 66**: Pierwszy standard ANSI — przenośny Fortran
- **FORTRAN 77 (1977)**: Klasyk
  - Programowanie strukturalne:`IF`/`THEN`/`ELSE`/`ENDIF`
  - typ`CHARACTER`(obsługa stringów)
  - We/wy kierowane na listę (format `*`)
  -`PARAMETER`(nazwane stałe)
  -`ENTRY`(wiele punktów wejścia)
  - Nadal szeroko stosowany w obliczeniach naukowych
### Fortran 90: Nowoczesna rewolucja (1991)
- **Źródło dowolne** — koniec z ograniczeniami dotyczącymi kolumn
- **Moduły** — enkapsulacja,`USE`
- **Tablice dynamiczne** —`ALLOCATABLE`,`ALLOCATE`
- **Operacje na tablicach** — składnia na całej tablicy`a = b + c`
-`SELECT CASE`— rozgałęzienie strukturalne
-`IMPLICIT NONE`— wymaga deklaracji zmiennych
- Procedury rekurencyjne
- Wskazówki
- Przeciążenie operatora
- Typy pochodne (struktury)
### Fortran 95–2003: Nadchodzi OOP (1997–2004)
- **Fortran 95**:`FORALL`,`WHERE`, procedury czyste/elementowe
- **Fortran 2003**: **Pełny OOP**
  - Klasy (typy pochodne z procedurami związanymi z typami)
  - Dziedziczenie (`EXTENDS`)
  - Polimorfizm (`CLASS`,`SELECT TYPE`)
  - Wskazówki proceduralne
  - Sterowanie zmiennoprzecinkowe IEEE
  - Wyciąg `FLUSH`
  -`NEWUNIT`dla wejść/wyjść
### Fortran 2008–2023: równoległy i nowoczesny (2010 – obecnie)
- **Fortran 2008**: **Coarrays** — programowanie równoległe wbudowane w język
  -`DO CONCURRENT`— konstrukcja pętli równoległej
  -`SUBMODULE`— programowanie modułowe
  - Atrybut `CONTIGUOUS`
- **Fortran 2018**: Ulepszone współrzędne, ulepszenia `ASSOCIATE`, zespoły
- **Fortran 2023**: ulepszenia konstrukcji `BLOCK`, ulepszenia `ALLOCATE`, `SELECT RANK`, liczby całkowite bez znaku
## Ewolucja składni
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

## Ewolucja funkcji
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

## Kluczowe zasady projektowania
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## Rozwój ekosystemu
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
