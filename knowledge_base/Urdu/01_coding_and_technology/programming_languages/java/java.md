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

#جاوا
Java ایک مستحکم ٹائپ شدہ، آبجیکٹ پر مبنی پروگرامنگ لینگویج ہے جسے James Gosling نے Sun Microsystems میں تخلیق کیا تھا اور اسے 1995 میں ریلیز کیا گیا تھا۔ اس کا ڈیزائن فلسفہ — "ایک بار لکھیں، کہیں بھی چلائیں" (WORA) — جاوا ورچوئل مشین (JVM) کے ذریعے حاصل کیا جاتا ہے، جو مرتب کردہ جاوا کوڈ کو کسی بھی JVM پلیٹ فارم پر چلانے کی اجازت دیتا ہے۔ Java تاریخ میں سب سے زیادہ استعمال ہونے والی پروگرامنگ زبانوں میں سے ایک ہے، جو انٹرپرائز بیک اینڈز، اینڈرائیڈ ایپس، بڑے ڈیٹا سسٹمز، اور مالیاتی خدمات کو طاقتور بناتی ہے۔
تقریباً 30 سال کی عمر کے باوجود، جاوا کا ارتقا جاری ہے۔ جدید جاوا (ورژن 17+) میں ریکارڈز، سیل شدہ کلاسز، پیٹرن میچنگ، ورچوئل تھریڈز، اور ایک بڑھتا ہوا ماحولیاتی نظام شامل ہے جو نئی زبانوں کے ساتھ مقابلہ کرتا ہے۔
---

## جاوا کیوں اہمیت رکھتا ہے۔
- **انٹرپرائز کا معیار**: فارچیون 500 بیک اینڈز کی ریڑھ کی ہڈی — بینکنگ، انشورنس، ای کامرس، صحت کی دیکھ بھال۔
- **اینڈرائیڈ ڈیولپمنٹ**: اینڈرائیڈ کے لیے بنیادی زبان (کوٹلن کے ساتھ)۔
- **بگ ڈیٹا ایکو سسٹم**: Apache Hadoop, Spark, Kafka, Elasticsearch — سب جاوا یا Scala میں لکھا گیا ہے (جو JVM پر چلتا ہے)۔
- **بڑے پیمانے پر ماحولیاتی نظام**: ماون سینٹرل پر 500,000 سے زیادہ لائبریریاں؛ ہر ضرورت کے لئے بالغ ٹولنگ.
- **کارکردگی**: JVM کا JIT کمپائلر رن ٹائم پر انتہائی بہتر مشین کوڈ تیار کرتا ہے، جو اکثر طویل عرصے سے چلنے والی ایپلیکیشنز کے لیے C++ سے ملتا ہے۔
- **پیچھے کی طرف مطابقت**: Java 1.0 (1996) کے لیے لکھا ہوا کوڈ اب بھی جدید JVMs پر چلتا ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **لفظی** | Python، Kotlin، یا Go | سے زیادہ بوائلر پلیٹ کی ضرورت ہوتی ہے۔ لومبوک، ریکارڈز (جاوا 16+) اور جدید IDEs کا استعمال کریں۔
| **میموری کا استعمال** | JVM اوور ہیڈ کا مطلب ہے اعلیٰ بنیادی میموری | JVM جھنڈوں کو ٹیون کریں؛ چھوٹی تعیناتیوں کے لیے GraalVM مقامی تصاویر استعمال کریں۔
| **شروع کا وقت** | JVM وارم اپ مختصر مدت کے عمل کے لیے سست ہو سکتا ہے | GraalVM مقامی تصویر، یا CLI ٹولز کے لیے C/Go استعمال کریں۔
| **چیک شدہ مستثنیات** | مستثنیات کو ہینڈل کرنے پر مجبور کرتا ہے جو قابل بازیافت نہیں ہوسکتے ہیں | غیر نشان زد مستثنیات یا`Optional`پیٹرن استعمال کریں۔
| **کوئی قدر کی قسم نہیں** | ہر چیز ایک چیز ہے (والہلہ پروجیکٹ تک) | قدیم مخصوص مجموعے استعمال کریں (ایکلیپس کلیکشن، ٹروو) |
---

