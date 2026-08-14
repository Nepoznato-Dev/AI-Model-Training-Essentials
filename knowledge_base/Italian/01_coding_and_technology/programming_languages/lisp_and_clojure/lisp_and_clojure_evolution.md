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
# Lisp & Clojure: storia ed evoluzione delle versioni
## Cronologia Lisp
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| Lisp 1.5 | 1962 | **Prima implementazione del Lisp** (John McCarthy, MIT) |
| Maclip | Anni '60 | Mainframe del MIT Lisp |
| Interlisp | 1967 | Xerox PARC: editing strutturato |
| Schema | 1975 | **Lisp minimalista** (Sussman & Steele, MIT) |
| Lisp comune | 1984 | **Lisp standardizzato** (Guy Steele, ANSI 1994) |
| EmacsLisp | 1985 | Lisp per l'editor Emacs |
| Schema R5RS | 1998 | Rapporto rivisto⁵: standard di sistema ampiamente adottato |
| Schema R6RS | 2007| Sistema modulare, Unicode |
| Schema R7RS | 2013| Lingua piccola (R7RS-piccolo) |
| Clojure | 2007| **Lisp moderno sulla JVM** (Rich Hickey) |
| Clojure 1.0 | 2009| Prima versione stabile |
| Clojure 1.3 | 2011 | Protocolli,`defrecord`|
| Clojure 1.4 | 2012| Condizionali del lettore |
| Clojure 1.5 | 2013| Trasduttori (più tardi) |
| Clojure 1.7 | 2015| **Trasduttori**, condizionali del lettore |
| Clojure 1.8 | 2016| `spec`(convalida dati),`clojure.spec`|
| Clojure 1.9 | 2017 | **`spec`stabile**, messaggi di errore migliorati |
| Clojure 1.10 | 2018 | Messaggi di errore migliorati,`clj`CLI |
| Clojure 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Clojure 1.12 | 2024 | **Miglioramenti dell'interoperabilità Java**,`definterface`|
## Traguardi importanti
### Primo Lisp (1958-1970)
- **1958**: John McCarthy crea Lisp al MIT — "List Processing"
- **1962**: Lisp 1.5 — prima versione implementata
- Innovazioni chiave: **garbage collection**, **ricorsione**, **omoiconicità** (codice = dati)
-`eval`— la funzione universale
-`cond`,`car`/ `cdr`, `cons`, lambda
### Schema (1975-oggi)
- **1975**: Guy Steele e Gerald Sussman creano Scheme al MIT
- **Filosofia**: minimalista: nucleo piccolo, astrazioni potenti
- Scoping lessicale (prima della maggior parte delle lingue)
- Continuazioni di prima classe
- Macro igieniche
- Ottimizzazione delle chiamate in coda (obbligatorio)
### Lisp comune (1984-oggi)
- **1984**: Guy Steele pubblica "Common Lisp the Language"
- **1994**: standard ANSI Common Lisp (ANSI X3.226)
- **Il Lisp del "lavello della cucina"**: un'enorme libreria standard
- CLOS (Common Lisp Object System): l'OOP più potente
- Sistema di condizioni: errori riavviabili
- Macro loop: potente iterazione DSL
### Clojure (2007-oggi)
- **2007**: Rich Hickey crea Clojure — Lisp per JVM
- **Filosofia**: Pratica, concorrente, immutabile
- Strutture dati persistenti e immutabili
- STM (Memoria Transazionale Software)
-`core.async`(concorrenza in stile CSP)
- Interoperabilità Java senza soluzione di continuità
- Sviluppo guidato da REPL
## Evoluzione della sintassi
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

## Evoluzione delle funzionalità
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

## Principi chiave di progettazione
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

## Crescita dell'ecosistema
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
