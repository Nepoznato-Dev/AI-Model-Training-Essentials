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
# Lisp & Clojure – Leitfaden für Ökosysteme und Werkzeuge
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im Lisp- und Clojure-Ökosystem.
---

## Lisp- und Clojure-Implementierungen
| Umsetzung | Sprache | Notizen |
|---------------|----------|-------|
| **Clojure** | JVM | Modernes Lisp auf der JVM |
| **ClojureScript** | JS | Clojure kompiliert zu JavaScript |
| **SBCL** | Gemeinsames Lispeln | Hochleistungs-CL |
| **CCL** | Gemeinsames Lispeln | OpenMCL, schnelle Kompilierung |
| **ECL** | Gemeinsames Lispeln | Einbettbar, C-Interop |
| **Emacs Lisp** | Emacs | Erweiterungssprache |
| **Schläger** | Schema | Sprachorientierte Programmierung |
| **Guile** | Schema | GNU-Erweiterungssprache |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Clojure-Werkzeug
| Werkzeug | Zweck |
|------|---------|
| **Clojure CLI (clj)** | Offizielles CLI-Tool |
| **Leiningen** | Klassisches Projekttool |
| **deps.edn** | Abhängigkeitsmanagement |
| **Babaschka** | Schnelle Clojure-Skripterstellung |
| **tools.build** | Build-Automatisierung |
| **shadow-cljs** | ClojureScript-Builds |
| **Feigenrad** | Live ClojureScript wird neu geladen |
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

## Gemeinsames Lisp-Tooling
| Werkzeug | Zweck |
|------|---------|
| **Quicklisp** | Paketmanager |
| **ASDF** | Build-System |
| **Roswell** | Lisp-Umgebungsmanager |
| **QLot** | Lokales Abhängigkeitsmanagement |
| **SCHLEIM** | Emacs Lisp IDE |
| **Schlau** | Emacs Lisp IDE (SLIME-Fork) |
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

## Web-Frameworks
| Rahmen | Sprache | Geben Sie | ein
|-----------|----------|------|
| **Ring + Compojure** | Clojure | HTTP-Handler + Routing |
| **Sockel** | Clojure | Full-Stack-Web |
| **Luminus** | Clojure | Web-Framework-Stack |
| ** Reitit ** | Clojure | Routing-Bibliothek |
| **Hunchentoot** | CL | HTTP-Server |
| **Höhlenmensch** | CL | Web-Framework |
| **Restas** | CL | REST-Framework |
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

## Datenbank
| Technologie | Sprache | Geben Sie | ein
|------------|----------|------|
| **next.jdbc** | Clojure | JDBC-Wrapper |
| **HugSQL** | Clojure | SQL-first |
| **honeysql** | Clojure | SQL-DSL |
| **clojure.jdbc** | Clojure | JDBC-Schnittstelle |
| **Postmodern** | CL | PostgreSQL |
| **CLSQL** | CL | SQL-Schnittstelle |
| **SxQL** | CL | SQL-DSL |
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

## Testen
| Rahmen | Sprache | Zweck |
|-----------|----------|---------|
| **clojure.test** | Clojure | Integrierte Tests |
| **midje** | Clojure | Tests im BDD-Stil |
| **Erwartungen** | Clojure | Erwartungsbasiert |
| **test.check** | Clojure | Eigenschaftsbasiert (QuickCheck) |
| **Fünf Uhr morgens** | CL | Unit-Tests |
| **beweisen** | CL | Testrahmen |
| **Lisp-Einheit** | CL | Unit-Tests |
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

## Codequalität
| Werkzeug | Sprache | Zweck |
|------|----------|---------|
| **clj-kondo** | Clojure | Linter |
| **cljfmt** | Clojure | Formatierer |
| **eastwood** | Clojure | Fusseln |
| **kibit** | Clojure | Codevorschläge |
| **Alex-und-Terrys** | Clojure | Styleguide |
| **alex-plus** | CL | Code-Analyse |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## Wichtige Bibliotheken
| Bibliothek | Sprache | Zweck |
|---------|----------|---------|
| **core.async** | Clojure | CSP-Parallelität |
| **Wandler** | Clojure | Zusammensetzbare Algorithmen |
| **Gespenst** | Clojure | Datennavigation |
| **Schema** | Clojure | Datenvalidierung |
| **malli** | Clojure | Datenvalidierung |
| **data.json** | Clojure | JSON |
| **Cheshire** | Clojure | JSON (schneller) |
| **Schluckauf** | Clojure | HTML-Generierung |
| **Neurahmen** | ClojureScript | SPA-Framework |
| **Reagenz** | ClojureScript | React-Wrapper |
| **Om** | ClojureScript | Reaktionsschnittstelle |
| **core.match** | Clojure | Mustervergleich |
| **tools.logging** | Clojure | Protokollierung |
| **mount** | Clojure | Staatsverwaltung |
| **integrant** | Clojure | Komponentensystem |
| **usocket** | CL | Socket-Bibliothek |
| **bordeaux-fäden** | CL | Einfädeln |
| **Alexandria** | CL | Dienstprogrammbibliothek |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **VS-Code + Calva** | Beste Clojure-IDE |
| **Apfelwein (Emacs)** | Klassische Clojure-IDE |
| **IntelliJ + Kursiv** | JetBrains Clojure |
| **SCHLEIM / Schlau** | Gemeinsames Lisp (Emacs) |
| **Lem** | Common Lisp IDE |
| **Vim + Kamin** | Vim Clojure |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Uberjar** | `clj -T:build jar`(Clojure) |
| **GraalVM Native** | Natives Bild (begrenzt) |
| **Docker** | Containerisiert |
| **Babaschka** | Schnelle Skripterstellung |
| **Lisp-Binärdatei** | Kompilierte Binärdatei (SBCL) |
| **Kubernetes** | Orchestrierung |
---

## Zusammenfassung
Das Lisp-Ökosystem umfasst mehrere Dialekte: **Clojure** (JVM, modern), **Common Lisp** (klassisch, ANSI), **Racket** (sprachorientiert) und **Emacs Lisp** (Editor-Skripting). Der Standard-Stack von Clojure ist: **Clojure CLI** mit **deps.edn** für Builds, **Ring + Compojure** oder **Pedestal** für das Web, **next.jdbc** für Datenbanken, **clojure.test** für Tests, **clj-kondo** für Linting und **VS Code + Calva** oder **CIDER** als IDE. Common Lisp verwendet **Quicklisp** für Pakete, **SBCL** für die Kompilierung und **SLIME** für die Entwicklung. Die Stärken von Lisp sind Makros, Homoikonizität, REPL-gesteuerte Entwicklung und interaktive Programmierung. Das Ökosystem zeichnet sich durch schnelles Prototyping, domänenspezifische Sprachen und Datenverarbeitung aus.