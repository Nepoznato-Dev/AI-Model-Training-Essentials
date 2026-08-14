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
#جافا
Java هي لغة برمجة موجهة للكائنات مكتوبة بشكل ثابت أنشأها جيمس جوسلينج في Sun Microsystems وتم إصدارها في عام 1995. ويتم تحقيق فلسفة التصميم الخاصة بها - "الكتابة مرة واحدة، والتشغيل في أي مكان" (WORA) - من خلال Java Virtual Machine (JVM)، والتي تسمح بتشغيل تعليمات Java البرمجية المترجمة على أي نظام أساسي يحتوي على تطبيق JVM. تعد Java واحدة من لغات البرمجة الأكثر استخدامًا في التاريخ، حيث تعمل على تشغيل الواجهات الخلفية للمؤسسات وتطبيقات Android وأنظمة البيانات الضخمة والخدمات المالية.
على الرغم من أن عمرها ما يقرب من 30 عامًا، إلا أن Java مستمرة في التطور. تشتمل Java الحديثة (الإصدارات 17+) على سجلات وفئات مختومة ومطابقة الأنماط وخيوط افتراضية ونظام بيئي متنامي يتنافس مع اللغات الأحدث.
---

## لماذا تعتبر جافا مهمة
- **معيار المؤسسة**: العمود الفقري لواجهات Fortune 500 الخلفية - الخدمات المصرفية والتأمين والتجارة الإلكترونية والرعاية الصحية.
- **تطوير Android**: اللغة الأساسية لنظام Android (إلى جانب Kotlin).
- **النظام البيئي للبيانات الضخمة**: Apache Hadoop، وSpark، وKafka، وElasticsearch — كلها مكتوبة بلغة Java أو Scala (التي تعمل على JVM).
- **نظام بيئي ضخم**: أكثر من 500000 مكتبة في Maven Central؛ الأدوات الناضجة لكل حاجة.
- **الأداء**: يقوم برنامج التحويل البرمجي JIT الخاص بـ JVM بإنتاج كود جهاز محسّن للغاية في وقت التشغيل، وغالبًا ما يطابق C++ للتطبيقات طويلة التشغيل.
- **التوافق مع الإصدارات السابقة**: التعليمات البرمجية المكتوبة لـ Java 1.0 (1996) لا تزال تعمل على أجهزة JVM الحديثة.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| **الإسهاب** | يتطلب نموذجًا معياريًا أكثر من Python أو Kotlin أو Go | استخدم Lombok والسجلات (Java 16+) وIDEs الحديثة |
| **استخدام الذاكرة** | الحمل الزائد لـ JVM يعني ذاكرة أساسية أعلى | ضبط أعلام JVM؛ استخدم صور GraalVM الأصلية لعمليات النشر الصغيرة |
| **وقت بدء التشغيل** | يمكن أن يكون إحماء JVM بطيئًا للعمليات قصيرة العمر | صورة GraalVM الأصلية، أو استخدم C/Go لأدوات CLI |
| **الاستثناءات المحددة** | يفرض معالجة الاستثناءات التي قد لا تكون قابلة للاسترداد | استخدم الاستثناءات غير المحددة أو نمط`Optional`|
| **لا توجد أنواع قيمة** | كل شيء كائن (حتى مشروع فالهالا) | استخدم المجموعات البدائية المتخصصة (Eclipse Collections، Trove) |
---

## أساسيات بناء الجملة
### البنية الأساسية
Java تعتمد على الفصل، كل شيء يعيش داخل الفصل. يجب أن يتطابق اسم الملف مع اسم الفئة العامة.
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

### البرمجة الشيئية
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

### السجلات (Java 16+) — فئات بيانات موجزة
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

### المجموعات والجداول
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

### التعامل مع الاستثناءات
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

## بناء الجملة والأنماط المتقدمة
### الأدوية العامة
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

### الفئات المختومة ومطابقة الأنماط (Java 17+)
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

### التعليقات التوضيحية
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

### الواجهات الوظيفية وLambdas
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

