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
# Lisp & Clojure — ایکو سسٹم اور ٹولنگ گائیڈ
اس گائیڈ میں Lisp اور Clojure ایکو سسٹم میں ضروری ٹولز، فریم ورک، اور انفراسٹرکچر کا احاطہ کیا گیا ہے۔
---

## Lisp & Clojure نفاذ
| نفاذ | زبان | نوٹس |
|---------------|---------|---------|
| **کلجور** | JVM | JVM پر جدید لِسپ |
| **ClojureScript** | جے ایس | Clojure جاوا اسکرپٹ پر مرتب کیا گیا |
| **SBCL** | کامن لِسپ | اعلی کارکردگی CL |
| **CCL** | کامن لِسپ | اوپن ایم سی ایل، تیز تالیف |
| **ECL** | کامن لِسپ | ایمبیڈ ایبل، سی انٹراپ |
| **Emacs Lisp** | ایماکس | توسیعی زبان |
| **ریکیٹ** | سکیم | زبان پر مبنی پروگرامنگ |
| **گائل** | سکیم | GNU توسیعی زبان |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## کلوجر ٹولنگ
| ٹول | مقصد |
|------|---------|
| **کلوجور CLI (clj)** | سرکاری CLI ٹول |
| **لیننگن** | کلاسک پروجیکٹ ٹول |
| **deps.edn** | انحصار کا انتظام |
| **بابشکا** | فاسٹ کلوجور اسکرپٹنگ |
| **tools.build** | آٹومیشن بنائیں |
| **shadow-cljs** | ClojureScript بناتا ہے |
| **فگ وہیل** | لائیو ClojureScript دوبارہ لوڈنگ |
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

## کامن لِسپ ٹولنگ
| ٹول | مقصد |
|------|---------|
| **کوئیکلسپ** | پیکیج مینیجر |
| **ASDF** | نظام کی تعمیر |
| **روز ویل** | Lisp ماحول کے مینیجر |
| **QLot** | مقامی انحصار کا انتظام |
| **کیچڑ** | Emacs Lisp IDE |
| ** چالاک** | Emacs Lisp IDE (SLIME fork) |
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

## ویب فریم ورک
| فریم ورک | زبان | قسم |
|------------|----------|------|
| **رنگ + کمپوزور** | Clojure | HTTP ہینڈلر + روٹنگ |
| **پیڈسٹل** | Clojure | مکمل اسٹیک ویب |
| **Luminus** | Clojure | ویب فریم ورک اسٹیک |
| ** Reitit** | Clojure | روٹنگ لائبریری |
| **ہنچنٹوٹ** | سی ایل | HTTP سرور |
| **غار والا** | سی ایل | ویب فریم ورک |
| **ریسٹاس** | سی ایل | REST فریم ورک |
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

## ڈیٹا بیس
| ٹیکنالوجی | زبان | قسم |
|------------|------------|------|
| **اگلا.jdbc** | Clojure | JDBC ریپر |
| **HugSQL** | Clojure | SQL-پہلے |
| **honeysql** | Clojure | SQL DSL |
| **clojure.jdbc** | Clojure | JDBC انٹرفیس |
| **پوسٹ ماڈرن** | سی ایل | PostgreSQL |
| **CLSQL** | سی ایل | ایس کیو ایل انٹرفیس |
| **SxQL** | سی ایل | SQL DSL |
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

## ٹیسٹنگ
| فریم ورک | زبان | مقصد |
|------------|---------|---------|
| **clojure.test** | Clojure | بلٹ ان ٹیسٹنگ |
| **مڈجے** | Clojure | BDD طرز کی جانچ |
| **توقعات** | Clojure | توقعات پر مبنی |
| ** test.check** | Clojure | پراپرٹی پر مبنی (QuickCheck) |
| **FiveAM** | سی ایل | یونٹ ٹیسٹنگ |
| **ثابت کریں** | سی ایل | جانچ کا فریم ورک |
| **لِسپ یونٹ** | سی ایل | یونٹ ٹیسٹنگ |
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

