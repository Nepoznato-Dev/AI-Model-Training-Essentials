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
Java 是一種靜態類型、物件導向的程式語言，由 Sun Microsystems 的 James Gosling 創建並於 1995 年發布。其設計理念「一次編寫，隨處運行」(WORA) 是透過 Java 虛擬機 (JVM) 實現的，它允許編譯後的 Java 程式碼在任何具有 JVM 實現的平台上運行。 Java 是歷史上使用最廣泛的程式語言之一，為企業後端、Android 應用、大數據系統和金融服務提供支援。
儘管 Java 已有近 30 年的歷史，但它仍在不斷發展中。現代 Java（版本 17+）包括記錄、密封類別、模式匹配、虛擬線程以及與更新語言競爭的不斷發展的生態系統。
---

## 為什麼 Java 很重要
- **企業標準**：財富 500 強後端的支柱 — 銀行、保險、電子商務、醫​​療保健。
- **Android 開發**：Android 的主要語言（與 Kotlin 並列）。
- **大數據生態系統**：Apache Hadoop、Spark、Kafka、Elasticsearch — 全部以 Java 或 Scala 編寫（在 JVM 上運行）。
- **龐大的生態系統**：Maven Central 上有超過 500,000 個庫；滿足各種需求的成熟工具。
- **效能**：JVM 的 JIT 編譯器在執行時間產生高度最佳化的機器碼，通常與長時間運行的應用程式的 C++ 相符。
- **向後相容性**：為 Java 1.0 (1996) 編寫的程式碼仍然可以在現代 JVM 上運行。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **冗長** |需要比 Python、Kotlin 或 Go 更多的樣板檔案 |使用 Lombok、檔案 (Java 16+) 和現代 IDE |
| **記憶體使用情況** | JVM 開銷意味著更高的基線記憶體 |調整 JVM 標誌；使用 GraalVM 原生鏡像進行小型部署 |
| **啟動時間** |對於短期進程來說，JVM 預熱可能會很慢 | GraalVM 原生鏡像，或使用 C/Go 作為 CLI 工具 |
| **檢查異常** |強制處理可能無法恢復的異常 |使用未經檢查的異常或`Optional`模式 |
| **無值類型** |一切皆物件（直到 Valhalla 專案）|使用原始專用集合（Eclipse Collections、Trove） |
---

## 文法基礎知識
### 基本結構
Java 是基於類別的－一切都存在於類別中。檔案名稱必須與公共類別名稱相符。
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

### 物件導向編程
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

### Records (Java 16+) — 簡潔資料類
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

### 集合和流
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

### 例外處理
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

## 進階語法和模式
### 泛型
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

### 密封類別和模式匹配 (Java 17+)
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

### 註釋
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

### 函數式介面與 Lambda 函數
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

## 並發與平行
### 虛擬執行緒（Java 21+）
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

### 傳統執行緒與同步
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

## 專案配置與建置系統
### 專案結構（Maven）
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

### build.gradle.kts（Gradle）
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

### CI/CD 管道
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

## 測試
### JUnit 5 與 Mockito
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

## 互通性
### JNI（Java 本機介面）
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

### 外部函數與記憶體 API (Java 22+)
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

## 設計模式
### 建構器模式
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

### 觀察者模式
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

## 效能與最佳化
### 分析工具
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### 優化技術
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

## 部署
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

## 生態系統
### 建置工具
|工具|目的|筆記|
|------|---------|--------|
| **Maven** |建置自動化+依賴管理|基於 XML (`pom.xml`)；企業產業標準|
| **搖籃** |建立自動化+依賴管理| Groovy/Kotlin DSL；大型專案速度更快； Android 使用 |
### 框架
|框架|網域 |描述 |
|------------|--------|-------------|
| **Spring Boot** |網路/企業|主導的 Java 框架 — REST API、微服務、安全性、資料存取 |
| **雅加達EE** |企業 | Java EE 的後繼者；標準化企業API |
| **休眠** |物件關係管理 |物件關聯映射；標準 JPA 實作 |
| **Micronaut / Quarkus** |雲端原生 |快速啟動、低記憶體－專為無伺服器和容器設計 |
### 測試
|工具|目的|
|------|---------|
| **JUnit 5** |單元測試框架|
| **莫基托** |模擬框架 |
| **斷言J** |流暢的斷言 |
| **測試容器** | Docker 中與真實資料庫的整合測試 |
---

