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
# JavaScript — 版本歷史與演變
## 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| ES1 | 1997 |初版（網景）|
| ES2 | 1998 |細微的編輯修改 |
| ES3 | 1999 |正規表示式，`try/catch`，`switch` |
| ES4 | — |被放棄（野心太大）|
| ES5 | 2009 |嚴格模式、JSON、`map/filter/reduce` |
| ES5.1 | 2011 |編輯修復|
| ES6/2015 | 2015 | 2015 **主要**：`let/const`、箭頭、類別、承諾、模組 |
| ES7/2016 | 2016 | 2016 `**`、`Array.includes` |
| ES8/2017 | 2017 | 2017 `async/await`、`Object.entries`、共享記憶體 |
| ES9/2018 | 2018 |休息/展開，`for-await-of`，`Promise.finally` |
| ES10/2019 | 2019 | 2019 `Array.flat`、`Object.fromEntries`、`BigInt` |
| ES11/2020 | 2020 | `??`、`?.`、`Promise.allSettled`、動態`import()` |
| ES12/2021 | 2021 |`String.replaceAll`、`Promise.any`、邏輯賦值 |
| ES13/2022 | 2022 | 2022頂級`await`、類別字段、`Array.at()`、`#private`|
| ES14/2023 | 2023 |`Array.findLast`、 hashbang、符號作為 WeakMap 鍵 |
| ES15/2024 | 2024 | 2024 `Promise.withResolvers`、`Object.groupBy`、`Atomics.waitAsync` |
| ES16/2025 | 2025 | 2025迭代器助手、`Set` 方法、`import attributes` |
## 主要里程碑
### 瀏覽器時代（1995–2009）
- **1995**：Brendan Eich 在 Netscape 10 天內創建了 JavaScript
- **1997**：ECMA-262 標準化了語言
- **1999**：ES3 — 統治十年的版本
- **2005**：AJAX 革命（Google 地圖、Gmail）—JS 變得嚴肅起來
- **2006**：jQuery 簡化了跨瀏覽器開發
- **2008**：V8 引擎 (Chrome) — JS 性能革命開始
- **2009**：Node.js — JavaScript 逃離瀏覽器
### 現代時代（2015 年至今）
- **2015**：ES6 — 有史以來最大的更新；`let/const`、箭頭函數、類別、Promise、模板文字、解構、模組、`Symbol` 、`Map/Set`、生成器、`for...of`
- **2017**：`async/await` — 非同步程式設計變得可讀
- **2020**：可選連結`?.`和無效合併 `??`
- **2022**：頂級`await`，私有類別字段
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

## 非同步進化
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

## 模組演化
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## 類型系統的演變
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## 運行時演變
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

## 生態系成長
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