## نحوی بنیادی باتیں
### بنیادی ڈھانچہ
جاوا کلاس پر مبنی ہے - ہر چیز کلاس کے اندر رہتی ہے۔ فائل کا نام پبلک کلاس کے نام سے مماثل ہونا چاہیے۔
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

### آبجیکٹ اورینٹڈ پروگرامنگ
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

### ریکارڈز (جاوا 16+) — جامع ڈیٹا کلاسز
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

### مجموعے اور سلسلے
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

### استثنیٰ ہینڈلنگ
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

## اعلی درجے کی نحو اور نمونے۔
### عام
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

### مہر بند کلاسز اور پیٹرن میچنگ (جاوا 17+)
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

### تشریحات
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

### فنکشنل انٹرفیس اور لیمبڈاس
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

## ہم آہنگی اور ہم آہنگی
### ورچوئل تھریڈز (جاوا 21+)
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

### روایتی تھریڈنگ اور سنکرونائزیشن
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ (Maven)
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

### build.gradle.kts (گریڈل)
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

### CI/CD پائپ لائن
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

## ٹیسٹنگ
### JUnit 5 موکیٹو کے ساتھ
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

## انٹرآپریبلٹی
### JNI (جاوا مقامی انٹرفیس)
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

### غیر ملکی فنکشن اور میموری API (جاوا 22+)
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

## ڈیزائن پیٹرن
### بلڈر پیٹرن
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

### مبصر پیٹرن
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### اصلاح کی تکنیک
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

## تعیناتی۔
### ڈاکر فائل
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

## ماحولیاتی نظام
### ٹولز بنائیں
| ٹول | مقصد | نوٹس |
|------|---------|------|
| **ماون** | آٹومیشن + انحصار کا انتظام بنائیں | XML پر مبنی (`pom.xml`); انٹرپرائز کے لئے صنعت کا معیار |
| **گریڈل** | آٹومیشن + انحصار کا انتظام بنائیں | گرووی/کوٹلن ڈی ایس ایل؛ بڑے منصوبوں کے لیے تیز؛ اینڈرائیڈ کے ذریعہ استعمال کیا جاتا ہے |
### فریم ورک
| فریم ورک | ڈومین | تفصیل |
|------------|---------|------------|
| **اسپرنگ بوٹ** | ویب / انٹرپرائز | غالب جاوا فریم ورک — REST APIs، مائیکرو سروسز، سیکورٹی، ڈیٹا تک رسائی |
| **جکارتہ EE** | انٹرپرائز | جاوا EE کا جانشین؛ معیاری انٹرپرائز APIs |
| **ہائبرنیٹ** | ORM | آبجیکٹ-ریلیشنل میپنگ؛ معیاری JPA نفاذ |
| **مائکروناٹ / کوارکس** | کلاؤڈ-آبائی | تیز آغاز، کم میموری — بغیر سرور اور کنٹینرز کے لیے ڈیزائن کیا گیا ہے۔
### ٹیسٹنگ
| ٹول | مقصد |
|------|---------|
| **جونائٹ 5** | یونٹ ٹیسٹنگ فریم ورک |
| **موکیٹو** | طنزیہ فریم ورک |
| **AssertJ** | روانی کے دعوے |
| **ٹیسٹ کنٹینرز** | ڈوکر میں حقیقی ڈیٹا بیس کے ساتھ انٹیگریشن ٹیسٹ |
---

## جے وی ایم ایکو سسٹم
| JVM زبان | جاوا سے تعلق |
|----------------------------|----------------------|
| **کوٹلن** | جاوا کا جدید متبادل؛ گوگل کی ترجیحی اینڈرائیڈ زبان؛ 100% جاوا کے موافق |
| **اسکالہ** | فنکشنل + OOP ہائبرڈ؛ پاورز اپاچی اسپارک |
| **کلجور** | جے وی ایم پر لِسپ بولی؛ فنکشنل پروگرامنگ |
| **گرووی** | JVM کے لیے متحرک اسکرپٹنگ؛ گریڈل بلڈ فائلوں میں استعمال کیا جاتا ہے |
یہ سب جاوا لائبریریوں کا استعمال کر سکتے ہیں، اور جاوا اپنی لائبریریوں کو استعمال کر سکتے ہیں۔ جے وی ایم ایک پلیٹ فارم ہے، نہ صرف جاوا۔
---

