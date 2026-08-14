---
# Metadata
title: "TypeScript — Version History & Evolution"
description: "Comprehensive version history and evolution of TypeScript from 0.8 to modern TypeScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [typescript, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# TypeScript — Kasaysayan ng Bersyon at Ebolusyon
## Timeline
| Bersyon | Petsa ng Paglabas | Pangunahing Tema |
|---------|-------------|-----------|
| 0.8 | Okt 2012 | Paunang pampublikong pagpapalabas (Anders Hejlsberg) |
| 0.9 | Abr 2013 | Generics |
| 1.0 | Abr 2014 | Unang matatag na release |
| 1.1 | Nob 2014 | Pagganap ng compiler |
| 1.4 | Ene 2015 | Mga literal na uri ng template (basic),`let`|
| 1.5 | Hul 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | Set 2015 | `abstract`na mga klase, suporta sa JSX |
| 1.7 | Nob 2015 | `async/await`(target ng ES2017) |
| 1.8 | Peb 2016 | Naka-tag na mga string ng template,`--strictNullChecks`|
| 2.0 | Set 2016 | **Major**: Mga uri ng unyon/intersection,`never`,`keyof`,`protected`|
| 2.1 | Dis 2016 | `keyof`, mga naka-map na uri,`async`generators |
| 2.2 | Peb 2017 |  Uri ng `object`, pinahusay na`this`|
| 2.3 | Abr 2017 | Mga generic na default,`--strict`mode |
| 2.4 | Hun 2017 | Mga mahihinang uri, mga string enum |
| 2.5 | Set 2017 | Opsyonal na catch binding |
| 2.6 | Okt 2017 | Mga uri ng mahigpit na function,`--strictFunctionTypes`|
| 2.7 | Ene 2018 | Tiyak na takdang-aralin (`!`),`const`enum |
| 2.8 | Mar 2018 | **Mga uri ng kondisyon**,`Exclude`,`Extract`|
| 2.9 | Hun 2018 | `keyof`para sa numeric/simbolo, mga uri ng`import()`|
| 3.0 | Hul 2018 | **Major**: Tuples in rest,`unknown`, mga sanggunian sa proyekto |
| 3.1 | Set 2018 | Mga naka-map na uri sa mga tuple,`readonly`array |
| 3.2 | Nob 2018 | `bigint`,`object`kumalat |
| 3.4 | Mar 2019 | `const`assertion, mas mataas na pagkakasunod-sunod na uri ng inference |
| 3.5 | Mayo 2019 | `Omit`uri ng katulong |
| 3.7 | Nob 2019 | **Opsyonal na chaining**, nullish coalescing, recursive na mga uri |
| 3.8 | Peb 2020 | `type-only`mga import/export,`#private`na mga field |
| 3.9 | Mayo 2020 | `// @ts-expect-error`, pinahusay na hinuha |
| 4.0 | Ago 2020 | **Major**: Variadic tuple, may label na tuple, template literal na mga uri |
| 4.1 | Nobyembre 2020 | **Mga literal na uri ng template**, key remapping, recursive conditional |
| 4.2 | Peb 2021 | Mga abstract na katangian,`~`sa mga naka-map na uri |
| 4.3 | Hun 2021 | Paghiwalayin ang mga uri ng pagsulat,`override`keyword |
| 4.4 | Ago 2021 | Mga lagda ng simbolo/index, pagpapaliit ng daloy ng kontrol |
| 4.5 | Nob 2021 | `.d.ts`mula sa`.js`,`await`sa`.d.ts`|
| 4.6 | Peb 2022 | Block-scoped function checks, object rest eksaktong mga uri |
| 4.7 | Mayo 2022 | `extends`mga hadlang para sa`infer`, ESM sa`.ts`|
| 4.8 | Ago 2022 | Pinahusay na pagbabawas ng intersection, mga pag-aayos ng`--strictNullChecks`|
| 4.9 | Nob 2022 | **`satisfies`operator**,`in`na nagpapaliit |
| 5.0 | Mar 2023 | **Major**:`const`type params, decorators,`enum`overhaul |
| 5.1 | Hun 2023 | Hindi nauugnay na mga setters ng uri,`--exactOptionalPropertyTypes`|
| 5.2 | Ago 2023 | `using`mga deklarasyon (tahasang pamamahala ng mapagkukunan) |
| 5.3 | Nob 2023 | Mag-import ng mga attribute,`switch true`na nagpapaliit |
| 5.4 | Mar 2024 | `NoInfer`utility, narrowed closure params |
| 5.5 | Hun 2024 | Inferred type predicates,`@`para sa regex |
| 5.6 | Set 2024 | `--erasableSyntaxOnly`, mga tagatulong ng iterator |
| 5.7 | Nob 2024 | `--noCheck`, mga pagkumpleto ng landas |
| 5.8 | Peb 2025 | Pinahusay na`isolatedDeclarations`|
## Mga Pangunahing Milestone
### Mga Unang Araw (2012–2015)
- **0.8 (2012)**: Pinangunahan ni Anders Hejlsberg (C# creator) ang TypeScript sa Microsoft
- **1.0 (2014)**: Stable na release; mga klase, mga interface, mga pangunahing uri
- **1.5 (2015)**: Mga feature ng ES6 — pagsira, mga namespace, `for...of`
### Ang Uri ng Rebolusyon (2016–2018)
- **2.0 (2016)**: Mga uri ng unyon, mga uri ng intersection,`never`,`keyof`— Nagiging natatangi ang type system ng TypeScript
- **2.8 (2018)**: Mga kondisyong uri — ang pundasyon para sa advanced na uri-level na programming
- **3.0 (2018)**: Mga Tuple sa mga parameter ng pahinga, uri ng `unknown`, mga sanggunian sa proyekto
### Modern TypeScript (2019–kasalukuyan)
- **3.7 (2019)**: Opsyonal na chaining`?.`at nullish coalescing`??`(bago ang JS standard!)
- **4.0 (2020)**: Variadic tuple, mga literal na uri ng template
- **4.1 (2020)**: Mga literal na uri ng template — pagmamanipula ng string sa antas ng uri
- **4.9 (2022)**:`satisfies`operator — type checking nang hindi lumalawak
- **5.0 (2023)**: Mga parameter ng uri ng `const`, mga dekorador (yugto 3)
- **5.2 (2023)**: Mga deklarasyon ng`using`— tahasang pamamahala ng mapagkukunan
## Uri ng System Evolution
```
2012: Basic types, classes, interfaces
2014: Generics, enums
2016: Union types, intersection types, discriminated unions
2018: Conditional types, mapped types, keyof, infer
2020: Template literal types, variadic tuples
2022: satisfies operator
2023: const type parameters
2023: using declarations
```

## Ebolusyon ng Dekorador
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## Ebolusyon ng Configuration
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## Paglago ng Ecosystem
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## Pangunahing Desisyon sa Disenyo
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
