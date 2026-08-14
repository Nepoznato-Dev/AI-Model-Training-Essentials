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
# Lisp & Clojure - Historia ya Toleo & Mageuzi
## Lisp Timeline
| Toleo | Mwaka | Mandhari Muhimu |
|---------|------|-----------|
| Lisp 1.5 | 1962 | ** Lisp iliyotekelezwa kwa mara ya kwanza** (John McCarthy, MIT) |
| Maclisp | Miaka ya 1960 | Jina kuu la MIT Lisp |
| Interlisp | 1967 | Xerox PARC - uhariri wa muundo |
| Mpango | 1975 | **Minimalist Lisp** (Sussman & Steele, MIT) |
| Lisp ya Kawaida | 1984 | **Lisp Sanifu** (Guy Steele, ANSI 1994) |
| Emacs Lisp | 1985 | Lisp kwa kihariri cha Emacs |
| Mpango R5RS | 1998 | Ripoti Iliyorekebishwa - kiwango cha Mpango kilichopitishwa na wengi |
| Mpango R6RS | 2007 | Mfumo wa moduli, Unicode |
| Mpango R7RS | 2013 | Lugha ndogo (R7RS-ndogo) |
| Cloju | 2007 | **Modern Lisp kwenye JVM** (Rich Hickey) |
| Clojure 1.0 | 2009 | Toleo la kwanza thabiti |
| Clojure 1.3 | 2011 | Itifaki,`defrecord`|
| Clojure 1.4 | 2012 | Masharti ya msomaji |
| Clojure 1.5 | 2013 | Transducers (baadaye) |
| Clojure 1.7 | 2015 | **Transducers**, masharti ya msomaji |
| Clojure 1.8 | 2016 | `spec`(uthibitishaji wa data),`clojure.spec`|
| Clojure 1.9 | 2017 | **`spec`thabiti**, ujumbe wa makosa ulioboreshwa |
| Clojure 1.10 | 2018 | Ujumbe bora wa makosa,`clj`CLI |
| Clojure 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Clojure 1.12 | 2024 | **Maboresho ya mwingiliano wa Java**,`definterface`|
## Mafanikio Makuu
### Early Lisp (1958–1970s)
- **1958**: John McCarthy anaunda Lisp huko MIT - "Utayarishaji wa Orodha"
- **1962**: Lisp 1.5 - toleo la kwanza lililotekelezwa
- Ubunifu muhimu: ** ukusanyaji wa takataka **, ** recursion **, ** homoiconicity ** (code = data)
-`eval`- kazi ya ulimwengu wote
-`cond`,`car`/`cdr`,`cons`, lambda
### Mpango (1975-sasa)
- **1975**: Guy Steele na Gerald Sussman huunda Mpango huko MIT
- **Falsafa**: Minimalist - msingi mdogo, vifupisho vyenye nguvu
- Upeo wa Lexical (kabla ya lugha nyingi)
- Muendelezo wa daraja la kwanza
- macros ya usafi
- Uboreshaji wa simu ya mkia (lazima)
### Common Lisp (1984–sasa)
- **1984**: Guy Steele anachapisha "Common Lisp the Language"
- **1994**: ANSI Kawaida Lisp kiwango (ANSI X3.226)
- ** "Sinki la jikoni" Lisp ** - maktaba kubwa ya kawaida
- CLOS (Mfumo wa Kawaida wa Kitu cha Lisp) - OOP yenye nguvu zaidi
- Mfumo wa hali - makosa yanayoweza kuanzishwa tena
- Loop macro - DSL yenye nguvu ya kurudia
### Clojure (2007–sasa)
- **2007**: Rich Hickey aunda Clojure - Lisp kwa JVM
- **Falsafa**: Kitendo, sambamba, kisichobadilika
- Miundo ya data isiyobadilika inayoendelea
STM (Kumbukumbu ya Muamala ya Programu)
`core.async` (sarafu ya mtindo wa CSP)
- Uingiliano wa Java usio na mshono
- Maendeleo yanayoendeshwa na REPL
## Mageuzi ya Sintaksia
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

## Mageuzi ya Kipengele
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

## Kanuni Muhimu za Usanifu
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

## Ukuaji wa Mfumo ikolojia
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
