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
# Lisp и Clojure — история версий и эволюция
## Временная шкала Лиспа
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| Лисп 1.5 | 1962 | **Впервые реализовал Lisp** (Джон Маккарти, Массачусетский технологический институт) |
| Маклисп | 1960-е годы | Мейнфрейм MIT Lisp |
| Интерлисп | 1967 | Xerox PARC — структурированное редактирование |
| Схема | 1975 | **Минималистский Лисп** (Сассман и Стил, Массачусетский технологический институт) |
| Общий Лисп | 1984 | **Стандартизированный Лисп** (Гай Стил, ANSI 1994) |
| Эмакс Лисп | 1985 | Редактор Lisp для Emacs |
| Схема R5RS | 1998 | Пересмотренный⁵ Отчет — широко распространенный стандарт схемы |
| Схема R6RS | 2007 | Система модулей, Юникод |
| Схема R7RS | 2013 | Малый язык (R7RS-маленький) |
| Кложур | 2007 | **Современный Lisp на JVM** (Рич Хикки) |
| Кложур 1.0 | 2009 | Первый стабильный выпуск |
| Клююр 1.3 | 2011 | Протоколы,`defrecord`|
| Кложур 1.4 | 2012 | Читательские условные обозначения |
| Кложур 1.5 | 2013 | Датчики (позже) |
| Клююр 1.7 | 2015 | **Преобразователи**, условные обозначения считывания |
| Кложур 1.8 | 2016 | `spec`(проверка данных),`clojure.spec`|
| Кложур 1.9 | 2017 | **`spec`стабильна**, улучшены сообщения об ошибках |
| Кложур 1.10 | 2018 | Улучшенные сообщения об ошибках,`clj`CLI |
| Клююр 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Кложур 1.12 | 2024 | **Улучшения взаимодействия с Java**,`definterface`|
## Основные вехи
### Ранний Лисп (1958–1970-е)
- **1958**: Джон Маккарти создает Lisp в Массачусетском технологическом институте — «Обработка списков».
- **1962**: Lisp 1.5 — первая реализованная версия.
- Ключевые нововведения: **сборка мусора**, **рекурсия**, **гомоиконичность** (код = данные).
-`eval`— универсальная функция.
- `cond`,`car`/ `cdr`, `cons`, лямбда
### Схема (1975 – настоящее время)
- **1975**: Гай Стил и Джеральд Сассман создают Scheme в Массачусетском технологическом институте.
- **Философия**: Минимализм — маленькое ядро, мощные абстракции.
- Лексическая область видимости (до большинства языков)
- Первоклассные продолжения
- Гигиенические макросы
- Оптимизация хвостового вызова (обязательно)
### Common Lisp (1984 – настоящее время)
- **1984**: Гай Стил публикует книгу «Язык Common Lisp».
- **1994**: стандарт ANSI Common Lisp (ANSI X3.226).
- **"Кухонная раковина" Lisp** — огромная стандартная библиотека.
- CLOS (Common Lisp Object System) — самое мощное ООП.
- Система состояний — перезапускаемые ошибки
- Макрос цикла — мощный итерационный DSL.
### Clojure (2007 – настоящее время)
- **2007**: Рич Хики создает Clojure — Lisp для JVM.
- **Философия**: практичная, параллельная, неизменная.
- Постоянные неизменяемые структуры данных
- STM (программная транзакционная память)
-`core.async`(параллелизм в стиле CSP)
- Бесшовное взаимодействие с Java
- Разработка на основе REPL
## Эволюция синтаксиса
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

## Эволюция функций
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

## Ключевые принципы проектирования
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

## Рост экосистемы
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
