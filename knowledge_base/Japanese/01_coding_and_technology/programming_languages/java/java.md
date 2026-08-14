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
Java は、Sun Microsystems の James Gosling によって作成され、1995 年にリリースされた静的型付けのオブジェクト指向プログラミング言語です。その設計哲学である「一度書けば、どこでも実行できる」(WORA) は、Java 仮想マシン (JVM) によって実現されており、コンパイルされた Java コードを、JVM 実装を備えた任意のプラットフォーム上で実行できます。 Java は歴史上最も広く使用されているプログラミング言語の 1 つであり、エンタープライズ バックエンド、Android アプリ、ビッグ データ システム、金融サービスを強化しています。
Java は 30 年近くの歴史があるにもかかわらず、進化し続けています。最新の Java (バージョン 17 以降) には、レコード、シールされたクラス、パターン マッチング、仮想スレッド、および新しい言語と競合する成長するエコシステムが含まれています。
---

## Java が重要な理由
- **エンタープライズ標準**: 銀行、保険、電子商取引、ヘルスケアなど、フォーチュン 500 のバックエンドのバックボーン。
- **Android 開発**: Android の主要言語 (Kotlin と並ぶ)。
- **ビッグ データ エコシステム**: Apache Hadoop、Spark、Kafka、Elasticsearch — すべて Java または Scala (JVM 上で実行) で書かれています。
- **大規模なエコシステム**: Maven Central 上の 500,000 を超えるライブラリ。あらゆるニーズに応える成熟したツール。
- **パフォーマンス**: JVM の JIT コンパイラは、実行時に高度に最適化されたマシン コードを生成し、長時間実行されるアプリケーションでは C++ に匹敵することがよくあります。
- **下位互換性**: Java 1.0 (1996) 用に作成されたコードは、現在でも最新の JVM で実行できます。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **冗長** | Python、Kotlin、Go よりも多くの定型文が必要 | Lombok、レコード (Java 16 以降)、および最新の IDE を使用する |
| **メモリ使用量** | JVM オーバーヘッドはベースライン メモリの増加を意味します。 JVM フラグを調整します。小規模な展開には GraalVM ネイティブ イメージを使用する |
| **起動時間** |有効期間が短いプロセスの場合、JVM のウォームアップが遅くなる可能性があります。 GraalVM ネイティブ イメージ、または CLI ツールに C/Go を使用する |
| **チェックされた例外** |回復できない可能性のある例外の処理を強制します。チェックされていない例外または`Optional`パターンを使用します。
| **値の種類はありません** |すべてはオブジェクトです (ヴァルハラプロジェクトまで) |プリミティブに特化したコレクションを使用する (Eclipse Collections、Trove) |
---

## 構文の基礎
### 基本構造
Java はクラスベースであり、すべてがクラス内に存在します。ファイル名はパブリック クラス名と一致する必要があります。
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

### オブジェクト指向プログラミング
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

### レコード (Java 16 以降) — 簡潔なデータ クラス
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

### コレクションとストリーム
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

### 例外処理
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

## 高度な構文とパターン
### ジェネリック医薬品
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

### シールされたクラスとパターン マッチング (Java 17 以降)
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

### 注釈
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

### 関数インターフェイスとラムダ
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

## 同時実行性と並列処理
### 仮想スレッド (Java 21+)
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

### 従来のスレッド化と同期
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

## プロジェクトの構成とシステムの構築
### プロジェクト構造 (Maven)
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

### CI/CD パイプライン
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

## テスト
### JUnit 5 と Mockito
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

## 相互運用性
### JNI (Java ネイティブ インターフェイス)
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

### 外部関数およびメモリ API (Java 22+)
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

## デザインパターン
### ビルダーパターン
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

### オブザーバーパターン
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

## パフォーマンスと最適化
### プロファイリングツール
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### 最適化手法
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

## デプロイメント
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

