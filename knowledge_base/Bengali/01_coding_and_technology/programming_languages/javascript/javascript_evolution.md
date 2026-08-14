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
# জাভাস্ক্রিপ্ট — সংস্করণ ইতিহাস এবং বিবর্তন
## টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| ES1 | 1997 | প্রথম সংস্করণ (নেটস্কেপ) |
| ES2 | 1998 | ছোটখাটো সম্পাদকীয় পরিবর্তন |
| ES3 | 1999 | Regex,`try/catch`,`switch`|
| ES4 | — | পরিত্যক্ত (খুব উচ্চাভিলাষী) |
| ES5 | 2009 | কঠোর মোড, JSON,`map/filter/reduce`|
| ES5.1 | 2011 | সম্পাদকীয় সংশোধন |
| ES6/2015 | 2015 | **মেজর**:`let/const`, তীর, ক্লাস, প্রতিশ্রুতি, মডিউল |
| ES7/2016 | 2016 | `**`,`Array.includes`|
| ES8/2017 | 2017 | `async/await`,`Object.entries`, শেয়ার করা মেমরি |
| ES9/2018 | 2018 | বিশ্রাম/স্প্রেড,`for-await-of`,`Promise.finally`|
| ES10/2019 | 2019 | `Array.flat`,`Object.fromEntries`,`BigInt`|
| ES11/2020 | 2020 | `??`,`?.`,`Promise.allSettled`, গতিশীল`import()`|
| ES12/2021 | 2021 | `String.replaceAll`,`Promise.any`, লজিক্যাল অ্যাসাইনমেন্ট |
| ES13/2022 | 2022 | শীর্ষ-স্তরের`await`, ক্লাস ক্ষেত্র,`Array.at()`,`#private`|
| ES14/2023 | 2023 | `Array.findLast`, হ্যাশব্যাং, উইকম্যাপ কী হিসাবে চিহ্ন |
| ES15/2024 | 2024 | `Promise.withResolvers`,`Object.groupBy`,`Atomics.waitAsync`|
| ES16/2025 | 2025 | ইটারেটর সাহায্যকারী,`Set`পদ্ধতি,`import attributes`|
## প্রধান মাইলফলক
### ব্রাউজার যুগ (1995-2009)
- **1995**: ব্রেন্ডন ইচ নেটস্কেপে 10 দিনের মধ্যে জাভাস্ক্রিপ্ট তৈরি করেন
- **1997**: ECMA-262 ভাষাকে প্রমিত করে
- **1999**: ES3 — একটি সংস্করণ যা এক দশক ধরে আধিপত্য বিস্তার করে
- **2005**: AJAX বিপ্লব (Google Maps, Gmail) — JS গুরুতর হয়ে ওঠে
- **2006**: jQuery ক্রস-ব্রাউজার বিকাশকে সহজ করে
- **2008**: V8 ইঞ্জিন (Chrome) — JS কর্মক্ষমতা বিপ্লব শুরু হয়
- **2009**: Node.js — জাভাস্ক্রিপ্ট ব্রাউজার থেকে পালিয়ে যায়
### আধুনিক যুগ (2015-বর্তমান)
- **2015**: ES6 — এখন পর্যন্ত সবচেয়ে বড় আপডেট; `let/const`, তীর ফাংশন, ক্লাস, প্রতিশ্রুতি, টেমপ্লেট লিটারাল, ডেস্ট্রাকচারিং, মডিউল,`Symbol`,`Map/Set`, জেনারেটর,`for...of`
- **2017**:`async/await`— অ্যাসিঙ্ক্রোনাস প্রোগ্রামিং পাঠযোগ্য হয়ে ওঠে
- **2020**: ঐচ্ছিক চেইনিং`?.`এবং শূন্য কোলেসিং`??`
- **2022**: শীর্ষ-স্তরের`await`, ব্যক্তিগত শ্রেণীর ক্ষেত্র
- **2024**:`Promise.withResolvers`, `Object.groupBy`
## ES6 (2015) — দ্য বিগ ব্যাং
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

## অ্যাসিঙ্ক বিবর্তন
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

## মডিউল বিবর্তন
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## টাইপ সিস্টেম বিবর্তন
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## রানটাইম বিবর্তন
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

## ইকোসিস্টেম বৃদ্ধি
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
