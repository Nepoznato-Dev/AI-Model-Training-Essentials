<!--
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

-->
# Lisp & Clojure — عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز تصحیح کے ساتھ Lisp اور Clojure میں سب سے عام غلطیوں، ٹریپس، اور مخالف پیٹرن کی فہرست بناتی ہے۔
---

## 1. اقتباس کنفیوژن
```lisp
;; ❌ WRONG — quoting prevents evaluation
'(1 2 (+ 1 2))  ;; (1 2 (+ 1 2)) — not (1 2 3)

;; ✅ CORRECT — use quasiquote for selective evaluation
`(1 2 ,(+ 1 2))  ;; (1 2 3)
```

---

## 2. نہیں سمجھنا`nil`بمقابلہ`false`(بندی)
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

## 3. مجموعوں میں ترمیم کرنا (کلوجور)
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

## 4. دم کی تکرار کے لیے`recur`استعمال نہیں کرنا (کلوجور)
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

## 5. میکرو ہائیجین (کامن لِسپ)
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

## خلاصہ
Lisp/clojure ٹریپس: اقتباس تشخیص کو روکتا ہے (`,` کے ساتھ quasiquote کا استعمال کریں)،`nil`اور`false`دونوں غلط ہیں لیکن الگ الگ ہیں، مجموعے ناقابل تغیر ہیں (ایٹموں کو دوبارہ باندھنا یا استعمال کریں)، XQZMARKER3 اور دوبارہ استعمال کرنے کے لیے استعمال کریں متغیر کیپچر سے بچنے کے لیے میکروز میں `gensym`۔ لِسپ کا طریقہ یہ ہے: تغیر پذیری کو قبول کریں، ریڈر میکرو سسٹم کو سمجھیں، اور حفظان صحت کے مطابق میکرو لکھیں۔