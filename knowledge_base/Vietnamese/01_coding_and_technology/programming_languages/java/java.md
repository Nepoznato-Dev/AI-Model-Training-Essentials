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
Java là ngôn ngữ lập trình hướng đối tượng, được gõ tĩnh do James Gosling tại Sun Microsystems tạo ra và phát hành vào năm 1995. Triết lý thiết kế của nó — "viết một lần, chạy mọi nơi" (WORA) — đạt được thông qua Máy ảo Java (JVM), cho phép mã Java được biên dịch để chạy trên bất kỳ nền tảng nào có triển khai JVM. Java là một trong những ngôn ngữ lập trình được sử dụng rộng rãi nhất trong lịch sử, hỗ trợ các chương trình phụ trợ doanh nghiệp, ứng dụng Android, hệ thống dữ liệu lớn và dịch vụ tài chính.
Dù đã gần 30 tuổi nhưng Java vẫn tiếp tục phát triển. Java hiện đại (phiên bản 17+) bao gồm các bản ghi, lớp kín, khớp mẫu, luồng ảo và hệ sinh thái đang phát triển cạnh tranh với các ngôn ngữ mới hơn.
---

## Tại sao Java lại quan trọng
- **Tiêu chuẩn doanh nghiệp**: Xương sống của hệ thống phụ trợ Fortune 500 — ngân hàng, bảo hiểm, thương mại điện tử, chăm sóc sức khỏe.
- **Phát triển Android**: Ngôn ngữ chính dành cho Android (cùng với Kotlin).
- **Hệ sinh thái dữ liệu lớn**: Apache Hadoop, Spark, Kafka, Elaticsearch — tất cả đều được viết bằng Java hoặc Scala (chạy trên JVM).
- **Hệ sinh thái khổng lồ**: Hơn 500.000 thư viện trên Maven Central; công cụ trưởng thành cho mọi nhu cầu.
- **Hiệu suất**: Trình biên dịch JIT của JVM tạo ra mã máy được tối ưu hóa cao trong thời gian chạy, thường khớp với C++ cho các ứng dụng chạy dài.
- **Khả năng tương thích ngược**: Mã được viết cho Java 1.0 (1996) vẫn chạy trên các JVM hiện đại.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Tính chi tiết** | Yêu cầu nhiều bản soạn sẵn hơn Python, Kotlin hoặc Go | Sử dụng Lombok, bản ghi (Java 16+) và IDE hiện đại |
| **Sử dụng bộ nhớ** | Chi phí JVM có nghĩa là bộ nhớ cơ sở cao hơn | Điều chỉnh cờ JVM; sử dụng hình ảnh gốc GraalVM cho các triển khai nhỏ |
| **Thời gian khởi động** | Quá trình khởi động JVM có thể chậm đối với các quy trình tồn tại trong thời gian ngắn | Hình ảnh gốc GraalVM hoặc sử dụng C/Go cho các công cụ CLI |
| **Đã kiểm tra các trường hợp ngoại lệ** | Buộc xử lý các trường hợp ngoại lệ có thể không thể phục hồi được | Sử dụng các ngoại lệ không được kiểm tra hoặc mẫu`Optional`|
| **Không có loại giá trị** | Mọi thứ đều là đối tượng (cho đến dự án Valhalla) | Sử dụng các bộ sưu tập chuyên biệt nguyên thủy (Bộ sưu tập Eclipse, Trove) |
---

##Cơ bản về cú pháp
###Cấu trúc cơ bản
Java dựa trên lớp - mọi thứ đều tồn tại bên trong một lớp. Tên tệp phải khớp với tên lớp công khai.
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

### Lập trình hướng đối tượng
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

### Bản ghi (Java 16+) — Các lớp dữ liệu ngắn gọn
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

### Bộ sưu tập và luồng
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

### Xử lý ngoại lệ
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

## Cú pháp & Mẫu nâng cao
### Thuốc gốc
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

