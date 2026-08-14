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
# Lisp & Clojure — Ecosystem & Tooling Guide

This guide covers the essential tools, frameworks, and infrastructure in the Lisp and Clojure ecosystem.

---

## Lisp & Clojure Implementations

| Implementation | Language | Notes |
|---------------|----------|-------|
| **Clojure** | JVM | Modern Lisp on the JVM |
| **ClojureScript** | JS | Clojure compiled to JavaScript |
| **SBCL** | Common Lisp | High-performance CL |
| **CCL** | Common Lisp | OpenMCL, fast compilation |
| **ECL** | Common Lisp | Embeddable, C interop |
| **Emacs Lisp** | Emacs | Extension language |
| **Racket** | Scheme | Language-oriented programming |
| **Guile** | Scheme | GNU extension language |

```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Clojure Tooling

| Tool | Purpose |
|------|---------|
| **Clojure CLI (clj)** | Official CLI tool |
| **Leiningen** | Classic project tool |
| **deps.edn** | Dependency management |
| **Babashka** | Fast Clojure scripting |
| **tools.build** | Build automation |
| **shadow-cljs** | ClojureScript builds |
| **Figwheel** | Live ClojureScript reloading |

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

## Common Lisp Tooling

| Tool | Purpose |
|------|---------|
| **Quicklisp** | Package manager |
| **ASDF** | Build system |
| **Roswell** | Lisp environment manager |
| **QLot** | Local dependency management |
| **SLIME** | Emacs Lisp IDE |
| **Sly** | Emacs Lisp IDE (SLIME fork) |

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

## Web Frameworks

| Framework | Language | Type |
|-----------|----------|------|
| **Ring + Compojure** | Clojure | HTTP handler + routing |
| **Pedestal** | Clojure | Full-stack web |
| **Luminus** | Clojure | Web framework stack |
| ** Reitit** | Clojure | Routing library |
| **Hunchentoot** | CL | HTTP server |
| **Caveman** | CL | Web framework |
| **Restas** | CL | REST framework |

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

## Database

| Technology | Language | Type |
|------------|----------|------|
| **next.jdbc** | Clojure | JDBC wrapper |
| **HugSQL** | Clojure | SQL-first |
| **honeysql** | Clojure | SQL DSL |
| **clojure.jdbc** | Clojure | JDBC interface |
| **Postmodern** | CL | PostgreSQL |
| **CLSQL** | CL | SQL interface |
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

## Testing

| Framework | Language | Purpose |
|-----------|----------|---------|
| **clojure.test** | Clojure | Built-in testing |
| **midje** | Clojure | BDD-style testing |
| **expectations** | Clojure | Expectation-based |
| **test.check** | Clojure | Property-based (QuickCheck) |
| **FiveAM** | CL | Unit testing |
| **prove** | CL | Testing framework |
| **lisp-unit** | CL | Unit testing |

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

## Code Quality

| Tool | Language | Purpose |
|------|----------|---------|
| **clj-kondo** | Clojure | Linter |
| **cljfmt** | Clojure | Formatter |
| **eastwood** | Clojure | Linting |
| **kibit** | Clojure | Code suggestions |
| **alex-and-terrys** | Clojure | Style guide |
| **alex-plus** | CL | Code analysis |

```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## Key Libraries

| Library | Language | Purpose |
|---------|----------|---------|
| **core.async** | Clojure | CSP concurrency |
| **transducers** | Clojure | Composable algorithms |
| **specter** | Clojure | Data navigation |
| **schema** | Clojure | Data validation |
| **malli** | Clojure | Data validation |
| **data.json** | Clojure | JSON |
| **cheshire** | Clojure | JSON (faster) |
| **hiccup** | Clojure | HTML generation |
| **re-frame** | ClojureScript | SPA framework |
| **reagent** | ClojureScript | React wrapper |
| **Om** | ClojureScript | React interface |
| **core.match** | Clojure | Pattern matching |
| **tools.logging** | Clojure | Logging |
| **mount** | Clojure | State management |
| **integrant** | Clojure | Component system |
| **usocket** | CL | Socket library |
| **bordeaux-threads** | CL | Threading |
| **alexandria** | CL | Utility library |

---

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **VS Code + Calva** | Best Clojure IDE |
| **CIDER (Emacs)** | Classic Clojure IDE |
| **IntelliJ + Cursive** | JetBrains Clojure |
| **SLIME / Sly** | Common Lisp (Emacs) |
| **Lem** | Common Lisp IDE |
| **Vim + Fireplace** | Vim Clojure |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Uberjar** | `clj -T:build jar` (Clojure) |
| **GraalVM Native** | Native image (limited) |
| **Docker** | Containerized |
| **Babashka** | Fast scripting |
| **Lisp binary** | Compiled binary (SBCL) |
| **Kubernetes** | Orchestration |

---

## Summary

The Lisp ecosystem spans multiple dialects: **Clojure** (JVM, modern), **Common Lisp** (classic, ANSI), **Racket** (language-oriented), and **Emacs Lisp** (editor scripting). Clojure's standard stack is: **Clojure CLI** with **deps.edn** for builds, **Ring + Compojure** or **Pedestal** for web, **next.jdbc** for databases, **clojure.test** for testing, **clj-kondo** for linting, and **VS Code + Calva** or **CIDER** as IDE. Common Lisp uses **Quicklisp** for packages, **SBCL** for compilation, and **SLIME** for development. Lisp's strengths are macros, homoiconicity, REPL-driven development, and interactive programming. The ecosystem excels at rapid prototyping, domain-specific languages, and data processing.
