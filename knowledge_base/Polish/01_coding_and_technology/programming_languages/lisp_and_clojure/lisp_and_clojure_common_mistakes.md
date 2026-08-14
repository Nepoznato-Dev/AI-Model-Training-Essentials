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
# Lisp i Clojure — typowe błędy i anty-wzorce
Dokument ten kataloguje najczęstsze błędy, pułapki i anty-wzorce w Lisp i Clojure wraz z poprawkami.
---

## 1. Zamieszanie w cytatach
```lisp
;; ❌ WRONG — quoting prevents evaluation
'(1 2 (+ 1 2))  ;; (1 2 (+ 1 2)) — not (1 2 3)

;; ✅ CORRECT — use quasiquote for selective evaluation
`(1 2 ,(+ 1 2))  ;; (1 2 3)
```

---

## 2. Brak zrozumienia`nil`vs`false`(Clojure)
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

## 3. Modyfikowanie kolekcji (Clojure)
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

## 4. Nieużywanie`recur`do rekurencji ogona (Clojure)
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

## 5. Higiena makro (wspólny Lisp)
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

## Streszczenie
Pułapki Lisp/Clojure: cudzysłów uniemożliwia ocenę (użyj quasicytatu z`,`),`nil`i`false`są fałszywe, ale odrębne, kolekcje są niezmienne (ponowne wiązanie lub użycie atomów), użyj`recur`do rekurencji ogona i użyj`gensym`w makrach, aby uniknąć przechwytywania zmiennych. Sposób Lispa polega na: przyjęciu niezmienności, zrozumieniu systemu makr czytnika i pisaniu higienicznych makr.