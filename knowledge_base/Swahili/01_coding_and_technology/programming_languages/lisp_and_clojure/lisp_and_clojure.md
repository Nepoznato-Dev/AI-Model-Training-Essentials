---
# Metadata
title: "Lisp & Clojure"
description: "Comprehensive reference for the Lisp and Clojure programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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
Lisp ni lugha ya pili ya kongwe ya programu ya kiwango cha juu ambayo bado inatumika (baada ya Fortran), iliyoundwa na John McCarthy mnamo 1958. Ilianzisha dhana nyingi zinazochukuliwa kuwa za kawaida: ukusanyaji wa takataka, urejeshaji, miundo ya data ya miti, kuandika kwa nguvu, na wazo la programu kama data (homoiconicity). Kipengele tofauti cha Lisp ni sintaksia yake — msimbo umeandikwa kama mabano yaliyowekwa kwenye kiota (S-maneno), ambayo hufanya lugha iweze kutambulishwa kidogo na kuwezesha uratibu wa nguvu kupitia **makro**.
Clojure ni lahaja ya kisasa ya Lisp iliyoundwa na Rich Hickey mwaka wa 2007. Inatumika kwenye JVM (pia ClojureScript ya JavaScript), inakumbatia utendakazi wa programu, kutobadilika, na upatanifu, na hutoa mwingiliano wa Java bila mshono. Clojure hutumiwa katika ukuzaji wa wavuti, usindikaji wa data na mifumo ya kifedha.
---

## Kwa Nini Lisp/Clojure Matters
- **Homoiconicity**: Msimbo ni data - programu zinaweza kudhibiti muundo wao wenyewe, na kuwezesha macros zenye nguvu.
- **Macros**: Lisp macros hufanya kazi kwa msimbo kama data, hukuruhusu kupanua lugha yenyewe.
- **Programu zinazofanya kazi**: Lisp dhana zilizoanzishwa za FP bado zinatumika leo.
- **Funga kwenye JVM**: Lisp ya Kisasa yenye ufikiaji kamili wa maktaba ya Java, miundo ya data isiyoweza kubadilika, na upatanisho bora kabisa.
- **Uendelezaji unaoendeshwa na REPL**: Ukuzaji mwingiliano na maoni ya papo hapo.
- **Urahisi**: Clojure ina muundo mdogo na thabiti wa lugha — hakuna kesi maalum.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Mabano** | Matumizi makubwa ya`()`yanaweza kuwa magumu kusoma mwanzoni | Tumia usaidizi wa IDE; jifunze kuona muundo |
| **Jumuiya ya Niche** | Soko dogo la ajira ikilinganishwa na lugha za kawaida | Jumuiya hai na yenye shauku |
| **Muda wa kuanza wa kufunga** | JVM-msingi; kuanza polepole kwa CLIs | Tumia picha asili ya GraalVM |
| **Lisp lahaja** | Midomo mingi isiyooana (Lisp ya Kawaida, Mpango, Emacs Lisp) | Chagua Clojure kwa kazi ya kisasa |
| **Si ya kawaida** | Maktaba chache, mifumo, na mafunzo | Tumia mfumo ikolojia wa Java (Clojure) |
---

## Sintaksia ya Clojure
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

## Sintaksia na Miundo ya Kina
### Macros Deep Dive
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

### Itifaki na Rekodi
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

### Mbinu nyingi
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

## Concurrency & Usambamba
### Atomu, Marejeleo, Mawakala, na STM
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

### Operesheni Sambamba
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Muundo wa Mradi (deps.edn)
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

### deps.edn Configuration
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

### Amri Muhimu za Kujenga
| Amri | Maelezo |
|---------|-------------|
| `clj -M:dev`| Anzisha REPL na utegemezi wa dev |
| `clj -M:test`| Run test suite |
| `clj -M:run`| Endesha programu |
| `clj -T:build uber`| Jenga uber JAR |
| `lein new app my-app`| Unda mradi wa Leiningen |
| `lein test`| Endesha majaribio (Leiningen) |
| `lein uberjar`| Jenga uber JAR (Leiningen) |
### CI/CD Bomba (Vitendo vya GitHub)
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

##Upimaji
### clojure.test - Jaribio lililojumuishwa ndani
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

### test.check — Jaribio linalotegemea Mali
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

## Kuingiliana
### Java Interop
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

## Miundo ya Kubuni
### Mfumo wa Sehemu na Mlima
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

### Mchoro wa Bomba lenye Uzi
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

## Utendaji na Uboreshaji
### Zana za Kuweka Wasifu
| Zana | Kusudi | Matumizi |
|------|---------|-------|
| **Kigezo** | Uwekaji alama wa takwimu | `(bench (expr))`|
| **VisualVM** | Uwekaji wasifu wa JVM | `jvisualvm`amri |
| **clj-async-profil** | Uwekaji wasifu wa chini wa CPU | `start`/`stop`/`serve`|
| **Tufte** | Uwekaji wasifu wa wakati unaotumika | `(p :tag (expr))`|
### Kulinganisha kwa Kigezo
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

