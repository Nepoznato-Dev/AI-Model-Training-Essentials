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
# Java
Java 是一种静态类型、面向对象的编程语言，由 Sun Microsystems 的 James Gosling 创建并于 1995 年发布。其设计理念“一次编写，随处运行”(WORA) 是通过 Java 虚拟机 (JVM) 实现的，它允许编译后的 Java 代码在任何具有 JVM 实现的平台上运行。 Java 是历史上使用最广泛的编程语言之一，为企业后端、Android 应用、大数据系统和金融服务提供支持。
尽管 Java 已有近 30 年的历史，但它仍在不断发展。现代 Java（版本 17+）包括记录、密封类、模式匹配、虚拟线程以及与更新语言竞争的不断发展的生态系统。
---

## 为什么 Java 很重要
- **企业标准**：财富 500 强后端的支柱 — 银行、保险、电子商务、医疗保健。
- **Android 开发**：Android 的主要语言（与 Kotlin 并列）。
- **大数据生态系统**：Apache Hadoop、Spark、Kafka、Elasticsearch — 全部用 Java 或 Scala 编写（在 JVM 上运行）。
- **庞大的生态系统**：Maven Central 上有超过 500,000 个库；满足各种需求的成熟工具。
- **性能**：JVM 的 JIT 编译器在运行时生成高度优化的机器代码，通常与长时间运行的应用程序的 C++ 相匹配。
- **向后兼容性**：为 Java 1.0 (1996) 编写的代码仍然可以在现代 JVM 上运行。
## 权衡
|限制|详情 |典型解决方法|
|------------|---------|--------------------|
| **冗长** |需要比 Python、Kotlin 或 Go 更多的样板文件 |使用 Lombok、文件 (Java 16+) 和现代 IDE |
| **内存使用情况** | JVM 开销意味着更高的基线内存 |调整 JVM 标志；使用 GraalVM 原生镜像进行小型部署 |
| **启动时间** |对于短期进程来说，JVM 预热可能会很慢 | GraalVM 原生镜像，或使用 C/Go 作为 CLI 工具 |
| **检查异常** |强制处理可能无法恢复的异常 |使用未经检查的异常或`Optional`模式 |
| **无值类型** |一切皆对象（直到 Valhalla 项目）|使用原始专用集合（Eclipse Collections、Trove） |
---

## 语法基础知识
### 基本结构
Java 是基于类的——一切都存在于类中。文件名必须与公共类名匹配。
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

### 面向对象编程
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

### Records (Java 16+) — 简洁数据类
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

### 异常处理
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

## 高级语法和模式
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

### 密封类和模式匹配 (Java 17+)
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

### 注释
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

### 函数式接口和 Lambda 函数
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

## 并发与并行
### 虚拟线程（Java 21+）
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

### 传统线程和同步
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

## 项目配置和构建系统
### 项目结构（Maven）
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

## 测试
### JUnit 5 与 Mockito
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

## 互操作性
### JNI（Java 本机接口）
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

### 外部函数和内存 API (Java 22+)
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

## 设计模式
### 构建器模式
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

### 观察者模式
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

## 性能与优化
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

### 优化技术
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

## 生态系统
### 构建工具
|工具|目的|笔记|
|------|---------|--------|
| **Maven** |构建自动化+依赖管理|基于 XML (`pom.xml`)；企业行业标准|
| **摇篮** |构建自动化+依赖管理| Groovy/Kotlin DSL；大型项目速度更快； Android 使用 |
### 框架
|框架|域名 |描述 |
|------------|--------|-------------|
| **Spring Boot** |网络/企业|占主导地位的 Java 框架 — REST API、微服务、安全性、数据访问 |
| **雅加达EE** |企业 | Java EE 的后继者；标准化企业API |
| **休眠** |对象关系管理 |对象关系映射；标准 JPA 实现 |
| **Micronaut / Quarkus** |云原生 |快速启动、低内存——专为无服务器和容器设计 |
### 测试
|工具|目的|
|------|---------|
| **JUnit 5** |单元测试框架|
| **莫基托** |模拟框架 |
| **断言J** |流畅的断言 |
| **测试容器** | Docker 中与真实数据库的集成测试 |
---

