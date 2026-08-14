<!--
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

-->
# JavaScript — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| ES1 | 1997 | Ấn bản đầu tiên (Netscape) |
| ES2 | 1998 | Những thay đổi nhỏ về biên tập |
| ES3 | 1999 | Regex,`try/catch`,`switch`|
| ES4 | — | Bị bỏ rơi (quá tham vọng) |
| ES5 | 2009 | Chế độ nghiêm ngặt, JSON,`map/filter/reduce`|
| ES5.1 | 2011 | Sửa lỗi biên tập |
| ES6/2015 | 2015 | **Chính**:`let/const`, mũi tên, lớp, lời hứa, mô-đun |
| ES7/2016 | 2016 | `**`,`Array.includes`|
| ES8/2017 | 2017 | `async/await`,`Object.entries`, bộ nhớ dùng chung |
| ES9/2018 | 2018 | Nghỉ ngơi/lan rộng,`for-await-of`,`Promise.finally`|
| ES10/2019 | 2019 | `Array.flat`,`Object.fromEntries`,`BigInt`|
| ES11/2020 | 2020 | `??`,`?.`,`Promise.allSettled`,`import()`năng động |
| ES12/2021 | 2021 | `String.replaceAll`,`Promise.any`, phân công logic |
| ES13/2022 | 2022 |`await`cấp cao nhất, trường lớp, `Array.at()`,`#private`|
| ES14/2023 | 2023 |  `Array.findLast`, hashbang, ký hiệu dưới dạng khóa WeakMap |
| ES15/2024 | 2024 | `Promise.withResolvers`,`Object.groupBy`,`Atomics.waitAsync`|
| ES16/2025 | 2025 | Trình trợ giúp vòng lặp, phương pháp `Set`,`import attributes`|
## Các cột mốc quan trọng
### Kỷ nguyên trình duyệt (1995–2009)
- **1995**: Brendan Eich tạo JavaScript trong 10 ngày tại Netscape
- **1997**: ECMA-262 chuẩn hóa ngôn ngữ
- **1999**: ES3 — phiên bản thống trị suốt một thập kỷ
- **2005**: Cuộc cách mạng AJAX (Google Maps, Gmail) — JS trở nên nghiêm túc
- **2006**: jQuery đơn giản hóa việc phát triển trên nhiều trình duyệt
- **2008**: Động cơ V8 (Chrome) — Cuộc cách mạng về hiệu suất JS bắt đầu
- **2009**: Node.js — JavaScript thoát khỏi trình duyệt
### Thời Hiện Đại (2015–nay)
- **2015**: ES6 — bản cập nhật lớn nhất từ trước đến nay; `let/const`, hàm mũi tên, lớp, Lời hứa, chữ mẫu, phá hủy, mô-đun,`Symbol`,`Map/Set`, trình tạo,`for...of`
- **2017**:`async/await`— lập trình không đồng bộ có thể đọc được
- **2020**:`?.`xâu chuỗi tùy chọn và vô hiệu hóa`??`
- **2022**:`await`cấp cao nhất, các trường lớp riêng
- **2024**:`Promise.withResolvers`, `Object.groupBy`
## ES6 (2015) — Vụ nổ lớn
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

## Tiến hóa không đồng bộ
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

## Tiến hóa mô-đun
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## Loại tiến hóa hệ thống
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## Tiến hóa thời gian chạy
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

## Tăng trưởng hệ sinh thái
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
