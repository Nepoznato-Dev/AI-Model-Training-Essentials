---
# Metadata
title: "Fortran — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern Fortran code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Fortran — 慣用模式與最佳實踐
本指南涵蓋了編寫乾淨、現代的 Fortran (2018+) 程式碼的慣用模式和最佳實踐。
---

## 現代 Fortran
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

## 派生類型
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

## 錯誤處理
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

＃＃ 概括
現代 Fortran 習慣用法強調：`implicit none`、陣列操作（避免循環）、假定形狀陣列、具有類型綁定過程的衍生型別以及所有參數的`intent`。按照 fprettify 進行格式化。具有 coarrays 和 DO CONCURRENT 的現代 Fortran (2018+) 本身支援並行計算。