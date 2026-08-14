<!--
---
# Metadata
title: "Java"
description: "Comprehensive reference for the Java programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [java, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
#Giava
Java è un linguaggio di programmazione orientato agli oggetti tipizzato staticamente creato da James Gosling presso Sun Microsystems e rilasciato nel 1995. La sua filosofia di progettazione - "scrivi una volta, esegui ovunque" (WORA) - è ottenuta attraverso Java Virtual Machine (JVM), che consente l'esecuzione del codice Java compilato su qualsiasi piattaforma dotata di un'implementazione JVM. Java è uno dei linguaggi di programmazione più utilizzati nella storia, alla base dei backend aziendali, delle app Android, dei sistemi Big Data e dei servizi finanziari.
Nonostante abbia quasi 30 anni, Java continua ad evolversi. Java moderno (versioni 17+) include record, classi sigillate, corrispondenza di modelli, thread virtuali e un ecosistema in crescita che compete con i linguaggi più recenti.
---

## Perché Java è importante
- **Standard aziendale**: la spina dorsale dei backend Fortune 500: banche, assicurazioni, e-commerce, sanità.
- **Sviluppo Android**: il linguaggio principale per Android (insieme a Kotlin).
- **Ecosistema di big data**: Apache Hadoop, Spark, Kafka, Elasticsearch, tutti scritti in Java o Scala (che funziona sulla JVM).
- **Ecosistema enorme**: oltre 500.000 biblioteche su Maven Central; attrezzatura matura per ogni esigenza.
- **Prestazioni**: il compilatore JIT di JVM produce codice macchina altamente ottimizzato in fase di esecuzione, spesso corrispondente a C++ per applicazioni a lunga esecuzione.
- **Compatibilità con le versioni precedenti**: il codice scritto per Java 1.0 (1996) funziona ancora su JVM moderne.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Verbosità** | Richiede più boilerplate di Python, Kotlin o Go | Utilizza Lombok, record (Java 16+) e IDE moderni |
| **Utilizzo della memoria** | Il sovraccarico della JVM significa una memoria di base più elevata | Ottimizza i flag JVM; utilizzare immagini native GraalVM per piccole distribuzioni |
| **Tempo di avvio** | Il riscaldamento della JVM può essere lento per i processi di breve durata | Immagine nativa GraalVM oppure utilizza C/Go per gli strumenti CLI |
| **Eccezioni verificate** | Forza la gestione delle eccezioni che potrebbero non essere recuperabili | Utilizza eccezioni non selezionate o il modello`Optional`|
| **Nessun tipo di valore** | Tutto è un oggetto (fino al progetto Valhalla) | Utilizza raccolte specializzate primitive (Raccolte Eclipse, Trove) |
---

## Fondamenti di sintassi
### Struttura di base
Java è basato su classi: tutto vive all'interno di una classe. Il nome del file deve corrispondere al nome della classe pubblica.
```java
// HelloWorld.java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        
        String name = "Alice";
        int age = 30;
        double score = 9.5;
        boolean active = true;
        
        String greeting = String.format("Hello, %s! You are %d years old.", name, age);
        System.out.println(greeting);
    }
}
```

### Programmazione orientata agli oggetti
```java
public abstract class Animal {
    private final String name;
    
    protected Animal(String name) { this.name = name; }
    public String getName() { return name; }
    public abstract String speak();
}

public class Dog extends Animal {
    public Dog(String name) { super(name); }
    
    @Override
    public String speak() { return getName() + " says woof"; }
}

public interface Serializable {
    String toJson();
}

public class User implements Serializable, Comparable<User> {
    private final String name;
    private final int age;
    
    public User(String name, int age) { this.name = name; this.age = age; }
    
    @Override
    public String toJson() { return "{\"name\":\"" + name + "\",\"age\":" + age + "}"; }
    
    @Override
    public int compareTo(User other) { return Integer.compare(this.age, other.age); }
}
```

### Records (Java 16+): classi di dati concise
```java
public record Point(double x, double y) {
    public Point {
        if (Double.isNaN(x) || Double.isNaN(y)) {
            throw new IllegalArgumentException("Coordinates cannot be NaN");
        }
    }
    
    public double distanceTo(Point other) {
        return Math.sqrt(Math.pow(x - other.x, 2) + Math.pow(y - other.y, 2));
    }
}

Point p1 = new Point(3.0, 4.0);
Point p2 = new Point(0.0, 0.0);
System.out.println(p1.distanceTo(p2));  // 5.0
```

