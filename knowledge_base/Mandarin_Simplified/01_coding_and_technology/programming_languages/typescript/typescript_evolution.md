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
# TypeScript — 版本历史和演变
## 时间轴
|版本 |发布日期 |关键主题 |
|--------|-------------|------------|
| 0.8 | 0.8 2012 年 10 月 |首次公开发布 (Anders Hejlsberg) |
| 0.9 | 0.9 2013 年 4 月 |泛型 |
| 1.0 | 2014 年 4 月 |第一个稳定版本 |
| 1.1| 2014 年 11 月 |编译器性能 |
| 1.4 | 1.4 2015 年 1 月 |模板文字类型（基本），`let` |
| 1.5 | 1.5 2015 年 7 月 |  `namespace`、`destructuring`、`for...of` |
| 1.6 | 1.6 2015 年 9 月 | `abstract`类，JSX 支持 |
| 1.7 | 1.7 2015 年 11 月 |  `async/await`（ES2017 目标）|
| 1.8 | 1.8 2016 年 2 月 |标记模板字符串，`--strictNullChecks` |
| 2.0 | 2016 年 9 月 | **主要**：并集/交集类型，`never`、`keyof`、`protected`|
| 2.1 | 2.1 2016 年 12 月 | `keyof`、映射类型、`async` 生成器 |
| 2.2 | 2.2 2017 年 2 月 |  `object`型，改进型`this` |
| 2.3 | 2.3 2017 年 4 月 |通用默认值，`--strict` 模式 |
| 2.4 | 2.4 2017 年 6 月 |弱类型、字符串枚举 |
| 2.5 | 2.5 2017 年 9 月 |可选的 catch 绑定 |
| 2.6 | 2.6 2017 年 10 月 |严格的函数类型，`--strictFunctionTypes` |
| 2.7 | 2.7 2018 年 1 月 |明确赋值 (`!`)、`const` 枚举 |
| 2.8 | 2.8 2018 年 3 月 | **条件类型**、`Exclude`、`Extract` |
| 2.9 | 2.9 2018 年 6 月 | `keyof`用于数字/符号，`import()` 类型 |
| 3.0 | 2018 年 7 月 | **主要**：静态元组，`unknown`，项目参考|
| 3.1| 2018 年 9 月 |元组、`readonly` 数组上的映射类型 |
| 3.2 | 2018 年 11 月 | `bigint`,`object`传播 |
| 3.4 | 3.4 2019 年 3 月 | `const`断言，高阶类型推断 |
| 3.5 | 3.5 2019 年 5 月 | `Omit`辅助型 |
| 3.7 | 3.7 2019 年 11 月 | **可选链接**、无效合并、递归类型 |
| 3.8 | 2020 年 2 月 | `type-only`导入/导出，`#private` 字段 |
| 3.9 | 3.9 2020 年 5 月 |  `// @ts-expect-error`，改进推理 |
| 4.0 | 2020 年 8 月 | **主要**：可变参数元组、标记元组、模板文字类型 |
| 4.1 | 2020 年 11 月 | **模板文字类型**、键重新映射、递归条件 |
| 4.2 | 2021 年 2 月 |抽象属性，映射类型中的`~`|
| 4.3 | 2021 年 6 月 |单独的写入类型，`override`关键字|
| 4.4 | 4.4 2021 年 8 月 |符号/索引签名，控制流程缩小|
| 4.5 | 4.5 2021 年 11 月 | `.d.ts`来自`.js`、`await` 中的`.d.ts`|
| 4.6 | 2022 年 2 月 |块作用域函数检查、对象剩余精确类型 |
| 4.7 | 4.7 2022 年 5 月 | `extends`对`infer`的约束，`.ts` 中的 ESM |
| 4.8 | 2022 年 8 月 |改进了交叉点减少，`--strictNullChecks` 修复 |
| 4.9 | 4.9 2022 年 11 月 | **`satisfies`运算符**，`in` 缩小|
| 5.0 | 2023 年 3 月 | **主要**：`const` 类型参数、装饰器、`enum` 大修 |
| 5.1 | 2023 年 6 月 |不相关的类型设置器，`--exactOptionalPropertyTypes` |
| 5.2 | 5.2 2023 年 8 月 | `using`声明（显式资源管理）|
| 5.3 | 2023 年 11 月 |导入属性，`switch true`缩小|
| 5.4 | 5.4 2024 年 3 月 | `NoInfer`实用程序，缩小闭包参数 |
| 5.5 | 5.5 2024 年 6 月 |推断类型谓词，正则表达式的`@`|
| 5.6 | 5.6 2024 年 9 月 | `--erasableSyntaxOnly`，迭代器助手 |
| 5.7 | 5.7 2024 年 11 月 |  `--noCheck`，路径完成 |
| 5.8 | 2025 年 2 月 |改进的`isolatedDeclarations` |
## 主要里程碑
### 早期（2012-2015）
- **0.8 (2012)**：Anders Hejlsberg（C# 创建者）在 Microsoft 领导 TypeScript
- **1.0 (2014)**：稳定版本；类、接口、基本类型
- **1.5 (2015)**：ES6 功能 — 解构、命名空间、`for...of`
### 类型革命（2016–2018）
- **2.0 (2016)**：联合类型、交集类型、`never`、`keyof`— TypeScript 的类型系统变得独一无二
- **2.8 (2018)**：条件类型 — 高级类型级编程的基础
- **3.0 (2018)**：剩余参数中的元组，`unknown` 类型，项目引用
### 现代 TypeScript（2019 年至今）
- **3.7 (2019)**：可选链接`?.`和无效合并 `??`（在 JS 标准之前！）
- **4.0 (2020)**：可变参数元组、模板文字类型
- **4.1 (2020)**：模板文字类型 — 类型级字符串操作
- **4.9 (2022)**：`satisfies` 运算符 — 不加宽的类型检查
- **5.0 (2023)**：`const` 类型参数、装饰器（第 3 阶段）
- **5.2 (2023)**：`using` 声明 — 显式资源管理
## 类型系统的演变
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

## 装饰器的演变
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## 配置演变
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## 生态系统增长
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## 关键设计决策
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
