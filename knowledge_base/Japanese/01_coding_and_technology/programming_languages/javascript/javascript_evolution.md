---
# Metadata
title: "JavaScript — Version History & Evolution"
description: "Comprehensive version history and evolution of JavaScript from ES1 to modern ECMAScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# JavaScript — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
| ES1 | 1997年 |初版 (Netscape) |
| ES2 | 1998年 |マイナーな編集上の変更 |
| ES3 | 1999年 |正規表現、`try/catch`、`switch`|
| ES4 | — |放棄された (野心的すぎる) |
| ES5 | 2009年 |厳密モード、JSON、`map/filter/reduce` |
| ES5.1 | 2011年 |編集上の修正 |
| ES6/2015 | 2015年 | **主要**:`let/const`、矢印、クラス、プロミス、モジュール |
| ES7/2016 | 2016年 |  `**`、`Array.includes` |
| ES8/2017 | 2017年 | `async/await`、`Object.entries`、共有メモリ |
| ES9/2018 | 2018年 |レスト/スプレッド、`for-await-of`、`Promise.finally`|
| ES10/2019 | 2019年 |  `Array.flat`、`Object.fromEntries`、`BigInt` |
| ES11/2020 | 2020年 | `??`、`?.`、`Promise.allSettled`、 動的`import()`|
| ES12/2021 | 2021年 | `String.replaceAll`、`Promise.any`、論理割り当て |
| ES13/2022 | 2022年 |トップレベル`await`、クラス フィールド、`Array.at()`、`#private`|
| ES14/2023 | 2023年 | `Array.findLast`、ハッシュバン、WeakMap キーとしてのシンボル |
| ES15/2024 | 2024年 |  `Promise.withResolvers`、`Object.groupBy`、`Atomics.waitAsync` |
| ES16/2025 | 2025年 |イテレータ ヘルパー、`Set` メソッド、`import attributes` |
## 主要なマイルストーン
### ブラウザ時代 (1995 ～ 2009 年)
- **1995**: ブレンダン・アイヒが Netscape で 10 日間で JavaScript を作成
- **1997**: ECMA-262 により言語が標準化される
- **1999**: ES3 — 10 年間主流だったバージョン
- **2005**: AJAX 革命 (Google マップ、Gmail) — JS が本格化
- **2006**: jQuery によりクロスブラウザ開発が簡素化
- **2008**: V8 エンジン (クローム) — JS パフォーマンス革命が始まる
- **2009**: Node.js — JavaScript がブラウザーをエスケープ
### 現代 (2015–現在)
- **2015**: ES6 — 史上最大のアップデート。 `let/const`、アロー関数、クラス、Promise、テンプレート リテラル、構造化、モジュール、`Symbol` 、`Map/Set`、ジェネレーター、`for...of` 
- **2017**:`async/await`— 非同期プログラミングが読みやすくなる
- **2020**: オプションのチェーン`?.`とヌル合体`??`
- **2022**: トップレベル`await`、プライベート クラス フィールド
- **2024**:`Promise.withResolvers`、 `Object.groupBy`
## ES6 (2015) — ビッグバン
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

## 非同期進化
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

## モジュールの進化
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## 型システムの進化
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## ランタイムの進化
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

## エコシステムの成長
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
