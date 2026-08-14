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
# Jawa
Java to zorientowany obiektowo język programowania stworzony przez Jamesa Goslinga w Sun Microsystems i wydany w 1995 roku. Filozofia jego projektowania — „pisz raz, uruchamiaj gdziekolwiek” (WORA) — jest realizowana poprzez wirtualną maszynę Java (JVM), która umożliwia uruchamianie skompilowanego kodu Java na dowolnej platformie z implementacją JVM. Java to jeden z najpowszechniej używanych języków programowania w historii, obsługujący backendy korporacyjne, aplikacje na Androida, systemy Big Data i usługi finansowe.
Mimo że Java ma prawie 30 lat, wciąż się rozwija. Nowoczesna Java (wersje 17 i nowsze) obejmuje rekordy, zapieczętowane klasy, dopasowywanie wzorców, wirtualne wątki i rozwijający się ekosystem, który konkuruje z nowszymi językami.
---

## Dlaczego Java ma znaczenie
- **Standard korporacyjny**: Podstawa backendów z listy Fortune 500 — bankowość, ubezpieczenia, handel elektroniczny i opieka zdrowotna.
- **Rozwój Androida**: Podstawowy język Androida (obok Kotlina).
- **Ekosystem Big Data**: Apache Hadoop, Spark, Kafka, Elasticsearch — wszystko napisane w Javie lub Scali (działającej na JVM).
- **Ogromny ekosystem**: Ponad 500 000 bibliotek w Maven Central; dojrzałe narzędzia na każdą potrzebę.
- **Wydajność**: Kompilator JIT firmy JVM tworzy wysoce zoptymalizowany kod maszynowy w czasie wykonywania, często dopasowując C++ do długotrwałych aplikacji.
- **Kompatybilność wsteczna**: Kod napisany dla Java 1.0 (1996) nadal działa na nowoczesnych maszynach JVM.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Opowiadanie** | Wymaga więcej szablonów niż Python, Kotlin lub Go | Użyj Lomboka, rekordów (Java 16+) i nowoczesnych IDE |
| **Wykorzystanie pamięci** | Narzut JVM oznacza większą pamięć bazową | Dostrój flagi JVM; użyj natywnych obrazów GraalVM dla małych wdrożeń |
| **Czas uruchomienia** | Rozgrzewanie JVM może być powolne w przypadku procesów krótkotrwałych | Obraz natywny GraalVM lub użyj C/Go dla narzędzi CLI |
| **Sprawdzone wyjątki** | Wymusza obsługę wyjątków, których odzyskanie może być niemożliwe | Użyj niesprawdzonych wyjątków lub wzorca`Optional`|
| **Brak typów wartości** | Wszystko jest przedmiotem (aż do projektu Valhalla) | Użyj prymitywnych, wyspecjalizowanych kolekcji (Eclipse Collections, Trove) |
---

## Podstawy składni
### Podstawowa struktura
Java jest oparta na klasach — wszystko żyje wewnątrz klasy. Nazwa pliku musi być zgodna z nazwą klasy publicznej.
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

### Programowanie obiektowe
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

### Rekordy (Java 16+) — zwięzłe klasy danych
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

### Kolekcje i strumienie
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

### Obsługa wyjątków
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

## Zaawansowana składnia i wzorce
### Ogólne
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

### Zapieczętowane klasy i dopasowywanie wzorców (Java 17+)
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

### Adnotacje
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

### Interfejsy funkcjonalne i lambdy
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

## Współbieżność i równoległość
### Wątki wirtualne (Java 21+)
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

### Tradycyjne wątkowanie i synchronizacja
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

## Konfiguracja projektu i budowanie systemu
### Struktura projektu (Maven)
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

### Rurociąg CI/CD
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

## Testowanie
### JUnit 5 z Mockito
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

## Interoperacyjność
### JNI (natywny interfejs Java)
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

### API funkcji obcych i pamięci (Java 22+)
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

## Wzorce projektowe
### Wzór konstruktora
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

### Wzór obserwatora
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

## Wydajność i optymalizacja
### Narzędzia do profilowania
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### Techniki optymalizacji
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

## Zastosowanie
### Plik Dockera
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

