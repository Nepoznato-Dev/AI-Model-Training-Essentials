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

# Fortran — Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, bibliotecas e infraestrutura essenciais do ecossistema Fortran.
---

## Padrões e compiladores Fortran
| Compilador | Plataforma | Notas |
|----------|----------|-------|
| **gfortran** | Plataforma cruzada | GNU Fortran (GCC), mais utilizado |
| **ifx/ifort** | Plataforma cruzada | Intel Fortran (oneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **flange** | Plataforma cruzada | Baseado em LLVM (novo) |
| **NAG** | Plataforma cruzada | Conformidade comercial e rigorosa |
| **Cray** | HPC | Supercomputadores Cray |
| **IBMXL** | HPC | Sistemas IBM |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Construir Sistemas
| Ferramenta | Tipo | Melhor para |
|------|------|----------|
| **CMake** | Plataforma cruzada | Padrão da indústria |
| **fpm** | Nativo de Fortran | Gerenciador de pacotes Fortran moderno |
| **Méson** | Moderno | Sintaxe rápida e limpa |
| **Fazer** | Clássico | Projetos simples |
| **SCons** | Baseado em Python | Construções complexas |
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

## Gerenciamento de pacotes
| Ferramenta | Finalidade |
|------|---------|
| **fpm** | Gerenciador de pacotes Fortran (moderno) |
| **Fortran stdlib** | Esforço de biblioteca padrão |
| **Conan** | Pacotes C/C++/Fortran |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Bibliotecas Científicas
| Biblioteca | Finalidade |
|--------|---------|
| **BLAS / LAPACK** | Álgebra linear |
| **OpenBLAS** | BLAS otimizado |
| **Intel MKL** | Biblioteca Intel Math Kernel |
| **FFW** | Transformadas rápidas de Fourier |
| **ARPACK** | Problemas de autovalores |
| **ScaLAPACK** | Álgebra linear paralela |
| **PETSc** | Computação científica paralela |
| **Trilinos** | Científico em grande escala |
| **HDF5** | Formato de dados hierárquico |
| **NetCDF** | Dados climáticos/científicos |
| **stdlib** | Biblioteca padrão Fortran |
| **fortran-os** | Interface do sistema operacional |
| **forlab** | Computação científica |
| **M_matriz** | Utilitários de matriz |
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

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **pFUnit** | Testes unitários (NASA) |
| **Teste Fortran** | Teste simples |
| **test-drive** | Testes modernos |
| **teste fpm** | Executor de testes integrado |
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

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **fpretificar** | Formatação de código |
| **descobrir** | Recuo e formatação |
| **fortran-linter** | Linting |
| **camfort** | Refatoração |
| **CoCoNuT** | Cobertura de código |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Computação Paralela
| Tecnologia | Finalidade |
|------------|---------|
| **OpenMP** | Paralelismo de memória compartilhada |
| **MPI** | Memória distribuída (passagem de mensagens) |
| **Coarrays** | Paralelismo nativo Fortran |
| **CUDAFortran** | Computação GPU |
| **AbertoACC** | GPU baseada em diretiva |
| **FAÇA CONCORRENTE** | Loops paralelos Fortran 2008 |
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

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **stdlib** | Biblioteca padrão |
| **json-fortran** | Análise JSON |
| **forutils** | Funções utilitárias |
| **ALTA** | Análise de argumentos de linha de comando |
| **por_tempo** | Tratamento de data/hora |
| **FinoR** | Tratamento de arquivos |
| **forxml** | Análise XML |
| **forpy** | Interoperabilidade Python |
| **ISO_C_BINDING** | Interoperabilidade C |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Código VS + Fortran moderno** | Melhor LSP Fortran |
| **IntelliJ + plug-in fortran** | Suporte JetBrains |
| **Neovim + fortes** | Baseado em terminal |
| **Eclipse + Fotran** | Eclipse Fortran |
| **Código::Blocos** | IDE leve |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Binário estático** | `gfortran -static`|
| **Biblioteca compartilhada** | `gfortran -shared`|
| **Interoperabilidade C** | Chamada de C/C++ via`ISO_C_BINDING`|
| **Interoperabilidade Python** | f2py, forpy |
| **Docker** | Contentorizado |
| **Clusters HPC** | MPI + SLURM |
---

## Resumo
O ecossistema do Fortran foi desenvolvido especificamente para computação científica de alto desempenho. O conjunto de ferramentas padrão é: **gfortran** ou **ifx** para compilação, **fpm** para gerenciamento de pacotes, **CMake** para compilações, **BLAS/LAPACK** para álgebra linear, **OpenMP** e **MPI** para paralelismo, **pFUnit** para testes e **fprettify** para formatação. Fortran é excelente em computação numérica, simulação meteorológica, dinâmica de fluidos computacional e simulações científicas em grande escala. Fortran moderno (2018/2023) com coarrays, DO CONCURRENT e OOP aprimorado é uma linguagem moderna capaz. O ecossistema é essencial em HPC, modelagem climática e física computacional.