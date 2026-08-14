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
# Fortran — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| Fortran I | 1957 | **Premier langage de haut niveau** (John Backus, IBM) |
| Fortran II | 1958 | Sous-programmes, fonctions |
| Fortran IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| FORTRAN 66 | 1966 | **Première norme ANSI** (X3.4-1966) |
| FORTRAN77 | 1977 | **Programmation structurée** :`IF`/`THEN`/`ELSE`,`CHARACTER`, E/S dirigées par liste |
| Fortran 90 | 1991 | **Majeur** : source de forme libre, modules, tableaux,`ALLOCATABLE`,`SELECT CASE`|
| Fortran 95 | 1997 | `FORALL`,`WHERE`, procédures pures/élémentaires |
| Fortran2003 | 2004 | **POO** : classes, héritage, polymorphisme, pointeurs `PROCEDURE`, arithmétique`IEEE`|
| Fortran 2008 | 2010 | **Coarrays** (programmation parallèle),`SUBMODULE`,`DO CONCURRENT`|
| Fortran 2018 | 2018 | **Coarrays améliorés**, améliorations`ASSOCIATE`et`TYPE IS`|
| Fortran 2023 | 2024 | **`BLOCK`**, améliorations de `ALLOCATE`,`SELECT RANK`, entiers non signés |
## Étapes majeures
### Fortran I-IV : La naissance de la programmation de haut niveau (1957-1965)
- **1957** : John Backus et son équipe chez IBM créent Fortran (Formula Translation)
- **Le premier langage de programmation de haut niveau largement utilisé**
- **Fortran I** : introduction des boucles `DO`,`IF`,`GO TO`, expressions arithmétiques
- **Fortran II (1958)** : Sous-programmes et fonctions (compilation séparée)
- **Fortran IV (1962)** : blocs`DATA`,`EQUIVALENCE`, `COMMON`
- Source sous forme fixe : colonnes 1 à 6 pour les étiquettes, 7 à 72 pour le code
### FORTRAN 66 & 77 : Normalisation (1966-1990)
- **FORTRAN 66** : première norme ANSI — Fortran portable
- **FORTRAN 77 (1977)** : Le classique
  - Programmation structurée :`IF`/`THEN`/`ELSE`/`ENDIF`
  - Type`CHARACTER`(gestion des chaînes)
  - E/S dirigées par liste (format `*`)
  -`PARAMETER`(constantes nommées)
  -`ENTRY`(points d'entrée multiples)
  - Encore largement utilisé en calcul scientifique
### Fortran 90 : La révolution moderne (1991)
- **Source de forme libre** — plus de restrictions de colonnes
- **Modules** — encapsulation,`USE`
- **Tableaux dynamiques** —`ALLOCATABLE`,`ALLOCATE`
- **Opérations sur les tableaux** — syntaxe de tableau entier`a = b + c`
-`SELECT CASE`— branchement structuré
-`IMPLICIT NONE`— nécessite des déclarations de variables
- Procédures récursives
- Pointeurs
- Surcharge des opérateurs
- Types dérivés (structs)
### Fortran 95–2003 : la POO arrive (1997–2004)
- **Fortran 95** :`FORALL`,`WHERE`, procédures pures/élémentaires
- **Fortran 2003** : **POO complète**
  - Classes (types dérivés avec procédures liées au type)
  - Héritage (`EXTENDS`)
  - Polymorphisme (`CLASS`,`SELECT TYPE`)
  - Pointeurs de procédure
  - Contrôle à virgule flottante IEEE
  - Instruction `FLUSH`
  -`NEWUNIT`pour les E/S
### Fortran 2008-2023 : parallèle et moderne (2010-présent)
- **Fortran 2008** : **Coarrays** — programmation parallèle intégrée au langage
  -`DO CONCURRENT`— construction de boucle parallèle
  -`SUBMODULE`— programmation modulaire
  - Attribut `CONTIGUOUS`
- **Fortran 2018** : Coarrays améliorés, améliorations `ASSOCIATE`, équipes
- **Fortran 2023** : améliorations de la construction `BLOCK`, améliorations `ALLOCATE`, `SELECT RANK`, entiers non signés
## Évolution de la syntaxe
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

## Évolution des fonctionnalités
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

## Principes de conception clés
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## Croissance de l'écosystème
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
