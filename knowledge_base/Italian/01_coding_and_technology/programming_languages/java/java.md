---
# Metadata
title: "Java"
description: "Comprehensive reference for the Java programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
| **Eccezioni verificate** | Forza la gestione delle eccezioni che potrebbero non essere recuperabili | Utilizza eccezioni non controllate o il pattern`Optional`|
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
| **Maven** | Automazione della creazione + gestione delle dipendenze | Basato su XML (`pom.xml`); standard di settore per le imprese |
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
| Giava17 | 2021 | **LTS** — Classi sigillate, corrispondenza di modelli per`instanceof`, record, blocchi di testo |
| Giava21 | 2023 | **LTS** — **Thread virtuali** (Project Loom), corrispondenza di modelli per`switch`, modelli di record |
| Giava25 | 2025 | **LTS**: modelli di stringhe, ulteriore corrispondenza di modelli, API di funzioni esterne |
Le versioni **LTS** (supporto a lungo termine) ricevono aggiornamenti per molti anni. Per la produzione, utilizzare Java 21 o versione successiva.
---

## Quando utilizzare Java
| Scenario | Perché Java | Alternativa migliore |
|----------|---------|-------------|
| Backend aziendali | Ecosistema enorme, Spring Boot, collaudato su larga scala | Kotlin (stessa JVM, meno dettagliata) |
| Sviluppo Android | Base di codice consolidata ed enorme | Kotlin (la scelta preferita di Google) |
| Big data (Hadoop, Spark, Kafka) | L'ecosistema è costruito su Java/Scala | Python per il lato della scienza dei dati |
| Sistemi finanziari | Prestazioni + affidabilità + strumenti maturi | -- |
| Microservizi | Spring Boot + framework nativi del cloud | Scegli servizi più semplici |
| Script semplici | Troppa cerimonia | Pitone, Shell |
| Strumenti CLI | Avvio lento | Vai, Ruggine |
---

## Riepilogo
Java è uno dei linguaggi di programmazione più importanti mai creati. Gestisce i sistemi bancari, i telefoni Android, le pipeline di big data e i backend aziendali di tutto il mondo. Modern Java (21+) è un linguaggio molto diverso da Java 8: è più conciso, più espressivo e sempre più competitivo con i linguaggi più recenti. L'ecosistema JVM (Kotlin, Scala, Clojure) estende ulteriormente la sua portata. Per lo sviluppo aziendale, Java rimane una scelta sicura e potente.