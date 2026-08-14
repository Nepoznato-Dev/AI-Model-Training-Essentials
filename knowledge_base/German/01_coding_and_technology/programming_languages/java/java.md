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
# Java
Java ist eine statisch typisierte, objektorientierte Programmiersprache, die von James Gosling bei Sun Microsystems entwickelt und 1995 veröffentlicht wurde. Ihre Designphilosophie – „Einmal schreiben, überall ausführen“ (WORA) – wird durch die Java Virtual Machine (JVM) erreicht, die es ermöglicht, kompilierten Java-Code auf jeder Plattform auszuführen, die über eine JVM-Implementierung verfügt. Java ist eine der am weitesten verbreiteten Programmiersprachen der Geschichte und unterstützt Unternehmens-Backends, Android-Apps, Big-Data-Systeme und Finanzdienstleistungen.
Obwohl Java fast 30 Jahre alt ist, entwickelt es sich weiter. Modernes Java (Versionen 17+) umfasst Datensätze, versiegelte Klassen, Mustervergleich, virtuelle Threads und ein wachsendes Ökosystem, das mit neueren Sprachen konkurriert.
---

## Warum Java wichtig ist
- **Unternehmensstandard**: Das Rückgrat der Fortune-500-Backends – Banken, Versicherungen, E-Commerce, Gesundheitswesen.
- **Android-Entwicklung**: Die primäre Sprache für Android (neben Kotlin).
- **Big-Data-Ökosystem**: Apache Hadoop, Spark, Kafka, Elasticsearch – alle geschrieben in Java oder Scala (das auf der JVM läuft).
- **Massives Ökosystem**: Über 500.000 Bibliotheken auf Maven Central; ausgereifte Werkzeuge für jeden Bedarf.
- **Leistung**: Der JIT-Compiler von JVM erzeugt zur Laufzeit hochoptimierten Maschinencode, der oft mit C++ für lang laufende Anwendungen übereinstimmt.
- **Abwärtskompatibilität**: Für Java 1.0 (1996) geschriebener Code läuft immer noch auf modernen JVMs.
## Die Kompromisse
| Einschränkung | Einzelheiten | Typische Problemumgehung |
|-----------|---------|-----|
| **Ausführlichkeit** | Erfordert mehr Boilerplate als Python, Kotlin oder Go | Verwenden Sie Lombok, Records (Java 16+) und moderne IDEs |
| **Speichernutzung** | JVM-Overhead bedeutet höheren Basisspeicher | JVM-Flags optimieren; Verwenden Sie native GraalVM-Images für kleine Bereitstellungen |
| **Startzeit** | Das Aufwärmen der JVM kann bei kurzlebigen Prozessen langsam sein | GraalVM natives Image, oder verwenden Sie C/Go für CLI-Tools |
| **Überprüfte Ausnahmen** | Erzwingt die Behandlung von Ausnahmen, die möglicherweise nicht behebbar sind | Verwenden Sie ungeprüfte Ausnahmen oder das `Optional`-Muster |
| **Keine Werttypen** | Alles ist ein Objekt (bis zum Valhalla-Projekt) | Verwenden Sie auf Primitive spezialisierte Sammlungen (Eclipse Collections, Trove) |
---

## Syntax-Grundlagen
### Grundstruktur
Java ist klassenbasiert – alles lebt innerhalb einer Klasse. Der Dateiname muss mit dem Namen der öffentlichen Klasse übereinstimmen.
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

### Objektorientierte Programmierung
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

### Datensätze (Java 16+) – Prägnante Datenklassen
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

### Sammlungen und Streams
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

### Ausnahmebehandlung
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

## Erweiterte Syntax und Muster
### Generika
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

### Versiegelte Klassen und Mustervergleich (Java 17+)
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

### Anmerkungen
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

### Funktionale Schnittstellen und Lambdas
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

## Parallelität und Parallelität
### Virtuelle Threads (Java 21+)
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

### Traditionelles Threading und Synchronisierung
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

## Projektkonfiguration und Build-System
### Projektstruktur (Maven)
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

### CI/CD-Pipeline
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

## Testen
### JUnit 5 mit Mockito
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

## Interoperabilität
### JNI (Java Native Interface)
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

### Fremdfunktions- und Speicher-API (Java 22+)
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

## Designmuster
### Builder-Muster
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

### Beobachtermuster
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

## Leistung und Optimierung
### Profilierungstools
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### Optimierungstechniken
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

## Bereitstellung
### Docker-Datei
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

