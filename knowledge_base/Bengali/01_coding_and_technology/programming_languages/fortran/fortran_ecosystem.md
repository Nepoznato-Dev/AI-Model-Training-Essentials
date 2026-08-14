---
# Metadata
title: "Fortran — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Fortran ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [fortran, ecosystem, tooling, compilers, hpc, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# ফোর্টরান — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি ফরট্রান ইকোসিস্টেমের প্রয়োজনীয় সরঞ্জাম, লাইব্রেরি এবং অবকাঠামো কভার করে।
---

## ফোরট্রান স্ট্যান্ডার্ড এবং কম্পাইলার
| কম্পাইলার | প্ল্যাটফর্ম | নোট |
|----------|----------|-------|
| **গফোর্ট্রান** | ক্রস-প্ল্যাটফর্ম | GNU Fortran (GCC), বহুল ব্যবহৃত |
| **ifx/ifort** | ক্রস-প্ল্যাটফর্ম | Intel Fortran (oneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **ফ্ল্যাং** | ক্রস-প্ল্যাটফর্ম | LLVM-ভিত্তিক (নতুন) |
| **নাগ** | ক্রস-প্ল্যাটফর্ম | বাণিজ্যিক, কঠোর সম্মতি |
| **ক্রে** | এইচপিসি | ক্রে সুপার কম্পিউটার |
| **IBM XL** | এইচপিসি | আইবিএম সিস্টেম |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## সিস্টেম তৈরি করুন
| টুল | প্রকার | জন্য সেরা |
|------|------|----------|
| **সিমেক** | ক্রস-প্ল্যাটফর্ম | শিল্প মান |
| **fpm** | ফোরট্রান-নেটিভ | আধুনিক ফোরট্রান প্যাকেজ ম্যানেজার |
| **মেসন** | আধুনিক | দ্রুত, পরিষ্কার বাক্য গঠন |
| **বানান** | ক্লাসিক | সহজ প্রকল্প |
| **SCons** | পাইথন ভিত্তিক | জটিল নির্মাণ |
```toml
# fpm.toml (Fortran Package Manager)
name = "myapp"
version = "0.1.0"
license = "MIT"
author = "Developer"

[build]
auto-executables = true
auto-tests = true

[dependencies]
stdlib = { git = "https://github.com/fortran-lang/stdlib.git" }

[[test]]
name = "test_main"
source-dir = "test"
main = "test_main.f90"
```

```bash
fpm build                 # build
fpm test                  # run tests
fpm run                   # run executable
fpm new myproject         # new project
```

```cmake
# CMakeLists.txt
cmake_minimum_required(VERSION 3.20)
project(myapp LANGUAGES Fortran)

add_executable(myapp src/main.f90 src/module1.f90)
set_target_properties(myapp PROPERTIES Fortran_MODULE_DIRECTORY ${CMAKE_BINARY_DIR}/modules)
target_include_directories(myapp PRIVATE ${CMAKE_BINARY_DIR}/modules)
```

---

## প্যাকেজ ব্যবস্থাপনা
| টুল | উদ্দেশ্য |
|------|---------|
| **fpm** | ফোরট্রান প্যাকেজ ম্যানেজার (আধুনিক) |
| **ফরট্রান stdlib** | স্ট্যান্ডার্ড লাইব্রেরি প্রচেষ্টা |
| **কোনান** | C/C++/Fortran প্যাকেজ |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## বৈজ্ঞানিক গ্রন্থাগার
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **BLAS / ল্যাপ্যাক** | রৈখিক বীজগণিত |
| **ওপেনব্লাস** | অপ্টিমাইজড BLAS |
| **ইন্টেল এমকেএল** | ইন্টেল ম্যাথ কার্নেল লাইব্রেরি |
| **FFTW** | ফাস্ট ফুরিয়ার রূপান্তর |
| **আরপ্যাক** | Eigenvalue সমস্যা |
| **স্ক্যাল্যাপ্যাক** | সমান্তরাল রৈখিক বীজগণিত |
| **PETSc** | সমান্তরাল বৈজ্ঞানিক কম্পিউটিং |
| **ট্রিলিনোস** | বড় মাপের বৈজ্ঞানিক |
| **HDF5** | শ্রেণিবিন্যাস তথ্য বিন্যাস |
| **NetCDF** | জলবায়ু/বৈজ্ঞানিক তথ্য |
| **stdlib** | ফরট্রান স্ট্যান্ডার্ড লাইব্রেরি |
| **ফোরট্রান-ওএস** | OS ইন্টারফেস |
| **ফরল্যাব** | বৈজ্ঞানিক কম্পিউটিং |
| **M_array** | অ্যারে ইউটিলিটি |
```fortran
! LAPACK example (solve linear system Ax = b)
program solve_linear
    use lapack95
    implicit none
    integer, parameter :: n = 3
    real(8) :: A(n,n), b(n)
    integer :: ipiv(n), info
    
    A = reshape([2.0, 1.0, 1.0, 1.0, 3.0, 2.0, 1.0, 2.0, 4.0], [n,n])
    b = [1.0, 2.0, 3.0]
    
    call gesv(A, b, ipiv, info)
    
    print *, "Solution:", b
end program
```

---

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **pFUnit** | ইউনিট টেস্টিং (NASA) |
| **ফরট্রান-পরীক্ষা** | সহজ পরীক্ষা |
| **টেস্ট-ড্রাইভ** | আধুনিক পরীক্ষা |
| **এফপিএম পরীক্ষা** | বিল্ট-ইন টেস্ট রানার |
```fortran
! test-drive example
module test_math
    use testdrive, only : new_unittest, unittest_type, error_type, check
    implicit none
contains
    subroutine collect_tests(testsuite)
        type(unittest_type), allocatable, intent(out) :: testsuite(:)
        testsuite = [ &
            new_unittest("addition", test_addition), &
            new_unittest("multiplication", test_multiplication) &
        ]
    end subroutine
    
    subroutine test_addition(error)
        type(error_type), allocatable, intent(out) :: error
        call check(2 + 3 == 5, error)
    end subroutine
end module
```

---

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **fprettify** | কোড ফরম্যাটিং |
| **অনুসন্ধানকারী** | ইন্ডেন্টেশন এবং ফরম্যাটিং |
| **ফরট্রান-লিন্টার** | লিন্টিং |
| **আরাম** | রিফ্যাক্টরিং |
| **CoCoNuT** | কোড কভারেজ |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## সমান্তরাল কম্পিউটিং
| প্রযুক্তি | উদ্দেশ্য |
|------------|---------|
| **ওপেনএমপি** | ভাগ-মেমরি সমান্তরাল |
| **এমপিআই** | ডিস্ট্রিবিউটেড-মেমরি (মেসেজ পাসিং) |
| **কোয়ারে** | ফোর্টরান নেটিভ প্যারালেলিজম |
| **CUDA ফোর্টরান** | GPU কম্পিউটিং |
| **OpenACC** | নির্দেশিকা-ভিত্তিক GPU |
| **একসঙ্গে করুন** | Fortran 2008 সমান্তরাল loops |
```fortran
! OpenMP example
program parallel_sum
    implicit none
    integer, parameter :: n = 1000000
    real(8) :: a(n), b(n), c(n)
    integer :: i
    
    !$omp parallel do
    do i = 1, n
        c(i) = a(i) + b(i)
    end do
    !$omp end parallel do
end program
```

```fortran
! Coarray example
program coarray_example
    implicit none
    integer :: i
    real, codimension[:] :: shared_value
    
    shared_value[this_image()] = real(this_image())
    sync all
    
    if (this_image() == 1) then
        do i = 1, num_images()
            print *, "Image", i, "has value", shared_value[i]
        end do
    end if
end program
```

---

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **stdlib** | স্ট্যান্ডার্ড লাইব্রেরি |
| **json-ফোর্ট্রান** | JSON পার্সিং |
| **forutils** | ইউটিলিটি ফাংশন |
| **ফ্ল্যাপ** | কমান্ড লাইন আর্গুমেন্ট পার্সিং |
| **সময়ের জন্য** | তারিখ/সময় পরিচালনা |
| **FiNeR** | ফাইল হ্যান্ডলিং |
| **ফরক্সএমএল** | XML পার্সিং |
| **ফরপি** | পাইথন ইন্টারপ |
| **ISO_C_BINDING** | C আন্তঃক্রিয়াশীলতা |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **ভিএস কোড + আধুনিক ফোর্টরান** | সেরা ফোর্টরান এলএসপি |
| **IntelliJ + fortran-plugin** | JetBrains সমর্থন |
| **নিওভিম + দুর্গ** | টার্মিনাল ভিত্তিক |
| **গ্রহণ + ফোট্রান** | Eclipse Fortran |
| **কোড::ব্লক** | লাইটওয়েট IDE |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **স্ট্যাটিক বাইনারি** | `gfortran -static`|
| **শেয়ারড লাইব্রেরি** | `gfortran -shared`|
| **C ইন্টারপ** |`ISO_C_BINDING`এর মাধ্যমে C/C++ থেকে কল করুন
| **পাইথন ইন্টারপ** | f2py, forpy |
| **ডকার** | কন্টেইনারাইজড |
| **HPC ক্লাস্টার** | MPI + SLURM |
---

## সারাংশ
Fortran এর ইকোসিস্টেম উচ্চ-কর্মক্ষমতা বৈজ্ঞানিক কম্পিউটিং জন্য উদ্দেশ্য-নির্মিত. স্ট্যান্ডার্ড টুলচেন হল: সংকলনের জন্য **gfortran** বা **ifx**, প্যাকেজ পরিচালনার জন্য **fpm**, বিল্ডের জন্য **CMake**, লিনিয়ার বীজগণিতের জন্য **BLAS/LAPACK**, সমান্তরালতার জন্য **OpenMP** এবং **MPI**, পরীক্ষার জন্য **pFUnit** এবং **fprettify** এর জন্য। ফোরট্রান সংখ্যাসূচক কম্পিউটিং, আবহাওয়ার সিমুলেশন, কম্পিউটেশনাল ফ্লুইড ডাইনামিকস এবং বড় আকারের বৈজ্ঞানিক সিমুলেশনে পারদর্শী। আধুনিক ফোরট্রান (2018/2023), কোয়ারে, DO ConcurrENT, এবং উন্নত OOP একটি সক্ষম আধুনিক ভাষা। এইচপিসি, ক্লাইমেট মডেলিং এবং কম্পিউটেশনাল ফিজিক্সে ইকোসিস্টেম অপরিহার্য।