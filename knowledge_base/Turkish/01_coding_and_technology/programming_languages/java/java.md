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

#Java
Java, Sun Microsystems'den James Gosling tarafından oluşturulan ve 1995 yılında piyasaya sürülen, statik olarak yazılan, nesne yönelimli bir programlama dilidir. Tasarım felsefesi - "bir kez yaz, her yerde çalıştır" (WORA) - derlenmiş Java kodunun JVM uygulamasına sahip herhangi bir platformda çalışmasına izin veren Java Sanal Makinesi (JVM) aracılığıyla gerçekleştirilir. Java tarihte en yaygın kullanılan programlama dillerinden biridir ve kurumsal arka uçları, Android uygulamalarını, büyük veri sistemlerini ve finansal hizmetleri destekler.
Yaklaşık 30 yaşında olmasına rağmen Java gelişmeye devam ediyor. Modern Java (sürüm 17+) kayıtları, mühürlü sınıfları, kalıp eşleştirmeyi, sanal iş parçacıklarını ve daha yeni dillerle rekabet eden büyüyen bir ekosistemi içerir.
---

## Java Neden Önemlidir
- **Kurumsal standart**: Fortune 500 arka uçlarının omurgası — bankacılık, sigorta, e-ticaret, sağlık hizmetleri.
- **Android geliştirme**: Android için birincil dil (Kotlin ile birlikte).
- **Büyük veri ekosistemi**: Apache Hadoop, Spark, Kafka, Elasticsearch — tümü Java veya Scala'da yazılmıştır (JVM'de çalışır).
- **Devasa ekosistem**: Maven Central'da 500.000'den fazla kütüphane; Her ihtiyaca uygun olgun takımlar.
- **Performans**: JVM'nin JIT derleyicisi, çalışma zamanında yüksek düzeyde optimize edilmiş makine kodu üretir ve genellikle uzun süreli uygulamalar için C++ ile eşleşir.
- **Geriye dönük uyumluluk**: Java 1.0 (1996) için yazılan kod hala modern JVM'lerde çalışmaktadır.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Ayrıntı düzeyi** | Python, Kotlin veya Go'dan daha fazla standart metin gerektirir | Lombok'u, kayıtları (Java 16+) ve modern IDE'leri kullanın |
| **Bellek kullanımı** | JVM yükü, daha yüksek temel bellek anlamına gelir | JVM bayraklarını ayarlayın; küçük dağıtımlar için GraalVM yerel görüntülerini kullanın |
| **Başlatma zamanı** | Kısa ömürlü işlemler için JVM'nin ısınması yavaş olabilir | GraalVM yerel görüntüsü veya CLI araçları için C/Go kullanın |
| **İşaretlenen istisnalar** | Kurtarılamayacak özel durumların işlenmesini zorlar | Denetlenmeyen özel durumları veya`Optional`modelini kullanın |
| **Değer türü yok** | Her şey bir nesnedir (Valhalla projesine kadar) | İlkel özel koleksiyonları kullanın (Eclipse Koleksiyonları, Trove) |
---

## Söz Diziminin Temelleri
### Temel Yapı
Java sınıf tabanlıdır; her şey bir sınıfın içinde yaşar. Dosya adı genel sınıf adıyla eşleşmelidir.
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

### Nesneye Yönelik Programlama
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

### Kayıtlar (Java 16+) — Kısa Veri Sınıfları
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

### Koleksiyonlar ve Akışlar
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

### İstisna İşleme
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

## Gelişmiş Sözdizimi ve Desenler
### Jenerikler
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

### Mühürlü Sınıflar ve Desen Eşleştirme (Java 17+)
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

### Ek Açıklamalar
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

### İşlevsel Arayüzler ve Lambdalar
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

## Eşzamanlılık ve Paralellik
### Sanal Konular (Java 21+)
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

### Geleneksel İş Parçacığı Oluşturma ve Senkronizasyon
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı (Maven)
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

### CI/CD Ardışık Düzeni
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

## Test etme
### JUnit 5 ile Mockito
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

## Birlikte Çalışabilirlik
### JNI (Java Yerel Arayüzü)
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

### Yabancı İşlev ve Bellek API'si (Java 22+)
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

## Tasarım Desenleri
### Oluşturucu Deseni
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

### Gözlemci Deseni
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

## Performans ve Optimizasyon
### Profil Oluşturma Araçları
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### Optimizasyon Teknikleri
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

## Dağıtım
### Docker dosyası
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

