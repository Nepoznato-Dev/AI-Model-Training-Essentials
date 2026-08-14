---
# Metadata
title: "Fortran — Cheat Sheet"
description: "Quick-reference cheat sheet for Fortran syntax, arrays, and scientific computing patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [fortran, scientific, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Fortran – Spickzettel
## Grundlagen
```fortran
program basics
    implicit none

    ! Variables
    integer :: x = 42
    real :: pi = 3.14159
    real(8) :: dpi = 3.14159265358979d0  ! double precision
    character(len=20) :: name = "Alice"
    logical :: active = .true.
    complex :: z = (1.0, 2.0)

    ! Constants
    integer, parameter :: MAX = 100
    real, parameter :: GRAVITY = 9.81

    ! Type conversion
    real(x)           ! int to real
    int(pi)           ! real to int
    dble(pi)          ! to double precision

    ! String operations
    len_trim(name)
    trim(name)
    adjustl(name)     ! left justify
    index(name, "lic")
    name(1:3)         ! "Ali"
    name // " Smith"  ! concatenation

    ! Output
    print *, "Hello, ", trim(name), "!"
    write(*, '(A, I0)') "Age: ", x
    write(*, '(F8.2)') pi

end program basics
```

## Arrays
```fortran
! Declaration
real :: v(5)                    ! 1D array, 5 elements
real :: A(3, 3)                 ! 2D array (matrix)
real, allocatable :: arr(:)     ! dynamic array
real, allocatable :: mat(:,:)

! Initialization
v = [1.0, 2.0, 3.0, 4.0, 5.0]
v = (/ 1.0, 2.0, 3.0, 4.0, 5.0 /)  ! older syntax
A = reshape([1,2,3,4,5,6,7,8,9], [3,3])

! Allocate
allocate(arr(10))
allocate(mat(3, 4))
deallocate(arr)

! Array operations (whole-array)
arr = arr * 2.0
arr = arr + 1.0
result = sum(arr)
avg = sum(arr) / size(arr)
max_val = maxval(arr)
min_val = minval(arr)
product = product(arr)

! Array slicing
v(2:4)          ! elements 2,3,4
v(::2)          ! every other element
v(size(v):1:-1) ! reversed
A(:, 1)         ! first column
A(1, :)         ! first row

! WHERE (conditional assignment)
where (arr > 0)
    arr = log(arr)
elsewhere
    arr = 0.0
end where

! Array intrinsics
dot_product(v1, v2)
matmul(A, B)
transpose(A)
reshape(arr, [2, 5])
```

## Kontrollfluss
```fortran
! If
if (x > 0) then
    print *, "positive"
else if (x == 0) then
    print *, "zero"
else
    print *, "negative"
end if

! Select case
select case (day)
case (1)
    print *, "Monday"
case (2:5)
    print *, "Weekday"
case (6, 7)
    print *, "Weekend"
case default
    print *, "Unknown"
end select

! Do loops
do i = 1, 10
    print *, i
end do

do i = 10, 1, -1    ! step -1
    print *, i
end do

do while (condition)
    ! ...
end do

! Implicit do (array construction)
v = [(i, i = 1, 10)]
v = [(real(i), i = 0, 100, 10)]
```

## Unterprogramme und Funktionen
```fortran
! Subroutine
subroutine swap(a, b)
    real, intent(inout) :: a, b
    real :: temp
    temp = a
    a = b
    b = temp
end subroutine swap

! Function
real function area(radius)
    real, intent(in) :: radius
    real, parameter :: PI = 3.14159
    area = PI * radius**2
end function area

! Module with contained procedures
module math_utils
    implicit none
contains
    function factorial(n) result(f)
        integer, intent(in) :: n
        integer :: f, i
        f = 1
        do i = 2, n
            f = f * i
        end do
    end function factorial

    subroutine solve_quadratic(a, b, c, x1, x2)
        real, intent(in) :: a, b, c
        real, intent(out) :: x1, x2
        real :: disc
        disc = b**2 - 4*a*c
        x1 = (-b + sqrt(disc)) / (2*a)
        x2 = (-b - sqrt(disc)) / (2*a)
    end subroutine solve_quadratic
end module math_utils
```

## Abgeleitete Typen
```fortran
! Derived type (struct)
type :: Point
    real :: x, y
end type Point

type :: Circle
    type(Point) :: center
    real :: radius
contains
    procedure :: area => circle_area
end type Circle

! Usage
type(Point) :: p
type(Circle) :: c

p = Point(1.0, 2.0)
c = Circle(p, 3.0)
print *, c%area()

contains
    real function circle_area(self)
        class(Circle), intent(in) :: self
        circle_area = 3.14159 * self%radius**2
    end function
```

## Datei-E/A
```fortran
! Write file
open(unit=10, file='output.txt', status='replace', action='write')
write(10, '(A)') "Hello, World!"
write(10, '(F8.2)') 3.14
close(10)

! Read file
open(unit=10, file='input.txt', status='old', action='read')
do while (.not. eof(10))
    read(10, '(A)') line
    print *, trim(line)
end do
close(10)

! Formatted I/O
write(*, '(I5)') 42
write(*, '(F10.3)') 3.14159
write(*, '(A, 2X, A)') "Hello", "World"
write(*, '(*(F8.2))') arr  ! all elements
```

## Fehlerbehandlung
```fortran
! I/O status
integer :: ios
open(unit=10, file='data.txt', status='old', iostat=ios)
if (ios /= 0) then
    print *, "Error opening file, iostat=", ios
    stop
end if

! Error handling with goto (common Fortran pattern)
real function safe_divide(a, b)
    real, intent(in) :: a, b
    if (abs(b) < epsilon(b)) then
        print *, "Error: division by zero"
        safe_divide = 0.0
        return
    end if
    safe_divide = a / b
end function safe_divide

! Assert (Fortran 2018)
use iso_fortran_env, only: error_unit
if (.not. (x > 0)) then
    write(error_unit, *) "Assertion failed: x > 0"
    error stop
end if
```