## エコシステム
### ビルドツール
|ツール |目的 |メモ |
|------|-------|------|
| **メイブン** |ビルド自動化 + 依存関係管理 | XML ベース (`pom.xml`)。企業向けの業界標準 |
| **グラドル** |ビルド自動化 + 依存関係管理 | Groovy/Kotlin DSL。大規模なプロジェクトの場合はより速くなります。 Android で使用 |
### フレームワーク
|フレームワーク |ドメイン |説明 |
|----------|----------|---------------|
| **スプリングブーツ** |ウェブ / エンタープライズ |主要な Java フレームワーク — REST API、マイクロサービス、セキュリティ、データ アクセス |
| **ジャカルタEE** |エンタープライズ | Java EEの後継。標準化されたエンタープライズ API |
| **休止状態** | ORM |オブジェクトリレーショナルマッピング。標準の JPA 実装 |
| **マイクロノート / クォーカス** |クラウドネイティブ |高速起動、低メモリ — サーバーレスおよびコンテナ向けに設計 |
### テスト
|ツール |目的 |
|-----|----------|
| **JUnit 5** |単体テストフレームワーク |
| **モキト** |モックフレームワーク |
| **アサートJ** |流暢な主張 |
| **テストコンテナ** | Docker で実際のデータベースとの統合テスト |
---

## JVM エコシステム
| JVM言語 | Javaとの関係 |
|---------------|----------|
| **Kotlin** | Java に代わる最新の代替手段。 Google が優先する Android 言語。 100% Java 互換 |
| **スカラ** |機能的 + OOP ハイブリッド。 Apache Spark のパワー |
| **Clojure** | JVM 上の Lisp 方言。関数型プログラミング |
| **グルーヴィー** | JVM の動的スクリプト。 Gradle ビルド ファイルで使用される |
これらはすべて Java ライブラリを使用でき、Java もそれらのライブラリを使用できます。 JVM は単なる Java ではなくプラットフォームです。
---

## Java バージョン
|バージョン |年 |主な機能 |
|----------|------|---------------|
| Java 8 | 2014年 | **LTS** — Lambda、Stream API、オプション、デフォルトのメソッド。今でも広く使われています。 |
| Java 11 | 2018年 | **LTS** — HTTP クライアント API、ローカル変数用の `var`、単一ファイル ソース ランチャー |
| Java 17 | 2021年 | **LTS** — シールされたクラス、`instanceof`、レコード、テキスト ブロックのパターン マッチング |
| Java 21 | 2023年 | **LTS** — **仮想スレッド** (Project Loom)、`switch`のパターン マッチング、レコード パターン |
| Java 25 | 2025年 | **LTS** — 文字列テンプレート、さらなるパターン マッチング、外部関数 API |
**LTS** (長期サポート) バージョンは、長年にわたりアップデートを受け取ります。運用環境では、Java 21 以降を使用してください。
---

## Java を使用する場合
|シナリオ |なぜ Java |より良い代替案 |
|----------|----------|----------|
|エンタープライズ バックエンド |大規模なエコシステム、Spring Boot が大規模に実証済み | Kotlin (同じ JVM、冗長性は低い) |
| Android開発 |確立された巨大なコードベース | Kotlin (Google が推奨する選択肢) |
|ビッグデータ (Hadoop、Spark、Kafka) |エコシステムは Java/Scala に基づいて構築されています。データサイエンス側のPython |
|金融システム |パフォーマンス + 信頼性 + 成熟したツール | -- |
|マイクロサービス | Spring Boot + クラウドネイティブ フレームワーク |よりシンプルなサービスを目指しましょう |
|単純なスクリプト |儀式が多すぎる | Python、シェル |
| CLI ツール |起動が遅い |さあ、錆びよ |
---

## 総合的な Q&A
### Q1: Java の`==`と`.equals()`の違いは何ですか?
**A:**`==`はオブジェクト参照 (同一性) を比較します。2 つの変数がメモリ内の同じオブジェクトを指しているかどうかをチェックします。 `.equals()`は、オブジェクトの内容 (値の同一性) を比較します。プリミティブ (`int`、`double`) の場合、`==`は値を直接比較します。オブジェクト (`String`を含む) の場合は、常に`.equals()`を使用してコンテンツを比較します。唯一の例外は`null`との比較であり、`==`が正しいです。
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

