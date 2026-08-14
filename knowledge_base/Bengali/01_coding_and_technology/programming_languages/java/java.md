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
# জাভা
জাভা হল একটি স্ট্যাটিকলি টাইপ করা, অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং ভাষা যা জেমস গসলিং দ্বারা সান মাইক্রোসিস্টেমে তৈরি করা হয়েছিল এবং 1995 সালে প্রকাশিত হয়েছিল৷ এর নকশা দর্শন — "একবার লিখুন, কোথাও চালান" (WORA) — জাভা ভার্চুয়াল মেশিন (JVM) এর মাধ্যমে অর্জন করা হয়েছে, যা JVM বাস্তবায়নের যে কোনও প্ল্যাটফর্মে কম্পাইল করা জাভা কোড চালানোর অনুমতি দেয়৷ জাভা ইতিহাসে সর্বাধিক ব্যবহৃত প্রোগ্রামিং ভাষাগুলির মধ্যে একটি, এন্টারপ্রাইজ ব্যাকএন্ড, অ্যান্ড্রয়েড অ্যাপস, বড় ডেটা সিস্টেম এবং আর্থিক পরিষেবাগুলিকে শক্তিশালী করে৷
প্রায় 30 বছর বয়সী হওয়া সত্ত্বেও, জাভা বিকশিত হতে থাকে। আধুনিক জাভা (সংস্করণ 17+) এর মধ্যে রয়েছে রেকর্ড, সিল করা ক্লাস, প্যাটার্ন ম্যাচিং, ভার্চুয়াল থ্রেড এবং একটি ক্রমবর্ধমান ইকোসিস্টেম যা নতুন ভাষার সাথে প্রতিযোগিতা করে।
---

## জাভা কেন গুরুত্বপূর্ণ
- **এন্টারপ্রাইজ স্ট্যান্ডার্ড**: ফরচুন 500 ব্যাকএন্ডের মেরুদণ্ড — ব্যাংকিং, বীমা, ই-কমার্স, স্বাস্থ্যসেবা।
- **অ্যান্ড্রয়েড ডেভেলপমেন্ট**: অ্যান্ড্রয়েডের জন্য প্রাথমিক ভাষা (কোটলিনের পাশাপাশি)।
- **বিগ ডেটা ইকোসিস্টেম**: Apache Hadoop, Spark, Kafka, Elasticsearch — সবই জাভা বা স্কালায় লেখা (যা JVM এ চলে)।
- **ম্যাসিভ ইকোসিস্টেম**: মাভেন সেন্ট্রালে ৫০০,০০০ এর বেশি লাইব্রেরি; প্রতিটি প্রয়োজনের জন্য পরিপক্ক টুলিং।
- **পারফরম্যান্স**: JVM-এর JIT কম্পাইলার রানটাইমে অত্যন্ত অপ্টিমাইজ করা মেশিন কোড তৈরি করে, যা প্রায়ই দীর্ঘ-চলমান অ্যাপ্লিকেশনের জন্য C++ এর সাথে মিলে যায়।
- **পিছন দিকের সামঞ্জস্য**: জাভা 1.0 (1996) এর জন্য লেখা কোড এখনও আধুনিক JVM-এ চলে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **শব্দবোধ** | পাইথন, কোটলিন বা গো | এর চেয়ে বেশি বয়লারপ্লেট প্রয়োজন৷ Lombok, রেকর্ড (Java 16+), এবং আধুনিক IDEs ব্যবহার করুন |
| **মেমরি ব্যবহার** | JVM ওভারহেড মানে উচ্চতর বেসলাইন মেমরি | টিউন JVM পতাকা; ছোট স্থাপনার জন্য GraalVM নেটিভ ইমেজ ব্যবহার করুন |
| **স্টার্টআপ সময়** | JVM ওয়ার্ম-আপ স্বল্পস্থায়ী প্রক্রিয়ার জন্য ধীর হতে পারে | GraalVM নেটিভ-ইমেজ, অথবা CLI টুলের জন্য C/Go ব্যবহার করুন |
| **চেক করা ব্যতিক্রম** | ব্যতিক্রমগুলি পরিচালনা করতে বাধ্য করে যা পুনরুদ্ধারযোগ্য নাও হতে পারে | অচেক করা ব্যতিক্রম বা`Optional`প্যাটার্ন ব্যবহার করুন |
| **কোন মান প্রকার নেই** | সবকিছু একটি বস্তু (ভালহাল্লা প্রকল্প পর্যন্ত) | আদিম-বিশেষ সংগ্রহ ব্যবহার করুন (Eclipse Collections, Trove) |
---

