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
# Fortran - Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| Fortrán I | 1957 | **Primer lenguaje de alto nivel** (John Backus, IBM) |
| Fortrán II | 1958 | Subrutinas, funciones |
| Fortrán IV | 1962 |  `DATA`, `EQUIVALENCE`,`COMMON`|
| FORTRAN 66 | 1966 | **Primer estándar ANSI** (X3.4-1966) |
| FORTRAN 77 | 1977 | **Programación estructurada**:`IF`/`THEN`/`ELSE`,`CHARACTER`, E/S dirigidas por lista |
| Fortran 90 | 1991 | **Principal**: fuente de formato libre, módulos, matrices, `ALLOCATABLE`,`SELECT CASE`|
| Fortran 95 | 1997 |  `FORALL`, `WHERE`, procedimientos puros/elementales |
| Fortrán 2003 | 2004 | **OOP**: clases, herencia, polimorfismo, punteros `PROCEDURE`, aritmética`IEEE`|
| Fortrán 2008 | 2010 | **Coarrays** (programación paralela), `SUBMODULE`,`DO CONCURRENT`|
| Fortrán 2018 | 2018 | **Coarrays mejorados**, mejoras en `ASSOCIATE`,`TYPE IS`|
| Fortrán 2023 | 2024 | **`BLOCK`**, mejoras `ALLOCATE`, `SELECT RANK`, enteros sin signo |
## Hitos importantes
### Fortran I–IV: El nacimiento de la programación de alto nivel (1957–1965)
- **1957**: John Backus y el equipo de IBM crean Fortran (Traducción de fórmulas)
- **El primer lenguaje de programación de alto nivel ampliamente utilizado**
- **Fortran I**: Se introdujeron bucles `DO`, `IF`, `GO TO`, expresiones aritméticas.
- **Fortran II (1958)**: Subrutinas y funciones (compilación separada)
- **Fortran IV (1962)**: bloques `DATA`, `EQUIVALENCE`, `COMMON`
- Fuente de formato fijo: columnas 1-6 para etiquetas, 7-72 para código
### FORTRAN 66 y 77: estandarización (1966-1990)
- **FORTRAN 66**: primer estándar ANSI: Fortran portátil
- **FORTRAN 77 (1977)**: El clásico
  - Programación estructurada:`IF`/`THEN`/`ELSE`/`ENDIF`
  - Tipo`CHARACTER`(manejo de cadenas)
  - E/S dirigida por lista (formato `*`)
  -`PARAMETER`(constantes con nombre)
  -`ENTRY`(múltiples puntos de entrada)
  - Todavía se utiliza ampliamente en informática científica.
### Fortran 90: La revolución moderna (1991)
- **Fuente de formato libre**: no más restricciones de columnas
- **Módulos** — encapsulación,`USE`
- **Matrices dinámicas** — `ALLOCATABLE`,`ALLOCATE`
- **Operaciones de matriz** — sintaxis de matriz completa`a = b + c`
-`SELECT CASE`— ramificación estructurada
- `IMPLICIT NONE`: requiere declaraciones de variables
- Procedimientos recursivos
- Punteros
- Sobrecarga del operador
- Tipos derivados (estructuras)
### Fortran 95–2003: llega la programación orientada a objetos (1997–2004)
- **Fortran 95**: `FORALL`, `WHERE`, procedimientos puros/elementales
- **Fortran 2003**: **POO completo**
  - Clases (tipos derivados con procedimientos vinculados a tipos)
  - Herencia (`EXTENDS`)
  - Polimorfismo (`CLASS`, `SELECT TYPE`)
  - Consejos de procedimiento
  - Control de punto flotante IEEE
  - Declaración `FLUSH`
  -`NEWUNIT`para E/S
### Fortran 2008–2023: paralelo y moderno (2010-presente)
- **Fortran 2008**: **Coarrays**: programación paralela integrada en el lenguaje
  -`DO CONCURRENT`— construcción de bucle paralelo
  -`SUBMODULE`— programación modular
  - Atributo `CONTIGUOUS`
- **Fortran 2018**: Coarrays mejorados, mejoras `ASSOCIATE`, equipos
- **Fortran 2023**: mejoras en la construcción `BLOCK`, mejoras en `ALLOCATE`, `SELECT RANK`, enteros sin signo
## Evolución de la sintaxis
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

## Evolución de funciones
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

## Principios clave de diseño
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## Crecimiento del ecosistema
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
