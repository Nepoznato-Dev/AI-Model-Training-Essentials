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
# Lisp & Clojure: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema Lisp y Clojure.
---

## Implementaciones de Lisp y Clojure
| Implementación | Idioma | Notas |
|---------------|----------|-------|
| **Clojure** | JVM | Lisp moderno en la JVM |
| **ClojureScript** | JS | Clojure compilado en JavaScript |
| **SBCL** | Ceceo común | CL de alto rendimiento |
| **CCL** | Ceceo común | OpenMCL, compilación rápida |
| **ECL** | Ceceo común | Integrable, interoperabilidad C |
| **Emacs Lisp** | Emacs | Idioma de extensión |
| **Raqueta** | Esquema | Programación orientada al lenguaje |
| **Astucia** | Esquema | Lenguaje de extensión GNU |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Herramientas Clojure
| Herramienta | Propósito |
|------|---------|
| **Clojure CLI (clj)** | Herramienta CLI oficial |
| **Leiningen** | Herramienta de proyecto clásica |
| **deps.edn** | Gestión de dependencia |
| **Babashka** | Secuencias de comandos rápidas de Clojure |
| **herramientas.build** | Automatización de construcciones |
| **sombra-cljs** | Construcciones de ClojureScript |
| **Rueda de higo** | Recarga de ClojureScript en vivo |
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

## Herramientas Lisp comunes
| Herramienta | Propósito |
|------|---------|
| **Lectura rápida** | Administrador de paquetes |
| **ASDF** | Sistema de construcción |
| **Roswell** | Gerente de entorno Lisp |
| **QLote** | Gestión de dependencia local |
| **SLIMO** | IDE de Emacs Lisp |
| **Astuto** | Emacs Lisp IDE (bifurcación SLIME) |
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

## Marcos web
| Marco | Idioma | Tipo |
|-----------|----------|------|
| **Anillo + Compojure** | Clojure | Controlador HTTP + enrutamiento |
| **Pedestal** | Clojure | Web de pila completa |
| **Lumino** | Clojure | Pila de marco web |
| **Reiniciar** | Clojure | Biblioteca de enrutamiento |
| **Hunchentoot** | CL | Servidor HTTP |
| **Cavernícola** | CL | Marco web |
| **Restas** | CL | Marco DESCANSO |
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

## Base de datos
| Tecnología | Idioma | Tipo |
|------------|----------|------|
| **siguiente.jdbc** | Clojure | Envoltorio JDBC |
| **AbrazoSQL** | Clojure | SQL primero |
| **mielsql** | Clojure | DSL SQL |
| **clojure.jdbc** | Clojure | Interfaz JDBC |
| **Posmoderno** | CL | PostgreSQL |
| **CLSQL** | CL | Interfaz SQL |
| **SxQL** | CL | DSL SQL |
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

## Pruebas
| Marco | Idioma | Propósito |
|-----------|----------|---------|
| **prueba.clojure** | Clojure | Pruebas integradas |
| **midje** | Clojure | Pruebas estilo BDD |
| **expectativas** | Clojure | Basado en expectativas |
| **prueba.comprobar** | Clojure | Basado en propiedad (QuickCheck) |
| **Cinco a.m.** | CL | Pruebas unitarias |
| **probar** | CL | Marco de pruebas |
| **unidad ceceo** | CL | Pruebas unitarias |
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

## Calidad del código
| Herramienta | Idioma | Propósito |
|------|----------|---------|
| **clj-kondo** | Clojure | Linter |
| **cljfmt** | Clojure | Formateador |
| ** madera del este ** | Clojure | pelusa |
| **kibit** | Clojure | Sugerencias de código |
| **alex-y-terrys** | Clojure | Guía de estilo |
| **alex-plus** | CL | Análisis de código |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## Bibliotecas clave
| Biblioteca | Idioma | Propósito |
|---------|----------|---------|
| **núcleo.async** | Clojure | Simultaneidad de CSP |
| **transductores** | Clojure | Algoritmos componibles |
| **espectro** | Clojure | Navegación de datos |
| **esquema** | Clojure | Validación de datos |
| **malli** | Clojure | Validación de datos |
| **datos.json** | Clojure | JSON |
| **cheshire** | Clojure | JSON (más rápido) |
| **hipo** | Clojure | Generación HTML |
| **reencuadrar** | ClojureScript | Marco SPA |
| **reactivo** | ClojureScript | Reaccionar contenedor |
| **Om** | ClojureScript | Interfaz de reacción |
| **core.match** | Clojure | Coincidencia de patrones |
| **herramientas.registro** | Clojure | Registro |
| **montar** | Clojure | Gestión estatal |
| **integrante** | Clojure | Sistema de componentes |
| **usocket** | CL | Biblioteca de sockets |
| **hilos-burdeos** | CL | Enhebrado |
| **alejandría** | CL | Biblioteca de utilidades |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Código VS + Calva** | Mejor IDE de Clojure |
| **SIDRA (Emacs)** | IDE clásico de Clojure |
| **IntelliJ + Cursiva** | Clojure de JetBrains |
| **SLIME / Astuto** | Lisp común (Emacs) |
| **Lem** | IDE Lisp común |
| **Vim + Chimenea** | Vim Clojure |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Uberjar** | `clj -T:build jar`(Clojure) |
| **GraalVM Nativo** | Imagen nativa (limitada) |
| **Acoplador** | En contenedores |
| **Babashka** | Secuencias de comandos rápidas |
| **Ceceo binario** | Binario compilado (SBCL) |
| **Kubernetes** | Orquestación |
---

## Resumen
El ecosistema Lisp abarca múltiples dialectos: **Clojure** (JVM, moderno), **Common Lisp** (clásico, ANSI), **Racket** (orientado al lenguaje) y **Emacs Lisp** (scripting de editor). La pila estándar de Clojure es: **Clojure CLI** con **deps.edn** para compilaciones, **Ring + Compojure** o **Pedestal** para web, **next.jdbc** para bases de datos, **clojure.test** para pruebas, **clj-kondo** para linting y **VS Code + Calva** o **CIDER** como IDE. Common Lisp usa **Quicklisp** para paquetes, **SBCL** para compilación y **SLIME** para desarrollo. Los puntos fuertes de Lisp son las macros, la homoiconicidad, el desarrollo impulsado por REPL y la programación interactiva. El ecosistema se destaca en la creación rápida de prototipos, lenguajes de dominios específicos y procesamiento de datos.