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

# Lisp & Clojure - تاریخچه نسخه و تکامل
## جدول زمانی Lisp
| نسخه | سال | تم کلید |
|---------|------|-----------|
| Lisp 1.5 | 1962 | **برای اولین بار Lisp اجرا شد** (جان مک کارتی، MIT) |
| Maclisp | دهه 1960 | MIT Mainframe Lisp |
| اینترلیسپ | 1967 | زیراکس PARC — ویرایش ساختار یافته |
| طرح | 1975 | **لیسپ مینیمالیست** (Sussman & Steele, MIT) |
| لب معمولی | 1984 | ** Lisp استاندارد ** (Guy Steele, ANSI 1994) |
| Emacs Lisp | 1985 | Lisp برای ویرایشگر Emacs |
| طرح R5RS | 1998 | گزارش تجدیدنظر شده⁵ — استاندارد طرح به طور گسترده پذیرفته شده |
| طرح R6RS | 2007 | سیستم ماژول، یونیکد |
| طرح R7RS | 2013 | زبان کوچک (R7RS-small) |
| کلوژور | 2007 | **لیسپ مدرن در JVM** (ریچ هیکی) |
| Clojure 1.0 | 2009 | اولین انتشار پایدار |
| Clojure 1.3 | 2011 | پروتکل ها،`defrecord`|
| Clojure 1.4 | 2012 | شرطی خواننده |
| Clojure 1.5 | 2013 | مبدل ها (بعد) |
| Clojure 1.7 | 2015 | **ترنسدیوسر**، شرطی خواننده |
| Clojure 1.8 | 2016 | `spec`(تأیید اعتبار داده)،`clojure.spec`|
| Clojure 1.9 | 2017 | **`spec`پایدار **، پیام های خطا بهبود یافته |
| Clojure 1.10 | 2018 | پیام های خطای بهتر،`clj`CLI |
| Clojure 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Clojure 1.12 | 2024 | **بهبودهای جاوای interop**،`definterface`|
## نقاط عطف اصلی
### اوایل لیسپ (1958-1970)
- **1958**: جان مک کارتی Lisp را در MIT ایجاد کرد - "List Processing"
- **1962**: Lisp 1.5 — اولین نسخه پیاده سازی شده
- نوآوری های کلیدی: **جمع آوری زباله**، **بازگشت**، **همسانی** (کد = داده)
-`eval`- عملکرد جهانی
- `cond`،`car`/ `cdr`، `cons`، لامبدا
### طرح (1975–اکنون)
- **1975**: گای استیل و جرالد ساسمن طرحی را در MIT ایجاد کردند
- **فلسفه**: مینیمالیست - هسته کوچک، انتزاعات قدرتمند
- محدوده واژگانی (قبل از اکثر زبان ها)
- ادامه درجه یک
- ماکروهای بهداشتی
- بهینه سازی دم تماس (اجباری)
### Common Lisp (1984–اکنون)
- **1984**: گای استیل "Common Lisp the Language" را منتشر کرد
- **1994**: استاندارد ANSI Common Lisp (ANSI X3.226)
- ** "سینک آشپزخانه" Lisp ** - کتابخانه استاندارد عظیم
- CLOS (Common Lisp Object System) - قدرتمندترین OOP
- سیستم وضعیت - خطاهای قابل راه اندازی مجدد
- حلقه ماکرو - تکرار قدرتمند DSL
### Clojure (2007–اکنون)
- **2007**: ریچ هیکی Clojure — Lisp را برای JVM ایجاد می کند
- **فلسفه**: عملی، همزمان، تغییرناپذیر
- ساختارهای داده تغییرناپذیر پایدار
- STM (حافظه معاملاتی نرم افزار)
-`core.async`(هم‌زمان به سبک CSP)
- تعامل بدون درز جاوا
- توسعه مبتنی بر REPL
## تکامل نحو
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

## تکامل ویژگی
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

## اصول کلیدی طراحی
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

## رشد اکوسیستم
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
