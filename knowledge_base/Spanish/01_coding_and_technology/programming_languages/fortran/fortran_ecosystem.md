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
# Fortran: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, bibliotecas e infraestructura esenciales en el ecosistema de Fortran.
---

## Estándares y compiladores de Fortran
| Compilador | Plataforma | Notas |
|----------|----------|-------|
| **gfortran** | Multiplataforma | GNU Fortran (GCC), el más utilizado |
| **ifx/ifort** | Multiplataforma | Intel Fortran (una API) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **brida** | Multiplataforma | Basado en LLVM (nuevo) |
| **NAG** | Multiplataforma | Comercial, estricta conformidad |
| **Cray** | HPC | Supercomputadoras Cray |
| **IBMXL** | HPC | Sistemas IBM |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Construir sistemas
| Herramienta | Tipo | Mejor para |
|------|------|----------|
| **CMake** | Multiplataforma | Estándar de la industria |
| **pies por minuto** | Nativo de Fortran | Administrador de paquetes Fortran moderno |
| **Mesón** | Moderno | Sintaxis rápida y limpia |
| **Hacer** | Clásico | Proyectos sencillos |
| **Contras** | Basado en Python | Construcciones complejas |
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

## Gestión de paquetes
| Herramienta | Propósito |
|------|---------|
| **pies por minuto** | Administrador de paquetes Fortran (moderno) |
| **Fortran stdlib** | Esfuerzo de biblioteca estándar |
| **Conan** | Paquetes C/C++/Fortran |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Bibliotecas científicas
| Biblioteca | Propósito |
|---------|---------|
| **BLAS/LAPACK** | Álgebra lineal |
| **OpenBLAS** | BLAS optimizado |
| **Intel MKL** | Biblioteca del núcleo matemático Intel |
| **FFTW** | Transformadas rápidas de Fourier |
| **ARPACK** | Problemas de valores propios |
| **ScaLAPACK** | Álgebra lineal paralela |
| **MASCOTASc** | Computación científica paralela |
| **Trilinos** | Científico a gran escala |
| **HDF5** | Formato de datos jerárquico |
| **NetCDF** | Datos climáticos/científicos |
| **stdlib** | Biblioteca estándar Fortran |
| **fortran-os** | Interfaz del sistema operativo |
| **forlab** | Computación científica |
| **M_matriz** | Utilidades de matriz |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **pFUnidad** | Pruebas unitarias (NASA) |
| **Prueba de Fortran** | Pruebas sencillas |
| **prueba de manejo** | Pruebas modernas |
| **prueba de fpm** | Corredor de prueba incorporado |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **fprettify** | Formato de código |
| **encontrar** | Sangría y formato |
| **fortran-linter** | pelusa |
| **comodidad** | Refactorización |
| **CoCo** | Cobertura de código |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Computación paralela
| Tecnología | Propósito |
|------------|---------|
| **OpenMP** | Paralelismo de memoria compartida |
| **IPM** | Memoria distribuida (paso de mensajes) |
| **Coarrays** | Paralelismo nativo de Fortran |
| **CUDA Fortran** | Computación GPU |
| **OpenACC** | GPU basada en directivas |
| **HACER CONCURRENTE** | Bucles paralelos Fortran 2008 |
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

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **stdlib** | Biblioteca estándar |
| **json-fortran** | Análisis JSON |
| **forutils** | Funciones de utilidad |
| **SOLETA** | Análisis de argumentos de línea de comandos |
| **por_tiempo** | Manejo de fecha/hora |
| **FiNeR** | Manejo de archivos |
| **forxml** | Análisis XML |
| **forpy** | Interoperabilidad de Python |
| **ISO_C_BINDING** | Interoperabilidad C |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Código VS + Fortran moderno** | Mejor LSP de Fortran |
| **IntelliJ + complemento fortran** | Soporte de JetBrains |
| **Neovim + fuertes** | Basado en terminal |
| **Eclipse + Photran** | Eclipse Fortrán |
| **Código::Bloques** | IDE ligero |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Binario estático** | `gfortran -static`|
| **Biblioteca compartida** | `gfortran -shared`|
| **Interoperabilidad C** | Llamada desde C/C++ a través de`ISO_C_BINDING`|
| **Interoperabilidad de Python** | f2py,forpy |
| **Acoplador** | En contenedores |
| **Clústeres de HPC** | IPM + SLURM |
---

## Resumen
El ecosistema de Fortran está diseñado específicamente para la informática científica de alto rendimiento. La cadena de herramientas estándar es: **gfortran** o **ifx** para compilación, **fpm** para administración de paquetes, **CMake** para compilaciones, **BLAS/LAPACK** para álgebra lineal, **OpenMP** y **MPI** para paralelismo, **pFUnit** para pruebas y **fprettify** para formateo. Fortran destaca en computación numérica, simulación meteorológica, dinámica de fluidos computacional y simulaciones científicas a gran escala. Fortran moderno (2018/2023) con coarrays, DO CONCURRENT y programación orientada a objetos mejorada es un lenguaje moderno capaz. El ecosistema es esencial en HPC, modelado climático y física computacional.