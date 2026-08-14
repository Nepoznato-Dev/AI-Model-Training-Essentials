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
Ang Java ay isang statically typed, object-oriented programming language na nilikha ni James Gosling sa Sun Microsystems at inilabas noong 1995. Ang pilosopiya ng disenyo nito — "write once, run anywhere" (WORA) — ay nakakamit sa pamamagitan ng Java Virtual Machine (JVM), na nagbibigay-daan sa pinagsama-samang Java code na tumakbo sa anumang platform na may pagpapatupad ng JVM. Ang Java ay isa sa pinakamalawak na ginagamit na mga programming language sa kasaysayan, pinapagana ang mga backend ng enterprise, Android app, malaking data system, at mga serbisyong pinansyal.
Sa kabila ng halos 30 taong gulang, ang Java ay patuloy na nagbabago. Kasama sa modernong Java (mga bersyon 17+) ang mga talaan, mga selyadong klase, pagtutugma ng pattern, mga virtual na thread, at isang lumalagong ecosystem na nakikipagkumpitensya sa mga mas bagong wika.
---

## Bakit Mahalaga ang Java
- **Enterprise standard**: Ang backbone ng Fortune 500 backends — banking, insurance, e-commerce, healthcare.
- **Android development**: Ang pangunahing wika para sa Android (sa tabi ng Kotlin).
- **Malaking ecosystem ng data**: Apache Hadoop, Spark, Kafka, Elasticsearch — lahat ay nakasulat sa Java o Scala (na tumatakbo sa JVM).
- **Malaking ecosystem**: Higit sa 500,000 library sa Maven Central; mature tooling para sa bawat pangangailangan.
- **Pagganap**: Gumagawa ang JIT compiler ng JVM ng lubos na na-optimize na machine code sa runtime, kadalasang tumutugma sa C++ para sa mga application na matagal nang tumatakbo.
- **Backwards compatibility**: Ang code na isinulat para sa Java 1.0 (1996) ay tumatakbo pa rin sa mga modernong JVM.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Verbosity** | Nangangailangan ng mas maraming boilerplate kaysa sa Python, Kotlin, o Go | Gumamit ng Lombok, mga talaan (Java 16+), at mga modernong IDE |
| **Paggamit ng memory** | Ang ibig sabihin ng JVM overhead ay mas mataas na baseline memory | I-tune ang mga flag ng JVM; gumamit ng mga katutubong larawan ng GraalVM para sa maliliit na deployment |
| **Oras ng pagsisimula** | Maaaring maging mabagal ang pag-init ng JVM para sa mga panandaliang proseso | GraalVM native-image, o gumamit ng C/Go para sa mga CLI tool |
| **Sinuri ang mga exception** | Pinipilit ang paghawak ng mga pagbubukod na maaaring hindi mabawi | Gumamit ng mga walang check na exception o ang`Optional`pattern |
| **Walang mga uri ng halaga** | Ang lahat ay isang bagay (hanggang sa proyekto ng Valhalla) | Gumamit ng mga primitive-specialised na koleksyon (Eclipse Collections, Trove) |
---

## Syntax Fundamentals
### Pangunahing Istruktura
Ang Java ay nakabatay sa klase — lahat ay nabubuhay sa loob ng isang klase. Dapat tumugma ang filename sa pangalan ng pampublikong klase.
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

### Object-Oriented Programming
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

### Records (Java 16+) — Mga Concise Data Classes
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

### Mga Koleksyon at Stream
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

### Exception Handling
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

## Advanced na Syntax at Mga Pattern
### Generics
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

### Mga Selyadong Klase at Pagtutugma ng Pattern (Java 17+)
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

### Mga anotasyon
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

### Mga Functional na Interface at Lambdas
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

## Concurrency at Paralelismo
### Mga Virtual Thread (Java 21+)
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

### Tradisyunal na Threading at Pag-synchronize
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

## Project Configuration at Build System
### Istraktura ng Proyekto (Maven)
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

### CI/CD Pipeline
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

## Pagsubok
### JUnit 5 kasama si Mockito
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

## Interoperability
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

### Foreign Function at Memory API (Java 22+)
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

## Mga Pattern ng Disenyo
### Pattern ng Tagabuo
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

### Pattern ng Tagamasid
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

## Pagganap at Pag-optimize
### Mga Tool sa Pag-profile
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### Mga Teknik sa Pag-optimize
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

## Deployment
### Dockerfile
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

