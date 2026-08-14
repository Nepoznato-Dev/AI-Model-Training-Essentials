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

# ফোর্টরান - সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| ফোরট্রান আই | 1957 | **প্রথম উচ্চ-স্তরের ভাষা** (জন ব্যাকাস, আইবিএম) |
| ফোরট্রান II | 1958 | সাবরুটিন, ফাংশন |
| ফোরট্রান IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| FORTRAN 66 | 1966 | **প্রথম ANSI মান** (X3.4-1966) |
| FORTRAN 77 | 1977 | **স্ট্রাকচার্ড প্রোগ্রামিং**:`IF`/`THEN`/`ELSE`,`CHARACTER`, তালিকা-নির্দেশিত I/O |
| ফোরট্রান 90 | 1991 | **মেজর**: ফ্রি-ফর্ম সোর্স, মডিউল, অ্যারে,`ALLOCATABLE`,`SELECT CASE`|
| ফোরট্রান 95 | 1997 | `FORALL`,`WHERE`, বিশুদ্ধ/মূল পদ্ধতি |
| ফোরট্রান 2003 | 2004 | **OOP**: ক্লাস, উত্তরাধিকার, পলিমারফিজম,`PROCEDURE`পয়েন্টার,`IEEE`পাটিগণিত |
| ফোরট্রান 2008 | 2010 | **কোয়ারে** (সমান্তরাল প্রোগ্রামিং),`SUBMODULE`,`DO CONCURRENT`|
| Fortran 2018 | 2018 | **বর্ধিত কোয়ারে**,`ASSOCIATE`,`TYPE IS`উন্নতি |
| ফোরট্রান 2023 | 2024 | **`BLOCK`**,`ALLOCATE`উন্নতি,`SELECT RANK`, স্বাক্ষরবিহীন পূর্ণসংখ্যা |
## প্রধান মাইলফলক
### ফোরট্রান I–IV: দ্য বার্থ অফ হাই-লেভেল প্রোগ্রামিং (1957-1965)
- **1957**: জন ব্যাকাস এবং আইবিএম-এর দল ফোরট্রান তৈরি করেছে (ফর্মুলা অনুবাদ)
- **প্রথম ব্যাপকভাবে ব্যবহৃত উচ্চ-স্তরের প্রোগ্রামিং ভাষা**
- **Fortran I**:`DO`লুপ, `IF`, `GO TO`, গাণিতিক অভিব্যক্তি প্রবর্তন করা হয়েছে
- **ফোরট্রান II (1958)**: সাবরুটিন এবং ফাংশন (পৃথক সংকলন)
- **ফোরট্রান IV (1962): `DATA`, `EQUIVALENCE`,`COMMON`ব্লক
- ফিক্সড-ফর্ম সোর্স: লেবেলের জন্য কলাম 1-6, কোডের জন্য 7-72
### FORTRAN 66 এবং 77: স্ট্যান্ডার্ডাইজেশন (1966-1990)
- **ফোরট্রান 66**: প্রথম ANSI স্ট্যান্ডার্ড — পোর্টেবল ফোরট্রান
- **ফোরট্রান 77 (1977): দ্য ক্লাসিক
  - স্ট্রাকচার্ড প্রোগ্রামিং:`IF`/`THEN`/`ELSE`/`ENDIF`
  -`CHARACTER`প্রকার (স্ট্রিং হ্যান্ডলিং)
  - তালিকা-নির্দেশিত I/O (`*`বিন্যাস)
  -`PARAMETER`(নামকৃত ধ্রুবক)
  -`ENTRY`(একাধিক এন্ট্রি পয়েন্ট)
  - এখনও বৈজ্ঞানিক কম্পিউটিং ব্যাপকভাবে ব্যবহৃত
### Fortran 90: The Modern Revolution (1991)
- **ফ্রি-ফর্ম সোর্স** — আর কোন কলাম সীমাবদ্ধতা নেই
- **মডিউল** — এনক্যাপসুলেশন,`USE`
- **ডাইনামিক অ্যারে** —`ALLOCATABLE`,`ALLOCATE`
- **অ্যারে অপারেশন** — পুরো-অ্যারে সিনট্যাক্স`a = b + c`
-`SELECT CASE`— কাঠামোগত শাখা
-`IMPLICIT NONE`— পরিবর্তনশীল ঘোষণার প্রয়োজন
- পুনরাবৃত্তিমূলক পদ্ধতি
- পয়েন্টার
- অপারেটর ওভারলোডিং
- প্রাপ্ত প্রকার (স্ট্রাকট)
### Fortran 95-2003: OOP এরাইভস (1997-2004)
- **ফরট্রান 95**: `FORALL`, `WHERE`, বিশুদ্ধ/মূল পদ্ধতি
- **Fortran 2003**: **Full OOP**
  - ক্লাস (টাইপ-বাউন্ড পদ্ধতি সহ প্রাপ্ত প্রকার)
  - উত্তরাধিকার (`EXTENDS`)
  - পলিমরফিজম (`CLASS`,`SELECT TYPE`)
  - পদ্ধতি পয়েন্টার
  - IEEE ফ্লোটিং-পয়েন্ট কন্ট্রোল
  -`FLUSH`বিবৃতি
  - I/O এর জন্য `NEWUNIT`
### ফোর্টরান 2008-2023: সমান্তরাল এবং আধুনিক (2010-বর্তমান)
- **Fortran 2008**: **Coarrays** — ভাষার মধ্যে নির্মিত সমান্তরাল প্রোগ্রামিং
  -`DO CONCURRENT`— সমান্তরাল লুপ নির্মাণ
  -`SUBMODULE`— মডুলার প্রোগ্রামিং
  -`CONTIGUOUS`অ্যাট্রিবিউট
- **Fortran 2018**: উন্নত কোরে,`ASSOCIATE`উন্নতি, দলগুলি
- **Fortran 2023**:`BLOCK`নির্মাণের উন্নতি,`ALLOCATE`বর্ধিতকরণ,`SELECT RANK`, স্বাক্ষরবিহীন পূর্ণসংখ্যা
## সিনট্যাক্স বিবর্তন
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

## বৈশিষ্ট্য বিবর্তন
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

## মূল ডিজাইনের নীতি
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## ইকোসিস্টেম বৃদ্ধি
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