## Ekosystem
### Narzędzia do tworzenia
| Narzędzie | Cel | Notatki |
|------|---------|-------|
| **Maven** | Automatyzacja budowania + zarządzanie zależnościami | Oparty na XML (`pom.xml`); standard branżowy dla przedsiębiorstw |
| **Stopnie** | Automatyzacja budowania + zarządzanie zależnościami | Groovy/Kotlin DSL; szybciej w przypadku dużych projektów; używany przez Androida |
### Ramy
| Ramy | Domena | Opis |
|---------------|--------|------------|
| **Wiosenny but** | Sieć / przedsiębiorstwo | Dominujący framework Java — API REST, mikroserwisy, bezpieczeństwo, dostęp do danych |
| **Dżakarta,EE** | Przedsiębiorstwo | Następca Java EE; standaryzowane interfejsy API dla przedsiębiorstw |
| **Hibernacja** | ORMO | Mapowanie obiektowo-relacyjne; standardowa implementacja WZP |
| **Mikronauta / Kwarc** | Natywny w chmurze | Szybkie uruchamianie, mało pamięci — przeznaczone do zastosowań bezserwerowych i kontenerów |
### Testowanie
| Narzędzie | Cel |
|------|-------------|
| **Jednostka 5** | Struktura testów jednostkowych |
| **Mockito** | Szyderczy framework |
| **TwierdźJ** | Płynne twierdzenia |
| **Kontenery testowe** | Testy integracyjne z rzeczywistymi bazami danych w Dockerze |
---

## Ekosystem JVM
| Język JVM | Związek z Javą |
|------------|--------------------------------------|
| **Kotlin** | Nowoczesna alternatywa dla Javy; preferowany język Androida przez Google; W 100% kompatybilny z Javą |
| **Scala** | Funkcjonalna + hybryda OOP; obsługuje Apache Spark |
| **Zamknięcie** | Dialekt Lisp na JVM; programowanie funkcjonalne |
| **Świetne** | Dynamiczne skrypty dla JVM; używane w plikach kompilacji Gradle |
Wszystkie one mogą korzystać z bibliotek Java, a Java może korzystać z ich bibliotek. JVM to platforma, a nie tylko Java.
---

## Wersje Java
| Wersja | Rok | Kluczowe funkcje |
|--------|------|------------|
| Java 8 | 2014 | **LTS** — Lambdas, Stream API, opcjonalne, metody domyślne. Nadal szeroko stosowany. |
| Java 11 | 2018 | **LTS** — API klienta HTTP,`var`dla zmiennych lokalnych, jednoplikowy program uruchamiający źródła |
| Java 17 | 2021 | **LTS** — Klasy zapieczętowane, dopasowywanie wzorców dla `instanceof`, rekordy, bloki tekstu |
| Java 21 | 2023 | **LTS** — **Wątki wirtualne** (Project Loom), dopasowywanie wzorców dla `switch`, wzorce rekordów |
| Java 25 | 2025 | **LTS** — szablony ciągów, dalsze dopasowywanie wzorców, API funkcji obcych |
Wersje **LTS** (Long-Term Support) otrzymują aktualizacje przez wiele lat. Do celów produkcyjnych użyj Java 21 lub nowszej wersji.
---

## Kiedy używać Java
| Scenariusz | Dlaczego Java | Lepsza alternatywa |
|---------|---------|--------------------------------|
| Backendy dla przedsiębiorstw | Ogromny ekosystem, Spring Boot, sprawdzony na dużą skalę | Kotlin (ta sama maszyna JVM, mniej gadatliwa) |
| Rozwój Androida | Ugruntowana, ogromna baza kodu | Kotlin (preferowany wybór Google) |
| Big data (Hadoop, Spark, Kafka) | Ekosystem jest zbudowany na Javie/Scala | Python dla analityki danych |
| Systemy finansowe | Wydajność + niezawodność + dojrzałe oprzyrządowanie | -- |
| Mikrousługi | Spring Boot + frameworki natywne dla chmury | Wybierz prostsze usługi |
| Proste skrypty | Za dużo ceremonii | Python, Shell |
| Narzędzia CLI | Powolne uruchamianie | Idź, Rust |
---

## Syntetyczne pytania i odpowiedzi
### P1: Jaka jest różnica między`==`i`.equals()`w Javie?
**A:**`==`porównuje odniesienia do obiektów (tożsamość) — sprawdza, czy dwie zmienne wskazują na ten sam obiekt w pamięci. `.equals()`porównuje zawartość obiektu (równość wartości). W przypadku prymitywów (`int`,`double`),`==`bezpośrednio porównuje wartości. W przypadku obiektów (w tym`String`) zawsze używaj`.equals()`do porównywania treści. Jedynym wyjątkiem jest porównanie z`null`, gdzie`==`jest poprawne.
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