## Ang Ecosystem
### Mga Tool sa Pagbuo
| Tool | Layunin | Mga Tala |
|------|---------|-------|
| **Maven** | Bumuo ng automation + pamamahala ng dependency | Nakabatay sa XML (`pom.xml`); pamantayan ng industriya para sa negosyo |
| **Gradle** | Bumuo ng automation + pamamahala ng dependency | Groovy/Kotlin DSL; mas mabilis para sa malalaking proyekto; ginagamit ng Android |
### Mga Framework
| Balangkas | Domain | Paglalarawan |
|-----------|--------|-------------|
| **Spring Boot** | Web / enterprise | Ang nangingibabaw na balangkas ng Java — REST API, microservice, seguridad, pag-access ng data |
| **Jakarta EE** | Enterprise | Successor sa Java EE; mga standardized na enterprise API |
| **Hibernate** | ORM | Object-relational na pagmamapa; ang karaniwang pagpapatupad ng JPA |
| **Micronaut / Quarkus** | Cloud-native | Mabilis na pagsisimula, mababang memory — idinisenyo para sa walang server at mga container |
### Pagsubok
| Tool | Layunin |
|------|---------|
| **JUnit 5** | Unit testing framework |
| **Mockito** | Mapanuksong framework |
| **AssertJ** | Mga matatas na pahayag |
| **Mga Testcontainer** | Mga pagsubok sa pagsasama sa totoong mga database sa Docker |
---

## Ang JVM Ecosystem
| Wika ng JVM | Relasyon sa Java |
|-------------|---------------------|
| **Kotlin** | Modernong alternatibo sa Java; Ang gustong wika ng Google sa Android; 100% Java-compatible |
| **Scala** | Functional + OOP hybrid; kapangyarihan Apache Spark |
| **Clojure** | Lisp dialect sa JVM; functional programming |
| **Groovy** | Dynamic na scripting para sa JVM; ginagamit sa Gradle build file |
Ang lahat ng ito ay maaaring gumamit ng mga aklatan ng Java, at magagamit ng Java ang kanilang mga aklatan. Ang JVM ay ang platform, hindi lamang Java.
---

## Mga Bersyon ng Java
| Bersyon | Taon | Mga Pangunahing Tampok |
|---------|------|-------------|
| Java 8 | 2014 | **LTS** — Lambdas, Stream API, Opsyonal, mga default na pamamaraan. Malawak pa ring ginagamit. |
| Java 11 | 2018 | **LTS** — HTTP Client API,`var`para sa mga lokal na variable, single-file source launcher |
| Java 17 | 2021 | **LTS** — Mga selyadong klase, pagtutugma ng pattern para sa`instanceof`, mga tala, mga bloke ng teksto |
| Java 21 | 2023 | **LTS** — **Mga virtual na thread** (Project Loom), pagtutugma ng pattern para sa`switch`, mga pattern ng record |
| Java 25 | 2025 | **LTS** — String templates, karagdagang pattern matching, foreign function API |
Ang **LTS** (Long-Term Support) na mga bersyon ay tumatanggap ng mga update sa loob ng maraming taon. Para sa produksyon, gamitin ang Java 21 o mas bago.
---

## Kailan Gamitin ang Java
| Sitwasyon | Bakit Java | Mas mahusay na Alternatibo |
|----------|---------|-------------------|
| Mga backend ng enterprise | Napakalaking ecosystem, Spring Boot, napatunayan sa sukat | Kotlin (parehong JVM, less verbose) |
| Pag-unlad ng Android | Itinatag, malaking codebase | Kotlin (ginustong pagpipilian ng Google) |
| Malaking data (Hadoop, Spark, Kafka) | Ang ecosystem ay binuo sa Java/Scala | Python para sa data science side |
| Mga sistema ng pananalapi | Pagganap + pagiging maaasahan + mature tooling | -- |
| Mga Microservice | Spring Boot + cloud-native frameworks | Pumunta para sa mas simpleng serbisyo |
| Mga simpleng script | Masyadong maraming seremonya | Python, Shell |
| Mga tool sa CLI | Mabagal na pagsisimula | Go, Rust |
---

## Synthetic na Q&A
### Q1: Ano ang pagkakaiba sa pagitan ng`==`at`.equals()`sa Java?
**A:** Inihahambing ng`==`ang mga object reference (identity) — sinusuri nito kung ang dalawang variable ay tumuturo sa parehong bagay sa memorya.  Inihahambing ng`.equals()`ang nilalaman ng bagay (pagkakapantay-pantay ng halaga). Para sa mga primitive (`int`,`double`), direktang inihahambing ng`==`ang mga halaga. Para sa mga bagay (kabilang ang`String`), palaging gamitin ang`.equals()`upang ihambing ang nilalaman. Ang tanging pagbubukod ay ang paghahambing sa`null`, kung saan tama ang `==`.
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

