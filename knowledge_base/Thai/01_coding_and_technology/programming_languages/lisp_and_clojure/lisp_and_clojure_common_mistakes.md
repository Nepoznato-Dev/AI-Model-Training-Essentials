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
# Lisp & Clojure - ข้อผิดพลาดทั่วไปและการต่อต้านรูปแบบ
เอกสารนี้รวบรวมข้อผิดพลาด กับดัก และรูปแบบการต่อต้านที่พบบ่อยที่สุดใน Lisp และ Clojure พร้อมการแก้ไข
---

## 1. อ้างความสับสน
```lisp
;; ❌ WRONG — quoting prevents evaluation
'(1 2 (+ 1 2))  ;; (1 2 (+ 1 2)) — not (1 2 3)

;; ✅ CORRECT — use quasiquote for selective evaluation
`(1 2 ,(+ 1 2))  ;; (1 2 3)
```

---

## 2. ไม่เข้าใจ`nil`กับ`false`(Clojure)
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

## 3. การแก้ไขคอลเลกชัน (Clojure)
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

## 4. ไม่ใช้`recur`สำหรับการเรียกซ้ำหาง (Clojure)
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

## 5. สุขอนามัยมาโคร (เสียงกระเพื่อมทั่วไป)
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

## สรุป
Lisp/Clojure traps: เครื่องหมายคำพูดป้องกันการประเมิน (ใช้ quasiquote กับ`,`),`nil`และ`false`มีทั้งเท็จแต่แตกต่างกัน คอลเลกชันไม่เปลี่ยนรูป (rebind หรือใช้อะตอม) ใช้`recur`สำหรับการเรียกซ้ำส่วนท้าย และใช้`gensym`ในมาโครเพื่อหลีกเลี่ยงการจับตัวแปร วิธี Lisp คือ: ยอมรับความไม่เปลี่ยนรูป ทำความเข้าใจระบบมาโครของผู้อ่าน และเขียนมาโครที่ถูกสุขลักษณะ