### P2: Jak działa moduł zbierający elementy bezużyteczne JVM i którego powinienem użyć?
**A:** GC automatycznie odzyskuje pamięć z obiektów, które nie są już dostępne. Nowoczesne maszyny JVM (21+) oferują kilka kolektorów: G1 (domyślny, zrównoważony), ZGC (bardzo krótkie czasy pauzy, <1 ms) i Shenandoah (niska pauza, OpenJDK). W przypadku większości zastosowań domyślne G1 jest w porządku. W przypadku usług wrażliwych na opóźnienia użyj ZGC (`-XX:+UseZGC`). W przypadku przetwarzania wsadowego zorientowanego na przepustowość użyj Parallel GC (`-XX:+UseParallelGC`).
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### P3: Kiedy powinienem używać`Stream API`w porównaniu z tradycyjnymi pętlami?
**A:** Używaj strumieni, gdy operacja jest przejrzystym potokiem (filtrowanie, mapowanie, redukcja) — lepiej wyrażają intencje i łatwo łączą się równolegle z`.parallelStream()`. Używaj tradycyjnych pętli do prostych iteracji, gdy musisz zmodyfikować stan zewnętrzny, gdy wydajność jest krytyczna (strumienie mają narzut) lub gdy logika obejmuje złożony przepływ sterowania (przerwanie, kontynuacja, wielokrotne powroty). Unikaj strumieni w przypadku prostych operacji `for-each`.
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

### P4: Czym są rekordy, zapieczętowane klasy i dopasowywanie wzorców we współczesnej Javie?
**A:** Rekordy (Java 16) są niezmiennymi nośnikami danych — automatycznie generują konstruktory, moduły pobierające, `equals`,`hashCode`i `toString`. Klasy zapieczętowane (Java 17) ograniczają, które klasy mogą je rozszerzać — przydatne do modelowania hierarchii typów skończonych. Dopasowywanie wzorców (Java 21) umożliwia wyrażeniom`switch`niszczenie typów, rekordów i wartości — zastępując szczegółowe łańcuchy `instanceof`.
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

