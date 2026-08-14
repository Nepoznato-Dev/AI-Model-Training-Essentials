<!--
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

-->
# Lisp at Clojure — Kasaysayan ng Bersyon at Ebolusyon
## Lisp Timeline
| Bersyon | Taon | Pangunahing Tema |
|---------|------|-----------|
| Lisp 1.5 | 1962 | **Unang ipinatupad Lisp** (John McCarthy, MIT) |
| Maclisp | 1960s | MIT mainframe Lisp |
| Interlisp | 1967 | Xerox PARC — structured editing |
| Scheme | 1975 | **Minimalist Lisp** (Sussman & Steele, MIT) |
| Karaniwang Lisp | 1984 | **Standardized Lisp** (Guy Steele, ANSI 1994) |
| Emacs Lisp | 1985 | Lisp para sa Emacs editor |
| Scheme R5RS | 1998 | Revised⁵ Report — malawakang pinagtibay na pamantayan ng Scheme |
| Scheme R6RS | 2007 | Sistema ng module, Unicode |
| Scheme R7RS | 2013 | Maliit na wika (R7RS-maliit) |
| Clojure | 2007 | **Modern Lisp on the JVM** (Rich Hickey) |
| Clojure 1.0 | 2009 | Unang matatag na release |
| Clojure 1.3 | 2011 | Mga Protocol,`defrecord`|
| Clojure 1.4 | 2012 | Mga kondisyon ng mambabasa |
| Clojure 1.5 | 2013 | Mga Transduser (mamaya) |
| Clojure 1.7 | 2015 | **Transducers**, reader conditional |
| Clojure 1.8 | 2016 | `spec`(pagpatunay ng data),`clojure.spec`|
| Clojure 1.9 | 2017 | **`spec`stable**, pinahusay na mga mensahe ng error |
| Clojure 1.10 | 2018 | Mas mahusay na mga mensahe ng error,`clj`CLI |
| Clojure 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Clojure 1.12 | 2024 | **Java interop improvements**,`definterface`|
## Mga Pangunahing Milestone
### Maagang Lisp (1958–1970s)
- **1958**: Si John McCarthy ay lumikha ng Lisp sa MIT — "List Processing"
- **1962**: Lisp 1.5 — unang ipinatupad na bersyon
- Mga pangunahing inobasyon: **pagkolekta ng basura**, **recursion**, **homoiconicity** (code = data)
-`eval`— ang unibersal na function
-`cond`,`car`/`cdr`,`cons`, lambda
### Scheme (1975–kasalukuyan)
- **1975**: Gumawa sina Guy Steele at Gerald Sussman ng Scheme sa MIT
- **Pilosopiya**: Minimalist — maliit na core, makapangyarihang abstraction
- Lexical scoping (bago ang karamihan sa mga wika)
- Mga pagpapatuloy ng unang klase
- Mga macro sa kalinisan
- Pag-optimize ng tail-call (mandatory)
### Karaniwang Lisp (1984–kasalukuyan)
- **1984**: Inilathala ni Guy Steele ang "Common Lisp the Language"
- **1994**: ANSI Common Lisp standard (ANSI X3.226)
- **Ang "kitchen sink" Lisp** — napakalaking karaniwang library
- CLOS (Common Lisp Object System) — pinakamakapangyarihang OOP
- Sistema ng kundisyon — mga error na mai-restart
- Loop macro — malakas na pag-ulit ng DSL
### Clojure (2007–kasalukuyan)
- **2007**: Gumawa si Rich Hickey ng Clojure — Lisp para sa JVM
- **Pilosopiya**: Praktikal, kasabay, hindi nababago
- Paulit-ulit na hindi nababagong istruktura ng data
- STM (Software Transactional Memory)
-`core.async`(CSP-style concurrency)
- Seamless Java interop
- Pag-unlad na hinihimok ng REPL
## Syntax Evolution
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

## Ebolusyon ng Tampok
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

## Pangunahing Prinsipyo ng Disenyo
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

## Paglago ng Ecosystem
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
