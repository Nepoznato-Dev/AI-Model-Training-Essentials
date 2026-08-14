---
# Metadata
title: "Lisp & Clojure — Cheat Sheet"
description: "Quick-reference cheat sheet for Common Lisp and Clojure syntax and patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [lisp, clojure, functional, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Lisp i Clojure — Ściągawka
## Podstawy Clojure
```clojure
;; Variables
(def name "Alice")
(def age 30)
(def pi 3.14159)
(def active true)

;; Types
(type name)       ;; String
(type 42)         ;; Long
(type 3.14)       ;; Double
(type true)       ;; Boolean
(type nil)        ;; nil
(type :keyword)   ;; Keyword

;; String operations
(count name)      ;; 5
(clojure.string/upper-case name)
(clojure.string/lower-case name)
(clojure.string/trim "  hello  ")
(clojure.string/includes? name "lic")
(clojure.string/replace name "Alice" "Bob")
(subs name 0 3)   ;; "Ali"
(format "Hello, %s!" name)
```

## Kolekcje Clojure
```clojure
;; List
'(1 2 3)
(list 1 2 3)
(cons 0 '(1 2 3))    ;; (0 1 2 3)
(first '(1 2 3))     ;; 1
(rest '(1 2 3))      ;; (2 3)
(nth '(1 2 3) 1)     ;; 2

;; Vector
[1 2 3]
(vector 1 2 3)
(conj [1 2 3] 4)     ;; [1 2 3 4]
(get [1 2 3] 0)      ;; 1
([1 2 3] 0)          ;; 1
(assoc [1 2 3] 1 99) ;; [1 99 3]
(subvec [1 2 3 4] 1 3) ;; [2 3]

;; Map
{:name "Alice" :age 30}
(hash-map :name "Alice" :age 30)
(get m :name)
(:name m)            ;; keyword as function
(assoc m :email "a@b.com")
(dissoc m :age)
(merge m1 m2)
(keys m)
(vals m)
(select-keys m [:name :age])

;; Set
#{1 2 3}
(conj #{1 2 3} 4)
(contains? #{1 2 3} 2)
(union #{1 2} #{3 4})
(intersection #{1 2 3} #{2 3 4})
(difference #{1 2 3} #{2})
```

## Funkcje Clojure
```clojure
;; Function definition
(defn greet [name]
  (str "Hello, " name "!"))

(defn add
  [a b]
  (+ a b))

;; Anonymous function
#(+ %1 %2)
(fn [a b] (+ a b))
(map #(* % 2) [1 2 3])

;; Higher-order functions
(map inc [1 2 3])                    ;; (2 3 4)
(filter even? [1 2 3 4])             ;; (2 4)
(reduce + [1 2 3 4])                 ;; 10
(reduce + 0 [1 2 3])                 ;; 10 (with init)
(apply str ["a" "b" "c"])            ;; "abc"
(partial + 10)                       ;; function
(comp inc double)                    ;; composition
(some even? [1 2 3])                 ;; truthy
(every? pos? [1 2 3])                ;; true

;; Threading macros
(-> "Hello"                          ;; thread first
    clojure.string/lower-case
    (str " world")
    clojure.string/upper-case)

(->> [1 2 3 4 5]                     ;; thread last
     (filter odd?)
     (map #(* % %))
     (reduce +))

;; Destructuring
(let [{:keys [name age]} user]
  (println name age))

(let [[first & rest] items]
  (println first rest))
```

## Wspólne podstawy Lispa
```lisp
;; Variables
(defvar *name* "Alice")
(defparameter *age* 30)
(defconstant +pi+ 3.14159)
(let ((x 42) (y 10)) (+ x y))

;; Types
(type-of 42)         ;; (INTEGER ...)
(type-of 3.14)       ;; DOUBLE-FLOAT
(type-of "hello")    ;; (SIMPLE-STRING ...)
(type-of 'hello)     ;; SYMBOL
(type-of '(1 2 3))   ;; CONS

;; String operations
(length "hello")
(string-upcase "hello")
(string-downcase "HELLO")
(string-trim " " "  hi  ")
(search "lic" name)
(subseq name 0 3)
(concatenate 'string "Hello" " " "World")
(format nil "Hello, ~A!" name)
```

## Typowe wzorce Lisp
```lisp
;; List operations
'(1 2 3)
(list 1 2 3)
(cons 0 '(1 2 3))
(car '(1 2 3))       ;; 1
(cdr '(1 2 3))       ;; (2 3)
(nth 1 '(1 2 3))     ;; 2
(length '(1 2 3))    ;; 3
(append '(1 2) '(3 4))
(reverse '(1 2 3))
(member 2 '(1 2 3))  ;; (2 3)
(assoc 'b '((a 1) (b 2)))  ;; (b 2)

;; Higher-order
(mapcar #'1+ '(1 2 3))
(remove-if #'evenp '(1 2 3 4))
(reduce #'+ '(1 2 3 4))
(remove-duplicates '(1 2 2 3))
(sort '(3 1 4 1 5) #'<)

;; Loop
(loop for x in '(1 2 3) collect (* x x))
(loop for i from 1 to 10 sum i)
(loop for x across "hello" collect x)
(loop while condition do ...)

;; Macros
(defmacro unless (test &body body)
  `(if (not ,test) (progn ,@body)))

;; with-open
(with-open-file (stream "data.txt" :direction :input)
  (loop for line = (read-line stream nil nil)
        while line
        do (process line)))
```

## Obsługa błędów
```clojure
;; Clojure
(try
  (risky-operation)
  (catch Exception e
    (println "Error:" (.getMessage e)))
  (finally
    (cleanup)))

;; throw
(throw (Exception. "Something failed"))

;; ex-info / ex-data
(throw (ex-info "Not found" {:id 42}))
(try
  (throw (ex-info "Oops" {:code 500}))
  (catch Exception e
    (ex-data e)))  ;; {:code 500}
```

```lisp
;; Common Lisp
(handler-case
    (risky-operation)
  (division-by-zero () (print "Div by zero"))
  (error (e) (format t "Error: ~A~%" e)))

;; restarts
(define-condition my-error (error)
  ((message :initarg :message :reader my-error-message)))

(error 'my-error :message "Something failed")
```
