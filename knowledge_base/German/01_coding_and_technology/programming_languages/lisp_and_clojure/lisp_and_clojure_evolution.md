---
# Metadata
title: "Lisp & Clojure — Version History & Evolution"
description: "Comprehensive version history and evolution of Lisp from 1958 to modern Clojure."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# Lisp & Clojure – Versionsgeschichte und Entwicklung
## Lisp-Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| Lisp 1,5 | 1962 | **Erstes implementiertes Lisp** (John McCarthy, MIT) |
| Maclisp | 1960er Jahre | MIT-Mainframe Lisp |
| Interlisp | 1967 | Xerox PARC – Strukturierte Bearbeitung |
| Schema | 1975 | **Minimalistisches Lisp** (Sussman & Steele, MIT) |
| Gemeinsames Lispeln | 1984 | **Standardisiertes Lisp** (Guy Steele, ANSI 1994) |
| Emacs Lisp | 1985 | Lisp für Emacs-Editor |
| Schema R5RS | 1998 | Überarbeiteter⁵ Bericht – weit verbreiteter Scheme-Standard |
| Schema R6RS | 2007 | Modulsystem, Unicode |
| Schema R7RS | 2013 | Kleine Sprache (R7RS-klein) |
| Clojure | 2007 | **Modernes Lisp auf der JVM** (Rich Hickey) |
| Clojure 1.0 | 2009 | Erste stabile Veröffentlichung |
| Clojure 1.3 | 2011 | Protokolle,`defrecord`|
| Clojure 1.4 | 2012 | Leserbedingungen |
| Clojure 1,5 | 2013 | Wandler (später) |
| Clojure 1.7 | 2015 | **Wandler**, Leserbedingungen |
| Clojure 1.8 | 2016 | `spec`(Datenvalidierung),`clojure.spec`|
| Clojure 1.9 | 2017 | **`spec`stabil**, verbesserte Fehlermeldungen |
| Clojure 1.10 | 2018 | Bessere Fehlermeldungen,`clj`CLI |
| Clojure 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Clojure 1.12 | 2024 | **Java-Interop-Verbesserungen**,`definterface`|
## Wichtige Meilensteine
### Frühes Lisp (1958–1970er Jahre)
- **1958**: John McCarthy erstellt Lisp am MIT – „List Processing“
- **1962**: Lisp 1.5 – erste implementierte Version
- Schlüsselinnovationen: **Garbage Collection**, **Rekursion**, **Homoikonizität** (Code = Daten)
-`eval`– die universelle Funktion
- `cond`,`car`/ `cdr`, `cons`, Lambda
###-Schema (1975–heute)
- **1975**: Guy Steele und Gerald Sussman gründen Scheme am MIT
- **Philosophie**: Minimalistisch – kleiner Kern, kraftvolle Abstraktionen
- Lexikalisches Scoping (vor den meisten Sprachen)
- Erstklassige Fortsetzungen
- Hygienische Makros
- Tail-Call-Optimierung (obligatorisch)
### Gemeinsames Lispeln (1984–heute)
- **1984**: Guy Steele veröffentlicht „Common Lisp the Language“
- **1994**: ANSI Common Lisp-Standard (ANSI X3.226)
- **Das „Küchenspülbecken“ Lisp** – riesige Standardbibliothek
- CLOS (Common Lisp Object System) – leistungsstärkstes OOP
- Bedingungssystem – neu startbare Fehler
- Schleifenmakro – leistungsstarkes Iterations-DSL
### Clojure (2007–heute)
- **2007**: Rich Hickey erstellt Clojure – Lisp für die JVM
- **Philosophie**: Praktisch, gleichzeitig, unveränderlich
- Persistente unveränderliche Datenstrukturen
- STM (Software-Transaktionsspeicher)
-`core.async`(Parallelität im CSP-Stil)
- Nahtlose Java-Interop
- REPL-gesteuerte Entwicklung
## Syntaxentwicklung
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

## Feature-Entwicklung
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

## Wichtige Designprinzipien
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

## Ökosystemwachstum
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
