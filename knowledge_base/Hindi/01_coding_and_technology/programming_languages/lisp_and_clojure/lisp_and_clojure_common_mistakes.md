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
# लिस्प और क्लोजर - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ सुधार के साथ लिस्प और क्लोजर में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है।
---

## 1. उद्धरण भ्रम
```lisp
;; ❌ WRONG — quoting prevents evaluation
'(1 2 (+ 1 2))  ;; (1 2 (+ 1 2)) — not (1 2 3)

;; ✅ CORRECT — use quasiquote for selective evaluation
`(1 2 ,(+ 1 2))  ;; (1 2 3)
```

---

## 2.`nil`बनाम`false`(क्लोजर) को नहीं समझना
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

## 3. संग्रह संशोधित करना (क्लोजर)
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

## 4. टेल रिकर्सन (क्लोजर) के लिए`recur`का उपयोग नहीं करना
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

## 5. मैक्रो हाइजीन (कॉमन लिस्प)
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

## सारांश
लिस्प/क्लोजर ट्रैप: उद्धरण मूल्यांकन को रोकता है (`,` के साथ quasiquote का उपयोग करें),`nil`और`false`दोनों गलत हैं लेकिन अलग हैं, संग्रह अपरिवर्तनीय हैं (परमाणुओं को फिर से बांधें या उपयोग करें), टेल रिकर्सन के लिए`recur`का उपयोग करें, और चर कैप्चर से बचने के लिए मैक्रोज़ में`gensym`का उपयोग करें। लिस्प तरीका है: अपरिवर्तनीयता को अपनाएं, रीडर मैक्रो सिस्टम को समझें, और स्वच्छ मैक्रोज़ लिखें।