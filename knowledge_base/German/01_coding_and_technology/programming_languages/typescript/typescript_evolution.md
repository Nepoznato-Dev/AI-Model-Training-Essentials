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
# TypeScript – Versionsverlauf und Entwicklung
## Zeitleiste
| Version | Erscheinungsdatum | Schlüsselthema |
|---------|-------------|-----------|
| 0,8 | Okt. 2012 | Erste öffentliche Veröffentlichung (Anders Hejlsberg) |
| 0,9 | April 2013 | Generika |
| 1,0 | April 2014 | Erste stabile Veröffentlichung |
| 1.1 | November 2014 | Compilerleistung |
| 1,4 | Januar 2015 | Vorlagenliteraltypen (einfach),`let`|
| 1,5 | Juli 2015 | `namespace`,`destructuring`,`for...of`|
| 1,6 | September 2015 |  `abstract`-Klassen, JSX-Unterstützung |
| 1,7 | November 2015 | `async/await`(ES2017-Ziel) |
| 1,8 | Februar 2016 | Markierte Vorlagenzeichenfolgen,`--strictNullChecks`|
| 2,0 | September 2016 | **Hauptsächlich**: Vereinigungs-/Schnittpunkttypen, `never`, `keyof`,`protected`|
| 2.1 | Dez. 2016 | `keyof`, zugeordnete Typen,`async`Generatoren |
| 2.2 | Februar 2017 |  Typ `object`, verbessert`this`|
| 2.3 | April 2017 | Allgemeine Standardeinstellungen, `--strict`-Modus |
| 2,4 | Juni 2017 | Schwache Typen, String-Enums |
| 2,5 | September 2017 | Optionale Fangbindung |
| 2,6 | Okt. 2017 | Strikte Funktionstypen,`--strictFunctionTypes`|
| 2,7 | Januar 2018 | Definitive Zuweisung (`!`),`const`Aufzählungen |
| 2,8 | März 2018 | **Bedingte Typen**,`Exclude`,`Extract`|
| 2,9 | Juni 2018 | `keyof`für Zahlen/Symbole, `import()`-Typen |
| 3,0 | Juli 2018 | **Hauptfach**: Tupel in Ruhe, `unknown`, Projektreferenzen |
| 3.1 | September 2018 | Zugeordnete Typen auf Tupeln, `readonly`-Arrays |
| 3.2 | November 2018 | `bigint`,`object`Spread |
| 3,4 | März 2019 | `const`Behauptungen, Typinferenz höherer Ordnung |
| 3,5 | Mai 2019 | `Omit`Hilfstyp |
| 3,7 | November 2019 | **Optionale Verkettung**, Nullish-Koaleszenz, rekursive Typen |
| 3,8 | Februar 2020 | `type-only`Importe/Exporte,`#private`Felder |
| 3,9 | Mai 2020 | `// @ts-expect-error`, verbesserte Inferenz |
| 4,0 | August 2020 | **Hauptsächlich**: Variadische Tupel, beschriftete Tupel, Vorlagenliteraltypen |
| 4.1 | November 2020 | **Vorlagenliteraltypen**, Schlüsselneuzuordnung, rekursive Bedingung |
| 4.2 | Februar 2021 | Abstrakte Eigenschaften,`~`in zugeordneten Typen |
| 4.3 | Juni 2021 | Separate Schreibtypen, Schlüsselwort`override`|
| 4,4 | August 2021 | Symbol-/Indexsignaturen, Einschränkung des Kontrollflusses |
| 4,5 | Nov. 2021 | `.d.ts`von`.js`,`await`in`.d.ts`|
| 4,6 | Februar 2022 | Blockbezogene Funktionsprüfungen, exakte Objektresttypen |
| 4,7 | Mai 2022 |  `extends`-Einschränkungen für `infer`, ESM in`.ts`|
| 4,8 | August 2022 | Verbesserte Kreuzungsreduzierung, `--strictNullChecks`-Korrekturen |
| 4,9 | Nov. 2022 | ** `satisfies`-Operator**, `in`-Verengung |
| 5,0 | März 2023 | **Major**: `const`-Typparameter, Dekoratoren, `enum`-Überarbeitung |
| 5.1 | Juni 2023 | Nicht verwandte Typsetzer,`--exactOptionalPropertyTypes`|
| 5.2 | August 2023 |  `using`-Deklarationen (explizite Ressourcenverwaltung) |
| 5,3 | Nov. 2023 | Importattribute,`switch true`Eingrenzung |
| 5,4 | März 2024 | `NoInfer`Dienstprogramm, eingegrenzte Verschlussparameter |
| 5,5 | Juni 2024 | Abgeleitete Typprädikate,`@`für Regex |
| 5,6 | September 2024 | `--erasableSyntaxOnly`, Iterator-Helfer |
| 5,7 | Nov. 2024 | `--noCheck`, Pfadvervollständigungen |
| 5,8 | Februar 2025 | Verbesserter`isolatedDeclarations`|
## Wichtige Meilensteine
### Anfänge (2012–2015)
- **0.8 (2012)**: Anders Hejlsberg (C#-Ersteller) leitet TypeScript bei Microsoft
- **1.0 (2014)**: Stabile Version; Klassen, Schnittstellen, Grundtypen
- **1.5 (2015)**: ES6-Funktionen – Destrukturierung, Namespaces, `for...of`
### Die Typenrevolution (2016–2018)
- **2.0 (2016)**: Union-Typen, Schnittmengentypen, `never`,`keyof`– Das Typsystem von TypeScript wird einzigartig
- **2.8 (2018)**: Bedingte Typen – die Grundlage für fortgeschrittene Programmierung auf Typebene
- **3.0 (2018)**: Tupel in Ruheparametern, Typ `unknown`, Projektreferenzen
### Modernes TypeScript (2019–heute)
- **3.7 (2019)**: Optionale Verkettung von`?.`und Nullish-Koaleszenz von`??`(vor dem JS-Standard!)
- **4.0 (2020)**: Variadische Tupel, Vorlagenliteraltypen
- **4.1 (2020)**: Vorlagenliteraltypen – String-Manipulation auf Typebene
- **4.9 (2022)**: `satisfies`-Operator – Typprüfung ohne Erweiterung
- **5.0 (2023)**: `const`-Typparameter, Dekoratoren (Stufe 3)
- **5.2 (2023)**: `using`-Deklarationen – explizite Ressourcenverwaltung
## Typsystementwicklung
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

## Dekorateur-Evolution
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## Konfigurationsentwicklung
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## Ökosystemwachstum
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## Wichtige Designentscheidungen
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