### Các lớp kín và So khớp mẫu (Java 17+)
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

### Chú thích
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

### Giao diện chức năng và Lambda
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

## Đồng thời & Song song
### Chủ đề ảo (Java 21+)
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

### Phân luồng và đồng bộ hóa truyền thống
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án (Maven)
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

### Đường ống CI/CD
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

##Thử nghiệm
### JUnit 5 với Mockito
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

## Khả năng tương tác
### JNI (Giao diện gốc Java)
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

### API bộ nhớ và hàm ngoại (Java 22+)
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

## Mẫu thiết kế
### Mẫu trình tạo
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

### Mẫu người quan sát
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

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### Kỹ thuật tối ưu hóa
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

## Triển khai
###Tệp Docker
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

## Hệ sinh thái
### Công cụ xây dựng
| Công cụ | Mục đích | Ghi chú |
|------|----------|-------|
| **Maven** | Xây dựng tự động hóa + quản lý phụ thuộc | Dựa trên XML (`pom.xml`); chuẩn ngành dành cho doanh nghiệp |
| **Cấp độ** | Xây dựng tự động hóa + quản lý phụ thuộc | Groovy/Kotlin DSL; nhanh hơn cho các dự án lớn; được sử dụng bởi Android |
### Khung
| Khung | Tên miền | Mô tả |
|----------|----------|-------------|
| **Khởi động mùa xuân** | Web / doanh nghiệp | Khung Java chiếm ưu thế - API REST, dịch vụ vi mô, bảo mật, truy cập dữ liệu |
| **Jakarta EE** | Doanh nghiệp | Người kế thừa Java EE; API doanh nghiệp được tiêu chuẩn hóa |
| **Ngủ đông** | ORM | Ánh xạ quan hệ đối tượng; việc triển khai JPA tiêu chuẩn |
| **Micronaut / Quarkus** | Bản địa trên nền tảng đám mây | Khởi động nhanh, ít bộ nhớ — được thiết kế cho serverless và container |
###Thử nghiệm
| Công cụ | Mục đích |
|------|----------|
| **JUnit 5** | Khung kiểm tra đơn vị |
| **Mockito** | Khung mô phỏng |
| **Khẳng địnhJ** | Khẳng định trôi chảy |
| **Vùng chứa thử nghiệm** | Kiểm tra tích hợp với cơ sở dữ liệu thực trong Docker |
---

## Hệ sinh thái JVM
| Ngôn ngữ JVM | Mối quan hệ với Java |
|-------------|----------------------|
| **Kotlin** | Thay thế hiện đại cho Java; Ngôn ngữ Android ưa thích của Google; Tương thích 100% với Java |
| **Scala** | Chức năng + OOP lai; quyền hạn Apache Spark |
| **Clojure** | Phương ngữ Lisp trên JVM; lập trình chức năng |
| ** Hấp dẫn ** | Kịch bản động cho JVM; được sử dụng trong tệp bản dựng Gradle |
Tất cả những thứ này đều có thể sử dụng thư viện Java và Java có thể sử dụng thư viện của chúng. JVM là nền tảng, không chỉ Java.
---

## Phiên bản Java
| Phiên bản | Năm | Các tính năng chính |
|----------|------|-------------|
| Java 8 | 2014 | **LTS** — Lambdas, API truyền phát, các phương thức mặc định, tùy chọn. Vẫn được sử dụng rộng rãi. |
| Java 11 | 2018 | **LTS** — API máy khách HTTP,`var`cho các biến cục bộ, trình khởi chạy nguồn một tệp |
| Java 17 | 2021 | **LTS** — Các lớp kín, khớp mẫu cho `instanceof`, bản ghi, khối văn bản |
| Java 21 | 2023 | **LTS** — **Chủ đề ảo** (Project Loom), khớp mẫu cho`switch`, mẫu bản ghi |
| Java 25 | 2025 | **LTS** — Mẫu chuỗi, khớp mẫu thêm, API hàm ngoại |
**Phiên bản LTS** (Hỗ trợ dài hạn) nhận được bản cập nhật trong nhiều năm. Để sản xuất, hãy sử dụng Java 21 trở lên.
---

