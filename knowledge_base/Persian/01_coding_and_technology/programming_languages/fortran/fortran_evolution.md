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

# Fortran - تاریخچه نسخه و تکامل
## جدول زمانی
| نسخه | سال | تم کلید |
|---------|------|-----------|
| فرترن I | 1957 | **اولین زبان سطح بالا** (John Backus، IBM) |
| Fortran II | 1958 | زیربرنامه ها، توابع |
| Fortran IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| FORTRAN 66 | 1966 | **اولین استاندارد ANSI** (X3.4-1966) |
| FORTRAN 77 | 1977 | **برنامه نویسی ساختاریافته**:`IF`/`THEN`/`ELSE`,`CHARACTER`, I/O با فهرست |
| فرترن 90 | 1991 | **عمده**: منبع فرم آزاد، ماژول ها، آرایه ها، `ALLOCATABLE`،`SELECT CASE`|
| فرترن 95 | 1997 |  `FORALL`، `WHERE`، رویه های خالص/عنصری |
| Fortran 2003 | 2004 | **OOP**: کلاس ها، وراثت، چندشکلی، نشانگرهای `PROCEDURE`، محاسبات`IEEE`|
| Fortran 2008 | 2010 | **Coarrays** (برنامه نویسی موازی),`SUBMODULE`,`DO CONCURRENT`|
| Fortran 2018 | 2018 | **همتراشه های پیشرفته**، بهبودهای `ASSOCIATE`،`TYPE IS`|
| Fortran 2023 | 2024 | **`BLOCK`**، بهبودهای `ALLOCATE`، `SELECT RANK`، اعداد صحیح بدون علامت |
## نقاط عطف اصلی
### فرترن I–IV: تولد برنامه‌نویسی سطح بالا (1957–1965)
- **1957**: جان بکوس و تیم IBM Fortran (ترجمه فرمول) را ایجاد کردند.
- **اولین زبان برنامه نویسی سطح بالا پرکاربرد**
- **Fortran I**: حلقه های `DO`، `IF`، `GO TO`، عبارات حسابی را معرفی کرد
- **فرترن II (1958)**: زیربرنامه ها و توابع (تلفیق جداگانه)
- **Fortran IV (1962)**: بلوک های `DATA`، `EQUIVALENCE`، `COMMON`
- منبع فرم ثابت: ستون های 1-6 برای برچسب ها، 7-72 برای کد
### فرترن 66 و 77: استانداردسازی (1966-1990)
- **FORTRAN 66**: اولین استاندارد ANSI — Fortran قابل حمل
- **FORTRAN 77 (1977)**: کلاسیک
  - برنامه نویسی ساختاریافته:`IF`/`THEN`/`ELSE`/`ENDIF`
  - نوع`CHARACTER`(دستکاری رشته)
  - ورودی/خروجی با فهرست (فرمت `*`)
  -`PARAMETER`(ثابت نامگذاری شده)
  -`ENTRY`(نقاط ورودی چندگانه)
  - هنوز به طور گسترده در محاسبات علمی استفاده می شود
### فرترن 90: انقلاب مدرن (1991)
- ** منبع فرم آزاد ** - بدون محدودیت ستون
- **ماژول** - کپسوله سازی،`USE`
- **آرایه های پویا** — `ALLOCATABLE`،`ALLOCATE`
- **عملیات آرایه** - نحو کل آرایه`a = b + c`
-`SELECT CASE`- انشعاب ساختاری
-`IMPLICIT NONE`- به اعلان های متغیر نیاز دارد
- رویه های بازگشتی
- اشاره گر
- بارگذاری بیش از حد اپراتور
- انواع مشتق شده (ساختارها)
### Fortran 95–2003: OOP Arrives (1997–2004)
- **فرترن 95**: `FORALL`، `WHERE`، رویه های خالص/عنصری
- **Fortran 2003**: **Full OOP**
  - کلاس ها (انواع مشتق شده با رویه های نوع محدود)
  - وراثت (`EXTENDS`)
  - چند شکلی (`CLASS`، `SELECT TYPE`)
  - نشانگرهای رویه
  - کنترل ممیز شناور IEEE
  - بیانیه `FLUSH`
  -`NEWUNIT`برای I/O
### فرترن 2008–2023: موازی و مدرن (2010–اکنون)
- **Fortran 2008**: **Coarrays** - برنامه نویسی موازی ساخته شده در زبان
  -`DO CONCURRENT`- ساختار حلقه موازی
  -`SUBMODULE`- برنامه نویسی ماژولار
  - ویژگی `CONTIGUOUS`
- **Fortran 2018**: همبستگی های پیشرفته، بهبودهای `ASSOCIATE`، تیم ها
- **Fortran 2023**: بهبودهای ساختار `BLOCK`، بهبودهای `ALLOCATE`، `SELECT RANK`، اعداد صحیح بدون علامت
## تکامل نحو
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

## تکامل ویژگی
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

## اصول کلیدی طراحی
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## رشد اکوسیستم
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
