---
# Metadata
title: "Lisp & Clojure"
description: "Comprehensive reference for the Lisp and Clojure programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [lisp-and-clojure, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "29 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Lisp と Clojure
Lisp は、1958 年に John McCarthy によって作成され、現在でも使用されている (Fortran に次ぐ) 2 番目に古い高級プログラミング言語です。Lisp は、ガベージ コレクション、再帰、ツリー データ構造、動的型付け、データとしてのプログラムの考え方 (ホモイコニシティ) など、現在では当然のことと考えられている多くの概念の先駆けとなりました。 Lisp の特徴はその構文です。コードは入れ子の括弧 (S 式) として記述されます。これにより言語が簡単に解析可能になり、**マクロ** による強力なメタプログラミングが可能になります。
Clojure は、2007 年に Rich Hickey によって設計された最新の Lisp 言語です。JVM (JavaScript 用の ClojureScript とも) 上で実行され、関数型プログラミング、不変性、同時実行性を採用し、シームレスな Java 相互運用性を提供します。 Clojure は、Web 開発、データ処理、金融システムで使用されています。
---

## Lisp/Clojure が重要な理由
- **同形性**: コードはデータです。プログラムは独自の構造を操作して、強力なマクロを有効にすることができます。
- **マクロ**: Lisp マクロはコードをデータとして操作し、言語自体を拡張できます。
- **関数型プログラミング**: Lisp は、現在でも使用されている FP 概念の先駆者です。
- **JVM 上の Clojure**: 完全な Java ライブラリ アクセス、不変のデータ構造、優れた同時実行性を備えた最新の Lisp。
- **REPL 主導の開発**: 即時のフィードバックを伴う対話型開発。
- **シンプルさ**: Clojure は小規模で一貫した言語設計を採用しており、特別なケースはありません。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **括弧** |`()`を頻繁に使用すると、最初は読みにくい場合があります。 IDE サポートを使用します。構造を見ることを学ぶ |
| **ニッチなコミュニティ** |主流言語に比べて雇用市場が小さい |アクティブで情熱的なコミュニティ |
| **Clojure の起動時間** | JVMベース。 CLI の起動が遅い | GraalVM ネイティブ イメージを使用する |
| **Lisp の方言** |多くの互換性のない Lisp (Common Lisp、Scheme、Emacs Lisp) |最新の作業には Clojure を選択してください |
| **主流ではありません** |ライブラリ、フレームワーク、チュートリアルが少ない | Java エコシステムを活用する (Clojure) |
---

## Clojure の構文
```clojure
;; Variables (immutable by default)
(def name "Alice")
(def age 30)
(def score 9.5)

;; Functions
(defn greet [name greeting]
  (str greeting ", " name "!"))

(greet "Alice" "Hello")  ;; "Hello, Alice!"

;; Higher-order functions
(def numbers [1 2 3 4 5])
(map #(* % 2) numbers)           ;; (2 4 6 8 10)
(filter even? numbers)           ;; (2 4)
(reduce + numbers)               ;; 15

;; Maps (hash maps)
(def user {:name "Alice" :age 30 :email "alice@example.com"})
(:name user)                     ;; "Alice"
(get user :age)                  ;; 30

;; Immutability
(def original [1 2 3])
(def modified (conj original 4)) ;; original is unchanged: [1 2 3]
                                  ;; modified: [1 2 3 4]

;; Destructuring
(let [{:keys [name age]} user]
  (println name "is" age "years old"))

;; Concurrency (atoms for shared mutable state)
(def counter (atom 0))
(swap! counter inc)              ;; 1
(swap! counter + 5)              ;; 6

;; Sequences and lazy evaluation
(def fibs (lazy-cat [0 1] (map + fibs (rest fibs))))
(take 10 fibs)                   ;; (0 1 1 2 3 5 8 13 21 34)

;; Java interop
(import 'java.util.Date)
(def now (Date.))
(.toUpperCase "hello")           ;; "HELLO"

;; Macros (extend the language)
(defmacro unless [condition & body]
  `(when (not ~condition) ~@body))

