---
# Metadata
title: "Fortran — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Fortran with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# فورٹران - عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز فورٹران میں سب سے عام غلطیوں، ٹریپس، اور اینٹی پیٹرن کو تصحیح کے ساتھ کیٹلاگ کرتا ہے۔
---

## 1. 1-بیسڈ انڈیکسنگ
```fortran
! ❌ WRONG — 0-based indexing
integer :: arr(10)
arr(0) = 42  ! Error or unexpected behavior

! ✅ CORRECT — Fortran arrays are 1-based by default
arr(1) = 42
```

---

## 2.`implicit none`استعمال نہیں کرنا
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

## 3. اری اسائنمنٹ بمقابلہ عنصر کے حساب سے
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

## 4. ارادہ متعین نہیں ہے۔
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

## 5. جدید فورٹران خصوصیات کا استعمال نہ کرنا
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

## 6. ایلوکیٹ ایبل اریز کے ساتھ میموری کا لیک ہونا
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

## خلاصہ
فورٹران کی سائنسی کمپیوٹنگ فوکس ٹریپس بناتی ہے: 1 پر مبنی اشاریہ سازی، مضمر ٹائپنگ (ہمیشہ`implicit none`استعمال کریں)، ارے آپریشنز بمقابلہ لوپس، اور ارادے کی تفصیلات۔ Modern Fortran (2003+) میں ماڈیولز، اخذ کردہ اقسام، اور OOP ہیں — انہیں استعمال کریں۔ فورٹران طریقہ یہ ہے: ہمیشہ `implicit none`، تمام دلائل کے لیے`intent`کی وضاحت کریں، ارے آپریشنز کا استعمال کریں، اور جو کچھ آپ مختص کرتے ہیں اسے ڈیلوکیٹ کریں۔