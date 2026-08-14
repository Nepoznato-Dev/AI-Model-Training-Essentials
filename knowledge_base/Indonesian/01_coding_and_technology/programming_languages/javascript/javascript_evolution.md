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
# JavaScript — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| ES1 | 1997 | Edisi pertama (Netscape) |
| ES2 | 1998 | Perubahan editorial kecil |
| ES3 | 1999 | Regex, `try/catch`,`switch`|
| ES4 | — | Ditinggalkan (terlalu ambisius) |
| ES5 | 2009 | Mode ketat, JSON,`map/filter/reduce`|
| ES5.1 | 2011 | Perbaikan editorial |
| ES6/2015 | 2015 | **Mayor**:`let/const`, panah, kelas, janji, modul |
| ES7/2016 | 2016 | `**`,`Array.includes`|
| ES8/2017 | 2017 | `async/await`,`Object.entries`, memori bersama |
| ES9/2018 | 2018 | Istirahat/penyebaran,`for-await-of`,`Promise.finally`|
| ES10/2019 | 2019 | `Array.flat`,`Object.fromEntries`,`BigInt`|
| ES11/2020 | 2020 | `??`,`?.`,`Promise.allSettled`,`import()`dinamis |
| ES12/2021 | 2021 | `String.replaceAll`,`Promise.any`, tugas logis |
| ES13/2022 | 2022 |`await`tingkat atas, bidang kelas,`Array.at()`,`#private`|
| ES14/2023 | 2023 | `Array.findLast`, hashbang, simbol sebagai kunci WeakMap |
| ES15/2024 | 2024 | `Promise.withResolvers`,`Object.groupBy`,`Atomics.waitAsync`|
| ES16/2025 | 2025 | Pembantu Iterator, metode `Set`,`import attributes`|
## Tonggak Penting
### Era Peramban (1995–2009)
- **1995**: Brendan Eich membuat JavaScript dalam 10 hari di Netscape
- **1997**: ECMA-262 menstandarkan bahasa
- **1999**: ES3 — versi yang mendominasi selama satu dekade
- **2005**: Revolusi AJAX (Google Maps, Gmail) — JS menjadi serius
- **2006**: jQuery menyederhanakan pengembangan lintas browser
- **2008**: Mesin V8 (Chrome) — Revolusi performa JS dimulai
- **2009**: Node.js — JavaScript lolos dari browser
### Era Modern (2015–sekarang)
- **2015**: ES6 — pembaruan terbesar yang pernah ada; `let/const`, fungsi panah, kelas, Janji, literal templat, penghancuran, modul,`Symbol`,`Map/Set`, generator,`for...of`
- **2017**:`async/await`— pemrograman asinkron menjadi mudah dibaca
- **2020**: Rangkaian opsional`?.`dan penggabungan nullish`??`
- **2022**:`await`tingkat atas, bidang kelas privat
- **2024**:`Promise.withResolvers`, `Object.groupBy`
## ES6 (2015) — Ledakan Besar
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

## Evolusi Asinkron
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

## Evolusi Modul
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## Ketik Evolusi Sistem
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## Evolusi Waktu Proses
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

## Pertumbuhan Ekosistem
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
