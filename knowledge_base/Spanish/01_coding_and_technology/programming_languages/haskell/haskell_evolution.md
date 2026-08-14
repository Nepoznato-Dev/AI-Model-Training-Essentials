<!--
---
# Metadata
title: "Haskell — Version History & Evolution"
description: "Comprehensive version history and evolution of Haskell from Haskell 1.0 to modern Haskell."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [haskell, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Haskell - Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| Haskel 1.0 | 1990 | Publicación inicial (esfuerzo del comité) |
| Haskel 1.2 | 1992 | Experimentos con sistemas de objetos |
| Haskel 1.3 | 1996 | Clases de tipos introducidas |
| Haskel 1.4 | 1997 | `IO`mónada aclarada |
| Haskel 98 | 1998 | **Primer estándar estable** |
| Haskel 2010 | 2010 | **Estándar revisado**, Cabal, módulos |
| GHC 7.0 | 2011 | Familias de tipos, tipos de datos |
| GHC 7.4 | 2012 | Comienza la propuesta Applicative-Monad |
| GHC 7.6 | 2013 | Mejoras en familias tipográficas |
| GHC 7.8 | 2014 | Sinónimos de patrón,`NegativeLiterals`|
| GHC 7.10 | 2015 | **Propuesta de mónada aplicativa (AMP)**,`-XStrict`|
| GHC 8.0 | 2016 | **TypeApplications**, `MonadFail`, errores de tipo personalizados |
| GHC 8.2 | 2017 | Sumas sin caja, mochila (sistema de módulos) |
| GHC 8.4 | 2018 | Ruta base abstracta,`Semigroup`>>`Monoid`|
| GHC 8.6 | 2018 | StarIsType,`DerivingVia`|
| GHC 8.8 | 2019 | MonadFail en Preludio |
| GHC 8.10 | 2020 | Notación unificada `do`, polimorfismo de tipo |
| GHC 9.0 | 2021 | **Polimorfismo de levedad**, tipos lineales |
| GHC 9.2 | 2022 |`do`calificado, mensajes de error mejorados |
| GHC 9.4 | 2022 | **GHC2021** conjunto de extensiones de idioma,`OverloadedRecordDot`|
| GHC 9.6 | 2023 | Argumentos de tipo obligatorios,`TypeAbstractions`|
| GHC 9.8 | 2024 | `TypeAbstractions`estable, mensajes de error mejorados |
| GHC 9.10 | 2024 | Otras mejoras, rendimiento |
| GHC 9.12 | 2025 | Desarrollo continuo |
## Hitos importantes
### Haskell 1.x — Los años del comité (1990–1998)
- **1990**: Haskell 1.0: lenguaje funcional perezoso diseñado por un comité
- **1.3 (1996)**: Clases de tipos: la característica definitoria de Haskell
- **1.4 (1997)**: Se aclara la mónada `IO`: cómo manejar los efectos secundarios puramente
- **Haskell 98**: primer estándar estable; todavía referenciado hoy
### Haskell 2010: el estándar moderno
- **2010**: Estándar revisado: Cabal (sistema de paquetes), mejoras en el sistema de módulos
- GHC se convierte en el compilador de facto
- Cabal + Hackage = ecosistema de paquetes de Haskell
### GHC 7.x: tipo de alimentación del sistema (2011-2015)
- Familias de tipos, tipos de datos, polimorfismo de tipos.
- Propuesta Applicative-Monad (AMP): arreglando la jerarquía de clases de tipos
- Sinónimos de patrón, extensión `Strict`
### GHC 8.x: Haskell moderno (2016-2020)
- `TypeApplications`: argumentos de tipo explícito en sitios de llamadas
- Errores de tipo personalizado: mejores mensajes del compilador
- Mochila: sistema de módulos para diseño basado en componentes
-`DerivingVia`— estrategias de derivación flexibles
### GHC 9.x: revolución de la usabilidad (2021-presente)
- **9.0**: Polimorfismo de levedad, tipos lineales (seguridad de recursos)
- **9.2**:`do`calificado, mensajes de error mejorados
- **9.4**: **GHC2021**: extensiones predeterminadas modernas; `OverloadedRecordDot`(acceso al campo con `.`)
- **9.6**: argumentos de tipo obligatorios,`TypeAbstractions`
- **9.8–9.12**: Mejoras continuas en los mensajes de error y el rendimiento.
## Evolución de la sintaxis
```haskell
-- Haskell 98: Basic type classes
class Eq a where
  (==) :: a -> a -> Bool

-- GHC extensions: Type applications (GHC 8.0)
-- Before:
read "[1,2,3]" :: [Int]
-- After:
read @[Int] "[1,2,3]"

-- GHC 9.4: OverloadedRecordDot
-- Before:
name (getPerson user)
-- After:
user.person.name

-- GHC 9.0: Linear types
-- Before:
processFile :: FilePath -> IO Result
-- After:
processFile :: FilePath %1 -> IO Result  -- file handle used exactly once

-- GHC 8.0: Custom type errors
type family ErrorMessage (a :: Type) :: ErrorMessage where
  ErrorMessage (NotSerializable a) =
    'Text "Cannot serialize type " ':<>: 'ShowType a
```

## Evolución del sistema tipo
```
Haskell 1.0:  Basic types, algebraic data types, pattern matching
Haskell 1.3:  Type classes
Haskell 98:   Multi-parameter type classes, functional dependencies
GHC 6.x:     GADTs, type families, rank-N types
GHC 7.0:     Data kinds, kind polymorphism
GHC 7.10:    Applicative-Monad Proposal
GHC 8.0:     TypeApplications, custom type errors
GHC 8.2:     Unboxed sums
GHC 9.0:     Levity polymorphism, linear types
GHC 9.4:     OverloadedRecordDot, GHC2021
GHC 9.6:     Required type arguments, TypeAbstractions
```

## Concurrencia y paralelismo
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## Principios clave de diseño
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## Crecimiento del ecosistema
```
1990: Haskell 1.0 — academic curiosity
1998: Haskell 98 — stable standard
2007: Cabal + Hackage — package ecosystem
2010: Haskell 2010 — revised standard
2012: Stack build tool — reproducible builds
2015: Haskell in industry — Facebook, Standard Chartered, Well-Typed
2021: GHC 9.0 — levity polymorphism, linear types
2023: GHC 9.6 — type abstractions
2025: Haskell used in finance, compilers, formal verification,
       blockchain (Cardano), and academic research
       GHC, Stack, Cabal; key libraries: lens, aeson, servant, yesod
```
