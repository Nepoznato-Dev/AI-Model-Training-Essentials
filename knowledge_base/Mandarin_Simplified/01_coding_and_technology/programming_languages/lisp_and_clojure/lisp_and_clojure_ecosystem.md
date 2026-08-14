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
# Lisp 和 Clojure — 生态系统和工具指南
本指南涵盖了 Lisp 和 Clojure 生态系统中的基本工具、框架和基础设施。
---

## Lisp 和 Clojure 实现
|实施 |语言 |笔记|
|----------------|----------|--------|
| **Clojure** | JVM | JVM 上的现代 Lisp |
| **ClojureScript** | JS | Clojure 编译为 JavaScript |
| **SBCL** |通用 Lisp |高性能CL |
| **覆铜板** |通用 Lisp | OpenMCL，快速编译 |
| **ECL** |通用 Lisp |可嵌入、C 互操作 |
| **Emacs Lisp** | Emacs |扩展语言 |
| **球拍** |方案|面向语言的编程|
| **诡计** |方案| GNU 扩展语言 |
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
| **莱宁根** |经典项目工具|
| **deps.edn** |依赖管理 |
| **巴巴什卡** |快速 Clojure 脚本 |
| **工具.build** |构建自动化|
| **shadow-cljs** | ClojureScript 构建 |
| **图轮** |实时 ClojureScript 重新加载 |
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
| **Quicklisp** |包管理器 |
| **航空自卫队** |构建系统|
| **罗斯威尔** | Lisp 环境管理器 |
| **QLot** |本地依赖管理|
| **史莱姆** | Emacs Lisp IDE |
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

## 网络框架
|框架|语言 |类型 |
|------------|----------|------|
| **环 + Compojure** | Clojure | HTTP 处理程序 + 路由 |
| **底座** | Clojure |全栈网络 |
| **发光** | Clojure | Web 框架堆栈 |
| ** 重新投资** | Clojure |路由库 |
| **亨肯图特** | CL | HTTP 服务器 |
| **穴居人** | CL |网页框架|
| **餐厅** | CL | REST框架|
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

＃＃ 数据库
|技术 |语言 |类型 |
|------------|----------|------|
| **下一个.jdbc** | Clojure | JDBC 包装器 |
| **HugSQL** | Clojure | SQL 优先 |
| **honeysql** | Clojure | SQL DSL |
| **clojure.jdbc** | Clojure | JDBC接口|
| **后现代** | CL | PostgreSQL |
| **CLSQL** | CL | SQL接口|
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

## 测试
|框架|语言 |目的|
|------------|----------|---------|
| **clojure.测试** | Clojure |内置测试|
| **米杰** | Clojure | BDD 式测试 |
| **期望** | Clojure |基于期望 |
| **测试.检查** | Clojure |基于财产（快速检查）|
| **上午五点** | CL |单元测试|
| **证明** | CL |测试框架|
| **lisp 单元** | CL |单元测试 |
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

## 代码质量
|工具|语言 |目的|
|------|----------|---------|
| **clj-近藤** | Clojure |短绒 |
| **cljfmt** | Clojure |格式化程序|
| **伊斯特伍德** | Clojure |绒毛 |
| **千比特** | Clojure |代码建议 |
| **亚历克斯和特里** | Clojure |风格指南 |
| **亚历克斯加** | CL |代码分析 |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## 关键库
|图书馆 |语言 |目的|
|---------|----------|---------|
| **核心.async** | Clojure | CSP 并发 |
| **换能器** | Clojure |可组合算法 |
| **幽灵** | Clojure |数据导航|
| **架构** | Clojure |数据验证|
| **马利** | Clojure |数据验证|
| **数据.json** | Clojure | JSON |
| **柴郡** | Clojure | JSON（更快）|
| **打嗝** | Clojure | HTML 生成 |
| **重新构建** | Clojure 脚本 | SPA框架|
| **试剂** | Clojure 脚本 |反应包装器 |
| **唵** | Clojure 脚本 |反应接口 |
| **核心.匹配** | Clojure |模式匹配|
| **工具.logging** | Clojure |记录 |
| **安装** | Clojure |状态管理|
| **积分** | Clojure |组件系统 |
| **usocket** | CL |套接字库 |
| **波尔多线** | CL |线程 |
| **亚历山大** | CL |实用程序库|
---

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **VS Code + Calva** |最佳 Clojure IDE |
| **CIDER (Emacs)** |经典 Clojure IDE |
| **IntelliJ + 草书** | JetBrains Clojure | JetBrains Clojure |
| **史莱姆/狡猾** |通用 Lisp (Emacs) |
| **莱姆** | Common Lisp IDE |
| **Vim + 壁炉** | Vim Clojure | Vim Clojure | Vim Clojure
---

## 部署
|方法|笔记|
|--------|--------|
| **尤伯贾尔** |  `clj -T:build jar`（Clojure）|
| **GraalVM Native** |原生镜像（有限）|
| **码头工人** |集装箱式|
| **巴巴什卡** |快速脚本编写 |
| **Lisp 二进制** |已编译的二进制文件 (SBCL) |
| **Kubernetes** |编排|
---

＃＃ 概括
Lisp 生态系统涵盖多种方言：**Clojure**（JVM、现代）、**Common Lisp**（经典、ANSI）、**Racket**（面向语言）和 **Emacs Lisp**（编辑器脚本）。 Clojure 的标准堆栈是：**Clojure CLI** 和 **deps.edn** 用于构建，**Ring + Compojure** 或 **Pedestal** 用于 Web，**next.jdbc** 用于数据库，**clojure.test** 用于测试，**clj-kondo** 用于 linting，以及 **VS Code + Calva** 或 **CIDER** 作为 IDE。 Common Lisp 使用 **Quicklisp** 进行封装，使用 **SBCL** 进行编译，使用 **SLIME** 进行开发。 Lisp 的优势是宏、同像性、REPL 驱动的开发和交互式编程。该生态系统擅长快速原型设计、特定领域语言和数据处理。