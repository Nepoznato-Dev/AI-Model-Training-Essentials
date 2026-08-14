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
# Lisp & Clojure — Các mẫu thành ngữ & các phương pháp hay nhất
Hướng dẫn này bao gồm các mẫu thành ngữ cho Lisp và Clojure.
---

## Thành ngữ Clojure
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

## Thành ngữ Lisp thông dụng
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

## Bản tóm tắt
Thành ngữ Clojure nhấn mạnh: dữ liệu bất biến, macro phân luồng (`->`,`->>`), phá hủy, từ khóa dưới dạng hàm và thông số xác thực. Các thành ngữ Lisp phổ biến nhấn mạnh:`with-open`dành cho tài nguyên,`push`/`nreverse`để xây dựng danh sách và nhiều giá trị. Cả hai đều coi trọng tính đồng nhất và sự phát triển theo hướng REPL.