### Q2: JVM ガベージ コレクターはどのように機能しますか?どれを使用する必要がありますか?
**A:** GC は、アクセスできなくなったオブジェクトからメモリを自動的に再利用します。最新の JVM (21 以降) は、G1 (デフォルト、バランス)、ZGC (超低停止時間、<1ms)、および Shenandoah (低停止、OpenJDK) などのいくつかのコレクターを提供します。ほとんどのアプリケーションでは、デフォルトの G1 で問題ありません。遅延の影響を受けやすいサービスの場合は、ZGC (`-XX:+UseZGC`) を使用します。スループット重視のバッチ処理の場合は、並列 GC (`-XX:+UseParallelGC`) を使用します。
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### Q3: 従来のループではなく、どのような場合に`Stream API`を使用する必要がありますか?
**A:** 操作が明確なパイプライン (フィルター、マップ、リデュース) である場合は、ストリームを使用します。ストリームは意図をより適切に表現し、`.parallelStream()`と簡単に並列化します。従来のループは、外部状態を変更する必要がある場合、パフォーマンスが重要な場合 (ストリームにオーバーヘッドがある場合)、またはロジックに複雑な制御フロー (中断、続行、複数のリターン) が含まれる場合、単純な反復に使用します。単純な`for-each`操作のストリームは避けてください。
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

### Q4: 最新の Java におけるレコード、シールされたクラス、パターン マッチングとは何ですか?
**A:** レコード (Java 16) は不変のデータ キャリアであり、コンストラクター、ゲッター、`equals`、`hashCode`、および`toString`を自動生成します。 Sealed クラス (Java 17) は、それを拡張できるクラスを制限します。これは、有限型の階層をモデル化するのに役立ちます。パターン マッチング (Java 21) では、`switch` 式を使用して型、レコード、および値を構造化でき、冗長な`instanceof`チェーンを置き換えることができます。
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

### Q5: チェックされた例外とチェックされていない例外を適切に処理するにはどうすればよいですか?
**A:** チェック例外 (`IOException`、`SQLException`) は、`throws`で宣言するか、キャッチする必要があります。これらは、呼び出し元が知っておく必要がある回復可能な状態を表します。未チェック例外 (`NullPointerException`、`IllegalArgumentException`などの`RuntimeException`サブクラス) はプログラミングのバグを表します。ベスト プラクティス: チェック例外は控えめに使用し (結合が作成されます)、不在が予想される場合は`Optional`を優先し、API 境界を越える場合はチェック例外を非チェック例外でラップします。
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

