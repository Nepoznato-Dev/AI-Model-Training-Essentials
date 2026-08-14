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
# Fortran — 관용적 패턴 및 모범 사례
이 가이드에서는 깔끔하고 현대적인 Fortran(2018+) 코드를 작성하기 위한 관용적 패턴과 모범 사례를 다룹니다.
---

## 현대 포트란
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

## 파생 유형
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

## 오류 처리
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

## 요약
최신 Fortran 관용구는 `implicit none`, 배열 연산(루프 방지), 가정된 형태의 배열, 유형 바인딩 프로시저가 있는 파생 유형 및 모든 인수에 대한 `intent`를 강조합니다. 포맷하려면 fpretify를 따르세요. Coarray 및 DO CONCURRENT를 갖춘 최신 Fortran(2018+)은 기본적으로 병렬 컴퓨팅을 지원합니다.