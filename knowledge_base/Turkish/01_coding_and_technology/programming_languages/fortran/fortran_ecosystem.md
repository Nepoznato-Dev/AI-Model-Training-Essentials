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
# Fortran — Ekosistem ve Takımlama Kılavuzu
Bu kılavuz Fortran ekosistemindeki temel araçları, kitaplıkları ve altyapıyı kapsar.
---

## Fortran Standartları ve Derleyicileri
| Derleyici | Platformu | Notlar |
|----------|----------|----------|
| **gfortran** | Çapraz platform | GNU Fortran (GCC), en yaygın kullanılan |
| **ifx / ifort** | Çapraz platform | Intel Fortran (oneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **flanş** | Çapraz platform | LLVM tabanlı (yeni) |
| **NAG** | Çapraz platform | Ticari, sıkı uyumluluk |
| **Cray** | HPC | Cray süper bilgisayarları |
| **IBM XL** | HPC | IBM sistemleri |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## Sistem Oluştur
| Araç | Tür | En İyisi |
|------|----------|----------|
| **CMake** | Çapraz platform | Endüstri standardı |
| **fpm** | Fortran-yerli | Modern Fortran paket yöneticisi |
| **Mezon** | Modern | Hızlı, temiz sözdizimi |
| **Yap** | Klasik | Basit projeler |
| **SCons** | Python tabanlı | Karmaşık yapılar |
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

## Paket Yönetimi
| Araç | Amaç |
|------|------------|
| **fpm** | Fortran Paket Yöneticisi (modern) |
| **Fortran stdlib** | Standart kütüphane çalışması |
| **Conan** | C/C++/Fortran paketleri |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## Bilimsel Kütüphaneler
| Kütüphane | Amaç |
|-----------|-----------|
| **BLAS / LAPACK** | Doğrusal cebir |
| **AçıkBLAS** | Optimize Edilmiş BLAS |
| **Intel MKL** | Intel Matematik Çekirdek Kitaplığı |
| **FFTW** | Hızlı Fourier dönüşümleri |
| **ARPACK** | Özdeğer problemleri |
| **ScaLAPACK** | Paralel doğrusal cebir |
| **PETSc** | Paralel bilimsel hesaplama |
| **Trilinos** | Büyük ölçekli bilimsel |
| **HDF5** | Hiyerarşik veri formatı |
| **NetCDF** | İklim/bilimsel veriler |
| **stdlib** | Fortran standart kütüphanesi |
| **fortran-os** | İşletim Sistemi arayüzü |
| **lab için** | Bilimsel hesaplama |
| **M_dizi** | Dizi yardımcı programları |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **pFUnit** | Birim testi (NASA) |
| **Fortran testi** | Basit test |
| **test sürüşü** | Modern testler |
| **fpm testi** | Yerleşik test çalıştırıcısı |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **fgüzelleştir** | Kod biçimlendirme |
| **bulucu** | Girinti ve biçimlendirme |
| **fortran-linter** | Linting |
| **kafort** | Yeniden Düzenleme |
| **CoCoNuT** | Kod kapsamı |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## Paralel Bilgi İşlem
| Teknoloji | Amaç |
|---------------|-----------|
| **OpenMP** | Paylaşılan bellek paralelliği |
| **MPI** | Dağıtılmış bellek (Mesaj Aktarma) |
| **Coarray'ler** | Fortran yerel paralellik |
| **CUDA Fortran** | GPU hesaplama |
| **ACC'yi açın** | Yönerge tabanlı GPU |
| **EŞzamanlı Yapın** | Fortran 2008 paralel döngüler |
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

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **stdlib** | Standart kütüphane |
| **json-fortran** | JSON ayrıştırma |
| **forutils** | Yardımcı işlevler |
| **FLAP** | Komut satırı bağımsız değişkeni ayrıştırma |
| **for_time** | Tarih/saat kullanımı |
| **FiNeR** | Dosya işleme |
| **forxml** | XML ayrıştırma |
| **forpy** | Python birlikte çalışma |
| **ISO_C_BINDING** | C birlikte çalışabilirliği |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + Modern Fortran** | En İyi Fortran LSP |
| **IntelliJ + fortran eklentisi** | JetBrains desteği |
| **Neovim + kaleler** | Terminal tabanlı |
| **Eclipse + Photran** | Tutulma Fortran |
| **Kod::Bloklar** | Hafif IDE |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Statik ikili** | `gfortran -static`|
| **Paylaşılan kitaplık** | `gfortran -shared`|
| **C birlikte çalışma** |`ISO_C_BINDING`aracılığıyla C/C++'dan çağrı |
| **Python birlikte çalışma** | f2py, forpy |
| **Docker** | Konteynerde |
| **HPC kümeleri** | MPI + SLURM |
---

## Özet
Fortran'ın ekosistemi, yüksek performanslı bilimsel bilgi işlem için özel olarak tasarlanmıştır. Standart araç zinciri şöyledir: derleme için **gfortran** veya **ifx**, paket yönetimi için **fpm**, derlemeler için **CMake**, doğrusal cebir için **BLAS/LAPACK**, paralellik için **OpenMP** ve **MPI**, test için **pFUnit** ve biçimlendirme için **fprettify**. Fortran sayısal hesaplama, hava durumu simülasyonu, hesaplamalı akışkanlar dinamiği ve büyük ölçekli bilimsel simülasyonlarda üstündür. Coarray'ler, DO CONCURRENT ve geliştirilmiş OOP ile modern Fortran (2018/2023), yetenekli bir modern dildir. Ekosistem HPC, iklim modelleme ve hesaplamalı fizik açısından önemlidir.