## Das Ökosystem
### Build-Tools
| Werkzeug | Zweck | Notizen |
|------|---------|-------|
| **Maven** | Build-Automatisierung + Abhängigkeitsmanagement | XML-basiert (`pom.xml`); Industriestandard für Unternehmen |
| **Gradle** | Build-Automatisierung + Abhängigkeitsmanagement | Groovy/Kotlin DSL; schneller für große Projekte; Wird von Android | verwendet
### Frameworks
| Rahmen | Domäne | Beschreibung |
|-----------|--------|-------------|
| **Frühlingsstiefel** | Web / Unternehmen | Das dominierende Java-Framework – REST-APIs, Microservices, Sicherheit, Datenzugriff |
| **Jakarta EE** | Unternehmen | Nachfolger von Java EE; standardisierte Unternehmens-APIs |
| **Winterschlaf** | ORM | Objektrelationale Zuordnung; die Standard-JPA-Implementierung |
| **Mikronaut / Quarkus** | Cloud-nativ | Schneller Start, wenig Speicher – konzipiert für Serverless und Container |
### Testen
| Werkzeug | Zweck |
|------|---------|
| **JUnit 5** | Unit-Test-Framework |
| **Mockito** | Spott-Framework |
| **AssertJ** | Fließende Aussagen |
| **Testcontainer** | Integrationstests mit echten Datenbanken in Docker |
---

## Das JVM-Ökosystem
| JVM-Sprache | Beziehung zu Java |
|-------------|-------|
| **Kotlin** | Moderne Alternative zu Java; Googles bevorzugte Android-Sprache; 100 % Java-kompatibel |
| **Scala** | Funktioneller + OOP-Hybrid; treibt Apache Spark an |
| **Clojure** | Lisp-Dialekt auf der JVM; funktionale Programmierung |
| **Groovy** | Dynamisches Scripting für die JVM; wird in Gradle-Build-Dateien verwendet |
Alle diese können Java-Bibliotheken verwenden, und Java kann deren Bibliotheken verwenden. Die JVM ist die Plattform, nicht nur Java.
---

## Java-Versionen
| Version | Jahr | Hauptmerkmale |
|---------|------|-------------|
| Java 8 | 2014 | **LTS** – Lambdas, Stream-API, optional, Standardmethoden. Immer noch weit verbreitet. |
| Java 11 | 2018 | **LTS** – HTTP-Client-API,`var`für lokale Variablen, Single-File-Source-Launcher |
| Java 17 | 2021 | **LTS** – Versiegelte Klassen, Mustervergleich für`instanceof`, Datensätze, Textblöcke |
| Java 21 | 2023 | **LTS** – **Virtuelle Threads** (Project Loom), Mustervergleich für`switch`, Muster aufzeichnen |
| Java 25 | 2025 | **LTS** – String-Vorlagen, weiterer Mustervergleich, Fremdfunktions-API |
**LTS**-Versionen (Long-Term Support) erhalten über viele Jahre Updates. Verwenden Sie für die Produktion Java 21 oder höher.
---

## Wann man Java verwendet
| Szenario | Warum Java | Bessere Alternative |
|----------|---------|-----|
| Enterprise-Backends | Riesiges Ökosystem, Spring Boot, im großen Maßstab bewährt | Kotlin (gleiche JVM, weniger ausführlich) |
| Android-Entwicklung | Etablierte, riesige Codebasis | Kotlin (Googles bevorzugte Wahl) |
| Big Data (Hadoop, Spark, Kafka) | Das Ökosystem basiert auf Java/Scala | Python für die datenwissenschaftliche Seite |
| Finanzsysteme | Leistung + Zuverlässigkeit + ausgereifte Werkzeuge | -- |
| Microservices | Spring Boot + Cloud-native Frameworks | Entscheiden Sie sich für einfachere Dienste |
| Einfache Skripte | Zu viel Zeremonie | Python, Shell |
| CLI-Tools | Langsamer Start | Geh, Rust |
---

## Synthetische Fragen und Antworten
### F1: Was ist der Unterschied zwischen`==`und`.equals()`in Java?
**A:**`==`vergleicht Objektreferenzen (Identität) – es prüft, ob zwei Variablen auf dasselbe Objekt im Speicher verweisen. `.equals()`vergleicht Objektinhalte (Wertegleichheit). Für Grundelemente (`int`, `double`) vergleicht`==`die Werte direkt. Verwenden Sie für Objekte (einschließlich`String`) immer `.equals()`, um Inhalte zu vergleichen. Die einzige Ausnahme ist der Vergleich mit`null`, wo`==`korrekt ist.
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

