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

# জাভা - সিনট্যাক্স রেফারেন্স
এই নথিটি জাভার জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, অপারেটর টেবিল, এবং JVM, OOP, এবং কনকারেন্সির অভ্যন্তরীণ মেকানিক্সের উপর ফোকাস করে মূল জাভা রেফারেন্সের পরিপূরক।
---

## অপারেটর এবং এক্সপ্রেশন
### পাটিগণিত অপারেটর
| অপারেটর | নাম | উদাহরণ | ফলাফল | নোট |
|----------|------|---------|---------|-------|
| `+`| সংযোজন | `3 + 2`| `5`| এছাড়াও স্ট্রিং সংযোগ |
| `-`| বিয়োগ | `3 - 2`| `1`| |
| `*`| গুণ | `3 * 2`| `6`| |
| `/`| বিভাগ | `7 / 2`| `3`|`int`এর জন্য পূর্ণসংখ্যা বিভাগ; `double`এর জন্য`3.5`|
| `%`| অবশিষ্ট | `7 % 2`| `1`| |
| `++`| বৃদ্ধি | `x++`/`++x`| | পোস্ট- এবং প্রি-ইনক্রিমেন্ট |
| `--`| হ্রাস | `x--`/`--x`| | পোস্ট- এবং প্রি-ডিক্রিমেন্ট |
### তুলনা ও লজিক্যাল অপারেটর
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `==`| সমান | `x == y`| বস্তুর জন্য রেফারেন্স সমতা |
| `!=`| সমান নয় | `x != y`| |
| `<`,`>`,`<=`,`>=`| সম্পর্কীয় | `x >= y`| |
| `&&`| যৌক্তিক এবং | `a && b`| শর্ট সার্কিট |
| `\|\|`| যৌক্তিক বা | `a \|\| b`| শর্ট সার্কিট |
| `!`| যৌক্তিক নয় | `!true`| `false`|
| `instanceof`| টাইপ চেক | `obj instanceof String`| এছাড়াও প্যাটার্ন ম্যাচিং (জাভা 16+) |
### বিটওয়াইজ অপারেটর
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `&`| এবং | `5 & 3`| `1`|
| `\|`| বা | `5 \| 3`| `7`|
| `^`| XOR | `5 ^ 3`| `6`|
| `~`| পরিপূরক | `~5`| `-6`|
| `<<`| বাম শিফট | `5 << 1`| `10`|
| `>>`| সাইন ইন রাইট শিফট | `-5 >> 1`| `-3`|
| `>>>`| স্বাক্ষরবিহীন ডান স্থানান্তর | `-1 >>> 0`| `4294967295`|
### অপারেটর অগ্রাধিকার (সর্বোচ্চ থেকে সর্বনিম্ন)
| অগ্রাধিকার | অপারেটর |
|------------|------------|
| 1 (সর্বোচ্চ) | পোস্টফিক্স:`expr++``expr--` |
| 2 | ইউনারি:`++expr``--expr``+expr``-expr``~``!` |
| 3 | কাস্ট:`(Type)expr`|
| 4 | গুণক:`*``/``%`|
| 5 | সংযোজন:`+``-` |
| 6 | শিফট:`<<``>>``>>>`|
| 7 | রিলেশনাল:`<``>``<=``>=``instanceof`|
| 8 | সমতা:`==``!=` |
| 9 | Bitwise এবং:`&`|
| 10 | Bitwise XOR:`^`|
| 11 | বিটওয়াইজ বা:`\|`|
| 12 | যৌক্তিক এবং:`&&`|
| 13 | যৌক্তিক বা:`\|\|`|
| 14 | টারনারি:`? :`|
| 15 | অ্যাসাইনমেন্ট:`=``+=``-=`ইত্যাদি |
---

## নিয়ন্ত্রণ প্রবাহ
### শর্তসাপেক্ষ বিবৃতি
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

### লুপ
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

## কার্যাবলী (পদ্ধতি)
### পদ্ধতি সিনট্যাক্স
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

### ল্যাম্বডাস এবং কার্যকরী ইন্টারফেস
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

## অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং
### ক্লাস এবং উত্তরাধিকার
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

## ডেটা স্ট্রাকচার
### সংগ্রহের ফ্রেমওয়ার্ক
| ইন্টারফেস | বাস্তবায়ন | আদেশ করা | থ্রেড-নিরাপদ বৈকল্পিক |
|------------|----------------|------------|----------------------|
| `List`| `ArrayList`,`LinkedList`| হ্যাঁ | `CopyOnWriteArrayList`|
| `Set`| `HashSet`,`TreeSet`,`LinkedHashSet`| পরিবর্তিত হয় | `CopyOnWriteArraySet`|
| `Map`| `HashMap`,`TreeMap`,`LinkedHashMap`| পরিবর্তিত হয় | `ConcurrentHashMap`|
| `Queue`| `ArrayDeque`,`PriorityQueue`| পরিবর্তিত হয় | `ConcurrentLinkedQueue`|
| `Deque`| `ArrayDeque`| উভয় প্রান্ত | `ConcurrentLinkedDeque`|
### তালিকা
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

### মানচিত্র
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

## জেনেরিক
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

## ত্রুটি হ্যান্ডলিং
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

## সামঞ্জস্য
### থ্রেড এবং এক্সিকিউটর
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

### সিঙ্ক্রোনাইজেশন
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

## মডিউল এবং প্যাকেজ
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

## সারাংশ
জাভা এর সিনট্যাক্স 1995 এর উত্স থেকে নাটকীয়ভাবে বিকশিত হয়েছে। আধুনিক জাভা (21+) বৈশিষ্ট্যগুলি রেকর্ড, সিল করা ক্লাস, প্যাটার্ন ম্যাচিং, ভার্চুয়াল থ্রেড এবং স্ট্রিং টেমপ্লেট - এটিকে আগের চেয়ে আরও সংক্ষিপ্ত এবং অভিব্যক্তিপূর্ণ করে তোলে। মূল সিনট্যাক্স পরিচিত রয়ে গেছে (C-এর মতো, দৃঢ়ভাবে টাইপ করা, শ্রেণী-ভিত্তিক), কিন্তু ল্যাম্বডাস, স্ট্রিম API, এবং`var`এর সংযোজন উল্লেখযোগ্যভাবে বয়লারপ্লেট হ্রাস করেছে। ভাষার শক্তি তার বিশাল ইকোসিস্টেম, পশ্চাদগামী সামঞ্জস্যের গ্যারান্টি, এবং JIT সংকলনের মাধ্যমে JVM-এর কর্মক্ষমতা অপ্টিমাইজেশানের মধ্যে রয়েছে।