## جاوا ورژن
| ورژن | سال | اہم خصوصیات |
|---------|------|------------|
| جاوا 8 | 2014 | **LTS** — لیمبڈاس، اسٹریم API، اختیاری، پہلے سے طے شدہ طریقے۔ اب بھی بڑے پیمانے پر استعمال کیا جاتا ہے. |
| جاوا 11 | 2018 | **LTS** — HTTP کلائنٹ API، مقامی متغیرات کے لیے `var`، سنگل فائل سورس لانچر |
| جاوا 17 | 2021 | **LTS** — مہر بند کلاسز،`instanceof`کے لیے پیٹرن میچنگ، ریکارڈز، ٹیکسٹ بلاکس |
| جاوا 21 | 2023 | **LTS** — **ورچوئل تھریڈز** (پروجیکٹ لوم)،`switch`کے لیے پیٹرن میچنگ، ریکارڈ پیٹرن |
| جاوا 25 | 2025 | **LTS** — سٹرنگ ٹیمپلیٹس، مزید پیٹرن میچنگ، غیر ملکی فنکشن API |
**LTS** (طویل مدتی سپورٹ) ورژن کئی سالوں تک اپ ڈیٹس وصول کرتے ہیں۔ پروڈکشن کے لیے، Java 21 یا اس کے بعد کا استعمال کریں۔
---

## جاوا کب استعمال کریں۔
| منظر نامہ | کیوں جاوا | بہتر متبادل |
|------------|---------|-------------------|
| انٹرپرائز بیک اینڈز | بڑے پیمانے پر ماحولیاتی نظام، بہار بوٹ، پیمانے پر ثابت | کوٹلن (وہی JVM، کم لفظی) |
| اینڈرائیڈ ڈویلپمنٹ | قائم، بہت بڑا کوڈ بیس | کوٹلن (گوگل کا پسندیدہ انتخاب) |
| بڑا ڈیٹا (ہڈوپ، اسپارک، کافکا) | ماحولیاتی نظام Java/Scala | پر بنایا گیا ہے۔ ڈیٹا سائنس سائڈ کے لیے ازگر |
| مالیاتی نظام | کارکردگی + وشوسنییتا + بالغ ٹولنگ | -- |
| مائیکرو سروسز | اسپرنگ بوٹ + کلاؤڈ-آبائی فریم ورک | آسان خدمات کے لیے جائیں |
| سادہ سکرپٹ | بہت زیادہ تقریب | ازگر، شیل |
| CLI ٹولز | سست آغاز | جاؤ، مورچا |
---

## مصنوعی سوال و جواب
### Q1: Java میں`==`اور`.equals()`میں کیا فرق ہے؟
**A:**`==`آبجیکٹ کے حوالہ جات (شناخت) کا موازنہ کرتا ہے — یہ چیک کرتا ہے کہ آیا دو متغیرات میموری میں ایک ہی چیز کی طرف اشارہ کرتے ہیں۔ `.equals()`آبجیکٹ مواد (قدر مساوات) کا موازنہ کرتا ہے۔ قدیم (`int`,`double`) کے لیے،`==`اقدار کا براہ راست موازنہ کرتا ہے۔ اشیاء (بشمول`String`) کے لیے، مواد کا موازنہ کرنے کے لیے ہمیشہ`.equals()`استعمال کریں۔ واحد استثنا`null`کے ساتھ موازنہ کرنا ہے، جہاں`==`درست ہے۔
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

