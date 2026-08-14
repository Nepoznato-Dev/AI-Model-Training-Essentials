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
# Fortran — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, biblioteki i infrastrukturę w ekosystemie Fortran.
---

## Standardy i kompilatory Fortran
| Kompilator | Platforma | Notatki |
|---------|-----|-------|
| **gfortran** | Wieloplatformowe | GNU Fortran (GCC), najczęściej używany |
| **ifx / ifort** | Wieloplatformowe | Intel Fortran (oneAPI) |
| **nvfortran** | Procesor graficzny | NVIDIA Fortran (CUDA) |
| **kołnierz** | Wieloplatformowe | oparty na LLVM (nowy) |
| **NAG** | Wieloplatformowe | Handlowa, ścisła zgodność |
| **Cray** | HPC | Superkomputery Cray |
| **IBM XL** | HPC | Systemy IBM |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Buduj systemy
| Narzędzie | Wpisz | Najlepsze dla |
|------|------|--------------|
| **CMrób** | Wieloplatformowe | Standard branżowy |
| **fpm** | Fortran-natywny | Nowoczesny menedżer pakietów Fortran |
| **Mezon** | Nowoczesne | Szybka, czysta składnia |
| **Zrób** | Klasyczny | Proste projekty |
| **SCady** | Oparte na Pythonie | Złożone kompilacje |
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

## Zarządzanie pakietami
| Narzędzie | Cel |
|------|-------------|
| **fpm** | Menedżer pakietów Fortran (nowoczesny) |
| **Fortran stdlib** | Standardowy wysiłek biblioteki |
| **Conan** | Pakiety C/C++/Fortran |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Biblioteki naukowe
| Biblioteka | Cel |
|--------|---------|
| **BLAS / LAPACK** | Algebra liniowa |
| **OpenBLAS** | Zoptymalizowany BLAS |
| **Intel MKL** | Biblioteka jądra matematycznego Intel |
| **FFW** | Szybka transformata Fouriera |
| **ARPACK** | Problemy wartości własnej |
| **ScaLAPACK** | Równoległa algebra liniowa |
| **PETSC** | Równoległe obliczenia naukowe |
| **Trilinos** | Naukowe na dużą skalę |
| **HDF5** | Hierarchiczny format danych |
| **NetCDF** | Dane klimatyczne/naukowe |
| **stdlib** | Standardowa biblioteka Fortran |
| **fortran-os** | Interfejs systemu operacyjnego |
| **dla laboratorium** | Obliczenia naukowe |
| **M_tablica** | Narzędzia tablicowe |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **pFUnit** | Testy jednostkowe (NASA) |
| **Test Fortranu** | Proste testowanie |
| **jazda próbna** | Nowoczesne testowanie |
| **test fpm** | Wbudowany tester |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **fpiękniej** | Formatowanie kodu |
| **znalazca** | Wcięcie i formatowanie |
| **fortran-linter** | Linting |
| **komfort** | Refaktoryzacja |
| **KOKOSU** | Pokrycie kodu |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Obliczenia równoległe
| Technologia | Cel |
|------------|------------|
| **OpenMP** | Równoległość pamięci współdzielonej |
| **MPI** | Pamięć rozproszona (przekazywanie wiadomości) |
| **Coarrays** | Natywna równoległość Fortranu |
| **CUDA Fortran** | Obliczenia GPU |
| **OpenACC** | Procesor graficzny oparty na dyrektywach |
| **RÓB RÓWNIEŻ** | Pętle równoległe Fortran 2008 |
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

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **stdlib** | Biblioteka standardowa |
| **json-fortran** | Analiza JSON |
| **forutils** | Funkcje użytkowe |
| **KLAPA** | Analiza argumentów wiersza poleceń |
| **na_czas** | Obsługa daty/godziny |
| **Dobrze** | Obsługa plików |
| **forxml** | Analiza XML |
| **forpy** | Współpraca z Pythonem |
| **ISO_C_BINDING** | Interoperacyjność C |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Kod VS + nowoczesny Fortran** | Najlepszy Fortran LSP |
| **IntelliJ + wtyczka fortran** | Wsparcie JetBrains |
| **Neovim + forty** | Oparte na terminalu |
| **Zaćmienie + Fotoran** | Zaćmienie Fortranu |
| **Kod::Bloki** | Lekkie IDE |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Statyczny plik binarny** | `gfortran -static`|
| **Wspólna biblioteka** | `gfortran -shared`|
| **Współpraca C** | Wywołanie z C/C++ poprzez`ISO_C_BINDING`|
| **Współpraca z Pythonem** | f2py, forpy |
| **Doker** | Kontenerowy |
| **Klastry HPC** | MPI + SLURM |
---

## Streszczenie
Ekosystem Fortran został stworzony specjalnie z myślą o wysokowydajnych obliczeniach naukowych. Standardowy zestaw narzędzi to: **gfortran** lub **ifx** do kompilacji, **fpm** do zarządzania pakietami, **CMake** do kompilacji, **BLAS/LAPACK** do algebry liniowej, **OpenMP** i **MPI** do równoległości, **pFUnit** do testowania i **fprettify** do formatowania. Fortran specjalizuje się w obliczeniach numerycznych, symulacjach pogody, obliczeniowej dynamice płynów i wielkoskalowych symulacjach naukowych. Nowoczesny Fortran (2018/2023) z prostymi tablicami, DO CONCURRENT i ulepszonym OOP to wydajny nowoczesny język. Ekosystem jest niezbędny w HPC, modelowaniu klimatu i fizyce obliczeniowej.