### Raccolte e flussi
```java
import java.util.*;
import java.util.stream.*;

List<String> names = new ArrayList<>(List.of("Alice", "Bob", "Charlie"));

// Stream API — functional-style data processing
List<String> filtered = names.stream()
    .filter(name -> name.length() > 3)
    .map(String::toUpperCase)
    .sorted()
    .collect(Collectors.toList());

// Grouping
Map<Integer, List<String>> byLength = names.stream()
    .collect(Collectors.groupingBy(String::length));

// Optional — avoid null pointer exceptions
Optional<String> findUser(String name) {
    return Optional.ofNullable(userDatabase.get(name));
}
```

### Gestione delle eccezioni
```java
public void readFile(String path) throws IOException {
    try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
    }
}

public class InsufficientFundsException extends Exception {
    private final double balance;
    private final double amount;
    
    public InsufficientFundsException(double balance, double amount) {
        super(String.format("Cannot withdraw $%.2f from $%.2f", amount, balance));
        this.balance = balance;
        this.amount = amount;
    }
}
```

---

## Sintassi e modelli avanzati
### Generici
```java
// Generic class
public class Box<T> {
    private T value;
    
    public Box(T value) { this.value = value; }
    public T get() { return value; }
    public <U> Box<U> map(Function<T, U> mapper) {
        return new Box<>(mapper.apply(value));
    }
}

// Bounded type parameters
public <T extends Comparable<T>> T findMax(List<T> items) {
    return items.stream().reduce(items.get(0), (a, b) -> a.compareTo(b) >= 0 ? a : b);
}

// Wildcards
public static void printAll(List<?> items) {
    items.forEach(System.out::println);
}

// Generic method with multiple bounds
public <T extends Serializable & Comparable<T>> void store(T item) {
    // T must implement both Serializable and Comparable
}
```

### Classi sigillate e corrispondenza di modelli (Java 17+)
```java
// Sealed classes — restrict which classes can extend
public sealed interface Shape permits Circle, Rectangle, Triangle {}

public record Circle(double radius) implements Shape {}
public record Rectangle(double width, double height) implements Shape {}
public record Triangle(double base, double height) implements Shape {}

// Pattern matching with switch (Java 21+)
public static double area(Shape shape) {
    return switch (shape) {
        case Circle c    -> Math.PI * c.radius() * c.radius();
        case Rectangle r -> r.width() * r.height();
        case Triangle t  -> 0.5 * t.base() * t.height();
    };
}

// Pattern matching for instanceof (Java 16+)
if (obj instanceof String s) {
    System.out.println("String of length: " + s.length());
}
```

### Annotazioni
```java
// Custom annotation
import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Retry {
    int maxAttempts() default 3;
    long delayMs() default 1000;
}

// Using the annotation
@Retry(maxAttempts = 5, delayMs = 500)
public void connectToDatabase() throws Exception {
    // Connection logic
}

// Processing annotations at runtime
public static void invokeWithRetry(Object target, Method method) throws Exception {
    Retry retry = method.getAnnotation(Retry.class);
    if (retry == null) {
        method.invoke(target);
        return;
    }
    
    for (int i = 0; i < retry.maxAttempts(); i++) {
        try {
            method.invoke(target);
            return;
        } catch (Exception e) {
            if (i == retry.maxAttempts() - 1) throw e;
            Thread.sleep(retry.delayMs());
        }
    }
}
```

### Interfacce funzionali e lambda
```java
// Built-in functional interfaces
Function<String, Integer> parseLength = s -> s.length();
Predicate<Integer> isEven = n -> n % 2 == 0;
Consumer<String> printer = s -> System.out.println(s);
Supplier<List<String>> listFactory = ArrayList::new;
BiFunction<Integer, Integer, Integer> adder = Integer::sum;

// Method references
List<String> names = List.of("Alice", "Bob", "Charlie");
names.forEach(System.out::println);          // Reference to instance method
names.stream().map(String::toUpperCase);     // Reference to instance method
names.stream().map(Integer::valueOf);        // Reference to static method

// Custom functional interface
@FunctionalInterface
public interface Transformer<T, R> {
    R transform(T input);
    
    // Default method
    default <V> Transformer<T, V> andThen(Transformer<R, V> after) {
        return input -> after.transform(this.transform(input));
    }
}
```

---

## Concorrenza e parallelismo
### Thread virtuali (Java 21+)
```java
// Virtual threads — lightweight, managed by the JVM (not OS)
// Can create millions of concurrent virtual threads
public void handleRequests(List<URL> urls) throws Exception {
    try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
        List<Future<String>> futures = urls.stream()
            .map(url -> executor.submit(() -> {
                try (var in = url.openStream()) {
                    return new String(in.readAllBytes());
                }
            }))
            .toList();
        
        for (var future : futures) {
            String html = future.get();
            System.out.println("Fetched " + html.length() + " bytes");
        }
    }
}

// Creating a single virtual thread
Thread.startVirtualThread(() -> {
    System.out.println("Running in virtual thread: " + Thread.currentThread());
});
```

