---
# فراداده
عنوان: "Lisp & Clojure"
توضیحات: "مرجع جامع برای زبان برنامه نویسی Lisp و Clojure شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم و زمان استفاده از آن."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب ها: [lisp-and-clojure، زبان برنامه نویسی، نحو، اکوسیستم، کدگذاری و فناوری]
سطح سختی: "پیشرفته"
پیش نیاز: []
تخمینی_زمان_خواندن: "29 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
# Lisp & Clojure
Lisp دومین زبان برنامه نویسی سطح بالا است که هنوز مورد استفاده قرار می گیرد (پس از فرترن)، که توسط جان مک کارتی در سال 1958 ایجاد شد. این زبان پیشگام بسیاری از مفاهیمی است که امروزه بدیهی هستند: جمع آوری زباله، بازگشت، ساختارهای داده درختی، تایپ پویا، و ایده برنامه ها به عنوان داده (همونیکونیکی). ویژگی متمایز Lisp، نحو آن است – کد به صورت پرانتز تودرتو (عبارات S) نوشته می‌شود، که زبان را به‌طور بی‌اهمیت تجزیه‌پذیر می‌کند و فرابرنامه‌نویسی قدرتمند را از طریق **ماکروها** ممکن می‌سازد.
Clojure یک گویش مدرن Lisp است که توسط Rich Hickey در سال 2007 طراحی شده است. این گویش بر روی JVM (همچنین ClojureScript برای جاوا اسکریپت) اجرا می شود، برنامه نویسی کاربردی، تغییر ناپذیری و همزمانی را در بر می گیرد و قابلیت همکاری یکپارچه جاوا را فراهم می کند. Clojure در توسعه وب، پردازش داده ها و سیستم های مالی استفاده می شود.
---

## چرا Lisp/Clojure مهم است
- **Homoiconicity**: کد یک داده است - برنامه ها می توانند ساختار خود را دستکاری کنند و ماکروهای قدرتمند را فعال کنند.
- **ماکروها**: ماکروهای Lisp بر روی کد به عنوان داده عمل می کنند و به شما امکان می دهند خود زبان را گسترش دهید.
- **برنامه نویسی عملکردی**: Lisp از مفاهیم FP پیشگام بود که هنوز هم امروزه استفاده می شود.
- **Clojure در JVM**: Lisp مدرن با دسترسی کامل به کتابخانه جاوا، ساختارهای داده غیرقابل تغییر و همزمانی عالی.
- ** توسعه مبتنی بر REPL **: توسعه تعاملی با بازخورد فوری.
- **سادگی**: Clojure طراحی زبانی کوچک و ثابتی دارد — بدون موارد خاص.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **پرانتز** | استفاده زیاد از`()`در ابتدا می تواند سخت باشد | از پشتیبانی IDE استفاده کنید. آموزش دیدن ساختار |
| **جامعه طاقچه** | بازار کار کوچک در مقایسه با زبان های رایج | جامعه فعال و پرشور |
| **زمان راه اندازی کلوژور** | مبتنی بر JVM؛ راه اندازی کند برای CLIs | استفاده از GraalVM native-image |
| **گویش های Lisp** | بسیاری از Lispهای ناسازگار (Common Lisp، Scheme، Emacs Lisp) | Clojure را برای کارهای مدرن انتخاب کنید |
| **جریان اصلی نیست** | کتابخانه، چارچوب و آموزش کمتر | اهرم اکوسیستم جاوا (Clojure) |
---

## نحو Clojure
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

## نحو و الگوهای پیشرفته
### شیرجه عمیق ماکرو
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

### پروتکل ها و سوابق
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

### چند روش
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

## همزمانی و موازی
### اتم ها، مراجع، عوامل و STM
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

### عملیات موازی
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه (deps.edn)
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

### پیکربندی deps.edn
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

### دستورات ساخت کلید
| فرمان | توضیحات |
|---------|-------------|
| `clj -M:dev`| شروع REPL با وابستگی های dev |
|  __محافظت شده_1__ | اجرای مجموعه تست |
| `clj -M:run`| برنامه را اجرا کنید |
|  __محافظت شده_3__ | ساخت uber JAR |
| `lein new app my-app`| ایجاد پروژه لاینینگن |
| `lein test`| اجرای تست ها (لینینگن) |
|  __محافظت شده_6__ | ساخت uber JAR (Leiningen) |
### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### clojure.test — تست داخلی
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

### test.check — تست مبتنی بر ویژگی
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

## قابلیت همکاری
### جاوا Interop
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

## الگوهای طراحی
### سیستم کامپوننت با Mount
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

### الگوی خط لوله با نخ
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
| ابزار | هدف | استفاده |
|------|---------|-------|
| **معیار** | معیارهای آماری | `(bench (expr))`|
| **VisualVM** | پروفایل JVM |  دستور`jvisualvm`|
| **clj-async-profil** | پروفایل کم سربار CPU | `start`/`stop`/`serve`|
| **تفت** | نمایه سازی زمان اجرا | `(p :tag (expr))`|
### محک زدن با معیار
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

### تکنیک های بهینه سازی
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

## استقرار
### ساخت Uber JARs
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

### استقرار داکر
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

### GraalVM Native Image
```bash
# Build with GraalVM for instant startup
native-image --no-fallback \
  --initialize-at-build-time \
  -jar target/my-app.jar \
  -o my-app-native

# Startup time: <50ms vs ~2s for JVM
```

---

## چه زمانی از Lisp/Clojure استفاده کنیم
| سناریو | چرا کلوژور | جایگزین بهتر |
|----------|-----------|------------------|
| پشتیبان های وب | Ring/Compojure مولد هستند | برو، Node.js برای API های ساده تر |
| پردازش داده | کتابخانه توالی عالی | پایتون (پاندا)، اسکالا (جرقه) |
| سیستم های همزمان | داده های تغییرناپذیر + STM | برو ارلنگ/اکسیر |
| DSL ها / پسوند زبان | ماکروها بی همتا هستند | — |
| توسعه مبتنی بر REPL | بهترین گردش کار تعاملی در کلاس | — |
| توسعه برنامه عمومی | ممکن است اما طاقچه | پایتون، جاوا، برو |
| برنامه های موبایل | ClojureScript برای برنامه های وب؛ بومی نیست | سویفت، کاتلین |
| علم داده | نه اکوسیستم | پایتون، R |
---

## خلاصه
Lisp پدربزرگ و مادربزرگ طراحی زبان برنامه نویسی است - اکثر زبان های مدرن ایده هایی را به عاریت گرفته اند که Lisp دهه ها پیش پیشگام بود. Clojure Lisp را با تغییر ناپذیری، پشتیبانی همزمان و ادغام یکپارچه JVM وارد عصر مدرن می‌کند. در حالی که Lisp/Clojure جریان اصلی نیست، یادگیری آن اساساً طرز فکر شما را در مورد برنامه نویسی تغییر می دهد. سیستم کلان به تنهایی ارزش سرمایه گذاری را دارد - احتمالاتی را نشان می دهد که زبان های دیگر نمی توانند با آنها مطابقت داشته باشند.