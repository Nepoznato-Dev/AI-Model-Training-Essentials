---
# البيانات الوصفية
العنوان: "ليسب وكلوجر"
الوصف: "مرجع شامل للغة البرمجة Lisp وClojure يغطي النظرة العامة والمقايضات وأساسيات بناء الجملة والنظام البيئي ومتى يتم استخدامها."
الفئة: "البرمجة والتكنولوجيا"
الإصدار: "1.0.0"
الحالة: "نشط"
#مساهمة
المؤلفين:
  - الاسم: "فريق تدريب نموذج الذكاء الاصطناعي"
    البريد الإلكتروني: ""
    الدور: "original_author"
المساهمين: []
سجل التغيير:
  - الإصدار: "1.0.0"
    التاريخ: "2026-08-05"
    المؤلف: "فريق تدريب نموذج الذكاء الاصطناعي"
    التغييرات: "تمت إضافة بيانات تعريف YAML الأمامية لتتبع المساهمين"
# مراجعة
تم الإنشاء: "05-08-2026"
آخر_تعديل: "05-08-2026"
تاريخ_المراجعة: "05-02-2027"
تمت المراجعة بواسطة: "فريق قاعدة معارف البرمجة والتكنولوجيا"
next_review: "2027-08-05"
# التصنيف
العلامات: [ليسب-و-كلوجور، لغة البرمجة، بناء الجملة، النظام البيئي، الترميز والتكنولوجيا]
مستوى الصعوبة: "متقدم"
المتطلبات الأساسية: []
وقت_القراءة المقدر: "29 دقيقة"
# دليل المساهمة
المساهمة:
  الترخيص: "MIT"
  Feedback_channel: "مشكلات GitHub"
  how_to_contribute: "أرسل رسالة عامة تحتوي على التغييرات وقم بتحديث سجل التغييرات"
  review_process: "تتم مراجعة التغييرات بواسطة مشرفي الفئة قبل الدمج"
---
# اللثغة وكلوجر
تعد لغة Lisp ثاني أقدم لغة برمجة عالية المستوى لا تزال قيد الاستخدام (بعد لغة Fortran)، وقد أنشأها جون مكارثي في ​​عام 1958. وكانت رائدة في العديد من المفاهيم التي تعتبر الآن أمرا مفروغا منه: تجميع البيانات المهملة، والتكرار، وهياكل البيانات الشجرية، والكتابة الديناميكية، وفكرة البرامج كبيانات (homoiconicity). السمة المميزة لـ Lisp هي بناء الجملة - تتم كتابة التعليمات البرمجية كأقواس متداخلة (تعبيرات S)، مما يجعل اللغة قابلة للتحليل بشكل تافه ويتيح البرمجة الفوقية القوية من خلال **وحدات الماكرو**.
Clojure هي لهجة Lisp حديثة صممها Rich Hickey في عام 2007. وهي تعمل على JVM (أيضًا ClojureScript لـ JavaScript)، وتتضمن البرمجة الوظيفية، والثبات، والتزامن، وتوفر إمكانية التشغيل التفاعلي السلس لـ Java. يستخدم Clojure في تطوير الويب ومعالجة البيانات والأنظمة المالية.
---

## لماذا يهم Lisp/Clojure
- **التماثل المتماثل**: الكود عبارة عن بيانات — يمكن للبرامج التعامل مع بنيتها الخاصة، مما يتيح وحدات ماكرو قوية.
- **وحدات الماكرو**: تعمل وحدات ماكرو Lisp على التعليمات البرمجية كبيانات، مما يسمح لك بتوسيع اللغة نفسها.
- **البرمجة الوظيفية**: لا تزال مفاهيم FP الرائدة في Lisp مستخدمة حتى اليوم.
- **Clojure on JVM**: Lisp حديث مع وصول كامل إلى مكتبة Java، وهياكل بيانات غير قابلة للتغيير، وتزامن ممتاز.
- ** التطوير القائم على REPL **: تطوير تفاعلي مع تعليقات فورية.
- **البساطة**: يتميز Clojure بتصميم لغة صغير ومتسق - ولا توجد حالات خاصة.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **الأقواس** | قد يكون من الصعب قراءة الاستخدام المكثف لـ`()`في البداية | استخدام دعم IDE. تعلم رؤية الهيكل |
| ** المجتمع المتخصص ** | سوق عمل صغير مقارنة باللغات السائدة | مجتمع نشط وعاطفي |
| **وقت بدء تشغيل Clojure** | على أساس JVM؛ بدء تشغيل بطيء لـ CLIs | استخدم صورة GraalVM الأصلية |
| **لهجات اللثغة** | العديد من اللثغات غير المتوافقة (Common Lisp، Scheme، Emacs Lisp) | اختر Clojure للعمل الحديث |
| **ليست سائدة** | مكتبات وأطر عمل وبرامج تعليمية أقل | الاستفادة من نظام Java البيئي (Clojure) |
---