### Threading e sincronizzazione tradizionali
```java
// Thread pool for CPU-bound tasks
ExecutorService cpuPool = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());

// CompletableFuture — composable async operations
CompletableFuture.supplyAsync(() -> fetchUser(1))
    .thenApplyAsync(user -> enrichUser(user))
    .thenAccept(user -> System.out.println(user))
    .exceptionally(ex -> {
        System.err.println("Failed: " + ex.getMessage());
        return null;
    });

// Combining futures
CompletableFuture<String> nameFuture = CompletableFuture.supplyAsync(() -> "Alice");
CompletableFuture<Integer> ageFuture = CompletableFuture.supplyAsync(() -> 30);

nameFuture.thenCombine(ageFuture, (name, age) -> name + " (age " + age + ")")
    .thenAccept(System.out::println);

// Synchronisation primitives
ReentrantLock lock = new ReentrantLock();
ConcurrentHashMap<String, Integer> cache = new ConcurrentHashMap<>();
CountDownLatch latch = new CountDownLatch(3);
Semaphore semaphore = new Semaphore(5);
```

---

## Configurazione del progetto e sistema di creazione
### Struttura del progetto (Maven)
```
my-java-project/
├── src/
│   ├── main/
│   │   ├── java/com/example/
│   │   │   ├── Application.java
│   │   │   ├── model/
│   │   │   ├── service/
│   │   │   └── controller/
│   │   └── resources/
│   │       └── application.properties
│   └── test/java/com/example/
│       └── service/
├── pom.xml
├── .github/workflows/ci.yml
└── README.md
```

### pom.xml (Maven)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
            <version>32.1.3-jre</version>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

### build.gradle.kts (Gradle)
```kotlin
plugins {
    java
    application
}

group = "com.example"
version = "1.0.0"

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(21))
    }
}

repositories { mavenCentral() }

dependencies {
    implementation("com.google.guava:guava:32.1.3-jre")
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.1")
    testImplementation("org.mockito:mockito-core:5.7.0")
}

application {
    mainClass.set("com.example.Application")
}

tasks.test { useJUnitPlatform() }
```

### Pipeline CI/CD
```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: "temurin"
          java-version: "21"
          cache: "maven"
      - run: mvn verify
      - run: mvn package -DskipTests
```

---

## Test
### JUnit 5 con Mockito
```java
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class UserServiceTest {
    private UserRepository mockRepo;
    private UserService service;

    @BeforeEach
    void setUp() {
        mockRepo = mock(UserRepository.class);
        service = new UserService(mockRepo);
    }

    @Test
    @DisplayName("Should create user with valid data")
    void createUser_validData_success() {
        when(mockRepo.save(any(User.class))).thenAnswer(inv -> {
            User u = inv.getArgument(0);
            return new User(1, u.name(), u.email());
        });

        User user = service.create("Alice", "alice@example.com");

        assertEquals("Alice", user.name());
        verify(mockRepo).save(any(User.class));
    }

    @Test
    void findById_existingUser_returnsUser() {
        when(mockRepo.findById(1)).thenReturn(Optional.of(new User(1, "Alice", "a@b.com")));
        Optional<User> result = service.findById(1);
        assertTrue(result.isPresent());
        assertEquals("Alice", result.get().name());
    }

    @Test
    void findById_nonExisting_returnsEmpty() {
        when(mockRepo.findById(999)).thenReturn(Optional.empty());
        assertTrue(service.findById(999).isEmpty());
    }

    @ParameterizedTest
    @ValueSource(strings = {"", "  ", "a"})
    void create_invalidName_throws(String name) {
        assertThrows(IllegalArgumentException.class, () -> service.create(name, "a@b.com"));
    }
}
```

---

## Interoperabilità
### JNI (interfaccia nativa Java)
```java
// Calling native C code from Java
public class NativeMath {
    static { System.loadLibrary("nativemath"); }
    
    public native int add(int a, int b);
    public native double sqrt(double value);
}

// Compile: javac -h . NativeMath.java
// Then compile the generated C header with your C implementation
```

### API di funzioni e memoria esterne (Java 22+)
```java
// Modern alternative to JNI — no C header needed
try (var arena = Arena.ofConfined()) {
    // Load C standard library
    SymbolLookup stdlib = Linker.nativeLinker().defaultLookup();
    MethodHandle strlen = Linker.nativeLinker().downcallHandle(
        stdlib.find("strlen").orElseThrow(),
        FunctionDescriptor.of(JAVA_LONG, ADDRESS)
    );
    
    // Call C function
    MemorySegment str = arena.allocateFrom("Hello, World!");
    long length = (long) strlen.invoke(str);
    System.out.println("Length: " + length);  // 13
}
```

