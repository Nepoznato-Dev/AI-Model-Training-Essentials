<!--
---
# Metadata
title: "Lisp & Clojure — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Lisp and Clojure ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [lisp, clojure, ecosystem, tooling, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Lisp i Clojure — Przewodnik po ekosystemie i narzędziach
Ten przewodnik omawia podstawowe narzędzia, frameworki i infrastrukturę w ekosystemie Lisp i Clojure.
---

## Implementacje Lisp i Clojure
| Wdrożenie | Język | Notatki |
|--------------|----------|-------|
| **Zamknięcie** | JVM | Nowoczesny Lisp na JVM |
| **ClojureScript** | JS | Clojure skompilowany do JavaScript |
| **SBCL** | Wspólny Lisp | Wysoka wydajność CL |
| **CCL** | Wspólny Lisp | OpenMCL, szybka kompilacja |
| **ECL** | Wspólny Lisp | Możliwość osadzenia, interoperacja C |
| **Emacs Lisp** | Emacs | Język rozszerzenia |
| **Rakieta** | Schemat | Programowanie zorientowane na język |
| **Przebiegłość** | Schemat | Język rozszerzenia GNU |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Narzędzia Clojure
| Narzędzie | Cel |
|------|-------------|
| **Clojure CLI (clj)** | Oficjalne narzędzie CLI |
| **Leiningen** | Klasyczne narzędzie projektowe |
| **deps.edn** | Zarządzanie zależnościami |
| **Babaszka** | Szybkie skrypty Clojure |
| **narzędzia.kompilacja** | Buduj automatyzację |
| **cień-cljs** | Kompilacje ClojureScript |
| **Koło figowe** | Ponowne ładowanie ClojureScript na żywo |
```clojure
;; deps.edn
{:paths ["src" "resources"]
 :deps {org.clojure/clojure {:mvn/version "1.11.1"}
        ring/ring-core {:mvn/version "1.11.0"}
        ring/ring-jetty-adapter {:mvn/version "1.11.0"}
        com.github.seancorfield/next.jdbc {:mvn/version "1.3.909"}}
 
 :aliases
 {:run {:main-opts ["-m" "myapp.core"]}
  :test {:extra-paths ["test"]
         :extra-deps {io.github.cognitect-labs/test-runner {:git/tag "v0.5.1"}}
         :main-opts ["-m" "cognitect.test-runner"]}
  :build {:deps {io.github.clojure/tools.build {:mvn/version "0.9.6"}}
          :ns-default build}}}
```

```bash
clj -M:run                # run with alias
clj -M:test               # run tests
clj -T:build jar          # build JAR
clj -M:nrepl              # start REPL
bb -e '(+ 1 2 3)'        # Babashka inline
```

---

## Wspólne narzędzia Lisp
| Narzędzie | Cel |
|------|-------------|
| **Szybki skrót** | Menedżer pakietów |
| **ASDF** | Zbuduj system |
| **Roswell** | Menedżer środowiska Lisp |
| **QLot** | Zarządzanie zależnościami lokalnymi |
| **ŚLUZ** | Emacs Lisp IDE |
| **Przebiegły** | Emacs Lisp IDE (widelec SLIME) |
```lisp
;; Quicklisp
(ql:quickload "hunchentoot")  ; install/load library
(ql:quickload "cl-json")
(ql:update-all-dists)          ; update all

;; ASDF system definition
(asdf:defsystem myapp
  :description "My application"
  :depends-on ("hunchentoot" "cl-json")
  :components ((:file "package")
               (:file "main" :depends-on ("package"))))
```

---

## Struktury internetowe
| Ramy | Język | Wpisz |
|----------|----------|------|
| **Pierścień + Kompojure** | Zamknięcie | Obsługa HTTP + routing |
| **Piedestał** | Zamknięcie | Sieć z pełnym stosem |
| **Światło** | Zamknięcie | Stos frameworków sieciowych |
| **Reita** | Zamknięcie | Biblioteka routingu |
| **Hunchentoot** | CL | Serwer HTTP |
| **Jaskiniowiec** | CL | Struktura internetowa |
| **Odpoczynek** | CL | Struktura REST |
```clojure
;; Ring + Compojure example
(ns myapp.handler
  (:require [compojure.core :refer [defroutes GET POST]]
            [compojure.route :as route]
            [ring.middleware.json :refer [wrap-json-body wrap-json-response]]
            [ring.adapter.jetty :refer [run-jetty]]))

(defroutes app-routes
  (GET "/" [] "Hello, World!")
  (GET "/users/:id" [id] {:status 200 :body {:id id :name "User"}})
  (route/not-found "Not Found"))

(def app (-> app-routes wrap-json-response (wrap-json-body {:keywords? true})))

(defn -main [] (run-jetty app {:port 8080}))
```

---

## Baza danych
| Technologia | Język | Wpisz |
|------------|---------|------|
| **next.jdbc** | Zamknięcie | Opakowanie JDBC |
| **Przytul SQL** | Zamknięcie | Najpierw SQL |
| **honeysql** | Zamknięcie | SQL DSL |
| **clojure.jdbc** | Zamknięcie | Interfejs JDBC |
| **Postmodernizm** | CL | PostgreSQL |
| **CLSQL** | CL | Interfejs SQL |
| **SxQL** | CL | SQL DSL |
```clojure
;; next.jdbc example
(require '[next.jdbc :as jdbc]
         '[next.jdbc.result-set :as rs])

(def db {:dbtype "postgresql" :dbname "mydb" :user "admin" :password "secret"})

(defn find-users [min-age]
  (jdbc/execute! db
    ["SELECT id, name, email FROM users WHERE age > ?" min-age]
    {:builder-fn rs/as-unqualified-lower-maps}))
```

