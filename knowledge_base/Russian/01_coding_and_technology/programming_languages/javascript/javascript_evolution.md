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

# JavaScript — история версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| ES1 | 1997 | Первое издание (Netscape) |
| ES2 | 1998 | Незначительные редакционные изменения |
| ES3 | 1999 | Регулярное выражение, `try/catch`,`switch`|
| ES4 | — | Заброшенный (слишком амбициозный) |
| ES5 | 2009 | Строгий режим, JSON,`map/filter/reduce`|
| ES5.1 | 2011 | Редакционные исправления |
| ES6/2015 | 2015 | **Основное**:`let/const`, стрелки, классы, обещания, модули |
| ES7/2016 | 2016 | `**`,`Array.includes`|
| ES8/2017 | 2017 |  `async/await`, `Object.entries`, общая память |
| ES9/2018 | 2018 | Отдых/распространение,`for-await-of`,`Promise.finally`|
| ES10/2019 | 2019 | `Array.flat`,`Object.fromEntries`,`BigInt`|
| ES11/2020 | 2020 | `??`,`?.`,`Promise.allSettled`, динамический`import()`|
| ЕС12/2021 | 2021 |  `String.replaceAll`, `Promise.any`, логическое присвоение |
| ЕС13/2022 | 2022 |`await`верхнего уровня, поля класса, `Array.at()`,`#private`|
| ЕС14/2023 | 2023 | `Array.findLast`, хэшбанг, символы как ключи WeakMap |
| ЕС15/2024 | 2024 | `Promise.withResolvers`,`Object.groupBy`,`Atomics.waitAsync`|
| ЕС16/2025 | 2025 | Помощники итераторов, методы `Set`,`import attributes`|
## Основные вехи
### Эра браузера (1995–2009)
- **1995**: Брендан Эйх создает JavaScript за 10 дней в Netscape.
- **1997**: ECMA-262 стандартизирует язык.
- **1999**: ES3 — версия, доминировавшая десятилетие.
- **2005**: революция AJAX (Google Maps, Gmail) — JS становится серьёзным
- **2006**: jQuery упрощает кроссбраузерную разработку.
- **2008**: двигатель V8 (хром) — начинается революция в производительности JS.
- **2009**: Node.js — JavaScript выходит за пределы браузера.
### Современная эпоха (2015 – настоящее время)
- **2015**: ES6 — самое большое обновление за всю историю;  `let/const`, стрелочные функции, классы, Promises, шаблонные литералы, деструктуризация, модули, `Symbol`, `Map/Set`, генераторы,`for...of`
- **2017**:`async/await`— асинхронное программирование становится читаемым.
- **2020**: опциональное объединение`?.`и нулевое объединение `??`. 
- **2022**:`await`верхнего уровня, поля частного класса.
- **2024**: `Promise.withResolvers`, `Object.groupBy`
##ES6 (2015) — Большой взрыв
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

## Асинхронная эволюция
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

## Эволюция модуля
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## Эволюция системы типов
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## Эволюция среды выполнения
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

## Рост экосистемы
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
