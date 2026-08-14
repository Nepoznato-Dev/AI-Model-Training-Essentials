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
# Fortran — Guide de l'écosystème et des outils
Ce guide couvre les outils, bibliothèques et infrastructures essentiels de l'écosystème Fortran.
---

## Normes et compilateurs Fortran
| Compilateur | Plateforme | Remarques |
|----------|----------|-------|
| **gfortran** | Multiplateforme | GNU Fortran (GCC), le plus utilisé |
| **ifx / iffort** | Multiplateforme | Intel Fortran (uneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **bride** | Multiplateforme | Basé sur LLVM (nouveau) |
| **NAG** | Multiplateforme | Commercial, stricte conformité |
| **Cray** | CHP | Supercalculateurs Cray |
| **IBMXL** | CHP | Systèmes IBM |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Construire des systèmes
| Outil | Tapez | Idéal pour |
|------|------|----------|
| **CMake** | Multiplateforme | Norme industrielle |
| **fpm** | Fortran-natif | Gestionnaire de paquets Fortran moderne |
| **Méson** | Moderne | Syntaxe rapide et propre |
| **Faire** | Classique | Projets simples |
| **SCons** | Basé sur Python | Constructions complexes |
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

## Gestion des paquets
| Outil | Objectif |
|------|--------------|
| **fpm** | Gestionnaire de packages Fortran (moderne) |
| **librairie Fortran** | Effort de bibliothèque standard |
| **Conan** | Packages C/C++/Fortran |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Bibliothèques scientifiques
| Bibliothèque | Objectif |
|---------|---------|
| **BLAS / LAPACK** | Algèbre linéaire |
| **OuvrirBLAS** | BLAS optimisé |
| **Intel MKL** | Bibliothèque du noyau mathématique Intel |
| **FFTW** | Transformées de Fourier rapides |
| **ARPACK** | Problèmes de valeurs propres |
| **ScaLAPACK** | Algèbre linéaire parallèle |
| **ScEP** | Calcul scientifique parallèle |
| **Trilinos** | Scientifique à grande échelle |
| **HDF5** | Format de données hiérarchique |
| **NetCDF** | Données climatiques/scientifiques |
| **stdlib** | Bibliothèque standard Fortran |
| **fortran-os** | Interface du système d'exploitation |
| **pourlab** | Calcul scientifique |
| **M_array** | Utilitaires de tableau |
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

## Tests
| Cadre | Objectif |
|-----------|---------|
| **pFUnit** | Tests unitaires (NASA) |
| **Test Fortran** | Tests simples |
| **essai routier** | Tests modernes |
| **test fpm** | Lanceur de test intégré |
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

## Qualité du code
| Outil | Objectif |
|------|--------------|
| **fjoindre** | Formatage des codes |
| **trouver** | Indentation et formatage |
| **fortran-linter** | Peluche |
| **camfort** | Refactorisation |
| **noix de coco** | Couverture du code |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Calcul parallèle
| Technologie | Objectif |
|------------|---------|
| **OpenMP** | Parallélisme de mémoire partagée |
| **MPI** | Mémoire distribuée (passage de messages) |
| **Coarrays** | Parallélisme natif Fortran |
| **CUDA Fortran** | Calcul GPU |
| **OpenACC** | GPU basé sur des directives |
| **FAIRE CONCURRENT** | Boucles parallèles Fortran 2008 |
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

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **stdlib** | Bibliothèque standard |
| **json-fortran** | Analyse JSON |
| **forutils** | Fonctions utilitaires |
| **Rabat** | Analyse des arguments de ligne de commande |
| **pour_temps** | Gestion date/heure |
| **Plus fin** | Gestion des fichiers |
| **forxml** | Analyse XML |
| **forpy** | Interopérabilité Python |
| **ISO_C_BINDING** | Interopérabilité C |
---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **Code VS + Fortran moderne** | Meilleur LSP Fortran |
| **IntelliJ + plugin fortran** | Prise en charge de JetBrains |
| **Neovim + forts** | Basé sur un terminal |
| **Éclipse + Photran** | Éclipse Fortran |
| **Code ::Blocs** | IDE léger |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Binaire statique** | `gfortran -static`|
| **Bibliothèque partagée** | `gfortran -shared`|
| **Interopérabilité C** | Appel depuis C/C++ via`ISO_C_BINDING`|
| **Interopérabilité Python** | f2py, forpy |
| **Docker** | Conteneurisé |
| **Clusters HPC** | MPI + SLURM |
---

## Résumé
L'écosystème de Fortran est spécialement conçu pour le calcul scientifique haute performance. La chaîne d'outils standard est : **gfortran** ou **ifx** pour la compilation, **fpm** pour la gestion des packages, **CMake** pour les builds, **BLAS/LAPACK** pour l'algèbre linéaire, **OpenMP** et **MPI** pour le parallélisme, **pFUnit** pour les tests et **fprettify** pour le formatage. Fortran excelle dans le calcul numérique, la simulation météorologique, la dynamique des fluides computationnelle et les simulations scientifiques à grande échelle. Le Fortran moderne (2018/2023) avec des coarrays, DO CONCURRENT et une POO améliorée est un langage moderne performant. L’écosystème est essentiel dans le HPC, la modélisation climatique et la physique computationnelle.