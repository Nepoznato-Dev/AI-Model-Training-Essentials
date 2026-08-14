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
#جاوا
جاوا یک زبان برنامه نویسی شی گرا و تایپ ایستا است که توسط جیمز گاسلینگ در Sun Microsystems ایجاد شد و در سال 1995 منتشر شد. فلسفه طراحی آن - "یک بار بنویس، هر کجا اجرا شود" (WORA) - از طریق ماشین مجازی جاوا (JVM) به دست می آید، که به کد جاوا کامپایل شده اجازه می دهد تا بر روی هر پلتفرم پیاده سازی JVM اجرا شود. جاوا یکی از پرکاربردترین زبان های برنامه نویسی در تاریخ است که به پشتوانه های سازمانی، برنامه های اندروید، سیستم های کلان داده و خدمات مالی نیرو می دهد.
با وجود اینکه جاوا نزدیک به 30 سال سن دارد، همچنان به تکامل خود ادامه می دهد. جاوای مدرن (نسخه‌های 17+) شامل رکوردها، کلاس‌های مهر و موم شده، تطبیق الگو، رشته‌های مجازی و یک اکوسیستم در حال رشد است که با زبان‌های جدیدتر رقابت می‌کند.
---

## چرا جاوا مهم است
- **استاندارد سازمانی**: ستون فقرات فورچون 500 باطن - بانکداری، بیمه، تجارت الکترونیک، مراقبت های بهداشتی.
- **توسعه اندروید**: زبان اصلی اندروید (در کنار Kotlin).
- **اکوسیستم کلان داده**: Apache Hadoop، Spark، Kafka، Elasticsearch - همه در جاوا یا اسکالا (که در JVM اجرا می شود) نوشته شده اند.
- **اکوسیستم عظیم**: بیش از 500000 کتابخانه در Maven Central. ابزار بالغ برای هر نیاز.
- **عملکرد**: کامپایلر JIT JVM کدهای ماشینی بسیار بهینه شده را در زمان اجرا تولید می کند که اغلب با C++ برای برنامه های طولانی مدت مطابقت دارد.
- **سازگاری با عقب**: کد نوشته شده برای جاوا 1.0 (1996) هنوز روی JVM های مدرن اجرا می شود.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **پرحرفی** | نسبت به Python، Kotlin یا Go | به دیگ بخار بیشتری نیاز دارد استفاده از Lombok، رکوردها (جاوا 16+)، و IDEهای مدرن |
| **استفاده از حافظه** | سربار JVM یعنی حافظه پایه بالاتر | تنظیم پرچم های JVM. استفاده از تصاویر بومی GraalVM برای استقرارهای کوچک |
| **زمان راه اندازی** | گرم کردن JVM می تواند برای فرآیندهای کوتاه مدت کند باشد | GraalVM native-image، یا از C/Go برای ابزارهای CLI |
| **استثناهای بررسی شده** | مدیریت استثناهایی که ممکن است قابل بازیابی نباشند را مجبور می کند | از استثناهای بدون علامت یا الگوی`Optional`| استفاده کنید
| **بدون انواع ارزش** | همه چیز یک شی است (تا پروژه والهالا) | از مجموعه‌های تخصصی بدوی (Eclipse Collections، Trove) استفاده کنید
---

## اصول نحو
### ساختار اساسی
جاوا مبتنی بر کلاس است - همه چیز در یک کلاس زندگی می کند. نام فایل باید با نام کلاس عمومی مطابقت داشته باشد.
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

### برنامه نویسی شی گرا
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

### رکوردها (جاوا 16+) - کلاس های داده مختصر
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

### مجموعه ها و جریان ها
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

### رسیدگی به استثنا
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

## نحو و الگوهای پیشرفته
### ژنریک
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

### کلاس های مهر و موم شده و تطبیق الگو (جاوا 17+)
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

### حاشیه نویسی
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

### رابط های کاربردی و لامبدا
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

## همزمانی و موازی
### موضوعات مجازی (جاوا 21+)
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

