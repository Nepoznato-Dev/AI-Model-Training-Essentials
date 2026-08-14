---
# Metadata
title: "Lisp & Clojure — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Lisp and Clojure ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Lisp & Clojure: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, i framework e le infrastrutture essenziali nell'ecosistema Lisp e Clojure.
---

## Implementazioni Lisp e Clojure
| Attuazione | Lingua | Note |
|---------------|----------|-------|
| **Clojure** | JVM | Lisp moderno sulla JVM |
| **ClojureScript** | JS | Clojure compilato in JavaScript |
| **SBCL** | Lisp comune | CL ad alte prestazioni |
| **CCL** | Lisp comune | OpenMCL, compilazione veloce |
| **ECL** | Lisp comune | Incorporabile, interoperabilità C |
| **Emacs Lisp** | Emacs | Lingua dell'estensione |
| **Racchetta** | Schema | Programmazione orientata al linguaggio |
| **Guile** | Schema | Lingua dell'estensione GNU |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Utensili Clojure
| Strumento | Scopo |
|------|---------|
| **Clojure CLI (clj)** | Strumento CLI ufficiale |
| **Leiningen** | Strumento di progetto classico |
| **deps.edn** | Gestione delle dipendenze |
| **Babashka** | Scripting veloce di Clojure |
| **tools.build** | Costruisci automazione |
| **shadow-cljs** | ClojureScript crea |
| **Ruota di figura** | Ricaricamento live ClojureScript |
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

## Strumenti Lisp comuni
| Strumento | Scopo |
|------|---------|
| **Breve breve** | Gestore pacchetti |
| **ASDF** | Costruisci sistema |
| **Roswell** | Responsabile dell'ambiente Lisp |
| **QLotto** | Gestione delle dipendenze locali |
| **LIMA** | IDE Emacs Lisp |
| **Astuto** | Emacs Lisp IDE (forcella SLIME) |
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

## Framework Web
| Quadro | Lingua | Digitare |
|-----------|----------|------|
| **Anello + Compojure** | Clojure | Gestore HTTP + instradamento |
| **Piedistallo** | Clojure | Web a stack completo |
| **Lumino** | Clojure | Stack di framework Web |
| **Reitit** | Clojure | Libreria di routing |
| **Hunchentoot** | CL | ServerHTTP |
| **Uomo delle caverne** | CL | Struttura Web |
| **Resta** | CL | Quadro REST |
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

##Banca dati
| Tecnologia | Lingua | Digitare |
|------------|----------|------|
| **successivo.jdbc** | Clojure | Involucro JDBC |
| **AbbracciaSQL** | Clojure | SQL-prima |
| **tesoroql** | Clojure | SQLDSL |
| **clojure.jdbc** | Clojure | Interfaccia JDBC |
| **Postmoderno** | CL | PostgreSQL |
| **CLSQL** | CL | Interfaccia SQL |
| **SxQL** | CL | SQLDSL |
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

## Test
| Quadro | Lingua | Scopo |
|-----------|----------|---------|
| **clojure.test** | Clojure | Test integrato |
| **midje** | Clojure | Test in stile BDD |
| **aspettative** | Clojure | Basato sulle aspettative |
| **test.controllo** | Clojure | Basato sulla proprietà (QuickCheck) |
| **Cinque del mattino** | CL | Test unitario |
| **dimostrare** | CL | Quadro di prova |
| **unità lisp** | CL | Test unitario |
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

## Qualità del codice
| Strumento | Lingua | Scopo |
|------|----------|---------|
| **clj-kondo** | Clojure | Linter |
| **cljfmt** | Clojure | Formattatore |
| **eastwood** | Clojure | Lining |
| **kibit** | Clojure | Suggerimenti sul codice |
| **alex-e-terrys** | Clojure | Guida allo stile |
| **alex-plus** | CL | Analisi del codice |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## Biblioteche chiave
| Biblioteca | Lingua | Scopo |
|---------|----------|---------|
| **core.async** | Clojure | Concorrenza CSP |
| **trasduttori** | Clojure | Algoritmi componibili |
| **spettro** | Clojure | Navigazione dati |
| **schema** | Clojure | Convalida dei dati |
| **malli** | Clojure | Convalida dei dati |
| **data.json** | Clojure | JSON |
| **Cheshire** | Clojure | JSON (più veloce) |
| **singhiozzo** | Clojure | Generazione HTML |
| **riincorniciare** | ClojureScript | Quadro SPA |
| **reagente** | ClojureScript | Involucro di reazione |
| **Om** | ClojureScript | Reagire interfaccia |
| **core.match** | Clojure | Corrispondenza di modelli |
| **tools.logging** | Clojure | Registrazione |
| **montare** | Clojure | Gestione statale |
| **integrante** | Clojure | Sistema di componenti |
| **usopresa** | CL | Libreria socket |
| **fili bordeaux** | CL | Filettatura |
| **Alessandria** | CL | Libreria di utilità |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **Codice VS + Calva** | Miglior IDE Clojure |
| **SIDRO (Emacs)** | IDE Clojure classico |
| **IntelliJ + corsivo** | Chiusura JetBrains |
| **SLIME / Furbo** | Lisp comune (Emacs) |
| **Lem** | IDE Lisp comune |
| **Vim + Camino** | Vim Clojure |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Uberjar** | `clj -T:build jar`(Clojure) |
| **GraalVM nativo** | Immagine nativa (limitata) |
| **Docker** | Containerizzato |
| **Babashka** | Scripting veloce |
| **Binario Lisp** | Binario compilato (SBCL) |
| **Kubernetes** | Orchestrazione |
---

## Riepilogo
L'ecosistema Lisp comprende più dialetti: **Clojure** (JVM, moderno), **Common Lisp** (classico, ANSI), **Racket** (orientato al linguaggio) e **Emacs Lisp** (scripting dell'editor). Lo stack standard di Clojure è: **Clojure CLI** con **deps.edn** per build, **Ring + Compojure** o **Pedestal** per il web, **next.jdbc** per database, **clojure.test** per test, **clj-kondo** per linting e **VS Code + Calva** o **CIDER** come IDE. Common Lisp utilizza **Quicklisp** per i pacchetti, **SBCL** per la compilazione e **SLIME** per lo sviluppo. I punti di forza di Lisp sono le macro, l'omoiconicità, lo sviluppo basato su REPL e la programmazione interattiva. L'ecosistema eccelle nella prototipazione rapida, nei linguaggi specifici del dominio e nell'elaborazione dei dati.