## التزامن والتوازي
### المواضيع الافتراضية (جافا 21+)
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

### الخيوط والمزامنة التقليدية
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

## تكوين المشروع ونظام البناء
### هيكل المشروع (مافن)
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

### pom.xml (مافن)
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

### خط أنابيب CI/CD
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

## الاختبار
### JUnit 5 مع Mockito
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

## إمكانية التشغيل البيني
### JNI (واجهة جافا الأصلية)
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

### واجهة برمجة التطبيقات للوظائف الخارجية والذاكرة (Java 22+)
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

## أنماط التصميم
### نمط البناء
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

### نمط المراقب
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

## الأداء والتحسين
### أدوات التنميط
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### تقنيات التحسين
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

## النشر
### ملف دوكر
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

## النظام البيئي
### أدوات البناء
| أداة | الغرض | ملاحظات |
|------|---------|------|
| **مافن** | أتمتة البناء + إدارة التبعية | مستند إلى XML (`pom.xml`)؛ معيار الصناعة للمؤسسات |
| ** جرادل ** | أتمتة البناء + إدارة التبعية | رائع/كوتلين DSL؛ أسرع للمشاريع الكبيرة. يستخدمه أندرويد |
### الأطر
| الإطار | المجال | الوصف |
|-----------|-------|-------------|
| **حذاء الربيع** | الويب / المؤسسة | إطار عمل Java المهيمن — واجهات برمجة تطبيقات REST والخدمات الصغيرة والأمان والوصول إلى البيانات |
| ** جاكرتا إي إي ** | مؤسسة | خليفة Java EE؛ واجهات برمجة التطبيقات الموحدة للمؤسسات |
| ** السبات ** | أو آر إم | رسم الخرائط العلائقية للكائنات؛ تنفيذ JPA القياسي |
| **ميكرونوت/كواركوس** | السحابة الأصلية | بدء تشغيل سريع وذاكرة منخفضة — مصمم للاستخدام بدون خوادم والحاويات |
### الاختبار
| أداة | الغرض |
|------|---------|
| ** الوحدة الخامسة ** | إطار اختبار الوحدة |
| ** موكيتو ** | إطار السخرية |
| **تأكيدJ** | التأكيدات بطلاقة |
| **حاويات الاختبار** | اختبارات التكامل مع قواعد البيانات الحقيقية في Docker |
---

## النظام البيئي JVM
| لغة JVM | العلاقة مع جافا |
|-------------|--------------------|
| **كوتلين** | البديل الحديث لجافا. لغة Android المفضلة لدى Google؛ متوافق مع جافا بنسبة 100% |
| **سكالا** | وظيفية + OOP الهجين. القوى أباتشي سبارك |
| ** كلوجور ** | لهجة Lisp على JVM؛ البرمجة الوظيفية |
| **رائع** | البرمجة النصية الديناميكية لـ JVM؛ المستخدمة في ملفات بناء Gradle |
كل هؤلاء يمكنهم استخدام مكتبات Java، ويمكن لـ Java استخدام مكتباتهم. JVM هو النظام الأساسي، وليس Java فقط.
---

## إصدارات جافا
| النسخة | سنة | الميزات الرئيسية |
|---------|------|-------------|
| جافا 8 | 2014 | **LTS** — Lambdas، Stream API، اختياري، الطرق الافتراضية. لا تزال تستخدم على نطاق واسع. |
| جافا 11 | 2018 | **LTS** — واجهة برمجة تطبيقات عميل HTTP،`var`للمتغيرات المحلية، مشغل مصدر أحادي الملف |
| جافا 17 | 2021 | **LTS** — فئات مختومة، مطابقة الأنماط لـ `instanceof`، والسجلات، وكتل النص |
| جافا 21 | 2023 | **LTS** — **خيوط افتراضية** (Project Loom)، مطابقة الأنماط لـ `switch`، أنماط التسجيل |
| جافا 25 | 2025 | **LTS** — قوالب السلسلة، مزيد من مطابقة الأنماط، واجهة برمجة التطبيقات للوظيفة الأجنبية |
تتلقى إصدارات **LTS** (الدعم طويل الأمد) تحديثات لسنوات عديدة. للإنتاج، استخدم Java 21 أو الأحدث.
---

