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

# ফোর্টরান — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি সংশোধন সহ Fortran-এর সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্ন ক্যাটালগ করে।
---

## 1. 1-ভিত্তিক ইন্ডেক্সিং
```fortran
! ❌ WRONG — 0-based indexing
integer :: arr(10)
arr(0) = 42  ! Error or unexpected behavior

! ✅ CORRECT — Fortran arrays are 1-based by default
arr(1) = 42
```

---

## 2.`implicit none`ব্যবহার করছেন না
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

## 3. অ্যারে অ্যাসাইনমেন্ট বনাম এলিমেন্ট অনুযায়ী
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

## 4. উদ্দেশ্য নির্দিষ্ট করা নেই
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

## 5. আধুনিক ফোরট্রান বৈশিষ্ট্য ব্যবহার না করা
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

## 6. বরাদ্দযোগ্য অ্যারে সহ মেমরি লিক
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

## সারাংশ
Fortran এর বৈজ্ঞানিক কম্পিউটিং ফোকাস ফাঁদ তৈরি করে: 1-ভিত্তিক সূচীকরণ, অন্তর্নিহিত টাইপিং (সর্বদা`implicit none`ব্যবহার করুন), অ্যারে অপারেশন বনাম লুপ, এবং উদ্দেশ্য স্পেসিফিকেশন। Modern Fortran (2003+) এর মডিউল, প্রাপ্ত প্রকার এবং OOP রয়েছে — সেগুলি ব্যবহার করুন। Fortran উপায় হল:`implicit none`সর্বদা, সমস্ত আর্গুমেন্টের জন্য`intent`নির্দিষ্ট করুন, অ্যারে অপারেশন ব্যবহার করুন এবং আপনি যা বরাদ্দ করেন তা ডিলকেট করুন।