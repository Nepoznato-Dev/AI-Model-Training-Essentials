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
| **Sử dụng bộ nhớ** | Chi phí chung của JVM có nghĩa là bộ nhớ cơ sở cao hơn | Điều chỉnh cờ JVM; sử dụng hình ảnh gốc GraalVM cho các triển khai nhỏ |
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
| Java 11 | 2018 | **LTS** — API ứng dụng khách HTTP,`var`cho các biến cục bộ, trình khởi chạy nguồn một tệp |
| Java 17 | 2021 | **LTS** — Các lớp kín, khớp mẫu cho`instanceof`, bản ghi, khối văn bản |
| Java 21 | 2023 | **LTS** — **Chủ đề ảo** (Project Loom), khớp mẫu cho`switch`, mẫu ghi |
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

## Bản tóm tắt
Java là một trong những ngôn ngữ lập trình quan trọng nhất từng được tạo ra. Nó điều hành các hệ thống ngân hàng, điện thoại Android, đường ống dữ liệu lớn và chương trình phụ trợ doanh nghiệp trên thế giới. Java hiện đại (21+) là một ngôn ngữ rất khác so với Java 8 - nó ngắn gọn hơn, biểu cảm hơn và ngày càng cạnh tranh với các ngôn ngữ mới hơn. Hệ sinh thái JVM (Kotlin, Scala, Clojure) mở rộng phạm vi hoạt động hơn nữa. Để phát triển doanh nghiệp, Java vẫn là sự lựa chọn an toàn và mạnh mẽ.