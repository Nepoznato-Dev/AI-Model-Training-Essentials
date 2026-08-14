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

#Jawa
Java adalah bahasa pemrograman berorientasi objek yang diketik secara statis yang dibuat oleh James Gosling di Sun Microsystems dan dirilis pada tahun 1995. Filosofi desainnya — "tulis sekali, jalankan di mana saja" (WORA) — dicapai melalui Java Virtual Machine (JVM), yang memungkinkan kode Java yang dikompilasi untuk dijalankan pada platform apa pun yang memiliki implementasi JVM. Java adalah salah satu bahasa pemrograman yang paling banyak digunakan dalam sejarah, mendukung backend perusahaan, aplikasi Android, sistem data besar, dan layanan keuangan.
Meski usianya hampir 30 tahun, Pulau Jawa terus berkembang. Java modern (versi 17+) mencakup catatan, kelas tersegel, pencocokan pola, rangkaian virtual, dan ekosistem berkembang yang bersaing dengan bahasa-bahasa baru.
---

## Mengapa Java Penting
- **Standar perusahaan**: Tulang punggung backend Fortune 500 — perbankan, asuransi, e-commerce, layanan kesehatan.
- **Pengembangan Android**: Bahasa utama untuk Android (bersama Kotlin).
- **Ekosistem data besar**: Apache Hadoop, Spark, Kafka, Elasticsearch — semuanya ditulis dalam Java atau Scala (yang berjalan di JVM).
- **Ekosistem besar**: Lebih dari 500.000 perpustakaan di Maven Central; perkakas matang untuk setiap kebutuhan.
- **Kinerja**: Kompiler JIT JVM menghasilkan kode mesin yang sangat optimal saat runtime, sering kali cocok dengan C++ untuk aplikasi yang berjalan lama.
- **Kompatibilitas mundur**: Kode yang ditulis untuk Java 1.0 (1996) masih berjalan di JVM modern.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Verbositas** | Memerlukan lebih banyak boilerplate dibandingkan Python, Kotlin, atau Go | Gunakan Lombok, rekaman (Java 16+), dan IDE modern |
| **Penggunaan memori** | Overhead JVM berarti memori dasar yang lebih tinggi | Sesuaikan bendera JVM; gunakan gambar asli GraalVM untuk penerapan kecil |
| **Waktu mulai** | Pemanasan JVM bisa lambat untuk proses yang berumur pendek | Gambar asli GraalVM, atau gunakan C/Go untuk alat CLI |
| **Pengecualian yang diperiksa** | Memaksa penanganan pengecualian yang mungkin tidak dapat dipulihkan | Gunakan pengecualian yang tidak dicentang atau pola`Optional`|
| **Tidak ada jenis nilai** | Semuanya adalah objek (sampai proyek Valhalla) | Gunakan koleksi khusus primitif (Eclipse Collections, Trove) |
---

## Dasar Sintaks
### Struktur Dasar
Java berbasis kelas — semuanya ada di dalam kelas. Nama file harus sesuai dengan nama kelas publik.
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

### Pemrograman Berorientasi Objek
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

### Records (Java 16+) — Kelas Data Ringkas
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

### Koleksi dan Aliran
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

### Penanganan Pengecualian
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

## Sintaks & Pola Tingkat Lanjut
### Generik
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

### Kelas Tersegel dan Pencocokan Pola (Java 17+)
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

### Anotasi
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

### Antarmuka Fungsional dan Lambda
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

## Konkurensi & Paralelisme
### Utas Virtual (Java 21+)
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

### Threading dan Sinkronisasi Tradisional
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

## Konfigurasi Proyek & Sistem Pembangunan
### Struktur Proyek (Maven)
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

### Saluran CI/CD
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

## Pengujian
### JUnit 5 dengan Mockito
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

## Interoperabilitas
### JNI (Antarmuka Asli Java)
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

### Fungsi Asing & API Memori (Java 22+)
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

## Pola Desain
### Pola Pembuat
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

### Pola Pengamat
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

## Kinerja & Optimasi
### Alat Pembuatan Profil
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### Teknik Optimasi
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