---

## Modelli di progettazione
### Modello di creazione
```java
public class HttpRequest {
    private final String method;
    private final String url;
    private final Map<String, String> headers;
    private final String body;

    private HttpRequest(Builder builder) {
        this.method = builder.method;
        this.url = builder.url;
        this.headers = Map.copyOf(builder.headers);
        this.body = builder.body;
    }

    public static class Builder {
        private String method = "GET";
        private String url = "";
        private final Map<String, String> headers = new HashMap<>();
        private String body = null;

        public Builder method(String m) { this.method = m; return this; }
        public Builder url(String u) { this.url = u; return this; }
        public Builder header(String k, String v) { headers.put(k, v); return this; }
        public Builder body(String b) { this.body = b; return this; }
        public HttpRequest build() { return new HttpRequest(this); }
    }
}

// Usage
HttpRequest request = new HttpRequest.Builder()
    .method("POST").url("/api/users")
    .header("Content-Type", "application/json")
    .body("{\"name\":\"Alice\"}")
    .build();
```

### Modello dell'osservatore
```java
public interface EventListener<T> {
    void onEvent(T event);
}

public class EventBus<T> {
    private final List<EventListener<T>> listeners = new CopyOnWriteArrayList<>();

    public void subscribe(EventListener<T> listener) { listeners.add(listener); }
    public void unsubscribe(EventListener<T> listener) { listeners.remove(listener); }
    public void publish(T event) { listeners.forEach(l -> l.onEvent(event)); }
}
```

---

## Prestazioni e ottimizzazione
### Strumenti di profilazione
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### Tecniche di ottimizzazione
```java
// Use StringBuilder for string concatenation in loops
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append("item").append(i).append(",");
}
String result = sb.toString();

// Use primitive streams for numeric operations
int sum = IntStream.rangeClosed(1, 1_000_000).sum();

// Use EnumSet/EnumMap for enum-based collections
EnumSet<DayOfWeek> weekdays = EnumSet.range(DayOfWeek.MONDAY, DayOfWeek.FRIDAY);
```

---

## Distribuzione
###Dockerfile
```dockerfile
FROM eclipse-temurin:21-jdk-alpine AS builder
WORKDIR /app
COPY . .
RUN ./mvnw package -DskipTests

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

## L'ecosistema
### Strumenti di creazione
| Strumento | Scopo | Note |
|------|---------|-------|
| **Maven** | Automazione della creazione + gestione delle dipendenze | Basato su XML (`pom.xml`); standard industriale per le imprese |
| **Gradle** | Automazione della creazione + gestione delle dipendenze | ADSL Groovy/Kotlin; più veloce per progetti di grandi dimensioni; utilizzato da Android |
### Quadri
| Quadro | Dominio | Descrizione |
|-----------|--------|-----|
| **Stivale primaverile** | Web/impresa | Il framework Java dominante: API REST, microservizi, sicurezza, accesso ai dati |
| **Giacarta EE** | Impresa | Successore di Java EE; API aziendali standardizzate |
| **Ibernazione** | ORMA | Mappatura relazionale degli oggetti; l'attuazione standard dell'APP |
| **Micronauta / Quarkus** | Nativo del cloud | Avvio rapido, memoria ridotta: progettato per serverless e contenitori |
### Test
| Strumento | Scopo |
|------|---------|
| **JUnità 5** | Quadro di test unitario |
| **Mockito** | Quadro beffardo |
| **AffermareJ** | Affermazioni fluenti |
| **Contenitori di prova** | Test di integrazione con database reali in Docker |
---

## L'ecosistema JVM
| Linguaggio JVM | Relazione con Java |
|-------------|---------------------|
| **Kotlin** | Alternativa moderna a Java; La lingua Android preferita da Google; Compatibile con Java al 100% |
| **Scala** | Ibrido funzionale + OOP; poteri Apache Spark |
| **Clojure** | Dialetto Lisp sulla JVM; programmazione funzionale |
| **Fantastico** | Scripting dinamico per la JVM; utilizzato nei file di build Gradle |
Tutti questi possono utilizzare le librerie Java e Java può utilizzare le loro librerie. La JVM è la piattaforma, non solo Java.
---

## Versioni Java
| Versione | Anno | Caratteristiche principali |
|---------|------|-----|
| Giava8 | 2014| **LTS**: Lambda, API Stream, facoltativi, metodi predefiniti. Ancora ampiamente utilizzato. |
| Giava11 | 2018 | **LTS**: API client HTTP,`var`per variabili locali, launcher di origine a file singolo |
| Giava17 | 2021 | **LTS** — Classi sigillate, corrispondenza di modelli per `instanceof`, record, blocchi di testo |
| Giava21 | 2023 | **LTS** — **Thread virtuali** (Project Loom), corrispondenza di modelli per `switch`, record di modelli |
| Giava25 | 2025 | **LTS**: modelli di stringhe, ulteriore corrispondenza di modelli, API di funzioni esterne |
Le versioni **LTS** (supporto a lungo termine) ricevono aggiornamenti per molti anni. Per la produzione, utilizzare Java 21 o versione successiva.
---

## Quando utilizzare Java
| Scenario | Perché Java | Alternativa migliore |
|----------|---------|-------------|
| Backend aziendali | Ecosistema enorme, Spring Boot, dimostrato su larga scala | Kotlin (stessa JVM, meno dettagliata) |
| Sviluppo Android | Base di codice consolidata ed enorme | Kotlin (la scelta preferita di Google) |
| Big data (Hadoop, Spark, Kafka) | L'ecosistema è costruito su Java/Scala | Python per il lato della scienza dei dati |
| Sistemi finanziari | Prestazioni + affidabilità + strumenti maturi | -- |
| Microservizi | Spring Boot + framework nativi del cloud | Scegli servizi più semplici |
| Script semplici | Troppa cerimonia | Pitone, Shell |
| Strumenti CLI | Avvio lento | Vai, Ruggine |
---

## Domande e risposte sintetiche
### D1: Qual è la differenza tra`==`e`.equals()`in Java?
**R:**`==`confronta i riferimenti agli oggetti (identità) — controlla se due variabili puntano allo stesso oggetto in memoria. `.equals()`confronta il contenuto dell'oggetto (uguaglianza dei valori). Per le primitive (`int`,`double`),`==`confronta direttamente i valori. Per gli oggetti (incluso`String`), utilizzare sempre`.equals()`per confrontare il contenuto. L'unica eccezione è il confronto con`null`, dove`==`è corretto.
```java
String a = new String("hello");
String b = new String("hello");
System.out.println(a == b);       // false — different objects
System.out.println(a.equals(b));  // true — same content