### نخ و همگام سازی سنتی
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه (Maven)
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

### خط لوله CI/CD
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

## تست
### JUnit 5 با Mockito
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

## قابلیت همکاری
### JNI (رابط بومی جاوا)
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

### API عملکرد و حافظه خارجی (جاوا 22+)
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

## الگوهای طراحی
### الگوی سازنده
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

### الگوی مشاهده گر
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### تکنیک های بهینه سازی
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

## استقرار
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

## اکوسیستم
### ابزارهای ساخت
| ابزار | هدف | یادداشت ها |
|------|---------|-------|
| **ماون** | اتوماسیون ساخت + مدیریت وابستگی | مبتنی بر XML (`pom.xml`)؛ استاندارد صنعتی برای شرکت |
| **گرادل** | اتوماسیون ساخت + مدیریت وابستگی | Groovy/Kotlin DSL; سریعتر برای پروژه های بزرگ؛ استفاده شده توسط اندروید |
### چارچوب
| چارچوب | دامنه | توضیحات |
|-----------|--------|-------------|
| **چکمه بهاره** | وب / شرکت | چارچوب غالب جاوا - REST API ها، میکروسرویس ها، امنیت، دسترسی به داده |
| **جاکارتا EE** | شرکت | جانشین Java EE. APIهای استاندارد سازمانی |
| **خواب زمستانی** | ORM | نگاشت شی رابطه ای; اجرای استاندارد JPA |
| **Micronaut / Quarkus** | Cloud-Native | راه اندازی سریع، حافظه کم — طراحی شده برای بدون سرور و کانتینر |
### تست
| ابزار | هدف |
|------|---------|
| **واحد 5** | چارچوب تست واحد |
| **موکیتو** | چارچوب تمسخر آمیز |
| **AssertJ** | ادعاهای روان |
| **تست ظروف** | تست های یکپارچه سازی با پایگاه های داده واقعی در Docker |
---

## اکوسیستم JVM
| زبان JVM | ارتباط با جاوا |
|-------------|---------------------|
| **کاتلین** | جایگزین مدرن برای جاوا؛ زبان اندروید ترجیحی گوگل؛ 100% سازگار با جاوا |
| **اسکالا** | عملکردی + OOP هیبرید. قدرت های آپاچی اسپارک |
| **کلاژور** | گویش Lisp در JVM. برنامه نویسی تابعی |
| **گرووی** | اسکریپت نویسی پویا برای JVM. مورد استفاده در فایل های ساخت Gradle |
همه اینها می توانند از کتابخانه های جاوا استفاده کنند و جاوا می تواند از کتابخانه های آنها استفاده کند. JVM پلتفرم است، نه فقط جاوا.
---

## نسخه های جاوا
| نسخه | سال | ویژگی های کلیدی |
|---------|------|-------------|
| جاوا 8 | 2014 | **LTS** - Lambdas، Stream API، اختیاری، روش های پیش فرض. هنوز به طور گسترده استفاده می شود. |
| جاوا 11 | 2018 | **LTS** — HTTP Client API،`var`برای متغیرهای محلی، راه‌انداز منبع تک فایل |
| جاوا 17 | 2021 | **LTS** — کلاس های مهر و موم شده، تطبیق الگو برای `instanceof`، رکوردها، بلوک های متنی |
| جاوا 21 | 2023 | **LTS** — **رشته های مجازی** (Project Loom)، تطبیق الگو برای `switch`، الگوهای ضبط |
| جاوا 25 | 2025 | **LTS** — الگوهای رشته، تطبیق بیشتر الگو، API تابع خارجی |
نسخه های **LTS ** (پشتیبانی طولانی مدت) سال ها به روز رسانی دریافت می کنند. برای تولید، از جاوا 21 یا بالاتر استفاده کنید.
---

