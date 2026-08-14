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

# C — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| K＆R C | 1972–78 |原創 C（Kernighan 和 Ritchie）|
| C89/C90 | 1989/90 |第一個 ANSI/ISO 標準 |
| C95| 1995 |修正 1：`wchar.h`，二合字母 |
| C99 | C99 1999 |`//`註解、`inline` 、`bool`、VLA、指定初始值設定項 |
| C11 | 2011 |原子、線程、`_Static_assert`、匿名結構/聯合 |
| C17 | C17 2018 |缺陷修復（無新功能）|
| C23 | C23 2024 | 2024 `nullptr`、`typeof`、`constexpr`、`#embed`、屬性 |
## 主要里程碑
### K&R C (1972–1989)
- **1972**：Dennis Ritchie 在貝爾實驗室為 Unix 創建了 C
- **1978**：Kernighan 和 Ritchie 出版“C 程式語言”
- 主要特性：`struct`、`int`、`char`、指標、函式、`#include`
- 沒有`void`、沒有`enum`、沒有`unsigned`、沒有 `const`
### C89/C90 — 標準 (1989)
- 第一個 ANSI 標準 (ANSI X3.159-1989)
- 新增：`void`、`enum`、`const`、`volatile`、函數原型、 `signed`
- 「黃金時代」—便攜、廣泛採用
- 仍然是許多嵌入式系統的基準
### C99 — 現代 C (1999)
-`//`單行註釋
-`inline`功能
-`bool`透過 `<stdbool.h>`
- 可變長度數組（VLA）
- 指定初始化器：`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— 循環中的聲明
-`<stdint.h>`:`int32_t`,`uint64_t`等
-`restrict`關鍵字
- 可變參數宏
- 複合文字
### C11 — 安全與同時 (2011)
-`<stdatomic.h>`— 原子操作
-`<threads.h>`— 線程支持
-`_Static_assert`— 編譯時斷言
- 嵌套結構中的匿名結構/聯合
-`_Alignof`,`_Alignas`— 對齊控制
- 通用選擇：`_Generic(x, int: ..., default: ...)`
- Unicode 支援：`<uchar.h>`
- 可選的 VLA 支援（由於嵌入式問題而成為可選）
### C23 — 文藝復興 (2024)
-`nullptr`— 空指標常數（取代`NULL`巨集）
-`typeof`— 型別推斷
-`constexpr`— 常數表達式
-`#embed`— 在編譯時嵌入二進位數據
-`[[attribute]]`語法（C23 樣式屬性）
-`true`/`false`作為關鍵字（不再需要`<stdbool.h>`）
-`auto`型態推斷
- `static_assert`（無底線）
- `alignof`（無底線）
- 預設`int`回傳已刪除
## 標準流程
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## 相容性理念
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## 預處理器的演變
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## 類型系統的演變
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## 生態系影響
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
