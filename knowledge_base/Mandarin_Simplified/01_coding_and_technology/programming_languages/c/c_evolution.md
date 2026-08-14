---
# Metadata
title: "C — Version History & Evolution"
description: "Comprehensive version history and evolution of C from K&R to C23."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [c, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# C — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
| K＆R C | 1972–78 |原创 C（Kernighan 和 Ritchie）|
| C89/C90 | 1989/90 |第一个 ANSI/ISO 标准 |
| C95| 1995 |修正 1：`wchar.h`，二合字母 |
| C99 | C99 1999 | `//`注释、`inline` 、`bool`、VLA、指定初始值设定项 |
| C11 | 2011 |原子、线程、`_Static_assert`、匿名结构/联合 |
| C17 | C17 2018 |缺陷修复（无新功能）|
| C23 | C23 2024 | 2024  `nullptr`、`typeof`、`constexpr`、`#embed`、属性 |
## 主要里程碑
### K&R C (1972–1989)
- **1972**：Dennis Ritchie 在贝尔实验室为 Unix 创建了 C
- **1978**：Kernighan 和 Ritchie 出版“C 编程语言”
- 主要特性：`struct`、`int`、`char`、指针、函数、`#include` 
- 没有`void`、没有`enum`、没有`unsigned`、没有 `const`
### C89/C90 — 标准 (1989)
- 第一个 ANSI 标准 (ANSI X3.159-1989)
- 新增：`void`、`enum`、`const`、`volatile`、函数原型、`signed`
- “黄金时代”——便携、广泛采用
- 仍然是许多嵌入式系统的基准
### C99 — 现代 C (1999)
-`//`单行注释
-`inline`功能
-`bool`通过`<stdbool.h>`
- 可变长度数组（VLA）
- 指定初始化器：`struct Point p = {.x = 1, .y = 2};` 
-`for (int i = 0; ...)`— 循环中的声明
-`<stdint.h>`:`int32_t`,`uint64_t`等
-`restrict`关键字
- 可变参数宏
- 复合文字
### C11 — 安全与并发 (2011)
-`<stdatomic.h>`— 原子操作
-`<threads.h>`— 线程支持
-`_Static_assert`— 编译时断言
- 嵌套结构中的匿名结构/联合
-`_Alignof`,`_Alignas`— 对齐控制
- 通用选择：`_Generic(x, int: ..., default: ...)` 
- Unicode 支持：`<uchar.h>` 
- 可选的 VLA 支持（由于嵌入式问题而成为可选）
### C23 — 文艺复兴 (2024)
-`nullptr`— 空指针常量（替换`NULL`宏）
-`typeof`— 类型推断
-`constexpr`— 常量表达式
-`#embed`— 在编译时嵌入二进制数据
-`[[attribute]]`语法（C23 样式属性）
-`true`/`false`作为关键字（不再需要`<stdbool.h>`）
-`auto`类型推断
- `static_assert`（无下划线）
- `alignof`（无下划线）
- 默认`int`返回已删除
## 标准流程
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## 兼容性理念
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## 预处理器的演变
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## 类型系统的演变
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## 生态系统影响
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