## متى يجب استخدام جافا
| السيناريو | لماذا جافا | البديل الأفضل |
|----------|--------|------------------|
| الواجهات الخلفية للمؤسسات | نظام بيئي ضخم، Spring Boot، مثبت على نطاق واسع | Kotlin (نفس JVM، أقل تفصيلاً) |
| تطوير أندرويد | تم إنشاء قاعدة تعليمات برمجية ضخمة | Kotlin (خيار Google المفضل) |
| البيانات الضخمة (هادوب، سبارك، كافكا) | النظام البيئي مبني على Java/Scala | بايثون لجانب علوم البيانات |
| الأنظمة المالية | الأداء + الموثوقية + الأدوات الناضجة | -- |
| الخدمات المصغرة | Spring Boot + أطر العمل السحابية الأصلية | اذهب لخدمات أبسط |
| مخطوطات بسيطة | حفل كثير جدًا | بايثون، شل |
| أدوات سطر الأوامر | بدء تشغيل بطيء | اذهب يا صدأ |
---

## أسئلة وأجوبة اصطناعية
### س1: ما الفرق بين`==`و`.equals()` في Java؟
**A:** يقارن`==`مراجع الكائنات (الهوية) - ويتحقق مما إذا كان هناك متغيران يشيران إلى نفس الكائن في الذاكرة.  يقارن`.equals()`محتوى الكائن (مساواة القيمة). بالنسبة للأوليات (`int`,`double`)، يقوم`==`بمقارنة القيم مباشرة. بالنسبة للكائنات (بما في ذلك`String`)، استخدم دائمًا`.equals()`لمقارنة المحتوى. الاستثناء الوحيد هو المقارنة مع `null`، حيث يكون`==`صحيحًا.
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

### السؤال الثاني: كيف يعمل جامع البيانات المهملة JVM، وأي واحد يجب أن أستخدمه؟
**أ:** يقوم GC تلقائيًا باستعادة الذاكرة من الكائنات التي لم يعد من الممكن الوصول إليها. تقدم JVMs الحديثة (21+) العديد من المجمعات: G1 (افتراضي، متوازن)، ZGC (أوقات توقف منخفضة للغاية، <1 مللي ثانية)، وShenandoah (توقف مؤقت منخفض، OpenJDK). بالنسبة لمعظم التطبيقات، يكون G1 الافتراضي مناسبًا. بالنسبة للخدمات الحساسة لزمن الوصول، استخدم ZGC (`-XX:+UseZGC`). لمعالجة الدفعات الموجهة نحو الإنتاجية، استخدم Parallel GC (`-XX:+UseParallelGC`).
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### Q3: متى يجب علي استخدام`Stream API`مقابل الحلقات التقليدية؟
**أ:** استخدم التدفقات عندما تكون العملية عبارة عن خط أنابيب واضح (مرشح، خريطة، تقليل) - فهي تعبر عن النية بشكل أفضل وتتوازي بسهولة مع`.parallelStream()`. استخدم الحلقات التقليدية للتكرارات البسيطة، عندما تحتاج إلى تعديل الحالة الخارجية، عندما يكون الأداء حرجًا (التدفقات لها حمل زائد)، أو عندما يتضمن المنطق تدفق تحكم معقد (فاصل، متابعة، إرجاعات متعددة). تجنب التدفقات لعمليات`for-each`البسيطة.
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

### س 4: ما هي السجلات والفئات المختومة ومطابقة الأنماط في Java الحديثة؟
**أ:** السجلات (Java 16) عبارة عن ناقلات بيانات غير قابلة للتغيير - فهي تُنشئ تلقائيًا مُنشئات وحاصلات و`equals` و`hashCode` و`toString`. تقيد الفئات المختومة (Java 17) الفئات التي يمكنها توسيعها - وهي مفيدة لنمذجة التسلسلات الهرمية للأنواع المحدودة. تسمح مطابقة الأنماط (Java 21) لتعبيرات`switch`بتدمير الأنواع والسجلات والقيم - لتحل محل سلاسل`instanceof`المطولة.
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

