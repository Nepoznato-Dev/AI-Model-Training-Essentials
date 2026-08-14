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
# Fortran — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| Fortran I | 1957 | **İlk üst düzey dil** (John Backus, IBM) |
| Fortran II | 1958 | Alt programlar, işlevler |
| Fortran IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| FORTRAN 66 | 1966 | **İlk ANSI standardı** (X3.4-1966) |
| FORTRAN 77 | 1977 | **Yapılandırılmış programlama**:`IF`/`THEN`/ `ELSE`, `CHARACTER`, listeye yönelik G/Ç |
| Fortran 90 | 1991 | **Ana**: serbest biçimli kaynak, modüller, diziler,`ALLOCATABLE`,`SELECT CASE`|
| Fortran 95 | 1997 | `FORALL`,`WHERE`, saf/elementel prosedürler |
| Fortran 2003 | 2004 | **OOP**: sınıflar, kalıtım, polimorfizm,`PROCEDURE`işaretçileri,`IEEE`aritmetiği |
| Fortran 2008 | 2010 | **Coarray'ler** (paralel programlama),`SUBMODULE`,`DO CONCURRENT`|
| Fortran 2018 | 2018 | **Geliştirilmiş coarray'ler**, `ASSOCIATE`,`TYPE IS`iyileştirmeleri |
| Fortran 2023 | 2024 | **`BLOCK`**,`ALLOCATE`iyileştirmeleri, `SELECT RANK`, işaretsiz tamsayılar |
## Önemli Kilometre Taşları
### Fortran I–IV: Yüksek Düzey Programlamanın Doğuşu (1957–1965)
- **1957**: John Backus ve IBM ekibi Fortran'ı (Formül Çevirisi) yarattı
- **Yaygın olarak kullanılan ilk yüksek seviye programlama dili**
- **Fortran I**:`DO`döngüleri, `IF`, `GO TO`, aritmetik ifadeler tanıtıldı
- **Fortran II (1958)**: Alt programlar ve işlevler (ayrı derleme)
- **Fortran IV (1962)**:`DATA`,`EQUIVALENCE`,`COMMON`blokları
- Sabit biçimli kaynak: etiketler için 1-6 sütunları, kod için 7-72 sütunları
### FORTRAN 66 ve 77: Standardizasyon (1966–1990)
- **FORTRAN 66**: İlk ANSI standardı — taşınabilir Fortran
- **FORTRAN 77 (1977)**: Klasik
  - Yapılandırılmış programlama:`IF`/`THEN`/`ELSE`/`ENDIF`
  -`CHARACTER`türü (dize işleme)
  - Listeye yönelik G/Ç (`*` formatı)
  -`PARAMETER`(adlandırılmış sabitler)
  -`ENTRY`(çoklu giriş noktası)
  - Halen bilimsel hesaplamalarda yaygın olarak kullanılmaktadır
### Fortran 90: Modern Devrim (1991)
- **Serbest biçimli kaynak** — artık sütun kısıtlaması yok
- **Modüller** — kapsülleme,`USE`
- **Dinamik diziler** —`ALLOCATABLE`,`ALLOCATE`
- **Dizi işlemleri** — tüm dizi sözdizimi`a = b + c`
-`SELECT CASE`— yapılandırılmış dallanma
-`IMPLICIT NONE`— değişken bildirimleri gerektirir
- Yinelemeli prosedürler
- İşaretçiler
- Operatör aşırı yüklemesi
- Türetilmiş türler (yapılar)
### Fortran 95–2003: OOP Geldi (1997–2004)
- **Fortran 95**: `FORALL`, `WHERE`, saf/elemental prosedürler
- **Fortran 2003**: **Tam OOP**
  - Sınıflar (türe bağlı prosedürlerle türetilmiş türler)
  - Miras (`EXTENDS`)
  - Polimorfizm (`CLASS`,`SELECT TYPE`)
  - Prosedür işaretçileri
  - IEEE kayan nokta kontrolü
  -`FLUSH`bildirimi
  - G/Ç için `NEWUNIT`
### Fortran 2008–2023: Paralel ve Modern (2010 – günümüz)
- **Fortran 2008**: **Coarrays** — dilde yerleşik paralel programlama
  -`DO CONCURRENT`— paralel döngü yapısı
  -`SUBMODULE`— modüler programlama
  -`CONTIGUOUS`özelliği
- **Fortran 2018**: Geliştirilmiş ortak diziler,`ASSOCIATE`iyileştirmeleri, ekipler
- **Fortran 2023**:`BLOCK`yapı iyileştirmeleri,`ALLOCATE`iyileştirmeleri, `SELECT RANK`, işaretsiz tamsayılar
## Söz Dizimi Gelişimi
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

## Özellik Gelişimi
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

## Temel Tasarım İlkeleri
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## Ekosistem Büyümesi
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
