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

# Fortran — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
| Fortran I | 1957 | **第一种高级语言**（John Backus，IBM）|
| Fortran II | 1958 |子程序、函数 |
| Fortran IV | 1962 |  `DATA`、`EQUIVALENCE`、`COMMON` |
| FORTRAN 66 | 语言1966 | **第一个 ANSI 标准** (X3.4-1966) |
| FORTRAN 77 | 语言1977 | **结构化编程**：`IF`/`THEN`/`ELSE`、`CHARACTER`、列表定向 I/O |
| Fortran 90 | 语言1991 | **主要**：自由格式源、模块、数组、`ALLOCATABLE`、`SELECT CASE` |
| Fortran 95 | 语言1997 |  `FORALL`、`WHERE`、纯/元素程序 |
| Fortran 2003 | 2004 | **OOP**：类、继承、多态性、`PROCEDURE` 指针、`IEEE` 算术 |
| Fortran 2008 | 2010 | **Coarrays**（并行编程）、`SUBMODULE`、`DO CONCURRENT` |
| Fortran 2018 | 2018 | **增强型协同阵列**、`ASSOCIATE`、`TYPE IS` 改进 |
| Fortran 2023 | 2024 | 2024 **`BLOCK`**、`ALLOCATE` 改进、`SELECT RANK` 、无符号整数 |
## 主要里程碑
### Fortran I–IV：高级编程的诞生（1957–1965）
- **1957**：John Backus 和 IBM 团队创建了 Fortran（公式翻译）
- **第一种广泛使用的高级编程语言**
- **Fortran I**：引入了`DO`循环、`IF`、`GO TO`、算术表达式
- **Fortran II (1958)**：子例程和函数（单独编译）
- **Fortran IV (1962)**：`DATA`、`EQUIVALENCE`、`COMMON`块
- 固定格式源：第 1-6 列用于标签，第 7-72 列用于代码
### FORTRAN 66 & 77：标准化（1966–1990）
- **FORTRAN 66**：第一个 ANSI 标准 — 可移植的 Fortran
- **FORTRAN 77 (1977)**：经典
  - 结构化编程：`IF` /`THEN`/`ELSE`/`ENDIF`
  -`CHARACTER`类型（字符串处理）
  - 列表定向 I/O（`*` 格式）
  - `PARAMETER`（命名常量）
  - `ENTRY`（多个入口点）
  - 仍然广泛应用于科学计算
### Fortran 90：现代革命 (1991)
- **自由格式源** — 不再有列限制
- **模块** — 封装，`USE` 
- **动态数组** —`ALLOCATABLE`、`ALLOCATE`
- **数组操作** — 整个数组语法`a = b + c`
-`SELECT CASE`— 结构化分支
-`IMPLICIT NONE`— 需要变量声明
- 递归过程
- 指针
- 运算符重载
- 派生类型（结构）
### Fortran 95–2003：OOP 到来（1997–2004）
- **Fortran 95**：`FORALL`、`WHERE`、纯/元素程序
- **Fortran 2003**：**完整的 OOP**
  - 类（具有类型绑定过程的派生类型）
  - 继承（`EXTENDS`）
  - 多态性（`CLASS`，`SELECT TYPE`）
  - 程序指针
  - IEEE浮点控制
  - `FLUSH`声明
  -`NEWUNIT`用于 I/O
### Fortran 2008–2023：并行和现代（2010 年至今）
- **Fortran 2008**：**Coarrays** — 语言内置的并行编程
  -`DO CONCURRENT`— 并行循环构造
  -`SUBMODULE`— 模块化编程
  -`CONTIGUOUS`属性
- **Fortran 2018**：增强的协同阵列、`ASSOCIATE` 改进、团队
- **Fortran 2023**：`BLOCK` 构造改进、`ALLOCATE` 增强、`SELECT RANK` 、无符号整数
## 语法演变
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

## 功能演变
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

## 关键设计原则
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## 生态系统增长
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
