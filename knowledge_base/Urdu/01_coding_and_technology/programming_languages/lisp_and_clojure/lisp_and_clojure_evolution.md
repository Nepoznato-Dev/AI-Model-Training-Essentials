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
# Lisp & Clojure - ورژن کی تاریخ اور ارتقاء
## لِسپ ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| لسپ 1.5 | 1962 | **پہلا نافذ کردہ Lisp** (جان میکارتھی، MIT) |
| میکلسپ | 1960 کی دہائی | MIT مین فریم Lisp |
| انٹرلیسپ | 1967 | زیروکس PARC - ساختی ترمیم |
| سکیم | 1975 | **Minimalist Lisp** (Sussman & Steele, MIT) |
| کامن لِسپ | 1984 | **معیاری لِسپ** (گائے اسٹیل، اے این ایس آئی 1994) |
| Emacs Lisp | 1985 | Emacs ایڈیٹر کے لیے Lisp |
| سکیم R5RS | 1998 | نظر ثانی شدہ⁵ رپورٹ — وسیع پیمانے پر اپنایا گیا اسکیم معیار |
| سکیم R6RS | 2007 | ماڈیول سسٹم، یونیکوڈ |
| سکیم R7RS | 2013 | چھوٹی زبان (R7RS-small) |
| Clojure | 2007 | **جدید لِسپ آن دی جے وی ایم** (رچ ہکی) |
| Clojure 1.0 | 2009 | پہلی مستحکم رہائی |
| کلوجور 1.3 | 2011 | پروٹوکول،`defrecord`|
| کلوجور 1.4 | 2012 | قارئین کی شرائط |
| کلوجور 1.5 | 2013 | Transducers (بعد میں) |
| کلوجور 1.7 | 2015 | **ٹرانسڈیوسرز**، ریڈر مشروط |
| کلوجور 1.8 | 2016 | `spec`(ڈیٹا کی توثیق)،`clojure.spec`|
| کلوجور 1.9 | 2017 | **`spec`مستحکم**، بہتر خرابی کے پیغامات |
| کلوجور 1.10 | 2018 | بہتر خرابی کے پیغامات،`clj`CLI |
| بندش 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| بندش 1.12 | 2024 | **جاوا انٹراپ میں بہتری**،`definterface`|
## اہم سنگ میل
### ابتدائی لِسپ (1958–1970)
- **1958**: جان میک کارتھی نے MIT میں Lisp تخلیق کیا - "لسٹ پروسیسنگ"
- **1962**: Lisp 1.5 - پہلا نافذ شدہ ورژن
- کلیدی اختراعات: **کوڑا جمع کرنا**، **دوبارہ ہونا**، **ہومویکونیسیٹی** (کوڈ = ڈیٹا)
-`eval`- یونیورسل فنکشن
- `cond`،`car`/ `cdr`، `cons`، لیمبڈا
### اسکیم (1975–موجودہ)
- **1975**: گائے اسٹیل اور جیرالڈ سوسمین نے MIT میں اسکیم بنائی
- **فلسفہ**: مرصع - چھوٹا بنیادی، طاقتور تجرید
- لغوی اسکوپنگ (زیادہ تر زبانوں سے پہلے)
- فرسٹ کلاس تسلسل
- حفظان صحت سے متعلق میکرو
- ٹیل کال آپٹیمائزیشن (لازمی)
### کامن لِسپ (1984–موجودہ)
- **1984**: گائے اسٹیل نے "کامن لسپ دی لینگویج" شائع کیا۔
- **1994**: ANSI کامن لِسپ اسٹینڈرڈ (ANSI X3.226)
- **"کچن سنک" لِسپ** — بڑے پیمانے پر معیاری لائبریری
- CLOS (Common Lisp Object System) - سب سے طاقتور OOP
- کنڈیشن سسٹم - دوبارہ شروع کرنے کے قابل غلطیاں
- لوپ میکرو - طاقتور تکرار DSL
### بندش (2007–موجودہ)
- **2007**: Rich Hickey JVM کے لیے Clojure — Lisp تخلیق کرتی ہے۔
- **فلسفہ**: عملی، ہم آہنگ، ناقابل تغیر
- مستقل ناقابل تغیر ڈیٹا ڈھانچے
- STM (سافٹ ویئر ٹرانزیکشنل میموری)
-`core.async`(CSP طرز کی ہم آہنگی)
- سیملیس جاوا انٹراپ
- REPL سے چلنے والی ترقی
## نحوی ارتقاء
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

## فیچر ارتقاء
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

## ڈیزائن کے کلیدی اصول
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

## ماحولیاتی نظام کی نمو
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
