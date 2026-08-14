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
Lisp è il secondo linguaggio di programmazione di alto livello più antico ancora in uso (dopo Fortran), creato da John McCarthy nel 1958. Ha aperto la strada a molti concetti ora dati per scontati: garbage collection, ricorsione, strutture dati ad albero, tipizzazione dinamica e l'idea di programmi come dati (omoiconicità). La caratteristica distintiva del Lisp è la sua sintassi: il codice è scritto come parentesi annidate (espressioni S), il che rende il linguaggio banalmente analizzabile e consente una potente metaprogrammazione tramite **macro**.
Clojure è un dialetto Lisp moderno progettato da Rich Hickey nel 2007. Funziona su JVM (anche ClojureScript per JavaScript), abbraccia la programmazione funzionale, l'immutabilità e la concorrenza e fornisce una perfetta interoperabilità Java. Clojure è utilizzato nello sviluppo web, nell'elaborazione dei dati e nei sistemi finanziari.
---

## Perché Lisp/Clojure è importante
- **Omoiconicità**: il codice è dato: i programmi possono manipolare la propria struttura, abilitando macro potenti.
- **Macro**: le macro Lisp operano sul codice come dati, consentendo di estendere il linguaggio stesso.
- **Programmazione funzionale**: Lisp ha aperto la strada ai concetti FP utilizzati ancora oggi.
- **Clojure su JVM**: Lisp moderno con accesso completo alla libreria Java, strutture dati immutabili ed eccellente concorrenza.
- **Sviluppo basato su REPL**: sviluppo interattivo con feedback immediato.
- **Semplicità**: Clojure ha un design linguistico piccolo e coerente, senza casi speciali.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Parentesi** | L'uso intenso di`()`può essere difficile da leggere inizialmente | Utilizzare il supporto IDE; imparare a vedere la struttura |
| **Comunità di nicchia** | Piccolo mercato del lavoro rispetto alle lingue tradizionali | Comunità attiva e appassionata |
| **Tempo di avvio di Clojure** | Basato su JVM; avvio lento per le CLI | Utilizza l'immagine nativa GraalVM |
| **Dialetti Lisp** | Molti Lisp incompatibili (Common Lisp, Scheme, Emacs Lisp) | Scegli Clojure per un lavoro moderno |
| **Non mainstream** | Meno librerie, framework ed esercitazioni | Sfruttare l'ecosistema Java (Clojure) |
---

## Sintassi Clojure
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

## Sintassi e modelli avanzati
### Approfondimento sulle macro
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

### Protocolli e registrazioni
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

### Multimetodi
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

## Concorrenza e parallelismo
### Atomi, riferimenti, agenti e STM
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

### Operazioni parallele
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

## Configurazione del progetto e sistema di creazione
### Struttura del progetto (deps.edn)
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

### Configurazione deps.edn
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

### Comandi di creazione chiave
| Comando | Descrizione |
|---------|-----|
| `clj -M:dev`| Avvia REPL con dipendenze dev |
| `clj -M:test`| Esegui la suite di test |
| `clj -M:run`| Eseguire l'applicazione |
| `clj -T:build uber`| Costruisci uber JAR |
| `lein new app my-app`| Crea progetto Leiningen |
| `lein test`| Eseguire test (Leiningen) |
| `lein uberjar`| Costruisci uber JAR (Leiningen) |
### Pipeline CI/CD (azioni GitHub)
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

## Test
### clojure.test — Test integrato
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

### test.check — Test basato sulle proprietà
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

## Interoperabilità
### Interoperabilità Java
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

## Modelli di progettazione
### Sistema di componenti con supporto
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

### Modello di pipeline con filettatura
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

## Prestazioni e ottimizzazione
### Strumenti di profilazione
| Strumento | Scopo | Utilizzo |
|------|---------|-------|
| **Criterio** | Benchmarking statistico | `(bench (expr))`|
| **VisualVM** | Profilazione JVM |  Comando`jvisualvm`|
| **clj-profilo-asincrono** | Profilatura della CPU a basso costo | `start`/`stop`/`serve`|
| **Tuft** | Profilazione runtime | `(p :tag (expr))`|
### Benchmarking con Criterium
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

