---
# Metadata
title: "Lisp & Clojure — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Lisp and Clojure with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Lisp & Clojure: errori comuni e anti-pattern
Questo documento cataloga gli errori, le trappole e gli anti-pattern più comuni in Lisp e Clojure con le correzioni.
---

## 1. Citazione Confusione
```lisp
;; ❌ WRONG — quoting prevents evaluation
'(1 2 (+ 1 2))  ;; (1 2 (+ 1 2)) — not (1 2 3)

;; ✅ CORRECT — use quasiquote for selective evaluation
`(1 2 ,(+ 1 2))  ;; (1 2 3)
```

---

## 2. Non capire`nil`vs`false`(Clojure)
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

## 3. Modifica delle raccolte (Clojure)
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

## 4. Non utilizzare`recur`per la ricorsione in coda (Clojure)
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

## 5. Macro Igiene (Lisp Comune)
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

## Riepilogo
Trappole Lisp/Clojure: la citazione impedisce la valutazione (usa quasiquote con`,`),`nil`e`false`sono entrambi falsi ma distinti, le raccolte sono immutabili (riassociano o usano atomi), usano`recur`per la ricorsione della coda e usano`gensym`nelle macro per evitare la cattura delle variabili. Il metodo Lisp è: abbracciare l'immutabilità, comprendere il sistema macro del lettore e scrivere macro igieniche.