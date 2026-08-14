---
# Metadata
title: "Fortran — Syntax Reference"
description: "Detailed syntax reference for Fortran covering array operations, modules, derived types, coarrays, and high-performance computing patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [fortran, syntax-reference, arrays, modules, hpc, scientific-computing, coarrays, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Fortran — Odniesienie do składni
Ten dokument zawiera kompleksowe, uporządkowane informacje o składni Modern Fortran (2008/2018). Uzupełnia główne odniesienia do języka Fortran, koncentrując się na wyczerpujących wzorcach składni, operacjach tablicowych, modułach, OOP i obliczeniach o wysokiej wydajności.
---

## Operatory i wyrażenia
### Główni operatorzy
| Operator | Imię | Przykład | Notatki |
|---------|------|---------|-------|
| `+``-``*``/``**`| Arytmetyka | `2**10`| `**`to potęgowanie |
| `==``/=` | Równość | `a == b`| `/=`jest „nierówny” |
| `<``>``<=``>=` | Porównanie | `a >= b`| |
| `.and.``.or.``.not.`| Logiczne | `a .and. b`| |
| `.eqv.``.neqv.` | Równoważność logiczna | `a .eqv. b`| |
| `//`| Łączenie ciągów | `'hello' // ' world'`| |
---

## Struktura programu
```fortran
program main
    implicit none  ! Always use this!

    ! Variable declarations
    integer :: i, n
    real(8) :: x, y
    character(len=100) :: name
    logical :: flag = .true.

    ! Constants
    real(8), parameter :: pi = 3.14159265358979323846d0
    integer, parameter :: dp = selected_real_kind(15, 307)

    ! Input/output
    write(*, '(A)') 'Enter your name:'
    read(*, '(A)') name
    write(*, '(A,A)') 'Hello, ', trim(name)

    ! Format specifiers
    write(*, '(I6)') 42              ! integer, width 6
    write(*, '(F10.4)') 3.14159      ! float, width 10, 4 decimals
    write(*, '(E12.5)') 1.23d5       ! scientific notation
    write(*, '(2F10.4)') x, y        ! two floats

end program main
```

---

## Tablice
```fortran
! Declaration
real(8), dimension(10) :: x              ! 1D, 1 to 10
real(8), dimension(-5:5) :: y            ! custom bounds
real(8), dimension(3, 3) :: A            ! 2D matrix
integer, dimension(10, 20, 30) :: B      ! 3D array

! Initialization
real(8) :: v(5) = [1.0d0, 2.0d0, 3.0d0, 4.0d0, 5.0d0]
real(8) :: w(3) = [(real(i, 8), i = 1, 3)]  ! implied do-loop

! Array constructor
integer :: arr(5)
arr = [10, 20, 30, 40, 50]

! Array operations (element-wise, no loops!)
real(8) :: a(100), b(100), c(100)
c = a + b              ! element-wise addition
c = a * b              ! element-wise multiply
c = sin(a) * cos(b)    ! element-wise functions
c = sqrt(a**2 + b**2)  ! complex expressions

! Array slicing
a(1:10)                ! first 10 elements
a(::2)                 ! every other element
A(:, 1)                ! first column
A(1, :)                ! first row
A(2:4, 3:5)            ! submatrix

! WHERE — conditional assignment
where (a > 0)
    c = sqrt(a)
elsewhere
    c = 0.0d0
end where

! Built-in array functions
sum(a)                 ! sum of all elements
product(a)             ! product
maxval(a)              ! maximum value
minval(a)              ! minimum
maxloc(a)              ! index of maximum
dot_product(a, b)      ! dot product
matmul(A, B)           ! matrix multiply
transpose(A)           ! transpose
size(a)                ! number of elements
size(A, dim=1)         ! number of rows
reshape(A, [9, 1])     ! reshape
```

---

## Kontroluj przepływ
```fortran
! if / else if / else
if (x > 0.0d0) then
    write(*, *) 'positive'
else if (x < 0.0d0) then
    write(*, *) 'negative'
else
    write(*, *) 'zero'
end if

! do loop
do i = 1, 10
    write(*, *) i
end do

! do with step
do i = 10, 1, -1
    write(*, *) i
end do

! do while
do while (err > tol)
    call iterate(x, err)
end do

! select case
select case (status)
case (1)
    write(*, *) 'active'
case (2)
    write(*, *) 'pending'
case default
    write(*, *) 'unknown'
end select

! Loop control
do i = 1, 100
    if (mod(i, 2) == 0) cycle    ! continue (skip to next)
    if (i > 50) exit             ! break
    write(*, *) i
end do
```

---