### F2: Wie funktioniert der JVM-Garbage Collector und welchen sollte ich verwenden?
**A:** Der GC fordert automatisch Speicher von Objekten zurück, die nicht mehr erreichbar sind. Moderne JVMs (21+) bieten mehrere Kollektoren: G1 (Standard, ausgeglichen), ZGC (extrem niedrige Pausenzeiten, <1 ms) und Shenandoah (geringe Pause, OpenJDK). Für die meisten Anwendungen ist die Standardeinstellung G1 ausreichend. Für latenzempfindliche Dienste verwenden Sie ZGC (`-XX:+UseZGC`). Für eine durchsatzorientierte Stapelverarbeitung verwenden Sie Parallel GC (`-XX:+UseParallelGC`).
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### F3: Wann sollte ich`Stream API`im Vergleich zu herkömmlichen Schleifen verwenden?
**A:** Verwenden Sie Streams, wenn der Vorgang eine klare Pipeline ist (Filtern, Zuordnen, Reduzieren) – sie drücken die Absicht besser aus und lassen sich leicht mit`.parallelStream()`parallelisieren. Verwenden Sie herkömmliche Schleifen für einfache Iterationen, wenn Sie den externen Status ändern müssen, wenn die Leistung kritisch ist (Streams haben Overhead) oder wenn die Logik einen komplexen Kontrollfluss beinhaltet (Unterbrechung, Fortsetzung, mehrere Rückgaben). Vermeiden Sie Streams für einfache `for-each`-Vorgänge.
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

### F4: Was sind Datensätze, versiegelte Klassen und Mustervergleich in modernem Java?
**A:** Datensätze (Java 16) sind unveränderliche Datenträger – sie generieren automatisch Konstruktoren, Getter, `equals`,`hashCode`und `toString`. Versiegelte Klassen (Java 17) schränken ein, welche Klassen sie erweitern können – nützlich für die Modellierung endlicher Typhierarchien. Mit dem Mustervergleich (Java 21) können `switch`-Ausdrücke Typen, Datensätze und Werte zerstören und so ausführliche `instanceof`-Ketten ersetzen.
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

