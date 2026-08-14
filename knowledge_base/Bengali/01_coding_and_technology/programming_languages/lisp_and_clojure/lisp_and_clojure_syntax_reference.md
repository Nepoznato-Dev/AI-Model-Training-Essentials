<!--
---
# Metadata
title: "Lisp & Clojure — Syntax Reference"
description: "Detailed syntax reference for Lisp and Clojure covering S-expressions, macros, persistent data structures, concurrency, and functional programming patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [lisp, clojure, syntax-reference, macros, s-expressions, persistent-data, concurrency, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Lisp & Clojure — সিনট্যাক্স রেফারেন্স
এই নথিটি কমন লিস্প এবং ক্লোজারের জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স সরবরাহ করে। এটি এস-এক্সপ্রেশন, ম্যাক্রো, স্থায়ী ডেটা স্ট্রাকচার এবং কার্যকরী প্রোগ্রামিং প্যাটার্নগুলিতে ফোকাস করে প্রধান লিস্প/ক্লোজার রেফারেন্সের পরিপূরক।
---

## ক্লোজার — মূল সিনট্যাক্স
```clojure
;; Literals
42              ;; integer
3.14            ;; float
"hello"         ;; string
:keyword        ;; keyword
true false nil  ;; booleans and nil
\c              ;; character

;; Collections
[1 2 3]                        ;; vector
{:name "Alice" :age 30}        ;; map
#{1 2 3}                       ;; set
'(1 2 3)                       ;; list (quoted)

;; Function calls
(+ 1 2 3)                      ;; 6
(str "hello" " " "world")      ;; "hello world"
(count [1 2 3])                ;; 3

;; Defining functions
(defn greet [name]
  (str "Hello, " name "!"))

(defn add
  ([x] x)                      ;; 1-arity
  ([x y] (+ x y)))             ;; 2-arity

;; Anonymous functions
#(+ % 1)                       ;; increment
(fn [x] (* x x))               ;; explicit
```

---

## নিয়ন্ত্রণ প্রবাহ
```clojure
;; if
(if (> x 0) "positive" "non-positive")

;; when (if without else)
(when (pos? x)
  (println "positive!")
  (do-something))

;; cond
(cond
  (< x 0)  "negative"
  (= x 0)  "zero"
  (> x 0)  "positive")

;; case
(case status
  :active   "Active"
  :pending  "Pending"
  "Unknown")

;; Loop
(loop [i 0]
  (when (< i 10)
    (println i)
    (recur (inc i))))

;; for (sequence comprehension)
(for [x (range 10) :when (even? x)]
  (* x x))

;; do (multiple expressions, return last)
(do
  (println "step 1")
  (println "step 2")
  :result)
```

---

## স্থায়ী ডেটা স্ট্রাকচার
```clojure
;; Vectors
(def v [1 2 3])
(conj v 4)           ;; [1 2 3 4] — original unchanged
(assoc v 1 99)       ;; [1 99 3]
(get v 0)            ;; 1
(subvec v 1 3)       ;; [2 3]

;; Maps
(def m {:a 1 :b 2})
(assoc m :c 3)       ;; {:a 1 :b 2 :c 3}
(dissoc m :b)        ;; {:a 1}
(get m :a)           ;; 1
(:a m)               ;; 1 — keyword lookup
(update m :a inc)    ;; {:a 2}
(merge m {:c 3 :d 4})

;; Sets
(def s #{1 2 3})
(conj s 4)           ;; #{1 2 3 4}
(disj s 2)           ;; #{1 3}
(contains? s 3)      ;; true
(clojure.set/union #{1 2} #{2 3})   ;; #{1 2 3}
(clojure.set/intersection #{1 2} #{2 3})  ;; #{2}

;; Sorted collections
(sorted-map :b 2 :a 1 :c 3)  ;; {:a 1 :b 2 :c 3}
(sorted-set 3 1 2)            ;; #{1 2 3}
```

---

## থ্রেডিং ম্যাক্রো
```clojure
;; -> (thread first)
(-> "Hello World"
    (.toLowerCase)
    (.split " ")
    (vec))
;; ["hello" "world"]

;; ->> (thread last)
(->> (range 10)
     (filter even?)
     (map #(* % %))
     (reduce +))
;; 120

;; some-> (thread if non-nil)
(some-> user
        :address
        :city
        (.toUpperCase))

;; as-> (bind name)
(as-> [1 2 3] $
  (conj $ 4)
  (map inc $)
  (reduce + $))
```

---

## ম্যাক্রো
```clojure
;; Simple macro
(defmacro unless [condition & body]
  `(if (not ~condition)
     (do ~@body)))

;; Macro with syntax quoting
(defmacro when-let [[binding expr] & body]
  `(let [temp# ~expr]
     (when temp#
       (let [~binding temp#]
         ~@body))))

;; Destructuring in macros
(defmacro defmemoized [name args & body]
  `(let [cache# (atom {})]
     (defn ~name ~args
       (let [key# ~args]
         (if-let [cached# (get @cache# key#)]
           cached#
           (let [result# (do ~@body)]
             (swap! cache# assoc key# result#)
             result#))))))
```

---

## সামঞ্জস্য
```clojure
;; Atoms — synchronous, uncoordinated
(def counter (atom 0))
(swap! counter inc)           ;; 1
(swap! counter + 10)          ;; 11
(deref counter)               ;; 11
@counter                      ;; 11

;; Refs — coordinated, transactional
(def account (ref {:balance 100}))
(dosync
  (alter account update :balance - 30))

;; Agents — asynchronous
(def logger (agent []))
(send logger conj "message 1")
(send logger conj "message 2")

;; core.async — channels
(require '[clojure.core.async :as async])
(let [ch (async/chan)]
  (async/go (async/>! ch "hello"))
  (async/go (println (async/<! ch))))
```

---

## সারাংশ
Clojure এর সিনট্যাক্স একইভাবে বন্ধনী করা হয়েছে — প্রতিটি ফর্ম একটি তালিকা। এই হোমোইকোনিসিটি শক্তিশালী ম্যাক্রোগুলিকে সক্ষম করে যা কোডকে ডেটা হিসাবে রূপান্তর করে। ক্রমাগত ডেটা স্ট্রাকচারগুলি দক্ষতার জন্য কাঠামোগত ভাগ করে নেওয়ার সাথে অপরিবর্তনীয়তা প্রদান করে। থ্রেডিং ম্যাক্রো পঠনযোগ্য ডেটা পাইপলাইন তৈরি করে। কনকারেন্সি আদিম (পরমাণু, রেফ, এজেন্ট, চ্যানেল) নিরাপদে রাষ্ট্র পরিবর্তন পরিচালনা করে। আধুনিক প্রোগ্রামিং-এ লিস্প/ক্লোজুরের প্রভাব প্রচুর — আবর্জনা সংগ্রহ, REPL, ম্যাক্রো এবং কার্যকরী প্রোগ্রামিং সবই লিস্পে ফিরে আসে।