### P5: Jak prawidłowo obsługiwać wyjątki zaznaczone i niesprawdzone?
**A:** Sprawdzone wyjątki (`IOException`,`SQLException`) muszą zostać zadeklarowane w`throws`lub przechwycone — reprezentują możliwe do odzyskania warunki, o których osoba wywołująca powinna wiedzieć. Niesprawdzone wyjątki (podklasy `RuntimeException`, takie jak `NullPointerException`, `IllegalArgumentException`) reprezentują błędy programistyczne. Najlepsza praktyka: oszczędnie używaj sprawdzonych wyjątków (tworzą sprzężenie), preferuj`Optional`w przypadku oczekiwanej nieobecności i zawijaj zaznaczone wyjątki w niesprawdzone podczas przekraczania granic API.
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

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Zbuduj bezpieczny dla wątków rurociąg producent-konsument
**Opis problemu:** Zaprojektuj potok producent-konsument w Javie, w którym wielu producentów generuje elementy pracy, wielu konsumentów przetwarza je jednocześnie, a system obsługuje płynne zamykanie z opróżnianiem pozostałych elementów.
**Krok 1 — Zrozum problem:**
Potrzebujemy: (1) ograniczonej kolejki do buforowania elementów pracy między producentami i konsumentami, (2) wielu wątków producenta dodających elementy, (3) wielu wątków konsumenckich przetwarzających elementy, (4) mechanizmu sygnalizującego zamknięcie i opróżnienie pozostałych elementów. Java`BlockingQueue`jest specjalnie do tego stworzona.
**Krok 2 — Zidentyfikuj podejście:**
- Użyj`ArrayBlockingQueue`(ograniczony), aby zapobiec nieograniczonemu wzrostowi pamięci.
- Użyj wzoru trującej pigułki do sygnalizacji wyłączenia.
- Użyj`ExecutorService`do zarządzania pulą wątków.
- Użyj `CountDownLatch`, aby poczekać, aż wszyscy odbiorcy zakończą opróżnianie.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
- Ograniczona kolejka zapobiega OOM:`ArrayBlockingQueue(1000)`ogranicza pamięć.
- Wzór trującej pigułki: każdy konsument wychodzi czysty po otrzymaniu pigułki.
-`poll(1, SECONDS)`z limitem czasu zapobiega blokowaniu konsumentów na zawsze, jeśli producenci są powolni.
- Produkcja: użyj`LinkedBlockingQueue`dla nieograniczonych lub`Disruptor`(LMAX) dla potoków o bardzo małych opóźnieniach.
### Problem 2: Zaimplementuj niestandardowy moduł sprawdzania poprawności oparty na adnotacjach
**Opis problemu:** Utwórz strukturę walidacji przy użyciu niestandardowych adnotacji. Użytkownicy dodają do pól adnotacje`@NotNull`,`@Min(0)`,`@Max(100)`,`@Size(min=1, max=50)`i wywołują `Validator.validate(obj)`, aby uzyskać listę naruszeń.
**Krok 1 — Zrozum problem:**
Potrzebujemy: (1) niestandardowych adnotacji z parametrami, (2) walidatora opartego na refleksjach, który odczytuje adnotacje w czasie wykonywania, (3) obiektu wynikowego zawierającego wszystkie błędy walidacji. To demonstruje możliwości przetwarzania i odzwierciedlania adnotacji w języku Java.
**Krok 2 — Zidentyfikuj podejście:**
- Zdefiniuj adnotacje za pomocą`@Retention(RUNTIME)`i`@Target(FIELD)`.
- Użyj`Class.getDeclaredFields()`do iteracji pól.
- Użyj `Field.getAnnotation()`, aby odczytać wartości adnotacji.
- Porównaj wartości pól z ograniczeniami adnotacji.
- Zbieraj naruszenia na liście.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
- Narzut odbicia: akceptowalny do walidacji (wywoływany raz na żądanie). W przypadku gorących ścieżek przeszukuj pola w pamięci podręcznej lub korzystaj z przetwarzania adnotacji w czasie kompilacji (np. Hibernate Validator).
- Rozszerzalność: dodaj nowe adnotacje, tworząc adnotację + blok obsługi w `validate()`.
- Produkcja: użyj`jakarta.validation`(Bean Validation 3.0) — robi to wszystko i więcej, z przetwarzaniem w czasie kompilacji za pośrednictwem procesorów adnotacji.
### Problem 3: Utwórz klienta HTTP z ograniczoną szybkością i ponów próbę
**Opis problemu:** Utwórz opakowanie klienta HTTP, które automatycznie ponawia nieudane żądania z wykładniczym wycofywaniem, przestrzega limitów szybkości i obsługuje przerywanie obwodów (przestaje wywoływać nieudaną usługę).
**Krok 1 — Zrozum problem:**
Potrzebujemy: (1) logiki ponawiania z wykładniczym wycofywaniem i jitterem, (2) ograniczania szybkości, aby uniknąć przytłoczenia usługi docelowej, (3) wzorca wyłącznika — po N kolejnych awariach przestań wywoływać usługę na okres odnowienia. Są to trzy problemy, które można skomponować.
**Krok 2 — Zidentyfikuj podejście:**
- Użyj`java.net.http.HttpClient`(Java 11+) jako klienta podstawowego.
- Zaimplementuj ponowną próbę jako opakowanie z`Thread.sleep`dla wycofania.
- Użyj`Semaphore`do ograniczenia szybkości (lub`java.time`do zbioru tokenów).
- Zaimplementuj wyłącznik jako maszynę stanów: ZAMKNIĘTY → OTWARTY → HALF_OPEN.
**Krok 3 — Wdróż rozwiązanie:**
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

**Krok 4 — Weryfikacja i optymalizacja:**
- Wykładnicze cofanie się z jitterem zapobiega grzmieniu stada (wszystkie próby uderzenia w tym samym czasie).
- Wyłącznik automatyczny: po kolejnych awariach`failureThreshold`obwód otwiera się dla`cooldownMs`— nie są wysyłane żadne żądania, co chroni uszkodzoną usługę.
- Ogranicznik szybkości:`Semaphore`z okresowym uzupełnianiem przepustowości.
- Produkcja: użyj`resilience4j`— zapewnia wszystkie trzy wzorce (ponowna próba, ogranicznik szybkości, wyłącznik automatyczny) z odpowiednimi implementacjami, metrykami i integracją Spring Boot.
---

## Streszczenie
Java jest jednym z najważniejszych języków programowania, jakie kiedykolwiek stworzono. Obsługuje światowe systemy bankowe, telefony z Androidem, potoki dużych zbiorów danych i zaplecze korporacyjne. Współczesna Java (21+) to zupełnie inny język niż Java 8 — jest bardziej zwięzły, bardziej wyrazisty i coraz bardziej konkurencyjny w stosunku do nowszych języków. Ekosystem JVM (Kotlin, Scala, Clojure) rozszerza swój zasięg jeszcze bardziej. Jeśli chodzi o rozwój przedsiębiorstw, Java pozostaje bezpiecznym i wydajnym wyborem.