## Penerapan
### File Docker
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
### Alat Pembuatan
| Alat | Tujuan | Catatan |
|------|---------|-------|
| **Maven** | Bangun otomatisasi + manajemen ketergantungan | Berbasis XML (`pom.xml`); standar industri untuk perusahaan |
| **Kelas** | Bangun otomatisasi + manajemen ketergantungan | DSL Groovy/Kotlin; lebih cepat untuk proyek besar; digunakan oleh Android |
### Kerangka kerja
| Kerangka | Domain | Deskripsi |
|-----------|--------|-------------|
| **Sepatu Musim Semi** | Web / perusahaan | Kerangka kerja Java yang dominan — REST API, layanan mikro, keamanan, akses data |
| **Jakarta EE** | Perusahaan | Penerus Java EE; API perusahaan standar |
| **Hibernasi** | ORM | Pemetaan objek-relasional; implementasi JPA standar |
| **Micronaut / Quarkus** | Cloud-asli | Startup cepat, memori rendah — dirancang untuk tanpa server dan container |
### Pengujian
| Alat | Tujuan |
|------|---------|
| **5 JUNI** | Kerangka pengujian unit |
| **Mockito** | Kerangka mengejek |
| **TegaskanJ** | Pernyataan lancar |
| **Wadah uji** | Tes integrasi dengan database nyata di Docker |
---

## Ekosistem JVM
| Bahasa JVM | Hubungan dengan Jawa |
|-------------|---------------------|
| **Kotlin** | Alternatif modern selain Java; Bahasa Android pilihan Google; 100% kompatibel dengan Java |
| **Skala** | Hibrida fungsional + OOP; mendukung Apache Spark |
| **Clojure** | Dialek cadel di JVM; pemrograman fungsional |
| **asyik** | Skrip dinamis untuk JVM; digunakan dalam file build Gradle |
Semua ini bisa menggunakan perpustakaan Java, dan Java bisa menggunakan perpustakaannya. JVM adalah platformnya, bukan hanya Java.
---

## Versi Java
| Versi | Tahun | Fitur Utama |
|---------|------|-------------|
| Jawa 8 | 2014 | **LTS** — Lambdas, Stream API, Opsional, metode default. Masih banyak digunakan. |
| Jawa 11 | 2018 | **LTS** — API Klien HTTP,`var`untuk variabel lokal, peluncur sumber file tunggal |
| Jawa 17 | 2021 | **LTS** — Kelas tersegel, pencocokan pola untuk`instanceof`, catatan, blok teks |
| Jawa 21 | 2023 | **LTS** — **Virtual thread** (Project Loom), pencocokan pola untuk`switch`, pola rekaman |
| Jawa 25 | 2025 | **LTS** — Templat string, pencocokan pola lebih lanjut, API fungsi asing |
**LTS** Versi (Dukungan Jangka Panjang) menerima pembaruan selama bertahun-tahun. Untuk produksi, gunakan Java 21 atau lebih baru.
---

## Kapan Menggunakan Java
| Skenario | Mengapa Jawa | Alternatif Lebih Baik |
|----------|---------|-------------------|
| Backend perusahaan | Ekosistem besar-besaran, Spring Boot, terbukti dalam skala besar | Kotlin (JVM yang sama, lebih sedikit verbose) |
| Pengembangan Android | Basis kode yang mapan dan besar | Kotlin (pilihan pilihan Google) |
| Data besar (Hadoop, Spark, Kafka) | Ekosistem dibangun di Java/Scala | Python untuk sisi ilmu data |
| Sistem keuangan | Performa + keandalan + perkakas matang | -- |
| Layanan mikro | Spring Boot + kerangka kerja cloud-native | Pilih layanan yang lebih sederhana |
| Skrip sederhana | Terlalu banyak upacara | Python, Cangkang |
| Alat CLI | Startup lambat | Ayo, Karat |
---

## Tanya Jawab Sintetis
### Q1: Apa perbedaan antara`==`dan`.equals()`di Java?
**A:**`==`membandingkan referensi objek (identitas) — memeriksa apakah dua variabel menunjuk ke objek yang sama di memori. `.equals()`membandingkan konten objek (kesetaraan nilai). Untuk primitif (`int`,`double`),`==`membandingkan nilai secara langsung. Untuk objek (termasuk`String`), selalu gunakan`.equals()`untuk membandingkan konten. Satu-satunya pengecualian adalah membandingkan dengan`null`, dimana`==`benar.
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

