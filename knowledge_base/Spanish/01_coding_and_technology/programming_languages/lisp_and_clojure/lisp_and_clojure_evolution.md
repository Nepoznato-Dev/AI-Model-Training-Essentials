---
# Metadata
title: "Lisp & Clojure — Version History & Evolution"
description: "Comprehensive version history and evolution of Lisp from 1958 to modern Clojure."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [lisp, clojure, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Lisp y Clojure: historial de versiones y evolución
## Línea de tiempo Lisp
| Versión | Año | Tema clave |
|---------|------|-----------|
| Ceceo 1.5 | 1962 | **Lisp implementado por primera vez** (John McCarthy, MIT) |
| maclisp | Década de 1960 | Lisp de la computadora central del MIT |
| Interlisp | 1967 | Xerox PARC: edición estructurada |
| Esquema | 1975 | **Lisp minimalista** (Sussman & Steele, MIT) |
| Ceceo común | 1984 | **Lisp estandarizado** (Guy Steele, ANSI 1994) |
| Emacs Lisp | 1985 | Lisp para el editor de Emacs |
| Esquema R5RS | 1998 | Informe revisado⁵: estándar del esquema ampliamente adoptado |
| Esquema R6RS | 2007 | Sistema de módulos, Unicode |
| Esquema R7RS | 2013 | Idioma pequeño (R7RS-pequeño) |
| Clojure | 2007 | **Lisp moderno en la JVM** (Rich Hickey) |
| Clojure 1.0 | 2009 | Primera versión estable |
| Clojure 1.3 | 2011 | Protocolos,`defrecord`|
| Clojure 1.4 | 2012 | Condicionales del lector |
| Clojure 1.5 | 2013 | Transductores (posteriormente) |
| Clojure 1.7 | 2015 | **Transductores**, condicionales del lector |
| Clojure 1.8 | 2016 | `spec`(validación de datos),`clojure.spec`|
| Clojure 1.9 | 2017 | **`spec`estable**, mensajes de error mejorados |
| Clojure 1.10 | 2018 | Mejores mensajes de error,`clj`CLI |
| Clojure 1.11 | 2022 |  `update-keys`, `update-vals`,`abs`|
| Clojure 1.12 | 2024 | **Mejoras de interoperabilidad de Java**,`definterface`|
## Hitos importantes
### Ceceo temprano (1958-1970)
- **1958**: John McCarthy crea Lisp en el MIT: "Procesamiento de listas"
- **1962**: Lisp 1.5 — primera versión implementada
- Innovaciones clave: **recolección de basura**, **recursión**, **homoiconicidad** (código = datos)
-`eval`— la función universal
- `cond`,`car`/ `cdr`, `cons`, lambda
### Esquema (1975-presente)
- **1975**: Guy Steele y Gerald Sussman crean Scheme en el MIT
- **Filosofía**: Minimalista: núcleo pequeño, abstracciones poderosas
- Alcance léxico (antes que la mayoría de los idiomas)
- Continuaciones de primera clase.
- Macros higiénicas
- Optimización de llamadas de cola (obligatorio)
### Lisp común (1984-presente)
- **1984**: Guy Steele publica "Common Lisp the Language"
- **1994**: Estándar ANSI Common Lisp (ANSI X3.226)
- **El Lisp "fregadero de la cocina"**: enorme biblioteca estándar
- CLOS (Common Lisp Object System): programación orientada a objetos más potente
- Sistema de condición: errores reiniciables
- Macro de bucle: potente iteración DSL
### Clojure (2007-presente)
- **2007**: Rich Hickey crea Clojure — Lisp para JVM
- **Filosofía**: Práctica, concurrente, inmutable
- Estructuras de datos persistentes e inmutables.
- STM (Memoria Transaccional de Software)
-`core.async`(simultaneidad estilo CSP)
- Interoperabilidad perfecta de Java
- Desarrollo impulsado por REPL
## Evolución de la sintaxis
```lisp
;; Lisp 1.5 (1962): The essentials
(defun factorial (n)
  (cond ((= n 0) 1)
        (t (* n (factorial (- n 1))))))

;; Scheme (1975): Minimalist, lexical scoping
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

;; Common Lisp (1984): CLOS, condition system
(defclass shape ()
  ((x :initarg :x :accessor shape-x)
   (y :initarg :y :accessor shape-y)))

(defclass circle (shape)
  ((radius :initarg :radius :accessor circle-radius)))

(defgeneric area (shape))

(defmethod area ((c circle))
  (* pi (expt (circle-radius c) 2)))

;; Clojure (2007): Modern, immutable, JVM
(defn factorial [n]
  (reduce * (range 1 (inc n))))

;; Clojure: Persistent data structures
(def m {:name "Alice" :age 30})
(def m2 (assoc m :email "alice@example.com"))  ; original unchanged

;; Clojure: Transducers (1.7)
(def xf (comp (filter even?) (map #(* % %))))
(transduce xf + 0 (range 10))

;; Clojure: spec (1.8+)
(require '[clojure.spec.alpha :as s])
(s/def ::name string?)
(s/def ::age (s/and int? #(<= 0 % 150)))
(s/def ::person (s/keys :req [::name ::age]))

;; Clojure: core.async (channels)
(require '[clojure.core.async :refer [go chan >! <!]])
(go (let [c (chan)]
      (>! c "hello")
      (println (<! c))))
```

## Evolución de funciones
```
Lisp 1.5 (1962):  car/cdr/cons, eval, cond, lambda
Scheme (1975):    Lexical scoping, continuations, hygienic macros, TCO
Common Lisp (1984): CLOS, conditions, loop, defstruct, defmacro
Clojure (2007):   Persistent data structures, STM, Java interop
Clojure 1.7 (2015): Transducers, reader conditionals
Clojure 1.8 (2016): spec (data validation)
Clojure 1.9 (2017): spec stable, improved errors
Clojure 1.11 (2022): update-keys, update-vals
Clojure 1.12 (2024): Java interop improvements
```

## Principios clave de diseño
```
Lisp (general):
1. "Code is data" — homoiconicity (programs are lists)
2. "Macros" — extend the language itself
3. "REPL-driven" — interactive development
4. "Functional" — functions are first-class

Clojure-specific:
5. "Immutable by default" — persistent data structures
6. "Concurrency" — STM, atoms, agents, core.async
7. "Practical" — Java interop, real-world libraries
8. "Simple" — few concepts, compose freely
```

## Crecimiento del ecosistema
```
1958: Lisp created by John McCarthy at MIT
1962: Lisp 1.5 — first implementation
1975: Scheme — minimalist Lisp
1984: Common Lisp — standardized, comprehensive
1994: ANSI Common Lisp standard
2007: Clojure — Lisp on the JVM
2009: Clojure 1.0 — stable release
2015: Clojure 1.7 — transducers
2016: Clojure 1.8 — spec
2024: Clojure 1.12 — Java interop
2025: Lisp family powers:
       - Emacs (Emacs Lisp)
       - Racket (modern Scheme)
       - Clojure (web, data, concurrent systems)
       - Arc, Hy, Janet (Lisp dialects)
       Used by: NASA (JPL), Amazon, Apple, Nubank, CircleCI
```
