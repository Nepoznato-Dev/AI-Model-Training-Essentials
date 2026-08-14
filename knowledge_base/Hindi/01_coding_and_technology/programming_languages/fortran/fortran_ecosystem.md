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

# फोरट्रान - पारिस्थितिकी तंत्र और टूलींग गाइड
यह मार्गदर्शिका फोरट्रान पारिस्थितिकी तंत्र में आवश्यक उपकरण, पुस्तकालय और बुनियादी ढांचे को शामिल करती है।
---

## फोरट्रान मानक एवं संकलक
| संकलक | प्लेटफार्म | नोट्स |
|---|-------|-------|
| **जीफोरट्रान** | क्रॉस-प्लेटफ़ॉर्म | जीएनयू फोरट्रान (जीसीसी), सबसे व्यापक रूप से उपयोग किया जाने वाला |
| **ifx / ifort** | क्रॉस-प्लेटफ़ॉर्म | इंटेल फोरट्रान (वनएपीआई) |
| **एनवीफोरट्रान** | जीपीयू | एनवीडिया फोरट्रान (सीयूडीए) |
| **फ्लैंग** | क्रॉस-प्लेटफ़ॉर्म | एलएलवीएम-आधारित (नया) |
| **नाग** | क्रॉस-प्लेटफ़ॉर्म | वाणिज्यिक, सख्त अनुरूपता |
| **क्रे** | एचपीसी | क्रे सुपर कंप्यूटर |
| **आईबीएम एक्सएल** | एचपीसी | आईबीएम सिस्टम |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## सिस्टम बनाएं
| उपकरण | प्रकार | के लिए सर्वश्रेष्ठ |
|------|------|----------|
| **सीमेक** | क्रॉस-प्लेटफ़ॉर्म | उद्योग मानक |
| **एफपीएम** | फोरट्रान-नेटिव | आधुनिक फोरट्रान पैकेज मैनेजर |
| **मेसन** | आधुनिक | तेज़, साफ़ वाक्यविन्यास |
| **बनाओ** | क्लासिक | सरल परियोजनाएँ |
| **स्कोन्स** | पायथन-आधारित | जटिल निर्माण |
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

## पैकेज प्रबंधन
| उपकरण | उद्देश्य |
|------|---------|
| **एफपीएम** | फोरट्रान पैकेज मैनेजर (आधुनिक) |
| **फोरट्रान stdlib** | मानक पुस्तकालय प्रयास |
| **कॉनन** | सी/सी++/फोरट्रान पैकेज |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## वैज्ञानिक पुस्तकालय
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **ब्लास / लैपैक** | रैखिक बीजगणित |
| **OpenBLAS** | अनुकूलित BLAS |
| **इंटेल एमकेएल** | इंटेल गणित कर्नेल लाइब्रेरी |
| **एफएफटीडब्ल्यू** | फास्ट फूरियर रूपांतरण |
| **आर्पैक** | आइजेनवैल्यू समस्याएं |
| **स्कैलापैक** | समानांतर रैखिक बीजगणित |
| **पीईटीएससी** | समानांतर वैज्ञानिक कंप्यूटिंग |
| **ट्रिलिनोस** | बड़े पैमाने पर वैज्ञानिक |
| **HDF5** | पदानुक्रमित डेटा प्रारूप |
| **नेटसीडीएफ** | जलवायु/वैज्ञानिक डेटा |
| **stdlib** | फोरट्रान मानक पुस्तकालय |
| **फोरट्रान-ओएस** | ओएस इंटरफ़ेस |
| **फोरलैब** | वैज्ञानिक कंप्यूटिंग |
| **M_array** | सरणी उपयोगिताएँ |
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

## परीक्षण
| ढाँचा | उद्देश्य |
|----|----|
| **pFUnit** | यूनिट परीक्षण (नासा) |
| **फोरट्रान-परीक्षण** | सरल परीक्षण |
| **टेस्ट-ड्राइव** | आधुनिक परीक्षण |
| **एफपीएम परीक्षण** | बिल्ट-इन टेस्ट रनर |
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

