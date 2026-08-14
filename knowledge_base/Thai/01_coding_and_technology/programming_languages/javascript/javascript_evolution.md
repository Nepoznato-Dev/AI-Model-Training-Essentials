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
# JavaScript - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| อีเอส1 | 1997 | ฉบับพิมพ์ครั้งแรก (Netscape) |
| อีเอส2 | 1998 | การเปลี่ยนแปลงทางบรรณาธิการเล็กน้อย |
| อีเอส3 | 1999 | Regex,`try/catch`,`switch`|
| ES4 | — | ถูกทอดทิ้ง (ทะเยอทะยานเกินไป) |
| ES5 | 2552 | โหมดเข้มงวด, JSON,`map/filter/reduce`|
| ES5.1 | 2554 | การแก้ไขด้านบรรณาธิการ |
| มส6/2558 | 2558 | **วิชาเอก**:`let/const`, ลูกศร, คลาส, คำสัญญา, โมดูล |
| ส7/2559 | 2559 | `**`,`Array.includes`|
| ส.8/2560 | 2017 | `async/await`,`Object.entries`, หน่วยความจำที่แชร์ |
| มส.9/2561 | 2018 | พัก/สเปรด`for-await-of`,`Promise.finally`|
| มส.10/2562 | 2019 | `Array.flat`,`Object.fromEntries`,`BigInt`|
| ส.11/2563 | 2020 | `??`,`?.`,`Promise.allSettled`, ไดนามิก`import()`|
| มส12/2564 | 2021 | `String.replaceAll`,`Promise.any`, การกำหนดโลจิคัล |
| มส13/2565 | 2022 |`await`ระดับบนสุด , ฟิลด์คลาส,`Array.at()`,`#private`|
| มส14/2566 | 2023 | `Array.findLast`, hashbang สัญลักษณ์เป็นปุ่ม WeakMap |
| มส15/2567 | 2024 | `Promise.withResolvers`,`Object.groupBy`,`Atomics.waitAsync`|
| มส16/2568 | 2025 | ตัวช่วยตัววนซ้ำ, วิธี `Set`,`import attributes`|
## เหตุการณ์สำคัญที่สำคัญ
### ยุคเบราว์เซอร์ (1995–2009)
- **1995**: Brendan Eich สร้าง JavaScript ใน 10 วันที่ Netscape
- **1997**: ECMA-262 สร้างมาตรฐานของภาษา
- **1999**: ES3 — เวอร์ชันที่ครองใจมานานนับทศวรรษ
- **2005**: การปฏิวัติ AJAX (Google Maps, Gmail) — JS เริ่มจริงจัง
- **2006**: jQuery ทำให้การพัฒนาข้ามเบราว์เซอร์ง่ายขึ้น
- **2008**: เครื่องยนต์ V8 (Chrome) — การปฏิวัติประสิทธิภาพของ JS เริ่มต้นขึ้น
- **2009**: Node.js — JavaScript หนีจากเบราว์เซอร์
### ยุคสมัยใหม่ (พ.ศ. 2558–ปัจจุบัน)
- **2015**: ES6 — การอัปเดตครั้งใหญ่ที่สุดเท่าที่เคยมีมา `let/const`, ฟังก์ชันลูกศร, คลาส, Promises, ตัวอักษรเทมเพลต, การทำลายโครงสร้าง, โมดูล,`Symbol`,`Map/Set`, เครื่องกำเนิดไฟฟ้า,`for...of`
- **2017**:`async/await`— การเขียนโปรแกรมแบบอะซิงโครนัสสามารถอ่านได้
- **2020**: การต่อสายโซ่เสริม`?.`และการรวมกันเป็นโมฆะ`??`
- **2022**:`await`ระดับบนสุด ฟิลด์คลาสส่วนตัว
- **2024**:`Promise.withResolvers`, `Object.groupBy`
## ES6 (2015) — บิ๊กแบง
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

## วิวัฒนาการแบบอะซิงก์
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

## วิวัฒนาการของโมดูล
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## ประเภทวิวัฒนาการของระบบ
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## วิวัฒนาการรันไทม์
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

## การเติบโตของระบบนิเวศ
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