### Q2: Paano gumagana ang JVM garbage collector, at alin ang dapat kong gamitin?
**A:** Awtomatikong kinukuha ng GC ang memorya mula sa mga bagay na hindi na maabot. Ang mga modernong JVM (21+) ay nag-aalok ng ilang collectors: G1 (default, balanse), ZGC (ultra-low pause times, <1ms), at Shenandoah (low pause, OpenJDK). Para sa karamihan ng mga application, ang default na G1 ay maayos. Para sa mga serbisyong sensitibo sa latency, gamitin ang ZGC (`-XX:+UseZGC`). Para sa throughput-oriented na batch processing, gamitin ang Parallel GC (`-XX:+UseParallelGC`).
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### Q3: Kailan ko dapat gamitin ang`Stream API`kumpara sa tradisyonal na mga loop?
**A:** Gumamit ng Mga Stream kapag ang operasyon ay isang malinaw na pipeline (filter, mapa, bawasan) — mas mahusay silang nagpapahayag ng layunin at madaling magkaparehas sa`.parallelStream()`. Gumamit ng mga tradisyunal na loop para sa mga simpleng pag-ulit, kapag kailangan mong baguhin ang panlabas na estado, kapag ang pagganap ay kritikal (ang mga stream ay may overhead), o kapag ang lohika ay nagsasangkot ng kumplikadong daloy ng kontrol (break, continue, multiple returns). Iwasan ang mga stream para sa mga simpleng operasyon ng `for-each`.
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

### Q4: Ano ang mga talaan, mga selyadong klase, at pagtutugma ng pattern sa modernong Java?
**A:** Ang mga tala (Java 16) ay hindi nababagong data carrier — sila ay awtomatikong bumubuo ng mga constructor, getter,`equals`,`hashCode`, at`toString`. Pinaghihigpitan ng mga selyadong klase (Java 17) kung aling mga klase ang makakapagpalawig sa kanila — kapaki-pakinabang para sa pagmomodelo ng mga hierarchy ng may hangganang uri. Ang pagtutugma ng pattern (Java 21) ay nagbibigay-daan sa mga expression ng`switch`na sirain ang mga uri, record, at value — pinapalitan ang mga verbose`instanceof`na chain.
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

