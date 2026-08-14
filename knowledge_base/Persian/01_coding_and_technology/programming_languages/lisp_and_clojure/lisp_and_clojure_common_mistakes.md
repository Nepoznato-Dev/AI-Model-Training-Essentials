---
# Metadata
title: "Lisp & Clojure — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Lisp and Clojure with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [lisp, clojure, common-mistakes, anti-patterns, pitfalls, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Lisp & Clojure - اشتباهات رایج و ضد الگوها
این سند رایج ترین اشتباهات، تله ها و ضد الگوها را در Lisp و Clojure با اصلاحات فهرست می کند.
---

## 1. نقل قول سردرگمی
```lisp
;; ❌ WRONG — quoting prevents evaluation
'(1 2 (+ 1 2))  ;; (1 2 (+ 1 2)) — not (1 2 3)

;; ✅ CORRECT — use quasiquote for selective evaluation
`(1 2 ,(+ 1 2))  ;; (1 2 3)
```

---

## 2. درک نکردن`nil`در مقابل`false`(Clojure)
```clojure
;; ❌ WRONG — assuming nil and false are interchangeable
(nil? false)   ;; false
(false? nil)   ;; false
(if nil "yes" "no")  ;; "no" (nil is falsy)
(if false "yes" "no")  ;; "no" (false is falsy)

;; ✅ CORRECT — both are falsy, but distinct
(identical? nil nil)   ;; true
(identical? false false) ;; true
(nil? nil)   ;; true
(false? false) ;; true
```

---

## 3. اصلاح مجموعه ها (Clojure)
```clojure
;; ❌ WRONG — expecting mutation
(def v [1 2 3])
(conj v 4)  ;; returns [1 2 3 4]
v  ;; still [1 2 3]!

;; ✅ CORRECT — rebind
(def v (conj v 4))
;; or use atoms/refs for shared mutable state
(def v (atom [1 2 3]))
(swap! v conj 4)
```

---

## 4. عدم استفاده از`recur`برای بازگشت دم (Clojure)
```clojure
;; ❌ WRONG — stack overflow on large inputs
(defn sum [n]
  (if (zero? n) 0 (+ n (sum (dec n)))))

;; ✅ CORRECT — use recur
(defn sum [n]
  (loop [i n acc 0]
    (if (zero? i)
      acc
      (recur (dec i) (+ acc i)))))
```

---

## 5. بهداشت ماکرو (معمولی لب)
```lisp
;; ❌ WRONG — variable capture in macro
(defmacro bad-double (x)
  `(* ,x 2))  ;; fine, but:
(defmacro bad-inc (x)
  `(let ((tmp 1))
     (+ ,x tmp)))  ;; tmp might be captured!

;; ✅ CORRECT — use gensym
(defmacro good-inc (x)
  (let ((tmp (gensym "tmp")))
    `(let ((,tmp 1))
       (+ ,x ,tmp))))
```

---

## خلاصه
تله‌های Lisp/Clojure: نقل قول از ارزیابی جلوگیری می‌کند (از شبه نقل قول با`,`استفاده کنید)،`nil`و`false`هر دو نادرست هستند اما متمایز هستند، مجموعه‌ها تغییرناپذیر هستند (بازدید کردن یا استفاده از اتم‌ها)، از`recur`برای استفاده از `recur`، و از`recur`برای استفاده مجدد استفاده کنید. گرفتن متغیر روش Lisp این است: تغییر ناپذیری را بپذیرید، سیستم کلان خواننده را درک کنید و ماکروهای بهداشتی بنویسید.