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
# JavaScript – Histórico e evolução da versão
## Linha do tempo
| Versão | Ano | Tema principal |
|--------|------|-----------|
| ES1 | 1997 | Primeira edição (Netscape) |
| ES2 | 1998 | Pequenas alterações editoriais |
| ES3 | 1999 | Regex, `try/catch`,`switch`|
| ES4 | — | Abandonado (muito ambicioso) |
| ES5 | 2009 | Modo estrito, JSON,`map/filter/reduce`|
| ES5.1 | 2011 | Correções editoriais |
| ES6/2015 | 2015 | **Principal**:`let/const`, setas, classes, promessas, módulos |
| ES7/2016 | 2016 | `**`,`Array.includes`|
| ES8/2017 | 2017 | `async/await`,`Object.entries`, memória compartilhada |
| ES9/2018 | 2018 | Descanso/propagação,`for-await-of`,`Promise.finally`|
| ES10/2019 | 2019 | `Array.flat`,`Object.fromEntries`,`BigInt`|
| ES11/2020 | 2020 | `??`,`?.`,`Promise.allSettled`,`import()`dinâmico |
| ES12/2021 | 2021 | `String.replaceAll`,`Promise.any`, atribuição lógica |
| ES13/2022 | 2022 |`await`de nível superior, campos de classe, `Array.at()`,`#private`|
| ES14/2023 | 2023 |  `Array.findLast`, hashbang, símbolos como chaves WeakMap |
| ES15/2024 | 2024 | `Promise.withResolvers`,`Object.groupBy`,`Atomics.waitAsync`|
| ES16/2025 | 2025 | Auxiliares de iterador, métodos `Set`,`import attributes`|
## Marcos importantes
### A era do navegador (1995–2009)
- **1995**: Brendan Eich cria JavaScript em 10 dias na Netscape
- **1997**: ECMA-262 padroniza a linguagem
- **1999**: ES3 — a versão que dominou por uma década
- **2005**: Revolução AJAX (Google Maps, Gmail) — JS torna-se sério
- **2006**: jQuery simplifica o desenvolvimento entre navegadores
- **2008**: motor V8 (Chrome) — começa a revolução do desempenho JS
- **2009**: Node.js — JavaScript escapa do navegador
### A Era Moderna (2015-presente)
- **2015**: ES6 — a maior atualização de todos os tempos; `let/const`, funções de seta, classes, promessas, literais de modelo, desestruturação, módulos,`Symbol`,`Map/Set`, geradores,`for...of`
- **2017**:`async/await`— a programação assíncrona torna-se legível
- **2020**: encadeamento opcional`?.`e coalescência nula`??`
- **2022**:`await`de nível superior, campos de classe privada
- **2024**: `Promise.withResolvers`, `Object.groupBy`
## ES6 (2015) — O Big Bang
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

## Evolução Assíncrona
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

## Evolução do Módulo
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## Tipo Evolução do Sistema
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## Evolução do tempo de execução
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

## Crescimento do Ecossistema
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
