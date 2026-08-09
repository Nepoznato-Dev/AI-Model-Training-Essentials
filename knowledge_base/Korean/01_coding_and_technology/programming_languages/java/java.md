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
# 자바
Java는 Sun Microsystems의 James Gosling이 만들어 1995년에 출시한 정적으로 유형이 지정된 객체 지향 프로그래밍 언어입니다. "한 번 작성하면 어디서나 실행"(WORA)이라는 설계 철학은 JVM(Java Virtual Machine)이 구현된 모든 플랫폼에서 컴파일된 Java 코드를 실행할 수 있도록 하는 JVM(Java Virtual Machine)을 통해 구현됩니다. Java는 역사상 가장 널리 사용되는 프로그래밍 언어 중 하나로 엔터프라이즈 백엔드, Android 앱, 빅 데이터 시스템 및 금융 서비스를 지원합니다.
거의 30년이 지났음에도 불구하고 Java는 계속 발전하고 있습니다. 최신 Java(버전 17+)에는 레코드, 밀봉 클래스, 패턴 일치, 가상 스레드 및 최신 언어와 경쟁하는 성장하는 생태계가 포함되어 있습니다.
---

## 자바가 중요한 이유
- **엔터프라이즈 표준**: 금융, 보험, 전자상거래, 의료 등 Fortune 500대 백엔드의 백본입니다.
- **Android 개발**: Android(Kotlin과 함께)의 기본 언어입니다.
- **빅 데이터 생태계**: Apache Hadoop, Spark, Kafka, Elasticsearch — 모두 Java 또는 Scala(JVM에서 실행)로 작성되었습니다.
- **대규모 생태계**: Maven Central에 500,000개 이상의 라이브러리가 있습니다. 모든 요구에 맞는 성숙한 도구.
- **성능**: JVM의 JIT 컴파일러는 런타임에 고도로 최적화된 기계어 코드를 생성하며, 종종 장기 실행 애플리케이션에 대해 C++와 일치합니다.
- **역호환성**: Java 1.0(1996)용으로 작성된 코드는 최신 JVM에서 계속 실행됩니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **자세한 내용** | Python, Kotlin 또는 Go보다 더 많은 상용구가 필요함 | Lombok, 레코드(Java 16+) 및 최신 IDE 사용 |
| **메모리 사용량** | JVM 오버헤드는 더 높은 기본 메모리를 의미합니다 | JVM 플래그를 조정합니다. 소규모 배포에 GraalVM 기본 이미지 사용 |
| **시작 시간** | 단기 프로세스의 경우 JVM 준비가 느려질 수 있음 | GraalVM 네이티브 이미지 또는 CLI 도구용 C/Go 사용 |
| **확인된 예외** | 복구할 수 없는 예외를 강제로 처리 | 확인되지 않은 예외 또는`Optional`패턴 사용 |
| **값 유형 없음** | 모든 것이 객체입니다(Valhalla 프로젝트까지) | 기본적으로 특화된 컬렉션 사용(Eclipse Collections, Trove) |
---

## 구문 기본 사항
### 기본 구조
Java는 클래스 기반이므로 모든 것이 클래스 내에 있습니다. 파일 이름은 공개 클래스 이름과 일치해야 합니다.
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

### 객체 지향 프로그래밍
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

### 레코드(Java 16+) — 간결한 데이터 클래스
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

### 컬렉션 및 스트림
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

### 예외 처리
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

## 고급 구문 및 패턴
### 제네릭
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

### 봉인된 클래스 및 패턴 일치(Java 17+)
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

### 주석
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

### 기능적 인터페이스 및 람다
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

## 동시성 및 병렬성
### 가상 스레드(Java 21+)
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

### 기존 스레딩 및 동기화
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 구조(Maven)
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

### pom.xml (메이븐)
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

### build.gradle.kts (그레이들)
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

### CI/CD 파이프라인
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

## 테스트
### Mockito를 사용한 JUnit 5
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

## 상호 운용성
### JNI(자바 네이티브 인터페이스)
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

### 외부 함수 및 메모리 API(Java 22+)
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

## 디자인 패턴
### 빌더 패턴
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

### 관찰자 패턴
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

## 성능 및 최적화
### 프로파일링 도구
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### 최적화 기술
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

## 배포
### 도커파일
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