// String pool — literals are interned
String c = "hello";
String d = "hello";
System.out.println(c == d);       // true — same pooled object

// Always use .equals() for value comparison, or Objects.equals() for null-safe comparison
Objects.equals(a, b);  // Handles nulls without NPE
```

### D2: Come funziona il garbage collector JVM e quale dovrei utilizzare?
**R:** Il GC recupera automaticamente la memoria dagli oggetti che non sono più raggiungibili. Le JVM moderne (21+) offrono diversi raccoglitori: G1 (predefinito, bilanciato), ZGC (tempi di pausa ultra bassi, <1 ms) e Shenandoah (pausa bassa, OpenJDK). Per la maggior parte delle applicazioni, il G1 predefinito va bene. Per i servizi sensibili alla latenza, utilizzare ZGC (`-XX:+UseZGC`). Per l'elaborazione batch orientata alla produttività, utilizzare Parallel GC (`-XX:+UseParallelGC`).
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### D3: Quando dovrei utilizzare`Stream API`rispetto ai loop tradizionali?
**R:** Utilizza gli Stream quando l'operazione è una pipeline chiara (filtra, mappa, riduci): esprimono meglio l'intento e si parallelizzano facilmente con`.parallelStream()`. Utilizza i cicli tradizionali per iterazioni semplici, quando è necessario modificare lo stato esterno, quando le prestazioni sono critiche (i flussi hanno un sovraccarico) o quando la logica implica un flusso di controllo complesso (interruzione, continuazione, ritorni multipli). Evita i flussi per operazioni`for-each`semplici.
```java
// Stream — clear pipeline, easy to read
List<String> names = people.stream()
    .filter(p -> p.age() > 18)
    .sorted(Comparator.comparing(Person::name))
    .map(Person::name)
    .toList();

// Traditional loop — better for complex logic or side effects
int maxAge = 0;
String oldestName = null;
for (Person p : people) {
    if (p.age() > maxAge) {
        maxAge = p.age();
        oldestName = p.name();
    }
}
```

### D4: Cosa sono i record, le classi sigillate e la corrispondenza dei modelli nel Java moderno?
**R:** I record (Java 16) sono supporti dati immutabili: generano automaticamente costruttori, getter,`equals`,`hashCode`e`toString`. Le classi sigillate (Java 17) limitano quali classi possono estenderle, utili per modellare gerarchie di tipi finiti. La corrispondenza dei modelli (Java 21) consente alle espressioni`switch`di destrutturare tipi, record e valori, sostituendo le catene`instanceof`dettagliate.
```java
// Record — immutable data class
public record Point(int x, int y) {
    // Compact constructor for validation
    public Point {
        if (x < 0 || y < 0) throw new IllegalArgumentException();
    }
}

