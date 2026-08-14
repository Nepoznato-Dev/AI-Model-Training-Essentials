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
# TypeScript — historia wersji i ewolucja
## Oś czasu
| Wersja | Data wydania | Kluczowy motyw |
|--------|------------|---------|
| 0,8 | październik 2012 | Pierwsze publiczne wydanie (Anders Hejlsberg) |
| 0,9 | kwiecień 2013 | Genetyki |
| 1,0 | kwiecień 2014 | Pierwsza stabilna wersja |
| 1.1 | listopad 2014 | Wydajność kompilatora |
| 1,4 | styczeń 2015 | Typy literałów szablonowych (podstawowe),`let`|
| 1,5 | lipiec 2015 | `namespace`,`destructuring`,`for...of`|
| 1,6 | wrzesień 2015 |  Klasy `abstract`, obsługa JSX |
| 1,7 | listopad 2015 | `async/await`(cel ES2017) |
| 1,8 | luty 2016 | Oznaczone ciągi szablonów,`--strictNullChecks`|
| 2,0 | wrzesień 2016 | **Główne**: Typy złączy/przecięć,`never`,`keyof`,`protected`|
| 2.1 | grudzień 2016 | `keyof`, typy mapowane, generatory`async`|
| 2.2 | luty 2017 |  Typ `object`, ulepszony`this`|
| 2.3 | kwiecień 2017 | Ogólne ustawienia domyślne, tryb`--strict`|
| 2.4 | czerwiec 2017 | Słabe typy, wyliczenia ciągów |
| 2,5 | wrzesień 2017 | Opcjonalne wiązanie zatrzaskowe |
| 2.6 | październik 2017 | Ścisłe typy funkcji,`--strictFunctionTypes`|
| 2.7 | styczeń 2018 | Przypisanie określone (`!`), wyliczenia`const`|
| 2.8 | marzec 2018 | **Typy warunkowe**,`Exclude`,`Extract`|
| 2.9 | czerwiec 2018 | `keyof`dla typów numerycznych/symbolowych,`import()`|
| 3,0 | lipiec 2018 | **Główne**: Krotki w spoczynku,`unknown`, referencje projektu |
| 3.1 | wrzesień 2018 | Mapowane typy na krotkach, tablice`readonly`|
| 3.2 | listopad 2018 | `bigint`,`object`spread |
| 3.4 | marzec 2019 |  Asercje `const`, wnioskowanie o typie wyższego rzędu |
| 3,5 | maj 2019 |  Typ pomocniczy`Omit`|
| 3,7 | listopad 2019 | **Opcjonalne łączenie**, łączenie zerowe, typy rekurencyjne |
| 3,8 | luty 2020 |  Import/eksport `type-only`, pola`#private`|
| 3,9 | maj 2020 |  `// @ts-expect-error`, ulepszone wnioskowanie |
| 4,0 | sierpień 2020 | **Główne**: krotki wariadyczne, krotki oznaczone, typy literałów szablonowych |
| 4.1 | listopad 2020 | **Typy literałów szablonów**, ponowne mapowanie kluczy, rekurencyjny tryb warunkowy |
| 4.2 | luty 2021 | Właściwości abstrakcyjne,`~`w mapowanych typach |
| 4.3 | czerwiec 2021 | Oddzielne typy zapisu, słowo kluczowe`override`|
| 4.4 | sierpień 2021 | Sygnatury symboli/indeksów, zawężenie przepływu sterowania |
| 4,5 | listopad 2021 | `.d.ts`z`.js`,`await`w`.d.ts`|
| 4,6 | luty 2022 | Sprawdzanie funkcji o zasięgu blokowym, dokładne typy obiektów |
| 4,7 | maj 2022 |  Ograniczenia`extends`dla`infer`, ESM w`.ts`|
| 4,8 | sierpień 2022 | Ulepszona redukcja skrzyżowań, poprawki`--strictNullChecks`|
| 4,9 | listopad 2022 | **Napęd `satisfies`**, zwężenie`in`|
| 5,0 | marzec 2023 | **Główne**: Parametry typu `const`, dekoratory, remont`enum`|
| 5.1 | czerwiec 2023 | Niepowiązane ustawiacze typów,`--exactOptionalPropertyTypes`|
| 5.2 | sierpień 2023 |  Deklaracje`using`(jawne zarządzanie zasobami) |
| 5.3 | listopad 2023 | Import atrybutów, zawężenie`switch true`|
| 5.4 | marzec 2024 | `NoInfer`użytkowy, zawężone parametry zamknięcia |
| 5,5 | czerwiec 2024 | Wywnioskowane predykaty typu,`@`dla wyrażenia regularnego |
| 5,6 | wrzesień 2024 | `--erasableSyntaxOnly`, pomocnicy iteratora |
| 5,7 | listopad 2024 | `--noCheck`, uzupełnienia ścieżek |
| 5,8 | luty 2025 | Ulepszony`isolatedDeclarations`|
## Główne kamienie milowe
### Wczesne dni (2012–2015)
- **0,8 (2012)**: Anders Hejlsberg (twórca C#) kieruje TypeScriptem w Microsoft
- **1.0 (2014)**: Wersja stabilna; klasy, interfejsy, podstawowe typy
- **1.5 (2015)**: Funkcje ES6 — destrukturyzacja, przestrzenie nazw, `for...of`
### Rewolucja typów (2016–2018)
- **2.0 (2016)**: Typy unii, typy skrzyżowań, `never`,`keyof`— system typów TypeScript staje się unikalny
- **2.8 (2018)**: Typy warunkowe — podstawa zaawansowanego programowania na poziomie typów
- **3.0 (2018)**: Krotki w parametrach spoczynkowych, typ `unknown`, referencje do projektu
### Nowoczesny TypeScript (od 2019 r.)
- **3.7 (2019)**: Opcjonalne łączenie`?.`i koalescencja zerowa`??`(przed standardem JS!)
- **4.0 (2020)**: Krotki wariadyczne, typy literałów szablonowych
- **4.1 (2020)**: Typy literałów szablonowych — manipulacja ciągami na poziomie typu
- **4.9 (2022)**: operator`satisfies`— sprawdzanie typu bez poszerzania
- **5.0 (2023)**: parametry typu `const`, dekoratory (etap 3)
- **5.2 (2023)**: Deklaracje`using`– jawne zarządzanie zasobami
## Wpisz ewolucję systemu
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

## Ewolucja dekoratorów
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## Ewolucja konfiguracji
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## Rozwój ekosystemu
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## Kluczowe decyzje projektowe
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
