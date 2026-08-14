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

# Lisp 和 Clojure
Lisp 是仍在使用的第二古老的高階程式語言（僅次於 Fortran），由 John McCarthy 於 1958 年創建。它開創了許多現在被視為理所當然的概念：垃圾收集、遞歸、樹資料結構、動態類型以及程式即資料的想法（同像性）。 Lisp 的顯著特徵是它的語法——程式碼被編寫為嵌套括號（S 表達式），這使得語言可以輕鬆解析，並透過**巨集**實現強大的元程式設計。
Clojure 是 Rich Hickey 於 2007 年設計的現代 Lisp 方言。它運行在 JVM（也稱為 JavaScript 的 ClojureScript）上，支援函數式程式設計、不變性和並發性，並提供無縫的 Java 互通性。 Clojure 用於 Web 開發、資料處理和金融系統。
---

## 為什麼 Lisp/Clojure 很重要
- **同像性**：程式碼就是資料－程式可以操縱自己的結構，從而啟用強大的巨集。
- **巨集**：Lisp 巨集將程式碼作為資料進行操作，讓您可以擴展語言本身。
- **函數式程式設計**：Lisp 開創的 FP 概念至今仍在使用。
- **JVM 上的 Clojure**：具有完整 Java 程式庫存取、不可變資料結構和出色並發性的現代 Lisp。
- **REPL 驅動的開發**：具有即時回饋的互動式開發。
- **簡單性**：Clojure 具有小型且一致的語言設計 — 沒有特殊情況。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **括號** |大量使用`()`最初可能難以閱讀 |使用IDE支援；學會觀察結構|
| **利基社群** |與主流語言相比，就業市場較小活躍且熱情的社群 |
| **Clojure 啟動時間** |基於 JVM； CLI 啟動緩慢 |使用 GraalVM 原生鏡像 |
| **Lisp 方言** |許多不相容的 Lisp（Common Lisp、Scheme、Emacs Lisp）|選擇 Clojure 進行現代工作 |
| **非主流** |更少的函式庫、框架和教學 |利用 Java 生態系統 (Clojure) |
---

## Clojure 語法
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

## 進階語法和模式
### 巨集深入探討
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

### 協定和記錄
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

### 多種方法
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

## 並發與平行
### 原子、參考、代理和 STM
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

### 並行操作
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

## 專案配置與建置系統
### 專案結構 (deps.edn)
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

### deps.edn 配置
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

### 關鍵建置命令
|命令 |描述 |
|---------|-------------|
|`clj -M:dev`|使用開發依賴項啟動 REPL |
|`clj -M:test`|運行測試套件 |
|`clj -M:run`|運行應用程式 |
|`clj -T:build uber`|建置 uber JAR |
|`lein new app my-app`|建立萊寧根專案 |
|`lein test`|運行測試 (Leiningen) |
|`lein uberjar`|建置 uber JAR (Leiningen) |
### CI/CD 管道 (GitHub Actions)
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

## 測試
### clojure.test — 內建測試
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

### test.check — 基於屬性的測試
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

## 互通性
### Java 互通
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

## 設計模式
### 附安裝組件系統
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

### 帶有線程的管道模式
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

## 效能與最佳化
### 分析工具
|工具|目的|用途 |
|------|---------|--------|
| **標準** |統計標竿|`(bench (expr))`|
| **VisualVM** | JVM 分析 |`jvisualvm`命令 |
| **clj-async-profile** |低開銷 CPU 分析 |`start`/`stop`/`serve`|
| **塔夫特** |運行時分析 |`(p :tag (expr))`|
### 使用 Criterium 進行基準測試
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

### 優化技術
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

## 部署
### 建構 Uber JAR
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

### Docker 部署
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

### GraalVM 原生映像
```bash
# Build with GraalVM for instant startup
native-image --no-fallback \
  --initialize-at-build-time \
  -jar target/my-app.jar \
  -o my-app-native

# Startup time: <50ms vs ~2s for JVM
```

---

## 何時使用 Lisp/Clojure
|場景|為什麼選擇 Clojure |更好的選擇|
|----------|------------|--------------------|
|網路後端 | Ring/Compojure 有成效 | Go、Node.js 提供更簡單的 API |
|資料處理|優秀序列庫 | Python (Pandas)、Scala (Spark) |
|並發系統|不可變資料+STM |去吧，Erlang/Elixir |
| DSL / 語言擴充 |巨集是無與倫比的 | — |
| REPL 驅動的開發 |一流的互動式工作流程 | — |
|通用應用開發 |可能但利基| Python、Java、Go |
|行動應用程式 |用於網頁應用程式的 ClojureScript；不是本地人|斯威夫特、科特林 |
|資料科學|不是生態系| Python、R |
---

## 綜合問答
### Q1：為什麼 Lisp/Clojure 程式有這麼多括號？
**A:** 括號代表 S 表達式 - 一種統一語法，其中程式碼和資料具有相同的結構（同像性）：
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

### Q2：Clojure 如何以不同的方式處理狀態和可變性？
**A:** Clojure 預設為不可變資料。對於受控狀態更改，它提供了引用類型：
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

### Q3：Clojure 的持久資料結構是什麼？
**A:** 所有 Clojure 集合都是持久的（不可變的、結構共享的）：
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

### Q4：Clojure 巨集如何運作？
**A:** 巨集接收未計算的程式碼（作為資料），對其進行轉換，然後傳回新程式碼：
```clojure
(defmacro unless [condition & body]
  `(if (not ~condition)
     (do ~@body)))

;; Usage
(unless false
  (println "This runs!"))
```

### Q5：如何在 Clojure 中處理並發？
**答：** Clojure 提供了多種並發原語：
-`atom`— 獨立、同步更改
-`ref`+`dosync`— 協調的事務性變更
-`agent`— 非同步、獨立的更改
-`core.async`通道 — CSP 式並發
---

## 解決問題的思路
### 問題 1：處理資料管道
**第 1 步：了解問題**
透過管道讀取資料、過濾、轉換和聚合。
**第 2 步：確定方法**
使用 Clojure 的線程巨集 (`->>`) 和轉換器。
**步驟 3：實施**```clojure
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

**第 4 步：優化**
轉換器避免創建中間序列——它們將轉換組合成一次傳遞。
### 問題 2：建立簡單的 Web 伺服器
**第 1 步：了解問題**
使用 Ring/Compojure 建立基本的 HTTP 伺服器。
**第 2 步：確定方法**
使用環適配器和 Compojure 路由。
**步驟 3：實施**```clojure
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

**第 4 步：擴充**
新增用於日誌記錄、JSON 解析、身份驗證和錯誤處理的中間件。
---

＃＃ 概括
Lisp 是程式語言設計的祖父母——大多數現代語言都藉鑒了 Lisp 幾十年前開創的思想。 Clojure 透過不變性、並發支援和無縫 JVM 整合將 Lisp 帶入現代時代。雖然 Lisp/Clojure 不是主流，但學習它將從根本上改變你對程式設計的看法。僅宏觀系統就值得投資——它揭示了其他語言無法比擬的可能性。