## সিনট্যাক্স মৌলিক
### মৌলিক কাঠামো
জাভা ক্লাস-ভিত্তিক — সবকিছুই ক্লাসের ভিতরে থাকে। ফাইলের নাম অবশ্যই পাবলিক ক্লাস নামের সাথে মিলবে।
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

### অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং
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

### রেকর্ড (জাভা 16+) — সংক্ষিপ্ত ডেটা ক্লাস
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

### সংগ্রহ এবং স্ট্রীম
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

### ব্যতিক্রম হ্যান্ডলিং
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### জেনেরিক
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

### সিল করা ক্লাস এবং প্যাটার্ন ম্যাচিং (জাভা 17+)
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

### টীকা
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

### কার্যকরী ইন্টারফেস এবং ল্যাম্বডাস
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

## সামঞ্জস্য এবং সমান্তরালতা
### ভার্চুয়াল থ্রেড (জাভা 21+)
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

### ঐতিহ্যগত থ্রেডিং এবং সিঙ্ক্রোনাইজেশন
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো (মাভেন)
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

### CI/CD পাইপলাইন
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

## পরীক্ষা
### JUnit 5 মকিটোর সাথে
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

## ইন্টারঅপারেবিলিটি
### JNI (জাভা নেটিভ ইন্টারফেস)
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

### বিদেশী ফাংশন এবং মেমরি API (জাভা 22+)
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

## ডিজাইন প্যাটার্ন
### নির্মাতা প্যাটার্ন
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

### পর্যবেক্ষক প্যাটার্ন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### অপ্টিমাইজেশন কৌশল
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

## স্থাপনা
### ডকারফাইল
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

## ইকোসিস্টেম
### বিল্ড টুলস
| টুল | উদ্দেশ্য | নোট |
|------|---------|-------|
| **মাভেন** | বিল্ড অটোমেশন + নির্ভরতা ব্যবস্থাপনা | XML-ভিত্তিক ( `pom.xml`); এন্টারপ্রাইজের জন্য শিল্প মান |
| **গ্রেডল** | বিল্ড অটোমেশন + নির্ভরতা ব্যবস্থাপনা | গ্রুভি/কোটলিন ডিএসএল; বড় প্রকল্পের জন্য দ্রুত; অ্যান্ড্রয়েড দ্বারা ব্যবহৃত |
### ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | ডোমেন | বর্ণনা |
|------------|---------|---------------|
| **স্প্রিং বুট** | ওয়েব / এন্টারপ্রাইজ | প্রভাবশালী জাভা ফ্রেমওয়ার্ক — REST API, মাইক্রোসার্ভিস, নিরাপত্তা, ডেটা অ্যাক্সেস |
| **জাকার্তা EE** | এন্টারপ্রাইজ | জাভা EE এর উত্তরসূরি; প্রমিত এন্টারপ্রাইজ APIs |
| **হাইবারনেট** | ORM | অবজেক্ট-রিলেশনাল ম্যাপিং; আদর্শ JPA বাস্তবায়ন |
| **মাইক্রোনট / কোয়ার্কাস** | মেঘ-দেশী | দ্রুত স্টার্টআপ, কম মেমরি — সার্ভারহীন এবং কন্টেইনারের জন্য ডিজাইন করা হয়েছে
### পরীক্ষা
| টুল | উদ্দেশ্য |
|------|---------|
| **জুনিট ৫** | ইউনিট টেস্টিং ফ্রেমওয়ার্ক |
| **মকিটো** | উপহাস কাঠামো |
| **AssertJ** | সাবলীল দাবী |
| **পরীক্ষার পাত্র** | ডকারে বাস্তব ডাটাবেসের সাথে ইন্টিগ্রেশন পরীক্ষা |
---

## জেভিএম ইকোসিস্টেম
| JVM ভাষা | জাভার সাথে সম্পর্ক |
|---------------|------------|
| **কোটলিন** | জাভার আধুনিক বিকল্প; গুগলের পছন্দের অ্যান্ড্রয়েড ভাষা; 100% জাভা-সামঞ্জস্যপূর্ণ |
| **স্ক্যালা** | কার্যকরী + OOP হাইব্রিড; ক্ষমতা Apache Spark |
| **বন্ধ** | JVM-তে লিস্প উপভাষা; কার্যকরী প্রোগ্রামিং |
| **গ্রুভি** | JVM-এর জন্য গতিশীল স্ক্রিপ্টিং; Gradle বিল্ড ফাইলে ব্যবহৃত |
এই সমস্ত জাভা লাইব্রেরি ব্যবহার করতে পারে, এবং জাভা তাদের লাইব্রেরি ব্যবহার করতে পারে। JVM হল প্ল্যাটফর্ম, শুধু জাভা নয়।
---