---

## Testowanie
| Ramy | Język | Cel |
|----------|----------|---------|
| **test zamknięcia** | Zamknięcie | Wbudowane testowanie |
| **pośrodku** | Zamknięcie | Testowanie w stylu BDD |
| **oczekiwania** | Zamknięcie | Oparte na oczekiwaniach |
| **test.sprawdz** | Zamknięcie | Oparte na właściwościach (QuickCheck) |
| **Piąta rano** | CL | Testowanie jednostkowe |
| **udowodnij** | CL | Ramy testowania |
| **jednostka Lisp** | CL | Testowanie jednostkowe |
```clojure
;; clojure.test
(ns myapp.user-service-test
  (:require [clojure.test :refer [deftest testing is are]]
            [myapp.user-service :as sut]))

(deftest find-user-test
  (testing "returns user when found"
    (let [repo (atom {1 {:id 1 :name "Alice"}})
          user (sut/find-user repo 1)]
      (is (= "Alice" (:name user)))))
  
  (testing "returns nil when not found"
    (let [repo (atom {})
          user (sut/find-user repo 999)]
      (is (nil? user)))))

;; test.check (property-based)
(require '[clojure.test.check :as tc]
         '[clojure.test.check.generators :as gen]
         '[clojure.test.check.properties :as prop])

(tc/quick-check 100
  (prop/for-all [v (gen/vector gen/int)]
    (= (sort v) (sort (sort v)))))
```

---

## Jakość kodu
| Narzędzie | Język | Cel |
|------|----------|--------|
| **clj-kondo** | Zamknięcie | Linter |
| **cljfmt** | Zamknięcie | Formater |
| **wschód** | Zamknięcie | Linting |
| **kibit** | Zamknięcie | Sugestie kodu |
| **Alex-i-Terrys** | Zamknięcie | Przewodnik po stylu |
| **alex-plus** | CL | Analiza kodu |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## Kluczowe biblioteki
| Biblioteka | Język | Cel |
|--------|----------|--------|
| **core.async** | Zamknięcie | Współbieżność CSP |
| **przetworniki** | Zamknięcie | Algorytmy komponowalne |
| **widmo** | Zamknięcie | Nawigacja danych |
| **schemat** | Zamknięcie | Walidacja danych |
| **male** | Zamknięcie | Walidacja danych |
| **data.json** | Zamknięcie | JSON |
| **Cheshire** | Zamknięcie | JSON (szybciej) |
| **czkawka** | Zamknięcie | Generowanie HTML |
| **wykadruj ponownie** | ClojureScript | Ramy SPA |
| **odczynnik** | ClojureScript | Opakowanie reakcji |
| **Om** | ClojureScript | Interfejs reakcji |
| **core.match** | Zamknięcie | Dopasowanie wzoru |
| **narzędzia.logowanie** | Zamknięcie | Rejestrowanie |
| **montaż** | Zamknięcie | Zarządzanie państwem |
| **integrator** | Zamknięcie | System komponentów |
| **usocket** | CL | Biblioteka gniazd |
| **bordowe nici** | CL | Gwintowanie |
| **aleksandria** | CL | Biblioteka narzędziowa |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Kod VS + Calva** | Najlepsze IDE Clojure |
| **CYDER (Emacs)** | Klasyczne Clojure IDE |
| **IntelliJ + kursywa** | Zamknięcie JetBrains |
| **ŚLIZM / Przebiegły** | Wspólny Lisp (Emacs) |
| **Lem** | Wspólne IDE Lispa |
| **Vim + Kominek** | Vim Clojure |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Uberjar** | `clj -T:build jar`(Zamknięcie) |
| **Natywny GraalVM** | Obraz natywny (ograniczony) |
| **Doker** | Kontenerowy |
| **Babaszka** | Szybkie pisanie |
| **Lisp binarny** | Skompilowany plik binarny (SBCL) |
| **Kubernetes** | Orkiestracja |
---

## Streszczenie
Ekosystem Lisp obejmuje wiele dialektów: **Clojure** (JVM, nowoczesny), **Common Lisp** (klasyczny, ANSI), **Racket** (zorientowany na język) i **Emacs Lisp** (skrypty edytora). Standardowy stos Clojure to: **Clojure CLI** z **deps.edn** dla kompilacji, **Ring + Compojure** lub **Pedestal** dla Internetu, **next.jdbc** dla baz danych, **clojure.test** dla testowania, **clj-kondo** dla lintingu i **VS Code + Calva** lub **CIDER** jako IDE. Common Lisp używa **Quicklisp** do pakietów, **SBCL** do kompilacji i **SLIME** do programowania. Mocnymi stronami Lispa są makra, homoikoniczność, rozwój oparty na REPL i programowanie interaktywne. Ekosystem wyróżnia się szybkim prototypowaniem, językami specyficznymi dla domeny i przetwarzaniem danych.