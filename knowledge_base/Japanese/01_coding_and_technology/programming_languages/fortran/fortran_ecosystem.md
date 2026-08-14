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

# Fortran — エコシステムとツールのガイド
このガイドでは、Fortran エコシステムの重要なツール、ライブラリ、インフラストラクチャについて説明します。
---

## Fortran 標準とコンパイラ
|コンパイラ |プラットフォーム |メモ |
|----------|----------|----------|
| **gfortran** |クロスプラットフォーム | GNU Fortran (GCC)、最も広く使用されています。
| **ifx / ifort** |クロスプラットフォーム |インテル Fortran (oneAPI) |
| **nvfortran** | GPU | NVIDIA Fortran (CUDA) |
| **フランジ** |クロスプラットフォーム | LLVM ベース (新規) |
| **NAG** |クロスプラットフォーム |商用、厳密な適合 |
| **クレイ** | HPC |クレイスーパーコンピューター |
| **IBM XL** | HPC | IBM システム |
```bash
gfortran --version          # check version
gfortran -o app main.f90    # compile
gfortran -O3 -march=native -o app main.f90  # optimized
ifx -o app main.f90         # Intel compiler
```

---

## ビルドシステム
|ツール |タイプ |最適な用途 |
|------|------|----------|
| **CMake** |クロスプラットフォーム |業界標準 |
| **fpm** | Fortran ネイティブ |最新の Fortran パッケージ マネージャー |
| **中間子** |モダン |高速でクリーンな構文 |
| **作る** |クラシック |単純なプロジェクト |
| **SCCon** | Python ベース |複雑なビルド |
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

## パッケージ管理
|ツール |目的 |
|-----|----------|
| **fpm** | Fortran パッケージ マネージャー (最新) |
| **Fortran 標準ライブラリ** |標準ライブラリの取り組み |
| **コナン** | C/C++/Fortran パッケージ |
```bash
# fpm with dependencies
fpm add stdlib
fpm add fortran正则
```

---

## 科学図書館
|図書館 |目的 |
|----------|----------|
| **ブラス / ラパック** |線形代数 |
| **OpenBLAS** |最適化されたBLAS |
| **インテル MKL** |インテル マス カーネル ライブラリ |
| **FFTW** |高速フーリエ変換 |
| **アーパック** |固有値の問題 |
| **スカラパック** |並列線形代数 |
| **PETSc** |並列科学計算 |
| **トリリノス** |大規模科学 |
| **HDF5** |階層データ形式 |
| **NetCDF** |気候/科学データ |
| **stdlib** | Fortran 標準ライブラリ |
| **fortran-os** | OSインターフェース |
| **フォーラボ** |科学コンピューティング |
| **M_配列** |配列ユーティリティ |
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

## テスト
|フレームワーク |目的 |
|----------|----------|
| **pFUnit** |単体テスト (NASA) |
| **Fortran テスト** |簡単なテスト |
| **試乗** |最新のテスト |
| **fpm テスト** |内蔵テストランナー |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **fprettify** |コードのフォーマット |
| **発見者** |インデントと書式設定 |
| **fortran-linter** |リンティング |
| **カムフォート** |リファクタリング |
| **ココナッツ** |コードカバレッジ |
```bash
fprettify main.f90        # format
findent < main.f90        # indent
```

---

## 並列コンピューティング
|テクノロジー |目的 |
|-----------|-----------|
| **OpenMP** |共有メモリ並列処理 |
| **MPI** |分散メモリ (メッセージ パッシング) |
| **共配列** | Fortran ネイティブ並列処理 |
| **CUDA Fortran** | GPUコンピューティング |
| **OpenACC** |ディレクティブベースの GPU |
| **同時実行** | Fortran 2008 並列ループ |
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

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **stdlib** |標準ライブラリ |
| **json-fortran** | JSON 解析 |
| **forutils** |ユーティリティ関数 |
| **フラップ** |コマンドライン引数の解析 |
| **当面** |日付/時刻の処理 |
| **FiNeR** |ファイル処理 |
| **forxml** | XML 解析 |
| **フォーピー** | Python 相互運用 |
| **ISO_C_BINDING** | C の相互運用性 |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **VS コード + モダン Fortran** |最高の Fortran LSP |
| **IntelliJ + fortran プラグイン** | JetBrains サポート |
| **ネオビム + フォートルズ** |ターミナルベース |
| **エクリプス + フォトラン** | Eclipse Fortran |
| **コード::ブロック** |軽量 IDE |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **静的バイナリ** | `gfortran -static`|
| **共有ライブラリ** | `gfortran -shared`|
| **C 相互運用機能** |`ISO_C_BINDING`経由で C/C++ から呼び出す |
| **Python 相互運用機能** | f2py、forpy |
| **ドッカー** |コンテナ化 |
| **HPC クラスター** | MPI + SLURM |
---

＃＃ まとめ
Fortran のエコシステムは、高性能科学コンピューティング専用に構築されています。標準ツールチェーンは次のとおりです。コンパイルには **gfortran** または **ifx**、パッケージ管理には **fpm**、ビルドには **CMake**、線形代数には **BLAS/LAPACK**、並列処理には **OpenMP** および **MPI**、テストには **pFUnit**、フォーマットには **fprettify** が使用されます。 Fortran は、数値計算、気象シミュレーション、数値流体力学、および大規模科学シミュレーションに優れています。 Coarray、DO CONCURRENT、改良された OOP を備えた Modern Fortran (2018/2023) は、有能な最新言語です。エコシステムは、HPC、気候モデリング、および計算物理学において不可欠です。