## জাভা সংস্করণ
| সংস্করণ | বছর | মূল বৈশিষ্ট্য |
|---------|------|---------------|
| জাভা 8 | 2014 | **LTS** — Lambdas, স্ট্রিম API, ঐচ্ছিক, ডিফল্ট পদ্ধতি। এখনও ব্যাপকভাবে ব্যবহৃত. |
| জাভা 11 | 2018 | **LTS** — HTTP ক্লায়েন্ট API, স্থানীয় ভেরিয়েবলের জন্য `var`, একক-ফাইল সোর্স লঞ্চার |
| জাভা 17 | 2021 | **LTS** — সিল করা ক্লাস,`instanceof`এর জন্য প্যাটার্ন ম্যাচিং, রেকর্ড, টেক্সট ব্লক |
| জাভা 21 | 2023 | **LTS** — **ভার্চুয়াল থ্রেড** (প্রজেক্ট লুম),`switch`এর জন্য প্যাটার্ন ম্যাচিং, রেকর্ড প্যাটার্ন |
| জাভা 25 | 2025 | **LTS** — স্ট্রিং টেমপ্লেট, আরও প্যাটার্ন ম্যাচিং, বিদেশী ফাংশন API |
**LTS** (দীর্ঘ-মেয়াদী সহায়তা) সংস্করণগুলি অনেক বছর ধরে আপডেট পায়। উৎপাদনের জন্য, Java 21 বা তার পরে ব্যবহার করুন।
---

## কখন জাভা ব্যবহার করবেন
| দৃশ্যকল্প | কেন জাভা | ভাল বিকল্প |
|------------|---------|---------|
| এন্টারপ্রাইজ ব্যাকএন্ড | বিশাল ইকোসিস্টেম, স্প্রিং বুট, স্কেলে প্রমাণিত | কোটলিন (একই JVM, কম ভার্বোস) |
| অ্যান্ড্রয়েড উন্নয়ন | প্রতিষ্ঠিত, বিশাল কোডবেস | কোটলিন (গুগলের পছন্দের পছন্দ) |
| বিগ ডেটা (হাদুপ, স্পার্ক, কাফকা) | ইকোসিস্টেমটি Java/Scala-তে নির্মিত ডাটা সায়েন্স সাইডের জন্য পাইথন |
| আর্থিক ব্যবস্থা | কর্মক্ষমতা + নির্ভরযোগ্যতা + পরিপক্ক টুলিং | -- |
| মাইক্রোসার্ভিস | স্প্রিং বুট + ক্লাউড-নেটিভ ফ্রেমওয়ার্ক | সহজ পরিষেবার জন্য যান |
| সহজ স্ক্রিপ্ট | খুব বেশি অনুষ্ঠান | পাইথন, শেল |
| CLI টুলস | ধীর স্টার্টআপ | যাও, মরিচা |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: জাভাতে`==`এবং`.equals()`এর মধ্যে পার্থক্য কী?
**A:**`==`অবজেক্ট রেফারেন্স (পরিচয়) তুলনা করে — এটি পরীক্ষা করে যে দুটি ভেরিয়েবল মেমরিতে একই বস্তুর দিকে নির্দেশ করে কিনা। `.equals()`বস্তুর বিষয়বস্তুর তুলনা করে (মান সমতা)। আদিম জন্য (`int`,`double`),`==`মানগুলি সরাসরি তুলনা করে। বস্তুর জন্য (`String` সহ), বিষয়বস্তু তুলনা করতে সর্বদা`.equals()`ব্যবহার করুন। একমাত্র ব্যতিক্রম হল`null`এর সাথে তুলনা করা, যেখানে`==`সঠিক।
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