### س5: كيف يمكنني التعامل مع الاستثناءات المحددة مقابل الاستثناءات غير المحددة بشكل صحيح؟
**أ:** الاستثناءات المحددة (`IOException`,`SQLException`) يجب الإعلان عنها في`throws`أو اكتشافها — فهي تمثل شروطًا قابلة للاسترداد يجب أن يعرفها المتصل. تمثل الاستثناءات غير المحددة (الفئات الفرعية`RuntimeException`مثل`NullPointerException`و `IllegalArgumentException`) أخطاء برمجية. أفضل الممارسات: استخدم الاستثناءات المحددة بشكل مقتصد (فهي تنشئ اقترانًا)، وفضل`Optional`للغياب المتوقع، وقم بتغليف الاستثناءات المحددة في الاستثناءات غير المحددة عند عبور حدود واجهة برمجة التطبيقات (API).
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

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة الأولى: إنشاء خط أنابيب آمن بين المنتج والمستهلك
**بيان المشكلة:** قم بتصميم خط أنابيب بين المنتج والمستهلك في Java حيث يقوم العديد من المنتجين بإنشاء عناصر عمل، ويقوم العديد من المستهلكين بمعالجتها بشكل متزامن، ويدعم النظام إيقاف التشغيل بسلاسة مع استنزاف العناصر المتبقية.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) قائمة انتظار محدودة لتخزين عناصر العمل مؤقتًا بين المنتجين والمستهلكين، (2) سلاسل إنتاج متعددة تضيف عناصر، (3) عناصر معالجة متعددة لخيوط المستهلك، (4) آلية للإشارة إلى إيقاف التشغيل واستنزاف العناصر المتبقية. تم تصميم`BlockingQueue`الخاص بـ Java لهذا الغرض.
**الخطوة الثانية — تحديد النهج:**
- استخدم`ArrayBlockingQueue`(محدود) لمنع نمو الذاكرة غير المحدودة.
- استخدم نمط الحبة السامة لإشارة إيقاف التشغيل.
- استخدم`ExecutorService`لإدارة تجمع مؤشرات الترابط.
- استخدم`CountDownLatch`للانتظار حتى ينتهي جميع المستهلكين من التصريف.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- قائمة الانتظار المحدودة تمنع OOM:`ArrayBlockingQueue(1000)`يحد من الذاكرة.
- نمط الحبة السامة: يخرج كل مستهلك بشكل نظيف بعد تلقي حبوبه.
-`poll(1, SECONDS)`مع انتهاء المهلة يمنع المستهلكين من الحظر إلى الأبد إذا كان المنتجون بطيئين.
- الإنتاج: استخدم`LinkedBlockingQueue`لخطوط الأنابيب غير المحدودة، أو`Disruptor`(LMAX) لخطوط الأنابيب ذات زمن الوصول المنخفض للغاية.
### المشكلة الثانية: تنفيذ أداة التحقق المخصصة المستندة إلى التعليقات التوضيحية
**بيان المشكلة:** قم بإنشاء إطار عمل للتحقق باستخدام التعليقات التوضيحية المخصصة. يقوم المستخدمون بتعليق الحقول باستخدام`@NotNull`و`@Min(0)`و`@Max(100)`و`@Size(min=1, max=50)`والاتصال بـ`Validator.validate(obj)`للحصول على قائمة بالانتهاكات.
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) تعليقات توضيحية مخصصة مع معلمات، (2) مدقق قائم على الانعكاس يقرأ التعليقات التوضيحية في وقت التشغيل، (3) كائن نتيجة يحتوي على جميع أخطاء التحقق من الصحة. يوضح هذا إمكانات معالجة التعليقات التوضيحية والانعكاس في Java.
**الخطوة الثانية — تحديد النهج:**
- تحديد التعليقات التوضيحية باستخدام`@Retention(RUNTIME)`و`@Target(FIELD)` .
- استخدم`Class.getDeclaredFields()`لتكرار الحقول.
- استخدم`Field.getAnnotation()`لقراءة قيم التعليقات التوضيحية.
- مقارنة قيم الحقول مع قيود الشرح.
- جمع الانتهاكات في القائمة.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- عبء الانعكاس: مقبول للتحقق من الصحة (يتم استدعاؤه مرة واحدة لكل طلب). بالنسبة للمسارات الساخنة، قم بعمليات البحث عن حقول ذاكرة التخزين المؤقت أو استخدم معالجة التعليقات التوضيحية في وقت الترجمة (مثل Hibernate Validator).
- القابلية للتوسعة: أضف تعليقات توضيحية جديدة عن طريق إنشاء التعليق التوضيحي + كتلة معالج في`validate()`.
- الإنتاج: استخدم`jakarta.validation`(Bean Validation 3.0) - وهو يفعل كل هذا وأكثر، مع معالجة وقت الترجمة عبر معالجات التعليقات التوضيحية.
### المشكلة 3: إنشاء عميل HTTP محدود السعر مع إعادة المحاولة
**بيان المشكلة:** قم بإنشاء برنامج تضمين عميل HTTP الذي يعيد محاولة الطلبات الفاشلة تلقائيًا مع التراجع الأسي، ويحترم حدود المعدل، ويدعم قطع الدائرة (توقف عن الاتصال بخدمة فاشلة).
**الخطوة الأولى — فهم المشكلة:**
نحتاج إلى: (1) إعادة المحاولة المنطقية مع التراجع الأسي والارتعاش، (2) تحديد المعدل لتجنب إرباك الخدمة المستهدفة، (3) نمط قاطع الدائرة - بعد N من حالات الفشل المتتالية، توقف عن الاتصال بالخدمة لفترة تهدئة. هذه ثلاثة اهتمامات قابلة للتركيب.
**الخطوة الثانية — تحديد النهج:**
- استخدم`java.net.http.HttpClient`(Java 11+) كعميل أساسي.
- تنفيذ إعادة المحاولة كمجمّع باستخدام`Thread.sleep`للتراجع.
- استخدم`Semaphore`لتحديد المعدل (أو`java.time`لحاوية الرمز المميز).
- تنفيذ قاطع الدائرة كجهاز حالة: مغلق → مفتوح → HALF_OPEN.
**الخطوة 3 — تنفيذ الحل:**
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

