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

# Fortran — Ecosystem & Tooling Guide

This guide covers the essential tools, libraries, and infrastructure in the Fortran ecosystem.

---

## Fortran Standards & Compilers

| Compiler | Platform | Notes |
|----------|----------|-------|
| **gfortran** | Cross-platform | GNU Fortran (GCC), most widely used |
| **ifx / ifort** | Cross-platform | Intel Fortran (oneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **flang** | Cross-platform | LLVM-based (new) |
| **NAG** | Cross-platform | Commercial, strict conformance |
| **Cray** | HPC | Cray supercomputers |
| **IBM XL** | HPC | IBM systems |

```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Build Systems

| Tool | Type | Best For |
|------|------|----------|
| **CMake** | Cross-platform | Industry standard |
| **fpm** | Fortran-native | Modern Fortran package manager |
| **Meson** | Modern | Fast, clean syntax |
| **Make** | Classic | Simple projects |
| **SCons** | Python-based | Complex builds |

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

## Package Management

| Tool | Purpose |
|------|---------|
| **fpm** | Fortran Package Manager (modern) |
| **Fortran stdlib** | Standard library effort |
| **Conan** | C/C++/Fortran packages |

```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Scientific Libraries

| Library | Purpose |
|---------|---------|
| **BLAS / LAPACK** | Linear algebra |
| **OpenBLAS** | Optimized BLAS |
| **Intel MKL** | Intel Math Kernel Library |
| **FFTW** | Fast Fourier transforms |
| **ARPACK** | Eigenvalue problems |
| **ScaLAPACK** | Parallel linear algebra |
| **PETSc** | Parallel scientific computing |
| **Trilinos** | Large-scale scientific |
| **HDF5** | Hierarchical data format |
| **NetCDF** | Climate/scientific data |
| **stdlib** | Fortran standard library |
| **fortran-os** | OS interface |
| **forlab** | Scientific computing |
| **M_array** | Array utilities |

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

## Testing

| Framework | Purpose |
|-----------|---------|
| **pFUnit** | Unit testing (NASA) |
| **Fortran-test** | Simple testing |
| **test-drive** | Modern testing |
| **fpm test** | Built-in test runner |

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

## Code Quality

| Tool | Purpose |
|------|---------|
| **fprettify** | Code formatting |
| **findent** | Indentation and formatting |
| **fortran-linter** | Linting |
| **camfort** | Refactoring |
| **CoCoNuT** | Code coverage |

```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Parallel Computing

| Technology | Purpose |
|------------|---------|
| **OpenMP** | Shared-memory parallelism |
| **MPI** | Distributed-memory (Message Passing) |
| **Coarrays** | Fortran native parallelism |
| **CUDA Fortran** | GPU computing |
| **OpenACC** | Directive-based GPU |
| **DO CONCURRENT** | Fortran 2008 parallel loops |

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

## Key Libraries

| Library | Purpose |
|---------|---------|
| **stdlib** | Standard library |
| **json-fortran** | JSON parsing |
| **forutils** | Utility functions |
| **FLAP** | Command-line argument parsing |
| **for_time** | Date/time handling |
| **FiNeR** | File handling |
| **forxml** | XML parsing |
| **forpy** | Python interop |
| **ISO_C_BINDING** | C interoperability |

---

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **VS Code + Modern Fortran** | Best Fortran LSP |
| **IntelliJ + fortran-plugin** | JetBrains support |
| **Neovim + fortls** | Terminal-based |
| **Eclipse + Photran** | Eclipse Fortran |
| **Code::Blocks** | Lightweight IDE |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Static binary** | `gfortran -static` |
| **Shared library** | `gfortran -shared` |
| **C interop** | Call from C/C++ via `ISO_C_BINDING` |
| **Python interop** | f2py, forpy |
| **Docker** | Containerized |
| **HPC clusters** | MPI + SLURM |

---

## Summary

Fortran's ecosystem is purpose-built for high-performance scientific computing. The standard toolchain is: **gfortran** or **ifx** for compilation, **fpm** for package management, **CMake** for builds, **BLAS/LAPACK** for linear algebra, **OpenMP** and **MPI** for parallelism, **pFUnit** for testing, and **fprettify** for formatting. Fortran excels at numerical computing, weather simulation, computational fluid dynamics, and large-scale scientific simulations. Modern Fortran (2018/2023) with coarrays, DO CONCURRENT, and improved OOP is a capable modern language. The ecosystem is essential in HPC, climate modeling, and computational physics.
