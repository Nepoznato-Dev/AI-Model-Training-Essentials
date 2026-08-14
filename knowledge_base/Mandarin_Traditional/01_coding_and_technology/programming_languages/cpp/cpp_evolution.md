---
# Metadata
title: "C++ — Version History & Evolution"
description: "Comprehensive version history and evolution of C++ from C with Classes to C++26."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# C++ — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
|前線 | 1983 | “C with Classes” — 類別、繼承 |
| C++98 | C++98 1998 |第一個 ISO 標準； STL、模板、例外 |
| C++03 | 2003 |缺陷修復 |
| C++11 | C++11 2011 | **主要**：移動語意、lambda、`auto`、智慧型指標、`nullptr`|
| C++14 | C++14 2014 |通用 lambda、`auto` 返回、`std::make_unique` |
| C++17 | C++17 2017 | 2017`std::optional`、`std::variant`、`if constexpr`、結構化綁定 |
| C++20 | C++20 2020 | **主要**：概念、範圍、協程、模組、`std::span`、三向比較 |
| C++23 | C++23 2024 | 2024`std::expected`、`std::print`、`std::flat_map`，推導`this`|
| C++26 | C++26 ~2026 |`std::execution`，反射（預期），合約 |
## 主要里程碑
### 前標準時代（1983–1998）
- **1983**：Bjarne Stroustrup 在貝爾實驗室創建了“C with Classes”
- **1985**：更名為 C++；《C++ 程式語言》第一版
- **1989**：提出範本、例外、命名空間
- **1990**：STL（標準範本庫），作者：Alexander Stepanov
- **1991**：模板標準化； 《帶註釋的 C++ 參考手冊》
### C++98 — 基礎 (1998)
- 類別、繼承、虛函數
- 模板（函數、類別、專業化）
- STL：`vector`、`map`、`set`、`algorithm`、`iterator`
- 例外（`try/catch/throw`）
- `namespace`、`bool`、`const_cast`、`dynamic_cast`
-`explicit`建構子、`mutable` 成員
- RTTI（`typeid`、`dynamic_cast`）
### C++11 — 文藝復興 (2011)
- **移動語意**：`&&` 右值引用、`std::move`
- **智慧型指標**：`unique_ptr`、`shared_ptr`、`weak_ptr`
- **`auto`**：型別推斷
- **`nullptr`**：替換 `NULL`
- **Lambda**：`[](int x) { return x * 2; }`
- **範圍**：`for (auto& x : container)`
- **`constexpr`**：編譯時計算
- **`static_assert`**：編譯時斷言
- **`using`**：型別別名（取代`typedef`）
- **可變參數模板**：`template<typename... Args>`
- **`enum class`**：強型別枚舉
- **`override`/`final`**：虛擬功能控制
- **`std::thread`**：本機線程
- **`std::atomic`**：無鎖編程
- **`std::function`/`std::bind`**：一流的功能
### C++17 — 細化 (2017)
- `std::optional<T>`、`std::variant<T...>`、`std::any`
-`if constexpr`— 編譯時分支
- 結構化綁定：`auto [x, y] = point;`
- `std::filesystem`
- `std::string_view`
- 平行演算法：`std::execution::par`
- 嵌套命名空間：`namespace A::B::C {}`
- `[[nodiscard]]`、`[[maybe_unused]]`、`[[fallthrough]]`
### C++20 — 現代語言 (2020)
- **概念**：`template<std::integral T>` — 限制模板
- **範圍**：`views::filter`、`views::transform`— 惰性管道
- **協程**：`co_await`、`co_yield`、 `co_return`
- **模組**：`import` /`export`— 更快的編譯
- **`std::span`**：連續資料的非擁有視圖
- **三向比較**：`<=>`（飛船操作員）
- **`std::format`**：Python 風格的格式化
- **`consteval`/`constinit`**：編譯時強制
- **指定初始化程序**：`Point{.x = 1, .y = 2}`
- **`std::jthread`**：帶有停止標記的自動加入線程
### C++23 — 實際改善 (2024)
-`std::expected<T, E>`— Rust 啟發的錯誤處理
-`std::print`/`std::println`— 快速格式化輸出
-`std::flat_map`, `std::flat_set`
- 推導`this`— 明確物件參數
-`std::mdspan`— 多維跨度
-`std::generator`— 同步發電機
-`#include <debugging>`— 斷點、轉儲
## 關鍵模式的演變
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

## 標準流程
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

## 生態系影響
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
