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

# Lisp & Clojure — Guide de l'écosystème et des outils
Ce guide couvre les outils, frameworks et infrastructures essentiels de l'écosystème Lisp et Clojure.
---

## Implémentations Lisp et Clojure
| Mise en œuvre | Langue | Remarques |
|---------------|----------|-------|
| **Clojure** | JVM | Lisp moderne sur la JVM |
| **ClojureScript** | JS | Clojure compilé en JavaScript |
| **SBCL** | Lisp commun | CL hautes performances |
| **CCL** | Lisp commun | OpenMCL, compilation rapide |
| **ECL** | Lisp commun | Intégrable, interopérabilité C |
| **Emacs Lisp** | Emacs | Langue d'extension |
| **Raquette** | Schéma | Programmation orientée langage |
| **Ruse** | Schéma | Langage d'extension GNU |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Outillage Clojure
| Outil | Objectif |
|------|--------------|
| **Clojure CLI (clj)** | Outil CLI officiel |
| **Leiningen** | Outil de projet classique |
| **deps.edn** | Gestion des dépendances |
| **Babachka** | Scripts Clojure rapides |
| **outils.build** | Construire l'automatisation |
| **shadow-cljs** | Constructions ClojureScript |
| **Roue de figure** | Rechargement ClojureScript en direct |
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

## Outils Lisp communs
| Outil | Objectif |
|------|--------------|
| **Quicklisp** | Gestionnaire de paquets |
| **ASDF** | Système de construction |
| **Roswell** | Gestionnaire d'environnement Lisp |
| **QLot** | Gestion des dépendances locales |
| **SLIME** | Emacs Lisp IDE |
| **Sournois** | Emacs Lisp IDE (fourchette SLIME) |
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

## Cadres Web
| Cadre | Langue | Tapez |
|-----------|----------|------|
| **Bague + Compojure** | Clojure | Gestionnaire HTTP + routage |
| **Piédestal** | Clojure | Web complet |
| **Luminus** | Clojure | Pile de framework Web |
| ** Réitit ** | Clojure | Bibliothèque de routage |
| **Hunchentoot** | CL | Serveur HTTP |
| **Homme des cavernes** | CL | Cadre Web |
| **Restas** | CL | Cadre REST |
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

## Base de données
| Technologie | Langue | Tapez |
|------------|----------|------|
| **suivant.jdbc** | Clojure | Encapsuleur JDBC |
| **HugSQL** | Clojure | SQL d'abord |
| **mielsql** | Clojure | SQLDSL |
| **clojure.jdbc** | Clojure | Interface JDBC |
| **Postmoderne** | CL | PostgreSQL |
| **CLSQL** | CL | Interface SQL |
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

## Tests
| Cadre | Langue | Objectif |
|-----------|----------|---------|
| **clojure.test** | Clojure | Tests intégrés |
| **mi-je** | Clojure | Tests de style BDD |
| **attentes** | Clojure | Basé sur les attentes |
| **test.check** | Clojure | Basé sur la propriété (QuickCheck) |
| **CinqAM** | CL | Tests unitaires |
| **prouver** | CL | Cadre de test |
| **unité lisp** | CL | Tests unitaires |
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

## Qualité du code
| Outil | Langue | Objectif |
|------|----------|---------|
| **clj-kondo** | Clojure | Linter |
| **cljfmt** | Clojure | Formateur |
| **bois d'est** | Clojure | Peluche |
| **kibit** | Clojure | Suggestions de codes |
| **alex-et-terrys** | Clojure | Guide de style |
| **alex-plus** | CL | Analyse de codes |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## Bibliothèques clés
| Bibliothèque | Langue | Objectif |
|---------|----------|---------|
| **core.async** | Clojure | Concurrence CSP |
| **transducteurs** | Clojure | Algorithmes composables |
| **spectre** | Clojure | Navigation des données |
| **schéma** | Clojure | Validation des données |
| **malli** | Clojure | Validation des données |
| **data.json** | Clojure | JSON |
| **Cheshire** | Clojure | JSON (plus rapide) |
| **hoquet** | Clojure | Génération HTML |
| **recadrer** | ClojureScript | Cadre SPA |
| **réactif** | ClojureScript | Wrapper de réaction |
| **Oh** | ClojureScript | Interface de réaction |
| **core.match** | Clojure | Correspondance de motifs |
| **tools.logging** | Clojure | Journalisation |
| **monter** | Clojure | Gestion de l'État |
| **intégrant** | Clojure | Système de composants |
| **usocket** | CL | Bibliothèque de sockets |
| **fils-bordeaux** | CL | Enfilage |
| **alexandrie** | CL | Bibliothèque utilitaire |
---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **Code VS + Calva** | Meilleur EDI Clojure |
| **CIDRE (Emacs)** | IDE Clojure classique |
| **IntelliJ + Cursive** | JetBrains Clojure |
| **SLIME / Sournois** | Lisp commun (Emacs) |
| **Lem** | IDE Common Lisp |
| **Vim + Cheminée** | Vim Clojure |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Uberjar** | `clj -T:build jar`(Clojure) |
| **GraalVM natif** | Image native (limitée) |
| **Docker** | Conteneurisé |
| **Babachka** | Scripts rapides |
| **Binaire Lisp** | Binaire compilé (SBCL) |
| **Kubernetes** | Orchestration |
---

## Résumé
L'écosystème Lisp couvre plusieurs dialectes : **Clojure** (JVM, moderne), **Common Lisp** (classique, ANSI), **Racket** (orienté langage) et **Emacs Lisp** (script d'éditeur). La pile standard de Clojure est : **Clojure CLI** avec **deps.edn** pour les builds, **Ring + Compojure** ou **Pedestal** pour le Web, **next.jdbc** pour les bases de données, **clojure.test** pour les tests, **clj-kondo** pour le peluchage et **VS Code + Calva** ou **CIDER** comme IDE. Common Lisp utilise **Quicklisp** pour les packages, **SBCL** pour la compilation et **SLIME** pour le développement. Les points forts de Lisp sont les macros, l'homoïconicité, le développement piloté par REPL et la programmation interactive. L'écosystème excelle dans le prototypage rapide, les langages spécifiques à un domaine et le traitement des données.