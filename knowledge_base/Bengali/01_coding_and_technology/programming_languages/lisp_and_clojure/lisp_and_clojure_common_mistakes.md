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
# Lisp & Clojure — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্ন
এই নথিটি সংশোধন সহ Lisp এবং Clojure-এ সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্ন ক্যাটালগ করে।
---

## 1. উদ্ধৃতি বিভ্রান্তি
```lisp
;; ❌ WRONG — quoting prevents evaluation
'(1 2 (+ 1 2))  ;; (1 2 (+ 1 2)) — not (1 2 3)

;; ✅ CORRECT — use quasiquote for selective evaluation
`(1 2 ,(+ 1 2))  ;; (1 2 3)
```

---

## 2.`nil`বনাম`false`(ক্লোজার) বোঝা যাচ্ছে না
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

## 3. সংগ্রহগুলি সংশোধন করা (ক্লোজার)
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

## 4. টেইল রিকারশনের জন্য`recur`ব্যবহার না করা (ক্লোজার)
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

## 5. ম্যাক্রো হাইজিন (সাধারণ লিস্প)
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

## সারাংশ
Lisp/clojure ট্র্যাপ: উদ্ধৃতি মূল্যায়ন প্রতিরোধ করে (`,` এর সাথে কোয়াসিকোট ব্যবহার করুন),`nil`এবং`false`উভয়ই মিথ্যা কিন্তু স্বতন্ত্র, সংগ্রহগুলি অপরিবর্তনীয় (পরমাণুগুলিকে রিবান্ড বা ব্যবহার করুন), XQZMARKER3 এবং পুনঃব্যবহারের জন্য ব্যবহার করুন পরিবর্তনশীল ক্যাপচার এড়াতে ম্যাক্রোতে `gensym`। লিস্পের উপায় হল: অপরিবর্তনীয়তাকে আলিঙ্গন করুন, পাঠক ম্যাক্রো সিস্টেমটি বুঝুন এবং স্বাস্থ্যকর ম্যাক্রো লিখুন।