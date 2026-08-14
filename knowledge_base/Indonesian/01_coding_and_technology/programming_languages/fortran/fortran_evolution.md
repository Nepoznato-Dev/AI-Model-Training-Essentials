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

# Fortran — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| Fortran I | 1957 | **Bahasa tingkat tinggi pertama** (John Backus, IBM) |
| Fortran II | 1958 | Subrutin, fungsi |
| Fortran IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| FORTRAN 66 | 1966 | **Standar ANSI pertama** (X3.4-1966) |
| FORTRAN 77 | 1977 | **Pemrograman terstruktur**:`IF`/`THEN`/`ELSE`,`CHARACTER`, I/O terarah daftar |
| Fortran 90 | 1991 | **Mayor**: sumber bentuk bebas, modul, array,`ALLOCATABLE`,`SELECT CASE`|
| Fortran 95 | 1997 | `FORALL`,`WHERE`, prosedur murni/elemen |
| Fortran 2003 | 2004 | **OOP**: kelas, pewarisan, polimorfisme, pointer `PROCEDURE`, aritmatika`IEEE`|
| Fortran 2008 | 2010 | **Coarrays** (pemrograman paralel),`SUBMODULE`,`DO CONCURRENT`|
| Benteng 2018 | 2018 | **Coarray yang ditingkatkan**, penyempurnaan`ASSOCIATE`,`TYPE IS`|
| Fortran 2023 | 2024 | **`BLOCK`**, peningkatan `ALLOCATE`,`SELECT RANK`, bilangan bulat tak bertanda |
## Tonggak Penting
### Fortran I–IV: Lahirnya Pemrograman Tingkat Tinggi (1957–1965)
- **1957**: John Backus dan tim di IBM membuat Fortran (Terjemahan Formula)
- **Bahasa pemrograman tingkat tinggi pertama yang banyak digunakan**
- **Fortran I**: Memperkenalkan loop `DO`,`IF`,`GO TO`, ekspresi aritmatika
- **Fortran II (1958)**: Subrutin dan fungsi (kompilasi terpisah)
- **Fortran IV (1962)**: blok`DATA`,`EQUIVALENCE`, `COMMON`
- Sumber bentuk tetap: kolom 1-6 untuk label, 7-72 untuk kode
### FORTRAN 66 & 77: Standardisasi (1966–1990)
- **FORTRAN 66**: Standar ANSI pertama — Fortran portabel
- **FORTRAN 77 (1977)**: Klasik
  - Pemrograman terstruktur:`IF`/`THEN`/`ELSE`/`ENDIF`
  - Tipe`CHARACTER`(penanganan string)
  - I/O terarah daftar (format `*`)
  -`PARAMETER`(bernama konstanta)
  -`ENTRY`(beberapa titik masuk)
  - Masih banyak digunakan dalam komputasi ilmiah
### Fortran 90: Revolusi Modern (1991)
- **Sumber bentuk bebas** — tidak ada lagi batasan kolom
- **Modul** — enkapsulasi,`USE`
- **Array dinamis** —`ALLOCATABLE`,`ALLOCATE`
- **Operasi array** — sintaks seluruh array`a = b + c`
-`SELECT CASE`— percabangan terstruktur
-`IMPLICIT NONE`— memerlukan deklarasi variabel
- Prosedur rekursif
- Petunjuk
- Operator kelebihan beban
- Tipe turunan (struct)
### Fortran 95–2003: OOP Tiba (1997–2004)
- **Fortran 95**:`FORALL`,`WHERE`, prosedur murni/elemen
- **Fortran 2003**: **OOP Penuh**
  - Kelas (tipe turunan dengan prosedur terikat tipe)
  - Warisan (`EXTENDS`)
  - Polimorfisme (`CLASS`,`SELECT TYPE`)
  - Petunjuk prosedur
  - Kontrol titik mengambang IEEE
  - Pernyataan `FLUSH`
  -`NEWUNIT`untuk I/O
### Fortran 2008–2023: Paralel & Modern (2010–sekarang)
- **Fortran 2008**: **Coarrays** — pemrograman paralel yang terintegrasi dalam bahasa tersebut
  -`DO CONCURRENT`— konstruksi loop paralel
  -`SUBMODULE`— pemrograman modular
  - Atribut `CONTIGUOUS`
- **Fortran 2018**: Coarray yang ditingkatkan, peningkatan `ASSOCIATE`, tim
- **Fortran 2023**: penyempurnaan konstruksi `BLOCK`, penyempurnaan `ALLOCATE`,`SELECT RANK`, bilangan bulat tak bertanda tangan
## Evolusi Sintaks
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

## Evolusi Fitur
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

## Prinsip Desain Utama
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## Pertumbuhan Ekosistem
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