### Q2: JVM کوڑا اٹھانے والا کیسے کام کرتا ہے، اور مجھے کون سا استعمال کرنا چاہیے؟
**A:** GC خود بخود ان اشیاء سے میموری کا دوبارہ دعوی کرتا ہے جو اب قابل رسائی نہیں ہیں۔ جدید JVMs (21+) کئی جمع کرنے والے پیش کرتے ہیں: G1 (پہلے سے طے شدہ، متوازن)، ZGC (انتہائی کم توقف کے اوقات، <1ms)، اور Shenandoah (کم توقف، OpenJDK)۔ زیادہ تر ایپلیکیشنز کے لیے، ڈیفالٹ G1 ٹھیک ہے۔ تاخیر سے متعلق حساس خدمات کے لیے، ZGC (`-XX:+UseZGC`) استعمال کریں۔ تھرو پٹ پر مبنی بیچ پروسیسنگ کے لیے، متوازی GC ( `-XX:+UseParallelGC`) استعمال کریں۔
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### Q3: مجھے`Stream API`بمقابلہ روایتی لوپس کب استعمال کرنا چاہئے؟
**A:** جب آپریشن واضح پائپ لائن ہو تو اسٹریمز کا استعمال کریں (فلٹر، نقشہ، کم) — وہ اپنے ارادے کا بہتر اظہار کرتے ہیں اور آسانی سے`.parallelStream()`کے ساتھ متوازی ہوتے ہیں۔ سادہ تکرار کے لیے روایتی لوپس استعمال کریں، جب آپ کو بیرونی حالت میں ترمیم کرنے کی ضرورت ہو، جب کارکردگی اہم ہو (اسٹریمز میں اوور ہیڈ ہو)، یا جب منطق میں پیچیدہ کنٹرول کا بہاؤ شامل ہو (بریک، جاری رکھیں، متعدد واپسی)۔ سادہ`for-each`آپریشنز کے لیے اسٹریمز سے گریز کریں۔
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

### Q4: جدید جاوا میں ریکارڈز، سیل شدہ کلاسز، اور پیٹرن میچنگ کیا ہیں؟
**A:** ریکارڈز (جاوا 16) ناقابل تغیر ڈیٹا کیریئرز ہیں — وہ کنسٹرکٹرز، گیٹرز، `equals`، `hashCode`، اور`toString`کو خود بخود تیار کرتے ہیں۔ مہر بند کلاسز (جاوا 17) محدود کرتی ہیں کہ کون سی کلاسز ان کو بڑھا سکتی ہیں - محدود قسم کے درجہ بندی کے ماڈلنگ کے لیے مفید۔ پیٹرن کی مماثلت (جاوا 21)`switch`اظہار کی اقسام، ریکارڈز، اور اقدار کو تباہ کرنے کی اجازت دیتی ہے — وربوز`instanceof`چینز کی جگہ لے کر۔
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

