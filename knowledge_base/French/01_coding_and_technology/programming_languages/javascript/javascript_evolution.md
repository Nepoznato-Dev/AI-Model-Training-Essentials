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
# JavaScript — Historique et évolution des versions
## Chronologie
| Version | Année | Thème clé |
|---------|------|-----------|
| ES1 | 1997 | Première édition (Netscape) |
| ES2 | 1998 | Modifications éditoriales mineures |
| ES3 | 1999 | Expression régulière,`try/catch`,`switch`|
| ES4 | — | Abandonné (trop ambitieux) |
| ES5 | 2009 | Mode strict, JSON,`map/filter/reduce`|
| ES5.1 | 2011 | Corrections éditoriales |
| ES6/2015 | 2015 | **Majeur** :`let/const`, flèches, classes, promesses, modules |
| ES7/2016 | 2016 | `**`,`Array.includes`|
| ES8/2017 | 2017 | `async/await`,`Object.entries`, mémoire partagée |
| ES9/2018 | 2018 | Repos/écartement,`for-await-of`,`Promise.finally`|
| ES10/2019 | 2019 | `Array.flat`,`Object.fromEntries`,`BigInt`|
| ES11/2020 | 2020 | `??`,`?.`,`Promise.allSettled`, dynamique`import()`|
| ES12/2021 | 2021 | `String.replaceAll`,`Promise.any`, affectation logique |
| ES13/2022 | 2022 |`await`de niveau supérieur, champs de classe,`Array.at()`,`#private`|
| ES14/2023 | 2023 |  `Array.findLast`, hashbang, symboles comme clés WeakMap |
| ES15/2024 | 2024 | `Promise.withResolvers`,`Object.groupBy`,`Atomics.waitAsync`|
| ES16/2025 | 2025 | Assistants d'itérateur, méthodes `Set`,`import attributes`|
## Étapes majeures
### L'ère des navigateurs (1995-2009)
- **1995** : Brendan Eich crée JavaScript en 10 jours chez Netscape
- **1997** : ECMA-262 standardise le langage
- **1999** : ES3 — la version qui a dominé pendant une décennie
- **2005** : Révolution AJAX (Google Maps, Gmail) — JS devient sérieux
- **2006** : jQuery simplifie le développement multi-navigateurs
- **2008** : Moteur V8 (Chrome) — La révolution des performances JS commence
- **2009** : Node.js — JavaScript échappe au navigateur
### L'ère moderne (2015-présent)
- **2015** : ES6 — la plus grande mise à jour jamais réalisée ; `let/const`, fonctions fléchées, classes, promesses, littéraux de modèles, déstructuration, modules,`Symbol`,`Map/Set`, générateurs,`for...of`
- **2017** :`async/await`— la programmation asynchrone devient lisible
- **2020** : chaînage optionnel`?.`et fusion nulle`??`
- **2022** :`await`de niveau supérieur, champs de classe privée
- **2024** : `Promise.withResolvers`, `Object.groupBy`
## ES6 (2015) — Le Big Bang
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

## Évolution asynchrone
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

## Évolution des modules
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## Évolution du système de types
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## Évolution du temps d'exécution
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

## Croissance de l'écosystème
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