## Khi nào nên sử dụng Java
| Kịch bản | Tại sao Java | Thay thế tốt hơn |
|----------|----------|-------------------|
| Phụ trợ doanh nghiệp | Hệ sinh thái khổng lồ, Spring Boot, đã được chứng minh trên quy mô lớn | Kotlin (cùng JVM, ít dài dòng hơn) |
| Phát triển Android | Đã có uy tín, cơ sở mã khổng lồ | Kotlin (lựa chọn ưu tiên của Google) |
| Dữ liệu lớn (Hadoop, Spark, Kafka) | Hệ sinh thái được xây dựng trên Java/Scala | Python dành cho lĩnh vực khoa học dữ liệu |
| Hệ thống tài chính | Hiệu suất + độ tin cậy + công cụ hoàn thiện | -- |
| Dịch vụ vi mô | Spring Boot + framework gốc trên nền tảng đám mây | Sử dụng các dịch vụ đơn giản hơn |
| Kịch bản đơn giản | Lễ quá nhiều | Python, Shell |
| công cụ CLI | Khởi động chậm | Đi đi, Rust |
---

## Hỏi đáp tổng hợp
### Q1: Sự khác biệt giữa`==`và`.equals()`trong Java là gì?
**A:**`==`so sánh các tham chiếu đối tượng (danh tính) — nó kiểm tra xem hai biến có trỏ đến cùng một đối tượng trong bộ nhớ hay không. `.equals()`so sánh nội dung đối tượng (giá trị bằng nhau). Đối với giá trị nguyên thủy (`int`,`double`),`==`so sánh trực tiếp các giá trị. Đối với các đối tượng (bao gồm`String`), hãy luôn sử dụng`.equals()`để so sánh nội dung. Ngoại lệ duy nhất là so sánh với `null`, trong đó`==`là chính xác.
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

### Câu hỏi 2: Trình thu gom rác JVM hoạt động như thế nào và tôi nên sử dụng trình thu thập rác nào?
**A:** GC tự động lấy lại bộ nhớ từ các đối tượng không thể truy cập được nữa. Các JVM hiện đại (21+) cung cấp một số bộ sưu tập: G1 (mặc định, cân bằng), ZGC (thời gian tạm dừng cực thấp, <1ms) và Shenandoah (tạm dừng thấp, OpenJDK). Đối với hầu hết các ứng dụng, G1 mặc định là ổn. Đối với các dịch vụ nhạy cảm với độ trễ, hãy sử dụng ZGC (`-XX:+UseZGC`). Để xử lý hàng loạt theo định hướng thông lượng, hãy sử dụng Parallel GC (`-XX:+UseParallelGC`).
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### Câu 3: Khi nào tôi nên sử dụng`Stream API`so với vòng lặp truyền thống?
**Đ:** Sử dụng Luồng khi hoạt động là một quy trình rõ ràng (lọc, ánh xạ, thu gọn) — chúng thể hiện ý định tốt hơn và dễ dàng song song hóa với`.parallelStream()`. Sử dụng vòng lặp truyền thống cho các lần lặp đơn giản, khi bạn cần sửa đổi trạng thái bên ngoài, khi hiệu suất là quan trọng (luồng có chi phí chung) hoặc khi logic liên quan đến luồng điều khiển phức tạp (ngắt, tiếp tục, trả về nhiều lần). Tránh các luồng cho các thao tác`for-each`đơn giản.
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

