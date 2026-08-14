<!--
---
# Metadata
title: "Fortran — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern Fortran code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [fortran, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Fortran — Mga Idiomatic Pattern at Pinakamahuhusay na Kasanayan
Sinasaklaw ng gabay na ito ang mga idiomatic pattern at pinakamahuhusay na kagawian para sa pagsusulat ng malinis, modernong Fortran (2018+) na code.
---

## Modern Fortran
```fortran
! ✅ implicit none always
module my_module
    implicit none
    private
    public :: process, calculate
contains
    subroutine process(input, output)
        real(8), intent(in)  :: input(:)
        real(8), intent(out) :: output(size(input))
        output = input**2 + 1.0d0
    end subroutine
end module

! ✅ Array operations (avoid loops)
program vectorized
    implicit none
    real(8) :: a(100), b(100), c(100)
    
    c = a + b           ! array addition
    c = a * b + sin(a)  ! element-wise
    a = where(b > 0, b, 0.0d0)  ! conditional
end program

! ✅ Assumed-shape arrays
subroutine compute(x, result)
    real(8), intent(in)  :: x(:)
    real(8), intent(out) :: result
    result = sum(x**2)
end subroutine
```

---

## Mga Uri ng Hinango
```fortran
! ✅ Derived types with type-bound procedures
module user_module
    implicit none
    
    type :: User
        character(len=64) :: name
        character(len=128) :: email
        integer :: age
    contains
        procedure :: greet => user_greet
    end type
    
contains
    subroutine user_greet(self)
        class(User), intent(in) :: self
        print '(A,A)', 'Hello, I am ', trim(self%name)
    end subroutine
end module
```

---

## Error sa Paghawak
```fortran
! ✅ I/O status checking
integer :: ios
open(unit=10, file='data.txt', status='old', iostat=ios)
if (ios /= 0) then
    print *, 'Error opening file'
    stop 1
end if

! ✅ Allocatable with error checking
real(8), allocatable :: array(:)
allocate(array(n), stat=ios)
if (ios /= 0) then
    print *, 'Allocation failed'
    stop 1
end if
```

---

## Buod
Binibigyang-diin ng mga modernong Fortran idiom ang:`implicit none`, array operations (iwasan ang mga loop), assumed-shape arrays, derived type na may type-bound procedures, at`intent`para sa lahat ng argumento. Sundin ang fprettify para sa pag-format. Ang Modern Fortran (2018+) na may mga coarray at DO CONCURRENT ay sumusuporta sa parallel computing na natively.