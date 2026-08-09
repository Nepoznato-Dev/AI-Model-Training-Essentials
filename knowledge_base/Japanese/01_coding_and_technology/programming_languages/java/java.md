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

### レコード (Java 16+) — 簡潔なデータ クラス
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

### 従来のスレッド処理と同期
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
| **テストコンテナ** | Docker での実際のデータベースとの統合テスト |
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
| Java 8 | 2014年 | **LTS** — ラムダ、ストリーム API、オプション、デフォルトのメソッド。今でも広く使われています。 |
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

＃＃ まとめ
Java は、これまでに作成された最も重要なプログラミング言語の 1 つです。世界中の銀行システム、Android スマートフォン、ビッグデータ パイプライン、エンタープライズ バックエンドを実行しています。 Modern Java (21+) は Java 8 とは大きく異なる言語です。より簡潔で表現力が高く、新しい言語との競争力も高まっています。 JVM エコシステム (Kotlin、Scala、Clojure) はその範囲をさらに拡大します。エンタープライズ開発にとって、Java は依然として安全で強力な選択肢です。