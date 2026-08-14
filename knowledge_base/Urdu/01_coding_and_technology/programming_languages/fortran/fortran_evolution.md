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
# فورٹران - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| فورٹران I | 1957 | **پہلی اعلیٰ سطحی زبان** (جان بیکس، IBM) |
| فورٹران II | 1958 | سبروٹینز، فنکشنز |
| فورٹران IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| فورٹران 66 | 1966 | **پہلا ANSI معیار** (X3.4-1966) |
| فورٹران 77 | 1977 | **سٹرکچرڈ پروگرامنگ**:`IF`/`THEN`/`ELSE`,`CHARACTER`, فہرست سے ہدایت شدہ I/O |
| فورٹران 90 | 1991 | **میجر**: فری فارم سورس، ماڈیولز، اری،`ALLOCATABLE`,`SELECT CASE`|
| فورٹران 95 | 1997 | `FORALL`,`WHERE`, خالص / بنیادی طریقہ کار |
| فورٹران 2003 | 2004 | **OOP**: کلاسز، وراثت، پولیمورفزم،`PROCEDURE`پوائنٹرز،`IEEE`ریاضی |
| فورٹران 2008 | 2010 | **Coarrays** (متوازی پروگرامنگ)،`SUBMODULE`,`DO CONCURRENT`|
| فورٹران 2018 | 2018 | **بڑھا ہوا coarrays**, `ASSOCIATE`,`TYPE IS`بہتری |
| فورٹران 2023 | 2024 | **`BLOCK`**،`ALLOCATE`بہتری، `SELECT RANK`، غیر دستخط شدہ عدد |
## اہم سنگ میل
### فورٹران I–IV: دی برتھ آف ہائی لیول پروگرامنگ (1957–1965)
- **1957**: IBM میں جان بیکس اور ٹیم نے فورٹران تخلیق کیا (فارمولہ ترجمہ)
- **پہلی وسیع پیمانے پر استعمال ہونے والی اعلیٰ سطحی پروگرامنگ زبان**
- **فورٹران I**: متعارف کروائے گئے`DO`لوپس، `IF`، `GO TO`، ریاضی کے تاثرات
- **فورٹران II (1958)**: سب روٹینز اور فنکشنز (علیحدہ تالیف)
- **فورٹران IV (1962)**: `DATA`، `EQUIVALENCE`،`COMMON`بلاکس
- فکسڈ فارم سورس: لیبلز کے لیے کالم 1-6، کوڈ کے لیے 7-72
### فورٹران 66 اور 77: معیاری کاری (1966-1990)
- **فورٹران 66**: پہلا ANSI معیار - پورٹیبل فورٹران
- **فورٹران 77 (1977): کلاسک
  - سٹرکچرڈ پروگرامنگ:`IF`/`THEN`/`ELSE`/`ENDIF`
  -`CHARACTER`قسم (سٹرنگ ہینڈلنگ)
  - فہرست سے ہدایت شدہ I/O (`*`فارمیٹ)
  -`PARAMETER`(نام مستقل)
  -`ENTRY`(متعدد اندراج پوائنٹس)
  - سائنسی کمپیوٹنگ میں اب بھی وسیع پیمانے پر استعمال کیا جاتا ہے۔
### فورٹران 90: جدید انقلاب (1991)
- **فری فارم سورس** — مزید کالم پابندیاں نہیں۔
- **ماڈیولز** — encapsulation،`USE`
- **متحرک صفوں** — `ALLOCATABLE`،`ALLOCATE`
- **ارے آپریشن** — پوری صف کا نحو`a = b + c`
-`SELECT CASE`— تشکیل شدہ برانچنگ
-`IMPLICIT NONE`- متغیر اعلانات کی ضرورت ہے۔
- تکراری طریقہ کار
- اشارے
- آپریٹر اوور لوڈنگ
- ماخوذ اقسام (سٹرکٹس)
### فورٹران 95–2003: او او پی آرائیوز (1997–2004)
- **فورٹران 95**: `FORALL`، `WHERE`، خالص/عنوی طریقہ کار
- **فورٹران 2003**: **مکمل او او پی**
  - کلاسز (قسم کے پابند طریقہ کار کے ساتھ اخذ کردہ اقسام)
  - وراثت (`EXTENDS`)
  - پولیمورفزم (`CLASS`,`SELECT TYPE`)
  - طریقہ کار کے اشارے
  - IEEE فلوٹنگ پوائنٹ کنٹرول
  -`FLUSH`بیان
  - I/O کے لیے `NEWUNIT`
### فورٹران 2008–2023: متوازی اور جدید (2010–موجودہ)
- **Fortran 2008**: **Coarrays** — متوازی پروگرامنگ جو زبان میں بنی ہوئی ہے
  -`DO CONCURRENT`- متوازی لوپ کی تعمیر
  -`SUBMODULE`- ماڈیولر پروگرامنگ
  -`CONTIGUOUS`وصف
- **فورٹران 2018**: بہتر کیری،`ASSOCIATE`بہتری، ٹیمیں
- **فورٹران 2023**:`BLOCK`تعمیراتی بہتری،`ALLOCATE`اضافہ، `SELECT RANK`، غیر دستخط شدہ عدد
## نحوی ارتقاء
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

## فیچر ارتقاء
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

## ڈیزائن کے کلیدی اصول
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## ماحولیاتی نظام کی نمو
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