// Sealed interface + pattern matching
public sealed interface Shape permits Circle, Rectangle, Triangle {}
public record Circle(double radius) implements Shape {}
public record Rectangle(double width, double height) implements Shape {}
public record Triangle(double base, double height) implements Shape {}

// Pattern matching switch (Java 21)
static double area(Shape shape) {
    return switch (shape) {
        case Circle(var r)       -> Math.PI * r * r;
        case Rectangle(var w, var h) -> w * h;
        case Triangle(var b, var h) -> 0.5 * b * h;
    };
}
```

### D5: Come posso gestire correttamente le eccezioni selezionate e non selezionate?
**R:** Le eccezioni selezionate (`IOException`,`SQLException`) devono essere dichiarate in`throws`o intercettate: rappresentano condizioni recuperabili di cui il chiamante dovrebbe essere a conoscenza. Le eccezioni non controllate (sottoclassi`RuntimeException`come `NullPointerException`, `IllegalArgumentException`) rappresentano bug di programmazione. Migliore pratica: utilizzare le eccezioni controllate con parsimonia (creano accoppiamento), preferire`Optional`per l'assenza prevista e racchiudere le eccezioni controllate in quelle non controllate quando si oltrepassano i limiti dell'API.
```java
// Prefer Optional over checked exception for expected absence
public Optional<User> findUser(String id) {
    return Optional.ofNullable(userRepository.findById(id));
}

// Wrap checked exceptions for cleaner APIs
public User getUser(String id) {
    try {
        return findUser(id).orElseThrow(
            () -> new UserNotFoundException("User not found: " + id));
    } catch (IOException e) {
        throw new UncheckedIOException(e);
    }
}

// Try-with-resources — automatic resource cleanup
try (var conn = dataSource.getConnection();
     var stmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?")) {
    stmt.setString(1, id);
    try (var rs = stmt.executeQuery()) {
        if (rs.next()) return mapUser(rs);
    }
}
```

---

## Risoluzione dei problemi basati sulla catena di pensiero
### Problema 1: costruire una pipeline produttore-consumatore thread-safe
**Dichiarazione del problema:** Progetta una pipeline produttore-consumatore in Java in cui più produttori generano elementi di lavoro, più consumatori li elaborano contemporaneamente e il sistema supporta l'arresto regolare con lo svuotamento degli elementi rimanenti.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) una coda delimitata per bufferizzare gli elementi di lavoro tra produttori e consumatori, (2) più thread di produttori che aggiungono elementi, (3) più thread di consumatori che elaborano elementi, (4) un meccanismo per segnalare l'arresto e drenare gli elementi rimanenti.`BlockingQueue`di Java è stato creato appositamente per questo.
**Passaggio 2: identificare l'approccio:**
- Utilizzare`ArrayBlockingQueue`(limitato) per impedire una crescita illimitata della memoria.
- Utilizzare un modello di pillola avvelenata per la segnalazione di spegnimento.
- Utilizzare`ExecutorService`per la gestione del pool di thread.
- Utilizzare`CountDownLatch`per attendere che tutti i consumatori finiscano di svuotarsi.
**Passaggio 3: implementa la soluzione:**
```java
import java.util.concurrent.*;

public class Pipeline<T> {
    private final BlockingQueue<T> queue;
    private final ExecutorService producers;
    private final ExecutorService consumers;
    private final CountDownLatch shutdownLatch;
    private static final Object POISON_PILL = new Object();

    public Pipeline(int producerCount, int consumerCount, int queueCapacity) {
        this.queue = new ArrayBlockingQueue<>(queueCapacity);
        this.producers = Executors.newFixedThreadPool(producerCount);
        this.consumers = Executors.newFixedThreadPool(consumerCount);
        this.shutdownLatch = new CountDownLatch(consumerCount);
    }

