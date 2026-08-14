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
# Lisp & Clojure — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz Lisp ve Clojure ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Lisp ve Clojure Uygulamaları
| Uygulama | Dil | Notlar |
|---------------|----------|----------|
| **Kapanış** | JVM | JVM'de Modern Lisp |
| **ClojureScript** | JS | Clojure JavaScript'e derlendi |
| **SBCL** | Ortak Lisp | Yüksek performanslı CL |
| **CCL** | Ortak Lisp | OpenMCL, hızlı derleme |
| **ECL** | Ortak Lisp | Yerleştirilebilir, C ile birlikte çalışma |
| **Emacs Lisp** | Emac'lar | Uzantı dili |
| **Raket** | Şema | Dil odaklı programlama |
| **Guile** | Şema | GNU uzantı dili |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Clojure Aletleri
| Araç | Amaç |
|------|------------|
| **Clojure CLI (clj)** | Resmi CLI aracı |
| **Leiningen** | Klasik proje aracı |
| **deps.edn** | Bağımlılık yönetimi |
| **Babaşka** | Hızlı Clojure komut dosyası oluşturma |
| **tools.build** | Yapı otomasyonu |
| **gölge-cljs** | ClojureScript derlemeleri |
| **Şekil çarkı** | Canlı ClojureScript yeniden yükleniyor |
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

## Common Lisp Aracı
| Araç | Amaç |
|------|------------|
| **Quicklisp** | Paket yöneticisi |
| **ASDF** | Sistemi oluştur |
| **Roswell** | Lisp ortam yöneticisi |
| **QLot** | Yerel bağımlılık yönetimi |
| **SLIME** | Emacs Lisp IDE'si |
| **Sinsi** | Emacs Lisp IDE (SLIME çatalı) |
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

## Web Çerçeveleri
| Çerçeve | Dil | Tür |
|-----------|----------|------|
| **Yüzük + Kompoze** | Clojure | HTTP işleyicisi + yönlendirme |
| **Kaide** | Clojure | Tam yığın web |
| **Aydınlık** | Clojure | Web çerçevesi yığını |
| ** Tekrar** | Clojure | Yönlendirme kitaplığı |
| **Hunchentoot** | CL | HTTP sunucusu |
| **mağara adamı** | CL | Web çerçevesi |
| **Restalar** | CL | REST çerçevesi |
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

## Veritabanı
| Teknoloji | Dil | Tür |
|---------------|----------|------|
| **sonraki.jdbc** | Clojure | JDBC sarıcı |
| **SQL'e sarılın** | Clojure | SQL öncelikli |
| **balsql** | Clojure | SQL DSL |
| **clojure.jdbc** | Clojure | JDBC arayüzü |
| **Postmodern** | CL | PostgreSQL |
| **CLSQL** | CL | SQL arayüzü |
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

## Test etme
| Çerçeve | Dil | Amaç |
|-----------|----------|-----------|
| **clojure.test** | Clojure | Yerleşik test |
| **orta** | Clojure | BDD tarzı testler |
| **beklentiler** | Clojure | Beklenti bazlı |
| **test.check** | Clojure | Özellik tabanlı (HızlıKontrol) |
| **Sabah beşte** | CL | Birim testi |
| **kanıtla** | CL | Test çerçevesi |
| **lisp ünitesi** | CL | Birim testi |
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

## Kod Kalitesi
| Araç | Dil | Amaç |
|------|----------|-----------|
| **clj-kondo** | Clojure | Linter |
| **cljfmt** | Clojure | Biçimlendirici |
| **doğu ağacı** | Clojure | Linting |
| **kibit** | Clojure | Kod önerileri |
| **alex-ve-terrys** | Clojure | Stil kılavuzu |
| **alex-artı** | CL | Kod analizi |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## Anahtar Kitaplıklar
| Kütüphane | Dil | Amaç |
|-----------|----------|-----------|
| **core.async** | Clojure | CSP eşzamanlılığı |
| **dönüştürücüler** | Clojure | Şekillendirilebilir algoritmalar |
| **hayalet** | Clojure | Veri navigasyonu |
| **şema** | Clojure | Veri doğrulama |
| **mallı** | Clojure | Veri doğrulama |
| **data.json** | Clojure | JSON |
| **cheshire** | Clojure | JSON (daha hızlı) |
| **hıçkırık** | Clojure | HTML oluşturma |
| **yeniden çerçeveleme** | ClojureScript | SPA çerçevesi |
| **reaktif** | ClojureScript | Tepki sarmalayıcı |
| **Om** | ClojureScript | Tepki arayüzü |
| **core.match** | Clojure | Desen eşleştirme |
| **tools.logging** | Clojure | Günlük |
| **bağlama** | Clojure | Devlet yönetimi |
| **entegretör** | Clojure | Bileşen sistemi |
| **usocket** | CL | Soket kitaplığı |
| **bordo iplikleri** | CL | Diş Açma |
| **İskenderiye** | CL | Yardımcı program kitaplığı |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + Calva** | En İyi Clojure IDE |
| **CIDER (Emacs)** | Klasik Clojure IDE |
| **IntelliJ + Cursive** | JetBrains Kapatma |
| **SLIME / Sinsi** | Ortak Lisp (Emacs) |
| **Lem** | Ortak Lisp IDE |
| **Vim + Şömine** | Vim Clojure |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Uberjar** | `clj -T:build jar`(Kapalı) |
| **GraalVM Yerel** | Yerel resim (sınırlı) |
| **Docker** | Konteynerde |
| **Babaşka** | Hızlı komut dosyası oluşturma |
| **Lisp ikilisi** | Derlenmiş ikili dosya (SBCL) |
| **Kubernetes** | Orkestrasyon |
---

## Özet
Lisp ekosistemi birden fazla lehçeyi kapsar: **Clojure** (JVM, modern), **Common Lisp** (klasik, ANSI), **Racket** (dil odaklı) ve **Emacs Lisp** (düzenleyici komut dosyası oluşturma). Clojure'un standart yığını şöyledir: Derlemeler için **deps.edn** içeren **Clojure CLI**, web için **Ring + Compojure** veya **Pedestal**, veritabanları için **next.jdbc**, test için **clojure.test**, linting için **clj-kondo** ve IDE olarak **VS Code + Calva** veya **CIDER**. Common Lisp, paketler için **Quicklisp**, derleme için **SBCL** ve geliştirme için **SLIME** kullanır. Lisp'in güçlü yönleri makrolar, homoikoniklik, REPL odaklı geliştirme ve etkileşimli programlamadır. Ekosistem, hızlı prototip oluşturma, alana özgü diller ve veri işleme konularında öne çıkıyor.