## چه زمانی از جاوا استفاده کنیم
| سناریو | چرا جاوا | جایگزین بهتر |
|----------|---------|-------------------|
| پشتیبان های سازمانی | اکوسیستم عظیم، چکمه بهار، اثبات شده در مقیاس | کاتلین (همان JVM، کمتر پرمخاطب) |
| توسعه اندروید | تاسیس، پایگاه کد بزرگ | Kotlin (انتخاب ترجیحی گوگل) |
| داده های بزرگ (هدوپ، اسپارک، کافکا) | اکوسیستم بر روی Java/Scala | ساخته شده است پایتون برای علم داده |
| سیستم های مالی | عملکرد + قابلیت اطمینان + ابزار کامل | -- |
| میکروسرویس | Spring Boot + فریمورک های ابری بومی | به سراغ خدمات ساده تر بروید |
| اسکریپت های ساده | مراسم خیلی زیاد | پایتون، شل |
| ابزارهای CLI | راه اندازی آهسته | برو زنگ بزن |
---

## پرسش و پاسخ مصنوعی
### Q1: تفاوت`==`و`.equals()`در جاوا چیست؟
**A:**`==`مراجع شی (هویت) را با هم مقایسه می کند - بررسی می کند که آیا دو متغیر به یک شی در حافظه اشاره می کنند یا خیر. `.equals()`محتوای شی را مقایسه می کند (برابری ارزش). برای موارد اولیه (`int`، `double`)،`==`مقادیر را مستقیماً مقایسه می کند. برای اشیا (از جمله `String`)، همیشه از`.equals()`برای مقایسه محتوا استفاده کنید. تنها استثنا مقایسه با`null`است که`==`درست است.
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

### Q2: زباله جمع کن JVM چگونه کار می کند، و از کدام یک باید استفاده کنم؟
**A:** GC به طور خودکار حافظه را از اشیایی که دیگر قابل دسترسی نیستند بازیابی می کند. JVM های مدرن (21+) چندین مجموعه ارائه می دهند: G1 (پیش فرض، متعادل)، ZGC (زمان مکث بسیار کم، <1 میلی ثانیه)، و Shenandoah (مکث کم، OpenJDK). برای اکثر برنامه ها، G1 پیش فرض مناسب است. برای سرویس‌های حساس به تأخیر، از ZGC (`-XX:+UseZGC`) استفاده کنید. برای پردازش دسته ای توان گرا، از GC موازی (`-XX:+UseParallelGC`) استفاده کنید.
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### Q3: چه زمانی باید از`Stream API`در مقابل حلقه های سنتی استفاده کنم؟
**A:** از Stream ها زمانی استفاده کنید که عملیات یک خط لوله واضح است (فیلتر، نقشه، کاهش) - آنها هدف را بهتر بیان می کنند و به راحتی با`.parallelStream()`موازی می شوند. از حلقه‌های سنتی برای تکرارهای ساده استفاده کنید، زمانی که نیاز به تغییر حالت خارجی دارید، زمانی که عملکرد بحرانی است (جریان‌ها دارای سربار هستند)، یا زمانی که منطق شامل جریان کنترل پیچیده (شکستن، ادامه دادن، بازگشت‌های متعدد) است. از پخش جریانی برای عملیات ساده`for-each`اجتناب کنید.
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

### Q4: رکوردها، کلاس های مهر و موم شده و تطبیق الگو در جاوا مدرن چیست؟
**A:** رکوردها (جاوا 16) حامل های داده غیرقابل تغییر هستند - سازنده ها، گیرندگان، `equals`،`hashCode`و`toString`را به طور خودکار تولید می کنند. کلاس های مهر و موم شده (جاوا 17) کلاس هایی را که می توانند آنها را گسترش دهند محدود می کند - برای مدل سازی سلسله مراتب نوع محدود مفید است. تطبیق الگو (جاوا 21) به عبارات`switch`اجازه می دهد تا انواع، رکوردها و مقادیر را تخریب کنند - جایگزین زنجیره های پرمخاطب `instanceof`.
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

