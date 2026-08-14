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

# Lisp & Clojure — Historique et évolution des versions
## Chronologie Lisp
| Version | Année | Thème clé |
|---------|------|-----------|
| Lisp1.5 | 1962 | **Premier Lisp implémenté** (John McCarthy, MIT) |
| Maclisp | années 1960 | Lisp sur ordinateur central du MIT |
| Interlisp | 1967 | Xerox PARC — édition structurée |
| Schéma | 1975 | **Lisp minimaliste** (Sussman & Steele, MIT) |
| Lisp commun | 1984 | **Lisp standardisé** (Guy Steele, ANSI 1994) |
| Emacs Lisp | 1985 | Lisp pour l'éditeur Emacs |
| Schéma R5RS | 1998 | Rapport révisé⁵ — Norme du système largement adoptée |
| Schéma R6RS | 2007 | Système de modules, Unicode |
| Schéma R7RS | 2013 | Petit langage (R7RS-small) |
| Clojure | 2007 | **Modern Lisp sur la JVM** (Rich Hickey) |
| Clojure 1.0 | 2009 | Première version stable |
| Clojure 1.3 | 2011 | Protocoles,`defrecord`|
| Clojure 1.4 | 2012 | Conditions du lecteur |
| Clojure 1.5 | 2013 | Transducteurs (plus tard) |
| Clojure 1.7 | 2015 | **Transducteurs**, conditions du lecteur |
| Clojure 1.8 | 2016 | `spec`(validation des données),`clojure.spec`|
| Clojure 1.9 | 2017 | **`spec`stable**, messages d'erreur améliorés |
| Clojure 1.10 | 2018 | De meilleurs messages d'erreur,`clj`CLI |
| Clojure 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Clojure 1.12 | 2024 | **Améliorations de l'interopérabilité Java**,`definterface`|
## Étapes majeures
### Premier Lisp (1958-1970)
- **1958** : John McCarthy crée Lisp au MIT — "List Processing"
- **1962** : Lisp 1.5 — première version implémentée
- Innovations clés : **garbage collection**, **récursion**, **homoïconicité** (code = data)
-`eval`— la fonction universelle
-`cond`,`car`/`cdr`,`cons`, lambda
### Programme (depuis 1975)
- **1975** : Guy Steele et Gerald Sussman créent Scheme au MIT
- **Philosophie** : Minimaliste — petit noyau, abstractions puissantes
- Cadrage lexical (avant la plupart des langues)
- Suite de première classe
- Macros hygiéniques
- Optimisation des appels de queue (obligatoire)
### Common Lisp (depuis 1984)
- **1984** : Guy Steele publie "Common Lisp the Language"
- **1994** : norme ANSI Common Lisp (ANSI X3.226)
- **L'« évier de cuisine » Lisp** — bibliothèque standard massive
- CLOS (Common Lisp Object System) — POO la plus puissante
- Système de condition - erreurs redémarrables
- Macro de boucle - itération DSL puissante
### Clojure (2007-présent)
- **2007** : Rich Hickey crée Clojure — Lisp pour la JVM
- **Philosophie** : Pratique, concurrente, immuable
- Structures de données persistantes et immuables
- STM (Mémoire Transactionnelle Logicielle)
-`core.async`(concurrence de style CSP)
- Interopérabilité Java transparente
- Développement piloté par REPL
## Évolution de la syntaxe
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

## Évolution des fonctionnalités
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

## Principes de conception clés
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

## Croissance de l'écosystème
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
