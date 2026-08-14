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
# Fortran — 生态系统和工具指南
本指南涵盖了 Fortran 生态系统中的基本工具、库和基础设施。
---

## Fortran 标准和编译器
|编译器|平台|笔记|
|----------|----------|--------|
| **gfortran** |跨平台| GNU Fortran (GCC)，使用最广泛 |
| **ifx / ifort** |跨平台|英特尔 Fortran (oneAPI) |
| **nvfortran** |图形处理器 | NVIDIA Fortran（CUDA）|
| **法兰** |跨平台|基于 LLVM（新）|
| **NAG** |跨平台|商业化，严格合规|
| **克雷** |高性能计算 |克雷超级计算机 |
| **IBM XL** |高性能计算 | IBM 系统 |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## 构建系统
|工具|类型 |最适合 |
|------|------|----------|
| **CMake** |跨平台|行业标准|
| **fpm** | Fortran 语言 |现代 Fortran 包管理器 |
| **介子** |现代|快速、简洁的语法 |
| **制作** |经典|简单的项目 |
| **SCons** |基于Python |复杂的构建 |
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

## 包管理
|工具|目的|
|------|---------|
| **fpm** | Fortran 包管理器（现代）|
| **Fortran 标准库** |标准库的努力|
| **柯南** | C/C++/Fortran 包 |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## 科学图书馆
|图书馆 |目的|
|---------|---------|
| **BLAS / 拉帕克** |线性代数 |
| **OpenBLAS** |优化BLAS |
| **英特尔 MKL** |英特尔数学内核库 |
| **FFTW** |快速傅立叶变换 |
| **ARPACK** |特征值问题|
| **ScaLAPACK** |并行线性代数 |
| **PETSc** |并行科学计算|
| **特里利诺斯** |大型科学|
| **HDF5** |分层数据格式|
| **NetCDF** |气候/科学数据 |
| **标准库** | Fortran 标准库 |
| **fortran-os** |操作系统界面|
| **实验室** |科学计算|
| **M_array** |数组实用程序 |
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

## 测试
|框架|目的|
|------------|---------|
| **pFUnit** |单元测试（NASA）|
| **Fortran 测试** |简单测试 |
| **试驾** |现代测试|
| **fpm 测试** |内置测试运行器 |
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

## 代码质量
|工具|目的|
|------|---------|
| **f美化** |代码格式化 |
| **发现** |缩进和格式 |
| **fortran-linter** |绒毛 |
| **康福特** |重构 |
| **椰子** |代码覆盖率|
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

＃＃ 并行计算
|技术 |目的|
|------------|---------|
| **OpenMP** |共享内存并行性
| **MPI** |分布式内存（消息传递）|
| **协同阵列** | Fortran 原生并行性 |
| **CUDA Fortran** | GPU计算|
| **OpenACC** |基于指令的 GPU |
| **并发** | Fortran 2008 并行循环 |
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

## 关键库
|图书馆 |目的|
|---------|---------|
| **标准库** |标准库 |
| **json-fortran** | JSON解析|
| **forutils** |实用功能|
| **襟翼** |命令行参数解析 |
| **暂时** |日期/时间处理 |
| **FiNeR** |文件处理 |
| **forxml** | XML解析|
| **forpy** | Python 互操作 |
| **ISO_C_BINDING** | C 互操作性 |
---

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **VS Code + 现代 Fortran** |最佳 Fortran LSP |
| **IntelliJ + fortran 插件** | JetBrains 支持 |
| **Neovim + fortls** |基于终端 |
| **Eclipse + Photran** | Eclipse Fortran | Eclipse
| **代码::块** |轻量级IDE |
---

## 部署
|方法|笔记|
|--------|--------|
| **静态二进制** | `gfortran -static`|
| **共享库** | `gfortran -shared`|
| **C 互操作** |通过`ISO_C_BINDING`从 C/C++ 调用 |
| **Python 互操作** | f2py、forpy |
| **码头工人** |集装箱式|
| **HPC 集群** | MPI + SLURM |
---

＃＃ 概括
Fortran 的生态系统专为高性能科学计算而构建。标准工具链是：用于编译的 **gfortran** 或 **ifx**、用于包管理的 **fpm**、用于构建的 **CMake**、用于线性代数的 **BLAS/LAPACK**、用于并行性的 **OpenMP** 和 **MPI**、用于测试的 **pFUnit** 以及用于格式化的 **fprettify**。 Fortran 擅长数值计算、天气模拟、计算流体动力学和大规模科学模拟。具有 coarray、DO CONCURRENT 和改进的 OOP 的现代 Fortran (2018/2023) 是一种功能强大的现代语言。生态系统对于 HPC、气候建模和计算物理至关重要。