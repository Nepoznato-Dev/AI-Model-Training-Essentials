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
# फोरट्रान - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ सुधार के साथ फोरट्रान में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है।
---

## 1. 1-आधारित अनुक्रमण
```fortran
! ❌ WRONG — 0-based indexing
integer :: arr(10)
arr(0) = 42  ! Error or unexpected behavior

! ✅ CORRECT — Fortran arrays are 1-based by default
arr(1) = 42
```

---

## 2.`implicit none`का उपयोग नहीं करना
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

## 3. ऐरे असाइनमेंट बनाम एलिमेंट-वार
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

## 4. इरादा निर्दिष्ट नहीं
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

## 5. आधुनिक फोरट्रान सुविधाओं का उपयोग न करना
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

## 6. आवंटन योग्य सारणियों के साथ मेमोरी लीक
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

## सारांश
फोरट्रान का वैज्ञानिक कंप्यूटिंग फोकस जाल बनाता है: 1-आधारित अनुक्रमण, अंतर्निहित टाइपिंग (हमेशा`implicit none`का उपयोग करें), सरणी संचालन बनाम लूप, और इरादे विनिर्देश। आधुनिक फोरट्रान (2003+) में मॉड्यूल, व्युत्पन्न प्रकार और ओओपी हैं - उनका उपयोग करें। फोरट्रान तरीका है:`implicit none`हमेशा, सभी तर्कों के लिए`intent`निर्दिष्ट करें, सरणी संचालन का उपयोग करें, और जो भी आप आवंटित करते हैं उसे हटा दें।