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
# Lisp & Clojure — Panduan Ekosistem & Perkakas
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Lisp dan Clojure.
---

## Implementasi Cadel & Clojure
| Implementasi | Bahasa | Catatan |
|---------------|----------|-------|
| **Clojure** | JVM | Lisp Modern di JVM |
| **Skrip Clojure** | JS | Clojure dikompilasi ke JavaScript |
| **SBCL** | Cadel Umum | CL berkinerja tinggi |
| **CCL** | Cadel Umum | OpenMCL, kompilasi cepat |
| **ECL** | Cadel Umum | Dapat disematkan, interop C |
| **Emacs Cacat** | Emacs | Bahasa ekstensi |
| **Raket** | Skema | Pemrograman berorientasi bahasa |
| **Tipu muslihat** | Skema | Bahasa ekstensi GNU |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Perkakas Clojure
| Alat | Tujuan |
|------|---------|
| **Clojure CLI (clj)** | Alat CLI resmi |
| **Leiningen** | Alat proyek klasik |
| **deps.edn** | Manajemen ketergantungan |
| **Babashka** | Skrip Clojure Cepat |
| **alat.membangun** | Bangun otomatisasi |
| **bayangan-cljs** | Pembuatan ClojureScript |
| **Roda Figur** | Pemuatan ulang ClojureScript langsung |
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

## Perkakas Cadel Umum
| Alat | Tujuan |
|------|---------|
| **Klik cepat** | Manajer paket |
| **ASDF** | Membangun sistem |
| **Roswell** | Manajer lingkungan cadel |
| **QLot** | Manajemen ketergantungan lokal |
| **LENDIR** | IDE Cacat Emacs |
| **Lici** | Emacs Lisp IDE (garpu SLIME) |
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

## Kerangka Web
| Kerangka | Bahasa | Ketik |
|-----------|----------|------|
| **Cincin + Kompojure** | Clojure | Penangan HTTP + perutean |
| **Alas** | Clojure | Web tumpukan penuh |
| **Luminus** | Clojure | Tumpukan kerangka web |
| ** Ulangi ** | Clojure | Perpustakaan perutean |
| **Hunchentoot** | kelas | Server HTTP |
| **Manusia Gua** | kelas | Kerangka web |
| **Resta** | kelas | Kerangka REST |
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

## Basis Data
| Teknologi | Bahasa | Ketik |
|------------|----------|------|
| **berikutnya.jdbc** | Clojure | Pembungkus JDBC |
| **HugSQL** | Clojure | SQL-pertama |
| **madusql** | Clojure | SQLDSL |
| **clojure.jdbc** | Clojure | Antarmuka JDBC |
| **Postmodern** | kelas | PostgreSQL |
| **CLSQL** | kelas | Antarmuka SQL |
| **SxQL** | kelas | SQLDSL |
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

## Pengujian
| Kerangka | Bahasa | Tujuan |
|-----------|----------|---------|
| **clojure.test** | Clojure | Pengujian bawaan |
| **tengah** | Clojure | Pengujian gaya BDD |
| **harapan** | Clojure | Berbasis harapan |
| **tes.periksa** | Clojure | Berbasis properti (QuickCheck) |
| **Lima pagi** | kelas | Pengujian satuan |
| **buktikan** | kelas | Kerangka pengujian |
| **unit cadel** | kelas | Pengujian satuan |
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

## Kualitas Kode
| Alat | Bahasa | Tujuan |
|------|----------|---------|
| **clj-kondo** | Clojure | Linter |
| **cljfmt** | Clojure | Pemformat |
| **kayu timur** | Clojure | Linting |
| **kibit** | Clojure | Saran kode |
| **alex-dan-terry** | Clojure | Panduan gaya |
| **alex-plus** | kelas | Analisis kode |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## Perpustakaan Utama
| Perpustakaan | Bahasa | Tujuan |
|---------|----------|---------|
| **inti.async** | Clojure | Konkurensi CSP |
| **transduser** | Clojure | Algoritma yang dapat disusun |
| **hantu** | Clojure | Navigasi data |
| **skema** | Clojure | Validasi data |
| **malli** | Clojure | Validasi data |
| **data.json** | Clojure | JSON |
| **cheshire** | Clojure | JSON (lebih cepat) |
| **cegukan** | Clojure | generasi HTML |
| **bingkai ulang** | Skrip Clojure | Kerangka SPA |
| **reagen** | Skrip Clojure | Pembungkus reaksi |
| **Om** | Skrip Clojure | Antarmuka reaksi |
| **inti.pertandingan** | Clojure | Pencocokan pola |
| **alat.logging** | Clojure | Pencatatan |
| **gunung** | Clojure | Pengelolaan negara |
| **integran** | Clojure | Sistem komponen |
| **usocket** | kelas | Perpustakaan soket |
| **benang bordeaux** | kelas | Mengulir |
| **aleksandria** | kelas | Perpustakaan utilitas |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS + Calva** | IDE Clojure Terbaik |
| **CIDER (Emacs)** | IDE Clojure Klasik |
| **IntelliJ + Kursif** | Clojure JetBrains |
| **LENDIR / Licik** | Cadel Umum (Emacs) |
| **Lem** | IDE Cadel Umum |
| **Vim + Perapian** | Vim Clojure |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Uberjar** | `clj -T:build jar`(Clojure) |
| **GraalVM Asli** | Gambar asli (terbatas) |
| **Buruh pelabuhan** | dalam kontainer |
| **Babashka** | Skrip cepat |
| **Cadel biner** | Biner terkompilasi (SBCL) |
| **Kubernetes** | Orkestrasi |
---

## Ringkasan
Ekosistem Lisp mencakup beberapa dialek: **Clojure** (JVM, modern), **Common Lisp** (klasik, ANSI), **Racket** (berorientasi bahasa), dan **Emacs Lisp** (skrip editor). Tumpukan standar Clojure adalah: **Clojure CLI** dengan **deps.edn** untuk build, **Ring + Compojure** atau **Pedestal** untuk web, **next.jdbc** untuk database, **clojure.test** untuk pengujian, **clj-kondo** untuk linting, dan **VS Code + Calva** atau **CIDER** sebagai IDE. Common Lisp menggunakan **Quicklisp** untuk paket, **SBCL** untuk kompilasi, dan **SLIME** untuk pengembangan. Kekuatan Lisp adalah makro, homoikonisitas, pengembangan berbasis REPL, dan pemrograman interaktif. Ekosistem ini unggul dalam pembuatan prototipe cepat, bahasa khusus domain, dan pemrosesan data.