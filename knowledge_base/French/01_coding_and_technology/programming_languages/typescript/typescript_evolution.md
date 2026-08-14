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

# TypeScript — Historique et évolution des versions
## Chronologie
| Version | Date de sortie | Thème clé |
|---------|-------------|---------------|
| 0,8 | octobre 2012 | Première diffusion publique (Anders Hejlsberg) |
| 0,9 | avril 2013 | Génériques |
| 1.0 | avril 2014 | Première version stable |
| 1.1 | novembre 2014 | Performances du compilateur |
| 1.4 | janvier 2015 | Types littéraux de modèle (de base),`let`|
| 1.5 | juillet 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | septembre 2015 |  Classes `abstract`, prise en charge JSX |
| 1.7 | novembre 2015 | `async/await`(cible ES2017) |
| 1.8 | Février 2016 | Chaînes de modèles taguées,`--strictNullChecks`|
| 2.0 | septembre 2016 | **Majeur** : types d'union/intersection,`never`,`keyof`,`protected`|
| 2.1 | décembre 2016 |  `keyof`, types mappés, générateurs`async`|
| 2.2 | Février 2017 |  Type `object`,`this`amélioré |
| 2.3 | avril 2017 | Paramètres génériques par défaut, mode`--strict`|
| 2.4 | juin 2017 | Types faibles, énumérations de chaînes |
| 2.5 | septembre 2017 | Liaison de capture en option |
| 2.6 | octobre 2017 | Types de fonctions strictes,`--strictFunctionTypes`|
| 2.7 | janvier 2018 | Affectation définie (`!`), énumérations`const`|
| 2.8 | mars 2018 | **Types conditionnels**,`Exclude`,`Extract`|
| 2.9 | juin 2018 | `keyof`pour chiffres/symboles, types`import()`|
| 3.0 | juillet 2018 | **Majeur** : Tuples au repos,`unknown`, références du projet |
| 3.1 | septembre 2018 | Types mappés sur des tuples, tableaux`readonly`|
| 3.2 | novembre 2018 | `bigint`,`object`propagation |
| 3.4 | mars 2019 |  Assertions `const`, inférence de type d'ordre supérieur |
| 3.5 | mai 2019 | `Omit`type d'assistance |
| 3.7 | novembre 2019 | **Chaînage facultatif**, fusion nulle, types récursifs |
| 3.8 | Février 2020 |  Importations/exportations `type-only`, champs`#private`|
| 3.9 | mai 2020 | `// @ts-expect-error`, inférence améliorée |
| 4.0 | août 2020 | **Majeur** : tuples variadiques, tuples étiquetés, types littéraux de modèles |
| 4.1 | novembre 2020 | **Types littéraux de modèle**, remappage de clés, conditionnel récursif |
| 4.2 | Février 2021 | Propriétés abstraites,`~`dans les types mappés |
| 4.3 | juin 2021 | Types d'écriture séparés, mot clé`override`|
| 4.4 | août 2021 | Signatures de symboles/index, rétrécissement du flux de contrôle |
| 4.5 | novembre 2021 | `.d.ts`de`.js`,`await`dans`.d.ts`|
| 4.6 | Février 2022 | Vérifications de fonctions à l'échelle du bloc, types exacts de repos d'objet |
| 4.7 | mai 2022 |  Contraintes`extends`pour `infer`, ESM dans`.ts`|
| 4.8 | août 2022 | Réduction des intersections améliorée, correctifs`--strictNullChecks`|
| 4.9 | novembre 2022 | ** Opérateur `satisfies`**, rétrécissement`in`|
| 5.0 | mars 2023 | **Majeur** : paramètres de type `const`, décorateurs, révision de`enum`|
| 5.1 | juin 2023 | Composeurs de caractères indépendants,`--exactOptionalPropertyTypes`|
| 5.2 | août 2023 |  Déclarations`using`(gestion explicite des ressources) |
| 5.3 | novembre 2023 | Importer des attributs, rétrécissement`switch true`|
| 5.4 | mars 2024 |  Utilitaire `NoInfer`, paramètres de fermeture rétrécis |
| 5.5 | juin 2024 | Prédicats de type déduits,`@`pour regex |
| 5.6 | septembre 2024 | `--erasableSyntaxOnly`, assistants d'itérateur |
| 5.7 | novembre 2024 | `--noCheck`, complétions de chemin |
| 5.8 | Février 2025 |`isolatedDeclarations`amélioré |
## Étapes majeures
### Premiers jours (2012-2015)
- **0.8 (2012)** : Anders Hejlsberg (créateur C#) dirige TypeScript chez Microsoft
- **1.0 (2014)** : version stable ; classes, interfaces, types de base
- **1.5 (2015)** : fonctionnalités ES6 — déstructuration, espaces de noms, `for...of`
### La révolution des types (2016-2018)
- **2.0 (2016)** : types d'union, types d'intersection,`never`,`keyof`— Le système de types de TypeScript devient unique
- **2.8 (2018)** : Types conditionnels — la base d'une programmation avancée au niveau des types
- **3.0 (2018)** : Tuples dans les paramètres de repos, type `unknown`, références du projet
### TypeScript moderne (2019-présent)
- **3.7 (2019)** : Chaînage optionnel`?.`et fusion nulle`??`(avant le standard JS !)
- **4.0 (2020)** : Tuples variadiques, types littéraux de modèles
- **4.1 (2020)** : types littéraux de modèles — manipulation de chaînes au niveau du type
- **4.9 (2022)** : opérateur`satisfies`— vérification de type sans élargissement
- **5.0 (2023)** : paramètres de type `const`, décorateurs (étape 3)
- **5.2 (2023)** : déclarations`using`— gestion explicite des ressources
## Évolution du système de types
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

## Évolution du décorateur
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## Évolution de la configuration
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## Croissance de l'écosystème
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## Décisions de conception clés
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