### F5: Wie gehe ich richtig mit aktivierten und nicht aktivierten Ausnahmen um?
**A:** Überprüfte Ausnahmen (`IOException`, Ungeprüfte Ausnahmen (`RuntimeException`-Unterklassen wie `NullPointerException`, `IllegalArgumentException`) stellen Programmierfehler dar. Best Practice: Verwenden Sie geprüfte Ausnahmen sparsam (sie erzeugen Kopplung), bevorzugen Sie`Optional`für erwartetes Fehlen und wickeln Sie geprüfte Ausnahmen in ungeprüfte Ausnahmen ein, wenn Sie API-Grenzen überschreiten.
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

## Problemlösung in der Gedankenkette
### Problem 1: Erstellen Sie eine Thread-sichere Producer-Consumer-Pipeline
**Problemstellung:** Entwerfen Sie eine Producer-Consumer-Pipeline in Java, in der mehrere Producer Arbeitselemente generieren, mehrere Consumer sie gleichzeitig verarbeiten und das System ein ordnungsgemäßes Herunterfahren mit Entleeren der verbleibenden Elemente unterstützt.
**Schritt 1 – Das Problem verstehen:**
Wir benötigen: (1) eine begrenzte Warteschlange zum Puffern von Arbeitselementen zwischen Produzenten und Konsumenten, (2) mehrere Produzenten-Threads, die Elemente hinzufügen, (3) mehrere Konsumenten-Threads, die Elemente verarbeiten, (4) einen Mechanismus, der das Herunterfahren signalisiert und verbleibende Elemente entleert. Javas`BlockingQueue`wurde speziell dafür entwickelt.
**Schritt 2 – Identifizieren Sie den Ansatz:**
– Verwenden Sie`ArrayBlockingQueue`(begrenzt), um unbegrenztes Speicherwachstum zu verhindern.
- Verwenden Sie ein Giftpillenmuster zur Abschaltsignalisierung.
– Verwenden Sie`ExecutorService`für die Thread-Pool-Verwaltung.
- Verwenden Sie `CountDownLatch`, um zu warten, bis alle Verbraucher den Entleervorgang abgeschlossen haben.
**Schritt 3 – Implementieren Sie die Lösung:**
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

**Schritt 4 – Überprüfen und Optimieren:**
– Begrenzte Warteschlange verhindert OOM:`ArrayBlockingQueue(1000)`begrenzt den Speicher.
- Giftpillenmuster: Jeder Konsument steigt sauber aus, nachdem er seine Pille erhalten hat.
–`poll(1, SECONDS)`mit Timeout verhindert, dass Verbraucher dauerhaft blockieren, wenn Produzenten langsam sind.
- Produktion: Verwenden Sie`LinkedBlockingQueue`für unbegrenzte oder`Disruptor`(LMAX) für Pipelines mit extrem niedriger Latenz.
### Problem 2: Implementieren Sie einen benutzerdefinierten annotationsbasierten Validator
**Problemstellung:** Erstellen Sie ein Validierungsframework mit benutzerdefinierten Anmerkungen. Benutzer kommentieren Felder mit `@NotNull`, `@Min(0)`, `@Max(100)`,`@Size(min=1, max=50)`und rufen`Validator.validate(obj)`auf, um eine Liste der Verstöße zu erhalten.
**Schritt 1 – Das Problem verstehen:**
Wir benötigen: (1) benutzerdefinierte Annotationen mit Parametern, (2) einen reflexionsbasierten Validator, der Anmerkungen zur Laufzeit liest, (3) ein Ergebnisobjekt, das alle Validierungsfehler enthält. Dies demonstriert die Annotationsverarbeitungs- und Reflektionsfähigkeiten von Java.
**Schritt 2 – Identifizieren Sie den Ansatz:**
- Definieren Sie Anmerkungen mit`@Retention(RUNTIME)`und `@Target(FIELD)`.
- Verwenden Sie `Class.getDeclaredFields()`, um Felder zu iterieren.
- Verwenden Sie `Field.getAnnotation()`, um Anmerkungswerte zu lesen.
- Vergleichen Sie Feldwerte mit Anmerkungsbeschränkungen.
- Sammeln Sie Verstöße in einer Liste.
**Schritt 3 – Implementieren Sie die Lösung:**
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

**Schritt 4 – Überprüfen und Optimieren:**
– Reflexionsaufwand: für die Validierung akzeptabel (einmal pro Anfrage aufgerufen). Für Hot Paths können Sie Feldsuchen zwischenspeichern oder die Annotationsverarbeitung zur Kompilierungszeit verwenden (wie Hibernate Validator).
- Erweiterbarkeit: Fügen Sie neue Anmerkungen hinzu, indem Sie die Anmerkung + einen Handlerblock in`validate()`erstellen.
- Produktion: Verwenden Sie`jakarta.validation`(Bean Validation 3.0) – es erledigt all dies und noch mehr, mit Verarbeitung zur Kompilierungszeit über Annotationsprozessoren.
### Problem 3: Erstellen Sie einen ratenbegrenzten HTTP-Client mit Wiederholung
**Problemstellung:** Erstellen Sie einen HTTP-Client-Wrapper, der fehlgeschlagene Anforderungen automatisch mit exponentiellem Backoff wiederholt, Ratenbeschränkungen respektiert und Circuit Breaking unterstützt (kein Aufruf eines ausgefallenen Dienstes mehr).
**Schritt 1 – Das Problem verstehen:**
Wir benötigen: (1) Wiederholungslogik mit exponentiellem Backoff und Jitter, (2) Ratenbegrenzung, um eine Überlastung des Zieldienstes zu vermeiden, (3) Schutzschaltermuster – nach N aufeinanderfolgenden Fehlern den Aufruf des Dienstes für eine Abklingzeit unterbrechen. Dies sind drei zusammensetzbare Anliegen.
**Schritt 2 – Identifizieren Sie den Ansatz:**
- Verwenden Sie`java.net.http.HttpClient`(Java 11+) als Basis-Client.
– Implementieren Sie einen Wiederholungsversuch als Wrapper mit`Thread.sleep`für den Backoff.
- Verwenden Sie`Semaphore`zur Ratenbegrenzung (oder`java.time`für den Token-Bucket).
- Leistungsschalter als Zustandsmaschine implementieren: CLOSED → OFFEN → HALF_OPEN.
**Schritt 3 – Implementieren Sie die Lösung:**
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

**Schritt 4 – Überprüfen und Optimieren:**
- Exponentielles Backoff mit Jitter verhindert donnernde Herden (alle Wiederholungsversuche treffen gleichzeitig).
- Leistungsschalter: Nach`failureThreshold`aufeinanderfolgenden Ausfällen öffnet sich der Stromkreis für`cooldownMs`– es werden keine Anforderungen gesendet, um den ausgefallenen Dienst zu schützen.
- Ratenbegrenzer:`Semaphore`mit periodischer Nachfüllung begrenzt den Durchsatz.
- Produktion: Verwenden Sie`resilience4j`– es bietet alle drei Muster (Wiederholung, Ratenbegrenzer, Leistungsschalter) mit geeigneten Implementierungen, Metriken und Spring Boot-Integration.
---

## Zusammenfassung
Java ist eine der wichtigsten Programmiersprachen, die jemals geschaffen wurden. Es betreibt die weltweiten Bankensysteme, Android-Telefone, Big-Data-Pipelines und Unternehmens-Backends. Modernes Java (21+) ist eine ganz andere Sprache als Java 8 – es ist prägnanter, ausdrucksvoller und zunehmend konkurrenzfähiger zu neueren Sprachen. Das JVM-Ökosystem (Kotlin, Scala, Clojure) erweitert seine Reichweite weiter. Für die Unternehmensentwicklung bleibt Java eine sichere und leistungsstarke Wahl.