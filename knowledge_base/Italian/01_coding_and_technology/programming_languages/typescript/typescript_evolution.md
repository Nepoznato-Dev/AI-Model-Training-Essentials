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
# TypeScript: cronologia ed evoluzione delle versioni
## Cronologia
| Versione | Data di rilascio | Tema chiave |
|---------|-------------|-----------|
| 0,8 | ottobre 2012 | Pubblicazione iniziale (Anders Hejlsberg) |
| 0,9 | aprile 2013 | Generici |
| 1.0 | aprile 2014 | Prima versione stabile |
| 1.1 | novembre 2014 | Prestazioni del compilatore |
| 1.4 | Gennaio 2015 | Tipi letterali modello (di base),`let`|
| 1,5 | Lug 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | settembre 2015 |  Classi `abstract`, supporto JSX |
| 1.7 | novembre 2015 | `async/await`(obiettivo ES2017) |
| 1.8 | Febbraio 2016 | Stringhe modello contrassegnate con tag,`--strictNullChecks`|
| 2.0 | settembre 2016 | **Maggiore**: tipi di unione/intersezione,`never`,`keyof`,`protected`|
| 2.1 | dicembre 2016 | `keyof`, tipi mappati, generatori`async`|
| 2.2 | Febbraio 2017 |  Tipo `object`, migliorato`this`|
| 2.3 | aprile 2017 | Impostazioni predefinite generiche, modalità`--strict`|
| 2.4 | giugno 2017 | Tipi deboli, enumerazioni di stringhe |
| 2,5 | settembre 2017 | Rilegatura opzionale |
| 2.6 | ottobre 2017 | Tipi di funzioni rigorose,`--strictFunctionTypes`|
| 2.7 | Gennaio 2018 | Assegnazione definita (`!`), enumerazioni`const`|
| 2.8 | marzo 2018 | **Tipi condizionali**,`Exclude`,`Extract`|
| 2.9 | giugno 2018 | `keyof`per numeri/simboli, tipi`import()`|
| 3.0 | Lug 2018 | **Maggiore**: Tuple in riposo,`unknown`, riferimenti al progetto |
| 3.1 | settembre 2018 | Tipi mappati su tuple, array`readonly`|
| 3.2 | novembre 2018 | `bigint`,`object`diffusione |
| 3.4 | marzo 2019 |  Asserzioni `const`, inferenza di tipo di ordine superiore |
| 3,5 | Maggio 2019 | `Omit`tipo di supporto |
| 3.7 | novembre 2019 | **Concatenamento opzionale**, coalescenza nulla, tipi ricorsivi |
| 3.8 | Febbraio 2020 | `type-only`importazioni/esportazioni, campi`#private`|
| 3.9 | Maggio 2020 | `// @ts-expect-error`, inferenza migliorata |
| 4.0 | Agosto 2020 | **Maggiore**: tuple variadiche, tuple etichettate, tipi letterali template |
| 4.1 | novembre 2020 | **Tipi letterali modello**, rimappatura chiavi, condizionale ricorsivo |
| 4.2 | Febbraio 2021 | Proprietà astratte,`~`nei tipi mappati |
| 4.3 | giugno 2021 | Tipi di scrittura separati, parola chiave`override`|
| 4.4 | Agosto 2021 | Firme di simboli/indici, restringimento del flusso di controllo |
| 4.5| novembre 2021 | `.d.ts`da`.js`,`await`in`.d.ts`|
| 4.6| Febbraio 2022 | Controlli delle funzioni con ambito blocco, tipi esatti del resto degli oggetti |
| 4.7| Maggio 2022 |  Vincoli`extends`per`infer`, ESM in`.ts`|
| 4.8| Agosto 2022 | Riduzione intersezione migliorata, correzioni`--strictNullChecks`|
| 4.9 | novembre 2022 | **Operatore `satisfies`**, restringimento`in`|
| 5.0 | marzo 2023 | **Maggiore**: parametri tipo `const`, decoratori, revisione`enum`|
| 5.1 | giugno 2023 | Setter di tipo non correlati,`--exactOptionalPropertyTypes`|
| 5.2 | Agosto 2023 |  Dichiarazioni`using`(gestione esplicita delle risorse) |
| 5.3 | novembre 2023 | Attributi di importazione, restringimento`switch true`|
| 5.4 | marzo 2024 |  Utilità `NoInfer`, parametri di chiusura ristretti |
| 5,5 | giugno 2024 | Predicati di tipo dedotto,`@`per regex |
| 5.6| settembre 2024 | `--erasableSyntaxOnly`, aiutanti dell'iteratore |
| 5.7| novembre 2024 | `--noCheck`, completamenti percorso |
| 5.8| Febbraio 2025 |`isolatedDeclarations`migliorato |
## Traguardi importanti
### Primi tempi (2012-2015)
- **0.8 (2012)**: Anders Hejlsberg (creatore di C#) guida TypeScript presso Microsoft
- **1.0 (2014)**: versione stabile; classi, interfacce, tipi base
- **1.5 (2015)**: funzionalità ES6: destrutturazione, spazi dei nomi, `for...of`
### La rivoluzione dei tipi (2016–2018)
- **2.0 (2016)**: tipi di unione, tipi di intersezione,`never`, `keyof`: il sistema di tipi di TypeScript diventa unico
- **2.8 (2018)**: tipi condizionali: la base per la programmazione avanzata a livello di tipo
- **3.0 (2018)**: Tuple nei parametri rest, tipo `unknown`, riferimenti al progetto
### Modern TypeScript (2019-oggi)
- **3.7 (2019)**: concatenamento opzionale`?.`e coalescenza nulla`??`(prima dello standard JS!)
- **4.0 (2020)**: tuple variadiche, tipi letterali modello
- **4.1 (2020)**: tipi letterali modello: manipolazione di stringhe a livello di tipo
- **4.9 (2022)**: operatore `satisfies`: controllo del tipo senza ampliamento
- **5.0 (2023)**: parametri di tipo `const`, decoratori (fase 3)
- **5.2 (2023)**: dichiarazioni `using`: gestione esplicita delle risorse
## Digitare Evoluzione del sistema
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

## Evoluzione del decoratore
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## Evoluzione della configurazione
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## Crescita dell'ecosistema
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## Decisioni chiave sulla progettazione
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
