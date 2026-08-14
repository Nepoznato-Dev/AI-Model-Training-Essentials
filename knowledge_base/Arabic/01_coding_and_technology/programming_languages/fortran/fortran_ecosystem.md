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

# فورتران - دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والمكتبات والبنية التحتية الأساسية في نظام فورتران البيئي.
---

## معايير ومجمعات فورتران
| مترجم | منصة | ملاحظات |
|----------|---------|-------|
| **جفورتران** | عبر منصة | جنو فورتران (دول مجلس التعاون الخليجي)، الأكثر استخدامًا |
| **آيفكس/آيفورت** | عبر منصة | إنتل فورتران (oneAPI) |
| **نفورتران** | GPU | نفيديا فورتران (كودا) |
| ** فلانج ** | عبر منصة | القائم على LLVM (جديد) |
| **تذمر** | عبر منصة | تجاري، توافق صارم |
| ** كراي ** | الحوسبة عالية الأداء | كراي الحواسيب العملاقة |
| ** آي بي إم XL ** | الحوسبة عالية الأداء | أنظمة آي بي إم |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## بناء الأنظمة
| أداة | اكتب | الأفضل لـ |
|------|------|----------|
| **CMake** | عبر منصة | معيار الصناعة |
| **التيار الوطني الحر** | فورتران الأصلي | مدير حزم فورتران الحديث |
| **ميسون** | حديث | بناء جملة سريع ونظيف |
| **اصنع** | كلاسيك | مشاريع بسيطة |
| **سلبيات** | القائم على بايثون | مجمع يبني |
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

## إدارة الحزم
| أداة | الغرض |
|------|---------|
| **التيار الوطني الحر** | مدير الحزم فورتران (حديث) |
| **فورتران ستدليب** | جهد المكتبة القياسي |
| **كونان** | حزم C/C++/فورتران |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## المكتبات العلمية
| مكتبة | الغرض |
|---------|--------|
| ** بلاس / لاباك ** | الجبر الخطي |
| **أوبن بلاس** | الأمثل بلاس |
| **إنتل MKL** | مكتبة إنتل الرياضيات النواة |
| ** ففتو ** | تحويلات فورييه السريعة |
| **ARPACK** | مشاكل القيمة الذاتية |
| ** سكالاباك ** | الجبر الخطي الموازي |
| ** بيتسك ** | الحوسبة العلمية الموازية |
| **تريلينوس** | علمية واسعة النطاق |
| **HDF5** | تنسيق البيانات الهرمي |
| **نيت سي دي إف ** | البيانات المناخية/العلمية |
| **ستدليب** | مكتبة فورتران القياسية |
| **فورتران-نظام التشغيل** | واجهة نظام التشغيل |
| **للمختبر** | الحوسبة العلمية |
| **M_array** | المرافق صفيف |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **pFUnit** | اختبار الوحدة (ناسا) |
| **اختبار فورتران** | اختبار بسيط |
| **اختبار القيادة** | الاختبارات الحديثة |
| **اختبار التيار الوطني الحر** | عداء اختبار مدمج |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| **تجميل** | تنسيق الكود |
| **وجد** | المسافة البادئة والتنسيق |
| **فورتران-لينتر** | البطانة |
| **كامفورت** | إعادة البناء |
| **جوز الهند** | تغطية الكود |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## الحوسبة المتوازية
| تكنولوجيا | الغرض |
|------------|---------|
| **أوبن إم بي** | توازي الذاكرة المشتركة |
| **MPI** | الذاكرة الموزعة (تمرير الرسائل) |
| **المصفوفات** | فورتران التوازي الأصلي |
| **كودا فورتران** | الحوسبة GPU |
| **أوبنACC** | GPU القائم على التوجيه |
| ** افعل المتزامنة ** | فورتران 2008 حلقات متوازية |
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

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **ستدليب** | المكتبة القياسية |
| **json-فورتران** | تحليل JSON |
| **الفوائد** | وظائف المرافق |
| **رفرف** | تحليل وسيطة سطر الأوامر |
| **للوقت** | التعامل مع التاريخ/الوقت |
| **فينير** | التعامل مع الملفات |
| **فوركسمل** | تحليل XML |
| **فوربي** | التشغيل البيني لبيثون |
| **ISO_C_BINDING** | قابلية التشغيل البيني C |
---

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **رمز VS + فورتران الحديث** | أفضل فورتران LSP |
| **IntelliJ + البرنامج المساعد fortran** | دعم JetBrains |
| **نيوفيم + فورتلس** | القائم على المحطة الطرفية |
| ** خسوف + فوتران ** | كسوف فورتران |
| **الكود::كتل** | بيئة تطوير متكاملة خفيفة الوزن |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **ثنائي ثابت** | `gfortran -static`|
| **المكتبة المشتركة** | `gfortran -shared`|
| **التشغيل المتداخل C** | اتصل من C/C++ عبر`ISO_C_BINDING`|
| **بايثون التشغيل المتداخل** | f2py، فوربي |
| ** عامل الميناء ** | في حاويات |
| ** مجموعات HPC ** | MPI + SLURM |
---

## ملخص
تم تصميم نظام Fortran البيئي خصيصًا للحوسبة العلمية عالية الأداء. سلسلة الأدوات القياسية هي: **gfortran** أو **ifx** للتجميع، **fpm** لإدارة الحزم، **CMake** للإنشاءات، **BLAS/LAPACK** للجبر الخطي، **OpenMP** و **MPI** للتوازي، **pFUnit** للاختبار، و **fprettify** للتنسيق. تتفوق فورتران في الحوسبة العددية، ومحاكاة الطقس، وديناميكيات الموائع الحسابية، والمحاكاة العلمية واسعة النطاق. تعتبر لغة Fortran الحديثة (2018/2023) مع المصفوفات، وDO CONCURRENT، وOOP المحسنة لغة حديثة قادرة. يعد النظام البيئي ضروريًا في الحوسبة عالية الأداء (HPC)، ونمذجة المناخ، والفيزياء الحاسوبية.