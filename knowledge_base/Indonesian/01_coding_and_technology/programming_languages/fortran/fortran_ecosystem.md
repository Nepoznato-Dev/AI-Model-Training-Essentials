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
# Fortran — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, perpustakaan, dan infrastruktur penting dalam ekosistem Fortran.
---

## Standar & Kompiler Fortran
| Kompiler | Peron | Catatan |
|----------|----------|-------|
| **gfortran** | Lintas platform | GNU Fortran (GCC), paling banyak digunakan |
| **ifx / ifort** | Lintas platform | Intel Fortran (satuAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **flang** | Lintas platform | Berbasis LLVM (baru) |
| **NAG** | Lintas platform | Komersial, kepatuhan yang ketat |
| **Kray** | HPC | Superkomputer gila |
| **IBMXL** | HPC | Sistem IBM |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Membangun Sistem
| Alat | Ketik | Terbaik Untuk |
|------|------|----------|
| **CMembuat** | Lintas platform | Standar industri |
| **fpm** | Fortran-asli | Manajer paket Fortran modern |
| **Meson** | Modern | Sintaks yang cepat dan bersih |
| **Buat** | Klasik | Proyek sederhana |
| **SKon** | Berbasis Python | Bangunan kompleks |
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

## Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **fpm** | Manajer Paket Fortran (modern) |
| **Stdlib Fortran** | Upaya perpustakaan standar |
| **Conan** | Paket C/C++/Fortran |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Perpustakaan Ilmiah
| Perpustakaan | Tujuan |
|---------|---------|
| **BLAS / LAPACK** | Aljabar linier |
| **OpenBLAS** | BLAS yang Dioptimalkan |
| **Intel MKL** | Perpustakaan Kernel Matematika Intel |
| **FFTW** | Transformasi Fast Fourier |
| **ARPACK** | Masalah nilai eigen |
| **ScaLAPACK** | Aljabar linier paralel |
| **HEWAN PELIHARAAN** | Komputasi ilmiah paralel |
| **Trilino** | Ilmiah skala besar |
| **HDF5** | Format data hierarki |
| **NetCDF** | Iklim/data ilmiah |
| **stdlib** | Perpustakaan standar Fortran |
| **fortran-os** | antarmuka sistem operasi |
| **forlab** | Komputasi ilmiah |
| **M_array** | Utilitas susunan |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **pFUnit** | Pengujian unit (NASA) |
| **Uji Fortran** | Pengujian sederhana |
| **uji coba** | Pengujian modern |
| **uji fpm** | Pelari uji bawaan |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **frettify** | Pemformatan kode |
| **menemukan** | Indentasi dan pemformatan |
| **fortran-linter** | Linting |
| **kenyamanan** | Pemfaktoran ulang |
| **CoCoNuT** | Cakupan kode |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Komputasi Paralel
| Teknologi | Tujuan |
|------------|---------|
| **BukaMP** | Paralelisme memori bersama |
| **MPI** | Memori terdistribusi (Message Passing) |
| **Coarray** | Paralelisme asli Fortran |
| **CUDA Fortran** | Komputasi GPU |
| **OpenACC** | GPU berbasis arahan |
| **LAKUKAN BERSAMAAN** | Loop paralel Fortran 2008 |
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

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **stdlib** | Perpustakaan standar |
| **json-fortran** | Penguraian JSON |
| **forutils** | Fungsi utilitas |
| **PENUTUP** | Penguraian argumen baris perintah |
| **untuk_waktu** | Penanganan tanggal/waktu |
| **Baik** | Penanganan berkas |
| **forxml** | Penguraian XML |
| **forpy** | Interop Python |
| **ISO_C_BINDING** | interoperabilitas C |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS + Fortran Modern** | LSP Fortran Terbaik |
| **IntelliJ + plugin fortran** | Dukungan JetBrain |
| **Neovim + benteng** | Berbasis terminal |
| **Gerhana + Photran** | Gerhana Fortran |
| **Kode::Blok** | IDE Ringan |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Biner statis** | `gfortran -static`|
| **Pustaka bersama** | `gfortran -shared`|
| **interop C** | Panggilan dari C/C++ melalui`ISO_C_BINDING`|
| **Interop Python** | f2py, forpy |
| **Buruh pelabuhan** | dalam kontainer |
| **Kluster HPC** | MPI + SLURM |
---

## Ringkasan
Ekosistem Fortran dibangun khusus untuk komputasi ilmiah berkinerja tinggi. Toolchain standarnya adalah: **gfortran** atau **ifx** untuk kompilasi, **fpm** untuk manajemen paket, **CMake** untuk build, **BLAS/LAPACK** untuk aljabar linier, **OpenMP** dan **MPI** untuk paralelisme, **pFUnit** untuk pengujian, dan **fprettify** untuk pemformatan. Fortran unggul dalam komputasi numerik, simulasi cuaca, dinamika fluida komputasi, dan simulasi ilmiah skala besar. Fortran modern (2018/2023) dengan coarrays, DO CONCURRENT, dan OOP yang ditingkatkan adalah bahasa modern yang mumpuni. Ekosistem sangat penting dalam HPC, pemodelan iklim, dan fisika komputasi.