### Tecniche di ottimizzazione
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

## Distribuzione
### Creazione di JAR Uber
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

### Distribuzione Docker
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

### Immagine nativa GraalVM
```bash
# Build with GraalVM for instant startup
native-image --no-fallback \
  --initialize-at-build-time \
  -jar target/my-app.jar \
  -o my-app-native

# Startup time: <50ms vs ~2s for JVM
```

---

## Quando utilizzare Lisp/Clojure
| Scenario | Perché Clojure | Alternativa migliore |
|----------|------------|-------------|
| Backend Web | Ring/Compojure sono produttivi | Vai, Node.js per API più semplici |
| Elaborazione dati | Eccellente libreria di sequenze | Pitone (Panda), Scala (Scintilla) |
| Sistemi concorrenti | Dati immutabili + STM | Vai, Erlang/Elisir |
| DSL / estensione linguistica | Le macro non hanno eguali | — |
| Sviluppo guidato da REPL | Flusso di lavoro interattivo migliore della categoria | — |
| Sviluppo di applicazioni generali | Possibile ma di nicchia | Python, Java, Vai |
| App mobili | ClojureScript per app Web; non nativo | Veloce, Kotlin |
| Scienza dei dati | Non l'ecosistema | Pitone, R |
---

## Domande e risposte sintetiche
### D1: Perché i programmi Lisp/Clojure hanno così tante parentesi?
**R:** Le parentesi rappresentano le espressioni S, una sintassi uniforme in cui codice e dati hanno la stessa struttura (omoiconicità):
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

### D2: In che modo Clojure gestisce lo stato e la mutabilità in modo diverso?
**R:** Clojure utilizza per impostazione predefinita dati immutabili. Per i cambiamenti di stato controllati, fornisce tipi di riferimento:
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

### D3: Quali sono le strutture dati persistenti di Clojure?
**R:** Tutte le raccolte Clojure sono persistenti (immutabili, strutturalmente condivise):
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

### D4: Come funzionano le macro Clojure?
**R:** Le macro ricevono codice non valutato (come dati), lo trasformano e restituiscono un nuovo codice:
```clojure
(defmacro unless [condition & body]
  `(if (not ~condition)
     (do ~@body)))

;; Usage
(unless false
  (println "This runs!"))
```

### D5: Come gestisco la concorrenza in Clojure?
**R:** Clojure fornisce più primitive di concorrenza:
- `atom`: modifiche indipendenti e sincrone
-`ref`+ `dosync`: modifiche transazionali coordinate
- `agent`: modifiche asincrone e indipendenti
- Canali `core.async`: concorrenza in stile CSP
---

## Risoluzione dei problemi basati sulla catena di pensiero
### Problema 1: elaborazione di una pipeline di dati
**Passaggio 1: comprendere il problema**
Leggi i dati, filtrali, trasformali e aggregali tramite una pipeline.
**Passaggio 2: identificare l'approccio**
Utilizza le macro di filettatura Clojure (`->>`) e i trasduttori.
**Passaggio 3: implementazione**```clojure
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

**Passaggio 4: ottimizza**
I trasduttori evitano di creare sequenze intermedie: compongono le trasformazioni in un unico passaggio.
### Problema 2: costruire un semplice server Web
**Passaggio 1: comprendere il problema**
Crea un server HTTP di base utilizzando Ring/Compojure.
**Passaggio 2: identificare l'approccio**
Utilizza l'adattatore Ring e il routing Compojure.
**Passaggio 3: implementazione**```clojure
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

**Passaggio 4: Estendi**
Aggiungi middleware per la registrazione, l'analisi JSON, l'autenticazione e la gestione degli errori.
---

## Riepilogo
Lisp è il nonno della progettazione dei linguaggi di programmazione: la maggior parte dei linguaggi moderni prende in prestito idee di cui Lisp è stato il pioniere decenni fa. Clojure porta Lisp nell'era moderna con immutabilità, supporto della concorrenza e integrazione JVM perfetta. Sebbene Lisp/Clojure non sia mainstream, impararlo cambierà radicalmente il modo in cui pensi alla programmazione. Il macrosistema da solo vale l’investimento: rivela possibilità che altre lingue non possono eguagliare.