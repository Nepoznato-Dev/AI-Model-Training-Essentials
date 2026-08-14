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
# Fortran – Ökosystem- und Tooling-Leitfaden
Dieser Leitfaden behandelt die wesentlichen Tools, Bibliotheken und Infrastruktur im Fortran-Ökosystem.
---

## Fortran-Standards und -Compiler
| Compiler | Plattform | Notizen |
|----------|----------|-------|
| **gfortran** | Plattformübergreifend | GNU Fortran (GCC), am häufigsten verwendet |
| **ifx / ifort** | Plattformübergreifend | Intel Fortran (oneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **Flang** | Plattformübergreifend | LLVM-basiert (neu) |
| **NAG** | Plattformübergreifend | Kommerziell, strikte Konformität |
| **Cray** | HPC | Cray-Supercomputer |
| **IBM XL** | HPC | IBM-Systeme |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Systeme erstellen
| Werkzeug | Geben Sie | ein Am besten für |
|------|------|----------|
| **CMake** | Plattformübergreifend | Industriestandard |
| **fpm** | Fortran-native | Moderner Fortran-Paketmanager |
| **Meson** | Modern | Schnelle, saubere Syntax |
| **Machen** | Klassisch | Einfache Projekte |
| **SCons** | Python-basiert | Komplexe Builds |
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

## Paketverwaltung
| Werkzeug | Zweck |
|------|---------|
| **fpm** | Fortran-Paketmanager (modern) |
| **Fortran stdlib** | Standard-Bibliotheksaufwand |
| **Conan** | C/C++/Fortran-Pakete |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Wissenschaftliche Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **BLAS / LAPACK** | Lineare Algebra |
| **OpenBLAS** | Optimiertes BLAS |
| **Intel MKL** | Intel Math Kernel-Bibliothek |
| **FFTW** | Schnelle Fourier-Transformationen |
| **ARPACK** | Eigenwertprobleme |
| **ScaLAPACK** | Parallele lineare Algebra |
| **PETSc** | Paralleles wissenschaftliches Rechnen |
| **Trilinos** | Groß angelegte wissenschaftliche |
| **HDF5** | Hierarchisches Datenformat |
| **NetCDF** | Klima/wissenschaftliche Daten |
| **stdlib** | Fortran-Standardbibliothek |
| **fortran-os** | Betriebssystemschnittstelle |
| **forlab** | Wissenschaftliches Rechnen |
| **M_array** | Array-Dienstprogramme |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **pFUnit** | Unit-Tests (NASA) |
| **Fortran-Test** | Einfaches Testen |
| **Probefahrt** | Modernes Testen |
| **FPM-Test** | Eingebauter Testläufer |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **fprettify** | Codeformatierung |
| **gefunden** | Einrückung und Formatierung |
| **fortran-linter** | Fusseln |
| **Camfort** | Refactoring |
| **Kokosnuss** | Codeabdeckung |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Paralleles Rechnen
| Technologie | Zweck |
|------------|---------|
| **OpenMP** | Shared-Memory-Parallelität |
| **MPI** | Verteilter Speicher (Message Passing) |
| **Coarrays** | Fortran native Parallelität |
| **CUDA Fortran** | GPU-Computing |
| **OpenACC** | Direktivenbasierte GPU |
| **GLEICHZEITIG MACHEN** | Fortran 2008 Parallelschleifen |
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

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **stdlib** | Standardbibliothek |
| **json-fortran** | JSON-Analyse |
| **fürutils** | Utility-Funktionen |
| **KLAPPE** | Parsen von Befehlszeilenargumenten |
| **für_zeit** | Datums-/Uhrzeitverarbeitung |
| **FiNeR** | Dateiverwaltung |
| **forxml** | XML-Analyse |
| **forpy** | Python-Interop |
| **ISO_C_BINDING** | C-Interoperabilität |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **VS-Code + modernes Fortran** | Bester Fortran LSP |
| **IntelliJ + Fortran-Plugin** | JetBrains-Unterstützung |
| **Neovim + fortls** | Terminalbasiert |
| **Finsternis + Photran** | Eclipse Fortran |
| **Code::Blocks** | Leichte IDE |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Statische Binärdatei** | `gfortran -static`|
| **Gemeinsam genutzte Bibliothek** | `gfortran -shared`|
| **C-Interop** | Aufruf von C/C++ über`ISO_C_BINDING`|
| **Python-Interop** | f2py, forpy |
| **Docker** | Containerisiert |
| **HPC-Cluster** | MPI + SLURM |
---

## Zusammenfassung
Das Ökosystem von Fortran ist speziell für leistungsstarkes wissenschaftliches Rechnen konzipiert. Die Standard-Toolchain ist: **gfortran** oder **ifx** für die Kompilierung, **fpm** für die Paketverwaltung, **CMake** für Builds, **BLAS/LAPACK** für lineare Algebra, **OpenMP** und **MPI** für Parallelität, **pFUnit** für Tests und **fprettify** für die Formatierung. Fortran zeichnet sich durch numerische Berechnungen, Wettersimulationen, numerische Strömungsdynamik und groß angelegte wissenschaftliche Simulationen aus. Modernes Fortran (2018/2023) mit Coarrays, DO CONCURRENT und verbessertem OOP ist eine leistungsfähige moderne Sprache. Das Ökosystem ist für HPC, Klimamodellierung und Computerphysik von wesentlicher Bedeutung.