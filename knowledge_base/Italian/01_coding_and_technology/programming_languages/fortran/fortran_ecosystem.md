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
# Fortran: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, le librerie e le infrastrutture essenziali nell'ecosistema Fortran.
---

## Standard e compilatori Fortran
| Compilatore | Piattaforma | Note |
|----------|----------|-------|
| **gfortran** | Multipiattaforma | GNU Fortran (GCC), il più utilizzato |
| **ifx / ifort** | Multipiattaforma | Intel Fortran (oneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **flangia** | Multipiattaforma | Basato su LLVM (nuovo) |
| **NAG** | Multipiattaforma | Commerciale, conformità rigorosa |
| **Cray** | HPC | Supercomputer Cray |
| **IBMXL** | HPC | Sistemi IBM |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Costruisci sistemi
| Strumento | Digitare | Ideale per |
|------|------|----------|
| **CMake** | Multipiattaforma | Standard di settore |
| **fpm** | Nativo Fortran | Gestore di pacchetti Fortran moderno |
| **Mesone** | Moderno | Sintassi veloce e pulita |
| **Fai** | Classico | Progetti semplici |
| **SCons** | Basato su Python | Costruzioni complesse |
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

## Gestione dei pacchetti
| Strumento | Scopo |
|------|---------|
| **fpm** | Gestore pacchetti Fortran (moderno) |
| **Fortran stdlib** | Sforzo della libreria standard |
| **Conan** | Pacchetti C/C++/Fortran |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

##Biblioteche scientifiche
| Biblioteca | Scopo |
|---------|---------|
| **BLAS/LAPACK** | Algebra lineare |
| **OpenBLAS** | BLAS ottimizzato |
| **Intel MKL** | Libreria del kernel matematico Intel |
| **FFTW** | Trasformate veloci di Fourier |
| **ARPACK** | Problemi agli autovalori |
| **ScaLAPACK** | Algebra lineare parallela |
| **ANIMALI DOMESTICI** | Calcolo scientifico parallelo |
| **Trilino** | Scientifico su larga scala |
| **HDF5** | Formato dati gerarchico |
| **NetCDF** | Dati climatici/scientifici |
| **stdlib** | Libreria standard Fortran |
| **fortran-os** | Interfaccia del sistema operativo |
| **forlab** | Calcolo scientifico |
| **M_array** | Utilità per array |
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

## Test
| Quadro | Scopo |
|-----------|---------|
| **pFUnit** | Test unitari (NASA) |
| **Test Fortran** | Test semplici |
| **prova di guida** | Test moderni |
| **test fpm** | Test runner integrato |
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

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **fprettifica** | Formattazione del codice |
| **trova** | Rientro e formattazione |
| **fortran-linter** | Lining |
| **comfort** | Refactoring |
| **CoCoNuT** | Copertura del codice |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Calcolo parallelo
| Tecnologia | Scopo |
|------------|---------|
| **OpenMP** | Parallelismo della memoria condivisa |
| **MPI** | Memoria distribuita (passaggio di messaggi) |
| **Coarray** | Parallelismo nativo Fortran |
| **CUDAFortran** | Calcolo GPU |
| **OpenACC** | GPU basata su direttive |
| **FARE CONCORRENTE** | Cicli paralleli Fortran 2008 |
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

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **stdlib** | Libreria standard |
| **json-fortran** | Analisi JSON |
| **forutils** | Funzioni di utilità |
| **FLAP** | Analisi degli argomenti della riga di comando |
| **per_tempo** | Gestione data/ora |
| **FiNeR** | Gestione dei file |
| **forxml** | Analisi XML |
| **forpy** | Interoperabilità Python |
| **ISO_C_BINDING** | Interoperabilità C |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **Codice VS + Fortran moderno** | Miglior LSP Fortran |
| **Plugin IntelliJ + fortran** | Supporto JetBrains |
| **Neovim + forti** | Basato su terminale |
| **Eclissi + Photran** | Eclissi Fortran |
| **Codice::Blocchi** | IDE leggero |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Binario statico** | `gfortran -static`|
| **Libreria condivisa** | `gfortran -shared`|
| **Interoperabilità C** | Chiamata da C/C++ tramite`ISO_C_BINDING`|
| **Interoperabilità Python** | f2py, forpy |
| **Docker** | Containerizzato |
| **Cluster HPC** | MPI + SLURM |
---

## Riepilogo
L'ecosistema Fortran è creato appositamente per il calcolo scientifico ad alte prestazioni. La toolchain standard è: **gfortran** o **ifx** per la compilazione, **fpm** per la gestione dei pacchetti, **CMake** per le build, **BLAS/LAPACK** per l'algebra lineare, **OpenMP** e **MPI** per il parallelismo, **pFUnit** per i test e **fprettify** per la formattazione. Fortran eccelle nel calcolo numerico, nella simulazione meteorologica, nella fluidodinamica computazionale e nelle simulazioni scientifiche su larga scala. Il Fortran moderno (2018/2023) con coarray, DO CONCURRENT e OOP migliorato è un linguaggio moderno capace. L’ecosistema è essenziale nell’HPC, nella modellistica climatica e nella fisica computazionale.