### Q5: چگونه استثناهای علامت زده شده در مقابل تیک نشده را به درستی مدیریت کنم؟
**A:** استثناهای علامت زده شده (`IOException`، `SQLException`) باید در`throws`اعلان شوند یا شناسایی شوند - آنها شرایط قابل بازیابی را نشان می دهند که تماس گیرنده باید از آنها مطلع باشد. استثناهای علامت نخورده (زیر کلاس های`RuntimeException`مانند `NullPointerException`، `IllegalArgumentException`) اشکالات برنامه نویسی را نشان می دهند. بهترین روش: از استثناهای علامت‌گذاری شده به مقدار کم استفاده کنید (آنها جفت ایجاد می‌کنند)،`Optional`را برای غیبت مورد انتظار ترجیح می‌دهند، و هنگام عبور از مرزهای API، استثناهای علامت‌خورده را در موارد علامت‌نشده قرار دهید.
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

## حل مسئله زنجیره ای از فکر
### مشکل 1: ایجاد یک خط لوله ایمن تولیدکننده-مصرف کننده
**بیانیه مشکل:** یک خط لوله تولیدکننده-مصرف کننده در جاوا طراحی کنید که در آن چندین تولیدکننده آیتم های کاری را تولید می کنند، چندین مصرف کننده همزمان آنها را پردازش می کنند، و سیستم از خاموش شدن دلپذیر با تخلیه اقلام باقی مانده پشتیبانی می کند.
** مرحله 1 - مشکل را درک کنید:**
ما به این موارد نیاز داریم: (1) یک صف محدود برای بافر اقلام کاری بین تولیدکنندگان و مصرف‌کنندگان، (2) رشته‌های تولیدکننده متعددی که آیتم‌ها را اضافه می‌کنند، (3) موضوعات پردازش موضوعات متعدد مصرف‌کننده، (4) مکانیزمی برای سیگنال خاموش شدن و تخلیه اقلام باقی‌مانده.`BlockingQueue`جاوا برای این منظور ساخته شده است.
** مرحله 2 - شناسایی رویکرد: **
- از`ArrayBlockingQueue`(محدود) برای جلوگیری از رشد حافظه نامحدود استفاده کنید.
- از الگوی قرص سمی برای سیگنال دهی خاموش استفاده کنید.
- از`ExecutorService`برای مدیریت Thread Pool استفاده کنید.
- از`CountDownLatch`برای صبر کردن تا پایان تخلیه تمام مصرف کنندگان استفاده کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- صف محدود از OOM جلوگیری می کند:`ArrayBlockingQueue(1000)`حافظه را محدود می کند.
- الگوی قرص سمی: هر مصرف کننده پس از دریافت قرص خود به طور تمیز خارج می شود.
-`poll(1, SECONDS)`با مهلت زمانی مانع از مسدود شدن مصرف کنندگان برای همیشه در صورت کندی تولیدکنندگان می شود.
- تولید: از`LinkedBlockingQueue`برای خطوط لوله نامحدود یا`Disruptor`(LMAX) برای خطوط لوله با تاخیر بسیار کم استفاده کنید.
### مشکل 2: یک اعتبارسنجی مبتنی بر حاشیه نویسی سفارشی را پیاده سازی کنید
**بیانیه مشکل:** یک چارچوب اعتبار سنجی با استفاده از حاشیه نویسی های سفارشی ایجاد کنید. کاربران فیلدها را با `@NotNull`، `@Min(0)`، `@Max(100)`،`@Size(min=1, max=50)`حاشیه نویسی می کنند و برای دریافت لیستی از تخلفات، با`Validator.validate(obj)`تماس می گیرند.
** مرحله 1 - مشکل را درک کنید:**
ما به این موارد نیاز داریم: (1) حاشیه نویسی سفارشی با پارامترها، (2) اعتبارسنجی مبتنی بر بازتاب که حاشیه نویسی ها را در زمان اجرا می خواند، (3) یک شی نتیجه حاوی تمام خطاهای اعتبارسنجی. این قابلیت پردازش حاشیه نویسی و بازتاب جاوا را نشان می دهد.
** مرحله 2 - شناسایی رویکرد: **
- حاشیه نویسی را با`@Retention(RUNTIME)`و`@Target(FIELD)`تعریف کنید.
- از`Class.getDeclaredFields()`برای تکرار فیلدها استفاده کنید.
- از`Field.getAnnotation()`برای خواندن مقادیر حاشیه نویسی استفاده کنید.
- مقادیر فیلد را با محدودیت های حاشیه نویسی مقایسه کنید.
- تخلفات را در یک لیست جمع آوری کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- سربار انعکاس: قابل قبول برای اعتبارسنجی (یک بار در هر درخواست فراخوانی می شود). برای مسیرهای داغ، جستجو در زمینه حافظه پنهان یا از پردازش حاشیه نویسی در زمان کامپایل (مانند اعتبارسنجی Hibernate) استفاده کنید.
- توسعه پذیری: با ایجاد حاشیه نویسی + یک بلوک کنترل کننده در `validate()`، حاشیه نویسی های جدید اضافه کنید.
- تولید: از`jakarta.validation`(Bean Validation 3.0) استفاده کنید - همه اینها و موارد دیگر را با پردازش زمان کامپایل از طریق پردازنده های حاشیه نویسی انجام می دهد.
### مشکل 3: با تلاش مجدد، یک کلاینت HTTP با نرخ محدود بسازید
**بیانیه مشکل:** یک پوشه کلاینت HTTP ایجاد کنید که به طور خودکار درخواست های ناموفق را با عقب نشینی نمایی مجدداً تکرار می کند، به محدودیت های نرخ احترام می گذارد و از قطع شدن مدار پشتیبانی می کند (تماس با سرویس ناموفق را متوقف کنید).
** مرحله 1 - مشکل را درک کنید:**
ما به این موارد نیاز داریم: (1) منطق را دوباره با عقب نشینی و لرزش نمایی، (2) محدود کردن نرخ برای جلوگیری از غلبه بر سرویس هدف، (3) الگوی قطع کننده مدار - پس از N خرابی متوالی، تماس با سرویس را برای یک دوره خنک شدن متوقف کنید. اینها سه نگرانی قابل ترکیب هستند.
** مرحله 2 - شناسایی رویکرد: **
- از`java.net.http.HttpClient`(جاوا 11+) به عنوان مشتری پایه استفاده کنید.
- اجرای مجدد تلاش به عنوان یک لفاف با`Thread.sleep`برای عقب نشینی.
- از`Semaphore`برای محدود کردن نرخ (یا`java.time`برای سطل توکن) استفاده کنید.
- اجرای قطع کننده مدار به عنوان یک ماشین حالت: CLOSED → OPEN → HALF_OPEN.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- عقب نشینی نمایی با جیتر از رعد و برق گله جلوگیری می کند (همه تلاش های مجدد همزمان ضربه می زنند).
- قطع کننده مدار: پس از خرابی های متوالی `failureThreshold`، مدار برای`cooldownMs`باز می شود - هیچ درخواستی ارسال نمی شود و از سرویس خراب محافظت می کند.
- محدود کننده نرخ:`Semaphore`با توان عملیاتی درپوش های تکمیل دوره ای.
- تولید: از`resilience4j`استفاده کنید - هر سه الگو (تلاش مجدد، محدود کننده نرخ، قطع کننده مدار) را با پیاده سازی مناسب، معیارها و ادغام Spring Boot فراهم می کند.
---

## خلاصه
جاوا یکی از مهم ترین زبان های برنامه نویسی است که تاکنون ساخته شده است. این سیستم‌های بانکی جهان، تلفن‌های اندرویدی، خطوط لوله داده‌های بزرگ و پشتیبان‌های سازمانی را اجرا می‌کند. جاوای مدرن (21+) زبانی بسیار متفاوت از جاوا 8 است - مختصرتر، رساتر و به طور فزاینده ای رقابتی با زبان های جدیدتر است. اکوسیستم JVM (Kotlin، Scala، Clojure) دامنه خود را بیشتر گسترش می دهد. برای توسعه سازمانی، جاوا یک انتخاب امن و قدرتمند باقی می ماند.