## JVM 生态系统
| JVM 语言 |与 Java 的关系 |
|----------|------------------------|
| **科特林** | Java 的现代替代方案； Google 首选的 Android 语言； 100% Java 兼容 |
| **斯卡拉** |函数式 + OOP 混合；为 Apache Spark 提供动力 |
| **Clojure** | JVM 上的 Lisp 方言；函数式编程 |
| **绝妙** | JVM 的动态脚本；在 Gradle 构建文件中使用 |
所有这些都可以使用Java库，Java也可以使用它们的库。 JVM 是一个平台，而不仅仅是 Java。
---

## Java 版本
|版本 |年份|主要特点|
|---------|------|-------------|
| Java 8 | 2014年| **LTS** — Lambda、Stream API、可选、默认方法。至今仍被广泛使用。 |
| Java 11 | 2018 | **LTS** — HTTP 客户端 API，用于局部变量的 `var`，单文件源启动器 |
| Java 17 | 2021 | **LTS** — 密封类、`instanceof` 的模式匹配、记录、文本块 |
| Java 21 | 2023 | **LTS** — **虚拟线程**（Project Loom），`switch` 的模式匹配，记录模式 |
| Java 25 | 2025 | 2025 **LTS** — 字符串模板、进一步模式匹配、外部函数 API |
**LTS**（长期支持）版本会持续多年更新。对于生产，请使用 Java 21 或更高版本。
---

## 何时使用 Java
|场景|为什么选择 Java |更好的选择|
|----------|---------|--------------------|
|企业后台 |庞大的生态系统，Spring Boot，经过规模验证 | Kotlin（相同的 JVM，更简洁）|
|安卓开发|已建立的庞大代码库 | Kotlin（Google 的首选）|
|大数据（Hadoop、Spark、Kafka）|生态系统构建于Java/Scala |用于数据科学方面的 Python |
|金融系统|性能+可靠性+成熟的工具| --|
|微服务| Spring Boot + 云原生框架 |寻求更简单的服务 |
|简单的脚本 |仪式太多 | Python、Shell |
| CLI 工具 |启动慢|去吧，鲁斯特 |
---

## 综合问答
### Q1：Java中`==`和`.equals()`有什么区别？
**A:**`==`比较对象引用（标识） - 它检查两个变量是否指向内存中的同一对象。 `.equals()`比较对象内容（值相等）。对于基元（`int`、`double`），`==` 直接比较值。对于对象（包括`String`），请始终使用`.equals()`来比较内容。唯一的例外是与`null`进行比较，其中`==`是正确的。
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

### Q2：JVM 垃圾收集器是如何工作的，我应该使用哪一个？
**A:** GC 会自动从不再可达的对象中回收内存。现代 JVM (21+) 提供多种收集器：G1（默认、平衡）、ZGC（超低暂停时间，<1 毫秒）和 Shenandoah（低暂停时间，OpenJDK）。对于大多数应用程序，默认的 G1 就可以了。对于延迟敏感的服务，请使用 ZGC (`-XX:+UseZGC`)。对于面向吞吐量的批处理，请使用并行 GC (`-XX:+UseParallelGC`)。
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### Q3：与传统循环相比，我什么时候应该使用 `Stream API`？
**答：** 当操作是清晰的管道（过滤器、映射、化简）时使用 Streams — 它们可以更好地表达意图，并且可以轻松地与`.parallelStream()`并行化。当您需要修改外部状态、当性能至关重要（流有开销）或当逻辑涉及复杂的控制流（中断、继续、多次返回）时，请使用传统循环进行简单迭代。避免使用流进行简单的`for-each`操作。
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

### Q4：现代 Java 中的记录、密封类和模式匹配是什么？
**答：** 记录 (Java 16) 是不可变的数据载体 - 它们自动生成构造函数、getter、`equals`、`hashCode`和`toString`。密封类 (Java 17) 限制哪些类可以扩展它们——对于建模有限类型层次结构很有用。模式匹配 (Java 21) 允许`switch`表达式解构类型、记录和值 — 替换冗长的`instanceof`链。
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

### Q5：如何正确处理检查异常和非检查异常？
**A:** 检查异常（`IOException`、`SQLException`）必须在`throws`中声明或捕获 - 它们代表调用者应该了解的可恢复条件。未经检查的异常（`RuntimeException`子类，如`NullPointerException`、`IllegalArgumentException`）代表编程错误。最佳实践：谨慎使用检查异常（它们会产生耦合），更喜欢使用`Optional`来避免预期的缺失，并在跨越 API 边界时将检查异常包装在未检查异常中。
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

