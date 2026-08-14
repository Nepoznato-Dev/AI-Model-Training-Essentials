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

# Фортран — распространенные ошибки и антипаттерны
В этом документе перечислены наиболее распространенные ошибки, ловушки и антишаблоны в Фортране с исправлениями.
---

## 1. Индексация на основе 1
```fortran
! ❌ WRONG — 0-based indexing
integer :: arr(10)
arr(0) = 42  ! Error or unexpected behavior

! ✅ CORRECT — Fortran arrays are 1-based by default
arr(1) = 42
```

---

## 2. Не использовать `implicit none`
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

## 3. Назначение массива и поэлементное сопоставление
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

## 4. Намерение не указано
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

## 5. Не использовать современные функции Fortran
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

## 6. Утечки памяти при использовании выделяемых массивов
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

## Краткое содержание
Научно-вычислительная направленность Фортрана создает ловушки: индексирование на основе 1, неявная типизация (всегда используйте `implicit none`), операции с массивами вместо циклов и спецификации намерений. В современном Фортране (2003+) есть модули, производные типы и ООП — используйте их. Способ Фортрана: всегда `implicit none`, указывайте`intent`для всех аргументов, используйте операции с массивами и освобождайте то, что вы выделяете.