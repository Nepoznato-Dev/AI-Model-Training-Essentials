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

# Lisp & Clojure
Lisp là ngôn ngữ lập trình cấp cao lâu đời thứ hai vẫn còn được sử dụng (sau Fortran), do John McCarthy tạo ra vào năm 1958. Nó đi tiên phong trong nhiều khái niệm hiện được coi là đương nhiên: thu thập rác, đệ quy, cấu trúc dữ liệu cây, gõ động và ý tưởng về các chương trình dưới dạng dữ liệu (tính đồng nhất). Tính năng đặc biệt của Lisp là cú pháp của nó — mã được viết dưới dạng dấu ngoặc đơn lồng nhau (biểu thức S), giúp ngôn ngữ có thể phân tích cú pháp một cách dễ dàng và cho phép lập trình siêu dữ liệu mạnh mẽ thông qua **macro**.
Clojure là một phương ngữ Lisp hiện đại được Rich Hickey thiết kế vào năm 2007. Nó chạy trên JVM (cũng là ClojureScript cho JavaScript), bao gồm lập trình chức năng, tính bất biến và tính đồng thời, đồng thời cung cấp khả năng tương tác Java liền mạch. Clojure được sử dụng trong phát triển web, xử lý dữ liệu và hệ thống tài chính.
---

## Tại sao Lisp/Clojure lại quan trọng
- **Tính đồng nhất**: Mã là dữ liệu — các chương trình có thể thao tác với cấu trúc của chính chúng, tạo ra các macro mạnh mẽ.
- **Macro**: Macro Lisp hoạt động trên mã dưới dạng dữ liệu, cho phép bạn tự mở rộng ngôn ngữ.
- **Lập trình chức năng**: Các khái niệm FP tiên phong của Lisp vẫn được sử dụng cho đến ngày nay.
- **Clojure trên JVM**: Lisp hiện đại với quyền truy cập đầy đủ vào thư viện Java, cấu trúc dữ liệu bất biến và khả năng chạy đồng thời tuyệt vời.
- **Phát triển dựa trên REPL**: Phát triển tương tác với phản hồi ngay lập tức.
- **Đơn giản**: Clojure có thiết kế ngôn ngữ nhỏ gọn, nhất quán — không có trường hợp đặc biệt.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Dấu ngoặc đơn** | Việc sử dụng nhiều`()`ban đầu có thể khó đọc | Sử dụng hỗ trợ IDE; học cách xem cấu trúc |
| **Cộng đồng thích hợp** | Thị trường việc làm nhỏ so với các ngôn ngữ chính thống | Cộng đồng năng động và đam mê |
| **Thời gian khởi động Clojure** | Dựa trên JVM; khởi động chậm cho CLI | Sử dụng hình ảnh gốc GraalVM |
| **Phương ngữ Lisp** | Nhiều Lisp không tương thích (Lisp thông thường, Lược đồ, Lisp Emacs) | Chọn Clojure cho công việc hiện đại |
| **Không chính thống** | Ít thư viện, khung và hướng dẫn hơn | Tận dụng hệ sinh thái Java (Clojure) |
---

## Cú pháp Clojure
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

## Cú pháp & Mẫu nâng cao
### Tìm hiểu sâu về macro
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

### Giao thức và bản ghi
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

### Đa phương thức
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

## Đồng thời & Song song
### Nguyên tử, Ref, Đại lý và STM
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

### Hoạt động song song
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án (deps.edn)
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

### cấu hình deps.edn
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

### Lệnh xây dựng chính
| Lệnh | Mô tả |
|----------|-------------|
| `clj -M:dev`| Bắt đầu REPL với các phụ thuộc của nhà phát triển |
| `clj -M:test`| Chạy bộ thử nghiệm |
| `clj -M:run`| Chạy ứng dụng |
| `clj -T:build uber`| Xây dựng JAR uber |
| `lein new app my-app`| Tạo dự án Leiningen |
| `lein test`| Chạy thử nghiệm (Leiningen) |
| `lein uberjar`| Xây dựng JAR uber (Leiningen) |
### Đường dẫn CI/CD (Hành động trên GitHub)
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

##Thử nghiệm
### clojure.test — Thử nghiệm tích hợp
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

### test.check — Kiểm tra dựa trên thuộc tính
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

## Khả năng tương tác
### Tương tác Java
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

## Mẫu thiết kế
### Hệ thống thành phần có gắn kết
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

### Mẫu đường ống có luồng
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

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
| Công cụ | Mục đích | Cách sử dụng |
|------|----------|-------|
| **Tiêu chí** | Điểm chuẩn thống kê | `(bench (expr))`|
| **VisualVM** | Hồ sơ JVM |  Lệnh`jvisualvm`|
| **clj-async-profile** | Cấu hình CPU chi phí thấp | `start`/`stop`/`serve`|
| **Tufte** | Hồ sơ thời gian chạy | `(p :tag (expr))`|
### Đo điểm chuẩn bằng Tiêu chí
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

