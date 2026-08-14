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
# Fortran — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang kasangkapan, aklatan, at imprastraktura sa Fortran ecosystem.
---

## Mga Pamantayan at Compiler ng Fortran
| Compiler | Platform | Mga Tala |
|----------|----------|-------|
| **gfortran** | Cross-platform | GNU Fortran (GCC), pinakamalawak na ginagamit |
| **ifx / ifort** | Cross-platform | Intel Fortran (oneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **flang** | Cross-platform | LLVM-based (bago) |
| **NAG** | Cross-platform | Komersyal, mahigpit na pagsunod |
| **Cray** | HPC | Cray supercomputers |
| **IBM XL** | HPC | IBM system |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Bumuo ng mga System
| Tool | Uri | Pinakamahusay Para sa |
|------|------|----------|
| **CMake** | Cross-platform | Pamantayan sa industriya |
| **fpm** | Fortran-native | Modernong Fortran package manager |
| **Meson** | Moderno | Mabilis, malinis na syntax |
| **Gumawa** | Klasiko | Mga simpleng proyekto |
| **SCons** | Batay sa Python | Mga kumplikadong build |
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

## Pamamahala ng Package
| Tool | Layunin |
|------|---------|
| **fpm** | Fortran Package Manager (moderno) |
| **Fortran stdlib** | Karaniwang pagsisikap sa aklatan |
| **Conan** | C/C++/Fortran na mga pakete |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Mga Siyentipikong Aklatan
| Aklatan | Layunin |
|---------|---------|
| **BLAS / LAPACK** | Linear algebra |
| **OpenBLAS** | Na-optimize na BLAS |
| **Intel MKL** | Intel Math Kernel Library |
| **FFTW** | Mabilis na nag-transform si Fourier |
| **ARPACK** | Mga problema sa eigenvalue |
| **ScaLAPACK** | Parallel linear algebra |
| **PETSc** | Parallel scientific computing |
| **Trilinos** | Malaking sukat na siyentipiko |
| **HDF5** | Hierarchical na format ng data |
| **NetCDF** | Climate/scientific data |
| **stdlib** | Fortran standard library |
| **fortran-os** | OS interface |
| **forlab** | Scientific computing |
| **M_array** | Mga kagamitan sa array |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **pFUnit** | Unit testing (NASA) |
| **Fortran-test** | Simpleng pagsubok |
| **test-drive** | Modernong pagsubok |
| **fpm test** | Built-in na test runner |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **fprettify** | Pag-format ng code |
| **naghahanap** | Indentation at pag-format |
| **fortran-linter** | Linting |
| **kaginhawahan** | Refactoring |
| **CoCoNuT** | Saklaw ng code |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Parallel Computing
| Teknolohiya | Layunin |
|------------|---------|
| **OpenMP** | Shared-memory parallelism |
| **MPI** | Ibinahagi-memorya (Message Passing) |
| **Mga Coarray** | Fortran katutubong paralelismo |
| **CUDA Fortran** | GPU computing |
| **OpenACC** | Directive-based na GPU |
| **GAWIN MAGKASABA** | Fortran 2008 parallel loops |
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

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **stdlib** | Karaniwang aklatan |
| **json-fortran** | Pag-parse ng JSON |
| **forutils** | Mga function ng utility |
| **FLAP** | Pag-parse ng argumento ng command-line |
| **para sa_panahon** | Petsa/oras ng pangangasiwa |
| **FiNeR** | Pangangasiwa ng file |
| **forxml** | XML parsing |
| **forpy** | Python interop |
| **ISO_C_BINDING** | C interoperability |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **VS Code + Modern Fortran** | Pinakamahusay na Fortran LSP |
| **IntelliJ + fortran-plugin** | Suporta sa JetBrains |
| **Neovim + fortls** | Nakabatay sa terminal |
| **Eclipse + Photran** | Eclipse Fortran |
| **Code::Blocks** | Magaang IDE |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Static binary** | `gfortran -static`|
| **Nakabahaging aklatan** | `gfortran -shared`|
| **C interop** | Tumawag mula sa C/C++ sa pamamagitan ng`ISO_C_BINDING`|
| **Python interop** | f2py, forpy |
| **Docker** | Naka-container |
| **Mga kumpol ng HPC** | MPI + SLURM |
---

## Buod
Ang ecosystem ng Fortran ay sadyang binuo para sa high-performance na scientific computing. Ang karaniwang toolchain ay: **gfortran** o **ifx** para sa compilation, **fpm** para sa pamamahala ng package, **CMake** para sa mga build, **BLAS/LAPACK** para sa linear algebra, **OpenMP** at **MPI** para sa parallelism, **pFUnit** para sa pagsubok, at **fprettify** para sa pag-format. Mahusay ang Fortran sa numerical computing, weather simulation, computational fluid dynamics, at large-scale scientific simulation. Ang Modern Fortran (2018/2023) na may mga coarray, DO CONCURRENT, at pinahusay na OOP ay isang may kakayahang modernong wika. Ang ecosystem ay mahalaga sa HPC, pagmomodelo ng klima, at computational physics.