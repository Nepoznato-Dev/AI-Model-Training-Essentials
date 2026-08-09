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
# Ява
Java — это статически типизированный объектно-ориентированный язык программирования, созданный Джеймсом Гослингом из Sun Microsystems и выпущенный в 1995 году. Его философия проектирования — «напиши один раз, запускай где угодно» (WORA) — достигается с помощью виртуальной машины Java (JVM), которая позволяет скомпилированному коду Java работать на любой платформе, имеющей реализацию JVM. Java — один из наиболее широко используемых языков программирования в истории, на котором базируются корпоративные серверные части, приложения Android, системы больших данных и финансовые услуги.
Несмотря на то, что Java уже почти 30 лет, она продолжает развиваться. Современная Java (версии 17+) включает в себя записи, запечатанные классы, сопоставление с образцом, виртуальные потоки и растущую экосистему, конкурирующую с новыми языками.
---

## Почему Java имеет значение
- **Корпоративный стандарт**: основа серверных частей из списка Fortune 500 — банковское дело, страхование, электронная коммерция, здравоохранение.
- **Разработка для Android**: основной язык Android (наряду с Kotlin).
- **Экосистема больших данных**: Apache Hadoop, Spark, Kafka, Elasticsearch — все они написаны на Java или Scala (работает на JVM).
- **Огромная экосистема**: более 500 000 библиотек на Maven Central; зрелые инструменты для любых нужд.
- **Производительность**: JIT-компилятор JVM создает высокооптимизированный машинный код во время выполнения, часто соответствующий C++ для долговыполняющихся приложений.
- **Обратная совместимость**: код, написанный для Java 1.0 (1996 г.), по-прежнему работает на современных JVM.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Многословие** | Требуется больше шаблонов, чем Python, Kotlin или Go | Используйте Lombok, записи (Java 16+) и современные IDE |
| **Использование памяти** | Накладные расходы JVM означают больший объем базовой памяти | Настройте флаги JVM; использовать собственные образы GraalVM для небольших развертываний |
| **Время запуска** | Разогрев JVM может быть медленным для недолговечных процессов | Собственный образ GraalVM или использование C/Go для инструментов CLI |
| **Проверенные исключения** | Принудительная обработка исключений, которые невозможно восстановить | Используйте непроверенные исключения или шаблон`Optional`|
| **Нет типов значений** | Все является объектом (до проекта Валгалла) | Использовать примитивно-специализированные коллекции (Eclipse Collections, Trove) |
---

## Основы синтаксиса
### Базовая структура
Java основана на классах — все находится внутри класса. Имя файла должно совпадать с именем общедоступного класса.
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

### Объектно-ориентированное программирование
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

### Records (Java 16+) — краткие классы данных
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

### Коллекции и потоки
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

### Обработка исключений
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

## Расширенный синтаксис и шаблоны
### Дженерики
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

### Запечатанные классы и сопоставление с образцом (Java 17+)
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

### Аннотации
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

### Функциональные интерфейсы и лямбды
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

## Параллелизм и параллелизм
### Виртуальные потоки (Java 21+)
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

### Традиционная обработка потоков и синхронизация
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

## Конфигурация проекта и система сборки
### Структура проекта (Maven)
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

### build.gradle.kts (Грейдл)
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

### Конвейер CI/CD
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

## Тестирование
### JUnit 5 с Mockito
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

## Совместимость
### JNI (собственный интерфейс Java)
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

### API внешних функций и памяти (Java 22+)
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

## Шаблоны проектирования
### Шаблон «Строитель»
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

### Шаблон наблюдателя
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

## Производительность и оптимизация
### Инструменты профилирования
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### Методы оптимизации
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

## Развертывание
### Докер-файл
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

