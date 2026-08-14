---
# Metadata
title: "Fortran — Version History & Evolution"
description: "Comprehensive version history and evolution of Fortran from Fortran I to modern Fortran."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Фортран — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| Фортран I | 1957 | **Первый язык высокого уровня** (Джон Бэкус, IBM) |
| Фортран II | 1958 | Подпрограммы, функции |
| Фортран IV | 1962 |  `DATA`, `EQUIVALENCE`,`COMMON`|
| ФОРТРАН 66 | 1966 | **Первый стандарт ANSI** (X3.4-1966) |
| ФОРТРАН 77 | 1977 | **Структурное программирование**:`IF`/`THEN`/`ELSE`,`CHARACTER`, ввод-вывод по списку |
| Фортран 90 | 1991 | **Основные**: исходный код в свободной форме, модули, массивы,`ALLOCATABLE`,`SELECT CASE`|
| Фортран 95 | 1997 | `FORALL`,`WHERE`, чистые/элементарные процедуры |
| Фортран 2003 | 2004 | **ООП**: классы, наследование, полиморфизм, указатели `PROCEDURE`, арифметика`IEEE`|
| Фортран 2008 | 2010 | **Coarrays** (параллельное программирование),`SUBMODULE`,`DO CONCURRENT`|
| Фортран 2018 | 2018 | **Улучшенные массивы**, улучшения `ASSOCIATE`,`TYPE IS`|
| Фортран 2023 | 2024 | **`BLOCK`**, улучшения `ALLOCATE`,`SELECT RANK`, целые числа без знака |
## Основные вехи
### Фортран I–IV: рождение высокоуровневого программирования (1957–1965)
- **1957**: Джон Бэкус и команда IBM создают Fortran (перевод формул).
- **Первый широко используемый язык программирования высокого уровня**
- **Фортран I**: добавлены циклы `DO`, `IF`, `GO TO`, арифметические выражения.
- **Fortran II (1958)**: Подпрограммы и функции (отдельная компиляция)
- **Фортран IV (1962 г.)**: блоки `DATA`, `EQUIVALENCE`, `COMMON`.
- Источник фиксированной формы: столбцы 1–6 для меток, 7–72 для кода.
### ФОРТРАН 66 и 77: Стандартизация (1966–1990)
- **ФОРТРАН 66**: первый стандарт ANSI — портативный Фортран.
- **ФОРТРАН 77 (1977)**: Классика
  - Структурное программирование:`IF`/`THEN`/`ELSE`/`ENDIF`
  - Тип`CHARACTER`(обработка строк)
  - Ввод-вывод, управляемый списком (формат `*`)
  -`PARAMETER`(именные константы)
  -`ENTRY`(несколько точек входа)
  - До сих пор широко используется в научных вычислениях
### Фортран 90: Современная революция (1991)
- **Источник в произвольной форме** – ограничений по столбцам больше нет.
- **Модули** — инкапсуляция,`USE`
- **Динамические массивы** —`ALLOCATABLE`,`ALLOCATE`
- **Операции с массивами** — синтаксис для всего массива`a = b + c`
-`SELECT CASE`— структурированное ветвление
-`IMPLICIT NONE`— требует объявления переменных
- Рекурсивные процедуры
- Указатели
- Перегрузка оператора
- Производные типы (структуры)
### Фортран 95–2003: появление ООП (1997–2004)
- **Фортран 95**:`FORALL`,`WHERE`, чистые/элементарные процедуры.
- **Фортран 2003**: **Полное ООП**
  - Классы (производные типы с процедурами, привязанными к типу)
  - Наследование (`EXTENDS`)
  - Полиморфизм (`CLASS`,`SELECT TYPE`)
  - Указатели процедур
  - IEEE-управление с плавающей запятой
  - Оператор `FLUSH`
  -`NEWUNIT`для ввода-вывода
### Фортран 2008–2023: Параллельный и современный (2010 – настоящее время)
- **Fortran 2008**: **Coarrays** — параллельное программирование, встроенное в язык.
  -`DO CONCURRENT`— конструкция параллельного цикла.
  -`SUBMODULE`— модульное программирование
  - Атрибут `CONTIGUOUS`
- **Fortran 2018**: улучшенные массивы, улучшения `ASSOCIATE`, команды.
- **Fortran 2023**: улучшения конструкции `BLOCK`, улучшения `ALLOCATE`, `SELECT RANK`, целые числа без знака.
## Эволюция синтаксиса
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

## Эволюция функций
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

## Ключевые принципы проектирования
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## Рост экосистемы
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
