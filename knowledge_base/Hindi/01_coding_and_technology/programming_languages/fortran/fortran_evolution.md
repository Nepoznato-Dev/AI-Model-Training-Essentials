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
# फोरट्रान - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| फोरट्रान I | 1957 | **पहली उच्च स्तरीय भाषा** (जॉन बैकस, आईबीएम) |
| फोरट्रान द्वितीय | 1958 | सबरूटीन्स, कार्य |
| फोरट्रान IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| फोरट्रान 66 | 1966 | **पहला एएनएसआई मानक** (X3.4-1966) |
| फोरट्रान 77 | 1977 | **संरचित प्रोग्रामिंग**:`IF`/`THEN`/ `ELSE`, `CHARACTER`, सूची-निर्देशित I/O |
| फोरट्रान 90 | 1991 | **प्रमुख**: फ्री-फॉर्म स्रोत, मॉड्यूल, सरणियाँ,`ALLOCATABLE`,`SELECT CASE`|
| फोरट्रान 95 | 1997 | `FORALL`,`WHERE`, शुद्ध/मौलिक प्रक्रियाएं |
| फोरट्रान 2003 | 2004 | **OOP**: वर्ग, वंशानुक्रम, बहुरूपता,`PROCEDURE`सूचक,`IEEE`अंकगणित |
| फोरट्रान 2008 | 2010 | **Coarrays** (समानांतर प्रोग्रामिंग),`SUBMODULE`,`DO CONCURRENT`|
| फोरट्रान 2018 | 2018 | **उन्नत कोरएरे**,`ASSOCIATE`,`TYPE IS`सुधार |
| फोरट्रान 2023 | 2024 | **`BLOCK`**,`ALLOCATE`सुधार, `SELECT RANK`, अहस्ताक्षरित पूर्णांक |
## प्रमुख मील के पत्थर
### फोरट्रान I-IV: उच्च-स्तरीय प्रोग्रामिंग का जन्म (1957-1965)
- **1957**: आईबीएम में जॉन बैकस और टीम ने फोरट्रान (फॉर्मूला अनुवाद) बनाया
- **पहली व्यापक रूप से उपयोग की जाने वाली उच्च-स्तरीय प्रोग्रामिंग भाषा**
- **फोरट्रान I**:`DO`लूप, `IF`, `GO TO`, अंकगणितीय अभिव्यक्ति प्रस्तुत की गई
- **फोरट्रान II (1958)**: सबरूटीन्स और फ़ंक्शन (अलग संकलन)
- **फोरट्रान IV (1962)**: `DATA`, `EQUIVALENCE`,`COMMON`ब्लॉक
- निश्चित-फ़ॉर्म स्रोत: लेबल के लिए कॉलम 1-6, कोड के लिए 7-72
### फोरट्रान 66 और 77: मानकीकरण (1966-1990)
- **फोरट्रान 66**: पहला एएनएसआई मानक - पोर्टेबल फोरट्रान
- **फोरट्रान 77 (1977)**: क्लासिक
  - संरचित प्रोग्रामिंग:`IF`/`THEN`/`ELSE`/`ENDIF`
  -`CHARACTER`प्रकार (स्ट्रिंग हैंडलिंग)
  - सूची-निर्देशित I/O (`*` प्रारूप)
  -`PARAMETER`(नामित स्थिरांक)
  -`ENTRY`(एकाधिक प्रवेश बिंदु)
  - अभी भी वैज्ञानिक कंप्यूटिंग में व्यापक रूप से उपयोग किया जाता है
### फोरट्रान 90: आधुनिक क्रांति (1991)
- **फ्री-फॉर्म स्रोत** - अब कोई कॉलम प्रतिबंध नहीं
- **मॉड्यूल** - एनकैप्सुलेशन,`USE`
- **गतिशील सरणियाँ** —`ALLOCATABLE`,`ALLOCATE`
- **सरणी संचालन** - संपूर्ण-सरणी सिंटैक्स`a = b + c`
-`SELECT CASE`- संरचित शाखा
-`IMPLICIT NONE`- परिवर्तनीय घोषणाओं की आवश्यकता है
- पुनरावर्ती प्रक्रियाएं
- सूचक
- ऑपरेटर ओवरलोडिंग कर रहा है
- व्युत्पन्न प्रकार (structs)
### फोरट्रान 95-2003: ओओपी आगमन (1997-2004)
- **फोरट्रान 95**: `FORALL`, `WHERE`, शुद्ध/मौलिक प्रक्रियाएं
- **फोरट्रान 2003**: **पूर्ण ओओपी**
  - कक्षाएं (टाइप-बाउंड प्रक्रियाओं के साथ व्युत्पन्न प्रकार)
  - वंशानुक्रम (`EXTENDS`)
  - बहुरूपता (`CLASS`, `SELECT TYPE`)
  - प्रक्रिया सूचक
  - IEEE फ़्लोटिंग-पॉइंट नियंत्रण
  -`FLUSH`कथन
  - I/O के लिए `NEWUNIT`
### फोरट्रान 2008-2023: समानांतर और आधुनिक (2010-वर्तमान)
- **फोरट्रान 2008**: **कोएरेज़** — भाषा में निर्मित समानांतर प्रोग्रामिंग
  -`DO CONCURRENT`- समानांतर लूप निर्माण
  -`SUBMODULE`- मॉड्यूलर प्रोग्रामिंग
  -`CONTIGUOUS`विशेषता
- **फोरट्रान 2018**: उन्नत कोररेज़,`ASSOCIATE`सुधार, टीमें
- **फोरट्रान 2023**:`BLOCK`निर्माण सुधार,`ALLOCATE`संवर्द्धन, `SELECT RANK`, अहस्ताक्षरित पूर्णांक
## सिंटेक्स इवोल्यूशन
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

## फ़ीचर इवोल्यूशन
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

## मुख्य डिज़ाइन सिद्धांत
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## पारिस्थितिकी तंत्र का विकास
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
