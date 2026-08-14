---
# Metadata
title: "Lisp & Clojure — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean Lisp and Clojure code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [lisp, clojure, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Lisp 和 Clojure — 惯用模式和最佳实践
本指南涵盖 Lisp 和 Clojure 的惯用模式。
---

## Clojure 习语
```clojure
;; ✅ Prefer immutable data
(def users [{:name "Alice" :age 30}])

;; ✅ Threading macros
(-> users
    (filter #(>= (:age %) 18))
    (map :name)
    (sort))

;; ✅ Destructuring
(let [{:keys [name email age]} user]
  (println name email))

(let [[first & rest] items]
  (println first rest))

;; ✅ Keywords as functions
(:name user)          ;; get :name from user
(filter :active users) ;; filter where :active is truthy

;; ✅ comp and partial
(def process (comp sort filter-active map-names))

;; ✅ Spec for validation
(s/def ::name string?)
(s/def ::age (s/and int? pos?))
(s/def ::user (s/keys :req [::name ::age]))
```

---

## 常见的 Lisp 习语
```lisp
;; ✅ Use push/new for building lists
(let ((result '()))
  (dolist (item items)
    (push (process item) result))
  (nreverse result))

;; ✅ with-open for resources
(with-open-file (stream "data.txt" :direction :input)
  (loop for line = (read-line stream nil nil)
        while line
        do (process line)))

;; ✅ Multiple values
(multiple-value-bind (quotient remainder)
    (truncate 17 5)
  (format t "~A remainder ~A~%" quotient remainder))
```

---

＃＃ 概括
Clojure 习惯用法强调：不可变数据、线程宏（`->`、`->>`）、解构、关键字作为函数以及验证规范。 Common Lisp 习语强调：`with-open` 用于资源，`push` /`nreverse`用于列表构建，以及多个值。两者都重视同像性和 REPL 驱动的开发。