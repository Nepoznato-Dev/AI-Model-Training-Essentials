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
# JavaScript - ورژن کی تاریخ اور ارتقاء
## ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| ES1 | 1997 | پہلا ایڈیشن (Netscape) |
| ES2 | 1998 | معمولی ادارتی تبدیلیاں |
| ES3 | 1999 | Regex,`try/catch`,`switch`|
| ES4 | - | ترک کر دیا گیا (بہت زیادہ مہتواکانکشی) |
| ES5 | 2009 | سخت موڈ، JSON،`map/filter/reduce`|
| ES5.1 | 2011 | ادارتی اصلاحات |
| ES6/2015 | 2015 | **میجر**:`let/const`, تیر، کلاسز، وعدے، ماڈیولز |
| ES7/2016 | 2016 | `**`,`Array.includes`|
| ES8/2017 | 2017 | `async/await`,`Object.entries`, مشترکہ میموری |
| ES9/2018 | 2018 | آرام/پھیلاؤ،`for-await-of`,`Promise.finally`|
| ES10/2019 | 2019 | `Array.flat`,`Object.fromEntries`,`BigInt`|
| ES11/2020 | 2020 | `??`,`?.`,`Promise.allSettled`, متحرک`import()`|
| ES12/2021 | 2021 | `String.replaceAll`,`Promise.any`, منطقی تفویض |
| ES13/2022 | 2022 | ٹاپ لیول`await`, کلاس فیلڈز ,`Array.at()`,`#private`|
| ES14/2023 | 2023 | `Array.findLast`, hashbang , علامتیں بطور WeakMap کیز |
| ES15/2024 | 2024 | `Promise.withResolvers`,`Object.groupBy`,`Atomics.waitAsync`|
| ES16/2025 | 2025 | تکرار کرنے والے مددگار،`Set`طریقے،`import attributes`|
## اہم سنگ میل
### براؤزر کا دور (1995–2009)
- **1995**: برینڈن ایچ نے نیٹ اسکیپ پر 10 دنوں میں جاوا اسکرپٹ بنایا
- **1997**: ECMA-262 زبان کو معیاری بناتا ہے۔
- **1999**: ES3 — وہ ورژن جس پر ایک دہائی تک غلبہ رہا۔
- **2005**: AJAX انقلاب (Google Maps, Gmail) — JS سنجیدہ ہو جاتا ہے۔
- **2006**: jQuery کراس براؤزر کی ترقی کو آسان بناتا ہے۔
- **2008**: V8 انجن (Chrome) — JS کارکردگی کا انقلاب شروع ہوتا ہے۔
- **2009**: Node.js — JavaScript براؤزر سے بچ جاتا ہے۔
### جدید دور (2015–موجودہ)
- **2015**: ES6 - اب تک کی سب سے بڑی تازہ کاری؛ `let/const`, تیر کے فنکشنز، کلاسز، وعدے، ٹیمپلیٹ لٹریلز، ڈیسٹرکچرنگ، ماڈیولز،`Symbol`,`Map/Set`, جنریٹرز،`for...of`
- **2017**:`async/await`— غیر مطابقت پذیر پروگرامنگ پڑھنے کے قابل ہو جاتی ہے
- **2020**: اختیاری سلسلہ بندی`?.`اور nullish coalescing`??`
- **2022**: ٹاپ لیول `await`، پرائیویٹ کلاس فیلڈز
- **2024**: `Promise.withResolvers`، `Object.groupBy`
## ES6 (2015) — دی بگ بینگ
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

## Async ارتقاء
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

## ماڈیول ارتقاء
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## ٹائپ سسٹم ارتقاء
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## رن ٹائم ارتقاء
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

## ماحولیاتی نظام کی نمو
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
