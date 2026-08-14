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
# Fortran: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| Fortran I | 1957 | **Primo linguaggio di alto livello** (John Backus, IBM) |
| Fortran II | 1958 | Sottoprogrammi, funzioni |
| Fortran IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| FORTRAN66 | 1966 | **Primo standard ANSI** (X3.4-1966) |
| FORTRAN77 | 1977 | **Programmazione strutturata**:`IF`/`THEN`/`ELSE`,`CHARACTER`, I/O diretto da elenco |
| Fortran90 | 1991 | **Maggiore**: sorgente in formato libero, moduli, array,`ALLOCATABLE`,`SELECT CASE`|
| Fortran95 | 1997 | `FORALL`,`WHERE`, procedure pure/elementari |
| Fortran2003 | 2004| **OOP**: classi, ereditarietà, polimorfismo, puntatori `PROCEDURE`, aritmetica`IEEE`|
| Fortran2008 | 2010| **Coarray** (programmazione parallela),`SUBMODULE`,`DO CONCURRENT`|
| Fortran 2018 | 2018 | **Coarray migliorati**, miglioramenti `ASSOCIATE`,`TYPE IS`|
| Fortran 2023 | 2024 | **`BLOCK`**, miglioramenti `ALLOCATE`,`SELECT RANK`, interi senza segno |
## Traguardi importanti
### Fortran I–IV: la nascita della programmazione di alto livello (1957–1965)
- **1957**: John Backus e il team dell'IBM creano Fortran (Traduzione di formule)
- **Il primo linguaggio di programmazione di alto livello ampiamente utilizzato**
- **Fortran I**: introdotti cicli `DO`,`IF`,`GO TO`, espressioni aritmetiche
- **Fortran II (1958)**: Subroutine e funzioni (compilazione separata)
- **Fortran IV (1962)**: blocchi`DATA`,`EQUIVALENCE`, `COMMON`
- Sorgente in formato fisso: colonne 1-6 per etichette, 7-72 per codice
### FORTRAN 66 e 77: Standardizzazione (1966–1990)
- **FORTRAN 66**: primo standard ANSI: Fortran portatile
- **FORTRAN 77 (1977)**: Il classico
  - Programmazione strutturata:`IF`/`THEN`/`ELSE`/`ENDIF`
  - Tipo`CHARACTER`(gestione delle stringhe)
  - I/O diretto da elenco (formato `*`)
  -`PARAMETER`(costanti denominate)
  -`ENTRY`(punti di ingresso multipli)
  - Ancora ampiamente utilizzato nel calcolo scientifico
### Fortran 90: La rivoluzione moderna (1991)
- **Sorgente in formato libero**: niente più restrizioni sulle colonne
- **Moduli**: incapsulamento,`USE`
- **Array dinamici** —`ALLOCATABLE`,`ALLOCATE`
- **Operazioni sugli array**: sintassi dell'intero array`a = b + c`
- `SELECT CASE`: ramificazione strutturata
- `IMPLICIT NONE`: richiede dichiarazioni di variabili
- Procedure ricorsive
- Puntatori
- Sovraccarico degli operatori
- Tipi derivati (strutture)
### Fortran 95–2003: arriva l'OOP (1997–2004)
- **Fortran 95**:`FORALL`,`WHERE`, procedure pure/elementari
- **Fortran 2003**: **OOP completo**
  - Classi (tipi derivati con procedure legate al tipo)
  - Ereditarietà (`EXTENDS`)
  - Polimorfismo (`CLASS`,`SELECT TYPE`)
  - Puntatori alla procedura
  - Controllo in virgola mobile IEEE
  - Dichiarazione `FLUSH`
  -`NEWUNIT`per I/O
### Fortran 2008–2023: Parallelo e moderno (2010-oggi)
- **Fortran 2008**: **Coarrays** — programmazione parallela integrata nel linguaggio
  - `DO CONCURRENT`: costrutto ad anello parallelo
  -`SUBMODULE`— programmazione modulare
  - Attributo `CONTIGUOUS`
- **Fortran 2018**: coarray migliorati, miglioramenti `ASSOCIATE`, team
- **Fortran 2023**: miglioramenti al costrutto `BLOCK`, miglioramenti `ALLOCATE`,`SELECT RANK`, numeri interi senza segno
## Evoluzione della sintassi
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

## Evoluzione delle funzionalità
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

## Principi chiave di progettazione
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## Crescita dell'ecosistema
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
