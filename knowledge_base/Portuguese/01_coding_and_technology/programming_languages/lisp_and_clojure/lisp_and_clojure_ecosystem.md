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
# Lisp & Clojure – Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais do ecossistema Lisp e Clojure.
---

## Implementações Lisp e Clojure
| Implementação | Idioma | Notas |
|---------------|----------|-------|
| **Clojure** | JVM | Lisp moderno na JVM |
| **ClojureScript** | JS | Clojure compilado para JavaScript |
| **SBCL** | Lisp comum | CL de alto desempenho |
| **CCL** | Lisp comum | OpenMCL, compilação rápida |
| **ECL** | Lisp comum | Incorporável, interoperabilidade C |
| **Emacs Lisp** | Emacs | Idioma de extensão |
| **Raquete** | Esquema | Programação orientada a linguagem |
| **Guil** | Esquema | Linguagem de extensão GNU |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Ferramentas Clojure
| Ferramenta | Finalidade |
|------|---------|
| **Cllojure CLI (clj)** | Ferramenta CLI oficial |
| **Leiningen** | Ferramenta de projeto clássica |
| **deps.edn** | Gestão de dependências |
| **Babashka** | Script Clojure rápido |
| **ferramentas.build** | Automação de construção |
| **shadow-cljs** | Compilações ClojureScript |
| **Roda de figueira** | Recarregamento ClojureScript ao vivo |
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

## Ferramentas Lisp Comuns
| Ferramenta | Finalidade |
|------|---------|
| **Quicklisp** | Gerenciador de pacotes |
| **ASDF** | Sistema de construção |
| **Roswell** | Gerenciador de ambiente Lisp |
| **QLote** | Gestão de dependências locais |
| **SLIME** | IDE Emacs Lisp |
| **Astuto** | Emacs Lisp IDE (garfo SLIME) |
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

## Estruturas Web
| Estrutura | Idioma | Tipo |
|-----------|----------|------|
| **Anel + Compojure** | Clojure | Manipulador HTTP + roteamento |
| **Pedestal** | Clojure | Web full-stack |
| **Luminoso** | Clojure | Pilha de estrutura da Web |
| **Reitit** | Clojure | Biblioteca de roteamento |
| **Hunchentoot** | CL | Servidor HTTP |
| **Homem das cavernas** | CL | Estrutura web |
| **Restauras** | CL | Estrutura REST |
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

## Banco de dados
| Tecnologia | Idioma | Tipo |
|------------|----------|------|
| **próximo.jdbc** | Clojure | Invólucro JDBC |
| **HugSQL** | Clojure | SQL primeiro |
| **honeysql** | Clojure | SQLDSL |
| **clojure.jdbc** | Clojure | Interface JDBC |
| **Pós-moderno** | CL | PostgreSQL |
| **CLSQL** | CL | InterfaceSQL |
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

## Teste
| Estrutura | Idioma | Finalidade |
|----------|----------|--------|
| **clojure.test** | Clojure | Testes integrados |
| **midje** | Clojure | Teste estilo BDD |
| **expectativas** | Clojure | Baseado em expectativas |
| **teste.verificação** | Clojure | Baseado em propriedade (QuickCheck) |
| **Cinco da manhã** | CL | Teste de unidade |
| **provar** | CL | Estrutura de teste |
| **unidade lisp** | CL | Teste de unidade |
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

## Qualidade do código
| Ferramenta | Idioma | Finalidade |
|------|----------|--------|
| **clj-kondo** | Clojure | Linter |
| **cljfmt** | Clojure | Formatador |
| **madeira leste** | Clojure | Linting |
| **kibit** | Clojure | Sugestões de código |
| **alex-e-terrys** | Clojure | Guia de estilo |
| **alex-mais** | CL | Análise de código |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## Bibliotecas principais
| Biblioteca | Idioma | Finalidade |
|--------|----------|---------|
| **núcleo.async** | Clojure | Simultaneidade CSP |
| **transdutores** | Clojure | Algoritmos combináveis ​​|
| **espectro** | Clojure | Navegação de dados |
| **esquema** | Clojure | Validação de dados |
| **malli** | Clojure | Validação de dados |
| **dados.json** | Clojure | JSON |
| **cheshire** | Clojure | JSON (mais rápido) |
| **soluço** | Clojure | Geração HTML |
| **reestruturar** | ClojureScript | Estrutura SPA |
| **reagente** | ClojureScript | Invólucro de reação |
| **Ah** | ClojureScript | Interface de reação |
| **core.match** | Clojure | Correspondência de padrões |
| **ferramentas.logging** | Clojure | Registro |
| **montar** | Clojure | Gestão do Estado |
| **integrante** | Clojure | Sistema de componentes |
| **usocket** | CL | Biblioteca de soquetes |
| **fios bordeaux** | CL | Rosqueamento |
| **Alexandria** | CL | Biblioteca de utilitários |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Código VS + Calva** | Melhor IDE Clojure |
| **CIDRA (Emacs)** | IDE Clojure Clássico |
| **IntelliJ + Cursivo** | Clojure JetBrains |
| **SLIME / Manhoso** | Lisp comum (Emacs) |
| **Lem** | IDE Lisp comum |
| **Vim + Lareira** | Vim Clojure |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Uberjar** | `clj -T:build jar`(Clojure) |
| **GraalVM nativo** | Imagem nativa (limitada) |
| **Docker** | Contentorizado |
| **Babashka** | Script rápido |
| **Lisp binário** | Binário compilado (SBCL) |
| **Kubernetes** | Orquestração |
---

## Resumo
O ecossistema Lisp abrange vários dialetos: **Clojure** (JVM, moderno), **Common Lisp** (clássico, ANSI), **Racket** (orientado à linguagem) e **Emacs Lisp** (editor de scripts). A pilha padrão do Clojure é: **Clojure CLI** com **deps.edn** para compilações, **Ring + Compojure** ou **Pedestal** para web, **next.jdbc** para bancos de dados, **clojure.test** para testes, **clj-kondo** para linting e **VS Code + Calva** ou **CIDER** como IDE. Common Lisp usa **Quicklisp** para pacotes, **SBCL** para compilação e **SLIME** para desenvolvimento. Os pontos fortes do Lisp são macros, homoiconicidade, desenvolvimento orientado por REPL e programação interativa. O ecossistema é excelente em prototipagem rápida, linguagens específicas de domínio e processamento de dados.