## کوڈ کا معیار
| ٹول | زبان | مقصد |
|------|------------|---------|
| **clj-kondo** | Clojure | لنٹر |
| **cljfmt** | Clojure | فارمیٹر |
| ** ایسٹ ووڈ** | Clojure | لنٹنگ |
| **کبٹ** | Clojure | کوڈ کی تجاویز |
| **الیکس اور ٹیریس** | Clojure | انداز گائیڈ |
| **ایلیکس پلس** | سی ایل | کوڈ کا تجزیہ |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## کلیدی لائبریریاں
| لائبریری | زبان | مقصد |
|---------|------------|---------|
| **core.async** | Clojure | CSP کنکرنسی |
| **ٹرانسڈیوسرز** | Clojure | کمپوز ایبل الگورتھم |
| ** تماشہ** | Clojure | ڈیٹا نیویگیشن |
| **سکیمہ** | Clojure | ڈیٹا کی توثیق |
| **مالی** | Clojure | ڈیٹا کی توثیق |
| **data.json** | Clojure | JSON |
| **چیشائر** | Clojure | JSON (تیز) |
| **ہچکی** | Clojure | HTML نسل |
| **ری فریم** | ClojureScript | SPA فریم ورک |
| **ریجنٹ** | ClojureScript | ری ایکٹ ریپر |
| **اوم** | ClojureScript | رد عمل کا انٹرفیس |
| **core.match** | Clojure | پیٹرن ملاپ |
| **tools.logging** | Clojure | لاگنگ |
| **ماؤنٹ** | Clojure | ریاستی انتظام |
| **انٹیگرنٹ** | Clojure | اجزاء کا نظام |
| **usocket** | سی ایل | ساکٹ لائبریری |
| **بورڈو تھریڈز** | سی ایل | تھریڈنگ |
| **الیگزینڈریا** | سی ایل | یوٹیلیٹی لائبریری |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **VS کوڈ + کالوا** | بہترین Clojure IDE |
| **سائیڈر (ایماکس)** | کلاسیکی Clojure IDE |
| **انٹیلی جے + کرسیو** | JetBrains Clojure |
| ** کیچڑ / چال ** | کامن لِسپ (ایماکس) |
| **لیم** | کامن لِسپ IDE |
| **Vim + چمنی** | Vim Clojure |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **Uberjar** | `clj -T:build jar`(کلوجور) |
| **GraalVM مقامی** | مقامی تصویر (محدود) |
| **ڈوکر** | کنٹینرائزڈ |
| **بابشکا** | تیز اسکرپٹنگ |
| **لِسپ بائنری** | مرتب شدہ بائنری (SBCL) |
| **Kubernetes** | آرکیسٹریشن |
---

## خلاصہ
Lisp ماحولیاتی نظام متعدد بولیوں پر محیط ہے: **Clojure** (JVM، جدید)، **Common Lisp** (کلاسک، ANSI)، **ریکیٹ** (زبان پر مبنی) اور **Emacs Lisp** (ایڈیٹر اسکرپٹنگ)۔ Clojure کا معیاری اسٹیک یہ ہے: **Clojure CLI** کے ساتھ **deps.edn** کے لیے تعمیرات، **Ring + Compojure** یا **Pedestal** برائے ویب، **next.jdbc** ڈیٹا بیس کے لیے، **clojure.test** ٹیسٹنگ کے لیے، **clj-kondo** linting کے لیے، **Clj-kondo** ID** کے طور پر، اور Calde** CI** Common Lisp پیکجز کے لیے **Quicklisp**، تالیف کے لیے **SBCL**، اور **SLIME** کو ترقی کے لیے استعمال کرتا ہے۔ لِسپ کی طاقتیں میکروز، ہوموکونیسیٹی، REPL سے چلنے والی ترقی، اور انٹرایکٹو پروگرامنگ ہیں۔ ماحولیاتی نظام تیز رفتار پروٹو ٹائپنگ، ڈومین کے لیے مخصوص زبانوں، اور ڈیٹا پروسیسنگ میں سبقت لے جاتا ہے۔