## بناء جملة كلوجر
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

## بناء الجملة والأنماط المتقدمة
### الغوص العميق في وحدات الماكرو
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

### البروتوكولات والسجلات
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

### طرق متعددة
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

## التزامن والتوازي
### الذرات والمراجع والوكلاء وSTM
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

### العمليات الموازية
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

## تكوين المشروع ونظام البناء
### هيكل المشروع (deps.edn)
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

### تكوين deps.edn
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

### أوامر بناء المفاتيح
| الأمر | الوصف |
|---------|------------|
|  __محمي_0__ | ابدأ REPL باستخدام تبعيات التطوير |
|  __محمي_1__ | تشغيل مجموعة الاختبار |
|  __محمي_2__ | قم بتشغيل التطبيق |
|  __محمي_3__ | قم ببناء أوبر جار |
|  __محمي_4__ | إنشاء مشروع لينينجن |
|  __محمي_5__ | تشغيل الاختبارات (لينينجن) |
|  __محمي_6__ | بناء أوبر JAR (لينينجن) |
### خط أنابيب CI/CD (إجراءات GitHub)
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

## الاختبار
### clojure.test — اختبار مدمج
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

### test.check — الاختبار المبني على الخاصية
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

## إمكانية التشغيل البيني
### جافا التشغيل المتداخل
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

## أنماط التصميم
### نظام المكونات مع التركيب
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

### نمط خط الأنابيب مع الخيوط
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

## الأداء والتحسين
### أدوات التنميط
| أداة | الغرض | الاستخدام |
|------|---------|------|
| **المعيار** | المقارنة الإحصائية |  __محمي_0__ |
| **VisualVM** | ملف تعريف JVM |  __محمي_1__ الأمر |
| **clj-async-profil** | ملفات تعريف وحدة المعالجة المركزية ذات الحمل المنخفض |  __محمي_2__ / __محمي_3__ / __محمي_4__ |
| **تافتي** | ملفات تعريف وقت التشغيل |  __محمي_5__ |
### المقارنة المعيارية
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

### تقنيات التحسين
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

## النشر
### بناء جارات أوبر
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

### نشر عامل الميناء
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

### الصورة الأصلية GraalVM
```bash
# Build with GraalVM for instant startup
native-image --no-fallback \
  --initialize-at-build-time \
  -jar target/my-app.jar \
  -o my-app-native

# Startup time: <50ms vs ~2s for JVM
```

---

## متى يجب استخدام Lisp/Clojure
| السيناريو | لماذا كلوجر | البديل الأفضل |
|----------|-----------|------------------|
| الواجهات الخلفية للويب | الحلقة/الكومبوجور منتجة | اذهب، Node.js لواجهات برمجة التطبيقات الأكثر بساطة |
| معالجة البيانات | مكتبة التسلسل الممتاز | بايثون (الباندا)، سكالا (سبارك) |
| الأنظمة المتزامنة | بيانات غير قابلة للتغيير + STM | اذهب، إرلانج/إلكسير |
| DSL / امتداد اللغة | وحدات الماكرو لا مثيل لها | — |
| التطوير المبني على REPL | سير العمل التفاعلي الأفضل في فئته | — |
| تطوير التطبيقات العامة | ممكن ولكن المتخصصة | بايثون، جافا، اذهب |
| تطبيقات الجوال | ClojureScript لتطبيقات الويب؛ ليست أصلية | سويفت، كوتلين |
| علم البيانات | ليس النظام البيئي | بايثون، ر |
---

## ملخص
Lisp هو جد تصميم لغة البرمجة - فمعظم اللغات الحديثة تستعير أفكارًا كانت Lisp رائدة فيها منذ عقود. يجلب Clojure Lisp إلى العصر الحديث من خلال الثبات ودعم التزامن والتكامل السلس لـ JVM. على الرغم من أن لغة Lisp/Clojure ليست سائدة، إلا أن تعلمها سيغير بشكل جذري طريقة تفكيرك في البرمجة. إن النظام الكلي وحده يستحق الاستثمار، فهو يكشف عن إمكانيات لا يمكن للغات الأخرى مضاهاتها.