## 생태계
### 빌드 도구
| 도구 | 목적 | 메모 |
|------|---------|-------|
| **메이븐** | 빌드 자동화 + 종속성 관리 | XML 기반(`pom.xml`); 기업을 위한 산업 표준 |
| **그라들** | 빌드 자동화 + 종속성 관리 | 그루비/코틀린 DSL; 대규모 프로젝트의 경우 더 빠릅니다. Android에서 사용 |
### 프레임워크
| 프레임워크 | 도메인 | 설명 |
|------------|---------|-------------|
| **스프링 부트** | 웹/기업 | 주요 Java 프레임워크 - REST API, 마이크로서비스, 보안, 데이터 액세스 |
| **자카르타 EE** | 기업 | Java EE의 후속 제품입니다. 표준화된 엔터프라이즈 API |
| **최대 절전 모드** | ORM | 객체 관계형 매핑; 표준 JPA 구현 |
| **마이크로넛/쿼커스** | 클라우드 네이티브 | 빠른 시작, 낮은 메모리 — 서버리스 및 컨테이너용으로 설계됨 |
### 테스트
| 도구 | 목적 |
|------|---------|
| **JUnit 5** | 단위 테스트 프레임워크 |
| **모키토** | 모의 프레임워크 |
| **주장J** ​​| 유창한 주장 |
| **테스트 컨테이너** | Docker에서 실제 데이터베이스와의 통합 테스트 |
---

## JVM 생태계
| JVM 언어 | 자바와의 관계 |
|-------------|---------|
| **코틀린** | Java에 대한 현대적인 대안; Google이 선호하는 Android 언어입니다. 100% Java 호환 |
| **스칼라** | 기능적 + OOP 하이브리드; Apache Spark 지원 |
| **클로저** | JVM의 Lisp 방언; 함수형 프로그래밍 |
| **그루비** | JVM을 위한 동적 스크립팅 Gradle 빌드 파일에 사용됨 |
이들 모두는 Java 라이브러리를 사용할 수 있으며 Java는 해당 라이브러리를 사용할 수 있습니다. JVM은 Java가 아닌 플랫폼입니다.
---

## 자바 버전
| 버전 | 연도 | 주요 기능 |
|---------|------|-------------|
| 자바 8 | 2014 | **LTS** — 람다, 스트림 API, 선택 사항, 기본 방법. 아직도 널리 사용되고 있습니다. |
| 자바 11 | 2018 | **LTS** — HTTP 클라이언트 API, 로컬 변수용 `var`, 단일 파일 소스 실행기 |
| 자바 17 | 2021 | **LTS** — 봉인된 클래스, `instanceof`에 대한 패턴 일치, 레코드, 텍스트 블록 |
| 자바 21 | 2023 | **LTS** — **가상 스레드**(Project Loom), `switch`에 대한 패턴 일치, 패턴 기록 |
| 자바 25 | 2025년 | **LTS** — 문자열 템플릿, 추가 패턴 일치, 외부 함수 API |
**LTS**(장기 지원) 버전은 수년 동안 업데이트를 받습니다. 프로덕션에는 Java 21 이상을 사용하세요.
---

## 자바를 사용해야 하는 경우
| 시나리오 | 왜 자바인가 | 더 나은 대안 |
|----------|---------|------|
| 엔터프라이즈 백엔드 | 대규모 생태계, Spring Boot, 규모로 입증됨 | Kotlin(동일한 JVM, 덜 장황함) |
| 안드로이드 개발 | 확립된 거대한 코드베이스 | Kotlin(Google이 선호하는 선택) |
| 빅데이터(Hadoop, Spark, Kafka) | 생태계는 Java/Scala | 데이터 과학 측면을 위한 Python |
| 금융 시스템 | 성능 + 안정성 + 성숙한 도구 | -- |
| 마이크로서비스 | Spring Boot + 클라우드 네이티브 프레임워크 | 더 간단한 서비스를 만나보세요 |
| 간단한 스크립트 | 너무 많은 행사 | 파이썬, 쉘 |
| CLI 도구 | 느린 시작 | 가서 러스트 |
---

## 요약
Java는 지금까지 만들어진 가장 중요한 프로그래밍 언어 중 하나입니다. 전 세계의 뱅킹 시스템, Android 휴대폰, 빅 데이터 파이프라인 및 엔터프라이즈 백엔드를 실행합니다. 최신 Java(21+)는 Java 8과 매우 다른 언어입니다. 즉, 더 간결하고 표현력이 뛰어나며 최신 언어와의 경쟁이 점점 더 치열해지고 있습니다. JVM 생태계(Kotlin, Scala, Clojure)는 그 범위를 더욱 확장합니다. 엔터프라이즈 개발의 경우 Java는 여전히 안전하고 강력한 선택입니다.