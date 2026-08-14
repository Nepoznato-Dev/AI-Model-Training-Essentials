<!--
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

-->
# فورٹران - ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ فورٹران ماحولیاتی نظام میں ضروری ٹولز، لائبریریوں اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## فورٹران کے معیارات اور مرتب کرنے والے
| مرتب کرنے والا | پلیٹ فارم | نوٹس |
|------------|---------|-------|
| **gfortran** | کراس پلیٹ فارم | GNU Fortran (GCC)، سب سے زیادہ استعمال شدہ |
| **ifx/ifort** | کراس پلیٹ فارم | Intel Fortran (oneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **فلانگ** | کراس پلیٹ فارم | LLVM پر مبنی (نیا) |
| **NAG** | کراس پلیٹ فارم | تجارتی، سخت موافقت |
| **کرے** | HPC | کرے سپر کمپیوٹرز |
| **IBM XL** | HPC | IBM سسٹمز |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## سسٹمز بنائیں
| ٹول | قسم | کے لیے بہترین |
|------|------|---------|
| **CMake** | کراس پلیٹ فارم | صنعت کا معیار |
| **fpm** | فورٹران مقامی | جدید فورٹران پیکیج مینیجر |
| **میسن** | جدید | تیز، صاف نحو |
| **بناؤ** | کلاسیکی | سادہ منصوبے |
| **SCons** | ازگر پر مبنی | کمپلیکس بناتا ہے |
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

## پیکیج مینجمنٹ
| ٹول | مقصد |
|------|---------|
| **fpm** | فورٹران پیکیج مینیجر (جدید) |
| **فورٹران stdlib** | معیاری لائبریری کی کوشش |
| **کانن** | C/C++/فورٹران پیکیجز |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## سائنسی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **BLAS / LAPACK** | لکیری الجبرا |
| **اوپن بلاس** | آپٹمائزڈ BLAS |
| **انٹیل ایم کے ایل** | انٹیل میتھ کرنل لائبریری |
| **FFTW** | فاسٹ فوئیر کی تبدیلی |
| **ARPACK** | Eigenvalue مسائل |
| **سکیلپیک** | متوازی لکیری الجبرا |
| **PETSc** | متوازی سائنسی کمپیوٹنگ |
| **ٹریلینوس** | بڑے پیمانے پر سائنسی |
| **HDF5** | درجہ بندی ڈیٹا فارمیٹ |
| **NetCDF** | موسمیاتی/سائنسی ڈیٹا |
| **stdlib** | فورٹران معیاری لائبریری |
| **فورٹران او ایس** | OS انٹرفیس |
| **فورلاب** | سائنسی کمپیوٹنگ |
| **M_array** | صف کی افادیت |
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

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **pFUnit** | یونٹ ٹیسٹنگ (NASA) |
| **فورٹران ٹیسٹ** | سادہ ٹیسٹنگ |
| **ٹیسٹ ڈرائیو** | جدید ٹیسٹنگ |
| **fpm ٹیسٹ** | بلٹ ان ٹیسٹ رنر |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **fprettify** | کوڈ فارمیٹنگ |
| ** تلاش کرنے والا** | انڈینٹیشن اور فارمیٹنگ |
| **فورٹران لنٹر** | لنٹنگ |
| **آرام** | ریفیکٹرنگ |
| **CoCoNuT** | کوڈ کوریج |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## متوازی کمپیوٹنگ
| ٹیکنالوجی | مقصد |
|------------|---------|
| **اوپن ایم پی** | مشترکہ میموری کی متوازی |
| **MPI** | تقسیم شدہ میموری (پیغام گزرنا) |
| **کورے** | فورٹران مقامی متوازی |
| **CUDA Fortran** | GPU کمپیوٹنگ |
| **اوپن اے سی سی** | ہدایت پر مبنی GPU |
| **ہم آہنگی کریں** | فورٹران 2008 متوازی لوپس |
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

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **stdlib** | معیاری لائبریری |
| **json-فورٹران** | JSON پارسنگ |
| **فروٹلز** | افادیت کے افعال |
| **فلاپ** | کمانڈ لائن آرگومنٹ پارسنگ |
| **وقت کے لیے** | تاریخ/وقت ہینڈلنگ |
| **FiNeR** | فائل ہینڈلنگ |
| **forxml** | XML پارسنگ |
| **فورپی** | ازگر انٹراپ |
| **ISO_C_BINDING** | C انٹرآپریبلٹی |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **VS کوڈ + ماڈرن فورٹران** | بہترین فورٹران ایل ایس پی |
| **انٹیلی جے + فورٹران پلگ ان** | JetBrains کی حمایت |
| **نیوم + قلعے** | ٹرمینل پر مبنی |
| **گرہن + فوٹوران** | چاند گرہن فورٹران |
| **کوڈ::بلاکس** | ہلکا پھلکا IDE |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **جامد بائنری** | `gfortran -static`|
| **مشترکہ لائبریری** | `gfortran -shared`|
| **C انٹراپ** | C/C++ سے`ISO_C_BINDING`کے ذریعے کال کریں۔
| **پائیتھن انٹراپ** | f2py، forpy |
| **ڈوکر** | کنٹینرائزڈ |
| **HPC کلسٹرز** | MPI + SLURM |
---

## خلاصہ
فورٹران کا ماحولیاتی نظام اعلیٰ کارکردگی والے سائنسی کمپیوٹنگ کے لیے مقصد سے بنایا گیا ہے۔ معیاری ٹول چین یہ ہے: تالیف کے لیے **gfortran** یا **ifx**، پیکج کے انتظام کے لیے **fpm**، تعمیرات کے لیے **CMake**، لکیری الجبرا کے لیے **BLAS/LAPACK**، متوازی کے لیے **OpenMP** اور **MPI**، جانچ کے لیے **pFUnit**، اور **fprettify** کے لیے۔ فورٹران عددی کمپیوٹنگ، موسم کی تخروپن، کمپیوٹیشنل فلوئڈ ڈائنامکس، اور بڑے پیمانے پر سائنسی نقوش میں مہارت رکھتا ہے۔ Modern Fortran (2018/2023) coarrays، DO CONCURRENT، اور بہتر OOP کے ساتھ ایک قابل جدید زبان ہے۔ ماحولیاتی نظام HPC، موسمیاتی ماڈلنگ، اور کمپیوٹیشنل فزکس میں ضروری ہے۔