### Q5: Paano ko hahawakan nang maayos ang mga checked vs unchecked exception?
**A:** Ang mga may check na exception (`IOException`,`SQLException`) ay dapat ideklara sa`throws`o mahuli — kinakatawan nila ang mga nare-recover na kondisyon na dapat malaman ng tumatawag. Ang mga hindi naka-check na exception (`RuntimeException`subclass tulad ng`NullPointerException`,`IllegalArgumentException`) ay kumakatawan sa mga programming bug. Pinakamahusay na kasanayan: gumamit ng mga naka-check na exception nang matipid (gumawa sila ng coupling), mas gusto ang`Optional`para sa inaasahang pagliban, at ibalot ang mga may check na exception sa mga hindi naka-check kapag tumatawid sa mga hangganan ng API.
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

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Bumuo ng Thread-Safe Producer-Consumer Pipeline
**Pahayag ng Problema:** Magdisenyo ng pipeline ng producer-consumer sa Java kung saan maraming producer ang bumubuo ng mga work item, maraming consumer ang nagpoproseso ng mga ito nang sabay-sabay, at sinusuportahan ng system ang magandang pagsara sa pag-draining ng mga natitirang item.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) isang limitadong pila upang mag-buffer ng mga item sa trabaho sa pagitan ng mga producer at mga consumer, (2) maramihang mga thread ng producer na nagdaragdag ng mga item, (3) maraming mga consumer thread na nagpoproseso ng mga item, (4) isang mekanismo upang magsenyas ng shutdown at maubos ang natitirang mga item. Ang`BlockingQueue`ng Java ay binuo para dito.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gamitin ang`ArrayBlockingQueue`(bounded) upang maiwasan ang walang hangganang paglaki ng memorya.
- Gumamit ng pattern ng poison pill para sa shutdown signaling.
- Gamitin ang`ExecutorService`para sa pamamahala ng thread pool.
- Gamitin ang`CountDownLatch`upang hintayin ang lahat ng mga mamimili na matapos ang draining.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Pinipigilan ng bounded queue ang OOM: Nililimitahan ng`ArrayBlockingQueue(1000)`ang memory.
- Pattern ng lason na tableta: malinis na lumalabas ang bawat mamimili pagkatapos matanggap ang tableta nito.
- Ang`poll(1, SECONDS)`na may timeout ay pumipigil sa mga consumer na humarang nang tuluyan kung mabagal ang mga producer.
- Produksyon: gamitin ang`LinkedBlockingQueue`para sa walang hangganan, o`Disruptor`(LMAX) para sa mga ultra-low-latency na pipeline.
### Problema 2: Magpatupad ng Custom na Annotation-Based Validator
**Problem Statement:** Gumawa ng validation framework gamit ang custom na anotasyon. Ang mga user ay nag-annotate ng mga field na may`@NotNull`,`@Min(0)`,`@Max(100)`,`@Size(min=1, max=50)`, at tumawag sa`Validator.validate(obj)`upang makakuha ng listahan ng mga paglabag.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) mga custom na annotation na may mga parameter, (2) isang reflection-based validator na nagbabasa ng mga anotasyon sa runtime, (3) isang resultang object na naglalaman ng lahat ng validation error. Ipinapakita nito ang pagpoproseso ng anotasyon ng Java at mga kakayahan sa pagmuni-muni.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Tukuyin ang mga anotasyon na may`@Retention(RUNTIME)`at`@Target(FIELD)`.
- Gamitin ang`Class.getDeclaredFields()`upang umulit ang mga field.
- Gamitin ang`Field.getAnnotation()`upang basahin ang mga halaga ng anotasyon.
- Ihambing ang mga halaga ng field laban sa mga hadlang sa anotasyon.
- Kolektahin ang mga paglabag sa isang listahan.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Reflection overhead: katanggap-tanggap para sa pagpapatunay (tinatawag nang isang beses bawat kahilingan). Para sa mga maiinit na landas, paghahanap sa field ng cache o gumamit ng compile-time na pagpoproseso ng anotasyon (tulad ng Hibernate Validator).
- Extensibility: magdagdag ng mga bagong anotasyon sa pamamagitan ng paggawa ng anotasyon + isang handler block sa`validate()`.
- Produksyon: gumamit ng`jakarta.validation`(Bean Validation 3.0) — ginagawa nito ang lahat ng ito at higit pa, na may pagpoproseso ng oras ng pag-compile sa pamamagitan ng mga processor ng anotasyon.
### Problema 3: Bumuo ng HTTP Client na Limitado sa Rate gamit ang Retry
**Problem Statement:** Lumikha ng HTTP client wrapper na awtomatikong muling sumusubok sa mga nabigong kahilingan na may exponential backoff, nirerespeto ang mga limitasyon sa rate, at sumusuporta sa circuit breaking (ihinto ang pagtawag sa isang palpak na serbisyo).
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) subukang muli ang logic na may exponential backoff at jitter, (2) rate limiting para maiwasan ang labis na target na serbisyo, (3) circuit breaker pattern — pagkatapos ng N magkakasunod na pagkabigo, ihinto ang pagtawag sa serbisyo para sa isang cooldown period. Ang mga ito ay tatlong composable alalahanin.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gamitin ang`java.net.http.HttpClient`(Java 11+) bilang batayang kliyente.
- Ipatupad ang muling pagsubok bilang isang wrapper na may`Thread.sleep`para sa backoff.
- Gamitin ang`Semaphore`para sa paglilimita sa rate (o`java.time`para sa token bucket).
- Ipatupad ang circuit breaker bilang state machine: SARADO → OPEN → HALF_OPEN.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Pinipigilan ng exponential backoff na may jitter ang dumadagundong na kawan (lahat ng muling sumusubok na tumama nang sabay-sabay).
- Circuit breaker: pagkatapos ng`failureThreshold`na magkakasunod na pagkabigo, ang circuit ay magbubukas para sa`cooldownMs`— walang mga kahilingan na ipinadala, na nagpoprotekta sa bagsak na serbisyo.
- Rate limiter:`Semaphore`na may periodic replenishment caps throughput.
- Produksyon: gumamit ng`resilience4j`— nagbibigay ito ng lahat ng tatlong pattern (subukang muli, limiter ng rate, circuit breaker) na may wastong mga pagpapatupad, sukatan, at pagsasama ng Spring Boot.
---

## Buod
Ang Java ay isa sa pinakamahalagang programming language na nilikha. Pinapatakbo nito ang mga sistema ng pagbabangko sa mundo, mga Android phone, mga pipeline ng malalaking data, at mga backend ng enterprise. Ang modernong Java (21+) ay isang ibang-iba na wika mula sa Java 8 — ito ay mas maigsi, mas nagpapahayag, at lalong nakikipagkumpitensya sa mga mas bagong wika. Ang JVM ecosystem (Kotlin, Scala, Clojure) ay pinalawak pa ang abot nito. Para sa pagpapaunlad ng negosyo, ang Java ay nananatiling isang ligtas at mahusay na pagpipilian.