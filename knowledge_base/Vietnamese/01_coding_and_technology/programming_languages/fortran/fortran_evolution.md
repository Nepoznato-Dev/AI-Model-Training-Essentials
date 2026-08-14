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
# Fortran — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| Fortran tôi | 1957 | **Ngôn ngữ cấp cao đầu tiên** (John Backus, IBM) |
| Fortran II | 1958 | Chương trình con, hàm |
| Fortran IV | 1962 | `DATA`,`EQUIVALENCE`,`COMMON`|
| FORTRAN 66 | 1966 | **Tiêu chuẩn ANSI đầu tiên** (X3.4-1966) |
| FORTRAN 77 | 1977 | **Lập trình có cấu trúc**:`IF`/`THEN`/`ELSE`,`CHARACTER`, I/O theo hướng danh sách |
| Fortran 90 | 1991 | **Chính**: nguồn dạng tự do, mô-đun, mảng,`ALLOCATABLE`,`SELECT CASE`|
| Fortran 95 | 1997 | `FORALL`,`WHERE`, thủ tục thuần túy/nguyên tố |
| Pháo đài 2003 | 2004 | **OOP**: lớp, kế thừa, đa hình, con trỏ `PROCEDURE`, số học`IEEE`|
| Fortran 2008 | 2010 | **Coarrays** (lập trình song song),`SUBMODULE`,`DO CONCURRENT`|
| Fortran 2018 | 2018 | **Coarray nâng cao**, cải tiến `ASSOCIATE`,`TYPE IS`|
| Fortran 2023 | 2024 | **`BLOCK`**, cải tiến `ALLOCATE`, `SELECT RANK`, số nguyên không dấu |
## Các cột mốc quan trọng
### Fortran I–IV: Sự ra đời của lập trình cấp cao (1957–1965)
- **1957**: John Backus và nhóm tại IBM tạo ra Fortran (Dịch công thức)
- **Ngôn ngữ lập trình cấp cao được sử dụng rộng rãi đầu tiên**
- **Fortran I**: Giới thiệu các vòng lặp `DO`,`IF`,`GO TO`, biểu thức số học
- **Fortran II (1958)**: Chương trình con và hàm (biên dịch riêng)
- **Fortran IV (1962)**: các khối`DATA`,`EQUIVALENCE`, `COMMON`
- Nguồn dạng cố định: cột 1-6 cho nhãn, 7-72 cho mã
### FORTRAN 66 & 77: Tiêu chuẩn hóa (1966–1990)
- **FORTRAN 66**: Tiêu chuẩn ANSI đầu tiên — Fortran di động
- **FORTRAN 77 (1977)**: Cổ điển
  - Lập trình có cấu trúc: `IF`/`THEN`/`ELSE`/`ENDIF` 
  - Kiểu`CHARACTER`(xử lý chuỗi)
  - I/O theo hướng danh sách (định dạng `*`)
  -`PARAMETER`(hằng số được đặt tên)
  -`ENTRY`(nhiều điểm vào)
  - Vẫn được sử dụng rộng rãi trong tính toán khoa học
### Fortran 90: Cuộc cách mạng hiện đại (1991)
- **Nguồn dạng tự do** — không còn hạn chế về cột
- **Mô-đun** — đóng gói,`USE`
- **Mảng động** —`ALLOCATABLE`,`ALLOCATE`
- **Các phép toán mảng** — cú pháp toàn bộ mảng`a = b + c`
-`SELECT CASE`— phân nhánh có cấu trúc
-`IMPLICIT NONE`- yêu cầu khai báo biến
- Thủ tục đệ quy
- Con trỏ
- Quá tải toán tử
- Các kiểu dẫn xuất (structs)
### Fortran 95–2003: OOP đến (1997–2004)
- **Fortran 95**:`FORALL`,`WHERE`, thủ tục thuần túy/nguyên tố
- **Fortran 2003**: **OOP đầy đủ**
  - Các lớp (kiểu dẫn xuất với các thủ tục ràng buộc kiểu)
  - Kế thừa (`EXTENDS`)
  - Đa hình (`CLASS`,`SELECT TYPE`)
  - Con trỏ thủ tục
  - Điều khiển dấu phẩy động IEEE
  - Tuyên bố `FLUSH`
  -`NEWUNIT`cho I/O
### Fortran 2008–2023: Song song & Hiện đại (2010–nay)
- **Fortran 2008**: **Coarrays** — lập trình song song được tích hợp trong ngôn ngữ
  -`DO CONCURRENT`- cấu trúc vòng lặp song song
  -`SUBMODULE`- lập trình mô-đun
  - Thuộc tính `CONTIGUOUS`
- **Fortran 2018**: Coarrays nâng cao, cải tiến `ASSOCIATE`, các nhóm
- **Fortran 2023**: Cải tiến cấu trúc `BLOCK`, cải tiến `ALLOCATE`,`SELECT RANK`, số nguyên không dấu
## Tiến hóa cú pháp
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

## Tiến hóa tính năng
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

## Nguyên tắc thiết kế chính
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## Tăng trưởng hệ sinh thái
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