### Kỹ thuật tối ưu hóa
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

## Triển khai
### Xây dựng JAR Uber
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

### Triển khai Docker
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

### Hình ảnh gốc GraalVM
```bash
# Build with GraalVM for instant startup
native-image --no-fallback \
  --initialize-at-build-time \
  -jar target/my-app.jar \
  -o my-app-native

# Startup time: <50ms vs ~2s for JVM
```

---

## Khi nào nên sử dụng Lisp/Clojure
| Kịch bản | Tại sao Clojure | Thay thế tốt hơn |
|----------|-------------|-------------------|
| Phụ trợ web | Ring/Compojure hoạt động hiệu quả | Đi, Node.js để có các API đơn giản hơn |
| Xử lý dữ liệu | Thư viện trình tự xuất sắc | Python (Gấu trúc), Scala (Spark) |
| Hệ thống đồng thời | Dữ liệu bất biến + STM | Đi, Erlang/Elixir |
| DSL / phần mở rộng ngôn ngữ | Macro chưa từng có | — |
| Phát triển dựa trên REPL | Quy trình làm việc tương tác tốt nhất | — |
| Phát triển ứng dụng chung | Có thể nhưng thích hợp | Python, Java, Đi |
| Ứng dụng di động | ClojureScript cho ứng dụng web; không phải người bản địa | Swift, Kotlin |
| Khoa học dữ liệu | Không phải hệ sinh thái | Python, R |
---

## Hỏi đáp tổng hợp
### Q1: Tại sao chương trình Lisp/Clojure lại có nhiều dấu ngoặc đơn đến vậy?
**A:** Dấu ngoặc đơn biểu thị biểu thức S — một cú pháp thống nhất trong đó mã và dữ liệu có cùng cấu trúc (tính đồng âm):
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

### Câu 2: Clojure xử lý trạng thái và khả năng biến đổi khác nhau như thế nào?
**A:** Clojure mặc định sử dụng dữ liệu không thể thay đổi. Đối với những thay đổi trạng thái được kiểm soát, nó cung cấp các loại tham chiếu:
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

### Câu 3: Cấu trúc dữ liệu liên tục của Clojure là gì?
**A:** Tất cả các bộ sưu tập Clojure đều ổn định (không thay đổi, được chia sẻ về mặt cấu trúc):
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

### Câu 4: Macro Clojure hoạt động như thế nào?
**A:** Macro nhận mã chưa được đánh giá (dưới dạng dữ liệu), chuyển đổi mã đó và trả về mã mới:
```clojure
(defmacro unless [condition & body]
  `(if (not ~condition)
     (do ~@body)))

;; Usage
(unless false
  (println "This runs!"))
```

### Câu hỏi 5: Làm cách nào để xử lý đồng thời trong Clojure?
**A:** Clojure cung cấp nhiều nguyên hàm đồng thời:
-`atom`— thay đổi độc lập, đồng bộ
-`ref`+`dosync`— các thay đổi mang tính giao dịch, phối hợp
-`agent`- thay đổi độc lập, không đồng bộ
- Kênh`core.async`— Đồng thời kiểu CSP
---

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Xử lý đường ống dữ liệu
**Bước 1: Tìm hiểu vấn đề**
Đọc dữ liệu, lọc, chuyển đổi và tổng hợp thông qua một đường dẫn.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng macro phân luồng của Clojure (`->>`) và bộ chuyển đổi.
**Bước 3: Thực hiện**```clojure
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

**Bước 4: Tối ưu hóa**
Bộ chuyển đổi tránh tạo ra các chuỗi trung gian - chúng kết hợp các phép biến đổi thành một lần truyền duy nhất.
### Bài toán 2: Xây dựng một Web Server đơn giản
**Bước 1: Tìm hiểu vấn đề**
Tạo một máy chủ HTTP cơ bản bằng Ring/Compojure.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng bộ chuyển đổi Ring và định tuyến Compojure.
**Bước 3: Thực hiện**```clojure
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

**Bước 4: Gia hạn**
Thêm phần mềm trung gian để ghi nhật ký, phân tích cú pháp JSON, xác thực và xử lý lỗi.
---

## Bản tóm tắt
Lisp là ông tổ của thiết kế ngôn ngữ lập trình - hầu hết các ngôn ngữ hiện đại đều vay mượn những ý tưởng mà Lisp đã đi tiên phong từ nhiều thập kỷ trước. Clojure đưa Lisp vào kỷ nguyên hiện đại với tính bất biến, hỗ trợ đồng thời và tích hợp JVM liền mạch. Mặc dù Lisp/Clojure không phổ biến nhưng việc học nó về cơ bản sẽ thay đổi cách bạn nghĩ về lập trình. Chỉ riêng hệ thống macro đã đáng để đầu tư — nó bộc lộ những khả năng mà các ngôn ngữ khác không thể sánh được.