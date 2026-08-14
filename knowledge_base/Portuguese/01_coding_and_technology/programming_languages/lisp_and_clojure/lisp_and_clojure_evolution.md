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
# Lisp & Clojure – Histórico de versões e evolução
## Linha do tempo Lisp
| Versão | Ano | Tema principal |
|--------|------|-----------|
| Lisp 1.5 | 1962 | **Lisp implementado pela primeira vez** (John McCarthy, MIT) |
| Maclisp | Década de 1960 | Lisp de mainframe do MIT |
| Interlisp | 1967 | Xerox PARC — edição estruturada |
| Esquema | 1975 | **Lisp minimalista** (Sussman & Steele, MIT) |
| Lisp comum | 1984 | **Lisp padronizado** (Guy Steele, ANSI 1994) |
| Emacs Lisp | 1985 | Lisp para editor Emacs |
| Esquema R5RS | 1998 | Relatório⁵ Revisado — Padrão de Esquema amplamente adotado |
| Esquema R6RS | 2007 | Sistema de módulos, Unicode |
| Esquema R7RS | 2013 | Linguagem pequena (R7RS-pequena) |
| Clojure | 2007 | **Lisp moderno na JVM** (Rich Hickey) |
| Clojure 1.0 | 2009 | Primeira versão estável |
| Clojure 1.3 | 2011 | Protocolos,`defrecord`|
| Clojure 1.4 | 2012 | Condicionais do leitor |
| Clojure 1.5 | 2013 | Transdutores (mais tarde) |
| Clojure 1.7 | 2015 | **Transdutores**, condicionais de leitura |
| Clojure 1.8 | 2016 | `spec`(validação de dados),`clojure.spec`|
| Clojure 1.9 | 2017 | **`spec`estável**, mensagens de erro aprimoradas |
| Clojure 1.10 | 2018 | Melhores mensagens de erro,`clj`CLI |
| Clojure 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Clojure 1.12 | 2024 | **Melhorias na interoperabilidade Java**,`definterface`|
## Marcos importantes
### Early Lisp (1958–1970)
- **1958**: John McCarthy cria Lisp no MIT — "List Processing"
- **1962**: Lisp 1.5 — primeira versão implementada
- Principais inovações: **coleta de lixo**, **recursão**, **homoiconicidade** (código = dados)
-`eval`— a função universal
- `cond`,`car`/ `cdr`, `cons`, lambda
### Esquema (1975-presente)
- **1975**: Guy Steele e Gerald Sussman criam Scheme no MIT
- **Filosofia**: Minimalista — núcleo pequeno, abstrações poderosas
- Escopo lexical (antes da maioria dos idiomas)
- Continuações de primeira classe
- Macros higiênicas
- Otimização da chamada final (obrigatório)
### Common Lisp (1984-presente)
- **1984**: Guy Steele publica "Common Lisp the Language"
- **1994**: padrão ANSI Common Lisp (ANSI X3.226)
- **O Lisp da "pia da cozinha"** — enorme biblioteca padrão
- CLOS (Common Lisp Object System) — OOP mais poderoso
- Sistema de condição – erros reinicializáveis
- Macro de loop – DSL de iteração poderosa
### Clojure (2007-presente)
- **2007**: Rich Hickey cria Clojure — Lisp para JVM
- **Filosofia**: Prático, simultâneo, imutável
- Estruturas de dados imutáveis ​​persistentes
- STM (memória transacional de software)
-`core.async`(simultaneidade estilo CSP)
- Interoperabilidade Java perfeita
- Desenvolvimento orientado por REPL
## Evolução da Sintaxe
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

## Evolução de recursos
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

## Princípios-chave de design
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

## Crescimento do Ecossistema
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
