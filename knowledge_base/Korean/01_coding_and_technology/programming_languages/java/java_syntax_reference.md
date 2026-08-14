---
# Metadata
title: "Java — Syntax Reference"
description: "Detailed syntax reference for Java covering operators, control flow, functions, data structures, OOP, generics, concurrency, error handling, and modern Java features."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [java, syntax-reference, operators, control-flow, oop, generics, concurrency, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Java — 구문 참조
이 문서는 Java에 대한 포괄적이고 구조화된 구문 참조를 제공합니다. 이는 철저한 구문 패턴, 연산자 테이블, JVM, OOP 및 동시성의 내부 메커니즘에 중점을 두어 기본 Java 참조를 보완합니다.
---

## 연산자 및 표현식
### 산술 연산자
| 운영자 | 이름 | 예 | 결과 | 메모 |
|----------|------|---------|---------|-------|
| `+`| 추가 | `3 + 2`| `5`| 또한 문자열 연결 |
| `-`| 빼기 | `3 - 2`| `1`| |
| `*`| 곱셈 | `3 * 2`| `6`| |
| `/`| 부문 | `7 / 2`| `3`| `int`의 정수 나누기 ;  `double`용`3.5`|
| `%`| 나머지 | `7 % 2`| `1`| |
| `++`| 증분 | `x++`/`++x`| | 사후 및 사전 증분 |
| `--`| 감소 | `x--`/`--x`| | 사후 및 사전 감소 |
### 비교 및 ​​논리 연산자
| 운영자 | 이름 | 예 | 메모 |
|------------|------|---------|-------|
| `==`| 같음 | `x == y`| 객체에 대한 참조 동일성 |
| `!=`| 같지 않음 | `x != y`| |
| `<`,`>`,`<=`,`>=`| 관계형 | `x >= y`| |
| `&&`| 논리 AND | `a && b`| 단락 |
| `\|\|`| 논리적 OR | `a \|\| b`| 단락 |
| `!`| 논리적 NOT | `!true`| `false`|
| `instanceof`| 유형 확인 | `obj instanceof String`| 또한 패턴 일치(Java 16+) |
### 비트 연산자
| 운영자 | 이름 | 예 | 메모 |
|------------|------|---------|-------|
| `&`| 그리고 | `5 & 3`| `1`|
| `\|`| 또는 | `5 \| 3`| `7`|
| `^`| XOR | `5 ^ 3`| `6`|
| `~`| 보완 | `~5`| `-6`|
| `<<`| 왼쪽 시프트 | `5 << 1`| `10`|
| `>>`| 부호 있는 오른쪽 시프트 | `-5 >> 1`| `-3`|
| `>>>`| 부호 없는 오른쪽 시프트 | `-1 >>> 0`| `4294967295`|
### 연산자 우선 순위(가장 높은 것에서 가장 낮은 것까지)
| 우선순위 | 운영자 |
|------------|------------|
| 1(가장 높음) | 접미사:`expr++``expr--` |
| 2 | 단항:`++expr``--expr``+expr``-expr``~``!` |
| 3 | 출연진:`(Type)expr`|
| 4 | 곱셈:`*``/``%`|
| 5 | 첨가제:`+``-` |
| 6 | 시프트:`<<``>>``>>>`|
| 7 | 관계형:`<``>``<=``>=``instanceof`|
| 8 | 같음:`==``!=` |
| 9 | 비트 AND:`&`|
| 10 | 비트별 XOR:`^`|
| 11 | 비트 OR:`\|`|
| 12 | 논리 AND:`&&`|
| 13 | 논리 OR:`\|\|`|
| 14 | 삼항:`? :`|
| 15 | 할당:`=``+=``-=`등 |
---

## 제어 흐름
### 조건문
```java
// if / else if / else
if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else {
    grade = "F";
}

// Ternary operator
String status = age >= 18 ? "adult" : "minor";

// Switch expression (Java 14+) — returns a value
String description = switch (status) {
    case "active"   -> "Currently active";
    case "pending"  -> "Awaiting activation";
    case "suspended" -> "Temporarily suspended";
    default         -> "Unknown status";
};

// Switch with pattern matching (Java 21+)
static double area(Shape shape) {
    return switch (shape) {
        case Circle c    -> Math.PI * c.radius() * c.radius();
        case Rectangle r -> r.width() * r.height();
        default          -> 0;
    };
}

// Traditional switch (still valid)
switch (day) {
    case MONDAY, FRIDAY:
        System.out.println("Weekday");
        break;
    case SATURDAY, SUNDAY:
        System.out.println("Weekend");
        break;
    default:
        System.out.println("Midweek");
}
```

### 루프
```java
// for loop
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}

// Enhanced for-each loop
for (String item : list) {
    System.out.println(item);
}

// While loop
int count = 0;
while (count < 5) {
    System.out.println(count++);
}

// Do-while loop
do {
    int input = scanner.nextInt();
    process(input);
} while (input != 0);

// Labeled break/continue (rarely used but available)
outer:
for (int i = 0; i < matrix.length; i++) {
    for (int j = 0; j < matrix[i].length; j++) {
        if (matrix[i][j] == target) {
            break outer;
        }
    }
}
```

---

## 기능(메소드)
### 메소드 구문
```java
// Basic method
public int add(int a, int b) {
    return a + b;
}

// Static method
public static double average(double... numbers) {
    double sum = 0;
    for (double n : numbers) sum += n;
    return sum / numbers.length;
}

// Method overloading
public String format(int value) { return String.valueOf(value); }
public String format(double value) { return String.format("%.2f", value); }
public String format(String value) { return "\"" + value + "\""; }

// Varargs
public void log(String format, Object... args) {
    System.out.printf(format + "%n", args);
}

// Generic method
public <T extends Comparable<T>> T max(T a, T b) {
    return a.compareTo(b) >= 0 ? a : b;
}

// Sealed method (cannot be overridden)
public final String getId() { return id; }
```

### 람다 및 기능적 인터페이스
```java
// Lambda syntax
Runnable task = () -> System.out.println("Hello");
Comparator<String> byLength = (a, b) -> Integer.compare(a.length(), b.length());
Function<String, Integer> parse = Integer::parseInt;  // Method reference

// Built-in functional interfaces (java.util.function)
Predicate<String>  isLong    = s -> s.length() > 10;
Function<String, Integer> toLen = String::length;
Consumer<String>   printer   = System.out::println;
Supplier<List<String>> factory = ArrayList::new;
BiFunction<Integer, Integer, Integer> adder = Integer::sum;

// Method references
// Static method reference
Function<String, Integer> parser = Integer::parseInt;
// Instance method reference
BiFunction<String, String, Boolean> checker = String::equals;
// Constructor reference
Function<String, StringBuilder> builder = StringBuilder::new;
```

---

## 객체지향 프로그래밍
### 클래스와 상속
```java
// Abstract class
public abstract class Shape {
    protected final String color;

    protected Shape(String color) {
        this.color = color;
    }

    public abstract double area();
    public abstract double perimeter();

    public String describe() {
        return "%s %s: area=%.2f".formatted(color, getClass().getSimpleName(), area());
    }
}

// Concrete class
public class Circle extends Shape {
    private final double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }

    @Override
    public double perimeter() {
        return 2 * Math.PI * radius;
    }
}

// Interface
public interface Drawable {
    void draw(Canvas canvas);

    // Default method
    default void fill(Canvas canvas, Color color) {
        canvas.fill(this, color);
    }

    // Static method
    static Drawable empty() {
        return canvas -> {};
    }
}

// Multiple interface implementation
public class Widget extends Shape implements Drawable, Serializable {
    // ...
}

// Record (Java 16+) — immutable data carrier
public record Point(int x, int y) {
    // Compact constructor for validation
    public Point {
        if (x < 0 || y < 0) throw new IllegalArgumentException();
    }

    // Additional method
    public double distanceTo(Point other) {
        return Math.sqrt(Math.pow(x - other.x, 2) + Math.pow(y - other.y, 2));
    }
}

// Sealed class (Java 17+) — restrict subtypes
public sealed interface Shape permits Circle, Rectangle, Triangle {}
public record Circle(double radius) implements Shape {}
public record Rectangle(double width, double height) implements Shape {}
public record Triangle(double base, double height) implements Shape {}
```

---

## 데이터 구조
### 컬렉션 프레임워크
| 인터페이스 | 구현 | 주문됨 | 스레드로부터 안전한 변형 |
|------------|---|---------|-------|
| `List`|  `ArrayList`,`LinkedList`| 예 | `CopyOnWriteArrayList`|
| `Set`| `HashSet`,`TreeSet`,`LinkedHashSet`| 다양함 | `CopyOnWriteArraySet`|
| `Map`| `HashMap`,`TreeMap`,`LinkedHashMap`| 다양함 | `ConcurrentHashMap`|
| `Queue`| `ArrayDeque`,`PriorityQueue`| 다양함 | `ConcurrentLinkedQueue`|
| `Deque`| `ArrayDeque`| 양쪽 끝 | `ConcurrentLinkedDeque`|
### 목록
```java
// Creation
List<String> list = new ArrayList<>();
List<String> immutable = List.of("a", "b", "c");         // Java 9+
List<String> copy = List.copyOf(otherList);               // Java 10+
List<String> mutable = new ArrayList<>(List.of("x", "y"));

// Access
String first = list.get(0);
String last = list.getLast();                              // Java 21+
int index = list.indexOf("target");

// Mutation
list.add("item");
list.add(0, "first");
list.addAll(otherList);
list.remove("item");
list.remove(0);
list.set(0, "replacement");
list.clear();

// Iteration
for (String item : list) { System.out.println(item); }
list.forEach(System.out::println);
list.stream().filter(s -> s.length() > 3).forEach(System.out::println);

// Sorting
list.sort(Comparator.naturalOrder());
list.sort(Comparator.comparing(String::length).reversed());
Collections.sort(list);
```

### 지도
```java
// Creation
Map<String, Integer> map = new HashMap<>();
Map<String, Integer> immutable = Map.of("a", 1, "b", 2);  // Java 9+

// Access
Integer val = map.get("key");
int valOrDefault = map.getOrDefault("key", 0);
boolean hasKey = map.containsKey("key");

// Mutation
map.put("key", 42);
map.putIfAbsent("key", 0);
map.putAll(otherMap);
map.remove("key");
map.merge("key", 1, Integer::sum);  // Increment or initialize

// Compute methods
map.compute("key", (k, v) -> v == null ? 1 : v + 1);
map.computeIfAbsent("key", k -> expensiveLookup(k));
map.computeIfPresent("key", (k, v) -> v * 2);

// Iteration
for (var entry : map.entrySet()) {
    System.out.printf("%s = %d%n", entry.getKey(), entry.getValue());
}
map.forEach((k, v) -> System.out.printf("%s = %d%n", k, v));

// Stream operations
Map<String, Long> wordCounts = words.stream()
    .collect(Collectors.groupingBy(w -> w, Collectors.counting()));
```

---

## 제네릭
```java
// Generic class
public class Box<T> {
    private T value;
    public Box(T value) { this.value = value; }
    public T getValue() { return value; }
    public void setValue(T value) { this.value = value; }
}

// Bounded type parameters
public <T extends Comparable<T>> T max(T a, T b) {
    return a.compareTo(b) >= 0 ? a : b;
}

// Multiple bounds
public <T extends Comparable<T> & Serializable> T process(T item) { ... }

// Wildcards
public void printAll(List<?> items) {           // Unbounded wildcard
    items.forEach(System.out::println);
}
public void addNumbers(List<? super Integer> list) {  // Lower bound
    list.add(1);
    list.add(2);
}
public double sum(List<? extends Number> numbers) {   // Upper bound
    return numbers.stream().mapToDouble(Number::doubleValue).sum();
}

// PECS: Producer Extends, Consumer Super
public <T> void copy(List<? extends T> source, List<? super T> dest) {
    for (T item : source) { dest.add(item); }
}
```

---

## 오류 처리
```java
// try / catch / finally
try {
    String data = Files.readString(path);
    process(data);
} catch (IOException e) {
    logger.error("Failed to read: {}", path, e);
    throw new AppException("Read failed", e);
} catch (ParseException e) {
    logger.warn("Parse error in {}", path);
} finally {
    cleanup();
}

// try-with-resources (auto-closeable)
try (var reader = Files.newBufferedReader(path);
     var writer = Files.newBufferedWriter(output)) {
    reader.lines().forEach(writer::println);
}

// Custom exception
public class AppException extends RuntimeException {
    public AppException(String message, Throwable cause) {
        super(message, cause);
    }
}

// Multi-catch
try {
    // ...
} catch (IOException | SQLException e) {
    logger.error("Resource error", e);
}
```

---

## 동시성
### 스레드 및 실행자
```java
// Create thread
Thread t = new Thread(() -> System.out.println("Hello from thread"));
t.start();

// Executor framework
ExecutorService executor = Executors.newFixedThreadPool(4);
Future<String> future = executor.submit(() -> {
    Thread.sleep(1000);
    return "Result";
});
String result = future.get();  // Blocks until complete
executor.shutdown();

// CompletableFuture — async composition
CompletableFuture.supplyAsync(() -> fetchUser(id))
    .thenApplyAsync(user -> user.name())
    .thenAccept(System.out::println)
    .exceptionally(ex -> { log.error(ex.getMessage()); return null; });

// Combine multiple futures
CompletableFuture<String> nameFuture = ...;
CompletableFuture<Integer> ageFuture = ...;
CompletableFuture.allOf(nameFuture, ageFuture)
    .thenRun(() -> System.out.println("Both complete"));

// Virtual threads (Java 21+)
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 10_000).forEach(i -> {
        executor.submit(() -> {
            Thread.sleep(Duration.ofSeconds(1));
            return i;
        });
    });
}
```

### 동기화
```java
// synchronized method
public synchronized void increment() { count++; }

// synchronized block
synchronized (lock) {
    sharedResource++;
}

// ReentrantLock — more flexible than synchronized
private final ReentrantLock lock = new ReentrantLock();
public void safeUpdate() {
    lock.lock();
    try {
        // critical section
    } finally {
        lock.unlock();
    }
}

// Atomic variables — lock-free thread safety
AtomicInteger count = new AtomicInteger(0);
count.incrementAndGet();
count.compareAndSet(10, 20);

// Concurrent collections
ConcurrentHashMap<String, Integer> map = new ConcurrentHashMap<>();
BlockingQueue<String> queue = new LinkedBlockingQueue<>();
```

---

## 모듈 및 패키지
```java
// Package declaration
package com.example.service;

// Imports
import java.util.List;
import java.util.Map;
import java.util.concurrent.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

// Module declaration (Java 9+ module-info.java)
module com.example.app {
    requires java.sql;
    requires transitive com.example.api;
    exports com.example.service;
    opens com.example.model to com.fasterxml.jackson;
}
```

---

## 요약
Java의 구문은 1995년에 시작된 것보다 극적으로 발전했습니다. 최신 Java(21+)는 레코드, 봉인된 클래스, 패턴 일치, 가상 스레드 및 문자열 템플릿을 갖추고 있어 그 어느 때보다 간결하고 표현력이 풍부합니다. 핵심 구문은 여전히 ​​익숙하지만(C와 유사, 강력한 형식, 클래스 기반) 람다, Stream API 및 `var`가 추가되어 상용구가 크게 줄었습니다. 이 언어의 강점은 대규모 생태계, 이전 버전과의 호환성 보장, JIT 컴파일을 통한 JVM 성능 최적화에 있습니다.