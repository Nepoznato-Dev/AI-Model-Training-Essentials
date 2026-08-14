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
# Fortran - Mfumo wa ikolojia na Mwongozo wa zana
Mwongozo huu unashughulikia zana muhimu, maktaba, na miundombinu katika mfumo ikolojia wa Fortran.
---

## Viwango na Vikusanyaji vya Fortran
| Mkusanyaji | Jukwaa | Vidokezo |
|----------|----------|-------|
| **gfortran** | Jukwaa la msalaba | GNU Fortran (GCC), inayotumika sana |
| **ifx / ifort** | Jukwaa la msalaba | Intel Fortran (oneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **flang** | Jukwaa la msalaba | Msingi wa LLVM (mpya) |
| **NAG** | Jukwaa la msalaba | Kibiashara, kufuata madhubuti |
| **Cray** | HPC | Kompyuta kubwa za Cray |
| **IBM XL** | HPC | Mifumo ya IBM |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Kujenga Mifumo
| Zana | Andika | Bora Kwa |
|------|------|----------|
| **CMake** | Jukwaa la msalaba | Kiwango cha sekta |
| **fpm** | Mzaliwa wa Fortran | Meneja wa kifurushi cha kisasa cha Fortran |
| **Meson** | Kisasa | Haraka, sintaksia safi |
| **Tengeneza** | Classic | Miradi rahisi |
| **Scons** | Inayotokana na chatu | Miundo tata |
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

## Usimamizi wa Kifurushi
| Zana | Kusudi |
|------|----------|
| **fpm** | Meneja wa Kifurushi cha Fortran (kisasa) |
| **Fortran stdlib** | Juhudi za maktaba za kawaida |
| **Conan** | Vifurushi vya C/C++/Fortran |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Maktaba za Kisayansi
| Maktaba | Kusudi |
|---------|---------|
| **BLAS / LAPAC** | Aljebra ya mstari |
| **FunguaBLAS** | Imeboreshwa BLAS |
| **Intel MKL** | Maktaba ya Intel Math Kernel |
| **FFTW** | Fast Fourier inabadilisha |
| **ARPACK** | Eigenvalue matatizo |
| **ScaLAPACK** | Aljebra ya mstari sambamba |
| **PETSc** | Kompyuta sambamba ya kisayansi |
| **Trilino** | Kisayansi kikubwa |
| **HDF5** | Umbizo la data ya daraja |
| **NetCDF** | Data ya hali ya hewa/kisayansi |
| **stdlib** | Maktaba ya kawaida ya Fortran |
| **fortran-os** | Kiolesura cha OS |
| **forlab** | Kompyuta ya kisayansi |
| **M_safu** | Mkusanyiko wa huduma |
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

##Upimaji
| Mfumo | Kusudi |
|-----------|---------|
| **pFUnit** | Upimaji wa kitengo (NASA) |
| **Mtihani wa Fortran** | Mtihani rahisi |
| **jaribio-gari** | Mtihani wa kisasa |
| **mtihani wa fpm** | Kikimbiaji cha majaribio kilichojengewa ndani |
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

## Ubora wa Kanuni
| Zana | Kusudi |
|------|----------|
| **fpretify** | Uumbizaji wa msimbo |
| **mpata ** | Ujongezaji na uumbizaji |
| **fortran-linter** | Kuimba |
| **starehe** | Inarekebisha |
| **CoCoNuT** | Chanjo ya msimbo |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Kompyuta Sambamba
| Teknolojia | Kusudi |
|------------|---------|
| **OpenMP** | Usambamba wa kumbukumbu ya pamoja |
| **MPI** | Kumbukumbu-iliyosambazwa (Kupitisha Ujumbe) |
| **Msururu** | Usambamba wa asili wa Fortran |
| **CUDA Fortran** | Kompyuta ya GPU |
| **FunguaACC** | GPU kulingana na maagizo |
| **FANYA SAWASAWA** | Vitanzi sambamba vya Fortran 2008 |
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

## Maktaba Muhimu
| Maktaba | Kusudi |
|---------|---------|
| **stdlib** | Maktaba ya kawaida |
| **json-fortran** | Uchanganuzi wa JSON |
| **matumizi** | Vitendaji vya matumizi |
| **FLAP** | Uchanganuzi wa hoja ya mstari wa amri |
| **kwa_muda** | Tarehe/saa kushughulikia |
| **FiNeR** | Ushughulikiaji wa faili |
| **forxml** | Uchanganuzi wa XML |
| **forpy** | Python interop |
| **ISO_C_BINDING** | C mwingiliano |
---

## Vitambulisho na Vihariri
| ID | Nguvu |
|-----|------------|
| **VS Code + Modern Fortran** | Bora Fortran LSP |
| **IntelliJ + fortran-plugin** | JetBrains msaada |
| **Neovim + fortls** | Kulingana na terminal |
| **Eclipse + Photoran** | Eclipse Fortran |
| **Msimbo::Vizuizi** | IDE nyepesi |
---

## Usambazaji
| Mbinu | Vidokezo |
|--------|-------|
| **Binary tuli** | `gfortran -static`|
| **Maktaba iliyoshirikiwa** | `gfortran -shared`|
| **C interop** | Piga simu kutoka kwa C/C++ kupitia`ISO_C_BINDING`|
| **Python interop** | f2py, forpy |
| **Docker** | Imewekwa kwenye vyombo |
| **Vikundi vya HPC** | MPI + SLURM |
---

## Muhtasari
Mfumo ikolojia wa Fortran umeundwa kwa madhumuni ya kompyuta yenye utendaji wa juu wa kisayansi. Msururu wa zana wa kawaida ni: **gfortran** au **ifx** kwa ujumuishaji, **fpm** kwa usimamizi wa kifurushi, **CMake** kwa miundo, **BLAS/LAPACK** ya aljebra ya mstari, **OpenMP** na **MPI** kwa ulinganifu, **pFUnit** ya majaribio, na **fprettify** kwa uumbizaji. Fortran hufaulu katika kompyuta ya nambari, uigaji wa hali ya hewa, mienendo ya maji ya kukokotoa, na masimulizi makubwa ya kisayansi. Modern Fortran (2018/2023) yenye safu shirikishi, DO CONCURRENT, na OOP iliyoboreshwa ni lugha ya kisasa yenye uwezo. Mfumo ikolojia ni muhimu katika HPC, modeli ya hali ya hewa, na fizikia ya hesabu.