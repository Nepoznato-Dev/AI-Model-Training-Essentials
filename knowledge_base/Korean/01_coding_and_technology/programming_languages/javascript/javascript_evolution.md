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
# JavaScript — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| ES1 | 1997 | 초판(넷스케이프) |
| ES2 | 1998 | 사소한 편집 변경 |
| ES3 | 1999 | 정규식,`try/catch`,`switch`|
| ES4 | — | 포기함(너무 야심적임) |
| ES5 | 2009 | 엄격 모드, JSON,`map/filter/reduce`|
| ES5.1 | 2011 | 편집 수정 |
| ES6/2015 | 2015 | **주요**:`let/const`, 화살표, 클래스, 약속, 모듈 |
| ES7/2016 | 2016 | `**`,`Array.includes`|
| ES8/2017 | 2017 | `async/await`,`Object.entries`, 공유 메모리 |
| ES9/2018 | 2018 | 나머지/확산,`for-await-of`,`Promise.finally`|
| ES10/2019 | 2019 | `Array.flat`,`Object.fromEntries`,`BigInt`|
| ES11/2020 | 2020 | `??`,`?.`,`Promise.allSettled`, 동적`import()`|
| ES12/2021 | 2021 | `String.replaceAll`,`Promise.any`, 논리 할당 |
| ES13/2022 | 2022 | 최상위`await`, 클래스 필드,`Array.at()`,`#private`|
| ES14/2023 | 2023년 | `Array.findLast`, hashbang, WeakMap 키로서의 기호 |
| ES15/2024 | 2024 | `Promise.withResolvers`,`Object.groupBy`,`Atomics.waitAsync`|
| ES16/2025 | 2025 | 반복기 도우미,`Set`메서드,`import attributes`|
## 주요 이정표
### 브라우저 시대(1995~2009)
- **1995**: Brendan Eich가 Netscape에서 10일 만에 JavaScript를 만듭니다.
- **1997**: ECMA-262는 언어를 표준화합니다.
- **1999**: ES3 — 10년 동안 지배적인 버전
- **2005**: AJAX 혁명(Google Maps, Gmail) — JS가 심각해짐
- **2006**: jQuery는 크로스 브라우저 개발을 단순화합니다.
- **2008**: V8 엔진(Chrome) — JS 성능 혁명이 시작됩니다.
- **2009**: Node.js — JavaScript가 브라우저를 이스케이프합니다.
### 현대 시대(2015~현재)
- **2015**: ES6 — 사상 최대 규모의 업데이트; `let/const`, 화살표 함수, 클래스, 약속, 템플릿 리터럴, 구조 분해, 모듈,`Symbol`,`Map/Set`, 생성기,`for...of`
- **2017**:`async/await`— 비동기 프로그래밍을 읽을 수 있게 되었습니다.
- **2020**: 선택적 연결`?.`및 nullish 병합`??`
- **2022**: 최상위`await`, 비공개 클래스 필드
- **2024**:`Promise.withResolvers`, `Object.groupBy`
## ES6(2015) — 빅뱅
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

## 비동기 진화
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

## 모듈 진화
```
2009: CommonJS (Node.js) — require/module.exports
2010: AMD (RequireJS) — define/require (browser)
2011: UMD — universal wrapper
2015: ES Modules — import/export (standard)
2017: Dynamic import() — import('./module.js')
2021: import.meta — module metadata
2023: Import attributes — import json from './data.json' with { type: 'json' }
```

## 유형 시스템 진화
```
2012: TypeScript 0.8 (Microsoft) — optional static typing
2014: Flow (Facebook) — alternative type checker
2018: TypeScript gains momentum (Angular adopts it)
2020: TypeScript 4.0 — labeled tuples, variadic tuples
2022: TypeScript 4.8 — improved narrowing
2024: TypeScript 5.x — decorators, const type params
2025: TypeScript dominates enterprise JS development
```

## 런타임 진화
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

## 생태계 성장
```
2010: npm launches with 12,000 packages
2015: npm reaches 200,000 packages
2017: yarn alternative package manager
2020: npm reaches 1.3 million packages
2023: 2+ million packages on npm
2025: JavaScript/TypeScript — most deployed language on Earth
```
