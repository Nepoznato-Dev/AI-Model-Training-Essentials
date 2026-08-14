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
# Lisp & Clojure - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم Lisp و Clojure را پوشش می‌دهد.
---

## پیاده سازی Lisp & Clojure
| پیاده سازی | زبان | یادداشت ها |
|---------------|---------|-------|
| **کلاژور** | JVM | Lisp مدرن در JVM |
| **ClojureScript** | JS | Clojure به جاوا اسکریپت کامپایل شد |
| **SBCL** | لب معمولی | CL با کارایی بالا |
| **CCL** | لب معمولی | OpenMCL، کامپایل سریع |
| **ECL** | لب معمولی | Embeddable، C interop |
| **Emacs Lisp** | ایمکس | زبان پسوند |
| **راکت** | طرح | برنامه نویسی زبان محور |
| **حیله** | طرح | زبان برنامه افزودنی گنو |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Clojure Tooling
| ابزار | هدف |
|------|---------|
| **Clojure CLI (clj)** | ابزار رسمی CLI |
| **لینینگن** | ابزار پروژه کلاسیک |
| **deps.edn** | مدیریت وابستگی |
| **باباشکا** | برنامه نویسی سریع Clojure |
| **tools.build** | اتوماسیون ساخت |
| **shadow-cljs** | ساخت ClojureScript |
| **چرخ فیگور** | بارگذاری مجدد ClojureScript زنده |
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
| ابزار | هدف |
|------|---------|
| **Quicklisp** | مدیر بسته |
| **ASDF** | ساخت سیستم |
| **روزول** | مدیر محیط Lisp |
| **QLot** | مدیریت وابستگی محلی |
| **اسلایم** | Emacs Lisp IDE |
| **حیله گر** | Emacs Lisp IDE (چنگال SLIME) |
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

## چارچوب های وب
| چارچوب | زبان | نوع |
|-----------|----------|------|
| **حلقه + ترکیب** | کلوژور | کنترل کننده HTTP + مسیریابی |
| **پایه** | کلوژور | وب تمام پشته |
| **لومینوس** | کلوژور | پشته چارچوب وب |
| ** ریتیت** | کلوژور | کتابخانه مسیریابی |
| **Hunchentoot** | CL | سرور HTTP |
| **غارنشین** | CL | چارچوب وب |
| **رستاس** | CL | چارچوب REST |
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

## پایگاه داده
| فناوری | زبان | نوع |
|------------|----------|------|
| **next.jdbc** | کلوژور | بسته بندی JDBC |
| **HugSQL** | کلوژور | SQL-first |
| **honeysql** | کلوژور | SQL DSL |
| **clojure.jdbc** | کلوژور | رابط JDBC |
| **پست مدرن** | CL | PostgreSQL |
| **CLSQL** | CL | رابط SQL |
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

## تست
| چارچوب | زبان | هدف |
|-----------|----------|---------|
| **clojure.test** | کلوژور | تست داخلی |
| **میدجه** | کلوژور | تست سبک BDD |
| **انتظارات** | کلوژور | مبتنی بر انتظار |
| **تست.بررسی** | کلوژور | مبتنی بر اموال (QuickCheck) |
| **FiveAM** | CL | تست واحد |
| **اثبات** | CL | چارچوب تست |
| **lisp-unit** | CL | تست واحد |
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

## کیفیت کد
| ابزار | زبان | هدف |
|------|----------|---------|
| **clj-kondo** | کلوژور | لینتر |
| **cljfmt** | کلوژور | فرمت کننده |
| **ایست وود** | کلوژور | پرز زدن |
| **کیبیت** | کلوژور | پیشنهادات کد |
| **الکس اند تری** | کلوژور | راهنمای سبک |
| **alex-plus** | CL | تحلیل کد |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## کتابخانه های کلیدی
| کتابخانه | زبان | هدف |
|---------|----------|---------|
| **core.async** | کلوژور | همزمانی CSP |
| **مبدل** | کلوژور | الگوریتم های قابل ترکیب |
| **شبح** | کلوژور | ناوبری داده |
| **طرحواره** | کلوژور | اعتبار سنجی داده ها |
| **مالی** | کلوژور | اعتبار سنجی داده ها |
| **data.json** | کلوژور | JSON |
| **چشایر** | کلوژور | JSON (سریعتر) |
| **سکسکه** | کلوژور | تولید HTML |
| **فراب مجدد** | ClojureScript | چارچوب SPA |
| **معرف** | ClojureScript | React wrapper |
| **ام** | ClojureScript | رابط React |
| **core.match** | کلوژور | تطبیق الگو |
| **tools.logging** | کلوژور | ورود به سیستم |
| **mount** | کلوژور | مدیریت دولتی |
| **یکپارچه** | کلوژور | سیستم کامپوننت |
| **usocket** | CL | کتابخانه سوکت |
| ** bordeaux-threads ** | CL | نخ زنی |
| **اسکندری** | CL | کتابخانه ابزار |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + Calva** | بهترین Clojure IDE |
| **CIDER (Emacs)** | کلاسیک Clojure IDE |
| **IntelliJ + شکسته** | JetBrains Clojure |
| **SLIME / Sly** | Common Lisp (Emacs) |
| **لم** | Common Lisp IDE |
| **Vim + شومینه** | Vim Clojure |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **اوبرجار** | `clj -T:build jar`(کلوژور) |
| **GraalVM Native** | تصویر بومی (محدود) |
| **داکر** | کانتینری |
| **باباشکا** | اسکریپت نویسی سریع |
| **باینری Lisp** | باینری کامپایل شده (SBCL) |
| **Kubernetes** | ارکستراسیون |
---

## خلاصه
اکوسیستم Lisp چندین گویش را در بر می گیرد: **Clojure** (JVM، مدرن)، **Common Lisp** (کلاسیک، ANSI)، **راکت** (زبان محور)، و **Emacs Lisp** (ویرایشگر اسکریپت). پشته استاندارد Clojure عبارت است از: **Clojure CLI** با **deps.edn** برای بیلدها، **Ring + Compojure** یا **Pedestal** برای وب، **next.jdbc** برای پایگاه‌های داده، **clojure.test** برای آزمایش، **clj-kondo****** برای linting، و **Calva به عنوان +CI یا کد V** Common Lisp از **Quicklisp** برای بسته ها، **SBCL** برای کامپایل و **SLIME** برای توسعه استفاده می کند. نقاط قوت Lisp عبارتند از: ماکروها، homoiconicity، توسعه مبتنی بر REPL و برنامه نویسی تعاملی. این اکوسیستم در نمونه سازی سریع، زبان های دامنه خاص و پردازش داده ها برتری دارد.