## 思考連鎖による問題解決
### 問題 1: スレッドセーフなプロデューサー/コンシューマー パイプラインの構築
**問題ステートメント:** Java でプロデューサー/コンシューマー パイプラインを設計します。このパイプラインでは、複数のプロデューサーが作業項目を生成し、複数のコンシューマーがそれらを同時に処理し、システムが残りのアイテムのドレインによる正常なシャットダウンをサポートします。
**ステップ 1 — 問題を理解する:**
(1) プロデューサーとコンシューマー間の作業アイテムをバッファリングするための境界付きキュー、(2) アイテムを追加する複数のプロデューサー スレッド、(3) アイテムを処理する複数のコンシューマー スレッド、(4) シャットダウンを通知し、残りのアイテムを排出するメカニズムが必要です。 Java の`BlockingQueue`は、この目的に特化して構築されています。
**ステップ 2 — アプローチを特定する:**
- 無制限のメモリ増加を防ぐには、`ArrayBlockingQueue` (制限付き) を使用します。
- シャットダウン信号にポイズンピルパターンを使用します。
- スレッドプール管理には`ExecutorService`を使用します。
-`CountDownLatch`を使用して、すべてのコンシューマが排出を完了するまで待ちます。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- 境界付きキューにより OOM を防止:`ArrayBlockingQueue(1000)`がメモリを制限します。
- 毒薬のパターン: 各消費者は薬を受け取った後、きれいに退場します。
- タイムアウト付きの`poll(1, SECONDS)`は、プロデューサーが遅い場合にコンシューマーが永久にブロックすることを防ぎます。
- プロダクション: 無制限の場合は`LinkedBlockingQueue`を使用し、超低遅延パイプラインの場合は`Disruptor`(LMAX) を使用します。
### 問題 2: カスタムのアノテーションベースのバリデーターを実装する
**問題ステートメント:** カスタム アノテーションを使用して検証フレームワークを作成します。ユーザーはフィールドに`@NotNull`、`@Min(0)`、`@Max(100)`、`@Size(min=1, max=50)`の注釈を付け、`Validator.validate(obj)`を呼び出して違反のリストを取得します。
**ステップ 1 — 問題を理解する:**
(1) パラメータを備えたカスタム アノテーション、(2) 実行時にアノテーションを読み取るリフレクション ベースのバリデータ、(3) すべての検証エラーを含む結果オブジェクトが必要です。これは、Java のアノテーション処理およびリフレクション機能を示しています。
**ステップ 2 — アプローチを特定する:**
-`@Retention(RUNTIME)`および`@Target(FIELD)`を使用してアノテーションを定義します。
-`Class.getDeclaredFields()`を使用してフィールドを反復します。
- 注釈値を読み取るには、`Field.getAnnotation()` を使用します。
- フィールド値を注釈制約と比較します。
- 違反をリストに収集します。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- リフレクション オーバーヘッド: 検証に許容されます (リクエストごとに 1 回呼び出されます)。ホット パスの場合、フィールド ルックアップをキャッシュするか、コンパイル時のアノテーション処理 (Hibernate Validator など) を使用します。
- 拡張性:`validate()`に注釈とハンドラー ブロックを作成して、新しい注釈を追加します。
- 実稼働:`jakarta.validation`(Bean Validation 3.0) を使用します。これは、アノテーション プロセッサを介したコンパイル時処理で、これらすべてを実行します。
### 問題 3: 再試行を伴うレート制限された HTTP クライアントの構築
**問題ステートメント:** 指数バックオフを使用して失敗したリクエストを自動的に再試行し、レート制限を尊重し、サーキット ブレーク (失敗したサービスの呼び出しを停止する) をサポートする HTTP クライアント ラッパーを作成します。
**ステップ 1 — 問題を理解する:**
必要なのは: (1) 指数バックオフとジッターを使用した再試行ロジック、(2) ターゲット サービスへの負荷を避けるためのレート制限、(3) サーキット ブレーカー パターン - N 回連続して失敗した後、クールダウン期間の間サービスの呼び出しを停止する。これらは 3 つの構成可能な懸念事項です。
**ステップ 2 — アプローチを特定する:**
-`java.net.http.HttpClient`(Java 11+) をベースクライアントとして使用します。
- バックオフ用に`Thread.sleep`を使用してラッパーとしてリトライを実装します。
- レート制限には`Semaphore`を使用します (トークン バケットには `java.time`)。
- サーキット ブレーカーをステート マシンとして実装します: CLOSED → OPEN → HALF_OPEN。
**ステップ 3 — ソリューションの実装:**
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

**ステップ 4 — 検証と最適化:**
- ジッターを伴う指数関数的バックオフにより、雷を散らす群れ (すべての再試行が同時にヒットする) を防ぎます。
- サーキット ブレーカー:`failureThreshold`が連続して失敗すると、`cooldownMs` に対して回線が開きます。リクエストは送信されず、失敗したサービスが保護されます。
- レート リミッター:`Semaphore`(定期補充上限スループットあり)。
- 運用:`resilience4j`を使用します。これは、適切な実装、メトリクス、Spring Boot 統合を備えた 3 つのパターン (再試行、レート リミッター、サーキット ブレーカー) をすべて提供します。
---

＃＃ まとめ
Java は、これまでに作成された最も重要なプログラミング言語の 1 つです。世界中の銀行システム、Android スマートフォン、ビッグデータ パイプライン、エンタープライズ バックエンドを実行しています。 Modern Java (21+) は Java 8 とは大きく異なる言語です。より簡潔で表現力が高く、新しい言語との競争力も高まっています。 JVM エコシステム (Kotlin、Scala、Clojure) はその範囲をさらに拡大します。エンタープライズ開発にとって、Java は依然として安全で強力な選択肢です。