## Podprogramy
```fortran
! Subroutine
subroutine swap(a, b)
    implicit none
    real(8), intent(inout) :: a, b
    real(8) :: temp
    temp = a
    a = b
    b = temp
end subroutine swap

! Function
function factorial(n) result(fact)
    implicit none
    integer, intent(in) :: n
    integer :: fact
    integer :: i
    fact = 1
    do i = 2, n
        fact = fact * i
    end do
end function factorial

! Pure function (no side effects, compiler can optimize)
pure function distance(x1, y1, x2, y2) result(d)
    implicit none
    real(8), intent(in) :: x1, y1, x2, y2
    real(8) :: d
    d = sqrt((x2-x1)**2 + (y2-y1)**2)
end function distance

! Elemental function (applied element-wise to arrays)
elemental function square(x) result(y)
    implicit none
    real(8), intent(in) :: x
    real(8) :: y
    y = x * x
end function square
! Usage: square([1.0d0, 2.0d0, 3.0d0]) => [1, 4, 9]
```

---

## Moduły i OOP
```fortran
module vector_module
    implicit none
    private
    public :: Vector, vector_add, vector_norm

    type :: Vector
        real(8), allocatable :: components(:)
    contains
        procedure :: norm => vector_norm_method
        procedure :: add => vector_add_method
        generic :: operator(+) => add
    end type Vector

contains

    function vector_add(a, b) result(c)
        type(Vector), intent(in) :: a, b
        type(Vector) :: c
        allocate(c%components(size(a%components)))
        c%components = a%components + b%components
    end function

    function vector_norm_method(self) result(n)
        class(Vector), intent(in) :: self
        real(8) :: n
        n = sqrt(sum(self%components**2))
    end function

    function vector_add_method(self, other) result(res)
        class(Vector), intent(in) :: self, other
        type(Vector) :: res
        allocate(res%components(size(self%components)))
        res%components = self%components + other%components
    end function
end module vector_module

! Inheritance
module shape_module
    implicit none

    type, abstract :: Shape
        character(len=50) :: name
    contains
        procedure(area_func), deferred :: area
    end type Shape

    abstract interface
        function area_func(self) result(a)
            import :: Shape
            class(Shape), intent(in) :: self
            real(8) :: a
        end function
    end interface

    type, extends(Shape) :: Circle
        real(8) :: radius
    contains
        procedure :: area => circle_area
    end type Circle

contains

    function circle_area(self) result(a)
        class(Circle), intent(in) :: self
        real(8) :: a
        a = 3.14159265358979d0 * self%radius**2
    end function
end module shape_module
```

---

## We/wy pliku
```fortran
! Write to file
integer :: unit_num
open(newunit=unit_num, file='output.dat', status='replace', action='write')
write(unit_num, '(3F12.6)') x, y, z
close(unit_num)

! Read from file
open(newunit=unit_num, file='input.dat', status='old', action='read')
do while (.not. eof(unit_num))
    read(unit_num, '(3F12.6)') x, y, z
    process(x, y, z)
end do
close(unit_num)

! Formatted I/O
write(*, '(A, I6, F10.4)') 'Result: ', n, value
write(*, '(*(F8.3))') array  ! all elements

! Namelist (group I/O)
integer :: nx, ny
real(8) :: dx, dt
namelist /grid/ nx, ny, dx, dt
read(*, nml=grid)
```

---

## Coarrays (programowanie równoległe)
```fortran
! Coarray — shared-memory parallelism
real(8) :: local_data[*]     ! one per image
real(8) :: shared_array(100)[*]

! Access another image's data
shared_array(1)[1] = 42.0d0  ! write to image 1's data
val = local_data[2]           ! read from image 2

! Synchronization
sync all                      ! barrier — all images wait

! Critical section
critical
    counter[1] = counter[1] + 1
end critical

! Lock
integer(lock_type) :: lk[*]
lock(lk)
! exclusive access
unlock(lk)

! Coarray collective operations (Fortran 2018)
call co_sum(result, result_image=1)
call co_broadcast(data, source_image=1)
```

---

## Streszczenie
Składnia współczesnego Fortranu jest przejrzysta, uporządkowana i zoptymalizowana pod kątem obliczeń numerycznych. Operacje na tablicach eliminują pętle w przypadku większości zadań matematycznych. Moduły zapewniają enkapsulację i zarządzanie przestrzenią nazw. Funkcje OOP (typy pochodne, dziedziczenie, polimorfizm) umożliwiają czystą organizację kodu. Coarrays oferuje natywne programowanie równoległe bez zewnętrznych bibliotek. Mocne strony Fortrana — wydajność, operacje na tablicach i precyzja numeryczna — pozostają niezrównane w obliczeniach naukowych. Jeśli chodzi o HPC, fizykę obliczeniową i symulacje inżynieryjne, Fortran nadal jest potęgą.