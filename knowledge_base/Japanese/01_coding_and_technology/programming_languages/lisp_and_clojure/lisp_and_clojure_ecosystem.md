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
# Lisp と Clojure — エコシステムとツールのガイド
このガイドでは、Lisp および Clojure エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## Lisp と Clojure の実装
|実装 |言語 |メモ |
|---------------|----------|------|
| **Clojure** | JVM | JVM 上の最新の Lisp |
| **ClojureScript** | JS | JavaScript にコンパイルされた Clojure |
| **SBCL** |共通Lisp |高性能CL |
| **CCL** |共通Lisp | OpenMCL、高速コンパイル |
| **ECL** |共通Lisp |組み込み可能、​​C 相互運用性 |
| **Emacs Lisp** | Emacs |拡張言語 |
| **ラケット** |スキーム |言語指向プログラミング |
| **ガイル** |スキーム | GNU 拡張言語 |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Clojure ツール
|ツール |目的 |
|-----|----------|
| **Clojure CLI (clj)** |公式 CLI ツール |
| **ライニンゲン** |クラシックなプロジェクトツール |
| **deps.edn** |依存関係の管理 |
| **ババシュカ** |高速 Clojure スクリプト |
| **ツール.ビルド** |ビルドの自動化 |
| **シャドウ cljs** | ClojureScript ビルド |
| **フィグホイール** |ライブ ClojureScript のリロード |
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

## 共通の Lisp ツール
|ツール |目的 |
|-----|----------|
| **クイックリスプ** |パッケージマネージャー |
| **空自** |ビルドシステム |
| **ロズウェル** | Lisp環境マネージャー |
| **Qロット** |ローカル依存関係管理 |
| **スライム** | Emacs Lisp IDE |
| **ずるい** | Emacs Lisp IDE (SLIME フォーク) |
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

## Web フレームワーク
|フレームワーク |言語 |タイプ |
|----------|----------|------|
| **リング + コンポジュール** |クロジュア | HTTP ハンドラー + ルーティング |
| **台座** |クロジュア |フルスタックウェブ |
| **ルミナス** |クロジュア | Web フレームワーク スタック |
| ** リーティット ** |クロジュア |ルーティングライブラリ |
| **フンチェントゥート** | CL | HTTPサーバー |
| **穴居人** | CL |ウェブフレームワーク |
| **レストラン** | CL | RESTフレームワーク |
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

## データベース
|テクノロジー |言語 |タイプ |
|-----------|----------|------|
| **next.jdbc** |クロジュア | JDBC ラッパー |
| **HugSQL** |クロジュア | SQL ファースト |
| **ハニーSQL** |クロジュア | SQL DSL |
| **clojure.jdbc** |クロジュア | JDBCインターフェース |
| **ポストモダン** | CL |ポストグレSQL |
| **CLSQL** | CL | SQLインターフェース |
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

## テスト
|フレームワーク |言語 |目的 |
|----------|----------|----------|
| **clojure.test** |クロジュア |組み込みのテスト |
| **ミジェ** |クロジュア | BDD スタイルのテスト |
| **期待** |クロジュア |期待ベース |
| **テスト.チェック** |クロジュア |プロパティベース (クイックチェック) |
| **午前5時** | CL |単体テスト |
| **証明** | CL |テストフレームワーク |
| **lisp ユニット** | CL |単体テスト |
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

## コードの品質
|ツール |言語 |目的 |
|------|----------|----------|
| **clj-近藤** |クロジュア |リンター |
| **cljfmt** |クロジュア |フォーマッタ |
| **イーストウッド** |クロジュア |リンティング |
| **キビット** |クロジュア |コードの提案 |
| **アレックスとテリー** |クロジュア |スタイルガイド |
| **アレックスプラス** | CL |コード分​​析 |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## 主要なライブラリ
|図書館 |言語 |目的 |
|----------|----------|----------|
| **コア.async** |クロジュア | CSP 同時実行 |
| **トランスデューサー** |クロジュア |構成可能なアルゴリズム |
| **スペクター** |クロジュア |データナビゲーション |
| **スキーマ** |クロジュア |データ検証 |
| **マリ** |クロジュア |データ検証 |
| **data.json** |クロジュア | JSON |
| **チェシャー** |クロジュア | JSON (高速) |
| **しゃっくり** |クロジュア | HTMLの生成 |
| **再フレーム** | ClojureScript | SPAフレームワーク |
| **試薬** | ClojureScript |反応ラッパー |
| **ああ** | ClojureScript |反応インターフェイス |
| **コア.マッチ** |クロジュア |パターンマッチング |
| **ツール.ロギング** |クロジュア |ロギング |
| **マウント** |クロジュア |状態管理 |
| **統合者** |クロジュア |コンポーネントシステム |
| **ウソケット** | CL |ソケットライブラリ |
| **ボルドースレッド** | CL |スレッド |
| **アレクサンドリア** | CL |ユーティリティライブラリ |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **VS コード + Calva** |最高の Clojure IDE |
| **CIDER (Emacs)** |クラシック Clojure IDE |
| **IntelliJ + 筆記体** | JetBrains Clojure |
| **スライム / スライ** | Common Lisp (Emacs) |
| **レム** |共通Lisp IDE |
| **Vim + 暖炉** |ヴィム・クロージュア |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **Uberjar** | `clj -T:build jar`(Clojure) |
| **GraalVM ネイティブ** |ネイティブ画像（限定） |
| **ドッカー** |コンテナ化 |
| **ババシュカ** |高速スクリプト |
| **Lisp バイナリ** |コンパイル済みバイナリ (SBCL) |
| **Kubernetes** |オーケストレーション |
---

＃＃ まとめ
Lisp エコシステムは複数の方言にまたがっています: **Clojure** (JVM、モダン)、**Common Lisp** (クラシック、ANSI)、**Racket** (言語指向)、**Emacs Lisp** (エディター スクリプト)。 Clojure の標準スタックは次のとおりです。ビルド用の **deps.edn** を備えた **Clojure CLI**、Web 用の **Ring + Compojure** または **Pedestal**、データベース用の **next.jdbc**、テスト用の **clojure.test**、lint 用の **clj-kondo**、IDE として **VS Code + Calva** または **CIDER**。 Common Lisp はパッケージに **Quicklisp**、コンパイルに **SBCL**、開発に **SLIME** を使用します。 Lisp の強みは、マクロ、同形性、REPL 駆動開発、対話型プログラミングです。このエコシステムは、ラピッド プロトタイピング、ドメイン固有言語、データ処理に優れています。