## Экосистема
### Инструменты сборки
| Инструмент | Цель | Заметки |
|------|---------|-------|
| **Мавен** | Автоматизация сборки + управление зависимостями | на основе XML (`pom.xml`); отраслевой стандарт для предприятий |
| **Грейдл** | Автоматизация сборки + управление зависимостями | Groovy/Kotlin DSL; быстрее для крупных проектов; используется Android |
### Фреймворки
| Рамочная | Домен | Описание |
|-----------|--------|-------------|
| **Весенние ботинки** | Интернет/предприятие | Доминирующая платформа Java — REST API, микросервисы, безопасность, доступ к данным |
| **Джакарта, Восточная Европа** | Предприятие | Преемник Java EE; стандартизированные корпоративные API |
| **Гибернация** | ОРМ | Объектно-реляционное отображение; стандартная реализация JPA |
| **Микронавт/Кваркус** | Облачный | Быстрый запуск, мало памяти — предназначено для бессерверных систем и контейнеров |
### Тестирование
| Инструмент | Цель |
|------|---------|
| **Юнит 5** | Платформа модульного тестирования |
| **Мокито** | Издевательская структура |
| **УтверждатьJ** | Беглые утверждения |
| **Тестовые контейнеры** | Интеграционные тесты с реальными базами данных в Docker |
---

## Экосистема JVM
| Язык JVM | Связь с Java |
|-------------|---------------------|
| **Котлин** | Современная альтернатива Java; Предпочитаемый язык Android от Google; 100% Java-совместимость |
| **Скала** | Гибрид функционал + ООП; полномочия Apache Spark |
| **Кложур** | Диалект Lisp на JVM; функциональное программирование |
| **Отлично** | Динамические сценарии для JVM; используется в файлах сборки Gradle |
Все они могут использовать библиотеки Java, а Java может использовать их библиотеки. JVM — это платформа, а не только Java.
---

## Версии Java
| Версия | Год | Ключевые особенности |
|---------|------|-------------|
| Ява 8 | 2014 | **LTS** — Lambdas, Stream API, необязательные методы по умолчанию. До сих пор широко используется. |
| Ява 11 | 2018 | **LTS** — API HTTP-клиента,`var`для локальных переменных, средство запуска однофайлового исходного кода |
| Ява 17 | 2021 | **LTS** — Запечатанные классы, сопоставление с образцом для `instanceof`, записи, текстовые блоки |
| Ява 21 | 2023 | **LTS** — **Виртуальные потоки** (Project Loom), сопоставление шаблонов для`switch`, шаблоны записи |
| Ява 25 | 2025 | **LTS** — Строковые шаблоны, дальнейшее сопоставление с образцом, API внешних функций |
**Версии LTS** (долгосрочная поддержка) получают обновления в течение многих лет. Для производства используйте Java 21 или более позднюю версию.
---

## Когда использовать Java
| Сценарий | Почему Java | Лучшая альтернатива |
|----------|---------|-------------------|
| Корпоративные серверные части | Массивная экосистема Spring Boot, проверенная в масштабе | Kotlin (тот же JVM, менее многословный) |
| Разработка для Android | Создана огромная кодовая база | Kotlin (предпочтительный выбор Google) |
| Большие данные (Hadoop, Spark, Kafka) | Экосистема построена на Java/Scala | Python для науки о данных |
| Финансовые системы | Производительность + надежность + проверенные инструменты | -- |
| Микросервисы | Spring Boot + облачные фреймворки | Выбирайте более простые услуги |
| Простые скрипты | Слишком много церемоний | Питон, оболочка |
| Инструменты CLI | Медленный запуск | Вперёд, Раст |
---

## Краткое содержание
Java — один из самых важных языков программирования, когда-либо созданных. Он управляет мировыми банковскими системами, телефонами Android, конвейерами больших данных и корпоративными серверными модулями. Современный Java (21+) сильно отличается от Java 8: он более краток, более выразителен и все более конкурирует с новыми языками. Экосистема JVM (Kotlin, Scala, Clojure) расширяет сферу применения. Для корпоративных разработок Java остается безопасным и мощным выбором.