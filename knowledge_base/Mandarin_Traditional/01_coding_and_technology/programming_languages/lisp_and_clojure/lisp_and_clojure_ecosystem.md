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

# Lisp 和 Clojure — 生態系和工具指南
本指南涵蓋了 Lisp 和 Clojure 生態系統中的基本工具、框架和基礎設施。
---

## Lisp 和 Clojure 實現
|實作 |語言 |筆記|
|----------------|----------|--------|
| **Clojure** | JVM | JVM 上的現代 Lisp |
| **ClojureScript** | JS | Clojure 編譯為 JavaScript |
| **SBCL** |通用 Lisp |高性能CL |
| **覆銅板** |通用 Lisp | OpenMCL，快速編譯 |
| **ECL** |通用 Lisp |可嵌入、C 互通 |
| **Emacs Lisp** | Emacs |擴充語言 |
| **球拍** |方案|語言導向的程式設計|
| **詭計** |方案| GNU 擴充語言 |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Clojure 工具
|工具|目的|
|------|---------|
| **Clojure CLI (clj)** |官方 CLI 工具 |
| **萊寧根** |經典項目工具|
| **deps.edn** |依賴管理 |
| **巴巴什卡** |快速 Clojure 腳本 |
| **工具.build** |建立自動化|
| **shadow-cljs** | ClojureScript 建置 |
| **圖輪** |即時 ClojureScript 重新加載 |
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

## 通用 Lisp 工具
|工具|目的|
|------|---------|
| **Quicklisp** |套件管理器 |
| **航空自衛隊** |建構系統|
| **羅斯威爾** | Lisp 環境管理器 |
| **QLot** |本地依賴管理|
| **史萊姆** | Emacs Lisp IDE |
| **狡猾** | Emacs Lisp IDE（SLIME 分支）|
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

## 網路框架
|框架|語言 |類型 |
|------------|----------|------|
| **環 + Compojure** | Clojure | HTTP 處理程序 + 路由 |
| **底座** | Clojure |全端網路 |
| **發光** | Clojure | Web 框架堆疊 |
| ** 重新投資** | Clojure |路由庫 |
| **亨肯圖特** | CL | HTTP 伺服器 |
| **穴居人** | CL |網頁架構|
| **餐廳** | CL | REST框架|
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

## 資料庫
|技術 |語言 |類型 |
|------------|----------|------|
| **下一個.jdbc** | Clojure | JDBC 包裝器 |
| **HugSQL** | Clojure | SQL 優先 |
| **honeysql** | Clojure | SQL DSL |
| **clojure.jdbc** | Clojure | JDBC介面|
| **後現代** | CL | PostgreSQL |
| **CLSQL** | CL | SQL介面|
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

## 測試
|框架|語言 |目的|
|------------|----------|---------|
| **clojure.測試** | Clojure |內建測試|
| **米傑** | Clojure | BDD 式測試 |
| **期望** | Clojure |基於期望 |
| **測試.檢查** | Clojure |基於財產（快速檢查）|
| **上午五點** | CL |單元測試 |
| **證明** | CL |測試框架|
| **lisp 單元** | CL |單元測試 |
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

## 程式碼品質
|工具|語言 |目的|
|------|----------|---------|
| **clj-近藤** | Clojure |短絨 |
| **cljfmt** | Clojure |格式化程式|
| **伊斯特伍德** | Clojure |絨毛 |
| **千位元** | Clojure |程式碼建議 |
| **亞歷克斯和特里** | Clojure |風格指南 |
| **亞歷克斯加** | CL |代碼分析 |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## 關鍵庫
|圖書館 |語言 |目的|
|---------|----------|---------|
| **核心.async** | Clojure | CSP 並發 |
| **換能器** | Clojure |可組合演算法 |
| **幽靈** | Clojure |資料導航|
| **架構** | Clojure |資料驗證|
| **馬利** | Clojure |資料驗證|
| **資料.json** | Clojure | JSON |
| **柴郡** | Clojure | JSON（更快）|
| **打嗝** | Clojure | HTML 產生 |
| **重新建置** | Clojure 腳本 | SPA框架|
| **試劑** | Clojure 腳本 |反應包裝器 |
| **唵** | Clojure 腳本 |反應介面 |
| **核心.匹配** | Clojure |模式匹配|
| **工具.logging** | Clojure |記錄 |
| **安裝** | Clojure |狀態管理|
| **積分** | Clojure |元件系統 |
| **usocket** | CL |套接字庫 |
| **波爾多線** | CL |線程 |
| **亞歷山大** | CL |實用程式庫|
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS Code + Calva** |最佳 Clojure IDE |
| **CIDER (Emacs)** |經典 Clojure IDE |
| **IntelliJ + 草寫** | JetBrains Clojure | JetBrains Clojure |
| **史萊姆/狡猾** |通用 Lisp (Emacs) |
| **萊姆** | Common Lisp IDE |
| **Vim + 壁爐** | Vim Clojure | Vim Clojure | Vim Clojure
---

## 部署
|方法|筆記|
|--------|--------|
| **尤伯賈爾** | `clj -T:build jar`（Clojure）|
| **GraalVM Native** |原生鏡像（限量）|
| **碼頭工人** |貨櫃式|
| **巴巴什卡** |快速腳本編寫 |
| **Lisp 二進位** |已編譯的二進位檔案 (SBCL) |
| **Kubernetes** |編排|
---

＃＃ 概括
Lisp 生態系統涵蓋多種方言：**Clojure**（JVM、現代）、**Common Lisp**（經典、ANSI）、**Racket**（面向語言）和 **Emacs Lisp**（編輯器腳本）。 Clojure 的標準堆疊是：**Clojure CLI** 和 **deps.edn** 用於構建，**Ring + Compojure** 或 **Pedestal** 用於 Web，**next.jdbc** 用於數據庫，**clojure.test** 用於測試，**clj-kondo** 用於 linting，以及數據庫，** CoCI + Calva** IDE**。 Common Lisp 使用 **Quicklisp** 進行封裝，使用 **SBCL** 進行編譯，使用 **SLIME** 進行開發。 Lisp 的優點是巨集、同像性、REPL 驅動的開發和互動式程式設計。此生態系統擅長快速原型設計、特定領域語言和資料處理。