### প্রশ্ন 2: JVM আবর্জনা সংগ্রহকারী কীভাবে কাজ করে এবং আমার কোনটি ব্যবহার করা উচিত?
**A:** GC স্বয়ংক্রিয়ভাবে এমন বস্তু থেকে মেমরি পুনরুদ্ধার করে যা আর পৌঁছানো যায় না। আধুনিক JVMs (21+) বেশ কয়েকটি সংগ্রাহক অফার করে: G1 (ডিফল্ট, সুষম), ZGC (অতি কম বিরতি সময়, <1ms), এবং Shenandoah (লো বিরতি, OpenJDK)। বেশিরভাগ অ্যাপ্লিকেশনের জন্য, ডিফল্ট G1 ঠিক আছে। লেটেন্সি-সংবেদনশীল পরিষেবাগুলির জন্য, ZGC (`-XX:+UseZGC`) ব্যবহার করুন। থ্রুপুট-ভিত্তিক ব্যাচ প্রক্রিয়াকরণের জন্য, সমান্তরাল GC ( `-XX:+UseParallelGC`) ব্যবহার করুন।
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### প্রশ্ন 3: কখন আমার`Stream API`বনাম ঐতিহ্যবাহী লুপ ব্যবহার করা উচিত?
**A:** স্ট্রীম ব্যবহার করুন যখন অপারেশনটি একটি পরিষ্কার পাইপলাইন (ফিল্টার, মানচিত্র, হ্রাস) — তারা অভিপ্রায়কে আরও ভালভাবে প্রকাশ করে এবং`.parallelStream()`এর সাথে সহজেই সমান্তরাল করে। সাধারণ পুনরাবৃত্তির জন্য প্রথাগত লুপগুলি ব্যবহার করুন, যখন আপনাকে বাহ্যিক অবস্থা পরিবর্তন করতে হবে, যখন কর্মক্ষমতা সমালোচনামূলক হয় (স্ট্রিমগুলির ওভারহেড থাকে), অথবা যখন যুক্তিতে জটিল নিয়ন্ত্রণ প্রবাহ জড়িত থাকে (ব্রেক, চালিয়ে যাওয়া, একাধিক রিটার্ন)। সাধারণ`for-each`অপারেশনের জন্য স্ট্রীম এড়িয়ে চলুন।
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

### প্রশ্ন 4: আধুনিক জাভাতে রেকর্ড, সিল করা ক্লাস এবং প্যাটার্ন ম্যাচিং কি কি?
**A:** রেকর্ডগুলি (জাভা 16) অপরিবর্তনীয় ডেটা ক্যারিয়ার — তারা স্বয়ংক্রিয়ভাবে কনস্ট্রাক্টর, গেটার, `equals`,`hashCode`এবং`toString`তৈরি করে। সিল করা ক্লাসগুলি (জাভা 17) সীমাবদ্ধ করে যে কোন ক্লাসগুলি সেগুলিকে প্রসারিত করতে পারে — সসীম ধরণের শ্রেণিবিন্যাসের মডেলিংয়ের জন্য দরকারী৷ প্যাটার্ন ম্যাচিং (জাভা 21)`switch`এক্সপ্রেশনের ধরন, রেকর্ড এবং মান ধ্বংস করতে দেয় — ভার্বোস`instanceof`চেইন প্রতিস্থাপন করে।
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