### Mbinu za Kuboresha
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

## Usambazaji
### Kujenga JAR za Uber
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

### Usambazaji wa Docker
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

### Picha ya Asili ya GraalVM
```bash
# Build with GraalVM for instant startup
native-image --no-fallback \
  --initialize-at-build-time \
  -jar target/my-app.jar \
  -o my-app-native

# Startup time: <50ms vs ~2s for JVM
```

---

## Wakati wa Kutumia Lisp/Clojure
| Hali | Kwa nini Clojure | Mbadala Bora |
|----------|-------------------------------|
| Nyuma za wavuti | Pete/Compojure ina tija | Nenda, Node.js kwa API rahisi |
| Usindikaji wa data | Maktaba bora ya mlolongo | Chatu (Pandas), Scala (Cheche) |
| Mifumo ya wakati mmoja | Data isiyoweza kubadilika + STM | Nenda, Erlang/Elixir |
| DSL / kiendelezi cha lugha | Macro hazilinganishwi | - |
| Maendeleo yanayoendeshwa na REPL | Mtiririko bora wa mwingiliano wa darasa | - |
| Maendeleo ya maombi ya jumla | Inawezekana lakini niche | Python, Java, Nenda |
| Programu za simu | ClojureScript kwa programu za wavuti; sio asili | Swift, Kotlin |
| Sayansi ya data | Sio mfumo wa ikolojia | Chatu, R |
---

## Maswali na Majibu Yaliyoundwa
### Q1: Kwa nini programu za Lisp/Clojure zina mabano mengi?
**J:** Mabano yanawakilisha misemo ya S - sintaksia sare ambapo msimbo na data zina muundo sawa (homoiconicity):
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

### Q2: Je! Clojure anashughulikiaje hali na kubadilika kwa njia tofauti?
**J:** Clojure chaguomsingi kwa data isiyoweza kubadilika. Kwa mabadiliko ya hali iliyodhibitiwa, hutoa aina za kumbukumbu:
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

### Q3: Je, miundo ya data ya Clojure ni ipi?
**J:** Mikusanyiko yote ya Clojure ni endelevu (haibadiliki, inashirikiwa kimuundo):
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

### Q4: Je, Clojure macros hufanya kazi vipi?
**J:** Macro hupokea msimbo ambao haujatathminiwa (kama data), uibadilishe, na urudishe msimbo mpya:
```clojure
(defmacro unless [condition & body]
  `(if (not ~condition)
     (do ~@body)))

;; Usage
(unless false
  (println "This runs!"))
```

### Q5: Je, ninawezaje kushughulikia concurrency katika Clojure?
**J:** Clojure hutoa malighafi nyingi za upatanishi:
-`atom`- mabadiliko huru, yanayolingana
-`ref`+`dosync`- imeratibiwa, mabadiliko ya shughuli
-`agent`- asynchronous, mabadiliko huru
- Vituo vya`core.async`- sarafu ya mtindo wa CSP
---

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Kuchakata Bomba la Data
**Hatua ya 1: Elewa Tatizo**
Soma data, chujio, badilisha, na ujumlishe kupitia bomba.
**Hatua ya 2: Tambua Mbinu**
Tumia makro ya kuunganisha ya Clojure (`->>`) na vibadilishaji sauti.
**Hatua ya 3: Tekeleza**```clojure
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

**Hatua ya 4: Boresha **
Transducers huepuka kuunda mfuatano wa kati - hutunga mabadiliko kuwa pasi moja.
### Tatizo la 2: Kuunda Seva Rahisi ya Wavuti
**Hatua ya 1: Elewa Tatizo**
Unda seva ya msingi ya HTTP kwa kutumia Ring/Compojure.
**Hatua ya 2: Tambua Mbinu**
Tumia adapta ya Gonga na uelekezaji wa Kuchanganya.
**Hatua ya 3: Tekeleza**```clojure
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

**Hatua ya 4: Panua**
Ongeza vifaa vya kati vya ukataji miti, uchanganuzi wa JSON, uthibitishaji, na kushughulikia makosa.
---

## Muhtasari
Lisp ndiye mzalishaji mkuu wa muundo wa lugha ya programu - lugha nyingi za kisasa hukopa mawazo ambayo Lisp alianzisha miongo kadhaa iliyopita. Clojure huleta Lisp katika enzi ya kisasa na kutoweza kubadilika, usaidizi wa sarafu, na muunganisho wa JVM usio na mshono. Ingawa Lisp/Clojure si ya kawaida, kujifunza kutabadilisha jinsi unavyofikiri kuhusu upangaji programu. Mfumo mkuu pekee ndio unaostahili kuwekeza - unaonyesha uwezekano ambao lugha zingine haziwezi kuendana.