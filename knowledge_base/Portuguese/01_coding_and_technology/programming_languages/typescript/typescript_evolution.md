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
# TypeScript – Histórico de versões e evolução
## Linha do tempo
| Versão | Data de lançamento | Tema principal |
|--------|-------------|-----------|
| 0,8 | Outubro 2012 | Lançamento público inicial (Anders Hejlsberg) |
| 0,9 | abril de 2013 | Genéricos |
| 1,0 | abril de 2014 | Primeira versão estável |
| 1.1 | Novembro de 2014 | Desempenho do compilador |
| 1.4 | Janeiro de 2015 | Tipos literais de modelo (básico),`let`|
| 1,5 | Julho de 2015 | `namespace`,`destructuring`,`for...of`|
| 1.6 | Setembro de 2015 |  Classes `abstract`, suporte JSX |
| 1.7 | Novembro de 2015 | `async/await`(meta ES2017) |
| 1.8 | Fevereiro de 2016 | Sequências de modelo marcadas,`--strictNullChecks`|
| 2.0 | Setembro de 2016 | **Principal**: Tipos de união/interseção,`never`,`keyof`,`protected`|
| 2.1 | dezembro de 2016 |  `keyof`, tipos mapeados, geradores`async`|
| 2.2 | Fevereiro de 2017 |  Tipo `object`,`this`aprimorado |
| 2.3 | abril de 2017 | Padrões genéricos, modo`--strict`|
| 2.4 | Junho de 2017 | Tipos fracos, enums de string |
| 2,5 | Setembro de 2017 | Ligação de captura opcional |
| 2.6 | Outubro 2017 | Tipos de função estritos,`--strictFunctionTypes`|
| 2.7 | Janeiro de 2018 | Atribuição definida (`!`), enumerações`const`|
| 2.8 | março de 2018 | **Tipos condicionais**,`Exclude`,`Extract`|
| 2.9 | Junho de 2018 | `keyof`para numérico/símbolo, tipos`import()`|
| 3.0 | Julho de 2018 | **Principal**: Tuplas em repouso,`unknown`, referências do projeto |
| 3.1 | Setembro de 2018 | Tipos mapeados em tuplas, matrizes`readonly`|
| 3.2 | Novembro de 2018 |  `bigint`,`object`spread |
| 3.4 | março de 2019 |  Asserções `const`, inferência de tipo de ordem superior |
| 3.5 | Maio de 2019 |  Tipo auxiliar`Omit`|
| 3.7 | Novembro de 2019 | **Encadeamento opcional**, coalescência nula, tipos recursivos |
| 3.8 | Fevereiro de 2020 |  Importações/exportações `type-only`, campos`#private`|
| 3.9 | Maio de 2020 |  `// @ts-expect-error`, inferência aprimorada |
| 4,0 | Agosto de 2020 | **Principal**: Tuplas variáveis, tuplas rotuladas, tipos literais de modelo |
| 4.1 | Novembro de 2020 | **Tipos literais de modelo**, remapeamento de chave, condicional recursiva |
| 4.2 | Fevereiro de 2021 | Propriedades abstratas,`~`em tipos mapeados |
| 4.3 | Junho de 2021 | Tipos de gravação separados, palavra-chave`override`|
| 4.4 | agosto de 2021 | Assinaturas de símbolos/índices, estreitamento do fluxo de controle |
| 4,5 | Novembro de 2021 | `.d.ts`de `.js`,`await`em`.d.ts`|
| 4.6 | Fevereiro de 2022 | Verificações de função com escopo de bloco, tipos exatos de resto de objeto |
| 4.7 | Maio de 2022 |  Restrições`extends`para`infer`, ESM em`.ts`|
| 4.8 | agosto de 2022 | Redução de interseção aprimorada, correções`--strictNullChecks`|
| 4.9 | Novembro de 2022 | ** Operador `satisfies`**, estreitamento`in`|
| 5,0 | Março de 2023 | **Principal**: parâmetros do tipo `const`, decoradores, revisão do`enum`|
| 5.1 | Junho de 2023 | Configuradores de tipo não relacionados,`--exactOptionalPropertyTypes`|
| 5.2 | agosto de 2023 |  Declarações`using`(gerenciamento explícito de recursos) |
| 5.3 | Novembro de 2023 | Atributos de importação, estreitamento`switch true`|
| 5.4 | Março de 2024 |  Utilitário `NoInfer`, parâmetros de fechamento reduzidos |
| 5.5 | Junho de 2024 | Predicados de tipo inferido,`@`para regex |
| 5.6 | Setembro de 2024 | `--erasableSyntaxOnly`, ajudantes do iterador |
| 5.7 | Novembro de 2024 | `--noCheck`, conclusões de caminho |
| 5.8 | Fevereiro de 2025 |`isolatedDeclarations`aprimorado |
## Marcos importantes
### Primeiros dias (2012–2015)
- **0.8 (2012)**: Anders Hejlsberg (criador de C#) lidera TypeScript na Microsoft
- **1.0 (2014)**: Versão estável; classes, interfaces, tipos básicos
- **1.5 (2015)**: recursos ES6 — desestruturação, namespaces, `for...of`
### A revolução dos tipos (2016–2018)
- **2.0 (2016)**: Tipos de união, tipos de interseção,`never`,`keyof`— O sistema de tipos do TypeScript torna-se único
- **2.8 (2018)**: Tipos condicionais — a base para programação avançada em nível de tipo
- **3.0 (2018)**: Tuplas em parâmetros restantes, tipo `unknown`, referências de projeto
### TypeScript moderno (2019-presente)
- **3.7 (2019)**: Encadeamento opcional`?.`e coalescência nula`??`(antes do padrão JS!)
- **4.0 (2020)**: tuplas variáveis, tipos literais de modelo
- **4.1 (2020)**: Tipos literais de modelo — manipulação de string em nível de tipo
- **4.9 (2022)**: operador`satisfies`— verificação de tipo sem ampliação
- **5.0 (2023)**: parâmetros do tipo `const`, decoradores (estágio 3)
- **5.2 (2023)**: declarações`using`— gerenciamento explícito de recursos
## Tipo Evolução do Sistema
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

## Evolução do Decorador
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## Evolução da configuração
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## Crescimento do Ecossistema
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## Principais decisões de design
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