**الخطوة 4 — التحقق والتحسين:**
- التراجع الأسي مع الارتعاش يمنع القطيع الرعد (كل محاولات الضرب في نفس الوقت).
- قاطع الدائرة: بعد فشل`failureThreshold`المتتالي، تفتح الدائرة لـ`cooldownMs`- لا يتم إرسال أي طلبات، مما يحمي الخدمة الفاشلة.
- محدد المعدل:`Semaphore`مع الحد الأقصى للإنتاجية الدورية.
- الإنتاج: استخدم`resilience4j`- فهو يوفر جميع الأنماط الثلاثة (إعادة المحاولة، محدد المعدل، قاطع الدائرة) مع التطبيقات المناسبة والمقاييس وتكامل Spring Boot.
---

## ملخص
تعد Java واحدة من أهم لغات البرمجة التي تم إنشاؤها على الإطلاق. فهو يدير الأنظمة المصرفية العالمية وهواتف Android وخطوط البيانات الضخمة والواجهات الخلفية للمؤسسات. تعد Java الحديثة (21+) لغة مختلفة تمامًا عن Java 8 - فهي أكثر إيجازًا وأكثر تعبيرًا وتنافسية بشكل متزايد مع اللغات الأحدث. يعمل نظام JVM البيئي (Kotlin، Scala، Clojure) على توسيع نطاق وصوله إلى أبعد من ذلك. بالنسبة لتطوير المؤسسات، تظل Java خيارًا آمنًا وقويًا.