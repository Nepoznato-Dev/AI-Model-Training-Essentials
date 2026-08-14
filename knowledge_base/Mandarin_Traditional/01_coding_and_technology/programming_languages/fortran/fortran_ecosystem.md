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
# Fortran — 生態系與工具指南
本指南涵蓋了 Fortran 生態系統中的基本工具、庫和基礎設施。
---

## Fortran 標準和編譯器
|編譯器|平台|筆記|
|----------|----------|--------|
| **gfortran** |跨平台| GNU Fortran (GCC)，使用最廣泛 |
| **ifx / ifort** |跨平台|英特爾 Fortran (oneAPI) |
| **nvfortran** |圖形處理器 | NVIDIA Fortran（CUDA）|
| **法蘭** |跨平台|基於 LLVM（新）|
| **NAG** |跨平台|商業化，嚴格合規|
| **克雷** |高效能運算 |克雷超級電腦 |
| **IBM XL** |高效能運算 | IBM 系統 |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## 建置系統
|工具|類型 |最適合 |
|------|------|----------|
| **CMake** |跨平台|業界標準|
| **fpm** | Fortran 語言 |現代 Fortran 套件管理器 |
| **介子** |現代|快速、簡潔的語法 |
| **製作** |經典|簡單的項目 |
| **SCons** |基於Python |複雜的構建 |
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

## 套件管理
|工具|目的|
|------|---------|
| **fpm** | Fortran 套件管理器（現代）|
| **Fortran 標準庫** |標準庫的努力|
| **柯南** | C/C++/Fortran 套件 |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## 科學圖書館
|圖書館 |目的|
|---------|---------|
| **BLAS / 拉帕克** |線性代數 |
| **OpenBLAS** |最佳化BLAS |
| **英特爾 MKL** |英特爾數學核心庫 |
| **FFTW** |快速傅立葉變換 |
| **ARPACK** |特徵值問題|
| **ScaLAPACK** |平行線性代數 |
| **PETSc** |平行科學計算|
| **特里利諾斯** |大型科學|
| **HDF5** |分層資料格式|
| **NetCDF** |氣候/科學數據 |
| **標準庫** | Fortran 標準庫 |
| **fortran-os** |作業系統介面|
| **實驗室** |科學計算|
| **M_array** |陣列實用程式 |
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

## 測試
|框架|目的|
|------------|---------|
| **pFUnit** |單元測試（NASA）|
| **Fortran 測試** |簡單測試 |
| **試駕** |現代測試|
| **fpm 測試** |內建測試運行器 |
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

## 程式碼品質
|工具|目的|
|------|---------|
| **f美化** |程式碼格式化 |
| **發現** |縮排與格式 |
| **fortran-linter** |絨毛 |
| **康福特** |重建 |
| **椰子** |代碼覆蓋率|
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## 平行計算
|技術 |目的|
|------------|---------|
| **OpenMP** |共享記憶體並行性
| **MPI** |分散式記憶體（訊息傳遞）|
| **協同陣列** | Fortran 原生並行性 |
| **CUDA Fortran** | GPU運算|
| **OpenACC** |基於指令的 GPU |
| **並發** | Fortran 2008 並行循環 |
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

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **標準庫** |標準庫 |
| **json-fortran** | JSON解析|
| **forutils** |實用功能|
| **襟翼** |命令列參數解析 |
| **暫時** |日期/時間處理 |
| **FiNeR** |文件處理 |
| **forxml** | XML解析|
| **forpy** | Python 互通 |
| **ISO_C_BINDING** | C 互通性 |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS Code + 現代 Fortran** |最佳 Fortran LSP |
| **IntelliJ + fortran 外掛程式** | JetBrains 支援 |
| **Neovim + fortls** |基於終端 |
| **Eclipse + Photran** | Eclipse Fortran | Eclipse
| **程式碼::塊** |輕量級IDE |
---

## 部署
|方法|筆記|
|--------|--------|
| **靜態二進位** |`gfortran -static`|
| **共享庫** |`gfortran -shared`|
| **C 互通** |透過`ISO_C_BINDING`從 C/C++ 呼叫 |
| **Python 互通** | f2py、forpy |
| **碼頭工人** |貨櫃式|
| **HPC 叢集** | MPI + SLURM |
---

＃＃ 概括
Fortran 的生態系統專為高效能科學運算而建構。標準工具鍊是：用於編譯的 **gfortran** 或 **ifx**、用於套件管理的 **fpm**、用於構建的 **CMake**、用於線性代數的 **BLAS/LAPACK**、用於並行性的 **OpenMP** 和 **MPI**、用於測試的 **pFUnit** 以及用於格式化的 **fprettify**。 Fortran 擅長數值計算、天氣模擬、計算流體動力學和大規模科學模擬。具有 coarray、DO CONCURRENT 和改進的 OOP 的現代 Fortran (2018/2023) 是一種強大的現代語言。生態系統對於 HPC、氣候建模和計算物理至關重要。