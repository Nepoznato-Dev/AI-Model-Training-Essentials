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
# Fortran — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| Fortran I | 1957 | **第一種高階語言**（John Backus，IBM）|
| Fortran II | 1958 |子程序、函數 |
| Fortran IV | 1962 | `DATA`、`EQUIVALENCE`、`COMMON` |
| FORTRAN 66 | 語言1966 | **第一個 ANSI 標準** (X3.4-1966) |
| FORTRAN 77 | 語言1977 | **結構化程式設計**：`IF`/`THEN`/`ELSE`、`CHARACTER`、列表定向 I/O |
| Fortran 90 | 語言1991 | **主要**：自由格式來源、模組、陣列、`ALLOCATABLE`、`SELECT CASE` |
| Fortran 95 | 語言1997 | `FORALL`、`WHERE`、純/元素程式 |
| Fortran 2003 | 2004 | **OOP**：類別、繼承、多態性、`PROCEDURE` 指標、`IEEE` 算術 |
| Fortran 2008 | 2010 | **Coarrays**（平行程式設計）、`SUBMODULE`、`DO CONCURRENT` |
| Fortran 2018 | 2018 | **增強型協同陣列**、`ASSOCIATE`、`TYPE IS` 改良 |
| Fortran 2023 | 2024 | 2024 **`BLOCK`**、`ALLOCATE` 改進、`SELECT RANK` 、無符號整數 |
## 主要里程碑
### Fortran I–IV：高階程式設計的誕生（1957–1965）
- **1957**：John Backus 和 IBM 團隊創建了 Fortran（公式翻譯）
- **第一種廣泛使用的高階程式語言**
- **Fortran I**：引入了`DO`循環、`IF`、`GO TO`、算術表達式
- **Fortran II (1958)**：子程式和函式（單獨編譯）
- **Fortran IV (1962)**：`DATA`、`EQUIVALENCE`、`COMMON`塊
- 固定格式來源：第 1-6 列用於標籤，第 7-72 列用於程式碼
### FORTRAN 66 & 77：標準化（1966–1990）
- **FORTRAN 66**：第一個 ANSI 標準 — 可移植的 Fortran
- **FORTRAN 77 (1977)**：經典
  - 結構化程式設計：`IF` /`THEN`/`ELSE`/ `ENDIF`
  -`CHARACTER`類型（字串處理）
  - 清單定向 I/O（`*` 格式）
  - `PARAMETER`（命名常數）
  - `ENTRY`（多個入口點）
  - 仍廣泛應用於科學計算
### Fortran 90：現代革命 (1991)
- **自由格式來源** — 不再有列限制
- **模組** — 封裝，`USE`
- **動態陣列** —`ALLOCATABLE`、 `ALLOCATE`
- **陣列操作** — 整個陣列語法 `a = b + c`
-`SELECT CASE`— 結構化分支
-`IMPLICIT NONE`— 需要變數聲明
- 遞迴過程
- 指針
- 運算子重載
- 派生類型（結構）
### Fortran 95–2003：OOP 到來（1997–2004）
- **Fortran 95**：`FORALL`、`WHERE`、純/元素程序
- **Fortran 2003**：**完整的 OOP**
  - 類別（具有類型綁定過程的衍生型別）
  - 繼承（`EXTENDS`）
  - 多態性（`CLASS`，`SELECT TYPE`）
  - 程式指針
  - IEEE浮點控制
  - `FLUSH`聲明
  -`NEWUNIT`用於 I/O
### Fortran 2008–2023：並行與現代（2010 年至今）
- **Fortran 2008**：**Coarrays** — 語言內建的平行編程
  -`DO CONCURRENT`— 平行循環構造
  -`SUBMODULE`— 模組化編程
  -`CONTIGUOUS`屬性
- **Fortran 2018**：增強的協同陣列、`ASSOCIATE` 改進、團隊
- **Fortran 2023**：`BLOCK` 構造改進、`ALLOCATE` 增強功能、`SELECT RANK` 、無符號整數
## 語法演變
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

## 功能演變
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

## 關鍵設計原則
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## 生態系成長
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