### Q2: Bagaimana cara kerja pengumpul sampah JVM, dan mana yang harus saya gunakan?
**A:** GC secara otomatis mengambil kembali memori dari objek yang tidak lagi dapat dijangkau. JVM modern (21+) menawarkan beberapa kolektor: G1 (default, seimbang), ZGC (waktu jeda sangat rendah, <1 md), dan Shenandoah (jeda rendah, OpenJDK). Untuk sebagian besar aplikasi, G1 default sudah cukup. Untuk layanan yang sensitif terhadap latensi, gunakan ZGC (`-XX:+UseZGC`). Untuk pemrosesan batch berorientasi throughput, gunakan Parallel GC (`-XX:+UseParallelGC`).
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### Q3: Kapan saya harus menggunakan`Stream API`vs loop tradisional?
**A:** Gunakan Streams ketika operasinya merupakan alur yang jelas (filter, petakan, pengurangan) — Streams mengekspresikan maksud dengan lebih baik dan diparalelkan dengan mudah dengan`.parallelStream()`. Gunakan loop tradisional untuk iterasi sederhana, ketika Anda perlu mengubah keadaan eksternal, ketika kinerja sangat penting (stream memiliki overhead), atau ketika logika melibatkan aliran kontrol yang kompleks (break, continue, multiple return). Hindari streaming untuk operasi`for-each`sederhana.
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

### Q4: Apa yang dimaksud dengan record, kelas tersegel, dan pencocokan pola di Java modern?
**A:** Catatan (Java 16) adalah pembawa data yang tidak dapat diubah — catatan tersebut menghasilkan konstruktor, pengambil,`equals`,`hashCode`, dan`toString`secara otomatis. Kelas tersegel (Java 17) membatasi kelas mana yang dapat memperluasnya — berguna untuk memodelkan hierarki tipe terbatas. Pencocokan pola (Java 21) memungkinkan ekspresi`switch`merusak struktur tipe, rekaman, dan nilai — menggantikan rantai`instanceof`yang verbose.
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

### Q5: Bagaimana cara menangani pengecualian yang dicentang dan tidak dicentang dengan benar?
**A:** Pengecualian yang dicentang (`IOException`,`SQLException`) harus dideklarasikan dalam`throws`atau ditangkap — pengecualian tersebut mewakili kondisi yang dapat dipulihkan yang harus diketahui oleh penelepon. Pengecualian yang tidak dicentang (subkelas`RuntimeException`seperti`NullPointerException`,`IllegalArgumentException`) menunjukkan bug pemrograman. Praktik terbaik: gunakan pengecualian yang dicentang dengan hemat (mereka membuat penggabungan), pilih`Optional`untuk ketidakhadiran yang diharapkan, dan gabungkan pengecualian yang dicentang dengan pengecualian yang tidak dicentang saat melewati batas API.
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

