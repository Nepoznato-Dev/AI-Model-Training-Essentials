<!--
---
# Metadata
title: "TypeScript — Version History & Evolution"
description: "Comprehensive version history and evolution of TypeScript from 0.8 to modern TypeScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# TypeScript - Historia ya Toleo na Mageuzi
## Rekodi ya matukio
| Toleo | Tarehe ya Kutolewa | Mandhari Muhimu |
|---------|-------------|-----------|
| 0.8 | Oktoba 2012 | Toleo la kwanza la umma (Anders Hejlsberg) |
| 0.9 | Aprili 2013 | Jenetiki |
| 1.0 | Aprili 2014 | Toleo la kwanza thabiti |
| 1.1 | Nov 2014 | Utendaji wa mkusanyaji |
| 1.4 | Januari 2015 | Aina halisi za kiolezo (msingi),`let`|
| 1.5 | Julai 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | Septemba 2015 |  Madarasa ya `abstract`, usaidizi wa JSX |
| 1.7 | Nov 2015 | `async/await`(lengo la ES2017) |
| 1.8 | Februari 2016 | Mifuatano ya kiolezo iliyotambulishwa,`--strictNullChecks`|
| 2.0 | Septemba 2016 | **Meja**: Aina za Muungano/makutano,`never`,`keyof`,`protected`|
| 2.1 | Desemba 2016 | `keyof`, aina zilizochorwa, jenereta za`async`|
| 2.2 | Februari 2017 |  aina ya `object`, iliyoboreshwa`this`|
| 2.3 | Aprili 2017 | Chaguo-msingi za kawaida, hali ya`--strict`|
| 2.4 | Juni 2017 | Aina dhaifu, kamba enums |
| 2.5 | Septemba 2017 | Hiari ya kukamata samaki |
| 2.6 | Oktoba 2017 | Aina kali za utendakazi,`--strictFunctionTypes`|
| 2.7 | Januari 2018 | Mgawo wa uhakika (`!`),`const`enums |
| 2.8 | Machi 2018 | **Aina za masharti**,`Exclude`,`Extract`|
| 2.9 | Juni 2018 | `keyof`kwa aina/alama za nambari,`import()`aina |
| 3.0 | Julai 2018 | **Meja**: Tuples katika mapumziko,`unknown`, marejeleo ya mradi |
| 3.1 | Septemba 2018 | Aina zilizowekwa kwenye ramani, safu za`readonly`|
| 3.2 | Novemba 2018 | `bigint`,`object`kuenea |
| 3.4 | Machi 2019 |  Madai ya `const`, aina ya maagizo ya juu |
| 3.5 | Mei 2019 | `Omit`aina ya msaidizi |
| 3.7 | Novemba 2019 | **Mnyororo wa hiari**, ubatilishaji wa kuunganisha, aina za kujirudia |
| 3.8 | Februari 2020 | `type-only`uagizaji/uuzaji nje, mashamba ya`#private`|
| 3.9 | Mei 2020 | `// @ts-expect-error`, uelekezaji ulioboreshwa |
| 4.0 | Agosti 2020 | **Kubwa**: Nakala anuwai, nakala zilizo na lebo, aina halisi za violezo |
| 4.1 | Novemba 2020 | **Aina za kiolezo halisi**, urekebishaji wa ufunguo, masharti ya kujirudia |
| 4.2 | Februari 2021 | Sifa za muhtasari,`~`katika aina zilizopangwa |
| 4.3 | Juni 2021 | Aina tofauti za uandishi, neno kuu la`override`|
| 4.4 | Agosti 2021 | Saini za ishara/faharasa, mtiririko wa udhibiti unapungua |
| 4.5 | Novemba 2021 | `.d.ts`kutoka`.js`,`await`katika`.d.ts`|
| 4.6 | Februari 2022 | Hundi za kukokotoa zilizo na upeo wa kuzuia, aina kamili za mapumziko ya kitu |
| 4.7 | Mei 2022 |  Vikwazo vya`extends`kwa`infer`, ESM katika`.ts`|
| 4.8 | Agosti 2022 | Upunguzaji wa makutano ulioboreshwa, Marekebisho ya`--strictNullChecks`|
| 4.9 | Novemba 2022 | ** Opereta wa `satisfies`**,`in`inapunguza |
| 5.0 | Machi 2023 | **Meja**: Vigezo vya aina ya `const`, wapambaji, urekebishaji wa`enum`|
| 5.1 | Juni 2023 | Seti za aina zisizohusiana,`--exactOptionalPropertyTypes`|
| 5.2 | Agosti 2023 | `using`matamko (usimamizi dhahiri wa rasilimali) |
| 5.3 | Novemba 2023 | Sifa za kuagiza,`switch true`inapunguza |
| 5.4 | Machi 2024 | `NoInfer`shirika, vigezo finyu vya kufungwa |
| 5.5 | Juni 2024 | Vihusishi vya aina iliyorejelewa,`@`kwa regex |
| 5.6 | Septemba 2024 | `--erasableSyntaxOnly`, wasaidizi wa iterator |
| 5.7 | Novemba 2024 | `--noCheck`, ukamilishaji wa njia |
| 5.8 | Februari 2025 | Imeboreshwa`isolatedDeclarations`|
## Mafanikio Makuu
### Siku za Mapema (2012–2015)
- **0.8 (2012)**: Anders Hejlsberg (C# muundaji) anaongoza TypeScript katika Microsoft
- ** 1.0 (2014) **: Kutolewa kwa utulivu; madarasa, miingiliano, aina za msingi
- **1.5 (2015)**: Vipengele vya ES6 - uharibifu, nafasi za majina, `for...of`
### Aina ya Mapinduzi (2016–2018)
- **2.0 (2016)**: Aina za muungano, aina za makutano,`never`,`keyof`— Mfumo wa aina ya TypeScript unakuwa wa kipekee
- **2.8 (2018)**: Aina za masharti — msingi wa upangaji programu wa kiwango cha juu
- **3.0 (2018)**: Nakala katika vigezo vya kupumzika, aina ya `unknown`, marejeleo ya mradi
### TypeScript ya Kisasa (2019–sasa)
- **3.7 (2019)**: Kuunganisha kwa hiari`?.`na kubatilisha uunganishaji`??`(kabla ya kiwango cha JS!)
- **4.0 (2020)**: Nakala anuwai, aina halisi za violezo
- **4.1 (2020)**: Aina halisi za violezo - uchezaji wa kamba wa kiwango cha aina
- **4.9 (2022)**: Opereta`satisfies`— aina ya kuangalia bila kupanua
- **5.0 (2023)**: Vigezo vya aina ya `const`, wapambaji (hatua ya 3)
- **5.2 (2023)**: matamko ya`using`— usimamizi wa rasilimali wazi
## Aina ya Mageuzi ya Mfumo
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

## Mageuzi ya Wapambaji
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## Mageuzi ya Usanidi
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## Ukuaji wa Mfumo ikolojia
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## Maamuzi Muhimu ya Usanifu
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
