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
# Lisp & Clojure — تاريخ الإصدار وتطوره
## الجدول الزمني ليسب
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| اللثغة 1.5 | 1962 | **تم تنفيذ Lisp لأول مرة** (جون مكارثي، معهد ماساتشوستس للتكنولوجيا) |
| ماكليسب | الستينيات | معهد ماساتشوستس للتكنولوجيا المركزية ليسب |
| انترليسب | 1967 | Xerox PARC — التحرير المنظم |
| مخطط | 1975 | ** اللثغة البسيطة ** (سوسمان وستيل، معهد ماساتشوستس للتكنولوجيا) |
| اللثغة المشتركة | 1984 | ** اللثغة الموحدة ** (جاي ستيل، ANSI 1994) |
| ايماكس ليسب | 1985 | ليسب لمحرر إيماكس |
| مخطط R5RS | 1998 | التقرير المنقح⁵ — معيار المخطط المعتمد على نطاق واسع |
| مخطط R6RS | 2007 | نظام الوحدة، يونيكود |
| مخطط R7RS | 2013 | لغة صغيرة (R7RS-صغير) |
| كلوجر | 2007 | ** اللثغة الحديثة على JVM ** (ريتش هيكي) |
| كلوجر 1.0 | 2009 | أول إصدار مستقر |
| كلوجر 1.3 | 2011 | البروتوكولات،`defrecord`|
| كلوجر 1.4 | 2012 | شروط القارئ |
| كلوجر 1.5 | 2013 | محولات الطاقة (في وقت لاحق) |
| كلوجر 1.7 | 2015 | ** محولات الطاقة **، الشرطية القارئ |
| كلوجر 1.8 | 2016 | `spec`(التحقق من صحة البيانات)،`clojure.spec`|
| كلوجر 1.9 | 2017 | **`spec`مستقر **، رسائل خطأ محسنة |
| كلوجر 1.10 | 2018 | رسائل خطأ أفضل،`clj`CLI |
| كلوجر 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| كلوجر 1.12 | 2024 | **تحسينات التشغيل المتداخل لـ Java**،`definterface`|
## المعالم الرئيسية
### اللثغة المبكرة (1958–70s)
- **1958**: أنشأ جون مكارثي Lisp في معهد ماساتشوستس للتكنولوجيا - "معالجة القائمة"
- **1962**: Lisp 1.5 — أول إصدار تم تنفيذه
- الابتكارات الرئيسية: **جمع البيانات المهملة**، **التكرار**، **التماثلية** (الرمز = البيانات)
-`eval`— الوظيفة العالمية
- `cond`،`car`/ `cdr`، `cons`، لامدا
### المخطط (1975 إلى الوقت الحاضر)
- **1975**: أنشأ جاي ستيل وجيرالد سوسمان مخططًا في معهد ماساتشوستس للتكنولوجيا
- **الفلسفة**: الحد الأدنى — جوهر صغير، تجريدات قوية
- النطاق المعجمي (قبل معظم اللغات)
- استمرارات من الدرجة الأولى
- وحدات الماكرو الصحية
- تحسين الاتصال الخلفي (إلزامي)
### اللثغة الشائعة (1984 إلى الوقت الحاضر)
- **1984**: نشر جاي ستيل كتاب "Common Lisp the Language"
- **1994**: معيار ANSI Common Lisp (ANSI X3.226)
- **"حوض المطبخ" ليسب** - مكتبة قياسية ضخمة
- CLOS (نظام كائن Lisp المشترك) - أقوى OOP
- نظام الحالة - أخطاء قابلة لإعادة التشغيل
- حلقة ماكرو - تكرار قوي لـ DSL
### كلوجر (2007 إلى الوقت الحاضر)
- **2007**: قام Rich Hickey بإنشاء Clojure — Lisp لـ JVM
- **الفلسفة**: عملية، متزامنة، غير قابلة للتغيير
- هياكل البيانات الثابتة غير القابلة للتغيير
- STM (ذاكرة المعاملات البرمجية)
-`core.async`(التزامن على نمط CSP)
- التشغيل التفاعلي السلس لجافا
- التطوير القائم على REPL
## تطور بناء الجملة
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

## تطور الميزة
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

## مبادئ التصميم الرئيسية
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

## نمو النظام البيئي
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