## 解决问题的思路
### 问题 1：构建线程安全的生产者-消费者管道
**问题陈述：** 用 Ja​​va 设计一个生产者-消费者管道，其中多个生产者生成工作项，多个消费者同时处理它们，并且系统支持正常关闭并耗尽剩余项。
**第 1 步 — 了解问题：**
我们需要：（1）一个有界队列来缓冲生产者和消费者之间的工作项，（2）多个生产者线程添加项目，（3）多个消费者线程处理项目，（4）一种发出关闭信号并耗尽剩余项目的机制。 Java 的`BlockingQueue`就是专门为此构建的。
**第 2 步 — 确定方法：**
- 使用 `ArrayBlockingQueue`（有界）来防止无界内存增长。
- 使用毒丸模式作为关闭信号。
- 使用`ExecutorService`进行线程池管理。
- 使用`CountDownLatch`等待所有消费者完成排空。
**第 3 步 — 实施解决方案：**
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

**第 4 步 — 验证和优化：**
- 有界队列防止 OOM：`ArrayBlockingQueue(1000)` 限制内存。
- 毒丸模式：每个消费者收到药丸后干净利落地退出。
-`poll(1, SECONDS)`具有超时功能，可防止生产者速度缓慢时消费者永远阻塞。
- 生产：使用`LinkedBlockingQueue`实现无界，或使用`Disruptor`(LMAX) 实现超低延迟管道。
### 问题 2：实现基于注释的自定义验证器
**问题陈述：** 使用自定义注释创建验证框架。用户使用`@NotNull`、`@Min(0)`、`@Max(100)`、`@Size(min=1, max=50)`注释字段，并调用`Validator.validate(obj)`来获取违规列表。
**第 1 步 — 了解问题：**
我们需要：（1）带有参数的自定义注释，（2）一个在运行时读取注释的基于反射的验证器，（3）一个包含所有验证错误的结果对象。这展示了Java的注解处理和反射能力。
**第 2 步 — 确定方法：**
- 使用`@Retention(RUNTIME)`和`@Target(FIELD)`定义注释。
- 使用`Class.getDeclaredFields()`迭代字段。
- 使用`Field.getAnnotation()`读取注释值。
- 将字段值与注释约束进行比较。
- 将违规行为收集到列表中。
**第 3 步 — 实施解决方案：**
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

**第 4 步 — 验证和优化：**
- 反射开销：验证可接受（每个请求调用一次）。对于热路径，缓存字段查找或使用编译时注释处理（如 Hibernate Validator）。
- 可扩展性：通过在`validate()`中创建注释 + 处理程序块来添加新注释。
- 生产：使用 `jakarta.validation`（Bean Validation 3.0）——它可以完成所有这些工作，并通过注释处理器进行编译时处理。
### 问题 3：使用重试构建速率受限的 HTTP 客户端
**问题陈述：** 创建一个 HTTP 客户端包装器，以指数退避自动重试失败的请求，遵守速率限制，并支持熔断（停止调用失败的服务）。
**第 1 步 — 了解问题：**
我们需要：（1）具有指数退避和抖动的重试逻辑，（2）速率限制以避免压倒目标服务，（3）断路器模式 - 在连续 N 次失败后，停止调用服务一段冷却时间。这是三个可组合的关注点。
**第 2 步 — 确定方法：**
- 使用`java.net.http.HttpClient`(Java 11+) 作为基本客户端。
- 使用`Thread.sleep`作为包装器实现重试以进行退避。
- 使用`Semaphore`进行速率限制（或使用`java.time`进行令牌桶）。
- 将断路器实现为状态机：CLOSED → OPEN → HALF_OPEN。
**第 3 步 — 实施解决方案：**
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

**第 4 步 — 验证和优化：**
- 带有抖动的指数退避可防止惊群（所有重试同时发生）。
- 断路器：在`failureThreshold`连续失败后，`cooldownMs` 的电路打开 — 不发送任何请求，从而保护失败的服务。
- 速率限制器：`Semaphore`，具有定期补货上限吞吐量。
- 生产：使用`resilience4j`— 它提供所有三种模式（重试、速率限制器、断路器）以及正确的实现、指标和 Spring Boot 集成。
---

＃＃ 概括
Java 是有史以来最重要的编程语言之一。它运行着全球的银行系统、Android 手机、大数据管道和企业后端。现代 Java (21+) 是一种与 Java 8 非常不同的语言 — 它更简洁、更具表现力，并且与新语言相比更具竞争力。 JVM 生态系统（Kotlin、Scala、Clojure）进一步扩展了其影响范围。对于企业开发来说，Java 仍然是一个安全且强大的选择。