---
# Metadata
title: "C++ — Version History & Evolution"
description: "Comprehensive version history and evolution of C++ from C with Classes to C++26."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [cpp, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C++ — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
|シーフロント | 1983年 | 「クラスを使用した C」 — クラス、継承 |
| C++98 | 1998年 |最初の ISO 規格。 STL、テンプレート、例外 |
| C++03 | 2003年 |欠陥修正 |
| C++11 | 2011年 | **主要**: 移動セマンティクス、ラムダ、`auto`、スマート ポインター、`nullptr` |
| C++14 | 2014年 |汎用ラムダ、`auto` 戻り、`std::make_unique` |
| C++17 | 2017年 | `std::optional`、`std::variant`、`if constexpr`、構造化バインディング |
| C++20 | 2020年 | **主要**: 概念、範囲、コルーチン、モジュール、`std::span`、三方向比較 |
| C++23 | 2024年 | `std::expected`、`std::print`、`std::flat_map`、`this`を推定します。
| C++26 | ～2026年 | `std::execution`、反射 (予想)、契約 |
## 主要なマイルストーン
### 標準化以前の時代 (1983 ～ 1998 年)
- **1983**: Bjarne Stroustrup がベル研究所で「C with Classes」を作成
- **1985**: C++ に名前変更。 『C++ プログラミング言語』の初版
- **1989**: テンプレート、例外、名前空間が提案されました
- **1990**: STL (標準テンプレート ライブラリ)、Alexander Stepanov 著
- **1991**: テンプレートが標準化されました。 「注釈付き C++ リファレンス マニュアル」
### C++98 — 財団 (1998)
- クラス、継承、仮想関数
- テンプレート (関数、クラス、特殊化)
- STL:`vector`、`map`、`set`、`algorithm`、`iterator`
- 例外 (`try/catch/throw`)
-`namespace`、`bool`、`const_cast`、`dynamic_cast`
-`explicit`コンストラクター、`mutable` メンバー
- RTTI (`typeid`、`dynamic_cast`)
### C++11 — ルネッサンス (2011)
- **移動セマンティクス**:`&&`右辺値参照、`std::move` 
- **スマート ポインター**:`unique_ptr`、`shared_ptr`、`weak_ptr`
- **`auto`**: 型推論
- **`nullptr`**:`NULL`を置き換えます 
- **ラムダ**:`[](int x) { return x * 2; }`
- **対象範囲**:`for (auto& x : container)`
- **`constexpr`**: コンパイル時の計算
- **`static_assert`**: コンパイル時のアサーション
- **`using`**: 型エイリアス (`typedef`を置き換えます)
- **可変個引数テンプレート**:`template<typename... Args>`
- **`enum class`**: 厳密に型指定された列挙型
- **`override`/`final`**: 仮想関数制御
- **`std::thread`**: ネイティブ スレッド
- **`std::atomic`**: ロックフリー プログラミング
- **`std::function`/`std::bind`**: 第一級関数
### C++17 — 改良 (2017)
- `std::optional<T>`、`std::variant<T...>`、`std::any` 
-`if constexpr`— コンパイル時の分岐
- 構造化バインディング:`auto [x, y] = point;`
- XQZマーカー5XQZ 
- XQZマーカー6XQZ 
- 並列アルゴリズム:`std::execution::par`
- ネストされた名前空間:`namespace A::B::C {}`
- `[[nodiscard]]`、`[[maybe_unused]]`、`[[fallthrough]]`
### C++20 — 現代言語 (2020)
- **概念**:`template<std::integral T>`— 制約付きテンプレート
- **範囲**:`views::filter`、`views::transform`— 遅延パイプライン
- **コルーチン**:`co_await`、`co_yield`、`co_return`
- **モジュール**:`import`/`export`— コンパイルの高速化
- **`std::span`**: 連続データの非所有ビュー
- **3者間比較**:`<=>`(宇宙船操縦者)
- **`std::format`**: Python スタイルの書式設定
- **`consteval`/`constinit`**: コンパイル時の強制
- **指定された初期化子**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: 停止トークンを使用した自動参加スレッド
### C++23 — 実用的な改善 (2024)
-`std::expected<T, E>`— Rust 風のエラー処理
-`std::print`/`std::println`— 高速フォーマットされた出力
- `std::flat_map`、`std::flat_set` 
-`this`の推定 — 明示的なオブジェクト パラメーター
-`std::mdspan`— 多次元スパン
-`std::generator`— 同期発電機
-`#include <debugging>`— ブレークポイント、ダンプ
## 主要なパターンの進化
```
Memory Management:
  1998: Raw pointers, manual new/delete
  2011: Smart pointers (unique_ptr, shared_ptr)
  2020: std::span, views (zero-copy abstractions)
  2023: std::expected (error without exceptions)

Error Handling:
  1998: Exceptions (try/catch)
  2011: noexcept, error codes
  2023: std::expected (Rust-inspired)
  2026: Contracts (expected)

Concurrency:
  1998: None (OS threads)
  2011: std::thread, std::mutex, std::atomic
  2017: Parallel algorithms
  2020: Coroutines, std::jthread

Abstraction:
  1998: Templates (unconstrained)
  2011: Move semantics, perfect forwarding
  2020: Concepts (constrained templates)
```

## 標準プロセス
```
1998: C++98 (ISO/IEC 14882:1998)
2003: C++03 (defect fixes)
2011: C++11 — "modern C++" begins
2014: C++14 — incremental
2017: C++17 — incremental
2020: C++20 — another revolution
2024: C++23 — practical improvements
2026: C++26 — reflection, contracts (expected)

3-year release cycle since C++11
```

## 生態系への影響
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