    public void start(Function<T, Void> processor) {
        // Start consumers
        for (int i = 0; i < shutdownLatch.getCount(); i++) {
            final int id = i;
            consumers.submit(() -> {
                try {
                    while (true) {
                        T item = queue.poll(1, TimeUnit.SECONDS);
                        if (item == null) continue;
                        if (item == POISON_PILL) break;
                        processor.apply(item);
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                } finally {
                    shutdownLatch.countDown();
                }
            });
        }
    }

    public void submit(T item) throws InterruptedException {
        queue.put(item);  // Blocks if queue is full
    }

    public void shutdown() throws InterruptedException {
        // Send poison pills — one per consumer
        for (int i = 0; i < shutdownLatch.getCount(); i++) {
            queue.put((T) POISON_PILL);
        }
        // Wait for all items to be processed
        shutdownLatch.await(30, TimeUnit.SECONDS);
        producers.shutdown();
        consumers.shutdown();
    }
}
```

**Passaggio 4: verifica e ottimizzazione:**
- La coda delimitata impedisce OOM:`ArrayBlockingQueue(1000)`limita la memoria.
- Modello pillola avvelenata: ogni consumatore esce in modo pulito dopo aver ricevuto la sua pillola.
-`poll(1, SECONDS)`con timeout impedisce ai consumatori di bloccarsi per sempre se i produttori sono lenti.
- Produzione: utilizzare`LinkedBlockingQueue`per pipeline illimitate o`Disruptor`(LMAX) per pipeline a latenza ultra bassa.
### Problema 2: implementare un validatore personalizzato basato su annotazioni
**Dichiarazione del problema:** Crea un framework di convalida utilizzando annotazioni personalizzate. Gli utenti annotano i campi con`@NotNull`,`@Min(0)`,`@Max(100)`,`@Size(min=1, max=50)`e chiamano`Validator.validate(obj)`per ottenere un elenco di violazioni.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) annotazioni personalizzate con parametri, (2) un validatore basato sulla riflessione che legga le annotazioni in fase di esecuzione, (3) un oggetto risultato contenente tutti gli errori di convalida. Ciò dimostra le capacità di elaborazione e riflessione delle annotazioni di Java.
**Passaggio 2: identificare l'approccio:**
- Definisci annotazioni con`@Retention(RUNTIME)`e`@Target(FIELD)`.
- Utilizzare`Class.getDeclaredFields()`per scorrere i campi.
- Utilizzare`Field.getAnnotation()`per leggere i valori delle annotazioni.
- Confronta i valori dei campi con i vincoli di annotazione.
- Raccogliere le violazioni in un elenco.
**Passaggio 3: implementa la soluzione:**
```java
// Annotations
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
@interface NotNull { String message() default "must not be null"; }

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
@interface Min { long value(); String message() default "must be >= {value}"; }

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
@interface Max { long value(); String message() default "must be <= {value}"; }

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
@interface Size { int min() default 0; int max() default Integer.MAX_VALUE; }

// Violation record
record Violation(String field, String message) {}

// Validator
public class Validator {
    public static List<Violation> validate(Object obj) {
        List<Violation> violations = new ArrayList<>();
        for (Field field : obj.getClass().getDeclaredFields()) {
            field.setAccessible(true);
            try {
                Object value = field.get(obj);
                String name = field.getName();

                if (field.isAnnotationPresent(NotNull.class) && value == null) {
                    violations.add(new Violation(name, "must not be null"));
                }

                if (value instanceof Number num) {
                    Min min = field.getAnnotation(Min.class);
                    if (min != null && num.longValue() < min.value()) {
                        violations.add(new Violation(name,
                            "must be >= " + min.value()));
                    }
                    Max max = field.getAnnotation(Max.class);
                    if (max != null && num.longValue() > max.value()) {
                        violations.add(new Violation(name,
                            "must be <= " + max.value()));
                    }
                }

                if (value instanceof String str) {
                    Size size = field.getAnnotation(Size.class);
                    if (size != null) {
                        if (str.length() < size.min() || str.length() > size.max()) {
                            violations.add(new Violation(name,
                                "length must be between " + size.min() + " and " + size.max()));
                        }
                    }
                }
            } catch (IllegalAccessException e) {
                throw new RuntimeException(e);
            }
        }
        return violations;
    }
}

// Usage
public class UserForm {
    @NotNull
    String name;
    @Min(0) @Max(150)
    int age;
    @Size(min = 5, max = 100)
    String email;
}

List<Violation> errors = Validator.validate(new UserForm(null, -1, "ab"));
// [Violation[field=name, message=must not be null],
//  Violation[field=age, message=must be >= 0],
//  Violation[field=email, message=length must be between 5 and 100]]
```

**Passaggio 4: verifica e ottimizzazione:**
- Overhead di riflessione: accettabile per la convalida (chiamato una volta per richiesta). Per percorsi attivi, memorizza nella cache le ricerche dei campi o utilizza l'elaborazione delle annotazioni in fase di compilazione (come Hibernate Validator).
- Estensibilità: aggiungi nuove annotazioni creando l'annotazione + un blocco gestore in`validate()`.
- Produzione: utilizza`jakarta.validation`(Bean Validation 3.0) — fa tutto questo e altro ancora, con elaborazione in fase di compilazione tramite processori di annotazione.
### Problema 3: creare un client HTTP a velocità limitata con Riprova
**Dichiarazione del problema:** crea un wrapper client HTTP che ritenta automaticamente le richieste non riuscite con backoff esponenziale, rispetta i limiti di velocità e supporta l'interruzione del circuito (interrompe la chiamata a un servizio in errore).
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) logica di ripetizione con backoff e jitter esponenziali, (2) limitazione della velocità per evitare di sovraccaricare il servizio di destinazione, (3) modello di interruttore: dopo N guasti consecutivi, interrompere la chiamata al servizio per un periodo di raffreddamento. Queste sono tre preoccupazioni componibili.
**Passaggio 2: identificare l'approccio:**
- Utilizza`java.net.http.HttpClient`(Java 11+) come client di base.
- Implementare il nuovo tentativo come wrapper con`Thread.sleep`per il backoff.
- Utilizzare`Semaphore`per la limitazione della velocità (o`java.time`per il bucket di token).
- Implementare l'interruttore come una macchina a stati: CHIUSO → APERTO → MEZZA_APERTA.
**Passaggio 3: implementa la soluzione:**
```java
import java.net.http.*;
import java.time.Duration;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;

public class ResilientClient {
    private final HttpClient client;
    private final int maxRetries;
    private final Semaphore rateLimiter;
    private final AtomicInteger consecutiveFailures;
    private final AtomicLong openUntil;
    private final int failureThreshold;
    private final long cooldownMs;