## JVM 生態系統
| JVM 語言 |與 Java 的關係 |
|----------|------------------------|
| **科特林** | Java 的現代替代方案； Google 首選的 Android 語言； 100% Java 相容 |
| **斯卡拉** |函數式 + OOP 混合；為 Apache Spark 提供動力 |
| **Clojure** | JVM 上的 Lisp 方言；函數式程式設計 |
| **絕妙** | JVM 的動態腳本；在 Gradle 建置檔中使用 |
所有這些都可以使用Java函式庫，Java也可以使用它們的函式庫。 JVM 是一個平台，而不僅僅是 Java。
---

## Java 版本
|版本 |年份|主要特點|
|---------|------|-------------|
| Java 8 | 2014年| **LTS** — Lambda、Stream API、可選、預設方法。至今仍被廣泛使用。 |
| Java 11 | 2018 | **LTS** — HTTP 用戶端 API，用於局部變數的 `var`，單一檔案來源啟動器 |
| Java 17 | 2021 | **LTS** — 密封類別、`instanceof` 的模式比對、記錄、文字區塊 |
| Java 21 | 2023 | **LTS** — **虛擬線程**（Project Loom），`switch` 的模式匹配，記錄模式 |
| Java 25 | 2025 | 2025 **LTS** — 字串範本、進一步模式比對、外部函數 API |
**LTS**（長期支援）版本會持續多年更新。對於生產，請使用 Java 21 或更高版本。
---

## 何時使用 Java
|場景|為什麼選擇 Java |更好的選擇|
|----------|---------|--------------------|
|企業後台 |龐大的生態系統，Spring Boot，經過規模驗證 | Kotlin（相同的 JVM，更簡潔）|
|安卓開發|已建立的龐大程式碼庫 | Kotlin（Google 的首選）|
|大數據（Hadoop、Spark、Kafka）|生態系統建構於Java/Scala |用於資料科學的 Python |
|金融系統|性能+可靠性+成熟的工具| --|
|微服務| Spring Boot + 雲端原生框架 |尋求更簡單的服務 |
|簡單的腳本 |儀式太多 | Python、Shell |
| CLI 工具 |啟動慢|去吧，魯斯特 |
---

## 綜合問答
### Q1：Java中`==`和`.equals()`有什麼差別？
**A:**`==`比較物件參考（標識） - 它檢查兩個變數是否指向記憶體中的相同物件。 `.equals()`比較物件內容（值相等）。對於基元（`int`、`double`），`==` 直接比較值。對於物件（包括`String`），請務必使用`.equals()`來比較內容。唯一的例外是與`null`進行比較，其中`==`是正確的。
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

### Q2：JVM 垃圾收集器是如何運作的，我該使用哪一個？
**A:** GC 會自動從不再可達的物件中回收記憶體。現代 JVM (21+) 提供多種收集器：G1（預設、平衡）、ZGC（超低暫停時間，<1 毫秒）和 Shenandoah（低暫停時間，OpenJDK）。對於大多數應用程序，預設的 G1 就可以了。對於延遲敏感的服務，請使用 ZGC (`-XX:+UseZGC`)。對於吞吐量導向的批次，請使用並行 GC (`-XX:+UseParallelGC`)。
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### Q3：與傳統循環相比，我什麼時候應該使用 `Stream API`？
**答：** 當操作是清晰的管道（過濾器、映射、化簡）時使用 Streams — 它們可以更好地表達意圖，並且可以輕鬆地與`.parallelStream()`並行化。當您需要修改外部狀態、當效能至關重要（流有開銷）或當邏輯涉及複雜的控制流（中斷、繼續、多次返回）時，請使用傳統循環進行簡單迭代。避免使用流程進行簡單的`for-each`操作。
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

### Q4：現代 Java 中的記錄、密封類別和模式匹配是什麼？
**答：** 記錄 (Java 16) 是不可變的資料載體 - 它們自動產生建構子、getter、`equals`、`hashCode`和`toString`。密封類別 (Java 17) 限制哪些類別可以擴展它們—對於建模有限類型層次結構很有用。模式匹配 (Java 21) 允許`switch`表達式解構類型、記錄和值 — 取代冗長的`instanceof`鏈。
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

### Q5：如何正確處理檢查異常和非檢查異常？
**A:** 檢查異常（`IOException`、`SQLException`）必須在`throws`中聲明或捕獲 - 它們代表呼叫者應該了解的可恢復條件。未經檢查的異常（`RuntimeException`子類，如`NullPointerException`、`IllegalArgumentException`）代表程式錯誤。最佳實踐：謹慎使用檢查異常（它們會產生耦合），偏好使用`Optional`來避免預期的缺失，並在跨越 API 邊界時將檢查異常包裝在未檢查異常中。
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

