---
# Metadata
title: "Java — Syntax Reference"
description: "Detailed syntax reference for Java covering operators, control flow, functions, data structures, OOP, generics, concurrency, error handling, and modern Java features."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
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
# जावा - सिंटैक्स संदर्भ
यह दस्तावेज़ जावा के लिए एक व्यापक, संरचित वाक्यविन्यास संदर्भ प्रदान करता है। यह संपूर्ण सिंटैक्स पैटर्न, ऑपरेटर तालिकाओं और जेवीएम, ओओपी और समवर्ती के आंतरिक यांत्रिकी पर ध्यान केंद्रित करके मुख्य जावा संदर्भ को पूरक करता है।
---

## ऑपरेटर्स और अभिव्यक्तियाँ
### अंकगणित संचालक
| ऑपरेटर | नाम | उदाहरण | परिणाम | नोट्स |
|-------|------|------|--------|-------|
| `+`| जोड़ | `3 + 2`| `5`| इसके अलावा स्ट्रिंग संयोजन |
| `-`| घटाव | `3 - 2`| `1`| |
| `*`| गुणन | `3 * 2`| `6`| |
| `/`| प्रभाग | `7 / 2`| `3`|`int`के लिए पूर्णांक विभाजन; `double`के लिए`3.5`|
| `%`| शेष | `7 % 2`| `1`| |
| `++`| वेतन वृद्धि | `x++`/`++x`| | पद- एवं पूर्व-वृद्धि |
| `--`| कमी | `x--`/`--x`| | पोस्ट- और प्री-डिक्रीमेंट |
### तुलना एवं तार्किक संचालक
| ऑपरेटर | नाम | उदाहरण | नोट्स |
|-------|------|------|-------|
| `==`| बराबर | `x == y`| वस्तुओं के लिए संदर्भ समानता |
| `!=`| समान नहीं | `x != y`| |
| `<`,`>`,`<=`,`>=`| संबंधपरक | `x >= y`| |
| `&&`| तार्किक और | `a && b`| शॉर्ट-सर्किट |
| `\|\|`| तार्किक या | `a \|\| b`| शॉर्ट-सर्किट |
| `!`| तार्किक नहीं | `!true`| `false`|
| `instanceof`| चेक टाइप करें | `obj instanceof String`| साथ ही पैटर्न मिलान (जावा 16+) |
### बिटवाइज़ ऑपरेटर्स
| ऑपरेटर | नाम | उदाहरण | नोट्स |
|-------|------|------|-------|
| `&`| तथा | `5 & 3`| `1`|
| `\|`| या | `5 \| 3`| `7`|
| `^`| एक्सओआर | `5 ^ 3`| `6`|
| `~`| पूरक | `~5`| `-6`|
| `<<`| वाम पारी | `5 << 1`| `10`|
| `>>`| दाहिनी ओर हस्ताक्षरित शिफ्ट | `-5 >> 1`| `-3`|
| `>>>`| अहस्ताक्षरित दायां शिफ्ट | `-1 >>> 0`| `4294967295`|
### ऑपरेटर प्राथमिकता (उच्चतम से निम्नतम)
| वरीयता | संचालक |
|-------|
| 1 (सर्वोच्च) | पोस्टफ़िक्स:`expr++``expr--` |
| 2 | यूनरी:`++expr``--expr``+expr``-expr``~``!` |
| 3 | कास्ट:`(Type)expr`|
| 4 | गुणक:`*``/``%`|
| 5 | योजक:`+``-` |
| 6 | शिफ्ट:`<<``>>``>>>`|
| 7 | संबंधपरक:`<``>``<=``>=``instanceof`|
| 8 | समानता:`==``!=` |
| 9 | बिटवाइज़ और:`&`|
| 10 | बिटवाइज़ XOR:`^`|
| 11 | बिटवाइज़ OR:`\|`|
| 12 | तार्किक और:`&&`|
| 13 | तार्किक या:`\|\|`|
| 14 | टर्नरी:`? :`|
| 15 | असाइनमेंट:`=``+=``-=`आदि |
---

## प्रवाह को नियंत्रित करें
### सशर्त कथन
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

### लूप्स
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

## फ़ंक्शंस (तरीके)
### विधि सिंटेक्स
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

### लैम्ब्डा और कार्यात्मक इंटरफेस
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

## ऑब्जेक्ट ओरिएंटेड प्रोग्रामिंग
### वर्ग और विरासत
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

## डेटा संरचनाएँ
### संग्रह ढांचा
| इंटरफ़ेस | कार्यान्वयन | आदेश दिया | थ्रेड-सुरक्षित संस्करण |
|----|---|---|---|---|
| `List`| `ArrayList`,`LinkedList`| हाँ | `CopyOnWriteArrayList`|
| `Set`| `HashSet`,`TreeSet`,`LinkedHashSet`| बदलता रहता है | `CopyOnWriteArraySet`|
| `Map`| `HashMap`,`TreeMap`,`LinkedHashMap`| बदलता रहता है | `ConcurrentHashMap`|
| `Queue`| `ArrayDeque`,`PriorityQueue`| बदलता रहता है | `ConcurrentLinkedQueue`|
| `Deque`| `ArrayDeque`| दोनों छोर | `ConcurrentLinkedDeque`|
### सूचियाँ
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

### मानचित्र
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

## जेनेरिक
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

## त्रुटि प्रबंधन
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

## समवर्ती
### धागे और निष्पादक
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

### तुल्यकालन
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

## मॉड्यूल और पैकेज
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

## सारांश
जावा का सिंटैक्स 1995 की शुरुआत से नाटकीय रूप से विकसित हुआ है। आधुनिक जावा (21+) में रिकॉर्ड, सीलबंद कक्षाएं, पैटर्न मिलान, वर्चुअल थ्रेड और स्ट्रिंग टेम्पलेट शामिल हैं - जो इसे पहले से कहीं अधिक संक्षिप्त और अभिव्यंजक बनाते हैं। कोर सिंटैक्स परिचित रहता है (सी-जैसा, दृढ़ता से टाइप किया गया, क्लास-आधारित), लेकिन लैम्ब्डा, स्ट्रीम एपीआई और`var`के अतिरिक्त ने बॉयलरप्लेट को काफी कम कर दिया है। भाषा की ताकत उसके विशाल पारिस्थितिकी तंत्र, पिछड़ी संगतता गारंटी और जेआईटी संकलन के माध्यम से जेवीएम के प्रदर्शन अनुकूलन में निहित है।