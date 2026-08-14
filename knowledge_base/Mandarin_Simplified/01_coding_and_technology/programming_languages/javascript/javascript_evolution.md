---
# Metadata
title: "JavaScript — Version History & Evolution"
description: "Comprehensive version history and evolution of JavaScript from ES1 to modern ECMAScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [javascript, es6, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# JavaScript — 版本历史和演变
## 时间轴
|版本 |年份|关键主题 |
|--------|------|------------|
| ES1 | 1997 |第一版（网景）|
| ES2 | 1998 |细微的编辑修改 |
| ES3 | 1999 |正则表达式，`try/catch`，`switch` |
| ES4 | — |被放弃（野心太大）|
| ES5 | 2009 |严格模式、JSON、`map/filter/reduce` |
| ES5.1 | 2011 |编辑修复|
| ES6/2015 | 2015 | 2015 **主要**：`let/const`、箭头、类、承诺、模块 |
| ES7/2016 | 2016 | 2016  `**`、`Array.includes` |
| ES8/2017 | 2017 | 2017  `async/await`、`Object.entries`、共享内存 |
| ES9/2018 | 2018 |休息/展开，`for-await-of`，`Promise.finally` |
| ES10/2019 | 2019 | 2019  `Array.flat`、`Object.fromEntries`、`BigInt` |
| ES11/2020 | 2020 |  `??`、`?.`、`Promise.allSettled`、动态`import()` |
| ES12/2021 | 2021 | `String.replaceAll`、`Promise.any`、逻辑赋值 |
| ES13/2022 | 2022 | 2022顶级`await`、类字段、`Array.at()`、`#private`|
| ES14/2023 | 2023 | `Array.findLast`、 hashbang、符号作为 WeakMap 键 |
| ES15/2024 | 2024 | 2024  `Promise.withResolvers`、`Object.groupBy`、`Atomics.waitAsync` |
| ES16/2025 | 2025 | 2025迭代器助手、`Set` 方法、`import attributes` |
## 主要里程碑
### 浏览器时代（1995–2009）
- **1995**：Brendan Eich 在 Netscape 10 天内创建了 JavaScript
- **1997**：ECMA-262 标准化了语言
- **1999**：ES3 — 统治十年的版本
- **2005**：AJAX 革命（Google 地图、Gmail）——JS 变得严肃起来
- **2006**：jQuery 简化了跨浏览器开发
- **2008**：V8 引擎 (Chrome) — JS 性能革命开始
- **2009**：Node.js — JavaScript 逃离浏览器
### 现代时代（2015 年至今）
- **2015**：ES6 — 有史以来最大的更新； `let/const`、箭头函数、类、Promise、模板文字、解构、模块、`Symbol` 、`Map/Set`、生成器、`for...of` 
- **2017**：`async/await` — 异步编程变得可读
- **2020**：可选链接`?.`和无效合并`??`
- **2022**：顶级`await`，私有类字段
- **2024**：`Promise.withResolvers`，`Object.groupBy`
## ES6 (2015) — 大爆炸
```javascript
// Before ES6
var name = "Alice";
function greet(name) { return "Hello, " + name; }
$.ajax({ url: "/api", success: function(data) { ... } });

// After ES6
const name = "Alice";
const greet = name => `Hello, ${name}`;
const data = await fetch("/api").then(r => r.json());

// New features at a glance
let/const          // block scoping
() => {}           // arrow functions
class {}           // class syntax
`template`         // template literals
{a, b} = obj       // destructuring
...args            // rest/spread
import/export      // modules
Promise            // async without callbacks
Symbol             // unique identifiers
Map/Set            // proper collections
for (x of iter)    // iteration protocol
function*() {}     // generators
```

## 异步进化
```
1995: Callbacks (nested → "callback hell")
2009: jQuery Deferred / Promises/A
2012: jQuery Deferred → Promises/A+ standard
2015: ES6 Promises (native)
2015: Generator-based async (co library)
2017: async/await (ES8) — "synchronous-looking" async
2019: for-await-of (async iteration)
2020: Promise.allSettled
2021: Promise.any
2024: Promise.withResolvers
```

## 模块演化
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## 类型系统的演变
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## 运行时演变
```
2008: V8 (Chrome) — JIT compilation
2009: Node.js — server-side JS
2011: Deno announced (later released 2018)
2015: Node.js io.js merge
2016: Node.js 6+ with ES6 support
2018: Deno 1.0 (secure by default, TypeScript native)
2020: Deno 1.x stable
2022: Bun — ultra-fast JS runtime (Zig + JavaScriptCore)
2023: Node.js 20 — stable test runner, permission model
2025: Bun 1.x — production-ready alternative
```

## 生态系统增长
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
