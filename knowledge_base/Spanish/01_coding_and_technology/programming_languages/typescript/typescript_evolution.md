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

# TypeScript: historial de versiones y evolución
## Línea de tiempo
| Versión | Fecha de lanzamiento | Tema clave |
|---------|-------------|-----------|
| 0,8 | Octubre de 2012 | Publicación pública inicial (Anders Hejlsberg) |
| 0,9 | abril de 2013 | Genéricos |
| 1.0 | abril de 2014 | Primera versión estable |
| 1.1 | noviembre de 2014 | Rendimiento del compilador |
| 1.4 | enero de 2015 | Tipos de literales de plantilla (básicos),`let`|
| 1.5 | julio de 2015 |  `namespace`, `destructuring`,`for...of`|
| 1.6 | Septiembre de 2015 |  Clases `abstract`, soporte JSX |
| 1.7 | noviembre de 2015 | `async/await`(objetivo ES2017) |
| 1.8 | febrero de 2016 | Cadenas de plantilla etiquetadas,`--strictNullChecks`|
| 2.0 | Septiembre de 2016 | **Principal**: tipos de unión/intersección,`never`,`keyof`,`protected`|
| 2.1 | diciembre de 2016 |  `keyof`, tipos mapeados, generadores`async`|
| 2.2 | febrero de 2017 |  Tipo `object`, mejorado`this`|
| 2.3 | abril de 2017 | Valores predeterminados genéricos, modo`--strict`|
| 2.4 | junio de 2017 | Tipos débiles, enumeraciones de cadenas |
| 2.5 | Septiembre de 2017 | Encuadernación de captura opcional |
| 2.6 | Octubre de 2017 | Tipos de funciones estrictas,`--strictFunctionTypes`|
| 2.7 | enero de 2018 | Asignación definitiva (`!`), enumeraciones`const`|
| 2.8 | marzo de 2018 | **Tipos condicionales**, `Exclude`,`Extract`|
| 2.9 | junio de 2018 | `keyof`para números/símbolos, tipos`import()`|
| 3.0 | julio de 2018 | **Principal**: Tuplas en reposo, `unknown`, referencias del proyecto |
| 3.1 | Septiembre de 2018 | Tipos mapeados en tuplas, matrices`readonly`|
| 3.2 | noviembre de 2018 |  `bigint`,`object`extendido |
| 3.4 | marzo de 2019 |  Afirmaciones `const`, inferencia de tipos de orden superior |
| 3.5 | mayo 2019 | `Omit`tipo de ayudante |
| 3.7 | noviembre de 2019 | **Encadenamiento opcional**, coalescencia nula, tipos recursivos |
| 3.8 | febrero de 2020 |  Importaciones/exportaciones `type-only`, campos`#private`|
| 3.9 | mayo 2020 |  `// @ts-expect-error`, inferencia mejorada |
| 4.0 | agosto de 2020 | **Principal**: tuplas variadas, tuplas etiquetadas, tipos literales de plantilla |
| 4.1 | noviembre de 2020 | **Tipos de literales de plantilla**, reasignación de claves, condicional recursivo |
| 4.2 | febrero de 2021 | Propiedades abstractas,`~`en tipos mapeados |
| 4.3 | junio de 2021 | Tipos de escritura separados, palabra clave`override`|
| 4.4 | agosto de 2021 | Firmas de símbolo/índice, estrechamiento del flujo de control |
| 4.5 | noviembre de 2021 | `.d.ts`de `.js`,`await`en`.d.ts`|
| 4.6 | febrero de 2022 | Verificaciones de funciones con ámbito de bloque, tipos exactos de resto de objetos |
| 4.7 | Mayo 2022 |  Restricciones de`extends`para `infer`, ESM en`.ts`|
| 4.8 | agosto de 2022 | Reducción de intersecciones mejorada, correcciones`--strictNullChecks`|
| 4.9 | noviembre de 2022 | ** Operador`satisfies`**, estrechamiento`in`|
| 5.0 | marzo de 2023 | **Principal**: parámetros de tipo `const`, decoradores, revisión de`enum`|
| 5.1 | junio de 2023 | Configuradores de tipos no relacionados,`--exactOptionalPropertyTypes`|
| 5.2 | agosto de 2023 |  Declaraciones`using`(gestión explícita de recursos) |
| 5.3 | noviembre de 2023 | Atributos de importación, estrechamiento`switch true`|
| 5.4 | marzo de 2024 |  Utilidad `NoInfer`, parámetros de cierre reducidos |
| 5.5 | junio de 2024 | Predicados de tipo inferido,`@`para expresiones regulares |
| 5.6 | septiembre de 2024 |  `--erasableSyntaxOnly`, ayudantes de iterador |
| 5.7 | noviembre de 2024 |  `--noCheck`, terminaciones de caminos |
| 5.8 | febrero de 2025 |`isolatedDeclarations`mejorado |
## Hitos importantes
### Primeros días (2012-2015)
- **0.8 (2012)**: Anders Hejlsberg (creador de C#) lidera TypeScript en Microsoft
- **1.0 (2014)**: versión estable; clases, interfaces, tipos básicos
- **1.5 (2015)**: características de ES6: desestructuración, espacios de nombres, `for...of`
### La revolución tipográfica (2016-2018)
- **2.0 (2016)**: tipos de unión, tipos de intersección, `never`, `keyof`: el sistema de tipos de TypeScript se vuelve único
- **2.8 (2018)**: Tipos condicionales: la base para la programación avanzada de nivel de tipo
- **3.0 (2018)**: Tuplas en parámetros en reposo, tipo `unknown`, referencias de proyecto
### TypeScript moderno (2019-presente)
- **3.7 (2019)**: Encadenamiento opcional`?.`y coalescencia nula`??`(¡antes del estándar JS!)
- **4.0 (2020)**: tuplas variadas, tipos literales de plantilla
- **4.1 (2020)**: Tipos literales de plantilla: manipulación de cadenas a nivel de tipo
- **4.9 (2022)**: operador `satisfies`: verificación de tipo sin ampliación
- **5.0 (2023)**: Parámetros de tipo `const`, decoradores (etapa 3)
- **5.2 (2023)**: Declaraciones `using`: gestión explícita de recursos
## Evolución del sistema tipo
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

## Evolución del decorador
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## Evolución de la configuración
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## Crecimiento del ecosistema
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## Decisiones clave de diseño
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
