---
# Metadata
title: "Fortran — Version History & Evolution"
description: "Comprehensive version history and evolution of Fortran from Fortran I to modern Fortran."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [fortran, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Fortran — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
|フォートラン I | 1957年 | **最初の高級言語** (John Backus、IBM) |
|フォートラン II | 1958年 |サブルーチン、関数 |
|フォートラン IV | 1962年 | `DATA`、`EQUIVALENCE`、`COMMON`|
|フォートラン66 | 1966年 | **最初の ANSI 規格** (X3.4-1966) |
|フォートラン77 | 1977年 | **構造化プログラミング**:`IF`/`THEN`/`ELSE`、`CHARACTER`、リスト指向 I/O |
|フォートラン90 | 1991年 | **主要**: 自由形式のソース、モジュール、配列、`ALLOCATABLE`、`SELECT CASE`|
|フォートラン95 | 1997年 | `FORALL`、`WHERE`、純粋/要素プロシージャ |
|フォートラン2003 | 2004年 | **OOP**: クラス、継承、ポリモーフィズム、`PROCEDURE` ポインター、`IEEE` 算術演算 |
|フォートラン 2008 | 2010年 | **Coarrays** (並列プログラミング)、`SUBMODULE`、`DO CONCURRENT`|
|フォートラン 2018 | 2018年 | **共同配列の強化**、`ASSOCIATE`、`TYPE IS`の改善 |
|フォートラン 2023 | 2024年 | **`BLOCK`**、`ALLOCATE` の改善、`SELECT RANK` 、符号なし整数 |
## 主要なマイルストーン
### Fortran I ～ IV: 高水準プログラミングの誕生 (1957 ～ 1965 年)
- **1957**: John Backus と IBM のチームが Fortran を作成 (数式翻訳)
- **広く使用されている最初の高級プログラミング言語**
- **Fortran I**:`DO`ループ、`IF`、`GO TO`、算術式を導入しました。
- **Fortran II (1958)**: サブルーチンと関数 (個別にコンパイル)
- **Fortran IV (1962)**:`DATA`、`EQUIVALENCE`、`COMMON`ブロック
- 固定形式ソース: ラベルの列 1 ～ 6、コードの列 7 ～ 72
### FORTRAN 66 & 77: 標準化 (1966 ～ 1990 年)
- **FORTRAN 66**: 最初の ANSI 標準 — ポータブル Fortran
- **FORTRAN 77 (1977)**: 古典的
  - 構造化プログラミング:`IF`/`THEN`/`ELSE`/`ENDIF`
  ・`CHARACTER`型（文字列扱い）
  - リスト指向I/O (`*`形式)
  -`PARAMETER`(名前付き定数)
  -`ENTRY`(複数のエントリ ポイント)
  - 現在でも科学計算で広く使用されています
### Fortran 90: 現代革命 (1991)
- **自由形式のソース** — 列の制限がなくなりました
- **モジュール** — カプセル化、`USE` 
- **動的配列** —`ALLOCATABLE`、`ALLOCATE`
- **配列操作** — 配列全体の構文`a = b + c`
-`SELECT CASE`— 構造化分岐
-`IMPLICIT NONE`— 変数宣言が必要です
- 再帰的手続き
- ポインター
- 演算子のオーバーロード
- 派生型 (構造体)
### Fortran 95–2003: OOP の登場 (1997–2004)
- **Fortran 95**:`FORALL`、`WHERE`、純粋/要素プロシージャ
- **Fortran 2003**: **完全な OOP**
  - クラス (型バインドされたプロシージャを持つ派生型)
  - 継承 (`EXTENDS`)
  - ポリモーフィズム (`CLASS`、`SELECT TYPE`)
  - 手順のポインタ
  - IEEE浮動小数点制御
  -`FLUSH`ステートメント
  - I/O 用 `NEWUNIT`
### Fortran 2008–2023: パラレル & モダン (2010–現在)
- **Fortran 2008**: **Coarrays** — 言語に組み込まれた並列プログラミング
  -`DO CONCURRENT`— 並列ループ構造
  -`SUBMODULE`— モジュール式プログラミング
  -`CONTIGUOUS`属性
- **Fortran 2018**: 強化された coarrays、`ASSOCIATE` の改善、チーム
- **Fortran 2023**:`BLOCK`構造の改善、`ALLOCATE` の機能強化、`SELECT RANK`、符号なし整数
## 構文の進化
```fortran
C     FORTRAN 77: Fixed-form, structured programming
      PROGRAM HELLO
      INTEGER I
      DO 10 I = 1, 10
         PRINT *, 'Iteration: ', I
   10 CONTINUE
      END

! Fortran 90: Free-form, modules, arrays
program hello
  implicit none
  integer :: i
  real, dimension(10) :: values
  do i = 1, 10
    values(i) = real(i) * 2.0
  end do
  print *, sum(values)
end program hello

! Fortran 90: Array operations (no loops needed!)
program array_ops
  implicit none
  real :: a(100), b(100), c(100)
  a = [(real(i), i=1,100)]  ! array constructor
  b = sin(a)
  c = a + b                  ! whole-array operation
  print *, sum(c)
end program array_ops

! Fortran 2003: Object-oriented
module shapes
  implicit none
  type :: shape
    character(len=20) :: name
  contains
    procedure :: area => shape_area
  end type

  type, extends(shape) :: circle
    real :: radius
  contains
    procedure :: area => circle_area
  end type
contains
  function shape_area(self) result(a)
    class(shape), intent(in) :: self
    real :: a
    a = 0.0
  end function
  function circle_area(self) result(a)
    class(circle), intent(in) :: self
    real :: a
    a = 3.14159 * self%radius**2
  end function
end module

! Fortran 2008: Coarrays (parallel)
program parallel_example
  implicit none
  real :: data[*]  ! coarray — one element per image
  data = real(this_image())  ! each image gets its number
  sync all
  if (this_image() == 1) then
    print *, 'Image 2 has:', data[2]
  end if
end program

! Fortran 2008: DO CONCURRENT
program concurrent_loop
  implicit none
  real :: a(1000)
  integer :: i
  do concurrent (i = 1:1000)
    a(i) = sin(real(i)) * cos(real(i))
  end do
end program
```

## 機能の進化
```
Fortran I (1957):   DO loops, IF, GO TO, arithmetic expressions
Fortran II (1958):  Subroutines, functions
Fortran IV (1962):  DATA, EQUIVALENCE, COMMON
FORTRAN 66 (1966):  First standard
FORTRAN 77 (1977):  IF/THEN/ELSE, CHARACTER, list-directed I/O
Fortran 90 (1991):  Free-form, modules, arrays, ALLOCATABLE, SELECT CASE
Fortran 95 (1997):  FORALL, WHERE, pure/elemental
Fortran 2003 (2004): OOP, IEEE arithmetic, procedure pointers
Fortran 2008 (2010): Coarrays, DO CONCURRENT, SUBMODULE
Fortran 2018 (2018): Enhanced coarrays, teams
Fortran 2023 (2024): BLOCK, SELECT RANK, unsigned integers
```

## 主要な設計原則
```
1. "Performance first" — designed for number crunching
2. "Array-native" — whole-array operations (no loops needed)
3. "Backward compatible" — 60+ years of code still compiles
4. "Scientific" — built for physics, engineering, climate modeling
5. "Parallel-ready" — coarrays built into the language (since 2008)
6. "Stable" — no hype, just computation
```

## エコシステムの成長
```
1957: Fortran I — first high-level language (IBM 704)
1966: FORTRAN 66 — first standard
1977: FORTRAN 77 — the classic (still used in legacy code)
1991: Fortran 90 — modern Fortran begins
2003: Fortran 2003 — OOP
2008: Fortran 2008 — parallel programming (coarrays)
2018: Fortran 2018 — enhanced parallelism
2024: Fortran 2023 — continued modernization
2025: Fortran powers:
       - Weather/climate modeling (WRF, CESM)
       - Computational fluid dynamics
       - Quantum chemistry (Gaussian, GAMESS)
       - Nuclear physics simulations
       - Financial modeling (legacy systems)
       Compilers: gfortran, ifx (Intel), nvfortran (NVIDIA), flang
```
