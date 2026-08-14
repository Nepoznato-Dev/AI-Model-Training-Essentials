---
# Metadata
title: "Fortran — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Fortran with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [fortran, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# فرترن - اشتباهات رایج و ضد الگوها
این سند رایج ترین اشتباهات، تله ها و ضد الگوها را در فرترن با اصلاحات فهرست می کند.
---

## 1. نمایه سازی بر اساس 1
```fortran
! ❌ WRONG — 0-based indexing
integer :: arr(10)
arr(0) = 42  ! Error or unexpected behavior

! ✅ CORRECT — Fortran arrays are 1-based by default
arr(1) = 42
```

---

## 2. عدم استفاده از `implicit none`
```fortran
! ❌ WRONG — implicit typing
program test
  x = 5.0  ! x is implicitly real
  i = 10   ! i is implicitly integer (starts with 'i')
end program

! ✅ CORRECT — always use implicit none
program test
  implicit none
  real :: x
  integer :: i
  x = 5.0
  i = 10
end program
```

---

## 3. تخصیص آرایه در مقابل عنصر عاقلانه
```fortran
! ❌ WRONG — loop when array operation suffices
do i = 1, n
  c(i) = a(i) + b(i)
end do

! ✅ CORRECT — array operations
c = a + b
c = a * b  ! element-wise, not matrix multiply!
```

---

## 4. Intent مشخص نشده است
```fortran
! ❌ WRONG — arguments can be modified accidentally
subroutine process(data, n)
  real :: data(n)
  integer :: n
  data(1) = 0  ! modifies caller's data!
end subroutine

! ✅ CORRECT — specify intent
subroutine process(data, n)
  real, intent(in) :: data(n)
  integer, intent(in) :: n
end subroutine
```

---

## 5. عدم استفاده از ویژگی های مدرن Fortran
```fortran
! ❌ WRONG — old FORTRAN 77 style
      PROGRAM TEST
      INTEGER I
      DO 10 I = 1, 100
   10 CONTINUE
      END

! ✅ CORRECT — modern Fortran (2003+)
program test
  implicit none
  integer :: i
  do i = 1, 100
    ! modern code
  end do
end program
```

---

## 6. نشت حافظه با آرایه های قابل تخصیص
```fortran
! ❌ WRONG — forgetting to deallocate
subroutine process()
  real, allocatable :: arr(:)
  allocate(arr(1000))
  ! use arr...
  return  ! memory leaked!
end subroutine

! ✅ CORRECT — deallocate or use automatic cleanup
subroutine process()
  real, allocatable :: arr(:)
  allocate(arr(1000))
  ! use arr...
  deallocate(arr)
end subroutine
```

---

## خلاصه
تمرکز محاسبات علمی فرترن تله‌هایی ایجاد می‌کند: نمایه‌سازی مبتنی بر 1، تایپ ضمنی (همیشه از`implicit none`استفاده کنید)، عملیات آرایه در مقابل حلقه‌ها، و مشخصات هدف. Fortran مدرن (2003+) دارای ماژول ها، انواع مشتق شده و OOP است - از آنها استفاده کنید. روش فرترن به این صورت است: همیشه `implicit none`،`intent`را برای همه آرگومان ها مشخص کنید، از عملیات آرایه استفاده کنید و آنچه را که تخصیص می دهید به آن اختصاص دهید.