## Ekosistem
### Oluşturma Araçları
| Araç | Amaç | Notlar |
|------|------------|-------|
| **Maven** | Otomasyon + bağımlılık yönetimi oluşturun | XML tabanlı (`pom.xml`); şirketler için endüstri standardı |
| **Kepçe** | Otomasyon + bağımlılık yönetimi oluşturun | Groovy/Kotlin DSL; büyük projeler için daha hızlı; Android tarafından kullanılıyor |
### Çerçeveler
| Çerçeve | Etki Alanı | Açıklama |
|-----------|-----------|------------|
| **Bahar Çizme** | Web / kurumsal | Baskın Java çerçevesi — REST API'ler, mikro hizmetler, güvenlik, veri erişimi |
| **Jakarta EE** | Kurumsal | Java EE'nin halefi; standartlaştırılmış kurumsal API'ler |
| **Hazırda Bekletme** | ORM | Nesne-ilişkisel haritalama; standart JPA uygulaması |
| **Mikronot / Kuarkus** | Bulutta yerel | Hızlı başlatma, düşük bellek — sunucusuz ve konteynerler için tasarlandı |
### Test
| Araç | Amaç |
|------|------------|
| **JÜnite 5** | Birim test çerçevesi |
| **Mockito** | Alaycı çerçeve |
| **İddiaJ** | Akıcı iddialar |
| **Test kapsayıcıları** | Docker'da gerçek veritabanlarıyla entegrasyon testleri |
---

## JVM Ekosistemi
| JVM Dili | Java ile İlişki |
|---------------|----------|
| **Kotlin** | Java'ya modern alternatif; Google'ın tercih ettiği Android dili; %100 Java uyumlu |
| **Skala** | İşlevsel + OOP hibriti; Apache Spark'a güç veriyor |
| **Kapanış** | JVM'de Lisp lehçesi; fonksiyonel programlama |
| **Harika** | JVM için dinamik komut dosyası oluşturma; Gradle derleme dosyalarında kullanılır |
Bunların hepsi Java kütüphanelerini kullanabilir ve Java da kütüphanelerini kullanabilir. JVM yalnızca Java değil, platformdur.
---

## Java Sürümleri
| Sürüm | Yıl | Temel Özellikler |
|-----------|------|------------|
| Java 8 | 2014 | **LTS** — Lambdalar, Akış API'si, İsteğe bağlı, varsayılan yöntemler. Halen yaygın olarak kullanılmaktadır. |
| Java 11 | 2018 | **LTS** — HTTP İstemci API'si, yerel değişkenler için `var`, tek dosya kaynak başlatıcısı |
| Java 17 | 2021 | **LTS** — Mühürlü sınıflar,`instanceof`için desen eşleştirme, kayıtlar, metin blokları |
| Java 21 | 2023 | **LTS** — **Sanal iş parçacıkları** (Proje Tezgahı),`switch`için desen eşleştirme, kayıt desenleri |
| Java 25 | 2025 | **LTS** — Dize şablonları, daha fazla kalıp eşleştirme, yabancı işlev API'si |
**LTS** (Uzun Süreli Destek) sürümleri uzun yıllar boyunca güncelleme alır. Üretim için Java 21 veya üstünü kullanın.
---