### Q4: Bản ghi, lớp niêm phong và khớp mẫu trong Java hiện đại là gì?
**A:** Bản ghi (Java 16) là các vật mang dữ liệu bất biến — chúng tự động tạo các hàm tạo, getter,`equals`,`hashCode`và`toString`. Các lớp kín (Java 17) hạn chế những lớp nào có thể mở rộng chúng — hữu ích cho việc lập mô hình phân cấp kiểu hữu hạn. So khớp mẫu (Java 21) cho phép các biểu thức`switch`phá hủy các loại, bản ghi và giá trị - thay thế các chuỗi`instanceof`dài dòng.
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

### Câu hỏi 5: Làm cách nào để xử lý các ngoại lệ được kiểm tra và không được kiểm tra đúng cách?
**A:** Các ngoại lệ đã chọn (`IOException`,`SQLException`) phải được khai báo trong`throws`hoặc bị bắt — chúng thể hiện các điều kiện có thể phục hồi mà người gọi nên biết. Các ngoại lệ không được kiểm tra (các lớp con`RuntimeException`như `NullPointerException`, `IllegalArgumentException`) thể hiện các lỗi lập trình. Cách thực hành tốt nhất: sử dụng các ngoại lệ đã kiểm tra một cách tiết kiệm (chúng tạo ra khớp nối), ưu tiên`Optional`cho sự vắng mặt dự kiến ​​và bao bọc các ngoại lệ đã kiểm tra trong các ngoại lệ không được kiểm tra khi vượt qua ranh giới API.
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

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Xây dựng quy trình sản xuất-người tiêu dùng an toàn theo luồng
**Báo cáo vấn đề:** Thiết kế quy trình sản xuất-người tiêu dùng trong Java trong đó nhiều nhà sản xuất tạo ra các mục công việc, nhiều người tiêu dùng xử lý chúng đồng thời và hệ thống hỗ trợ tắt máy nhẹ nhàng bằng cách xả các mục còn lại.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng ta cần: (1) một hàng đợi có giới hạn để đệm các mục công việc giữa nhà sản xuất và người tiêu dùng, (2) nhiều luồng nhà sản xuất thêm các mục, (3) nhiều mục xử lý các luồng tiêu dùng, (4) cơ chế báo hiệu tắt và tiêu hủy các mục còn lại.`BlockingQueue`của Java được xây dựng có mục đích cho việc này.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng`ArrayBlockingQueue`(có giới hạn) để ngăn chặn việc tăng trưởng bộ nhớ không giới hạn.
- Sử dụng mẫu thuốc độc để báo hiệu tắt máy.
- Sử dụng`ExecutorService`để quản lý nhóm luồng.
- Sử dụng`CountDownLatch`để đợi tất cả các thiết bị tiêu thụ thoát nước xong.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Hàng đợi bị chặn ngăn chặn OOM:`ArrayBlockingQueue(1000)`giới hạn bộ nhớ.
- Mẫu thuốc độc: mỗi người tiêu dùng sẽ thoát ra sạch sẽ sau khi nhận được viên thuốc của mình.
-`poll(1, SECONDS)`có thời gian chờ ngăn người tiêu dùng chặn vĩnh viễn nếu nhà sản xuất chậm.
- Sản xuất: sử dụng`LinkedBlockingQueue`cho đường ống không giới hạn hoặc`Disruptor`(LMAX) cho đường ống có độ trễ cực thấp.
### Vấn đề 2: Triển khai Trình xác thực dựa trên chú thích tùy chỉnh
**Báo cáo vấn đề:** Tạo khung xác thực bằng cách sử dụng chú thích tùy chỉnh. Người dùng chú thích các trường có`@NotNull`,`@Min(0)`,`@Max(100)`,`@Size(min=1, max=50)`và gọi`Validator.validate(obj)`để nhận danh sách các vi phạm.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần: (1) chú thích tùy chỉnh với các tham số, (2) trình xác thực dựa trên phản chiếu đọc chú thích trong thời gian chạy, (3) đối tượng kết quả chứa tất cả các lỗi xác thực. Điều này thể hiện khả năng xử lý và phản chiếu chú thích của Java.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Xác định chú thích bằng`@Retention(RUNTIME)`và `@Target(FIELD)`.
- Sử dụng`Class.getDeclaredFields()`để lặp lại các trường.
- Sử dụng`Field.getAnnotation()`để đọc các giá trị chú thích.
- So sánh các giá trị trường với các ràng buộc chú thích.
- Thu thập các vi phạm vào danh sách.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Chi phí phản ánh: được chấp nhận để xác thực (được gọi một lần cho mỗi yêu cầu). Đối với các đường dẫn nóng, tra cứu trường bộ nhớ đệm hoặc sử dụng xử lý chú thích tại thời điểm biên dịch (như Trình xác thực Hibernate).
- Khả năng mở rộng: thêm chú thích mới bằng cách tạo chú thích + khối xử lý trong`validate()`.
- Sản xuất: sử dụng`jakarta.validation`(Xác thực Bean 3.0) — nó thực hiện tất cả những điều này và hơn thế nữa, với quá trình xử lý thời gian biên dịch thông qua bộ xử lý chú thích.
### Vấn đề 3: Xây dựng ứng dụng khách HTTP có tốc độ giới hạn bằng Retry
**Báo cáo sự cố:** Tạo trình bao bọc máy khách HTTP tự động thử lại các yêu cầu không thành công với độ trễ theo cấp số nhân, tôn trọng giới hạn tốc độ và hỗ trợ ngắt mạch (ngừng gọi dịch vụ bị lỗi).
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần: (1) thử lại logic với độ trễ theo cấp số nhân và jitter, (2) giới hạn tốc độ để tránh làm quá tải dịch vụ mục tiêu, (3) kiểu ngắt mạch — sau N lần thất bại liên tiếp, hãy ngừng gọi dịch vụ trong một khoảng thời gian hồi chiêu. Đây là ba mối quan tâm tổng hợp.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng`java.net.http.HttpClient`(Java 11+) làm máy khách cơ sở.
- Triển khai thử lại dưới dạng trình bao bọc với`Thread.sleep`để chờ đợi.
- Sử dụng`Semaphore`để giới hạn tốc độ (hoặc`java.time`cho nhóm mã thông báo).
- Triển khai bộ ngắt mạch dưới dạng máy trạng thái: ĐÓNG → MỞ → HALF_OPEN.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Phản hồi theo cấp số nhân với jitter ngăn chặn tiếng sét bầy đàn (tất cả các lần thử lại đánh cùng một lúc).
- Bộ ngắt mạch: sau khi`failureThreshold`bị lỗi liên tiếp, mạch sẽ mở cho`cooldownMs`— không có yêu cầu nào được gửi, bảo vệ dịch vụ bị lỗi.
- Bộ giới hạn tốc độ:`Semaphore`với thông lượng giới hạn bổ sung định kỳ.
- Sản xuất: sử dụng`resilience4j`— nó cung cấp cả ba mẫu (thử lại, giới hạn tốc độ, ngắt mạch) với cách triển khai, số liệu và tích hợp Spring Boot phù hợp.
---

## Bản tóm tắt
Java là một trong những ngôn ngữ lập trình quan trọng nhất từng được tạo ra. Nó điều hành các hệ thống ngân hàng, điện thoại Android, đường ống dữ liệu lớn và chương trình phụ trợ doanh nghiệp trên thế giới. Java hiện đại (21+) là một ngôn ngữ rất khác so với Java 8 - nó ngắn gọn hơn, biểu cảm hơn và ngày càng cạnh tranh với các ngôn ngữ mới hơn. Hệ sinh thái JVM (Kotlin, Scala, Clojure) mở rộng phạm vi hoạt động hơn nữa. Để phát triển doanh nghiệp, Java vẫn là sự lựa chọn an toàn và mạnh mẽ.