### প্রশ্ন 5: আমি কীভাবে চেক করা বনাম চেক করা ব্যতিক্রমগুলি সঠিকভাবে পরিচালনা করব?
**A:** চেক করা ব্যতিক্রমগুলি (`IOException`,`SQLException`) অবশ্যই `throws`-এ ঘোষণা করতে হবে বা ধরা পড়তে হবে — এগুলি পুনরুদ্ধারযোগ্য অবস্থার প্রতিনিধিত্ব করে যেগুলি সম্পর্কে কলারের জানা উচিত৷ অচেক করা ব্যতিক্রমগুলি (`RuntimeException`সাবক্লাস যেমন`NullPointerException`,`IllegalArgumentException`) প্রোগ্রামিং বাগগুলি উপস্থাপন করে৷ সর্বোত্তম অনুশীলন: পরীক্ষিত ব্যতিক্রমগুলি অল্প পরিমাণে ব্যবহার করুন (তারা কাপলিং তৈরি করে), প্রত্যাশিত অনুপস্থিতির জন্য`Optional`পছন্দ করুন এবং API সীমানা অতিক্রম করার সময় চেক করা ব্যতিক্রমগুলিকে অচেক করা জায়গায় মোড়ানো করুন।
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

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি থ্রেড-নিরাপদ প্রযোজক-ভোক্তা পাইপলাইন তৈরি করুন
**সমস্যা বিবৃতি:** জাভাতে একটি প্রযোজক-ভোক্তা পাইপলাইন ডিজাইন করুন যেখানে একাধিক প্রযোজক কাজের আইটেম তৈরি করে, একাধিক ভোক্তা সেগুলিকে একযোগে প্রক্রিয়া করে এবং সিস্টেমটি অবশিষ্ট আইটেমগুলি নিষ্কাশনের সাথে সুন্দর শাটডাউন সমর্থন করে।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) প্রযোজক এবং ভোক্তাদের মধ্যে কাজের আইটেমগুলিকে বাফার করার জন্য একটি আবদ্ধ সারি, (2) একাধিক প্রযোজক থ্রেড আইটেম যোগ করে, (3) একাধিক ভোক্তা থ্রেড প্রক্রিয়াকরণ আইটেম, (4) একটি প্রক্রিয়া বন্ধ করার সংকেত দেয় এবং অবশিষ্ট আইটেমগুলি নিষ্কাশন করে৷ জাভা এর`BlockingQueue`এর জন্য উদ্দেশ্য-নির্মিত।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- সীমাহীন মেমরি বৃদ্ধি রোধ করতে`ArrayBlockingQueue`(বাউন্ডেড) ব্যবহার করুন।
- শাটডাউন সিগন্যালিংয়ের জন্য একটি বিষ পিল প্যাটার্ন ব্যবহার করুন।
- থ্রেড পুল ব্যবস্থাপনার জন্য`ExecutorService`ব্যবহার করুন।
- সমস্ত ভোক্তাদের নিষ্কাশন শেষ হওয়ার জন্য অপেক্ষা করতে`CountDownLatch`ব্যবহার করুন৷
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- আবদ্ধ সারি OOM প্রতিরোধ করে:`ArrayBlockingQueue(1000)`মেমরি সীমিত করে।
- বিষ বড়ি প্যাটার্ন: প্রতিটি ভোক্তা তার বড়ি গ্রহণের পর পরিষ্কারভাবে প্রস্থান করে।
- টাইমআউট সহ`poll(1, SECONDS)`প্রযোজকরা ধীর হলে গ্রাহকদের চিরতরে ব্লক করা থেকে বাধা দেয়।
- উত্পাদন: সীমাহীন জন্য `LinkedBlockingQueue`, বা অতি-লো-ল্যাটেন্সি পাইপলাইনের জন্য`Disruptor`(LMAX) ব্যবহার করুন৷
### সমস্যা 2: একটি কাস্টম টীকা-ভিত্তিক যাচাইকারী প্রয়োগ করুন
**সমস্যা বিবৃতি:** কাস্টম টীকা ব্যবহার করে একটি বৈধতা কাঠামো তৈরি করুন। ব্যবহারকারীরা`@NotNull`,`@Min(0)`,`@Max(100)`,`@Size(min=1, max=50)`, এবং লঙ্ঘনের একটি তালিকা পেতে `Validator.validate(obj)`-এর সাথে ক্ষেত্রগুলিকে টীকা করে৷
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) পরামিতি সহ কাস্টম টীকা, (2) একটি প্রতিফলন-ভিত্তিক যাচাইকারী যা রানটাইমে টীকা পড়ে, (3) সমস্ত বৈধতা ত্রুটি ধারণকারী একটি ফলাফল বস্তু। এটি জাভা এর টীকা প্রক্রিয়াকরণ এবং প্রতিফলন ক্ষমতা প্রদর্শন করে।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
-`@Retention(RUNTIME)`এবং`@Target(FIELD)`দিয়ে টীকা সংজ্ঞায়িত করুন।
- ক্ষেত্রগুলি পুনরাবৃত্তি করতে`Class.getDeclaredFields()`ব্যবহার করুন৷
- টীকা মান পড়তে`Field.getAnnotation()`ব্যবহার করুন।
- টীকা সীমাবদ্ধতার সাথে ক্ষেত্রের মান তুলনা করুন।
- একটি তালিকায় লঙ্ঘন সংগ্রহ করুন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- প্রতিফলন ওভারহেড: বৈধতার জন্য গ্রহণযোগ্য (প্রতি অনুরোধে একবার বলা হয়)। হট পাথের জন্য, ক্যাশে ফিল্ড লুকআপ বা কম্পাইল-টাইম টীকা প্রক্রিয়াকরণ ব্যবহার করুন (যেমন হাইবারনেট ভ্যালিডেটর)।
- এক্সটেনসিবিলিটি:`validate()`এ টীকা + একটি হ্যান্ডলার ব্লক তৈরি করে নতুন টীকা যোগ করুন।
- উত্পাদন:`jakarta.validation`(Bean Validation 3.0) ব্যবহার করুন — এটি টীকা প্রসেসরের মাধ্যমে কম্পাইল-টাইম প্রক্রিয়াকরণ সহ এই এবং আরও অনেক কিছু করে।
### সমস্যা 3: পুনরায় চেষ্টা করে একটি রেট-সীমিত HTTP ক্লায়েন্ট তৈরি করুন
**সমস্যা বিবৃতি:** একটি HTTP ক্লায়েন্ট র‍্যাপার তৈরি করুন যা স্বয়ংক্রিয়ভাবে সূচকীয় ব্যাকঅফের সাথে ব্যর্থ অনুরোধগুলি পুনরায় চেষ্টা করে, হারের সীমাকে সম্মান করে এবং সার্কিট ব্রেকিং সমর্থন করে (একটি ব্যর্থ পরিষেবা কল করা বন্ধ করুন)৷
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) এক্সপোনেনশিয়াল ব্যাকঅফ এবং জিটার সহ যুক্তির পুনরায় চেষ্টা করুন, (2) লক্ষ্য পরিষেবাকে অপ্রতিরোধ্য এড়াতে হার সীমিত করুন, (3) সার্কিট ব্রেকার প্যাটার্ন — পরপর N ব্যর্থতার পরে, কুলডাউন সময়ের জন্য পরিষেবাটি কল করা বন্ধ করুন৷ এই তিনটি সংমিশ্রণযোগ্য উদ্বেগ.
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- বেস ক্লায়েন্ট হিসাবে`java.net.http.HttpClient`(জাভা 11+) ব্যবহার করুন।
- ব্যাকঅফের জন্য`Thread.sleep`এর সাথে একটি মোড়ক হিসাবে পুনঃপ্রচেষ্টা বাস্তবায়ন করুন৷
- হার সীমিত করার জন্য`Semaphore`ব্যবহার করুন (বা টোকেন বাকেটের জন্য `java.time`)।
- একটি স্টেট মেশিন হিসাবে সার্কিট ব্রেকার প্রয়োগ করুন: বন্ধ → খোলা → HALF_OPEN।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- জিটার সহ সূচকীয় ব্যাকঅফ বজ্রপাত প্রতিরোধ করে (একই সময়ে সমস্ত পুনঃপ্রচার চেষ্টা)।
- সার্কিট ব্রেকার:`failureThreshold`পরপর ব্যর্থতার পরে, সার্কিটটি `cooldownMs`-এর জন্য খোলে — ব্যর্থ পরিষেবা রক্ষা করে কোনও অনুরোধ পাঠানো হয় না।
- রেট লিমিটার:`Semaphore`পর্যায়ক্রমিক পুনরায় পূরণের ক্যাপ থ্রুপুট সহ।
- উত্পাদন:`resilience4j`ব্যবহার করুন — এটি যথাযথ বাস্তবায়ন, মেট্রিক্স এবং স্প্রিং বুট ইন্টিগ্রেশন সহ তিনটি প্যাটার্ন (পুনরায় চেষ্টা, রেট লিমিটার, সার্কিট ব্রেকার) প্রদান করে।
---

## সারাংশ
জাভা এখন পর্যন্ত নির্মিত সবচেয়ে গুরুত্বপূর্ণ প্রোগ্রামিং ভাষাগুলির মধ্যে একটি। এটি বিশ্বের ব্যাঙ্কিং সিস্টেম, অ্যান্ড্রয়েড ফোন, বড় ডেটা পাইপলাইন এবং এন্টারপ্রাইজ ব্যাকএন্ড চালায়। আধুনিক জাভা (21+) জাভা 8 থেকে খুব আলাদা একটি ভাষা - এটি আরও সংক্ষিপ্ত, আরও অভিব্যক্তিপূর্ণ এবং নতুন ভাষার সাথে ক্রমবর্ধমান প্রতিযোগিতামূলক। JVM ইকোসিস্টেম (Kotlin, Scala, Clojure) এর নাগাল আরও প্রসারিত করে। এন্টারপ্রাইজ ডেভেলপমেন্টের জন্য, জাভা একটি নিরাপদ এবং শক্তিশালী পছন্দ।