## Java Ne Zaman Kullanılmalı
| Senaryo | Neden Java | Daha İyi Alternatif |
|----------|------------|-----------|
| Kurumsal arka uçlar | Büyük ekosistem, Spring Boot, geniş ölçekte kanıtlanmış | Kotlin (aynı JVM, daha az ayrıntılı) |
| Android geliştirme | Yerleşik, devasa kod tabanı | Kotlin (Google'ın tercih ettiği seçim) |
| Büyük veri (Hadoop, Spark, Kafka) | Ekosistem Java/Scala üzerine kurulmuştur | Veri bilimi tarafı için Python |
| Finansal sistemler | Performans + güvenilirlik + gelişmiş takımlama | -- |
| Mikro hizmetler | Spring Boot + bulutta yerel çerçeveler | Daha basit hizmetlere gidin |
| Basit komut dosyaları | Çok fazla tören | Python, Kabuk |
| CLI araçları | Yavaş başlatma | Git, Pas |
---

## Sentetik Soru-Cevap
### S1: Java'da`==`ile`.equals()`arasındaki fark nedir?
**C:**`==`nesne referanslarını (kimlik) karşılaştırır — iki değişkenin bellekteki aynı nesneyi gösterip göstermediğini kontrol eder. `.equals()`nesne içeriğini karşılaştırır (değer eşitliği). İlkel değerler için (`int`,`double`),`==`değerleri doğrudan karşılaştırır. Nesneler için (`String` dahil), içeriği karşılaştırmak için her zaman `.equals()`'yi kullanın. Bunun tek istisnası, `==`'nin doğru olduğu`null`ile karşılaştırmadır.
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

### S2: JVM çöp toplayıcı nasıl çalışır ve hangisini kullanmalıyım?
**C:** GC, artık ulaşılamayan nesnelerden belleği otomatik olarak geri alır. Modern JVM'ler (21+) çeşitli toplayıcılar sunar: G1 (varsayılan, dengeli), ZGC (ultra düşük duraklama süreleri, <1 ms) ve Shenandoah (düşük duraklama, OpenJDK). Çoğu uygulama için varsayılan G1 uygundur. Gecikmeye duyarlı hizmetler için ZGC'yi (`-XX:+UseZGC`) kullanın. Üretim odaklı toplu işleme için Paralel GC'yi (`-XX:+UseParallelGC`) kullanın.
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### S3: `Stream API`'yi geleneksel döngülere karşı ne zaman kullanmalıyım?
**C:** İşlem net bir işlem hattı olduğunda (filtreleme, eşleme, azaltma) Akışları kullanın; niyeti daha iyi ifade ederler ve`.parallelStream()`ile kolayca paralel hale gelirler. Harici durumu değiştirmeniz gerektiğinde, performans kritik olduğunda (akışlar ek yüke sahiptir) veya mantık karmaşık kontrol akışı içerdiğinde (kesme, devam etme, çoklu dönüşler) basit yinelemeler için geleneksel döngüleri kullanın. Basit`for-each`işlemleri için akışlardan kaçının.
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

### S4: Modern Java'da kayıtlar, mühürlü sınıflar ve kalıp eşleştirme nedir?
**C:** Kayıtlar (Java 16) değişmez veri taşıyıcılarıdır; yapıcıları, alıcıları,`equals`,`hashCode`ve `toString`'yi otomatik olarak oluştururlar. Kapalı sınıflar (Java 17), hangi sınıfların kendilerini genişletebileceğini kısıtlar; sonlu tür hiyerarşilerini modellemek için kullanışlıdır. Desen eşleştirme (Java 21),`switch`ifadelerinin türleri, kayıtları ve değerleri bozarak ayrıntılı`instanceof`zincirlerinin yerini almasına olanak tanır.
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

### S5: İşaretli ve denetlenmeyen istisnaları doğru şekilde nasıl ele alabilirim?
**C:** İşaretlenen istisnalar (`IOException`,`SQLException`) `throws`'de bildirilmeli veya yakalanmalıdır; bunlar arayanın bilmesi gereken kurtarılabilir koşulları temsil eder. Denetlenmeyen istisnalar (`NullPointerException`,`IllegalArgumentException`gibi`RuntimeException`alt sınıfları) programlama hatalarını temsil eder. En iyi uygulama: kontrol edilen istisnaları dikkatli kullanın (bağlantı oluştururlar), beklenen yokluk için `Optional`'yi tercih edin ve API sınırlarını geçerken kontrol edilen istisnaları kontrol edilmeyenlerin içine sarın.
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

## Düşünce Zinciri Problem Çözme
### Sorun 1: İş parçacığı açısından güvenli bir Üretici-Tüketici Boru Hattı Oluşturun
**Sorun Açıklaması:** Java'da birden fazla üreticinin iş öğeleri oluşturduğu, birden fazla tüketicinin bunları eşzamanlı olarak işlediği ve sistemin kalan öğelerin boşaltılmasıyla sorunsuz kapatmayı desteklediği bir üretici-tüketici hattı tasarlayın.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1) iş öğelerini üreticiler ve tüketiciler arasında tamponlamak için sınırlı bir kuyruk, (2) öğeleri ekleyen birden fazla üretici iş parçacığı, (3) öğeleri işleyen birden fazla tüketici iş parçacığı, (4) kapatma sinyali verecek ve kalan öğeleri boşaltacak bir mekanizma. Java'nın `BlockingQueue`'si bunun için özel olarak tasarlanmıştır.
**2. Adım — Yaklaşımı Belirleyin:**
- Sınırsız bellek büyümesini önlemek için`ArrayBlockingQueue`(sınırlı) kullanın.
- Kapatma sinyali için zehirli hap modeli kullanın.
- İş parçacığı havuzu yönetimi için`ExecutorService`kullanın.
- Tüm tüketicilerin boşaltma işlemini bitirmesini beklemek için `CountDownLatch`'yi kullanın.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Sınırlı kuyruk OOM'u önler:`ArrayBlockingQueue(1000)`belleği sınırlar.
- Zehirli hap modeli: Her tüketici hapını aldıktan sonra temiz bir şekilde çıkar.
- Zaman aşımına sahip `poll(1, SECONDS)`, üreticilerin yavaş olması durumunda tüketicilerin sonsuza kadar bloke olmasını önler.
- Üretim: Sınırsız için `LinkedBlockingQueue`'yi veya ultra düşük gecikme süreli işlem hatları için`Disruptor`(LMAX) kullanın.
### Sorun 2: Özel Açıklama Tabanlı Doğrulayıcı Uygulama
**Sorun Açıklaması:** Özel ek açıklamaları kullanarak bir doğrulama çerçevesi oluşturun. Kullanıcılar alanlara `@NotNull`, `@Min(0)`, `@Max(100)`,`@Size(min=1, max=50)`ile açıklama ekler ve ihlallerin listesini almak için `Validator.validate(obj)`'yi arar.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1) parametreler içeren özel açıklamalara, (2) çalışma zamanında açıklamaları okuyan yansıma tabanlı bir doğrulayıcıya, (3) tüm doğrulama hatalarını içeren bir sonuç nesnesine. Bu, Java'nın açıklama işleme ve yansıtma yeteneklerini gösterir.
**2. Adım — Yaklaşımı Belirleyin:**
-`@Retention(RUNTIME)`ve`@Target(FIELD)`ile ek açıklamaları tanımlayın.
- Alanları yinelemek için`Class.getDeclaredFields()`kullanın.
- Ek açıklama değerlerini okumak için `Field.getAnnotation()`'yi kullanın.
- Alan değerlerini açıklama kısıtlamalarıyla karşılaştırın.
- İhlalleri bir listede toplayın.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Yansıma ek yükü: doğrulama için kabul edilebilir (istek başına bir kez çağrılır). Sıcak yollar için, alan aramalarını önbelleğe alın veya derleme zamanı açıklama işlemeyi kullanın (Hazırda Bekletme Doğrulayıcı gibi).
- Genişletilebilirlik: `validate()`'de ek açıklama + bir işleyici bloğu oluşturarak yeni ek açıklamalar ekleyin.
- Üretim:`jakarta.validation`(Bean Validation 3.0) kullanın — tüm bunları ve daha fazlasını, açıklama işlemcileri aracılığıyla derleme zamanı işlemeyle yapar.
### Sorun 3: Yeniden Deneme ile Hız Sınırlı bir HTTP İstemcisi Oluşturun
**Sorun Açıklaması:** Üstel geri çekilmeyle başarısız istekleri otomatik olarak yeniden deneyen, hız sınırlarına uyan ve devre kesmeyi destekleyen (başarısız bir hizmeti çağırmayı durduran) bir HTTP istemci sarmalayıcısı oluşturun.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1) üstel geri çekilme ve titreşim ile yeniden deneme mantığı, (2) hedef hizmetin aşırı yüklenmesini önlemek için hız sınırlama, (3) devre kesici modeli — N ardışık arızadan sonra, bir bekleme süresi için hizmeti aramayı bırakın. Bunlar birleştirilebilir üç endişedir.
**2. Adım — Yaklaşımı Belirleyin:**
- Temel istemci olarak`java.net.http.HttpClient`(Java 11+) kullanın.
- Geri alma için`Thread.sleep`ile sarmalayıcı olarak yeniden denemeyi uygulayın.
- Hız sınırlaması için`Semaphore`kullanın (veya jeton kovası için `java.time`).
- Devre kesiciyi durum makinesi olarak uygulayın: KAPALI → AÇIK → HALF_AÇIK.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Titreşimli üstel geri çekilme sürünün gürlemesini önler (tüm yeniden denemeler aynı anda vurur).
- Devre kesici:`failureThreshold`ardışık arızalarından sonra devre`cooldownMs`için açılır — hiçbir istek gönderilmez ve arızalı hizmeti korur.
- Hız sınırlayıcı: Periyodik ikmal kapasitesi ile `Semaphore`.
- Üretim:`resilience4j`kullanın — üç modeli de (yeniden deneme, hız sınırlayıcı, devre kesici) uygun uygulamalar, ölçümler ve Spring Boot entegrasyonuyla sağlar.
---

## Özet
Java şimdiye kadar oluşturulmuş en önemli programlama dillerinden biridir. Dünyanın bankacılık sistemlerini, Android telefonlarını, büyük veri hatlarını ve kurumsal arka uçları çalıştırır. Modern Java (21+), Java 8'den çok farklı bir dildir; daha kısa ve özdür, daha anlamlıdır ve yeni dillerle giderek daha rekabetçi hale gelir. JVM ekosistemi (Kotlin, Scala, Clojure) erişimini daha da genişletiyor. Kurumsal gelişim için Java güvenli ve güçlü bir seçim olmaya devam ediyor.