    public ResilientClient(int maxRetries, int requestsPerSecond,
                           int failureThreshold, long cooldownMs) {
        this.client = HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(10))
            .build();
        this.maxRetries = maxRetries;
        this.rateLimiter = new Semaphore(requestsPerSecond);
        this.consecutiveFailures = new AtomicInteger(0);
        this.openUntil = new AtomicLong(0);
        this.failureThreshold = failureThreshold;
        this.cooldownMs = cooldownMs;

        // Replenish semaphore permits every second
        Executors.newSingleThreadScheduledExecutor(r -> {
            Thread t = new Thread(r, "rate-limiter");
            t.setDaemon(true);
            return t;
        }).scheduleAtFixedRate(() -> {
            int drain = requestsPerSecond - rateLimiter.availablePermits();
            if (drain > 0) rateLimiter.release(drain);
        }, 1, 1, TimeUnit.SECONDS);
    }

    public HttpResponse<String> send(HttpRequest request) throws Exception {
        // Circuit breaker check
        if (System.currentTimeMillis() < openUntil.get()) {
            throw new CircuitOpenException("Circuit breaker is open");
        }

        Exception lastException = null;
        for (int attempt = 0; attempt <= maxRetries; attempt++) {
            try {
                rateLimiter.acquire();  // Wait for rate limit permit
                HttpResponse<String> response = client.send(request,
                    HttpResponse.BodyHandlers.ofString());

                if (response.statusCode() >= 500) {
                    throw new ServerException("HTTP " + response.statusCode());
                }

                // Success — reset failure counter
                consecutiveFailures.set(0);
                return response;

            } catch (Exception e) {
                lastException = e;
                int failures = consecutiveFailures.incrementAndGet();

                if (failures >= failureThreshold) {
                    openUntil.set(System.currentTimeMillis() + cooldownMs);
                    throw new CircuitOpenException(
                        "Circuit opened after " + failures + " failures");
                }

                if (attempt < maxRetries) {
                    long delay = (long) Math.pow(2, attempt) * 100;
                    long jitter = ThreadLocalRandom.current().nextLong(0, delay / 2);
                    Thread.sleep(delay + jitter);
                }
            }
        }
        throw lastException;
    }
}
```

**Passaggio 4: verifica e ottimizzazione:**
- Il backoff esponenziale con jitter impedisce un gregge tuonante (tutti i tentativi colpiscono contemporaneamente).
- Interruttore automatico: dopo guasti consecutivi di `failureThreshold`, il circuito si apre per`cooldownMs`— non vengono inviate richieste, proteggendo il servizio in errore.
- Limitatore di velocità:`Semaphore`con limiti di rifornimento periodico.
- Produzione: utilizza `resilience4j`: fornisce tutti e tre i modelli (riprova, limitatore di velocità, interruttore automatico) con implementazioni, metriche e integrazione Spring Boot adeguate.
---

## Riepilogo
Java è uno dei linguaggi di programmazione più importanti mai creati. Gestisce i sistemi bancari, i telefoni Android, le pipeline di big data e i backend aziendali di tutto il mondo. Modern Java (21+) è un linguaggio molto diverso da Java 8: è più conciso, più espressivo e sempre più competitivo con i linguaggi più recenti. L'ecosistema JVM (Kotlin, Scala, Clojure) estende ulteriormente la sua portata. Per lo sviluppo aziendale, Java rimane una scelta sicura e potente.