## Pemecahan Masalah Rantai Pemikiran
### Masalah 1: Membangun Saluran Produsen-Konsumen yang Aman untuk Thread
**Pernyataan Masalah:** Rancang saluran produsen-konsumen di Java di mana beberapa produsen menghasilkan item kerja, beberapa konsumen memprosesnya secara bersamaan, dan sistem mendukung penghentian yang baik dengan pengurasan item yang tersisa.
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan: (1) antrean terbatas untuk menyangga item kerja antara produsen dan konsumen, (2) beberapa rangkaian produsen menambahkan item, (3) beberapa rangkaian konsumen memproses item, (4) mekanisme untuk memberi sinyal penghentian dan menguras item yang tersisa.`BlockingQueue`Java dibuat khusus untuk ini.
**Langkah 2 — Identifikasi Pendekatannya:**
- Gunakan`ArrayBlockingQueue`(dibatasi) untuk mencegah pertumbuhan memori tanpa batas.
- Gunakan pola pil racun untuk sinyal mematikan.
- Gunakan`ExecutorService`untuk manajemen kumpulan thread.
- Gunakan`CountDownLatch`untuk menunggu semua konsumen selesai melakukan pengurasan.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Antrian yang dibatasi mencegah OOM:`ArrayBlockingQueue(1000)`membatasi memori.
- Pola pil racun: setiap konsumen keluar dengan bersih setelah menerima pilnya.
-`poll(1, SECONDS)`dengan batas waktu mencegah konsumen memblokir selamanya jika produsen lambat.
- Produksi: gunakan`LinkedBlockingQueue`untuk jaringan pipa tanpa batas, atau`Disruptor`(LMAX) untuk jaringan pipa dengan latensi sangat rendah.
### Masalah 2: Menerapkan Validator Berbasis Anotasi Kustom
**Pernyataan Masalah:** Buat kerangka validasi menggunakan anotasi khusus. Pengguna membubuhi keterangan pada kolom dengan`@NotNull`,`@Min(0)`,`@Max(100)`,`@Size(min=1, max=50)`, dan memanggil`Validator.validate(obj)`untuk mendapatkan daftar pelanggaran.
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan: (1) anotasi khusus dengan parameter, (2) validator berbasis refleksi yang membaca anotasi saat runtime, (3) objek hasil yang berisi semua kesalahan validasi. Ini menunjukkan kemampuan pemrosesan dan refleksi anotasi Java.
**Langkah 2 — Identifikasi Pendekatannya:**
- Tentukan anotasi dengan`@Retention(RUNTIME)`dan`@Target(FIELD)`.
- Gunakan`Class.getDeclaredFields()`untuk mengulangi bidang.
- Gunakan`Field.getAnnotation()`untuk membaca nilai anotasi.
- Bandingkan nilai bidang dengan batasan anotasi.
- Kumpulkan pelanggaran dalam daftar.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Overhead refleksi: dapat diterima untuk validasi (dipanggil sekali per permintaan). Untuk jalur panas, pencarian bidang cache atau gunakan pemrosesan anotasi waktu kompilasi (seperti Hibernate Validator).
- Ekstensibilitas: tambahkan anotasi baru dengan membuat anotasi + blok penangan di`validate()`.
- Produksi: gunakan`jakarta.validation`(Bean Validation 3.0) — ia melakukan semua ini dan lebih banyak lagi, dengan pemrosesan waktu kompilasi melalui pemroses anotasi.
### Masalah 3: Bangun Klien HTTP dengan Tarif Terbatas dengan Coba Lagi
**Pernyataan Masalah:** Membuat wrapper klien HTTP yang secara otomatis mencoba ulang permintaan yang gagal dengan backoff eksponensial, mematuhi batas kecepatan, dan mendukung pemutusan sirkuit (berhenti memanggil layanan yang gagal).
**Langkah 1 — Pahami Masalahnya:**
Kita memerlukan: (1) logika percobaan ulang dengan backoff dan jitter eksponensial, (2) pembatasan kecepatan agar layanan target tidak kewalahan, (3) pola pemutus sirkuit — setelah N kegagalan berturut-turut, berhenti memanggil layanan selama periode jeda pakai. Ini adalah tiga kekhawatiran yang dapat digabungkan.
**Langkah 2 — Identifikasi Pendekatannya:**
- Gunakan`java.net.http.HttpClient`(Java 11+) sebagai klien dasar.
- Terapkan percobaan ulang sebagai pembungkus dengan`Thread.sleep`untuk backoff.
- Gunakan`Semaphore`untuk pembatasan tarif (atau`java.time`untuk keranjang token).
- Menerapkan pemutus arus sebagai mesin keadaan: TUTUP → TERBUKA → HALF_OPEN.
**Langkah 3 — Terapkan Solusi:**
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

**Langkah 4 — Verifikasi dan Optimalkan:**
- Backoff eksponensial dengan jitter mencegah kawanan yang bergemuruh (semua percobaan ulang terjadi pada saat yang sama).
- Pemutus sirkuit: setelah kegagalan berturut-turut `failureThreshold`, sirkuit terbuka untuk`cooldownMs`— tidak ada permintaan yang dikirim, melindungi layanan yang gagal.
- Pembatas tarif:`Semaphore`dengan throughput batas pengisian berkala.
- Produksi: gunakan`resilience4j`— ini menyediakan ketiga pola (coba ulang, pembatas kecepatan, pemutus sirkuit) dengan implementasi, metrik, dan integrasi Spring Boot yang tepat.
---

## Ringkasan
Java adalah salah satu bahasa pemrograman terpenting yang pernah dibuat. Ia menjalankan sistem perbankan dunia, ponsel Android, jaringan big data, dan backend perusahaan. Java modern (21+) adalah bahasa yang sangat berbeda dari Java 8 — bahasa ini lebih ringkas, lebih ekspresif, dan semakin kompetitif dengan bahasa-bahasa baru. Ekosistem JVM (Kotlin, Scala, Clojure) memperluas jangkauannya lebih jauh. Untuk pengembangan perusahaan, Java tetap menjadi pilihan yang aman dan ampuh.