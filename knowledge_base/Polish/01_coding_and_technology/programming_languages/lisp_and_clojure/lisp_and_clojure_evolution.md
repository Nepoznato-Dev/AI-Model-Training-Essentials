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

# Lisp i Clojure — historia wersji i ewolucja
## Oś czasu Lispa
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| Lisp 1.5 | 1962 | **Po raz pierwszy wdrożono Lisp** (John McCarthy, MIT) |
| Maclisp | lata 60. | Lisp na komputerze mainframe MIT |
| Interlisp | 1967 | Xerox PARC — edycja strukturalna |
| Schemat | 1975 | **Minimalistyczny Lisp** (Sussman & Steele, MIT) |
| Wspólny Lisp | 1984 | **Standardowy Lisp** (Guy Steele, ANSI 1994) |
| Lisp Emacsa | 1985 | Lisp dla edytora Emacsa |
| Schemat R5RS | 1998 | Zmieniony⁵ Raport — powszechnie przyjęty standard programu |
| Schemat R6RS | 2007 | System modułowy, Unicode |
| Schemat R7RS | 2013 | Mały język (R7RS-mały) |
| Zamknięcie | 2007 | **Nowoczesny Lisp na JVM** (Rich Hickey) |
| Zamknięcie 1.0 | 2009 | Pierwsza stabilna wersja |
| Zamknięcie 1.3 | 2011 | Protokoły,`defrecord`|
| Zamknięcie 1.4 | 2012 | Warunki czytelnika |
| Zamknięcie 1.5 | 2013 | Przetworniki (później) |
| Zamknięcie 1.7 | 2015 | **Przetworniki**, warunki czytnika |
| Zamknięcie 1.8 | 2016 | `spec`(weryfikacja danych),`clojure.spec`|
| Zamknięcie 1.9 | 2017 | **`spec`stabilny**, ulepszone komunikaty o błędach |
| Zamknięcie 1.10 | 2018 | Lepsze komunikaty o błędach,`clj`CLI |
| Zamknięcie 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Zamknięcie 1.12 | 2024 | **Ulepszenia współdziałania Java**,`definterface`|
## Główne kamienie milowe
### Wczesny Lisp (1958–1970)
- **1958**: John McCarthy tworzy Lisp na MIT — „Przetwarzanie list”
- **1962**: Lisp 1.5 — pierwsza zaimplementowana wersja
- Kluczowe innowacje: **zbieranie śmieci**, **rekurencja**, **homoikoniczność** (kod = dane)
-`eval`— funkcja uniwersalna
-`cond`,`car`/`cdr`,`cons`, lambda
### Schemat (1975 – obecnie)
- **1975**: Guy Steele i Gerald Sussman tworzą program w MIT
- **Filozofia**: Minimalistyczna — mały rdzeń, potężne abstrakcje
- Zakres leksykalny (przed większością języków)
- Kontynuacje najwyższej klasy
- Higieniczne makra
- Optymalizacja połączeń końcowych (obowiązkowe)
### Lisp pospolity (1984 – obecnie)
- **1984**: Guy Steele publikuje „Common Lisp the Language”
- **1994**: Standard ANSI Common Lisp (ANSI X3.226)
- **Lisp „zlew kuchenny”** — ogromna biblioteka standardowa
- CLOS (Common Lisp Object System) — najpotężniejszy OOP
- System stanu — błędy możliwe do ponownego uruchomienia
- Makro pętli — potężna iteracja DSL
### Clojure (2007 – obecnie)
- **2007**: Rich Hickey tworzy Clojure — Lisp dla JVM
- **Filozofia**: Praktyczna, współbieżna, niezmienna
- Trwałe, niezmienne struktury danych
- STM (programowa pamięć transakcyjna)
-`core.async`(współbieżność w stylu CSP)
- Bezproblemowa współpraca z Java
- Rozwój oparty na REPL
## Ewolucja składni
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

## Ewolucja funkcji
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

## Kluczowe zasady projektowania
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

## Rozwój ekosystemu
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