(unless false (println "This runs!"))
```

---

## 高度な構文とパターン
### マクロの詳細
```clojure
;; Syntax quoting and unquoting
(defmacro when-let [[binding expr] & body]
  `(let [temp# ~expr]
     (when temp#
       (let [~binding temp#]
         ~@body))))

;; temp# generates a unique symbol to avoid name collisions (gensym)

;; Macro that creates a DSL
(defmacro defroutes [name & routes]
  `(def ~name
     (fn [request#]
       (cond
         ~@(mapcat (fn [[method path handler]]
                     [`(and (= (:request-method request#) ~method)
                            (= (:uri request#) ~path))
                      `(~handler request#)])
                   (partition 3 routes))))))

;; Usage
(defroutes app-routes
  :get "/" index-handler
  :get "/users" list-users-handler
  :post "/users" create-user-handler)

;; Reader conditionals for cross-platform code
#?(:clj (def platform :jvm)
   :cljs (def platform :js)
   :default (def platform :unknown))

;; Threading macros
(-> "Hello World"
    .toLowerCase
    (.replace "world" "clojure")
    (str "!!!"))
;; "hello clojure!!!"

(->> (range 20)
     (filter even?)
     (map #(* % %))
     (take 5)
     (reduce +))
;; 120 (0 + 4 + 16 + 36 + 64)
```

### プロトコルと記録
```clojure
;; Protocols — Clojure's approach to polymorphism
(defprotocol Serializable
  (serialize [obj] "Convert object to a serializable string")
  (deserialize [data] "Reconstruct object from string"))

;; Records — efficient immutable data types
(defrecord User [id name email created-at])

(def alice (->User 1 "Alice" "alice@example.com" (java.time.Instant/now)))

;; Implement protocol for a record
(extend-type User
  Serializable
  (serialize [user]
    (str "{\"id\":" (:id user)
         ",\"name\":\"" (:name user)
         "\",\"email\":\"" (:email user) "\"}"))
  (deserialize [data]
    ;; parse JSON back to User
    user))

;; Implement for built-in types
(extend-type java.util.Map
  Serializable
  (serialize [m] (clojure.data.json/write-str m)))

;; Usage
(serialize alice)
;; "{\"id\":1,\"name\":\"Alice\",\"email\":\"alice@example.com\"}"
```

### マルチメソッド
```clojure
;; Multimethods — dispatch on any function of arguments
(defmulti area
  "Calculate the area of a shape"
  :type)

(defmethod area :circle [{:keys [radius]}]
  (* Math/PI radius radius))

(defmethod area :rectangle [{:keys [width height]}]
  (* width height))

(defmethod area :triangle [{:keys [a b c]}]
  (let [s (/ (+ a b c) 2)]
    (Math/sqrt (* s (- s a) (- s b) (- s c)))))

;; Default method
(defmethod area :default [shape]
  (throw (ex-info "Unknown shape" {:shape shape})))

(area {:type :circle :radius 5})       ;; 78.539...
(area {:type :rectangle :width 3 :height 4})  ;; 12

;; Custom dispatch function
(defmulti process-event (fn [event] [(::type event) (::version event)]))
(defmethod process-event [:user-created 1] [event] ...)
(defmethod process-event [:user-created 2] [event] ...)
```


---

## 同時実行性と並列処理
### アトム、参照、エージェント、および STM
```clojure
;; Atoms — uncoordinated, synchronous updates
(def balance (atom 1000))
(swap! balance - 200)         ;; 800
(swap! balance (fn [b] (+ b 500)))  ;; 1300
(compare-and-set! balance 1300 1500)  ;; true (CAS operation)

;; Refs — coordinated, synchronous updates (STM)
(def account-a (ref 1000))
(def account-b (ref 500))

(dosync
  (alter account-a - 200)
  (alter account-b + 200))

;; Agents — asynchronous, independent updates
(def logger (agent []))
(send logger conj "Log entry 1")
(send logger conj "Log entry 2")
(await logger)
(deref logger)  ;; ["Log entry 1" "Log entry 2"]

;; Futures
(let [f (future (Thread/sleep 1000) 42)]
  (println "Doing other work...")
  (println "Result:" @f))

;; Core.async — CSP-style concurrency
(require '[clojure.core.async :as async])

(let [ch (async/chan)]
  (async/go
    (dotimes [i 5] (async/>! ch i)))
  (async/go
    (dotimes [i 5]
      (println "Received:" (async/<! ch)))))
```

### 並列操作
```clojure
;; pmap — parallel map
(defn slow-square [n]
  (Thread/sleep 100)
  (* n n))

(pmap slow-square (range 10))  ;; uses all cores

;; Reducers — parallel reduction
(require '[clojure.core.reducers :as r])
(def large-vec (vec (range 1000000)))
(r/fold + (r/map #(* % %) large-vec))

;; Transducers — composable transformations
(def xform
  (comp (filter even?) (map #(* % %)) (take 10)))

(transduce xform + 0 (range 100))
```


---

## プロジェクトの構成とシステムの構築
### プロジェクト構造 (deps.edn)
```
my-clojure-project/
├── src/
│   └── my_project/
│       ├── core.clj
│       ├── handlers.clj
│       ├── models.clj
│       └── db.clj
├── test/
│   └── my_project/
│       ├── core_test.clj
│       └── handlers_test.clj
├── resources/
│   ├── config.edn
│   └── logback.xml
├── deps.edn
├── build.clj
├── .cljfmt.edn
└── README.md
```

### deps.edn 構成
```clojure
{:paths ["src" "resources"]

 :deps
 {org.clojure/clojure {:mvn/version "1.11.1"}
  org.clojure/core.async {:mvn/version "1.6.681"}
  ring/ring-core {:mvn/version "1.10.0"}
  ring/ring-jetty-adapter {:mvn/version "1.10.0"}
  compojure/compojure {:mvn/version "1.7.0"}
  hiccup/hiccup {:mvn/version "2.0.0-RC2"}
  next.jdbc {:mvn/version "1.3.894"}
  org.postgresql/postgresql {:mvn/version "42.6.0"}
  clojure.data/json {:mvn/version "2.4.0"}
  mount/mount {:mvn/version "0.1.17"}
  clojure.tools.logging {:mvn/version "1.2.4"}}

 :aliases
 {:dev {:extra-paths ["dev"]
        :extra-deps {nrepl/nrepl {:mvn/version "1.1.0"}
                     cider/cider-nrepl {:mvn/version "0.44.0"}}}

  :test {:extra-paths ["test"]
         :extra-deps {io.github.cognitect-labs/test-runner
                      {:git/tag "v0.5.1" :git/sha "dfb30dd"}}
         :main-opts ["-m" "cognitect.test-runner"]
         :exec-fn cognitect.test-runner.runner/test}

  :build {:deps {io.github.clojure/tools.build {:mvn/version "0.9.6"}}
          :ns-default build}

  :run {:main-opts ["-m" "my-project.core"]}}}
```

### 主要なビルド コマンド
|コマンド |説明 |
|----------|---------------|
| `clj -M:dev`|開発依存関係を使用して REPL を開始する |
| `clj -M:test`|テストスイートを実行する |
| `clj -M:run`|アプリケーションを実行します |
| `clj -T:build uber`| uber JAR をビルドする |
| `lein new app my-app`|ライニンゲン プロジェクトの作成 |
| `lein test`|テストの実行 (ライニンゲン) |
| `lein uberjar`| uber JAR のビルド (ライニンゲン) |
### CI/CD パイプライン (GitHub アクション)
```yaml
name: Clojure CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v3
        with:
          distribution: temurin
          java-version: '21'
      - uses: DeLaGuardo/setup-clojure@12.1
        with:
          cli: latest
      - name: Cache deps
        uses: actions/cache@v3
        with:
          path: ~/.m2
          key: clj-${{ hashFiles('deps.edn') }}
      - run: clj -M:test
      - run: clj -T:build uber
```


---

## テスト
### clojure.test — 組み込みテスト
```clojure
(ns my-project.core-test
  (:require [clojure.test :refer :all]
            [my-project.core :as core]))

(deftest test-add
  (testing "adds two positive numbers"
    (is (= 5 (core/add 2 3))))
  (testing "handles negative numbers"
    (is (= -3 (core/add -1 -2))))
  (testing "handles zero"
    (is (= 5 (core/add 0 5)))))

(deftest test-factorial
  (is (= 1 (core/factorial 0)))
  (is (= 120 (core/factorial 5)))
  (is (= 3628800 (core/factorial 10))))

;; Testing with fixtures
(defn setup-db [f]
  ;; setup before tests
  (core/init-test-db)
  (f)
  ;; teardown after tests
  (core/drop-test-db))

(use-fixtures :once setup-db)

(deftest test-user-crud
  (testing "create and retrieve user"
    (let [user (core/create-user! {:name "Alice" :email "a@b.com"})]
      (is (some? (:id user)))
      (is (= "Alice" (:name (core/get-user (:id user))))))))
```

### test.check — プロパティベースのテスト
```clojure
(require '[clojure.test.check :as tc]
         '[clojure.test.check.generators :as gen]
         '[clojure.test.check.properties :as prop])

;; Properties
(def reverse-involutive
  (prop/for-all [v (gen/vector gen/int)]
    (= v (reverse (reverse v)))))

(tc/quick-check 100 reverse-involutive)
;; {:result true, :num-tests 100, ...}

;; Custom generators
(def gen-email
  (gen/fmap (fn [[user domain]]
              (str user "@" domain ".com"))
            (gen/tuple gen/string-alphanumeric
                       gen/string-alphanumeric)))

(def sort-preserves-length
  (prop/for-all [v (gen/vector gen/int 1 100)]
    (= (count v) (count (sort v)))))

(tc/quick-check 100 sort-preserves-length)
```

---

## 相互運用性
### Java 相互運用性
```clojure
;; Creating Java objects
(def date (java.util.Date.))
(def list (java.util.ArrayList.))
(def file (java.io.File. "/tmp/test.txt"))

;; Calling Java methods
(.toUpperCase "hello")           ;; "HELLO"
(.length "hello")                ;; 5
(.substring "hello world" 6)     ;; "world"

;; Calling static methods
(Math/sqrt 144)                  ;; 12.0
(System/currentTimeMillis)       ;; epoch millis
(Integer/parseInt "42")          ;; 42

;; Accessing fields
(.-PI Math)                      ;; 3.14159...

;; Importing classes
(import '[java.time LocalDate Duration]
        '[java.util.concurrent ConcurrentHashMap])

(def today (LocalDate/now))
(def map (ConcurrentHashMap.))
(.put map "key" "value")

;; Implementing Java interfaces
(def runnable
  (reify Runnable
    (run [_] (println "Running in thread!"))))

(.start (Thread. runnable))

;; Extending Java classes
(def custom-exception
  (proxy [RuntimeException] ["Custom error"]
    (getMessage [] (str "Custom: " (.getMessage ^RuntimeException this)))))
```

---

## デザインパターン
### マウント付きコンポーネント システム
```clojure
;; Mount — lightweight state management
(require '[mount.core :refer [defstate]])

(defstate db
  :start (do (println "Starting DB connection...")
             (connect-to-db (config :db-url)))
  :stop (do (println "Stopping DB connection...")
            (disconnect db)))

(defstate http-server
  :start (do (println "Starting HTTP server...")
             (start-server {:port (config :port)
                            :handler (make-handler)}))
  :stop (stop-server http-server))

;; Start all components
(mount.core/start)
;; Stop all components (in reverse order)
(mount.core/stop)
```

### スレッドを使用したパイプライン パターン
```clojure
;; Data processing pipeline
(defn process-order [order]
  (-> order
      validate-order
      calculate-tax
      apply-discounts
      charge-payment
      create-fulfillment
      send-confirmation))

;; Each function takes and returns the order map
(defn validate-order [{:keys [items] :as order}]
  (if (empty? items)
    (throw (ex-info "Empty order" {:order order}))
    order))

(defn calculate-tax [order]
  (let [subtotal (reduce + (map :price (:items order)))]
    (assoc order :tax (* subtotal 0.08) :subtotal subtotal)))

(defn apply-discounts [{:keys [subtotal] :as order}]
  (let [discount (if (> subtotal 100) (* subtotal 0.1) 0)]
    (assoc order :discount discount)))

;; Transducer pipeline for streaming data
(def process-pipeline
  (comp
    (map parse-line)
    (filter valid-record?)
    (map enrich-record)
    (partition-all 100)))

;; Apply to a data source
(transduce process-pipeline conj [] (line-seq (reader "data.csv")))
```


---

## パフォーマンスと最適化
### プロファイリングツール
|ツール |目的 |使い方 |
|------|-------|------|
| **クリテリウム** |統計的ベンチマーク | `(bench (expr))`|
| **VisualVM** | JVMプロファイリング | `jvisualvm`コマンド |
| **clj-async-profil** |低オーバーヘッドの CPU プロファイリング | `start`/`stop`/`serve`|
| **タフテ** |ランタイムプロファイリング | `(p :tag (expr))`|
### Criterium によるベンチマーク
```clojure
(require '[criterium.core :as crit])

;; Benchmark an expression
(crit/bench
  (reduce + (map #(* % %) (range 10000))))

;; Output: mean ~X ms, std deviation ~Y us
;; Also reports GC pauses, overhead, etc.

;; Compare two implementations
(crit/with-progress-reporting
  (crit/quick-bench
    (into [] (comp (filter even?) (map #(* % %))) (range 10000))))
```

### 最適化手法
```clojure
;; 1. Use transients for batch mutations
(defn fast-merge [maps]
  (persistent!
    (reduce (fn [acc m]
              (reduce-kv (fn [a k v] (assoc! a k v)) acc m))
            (transient {})
            maps)))

;; 2. Use type hints to avoid reflection
(defn ^String fast-upper [^String s]
  (.toUpperCase s))

;; 3. Use arrays for numeric computation
(defn dot-product [^doubles a ^doubles b]
  (areduce a i ret 0.0
    (+ ret (* (aget a i) (aget b i)))))

;; 4. Prefer persistent data structures with structural sharing
;; Vectors: O(log32 n) access, efficient appends
;; Maps: O(log32 n) access, efficient updates

;; 5. Use unchecked math for tight numeric loops
(defn fast-sum ^long [^longs arr]
  (areduce arr i ret 0
    (unchecked-add ret (aget arr i))))

;; 6. Compile with :unchecked-math :warn-on-boxed for optimization
```

---

## デプロイメント
### Uber JAR の構築
```clojure
;; build.clj
(ns build
  (:require [clojure.tools.build.api :as b]))

(def class-dir "target/classes")
(def basis (b/create-basis {:project "deps.edn"}))
(def uber-file "target/my-app.jar")

(defn uber [_]
  (b/copy-dir {:src-dirs ["src" "resources"]
               :target-dir class-dir})
  (b/compile-clj {:basis basis
                  :src-dirs ["src"]
                  :class-dir class-dir})
  (b/uber {:class-dir class-dir
           :uber-file uber-file
           :basis basis
           :main 'my-project.core}))
```

```bash
# Build uber JAR
clj -T:build uber

# Run it
java -jar target/my-app.jar
```

### Docker のデプロイメント
```dockerfile
FROM clojure:temurin-21-tools-deps AS builder
WORKDIR /app
COPY deps.edn ./
RUN clojure -P -M:test
COPY . .
RUN clojure -T:build uber

FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=builder /app/target/my-app.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### GraalVM ネイティブ イメージ
```bash
# Build with GraalVM for instant startup
native-image --no-fallback \
  --initialize-at-build-time \
  -jar target/my-app.jar \
  -o my-app-native

# Startup time: <50ms vs ~2s for JVM
```

---

## Lisp/Clojure を使用する場合
|シナリオ | Clojure を使用する理由 |より良い代替案 |
|----------|-----------|----------|
| Web バックエンド |リング/コンポジュールは生産的です |より単純な API については Node.js を使用してください |
|データ処理 |優れた配列ライブラリ | Python (パンダ)、Scala (スパーク) |
|同時システム |不変データ + STM |行く、Erlang/Elixir |
| DSL / 言語拡張 |マクロは比類のないものです | — |
| REPL 主導の開発 |クラス最高のインタラクティブなワークフロー | — |
|一般的なアプリケーション開発 |可能だがニッチ | Python、Java、Go |
|モバイルアプリ | Web アプリ用の ClojureScript。ネイティブではありません |スウィフト、コトリン |
|データサイエンス |エコシステムではありません |パイソン、R |
---

## 総合的な Q&A
### Q1: Lisp/Clojure プログラムにはなぜこれほど多くのかっこがあるのですか?
**A:** 括弧は S 式を表します。コードとデータが同じ構造 (同形性) を持つ統一構文です。
```clojure
;; Every form is a list: (operator arg1 arg2 ...)
(+ 1 2 3)          ;; 6
(str "hello" " " "world")  ;; "hello world"

;; Nested expressions
(defn factorial [n]
  (if (<= n 1)
    1
    (* n (factorial (dec n)))))

;; The uniform syntax means macros can manipulate code as data
```

### Q2: Clojure は状態と可変性をどのように異なる方法で処理しますか?
**A:** Clojure はデフォルトで不変データを使用します。制御された状態変更については、参照タイプが提供されます。
```clojure
;; Immutable by default
(def x [1 2 3])
(conj x 4)     ;; [1 2 3 4] — original unchanged
x              ;; still [1 2 3]

;; Atoms — synchronous, uncoordinated changes
(def counter (atom 0))
(swap! counter inc)    ;; 1
(swap! counter + 10)   ;; 11

;; Refs — coordinated, transactional changes
(def account-a (ref 100))
(def account-b (ref 50))
(dosync
  (alter account-a - 30)
  (alter account-b + 30))
```

### Q3: Clojure の永続データ構造は何ですか?
**A:** すべての Clojure コレクションは永続的です (不変、構造的に共有されています)。
```clojure
;; Vectors
[1 2 3]                  ;; literal
(vec (range 10))         ;; from range
(conj [1 2] 3)           ;; [1 2 3] — O(1) append

;; Maps (hash maps)
{:name "Alice" :age 30}
(assoc {:a 1} :b 2)      ;; {:a 1 :b 2}
(dissoc {:a 1 :b 2} :a)  ;; {:b 2}

;; Sets
#{1 2 3}
(clojure.set/union #{1 2} #{2 3})  ;; #{1 2 3}
```

### Q4: Clojure マクロはどのように機能しますか?
**A:** マクロは未評価のコードを (データとして) 受け取り、それを変換して、新しいコードを返します。
```clojure
(defmacro unless [condition & body]
  `(if (not ~condition)
     (do ~@body)))

;; Usage
(unless false
  (println "This runs!"))
```

### Q5: Clojure で同時実行性を処理するにはどうすればよいですか?
**A:** Clojure は複数の同時実行プリミティブを提供します。
-`atom`— 独立した同期変更
-`ref`+`dosync`— 調整されたトランザクションの変更
-`agent`— 非同期で独立した変更
-`core.async`チャネル — CSP スタイルの同時実行
---

## 思考連鎖による問題解決
### 問題 1: データ パイプラインの処理
**ステップ 1: 問題を理解する**
パイプラインを通じてデータを読み取り、フィルターし、変換し、集計します。
**ステップ 2: アプローチを特定する**
Clojure のスレッド マクロ (`->>`) とトランスデューサーを使用します。
**ステップ 3: 実装**```clojure
(def data
  [{:name "Alice" :age 30 :dept "Eng"}
   {:name "Bob" :age 25 :dept "Sales"}
   {:name "Charlie" :age 35 :dept "Eng"}
   {:name "Diana" :age 28 :dept "Eng"}])

;; Threading macro pipeline
(->> data
     (filter #(= (:dept %) "Eng"))
     (map :age))
;; => (30 35 28)

;; Average age of Engineering department
(let [eng-ages (->> data
                    (filter #(= (:dept %) "Eng"))
                    (map :age))]
  (/ (reduce + eng-ages) (count eng-ages)))
;; => 31

;; Transducers — composable, reusable transformations
(def xform (comp (filter #(= (:dept %) "Eng"))
                 (map :age)))

(transduce xform conj [] data)
;; => [30 35 28]
```

**ステップ 4: 最適化**
トランスデューサは中間シーケンスの作成を回避し、変換を 1 つのパスにまとめます。
### 問題 2: 単純な Web サーバーの構築
**ステップ 1: 問題を理解する**
Ring/Compojure を使用して基本的な HTTP サーバーを作成します。
**ステップ 2: アプローチを特定する**
リング アダプターと Compojure ルーティングを使用します。
**ステップ 3: 実装**```clojure
(require '[ring.adapter.jetty :as jetty]
         '[compojure.core :refer [defroutes GET]]
         '[compojure.route :as route])

(defroutes app
  (GET "/" [] "Hello, World!")
  (GET "/users/:id" [id] (str "User: " id))
  (route/not-found "Not Found"))

(defn -main []
  (jetty/run-jetty app {:port 3000}))
```

**ステップ 4: 延長**
ロギング、JSON 解析、認証、エラー処理のためのミドルウェアを追加します。
---

＃＃ まとめ
Lisp はプログラミング言語設計の祖先です。現代のほとんどの言語は、Lisp が数十年前に開拓したアイデアを借用しています。 Clojure は、不変性、同時実行サポート、シームレスな JVM 統合を備えた Lisp を現代にもたらします。 Lisp/Clojure は主流ではありませんが、Lisp/Clojure を学ぶことでプログラミングに対する考え方が根本的に変わります。マクロ システムだけでも投資する価値があります。他の言語では実現できない可能性が明らかになります。