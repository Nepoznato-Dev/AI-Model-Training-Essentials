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

# فورتران — تاريخ الإصدار وتطوره
## الجدول الزمني
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| فورتران الأول | 1957 | **أول لغة عالية المستوى** (جون باكوس، IBM) |
| فورتران الثاني | 1958 | الإجراءات الفرعية والوظائف |
| فورتران الرابع | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| فورتران 66 | 1966 | **معيار ANSI الأول** (X3.4-1966) |
| فورتران 77 | 1977 | **برمجة منظمة**:`IF`/`THEN`/ `ELSE`، `CHARACTER`، الإدخال/الإخراج الموجه بالقائمة |
| فورتران 90 | 1991 | **التخصص**: المصدر الحر، الوحدات، المصفوفات،`ALLOCATABLE`،`SELECT CASE`|
| فورتران 95 | 1997 | `FORALL`,`WHERE`إجراءات نقية/عنصرية |
| فورتران 2003 | 2004 | **OOP**: الطبقات، الميراث، تعدد الأشكال، مؤشرات `PROCEDURE`، حساب`IEEE`|
| فورتران 2008 | 2010 | **المصفوفات المتعرجة** (البرمجة المتوازية),`SUBMODULE`,`DO CONCURRENT`|
| فورتران 2018 | 2018 | **المصفوفات المحسّنة**، تحسينات `ASSOCIATE`،`TYPE IS`|
| فورتران 2023 | 2024 | **`BLOCK`**، تحسينات `ALLOCATE`، `SELECT RANK`، الأعداد الصحيحة غير الموقعة |
## المعالم الرئيسية
### فورتران 1-4: ولادة البرمجة عالية المستوى (1957-1965)
- **1957**: قام جون باكوس وفريق IBM بإنشاء فورتران (ترجمة الصيغ)
- **أول لغة برمجة عالية المستوى مستخدمة على نطاق واسع**
- **Fortran I**: تقديم حلقات `DO`، و`IF`، و`GO TO`، والتعبيرات الحسابية
- **Fortran II (1958)**: الإجراءات الفرعية والوظائف (تجميع منفصل)
- **فورتران 4 (1962)**: كتل`DATA`و`EQUIVALENCE` و`COMMON`
- مصدر ذو نموذج ثابت: الأعمدة من 1 إلى 6 للتسميات، ومن 7 إلى 72 للتعليمات البرمجية
### فورتران 66 و77: التقييس (1966-1990)
- **FORTRAN 66**: معيار ANSI الأول — فورتران المحمول
- **فورتران 77 (1977)**: الكلاسيكية
  - البرمجة المنظمة:`IF`/`THEN`/`ELSE`/`ENDIF`
  - نوع`CHARACTER`(التعامل مع السلسلة)
  - الإدخال/الإخراج الموجه بالقائمة (تنسيق `*`)
  -`PARAMETER`(الثوابت المسماة)
  -`ENTRY`(نقاط دخول متعددة)
  - لا يزال يستخدم على نطاق واسع في الحوسبة العلمية
### فورتران 90: الثورة الحديثة (1991)
- **مصدر حر** — لا مزيد من قيود الأعمدة
- **الوحدات** — التغليف،`USE`
- **المصفوفات الديناميكية** —`ALLOCATABLE`,`ALLOCATE`
- **عمليات المصفوفة** — بناء جملة المصفوفة الكاملة`a = b + c`
-`SELECT CASE`— التفرع المنظم
-`IMPLICIT NONE`— تتطلب إعلانات متغيرة
- الإجراءات العودية
- المؤشرات
- التحميل الزائد على المشغل
- الأنواع المشتقة (البنيات)
### فورتران 95-2003: وصول OOP (1997-2004)
- **Fortran 95**:`FORALL`,`WHERE`, الإجراءات النقية/العنصرية
- **فورتران 2003**: **البرمجة المفتوحة الكاملة**
  - الفئات (الأنواع المشتقة مع الإجراءات المرتبطة بالنوع)
  - الميراث (`EXTENDS`)
  - تعدد الأشكال (`CLASS`,`SELECT TYPE`)
  - مؤشرات الإجراء
  - IEEE التحكم بالفاصلة العائمة
  - بيان `FLUSH`
  -`NEWUNIT`للإدخال/الإخراج
### فورتران 2008-2023: الموازي والحديث (2010 إلى الوقت الحاضر)
- **Fortran 2008**: **Coarrays** — برمجة متوازية مدمجة في اللغة
  -`DO CONCURRENT`— بناء حلقة متوازية
  -`SUBMODULE`— البرمجة المعيارية
  - سمة `CONTIGUOUS`
- **Fortran 2018**: المصفوفات المحسنة، وتحسينات `ASSOCIATE`، والفرق
- **Fortran 2023**: تحسينات بناء `BLOCK`، تحسينات `ALLOCATE`، `SELECT RANK`، الأعداد الصحيحة غير الموقعة
## تطور بناء الجملة
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

## تطور الميزة
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

## مبادئ التصميم الرئيسية
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## نمو النظام البيئي
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
