---
# Metadata
title: "Java — Cheat Sheet"
description: "Quick-reference cheat sheet for Java syntax, collections, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [java, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Java — チートシート
## 基本
```java
// Variables
int x = 42;
double pi = 3.14159;
String name = "Alice";
boolean active = true;
var inferred = "hello";  // Java 10+ local variable type inference
final int MAX = 100;     // constant

// Primitive types
byte b = 127;
short s = 32767;
int i = 2_000_000;       // underscores in literals
long l = 100L;
float f = 3.14f;
double d = 3.14159;
char c = 'A';

// String formatting
String msg = String.format("Hello, %s! Age: %d", name, age);
"Hello, %s!".formatted(name);  // Java 15+
String template = STR."Hello, \{name}!";  // Java 21+ preview

// String methods
name.length()
name.toUpperCase()
name.contains("lic")
name.substring(0, 3)
name.strip()              // trim (Java 11+)
name.isBlank()            // Java 11+
"hello".repeat(3)         // "hellohellohello"
```

## データ構造
```java
// ArrayList
var list = new ArrayList<String>();
list.add("Alice");
list.add("Bob");
list.get(0);
list.size();
list.remove("Bob");
list.stream().filter(s -> s.length() > 3).toList();

// HashMap
var map = new HashMap<String, Integer>();
map.put("alice", 90);
map.getOrDefault("bob", 0);
map.computeIfAbsent("charlie", k -> 0);
map.entrySet().forEach((e) -> System.out.println(e));

// Set
var set = new HashSet<>(List.of(1, 2, 3));
set.add(4);
set.contains(2);

// Immutable collections (Java 9+)
var list = List.of("a", "b", "c");
var set = Set.of(1, 2, 3);
var map = Map.of("a", 1, "b", 2);

// Array
int[] arr = {1, 2, 3};
int[] copy = Arrays.copyOf(arr, 5);
Arrays.sort(arr);
```

## 制御フロー
```java
if (condition) {
    // ...
} else if (other) {
    // ...
} else {
    // ...
}

// Ternary
String result = condition ? "yes" : "no";

// Switch expression (Java 14+)
String label = switch (day) {
    case MONDAY, TUESDAY -> "early week";
    case WEDNESDAY       -> "midweek";
    default              -> "later";
};

// Enhanced switch with yield
int numLetters = switch (day) {
    case MONDAY, FRIDAY, SUNDAY -> 6;
    default -> {
        int len = day.name().length();
        yield len;
    }
};

// Loops
for (var item : collection) { ... }
for (int i = 0; i < 10; i++) { ... }
while (condition) { ... }
```

## クラスと記録
```java
// Record (Java 16+)
public record Point(double x, double y) {
    // compact constructor
    public Point {
        if (x < 0 || y < 0) throw new IllegalArgumentException();
    }
}
var p = new Point(1.0, 2.0);
p.x();  // accessor (not getX)

// Sealed class (Java 17+)
public sealed interface Shape permits Circle, Rectangle {
    double area();
}
public record Circle(double radius) implements Shape {
    public double area() { return Math.PI * radius * radius; }
}

// Class basics
public class User {
    private String name;
    private int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() { return name; }
}
```

## ストリームとラムダ
```java
// Stream pipeline
List<String> names = users.stream()
    .filter(u -> u.age() >= 18)
    .sorted(Comparator.comparing(User::name))
    .map(User::name)
    .toList();

// Collectors
Map<String, Long> counts = items.stream()
    .collect(Collectors.groupingBy(Item::category, Collectors.counting()));

// Optional
Optional<String> opt = findUser(id).map(User::name);
String name = opt.orElse("Unknown");
opt.ifPresent(n -> System.out.println(n));

// Method references
list.forEach(System.out::println);
list.stream().map(String::toUpperCase);
```

## エラー処理
```java
try {
    riskyOperation();
} catch (IOException e) {
    log.error("IO failed", e);
} catch (SQLException e) {
    throw new RuntimeException("DB error", e);
} finally {
    cleanup();
}

// Try-with-resources
try (var reader = new BufferedReader(new FileReader("data.txt"))) {
    String line = reader.readLine();
}

// Custom exception
public class BusinessException extends RuntimeException {
    public BusinessException(String message) {
        super(message);
    }
}
```

## 同時実行性
```java
// Virtual threads (Java 21+)
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 100).forEach(i ->
        executor.submit(() -> {
            Thread.sleep(Duration.ofSeconds(1));
            return i;
        })
    );
}

// CompletableFuture
CompletableFuture.supplyAsync(() -> fetchData())
    .thenApply(data -> process(data))
    .thenAccept(result -> System.out.println(result))
    .exceptionally(ex -> { log.error("Failed", ex); return null; });

// Synchronized
synchronized (lock) {
    counter++;
}
```
