<!--
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

-->
# Lisp & Clojure — Modèles idiomatiques et meilleures pratiques
Ce guide couvre les modèles idiomatiques pour Lisp et Clojure.
---

## Idiomes Clojure
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

## Expressions idiomatiques courantes en Lisp
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

## Résumé
Les idiomes Clojure mettent l'accent sur : les données immuables, les macros de thread (`->`,`->>`), la déstructuration, les mots-clés en tant que fonctions et les spécifications de validation. Les idiomes Common Lisp mettent l'accent sur :`with-open`pour les ressources,`push`/`nreverse`pour la création de listes et plusieurs valeurs. Tous deux valorisent l’homoïconicité et le développement piloté par REPL.