## 解決問題的思路
### 問題 1：建立線程安全的生產者-消費者管道
**問題陳述：** 用 Jva 設計一個生產者-消費者管道，其中多個生產者生成工作項，多個消費者同時處理它們，並且系統支援正常關閉並耗盡剩餘項。
**第 1 步 — 了解問題：**
我們需要：（1）一個有界隊列來緩衝生產者和消費者之間的工作項，（2）多個生產者線程添加項目，（3）多個消費者線程處理項目，（4）一種發出關閉信號並耗盡剩餘項目的機制。 Java 的`BlockingQueue`就是專門為此而建構的。
**第 2 步 — 確定方法：**
- 使用 `ArrayBlockingQueue`（有界）來防止無界記憶體成長。
- 使用毒丸模式作為關閉訊號。
- 使用`ExecutorService`進行執行緒池管理。
- 使用`CountDownLatch`等待所有消費者完成排空。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 有界佇列防止 OOM：`ArrayBlockingQueue(1000)` 限制記憶體。
- 毒丸模式：每個消費者收到藥丸後乾淨俐落地退出。
-`poll(1, SECONDS)`具有超時功能，可防止生產者速度緩慢時消費者永遠阻塞。
- 生產：使用`LinkedBlockingQueue`實現無界，或使用`Disruptor`(LMAX) 實現超低延遲管道。
### 問題 2：實作基於註解的自訂驗證器
**問題陳述：** 使用自訂註解建立驗證框架。使用者使用`@NotNull`、`@Min(0)`、`@Max(100)`、`@Size(min=1, max=50)`註解字段，並呼叫`Validator.validate(obj)`來取得違規清單。
**第 1 步 — 了解問題：**
我們需要：（1）帶有參數的自訂註釋，（2）一個在運行時讀取註釋的基於反射的驗證器，（3）一個包含所有驗證錯誤的結果物件。這展示了Java的註解處理和反射能力。
**第 2 步 — 確定方法：**
- 使用`@Retention(RUNTIME)`和`@Target(FIELD)`定義註解。
- 使用`Class.getDeclaredFields()`迭代欄位。
- 使用`Field.getAnnotation()`讀取註解值。
- 將欄位值與註解約束進行比較。
- 將違規行為收集到清單中。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 反射開銷：驗證可接受（每個請求呼叫一次）。對於熱路徑，快取欄位尋找或使用編譯時註解處理（如 Hibernate Validator）。
- 可擴充性：透過在`validate()`中建立註解 + 處理程序區塊來新增註解。
- 生產：使用 `jakarta.validation`（Bean Validation 3.0）－它可以完成所有這些工作，並透過註解處理器進行編譯時處理。
### 問題 3：使用重試建置速率受限的 HTTP 用戶端
**問題陳述：** 建立一個 HTTP 用戶端包裝器，以指數退避自動重試失敗的請求，遵守速率限制，並支援熔斷（停止呼叫失敗的服務）。
**第 1 步 — 了解問題：**
我們需要：（1）具有指數退避和抖動的重試邏輯，（2）速率限制以避免壓倒目標服務，（3）斷路器模式 - 在連續 N 次失敗後，停止呼叫服務一段冷卻時間。這是三個可組合的關注點。
**第 2 步 — 確定方法：**
- 使用`java.net.http.HttpClient`(Java 11+) 作為基本客戶端。
- 使用`Thread.sleep`作為包裝器實作重試以進行退避。
- 使用`Semaphore`進行速率限制（或使用`java.time`進行令牌桶）。
- 將斷路器實作為狀態機：CLOSED → OPEN → HALF_OPEN。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 有抖動的指數退避可防止驚群（所有重試同時發生）。
- 斷路器：在`failureThreshold`連續失敗後，`cooldownMs` 的電路開啟 — 不發送任何要求，從而保護失敗的服務。
- 速率限制器：`Semaphore`，具有定期補貨上限吞吐量。
- 生產：使用`resilience4j`— 它提供所有三種模式（重試、速率限制器、斷路器）以及正確的實作、指標和 Spring Boot 整合。
---

＃＃ 概括
Java 是有史以來最重要的程式語言之一。它運行著全球的銀行系統、Android 手機、大數據管道和企業後端。現代 Java (21+) 是一種與 Java 8 非常不同的語言 — 它更簡潔、更具表現力，並且與新語言相比更具競爭力。 JVM 生態系（Kotlin、Scala、Clojure）進一步擴展了其影響範圍。對於企業開發來說，Java 仍然是一個安全且強大的選擇。