## कोड गुणवत्ता
| उपकरण | उद्देश्य |
|------|---------|
| **सुंदरता** | कोड फ़ॉर्मेटिंग |
| **खोजकर्ता** | इंडेंटेशन और फ़ॉर्मेटिंग |
| **फोरट्रान-लिंटर** | लिंटिंग |
| **आरामदेह** | रिफैक्टरिंग |
| **CoCoNuT** | कोड कवरेज |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## समानांतर कंप्यूटिंग
| प्रौद्योगिकी | उद्देश्य |
|---|---|
| **ओपनएमपी** | साझा-स्मृति समानता |
| **एमपीआई** | वितरित-स्मृति (संदेश पासिंग) |
| **कोरेरे** | फोरट्रान मूल समानता |
| **क्यूडा फोरट्रान** | जीपीयू कंप्यूटिंग |
| **ओपनएसीसी** | निर्देश-आधारित जीपीयू |
| **सहमत रहें** | फोरट्रान 2008 समानांतर लूप |
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

## प्रमुख पुस्तकालय
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **stdlib** | मानक पुस्तकालय |
| **जेसन-फोरट्रान** | JSON पार्सिंग |
| **forutils** | उपयोगिता कार्य |
| **फ़्लैप** | कमांड-लाइन तर्क पार्सिंग |
| **समय_के लिए** | दिनांक/समय प्रबंधन |
| **FiNeR** | फ़ाइल प्रबंधन |
| **forxml** | एक्सएमएल पार्सिंग |
| **फोरपी** | पायथन इंटरऑप |
| **आईएसओ_सी_बाइंडिंग** | सी अंतरसंचालनीयता |
---

## आईडीई और संपादक
| आईडीई | ताकतें |
|----|-----|
| **वीएस कोड + आधुनिक फोरट्रान** | सर्वश्रेष्ठ फोरट्रान एलएसपी |
| **इंटेलिजे + फोरट्रान-प्लगइन** | JetBrains समर्थन |
| **नियोविम + फोर्टल्स** | टर्मिनल-आधारित |
| **ग्रहण + फोट्रान** | ग्रहण फोरट्रान |
| **कोड::ब्लॉक** | हल्का आईडीई |
---

## तैनाती
| विधि | नोट्स |
|-------|-------|
| **स्टेटिक बाइनरी** | `gfortran -static`|
| **साझा पुस्तकालय** | `gfortran -shared`|
| **सी इंटरऑप** |`ISO_C_BINDING`के माध्यम से C/C++ से कॉल करें |
| **पायथन इंटरऑप** | f2py, फ़ोरपी |
| **डॉकर** | कंटेनरीकृत |
| **एचपीसी क्लस्टर** | एमपीआई + स्लम |
---

## सारांश
फोरट्रान का पारिस्थितिकी तंत्र उच्च-प्रदर्शन वैज्ञानिक कंप्यूटिंग के उद्देश्य से बनाया गया है। मानक टूलचेन है: संकलन के लिए **gfortrans** या **ifx**, पैकेज प्रबंधन के लिए **fpm**, बिल्ड के लिए **CMake**, रैखिक बीजगणित के लिए **BLAS/LAPACK**, समानता के लिए **OpenMP** और **MPI**, परीक्षण के लिए **pFUnit** और फ़ॉर्मेटिंग के लिए **fprettify**। फोरट्रान संख्यात्मक कंप्यूटिंग, मौसम सिमुलेशन, कम्प्यूटेशनल तरल गतिशीलता और बड़े पैमाने पर वैज्ञानिक सिमुलेशन में उत्कृष्टता प्राप्त करता है। आधुनिक फोरट्रान (2018/2023) कोएरेज़, डीओ कॉन्करेंट और बेहतर ओओपी के साथ एक सक्षम आधुनिक भाषा है। एचपीसी, जलवायु मॉडलिंग और कम्प्यूटेशनल भौतिकी में पारिस्थितिकी तंत्र आवश्यक है।