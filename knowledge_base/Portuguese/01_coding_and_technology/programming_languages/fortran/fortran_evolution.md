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
# Fortran — Histórico e evolução da versão
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| Fortran I | 1957 | **Primeira linguagem de alto nível** (John Backus, IBM) |
| Fortran II | 1958 | Subrotinas, funções |
| Fortran IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| FORTRAN 66 | 1966 | **Primeiro padrão ANSI** (X3.4-1966) |
| FORTRAN 77 | 1977 | **Programação estruturada**:`IF`/`THEN`/`ELSE`,`CHARACTER`, E/S direcionada a lista |
| Fortran 90 | 1991 | **Principal**: fonte de formato livre, módulos, matrizes,`ALLOCATABLE`,`SELECT CASE`|
| Fortran 95 | 1997 | `FORALL`,`WHERE`, procedimentos puros/elementares |
| Fortran 2003 | 2004 | **OOP**: classes, herança, polimorfismo, ponteiros `PROCEDURE`, aritmética`IEEE`|
| Fortran 2008 | 2010 | **Coarrays** (programação paralela),`SUBMODULE`,`DO CONCURRENT`|
| Fortran 2018 | 2018 | **Coarrays aprimorados**, melhorias em`ASSOCIATE`e`TYPE IS`|
| Fortran 2023 | 2024 | **`BLOCK`**, melhorias em `ALLOCATE`,`SELECT RANK`, inteiros sem sinal |
## Marcos importantes
### Fortran I–IV: O nascimento da programação de alto nível (1957–1965)
- **1957**: John Backus e equipe da IBM criam Fortran (Formula Translation)
- **A primeira linguagem de programação de alto nível amplamente utilizada**
- **Fortran I**: introduzidos loops `DO`,`IF`,`GO TO`, expressões aritméticas
- **Fortran II (1958)**: Sub-rotinas e funções (compilação separada)
- **Fortran IV (1962)**: blocos `DATA`, `EQUIVALENCE`, `COMMON`
- Fonte de formato fixo: colunas 1 a 6 para rótulos, 7 a 72 para código
### FORTRAN 66 e 77: Padronização (1966–1990)
- **FORTRAN 66**: Primeiro padrão ANSI — Fortran portátil
- **FORTRAN 77 (1977)**: O clássico
  - Programação estruturada:`IF`/`THEN`/`ELSE`/`ENDIF`
  - Tipo`CHARACTER`(manipulação de string)
  - E/S direcionada a lista (formato `*`)
  -`PARAMETER`(constantes nomeadas)
  -`ENTRY`(múltiplos pontos de entrada)
  - Ainda amplamente utilizado em computação científica
### Fortran 90: A Revolução Moderna (1991)
- **Fonte de formato livre** — sem mais restrições de coluna
- **Módulos** — encapsulamento,`USE`
- **Matrizes dinâmicas** —`ALLOCATABLE`,`ALLOCATE`
- **Operações de array** — sintaxe de array completo`a = b + c`
-`SELECT CASE`— ramificação estruturada
-`IMPLICIT NONE`— requer declarações de variáveis
- Procedimentos recursivos
- Ponteiros
- Sobrecarga do operador
- Tipos derivados (estruturas)
### Fortran 95–2003: OOP chega (1997–2004)
- **Fortran 95**:`FORALL`,`WHERE`, procedimentos puros/elementares
- **Fortran 2003**: **OOP completo**
  - Classes (tipos derivados com procedimentos vinculados ao tipo)
  - Herança (`EXTENDS`)
  - Polimorfismo (`CLASS`, `SELECT TYPE`)
  - Indicadores de procedimento
  - Controle de ponto flutuante IEEE
  - Instrução `FLUSH`
  -`NEWUNIT`para E/S
### Fortran 2008–2023: Paralelo e Moderno (2010–presente)
- **Fortran 2008**: **Coarrays** — programação paralela incorporada à linguagem
  -`DO CONCURRENT`— construção de loop paralelo
  -`SUBMODULE`— programação modular
  - Atributo `CONTIGUOUS`
- **Fortran 2018**: coarrays aprimorados, melhorias `ASSOCIATE`, equipes
- **Fortran 2023**: melhorias de construção `BLOCK`, melhorias `ALLOCATE`, `SELECT RANK`, números inteiros não assinados
## Evolução da Sintaxe
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

## Evolução de recursos
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

## Princípios-chave de design
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## Crescimento do Ecossistema
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
