---
# Metadata
title: "Fortran — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Fortran ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Fortran - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، کتابخانه‌ها و زیرساخت‌های ضروری در اکوسیستم فرترن را پوشش می‌دهد.
---

## استانداردها و کامپایلرهای فرترن
| کامپایلر | پلت فرم | یادداشت ها |
|----------|----------|-------|
| **گفورتران** | کراس پلتفرم | گنو فرترن (GCC)، پرکاربردترین |
| **ifx / ifort** | کراس پلتفرم | Intel Fortran (oneAPI) |
| **nvfortran** | پردازنده گرافیکی | NVIDIA Fortran (CUDA) |
| **فلنگ** | کراس پلتفرم | مبتنی بر LLVM (جدید) |
| **NAG** | کراس پلتفرم | تجاری، انطباق دقیق |
| **کری** | HPC | ابر رایانه های کری |
| **IBM XL** | HPC | سیستم های آی بی ام |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## ساخت سیستم
| ابزار | نوع | بهترین برای |
|------|------|----------|
| **CMake** | کراس پلتفرم | استاندارد صنعت |
| **fpm** | Fortran-native | مدیر بسته مدرن فرترن |
| **مزون** | مدرن | نحو سریع و تمیز |
| **ساخت ** | کلاسیک | پروژه های ساده |
| **Scons** | مبتنی بر پایتون | ساختمان های پیچیده |
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

## مدیریت بسته
| ابزار | هدف |
|------|---------|
| **fpm** | مدیر پکیج فرترن (مدرن) |
| **Fortran stdlib** | تلاش استاندارد کتابخانه |
| **کونان** | بسته های C/C++/Fortran |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## کتابخانه های علمی
| کتابخانه | هدف |
|---------|---------|
| **BLAS / LAPACK** | جبر خطی |
| **OpenBLAS** | BLAS بهینه شده |
| **اینتل MKL** | کتابخانه هسته ریاضی اینتل |
| **FFTW** | تبدیل فوریه سریع |
| **ARPACK** | مشکلات ارزش ویژه |
| **ScaLAPACK** | جبر خطی موازی |
| ** petsc** | محاسبات علمی موازی |
| **تریلینوس** | علمی در مقیاس بزرگ |
| **HDF5** | قالب داده های سلسله مراتبی |
| **NetCDF** | آب و هوا/ داده های علمی |
| **stdlib** | کتابخانه استاندارد فرترن |
| **fortran-os** | رابط سیستم عامل |
| **فورلب** | محاسبات علمی |
| **M_array** | ابزارهای آرایه |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **pFUnit** | تست واحد (ناسا) |
| **آزمون فرترن** | تست ساده |
| **تست درایو** | تست مدرن |
| **تست fpm** | رانر تست داخلی |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **زیبا کردن** | قالب بندی کد |
| **یاب** | تورفتگی و قالب بندی |
| **fortran-linter** | پرز زدن |
| **کامفورت** | بازسازی |
| **CoNuT** | پوشش کد |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## محاسبات موازی
| فناوری | هدف |
|------------|---------|
| **OpenMP** | توازی حافظه مشترک |
| **MPI** | Distributed-Memory (Passage Passing) |
| **همواره** | توازی بومی فرترن |
| **CUDA Fortran** | محاسبات GPU |
| **OpenACC** | GPU مبتنی بر دستورالعمل |
| ** انجام همزمان ** | حلقه های موازی فرترن 2008 |
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

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **stdlib** | کتابخانه استاندارد |
| **json-fortran** | تجزیه JSON |
| **forutils** | توابع سودمند |
| **فلپ** | تجزیه آرگومان خط فرمان |
| **برای_زمان** | رسیدگی به تاریخ/زمان |
| **FiNeR** | مدیریت فایل |
| **forxml** | تجزیه XML |
| **forpy** | interop پایتون |
| **ISO_C_BINDING** | قابلیت همکاری C |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + Modern Fortran** | بهترین Fortran LSP |
| **IntelliJ + افزونه fortran** | پشتیبانی JetBrains |
| **Neovim + fortls** | مبتنی بر ترمینال |
| **کسوف+فوتران** | Eclipse Fortran |
| **کد::Blocks** | IDE سبک |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **باینری استاتیک** | `gfortran -static`|
| **کتابخانه مشترک** | `gfortran -shared`|
| **C interop** | تماس از C/C++ از طریق`ISO_C_BINDING`|
| **تعامل پایتون** | f2py, forpy |
| **داکر** | کانتینری |
| **خوشه های HPC** | MPI + SLURM |
---

## خلاصه
اکوسیستم فرترن برای محاسبات علمی با کارایی بالا ساخته شده است. زنجیره ابزار استاندارد عبارتند از: **gfortran** یا **ifx** برای کامپایل، **fpm** برای مدیریت بسته، **CMake** برای ساخت، **BLAS/LAPACK** برای جبر خطی، **OpenMP** و **MPI** برای موازی، **pFUnit** برای آزمایش، و **fprettify برای قالب‌بندی. فرترن در محاسبات عددی، شبیه‌سازی آب و هوا، دینامیک سیالات محاسباتی و شبیه‌سازی‌های علمی در مقیاس بزرگ برتری دارد. Fortran مدرن (2018/2023) با هم‌آهنگ‌ها، DO CONCURRENT و OOP بهبودیافته یک زبان مدرن توانا است. اکوسیستم در HPC، مدل‌سازی آب و هوا و فیزیک محاسباتی ضروری است.