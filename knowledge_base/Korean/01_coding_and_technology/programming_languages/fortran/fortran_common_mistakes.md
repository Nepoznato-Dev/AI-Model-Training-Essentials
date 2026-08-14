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

# Fortran — 일반적인 실수 및 안티 패턴
이 문서에는 Fortran에서 가장 흔히 발생하는 실수, 함정, 안티 패턴을 수정 사항이 포함된 목록으로 정리되어 있습니다.
---

## 1. 1 기반 인덱싱
```fortran
! ❌ WRONG — 0-based indexing
integer :: arr(10)
arr(0) = 42  ! Error or unexpected behavior

! ✅ CORRECT — Fortran arrays are 1-based by default
arr(1) = 42
```

---

## 2. `implicit none`를 사용하지 않음
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

## 3. 배열 할당과 요소별 할당
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

## 4. 의도가 지정되지 않음
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

## 5. 최신 포트란 기능을 사용하지 않음
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

## 6. 할당 가능한 배열의 메모리 누수
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

## 요약
Fortran의 과학 컴퓨팅 초점은 1 기반 인덱싱, 암시적 타이핑(항상`implicit none`사용), 배열 작업 대 루프 및 의도 사양과 같은 함정을 만듭니다. Modern Fortran(2003+)에는 모듈, 파생 유형 및 OOP가 있습니다. 이를 사용하세요. Fortran 방식은 다음과 같습니다. 항상 `implicit none`, 모든 인수에 대해 `intent`를 지정하고, 배열 작업을 사용하고, 할당한 것을 할당 해제합니다.