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
# JavaScript — historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| ES1 | 1997 | Wydanie pierwsze (Netscape) |
| ES2 | 1998 | Drobne zmiany redakcyjne |
| ES3 | 1999 | Regex, `try/catch`,`switch`|
| ES4 | — | Opuszczony (zbyt ambitny) |
| ES5 | 2009 | Tryb ścisły, JSON,`map/filter/reduce`|
| ES5.1 | 2011 | Poprawki redakcyjne |
| ES6/2015 | 2015 | **Główny**:`let/const`, strzałki, klasy, obietnice, moduły |
| ES7/2016 | 2016 | `**`,`Array.includes`|
| ES8/2017 | 2017 | `async/await`,`Object.entries`, pamięć współdzielona |
| ES9/2018 | 2018 | Reszta/rozpórka,`for-await-of`,`Promise.finally`|
| ES10/2019 | 2019 | `Array.flat`,`Object.fromEntries`,`BigInt`|
| ES11/2020 | 2020 | `??`,`?.`,`Promise.allSettled`, dynamiczny`import()`|
| ES12/2021 | 2021 | `String.replaceAll`,`Promise.any`, przypisanie logiczne |
| ES13/2022 | 2022 | Najwyższy poziom`await`, pola klas,`Array.at()`,`#private`|
| ES14/2023 | 2023 | `Array.findLast`, hashbang, symbole jako klucze WeakMap |
| ES15/2024 | 2024 | `Promise.withResolvers`,`Object.groupBy`,`Atomics.waitAsync`|
| ES16/2025 | 2025 | Pomocnicy iteratora, metody `Set`,`import attributes`|
## Główne kamienie milowe
### Era przeglądarek (1995–2009)
- **1995**: Brendan Eich tworzy JavaScript w 10 dni w Netscape
- **1997**: ECMA-262 standaryzuje język
- **1999**: ES3 — wersja, która dominowała przez dekadę
- **2005**: Rewolucja AJAX (Google Maps, Gmail) — JS staje się poważny
- **2006**: jQuery upraszcza rozwój w różnych przeglądarkach
- **2008**: Silnik V8 (Chrome) — rozpoczyna się rewolucja w zakresie wydajności JS
- **2009**: Node.js — JavaScript ucieka z przeglądarki
### Era nowożytna (2015 – obecnie)
- **2015**: ES6 — największa aktualizacja w historii; `let/const`, funkcje strzałkowe, klasy, Promises, literały szablonów, destrukturyzacja, moduły,`Symbol`,`Map/Set`, generatory,`for...of`
- **2017**:`async/await`— programowanie asynchroniczne staje się czytelne
- **2020**: Opcjonalne łączenie`?.`i koalescencja zerowa`??`
- **2022**: Najwyższy poziom `await`, pola klasy prywatnej
- **2024**: `Promise.withResolvers`, `Object.groupBy`
## ES6 (2015) — Wielki Wybuch
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

## Asynchroniczna ewolucja
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

## Ewolucja modułu
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## Wpisz ewolucję systemu
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## Ewolucja środowiska wykonawczego
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

## Rozwój ekosystemu
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
