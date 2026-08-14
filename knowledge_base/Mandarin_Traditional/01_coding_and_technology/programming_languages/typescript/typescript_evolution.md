<!--
---
# Metadata
title: "TypeScript — Version History & Evolution"
description: "Comprehensive version history and evolution of TypeScript from 0.8 to modern TypeScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [typescript, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# TypeScript — 版本歷史與演變
## 時間軸
|版本 |發佈日期 |關鍵主題 |
|--------|-------------|------------|
| 0.8 | 0.8 2012 年 10 月 |首次公開發布 (Anders Hejlsberg) |
| 0.9 | 0.9 2013 年 4 月 |泛型 |
| 1.0 | 2014 年 4 月 |第一個穩定版本 |
| 1.1| 2014 年 11 月 |編譯器效能 |
| 1.4 | 1.4 2015 年 1 月 |範本文字類型（基本），`let` |
| 1.5 | 1.5 2015 年 7 月 | `namespace`、`destructuring`、`for...of` |
| 1.6 | 1.6 2015 年 9 月 |`abstract`類，JSX 支援 |
| 1.7 | 1.7 2015 年 11 月 | `async/await`（ES2017 目標）|
| 1.8 | 1.8 2016 年 2 月 |標記模板字串，`--strictNullChecks` |
| 2.0 | 2016 年 9 月 | **主要**：並集/交集類型，`never`、`keyof`、`protected`|
| 2.1 | 2.1 2016 年 12 月 |`keyof`、映射類型、`async` 產生器 |
| 2.2 | 2.2 2017 年 2 月 | `object`型，改良型`this` |
| 2.3 | 2.3 2017 年 4 月 |通用預設值，`--strict` 模式 |
| 2.4 | 2.4 2017 年 6 月 |弱型別、字串枚舉 |
| 2.5 | 2.5 2017 年 9 月 |可選的 catch 綁定 |
| 2.6 | 2.6 2017 年 10 月 |嚴格的函數類型，`--strictFunctionTypes` |
| 2.7 | 2.7 2018 年 1 月 |明確賦值 (`!`)、`const` 枚舉 |
| 2.8 | 2.8 2018 年 3 月 | **條件類型**、`Exclude`、`Extract` |
| 2.9 | 2.9 2018 年 6 月 |`keyof`用於數字/符號，`import()` 類型 |
| 3.0 | 2018 年 7 月 | **主要**：靜態元組，`unknown`，專案參考|
| 3.1| 2018 年 9 月 |元組、`readonly` 陣列上的映射類型 |
| 3.2 | 2018 年 11 月 |`bigint`,`object`傳播 |
| 3.4 | 3.4 2019 年 3 月 |`const`斷言，高階型別推論 |
| 3.5 | 3.5 2019 年 5 月 |`Omit`輔助型 |
| 3.7 | 3.7 2019 年 11 月 | **可選連結**、無效合併、遞迴類型 |
| 3.8 | 2020 年 2 月 |`type-only`導入/匯出，`#private` 欄位 |
| 3.9 | 3.9 2020 年 5 月 | `// @ts-expect-error`，改進推理 |
| 4.0 | 2020 年 8 月 | **主要**：可變參數元組、標記元組、模板文字類型 |
| 4.1 | 2020 年 11 月 | **範本文字類型**、鍵重新映射、遞歸條件 |
| 4.2 | 2021 年 2 月 |抽象屬性，映射類型中的`~`|
| 4.3 | 2021 年 6 月 |單獨的寫入類型，`override`關鍵字|
| 4.4 | 4.4 2021 年 8 月 |符號/索引簽名，控制流程縮小|
| 4.5 | 4.5 2021 年 11 月 |`.d.ts`來自`.js`、`await` 中的`.d.ts`|
| 4.6 | 2022 年 2 月 |區塊作用域函數檢查、物件剩餘精確型別 |
| 4.7 | 4.7 2022 年 5 月 |`extends`對`infer`的約束，`.ts` 中的 ESM |
| 4.8 | 2022 年 8 月 |改進了交叉點減少，`--strictNullChecks` 修復 |
| 4.9 | 4.9 2022 年 11 月 | **`satisfies`運算子**，`in` 縮小|
| 5.0 | 2023 年 3 月 | **主要**：`const` 型別參數、裝飾器、`enum` 大修 |
| 5.1 | 2023 年 6 月 |不相關的型別設定器，`--exactOptionalPropertyTypes` |
| 5.2 | 5.2 2023 年 8 月 |`using`聲明（顯式資源管理）|
| 5.3 | 2023 年 11 月 |導入屬性，`switch true`縮小|
| 5.4 | 5.4 2024 年 3 月 |`NoInfer`實用程序，縮小閉包參數 |
| 5.5 | 5.5 2024 年 6 月 |推斷型別謂詞，正規表示式的`@`|
| 5.6 | 5.6 2024 年 9 月 |`--erasableSyntaxOnly`，迭代器助手 |
| 5.7 | 5.7 2024 年 11 月 | `--noCheck`，路徑完成 |
| 5.8 | 2025 年 2 月 |改進的`isolatedDeclarations` |
## 主要里程碑
### 早期（2012-2015）
- **0.8 (2012)**：Anders Hejlsberg（C# 創建者）在 Microsoft 領導 TypeScript
- **1.0 (2014)**：穩定版本；類別、介面、基本型別
- **1.5 (2015)**：ES6 功能 — 解構、命名空間、`for...of`
### 類型革命（2016–2018）
- **2.0 (2016)**：聯合型別、交集型別、`never`、`keyof`— TypeScript 的型別系統變得獨一無二
- **2.8 (2018)**：條件類型 — 高階類型級程式設計的基礎
- **3.0 (2018)**：剩餘參數中的元組，`unknown` 類型，項目引用
### 現代 TypeScript（2019 年至今）
- **3.7 (2019)**：可選連結`?.`和無效合併 `??`（在 JS 標準之前！）
- **4.0 (2020)**：可變參數元組、範本文字類型
- **4.1 (2020)**：範本文字類型 — 類型級字串操作
- **4.9 (2022)**：`satisfies` 運算子 — 不加寬的型別檢查
- **5.0 (2023)**：`const` 類型參數、裝飾器（第 3 階段）
- **5.2 (2023)**：`using` 聲明 — 明確資源管理
## 類型系統的演變
```
2012: Basic types, classes, interfaces
2014: Generics, enums
2016: Union types, intersection types, discriminated unions
2018: Conditional types, mapped types, keyof, infer
2020: Template literal types, variadic tuples
2022: satisfies operator
2023: const type parameters
2023: using declarations
```

## 裝飾器的演變
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## 配置演變
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## 生態系成長
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## 關鍵設計決策
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
