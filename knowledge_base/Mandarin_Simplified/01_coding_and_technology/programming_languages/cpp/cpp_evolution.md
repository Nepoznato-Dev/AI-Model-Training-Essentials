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
# C++ — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
|前线 | 1983 | “C with Classes” — 类、继承 |
| C++98 | C++98 1998 |第一个 ISO 标准； STL、模板、例外 |
| C++03 | 2003 |缺陷修复 |
| C++11 | C++11 2011 | **主要**：移动语义、lambda、`auto`、智能指针、`nullptr`|
| C++14 | C++14 2014年|通用 lambda、`auto` 返回、`std::make_unique` |
| C++17 | C++17 2017 | 2017 `std::optional`、`std::variant`、`if constexpr`、结构化绑定 |
| C++20 | C++20 2020 | **主要**：概念、范围、协程、模块、`std::span`、三向比较 |
| C++23 | C++23 2024 | 2024 `std::expected`、`std::print`、`std::flat_map`，推导`this`|
| C++26 | C++26 ~2026 | `std::execution`，反射（预期），合约 |
## 主要里程碑
### 前标准时代（1983–1998）
- **1983**：Bjarne Stroustrup 在贝尔实验室创建了“C with Classes”
- **1985**：更名为 C++； 《C++ 编程语言》第一版
- **1989**：提出模板、例外、命名空间
- **1990**：STL（标准模板库），作者：Alexander Stepanov
- **1991**：模板标准化； 《带注释的 C++ 参考手册》
### C++98 — 基础 (1998)
- 类、继承、虚函数
- 模板（函数、类、专业化）
- STL：`vector`、`map`、`set`、`algorithm`、`iterator` 
- 例外（`try/catch/throw`）
- `namespace`、`bool`、`const_cast`、`dynamic_cast` 
-`explicit`构造函数、`mutable` 成员
- RTTI（`typeid`、`dynamic_cast`）
### C++11 — 文艺复兴 (2011)
- **移动语义**：`&&` 右值引用、`std::move` 
- **智能指针**：`unique_ptr`、`shared_ptr`、`weak_ptr` 
- **`auto`**：类型推断
- **`nullptr`**：替换`NULL`
- **Lambda**：`[](int x) { return x * 2; }` 
- **范围**：`for (auto& x : container)` 
- **`constexpr`**：编译时计算
- **`static_assert`**：编译时断言
- **`using`**：类型别名（替换`typedef`）
- **可变参数模板**：`template<typename... Args>` 
- **`enum class`**：强类型枚举
- **`override`/`final`**：虚拟功能控制
- **`std::thread`**：本机线程
- **`std::atomic`**：无锁编程
- **`std::function`/`std::bind`**：一流的功能
### C++17 — 细化 (2017)
- `std::optional<T>`、`std::variant<T...>`、`std::any` 
-`if constexpr`— 编译时分支
- 结构化绑定：`auto [x, y] = point;` 
-`std::filesystem`
-`std::string_view`
- 并行算法：`std::execution::par` 
- 嵌套命名空间：`namespace A::B::C {}` 
- `[[nodiscard]]`、`[[maybe_unused]]`、`[[fallthrough]]`
### C++20 — 现代语言 (2020)
- **概念**：`template<std::integral T>` — 约束模板
- **范围**：`views::filter`、`views::transform`— 惰性管道
- **协程**：`co_await`、`co_yield`、`co_return`
- **模块**：`import` /`export`— 更快的编译
- **`std::span`**：连续数据的非拥有视图
- **三向比较**：`<=>`（飞船操作员）
- **`std::format`**：Python 风格的格式化
- **`consteval`/`constinit`**：编译时强制
- **指定初始化程序**：`Point{.x = 1, .y = 2}` 
- **`std::jthread`**：带有停止标记的自动加入线程
### C++23 — 实际改进 (2024)
-`std::expected<T, E>`— Rust 启发的错误处理
-`std::print`/`std::println`— 快速格式化输出
-`std::flat_map`,`std::flat_set`
- 推导`this`— 显式对象参数
-`std::mdspan`— 多维跨度
-`std::generator`— 同步发电机
-`#include <debugging>`— 断点、转储
## 关键模式的演变
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

## 标准流程
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

## 生态系统影响
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