### Q5: میں چیک شدہ بمقابلہ غیر چیک شدہ مستثنیات کو صحیح طریقے سے کیسے ہینڈل کروں؟
**A:** چیک شدہ مستثنیات (`IOException`,`SQLException`) کا اعلان`throws`میں کیا جانا چاہیے یا پکڑا جانا چاہیے — وہ قابل بازیافت حالات کی نمائندگی کرتے ہیں جن کے بارے میں کال کرنے والے کو معلوم ہونا چاہیے۔ غیر نشان زد مستثنیات (`RuntimeException` ذیلی طبقات جیسے `NullPointerException`،`IllegalArgumentException`) پروگرامنگ کیڑے کی نمائندگی کرتے ہیں۔ بہترین پریکٹس: چیک شدہ مستثنیات کو تھوڑا سا استعمال کریں (وہ جوڑے بناتے ہیں)، متوقع غیر موجودگی کے لیے`Optional`کو ترجیح دیں، اور API کی حدود کو عبور کرتے وقت چیک شدہ مستثنیات کو غیر چیک شدہ میں لپیٹیں۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: تھریڈ سے محفوظ پروڈیوسر-صارف پائپ لائن بنائیں
**مسئلہ کا بیان:** جاوا میں ایک پروڈیوسر کنزیومر پائپ لائن ڈیزائن کریں جہاں ایک سے زیادہ پروڈیوسرز کام کی اشیاء تیار کرتے ہیں، متعدد صارفین بیک وقت ان پر کارروائی کرتے ہیں، اور سسٹم بقیہ آئٹمز کی نکاسی کے ساتھ خوبصورت شٹ ڈاؤن کو سپورٹ کرتا ہے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) پروڈیوسر اور صارفین کے درمیان کام کی اشیاء کو بفر کرنے کے لیے ایک پابند قطار، (2) ایک سے زیادہ پروڈیوسر تھریڈز جو آئٹمز شامل کرتے ہیں، (3) ایک سے زیادہ کنزیومر تھریڈز پراسیسنگ آئٹمز، (4) ایک طریقہ کار بند کرنے اور باقی اشیاء کو نکالنے کا اشارہ دینے کے لیے۔ جاوا کا`BlockingQueue`اس کے لیے مقصد سے بنایا گیا ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- بے حد میموری کی ترقی کو روکنے کے لیے`ArrayBlockingQueue`(باؤنڈڈ) کا استعمال کریں۔
- شٹ ڈاؤن سگنلنگ کے لیے زہر کی گولی کا نمونہ استعمال کریں۔
- تھریڈ پول مینجمنٹ کے لیے`ExecutorService`استعمال کریں۔
- تمام صارفین کے ختم ہونے کا انتظار کرنے کے لیے`CountDownLatch`استعمال کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- پابند قطار OOM کو روکتی ہے:`ArrayBlockingQueue(1000)`میموری کو محدود کرتی ہے۔
- زہر کی گولی کا نمونہ: ہر صارف اپنی گولی لینے کے بعد صاف طور پر باہر نکلتا ہے۔
-`poll(1, SECONDS)`ٹائم آؤٹ کے ساتھ صارفین کو ہمیشہ کے لیے بلاک ہونے سے روکتا ہے اگر پروڈیوسرز سست ہیں۔
- پیداوار: بے حد کے لیے `LinkedBlockingQueue`، یا انتہائی کم تاخیر والی پائپ لائنوں کے لیے`Disruptor`(LMAX) استعمال کریں۔
### مسئلہ 2: حسب ضرورت تشریح پر مبنی توثیق کار کو لاگو کریں۔
**مسئلہ کا بیان:** حسب ضرورت تشریحات کا استعمال کرتے ہوئے توثیق کا فریم ورک بنائیں۔ صارفین`@NotNull`,`@Min(0)`,`@Max(100)`,`@Size(min=1, max=50)`کے ساتھ فیلڈز کی تشریح کرتے ہیں اور خلاف ورزیوں کی فہرست حاصل کرنے کے لیے`Validator.validate(obj)`کو کال کرتے ہیں۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) پیرامیٹرز کے ساتھ حسب ضرورت تشریحات، (2) ایک عکاسی پر مبنی توثیق کار جو رن ٹائم پر تشریحات پڑھتا ہے، (3) ایک نتیجہ آبجیکٹ جس میں توثیق کی تمام خرابیاں ہوں۔ یہ جاوا کی تشریح پروسیسنگ اور عکاسی کی صلاحیتوں کو ظاہر کرتا ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
-`@Retention(RUNTIME)`اور`@Target(FIELD)`کے ساتھ تشریحات کی وضاحت کریں۔
- کھیتوں کو اعادہ کرنے کے لیے`Class.getDeclaredFields()`استعمال کریں۔
- تشریحی اقدار کو پڑھنے کے لیے`Field.getAnnotation()`استعمال کریں۔
- تشریحی رکاوٹوں کے خلاف فیلڈ کی اقدار کا موازنہ کریں۔
- ایک فہرست میں خلاف ورزیوں کو جمع کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- ریفلیکشن اوور ہیڈ: توثیق کے لیے قابل قبول (ایک بار فی درخواست کہا جاتا ہے)۔ گرم راستوں کے لیے، کیش فیلڈ تلاش کریں یا کمپائل ٹائم اینوٹیشن پروسیسنگ استعمال کریں (جیسے ہائبرنیٹ ویلیڈیٹر)۔
- توسیع پذیری:`validate()`میں تشریح + ایک ہینڈلر بلاک بنا کر نئی تشریحات شامل کریں۔
- پروڈکشن:`jakarta.validation`(Bean Validation 3.0) کا استعمال کریں — یہ تشریحی پروسیسرز کے ذریعے کمپائل ٹائم پروسیسنگ کے ساتھ یہ سب اور بہت کچھ کرتا ہے۔
### مسئلہ 3: دوبارہ کوشش کے ساتھ ریٹ محدود HTTP کلائنٹ بنائیں
**مسئلہ کا بیان:** ایک HTTP کلائنٹ ریپر بنائیں جو ناکام ہونے والی درخواستوں کو ایکسپونینشل بیک آف کے ساتھ دوبارہ آزماتا ہے، شرح کی حدود کا احترام کرتا ہے، اور سرکٹ بریکنگ کو سپورٹ کرتا ہے (ناکام سروس کو کال کرنا بند کریں)۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) ایکسپونینشل بیک آف اور جٹر کے ساتھ دوبارہ منطق کی کوشش کریں، (2) ٹارگٹ سروس کو مغلوب کرنے سے بچنے کے لیے شرح کو محدود کرنا، (3) سرکٹ بریکر پیٹرن — N مسلسل ناکامیوں کے بعد، سروس کو کولڈاؤن مدت کے لیے کال کرنا بند کریں۔ یہ تین کمپوز ایبل خدشات ہیں۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
-`java.net.http.HttpClient`(جاوا 11+) کو بیس کلائنٹ کے طور پر استعمال کریں۔
- بیک آف کے لیے`Thread.sleep`کے ساتھ ریپر کے طور پر دوبارہ کوشش کو لاگو کریں۔
- شرح کو محدود کرنے کے لیے`Semaphore`استعمال کریں (یا ٹوکن بالٹی کے لیے `java.time`)۔
- سرکٹ بریکر کو ریاستی مشین کے طور پر لاگو کریں: بند → کھلا → HALF_OPEN۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- گھنٹی کے ساتھ تیز رفتار بیک آف گرجنے والے ریوڑ کو روکتا ہے (ایک ہی وقت میں مارنے کی تمام کوششیں)۔
- سرکٹ بریکر:`failureThreshold`کی مسلسل ناکامیوں کے بعد، سرکٹ`cooldownMs`کے لیے کھل جاتا ہے — ناکام سروس کی حفاظت کرتے ہوئے کوئی درخواست نہیں بھیجی جاتی ہے۔
- ریٹ محدود کرنے والا:`Semaphore`متواتر دوبارہ بھرنے والے کیپس تھرو پٹ کے ساتھ۔
- پیداوار: استعمال کریں`resilience4j`— یہ تینوں پیٹرن (دوبارہ کوشش، ریٹ محدود کرنے والا، سرکٹ بریکر) مناسب نفاذ، میٹرکس، اور اسپرنگ بوٹ انضمام کے ساتھ فراہم کرتا ہے۔
---

## خلاصہ
جاوا اب تک کی تخلیق کردہ سب سے اہم پروگرامنگ زبانوں میں سے ایک ہے۔ یہ دنیا کے بینکنگ سسٹمز، اینڈرائیڈ فونز، بڑی ڈیٹا پائپ لائنز، اور انٹرپرائز بیک اینڈز چلاتا ہے۔ جدید جاوا (21+) Java 8 سے بہت مختلف زبان ہے — یہ زیادہ جامع، زیادہ اظہار خیال، اور نئی زبانوں کے ساتھ تیزی سے مسابقتی ہے۔ JVM ماحولیاتی نظام (Kotlin, Scala, Clojure) اپنی رسائی کو مزید بڑھاتا ہے۔ انٹرپرائز کی ترقی کے لیے، Java ایک محفوظ اور طاقتور انتخاب ہے۔