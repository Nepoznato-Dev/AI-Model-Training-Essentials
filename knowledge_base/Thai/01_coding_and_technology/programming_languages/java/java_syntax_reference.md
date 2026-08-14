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
# Java - การอ้างอิงไวยากรณ์
เอกสารนี้ให้ข้อมูลอ้างอิงไวยากรณ์ที่มีโครงสร้างและครอบคลุมสำหรับ Java ช่วยเสริมการอ้างอิง Java หลักโดยมุ่งเน้นไปที่รูปแบบไวยากรณ์ที่ละเอียดถี่ถ้วน ตารางตัวดำเนินการ และกลไกภายในของ JVM, OOP และการทำงานพร้อมกัน
---

## ตัวดำเนินการและนิพจน์
### ตัวดำเนินการทางคณิตศาสตร์
| ตัวดำเนินการ | ชื่อ | ตัวอย่าง | ผลลัพธ์ | หมายเหตุ |
|----------|-|---------|--------|-------|
| `+`| นอกจากนี้ | `3 + 2`| `5`| การต่อสตริงด้วย |
| `-`| การลบ | `3 - 2`| `1`| |
| `*`| การคูณ | `3 * 2`| `6`| |
| `/`| กอง | `7 / 2`| `3`| การหารจำนวนเต็มสำหรับ`int`; `3.5`สำหรับ`double`|
| `%`| ส่วนที่เหลือ | `7 % 2`| `1`| |
| `++`| เพิ่มขึ้น | `x++`/`++x`| | หลังและก่อนเพิ่ม |
| `--`| ลดลง | `x--`/`--x`| | หลังและก่อนการลดลง |
### การเปรียบเทียบและตัวดำเนินการเชิงตรรกะ
| ตัวดำเนินการ | ชื่อ | ตัวอย่าง | หมายเหตุ |
|----------|-|---------|-------|
| `==`| เท่ากับ | `x == y`| ความเท่าเทียมกันในการอ้างอิงสำหรับวัตถุ |
| `!=`| ไม่เท่ากัน | `x != y`| |
| `<`,`>`,`<=`,`>=`| เชิงสัมพันธ์ | `x >= y`| |
| `&&`| ตรรกะและ | `a && b`| ลัดวงจร |
| `\|\|`| ตรรกะหรือ | `a \|\| b`| ลัดวงจร |
| `!`| ตรรกะไม่ใช่ | `!true`| `false`|
| `instanceof`| พิมพ์ตรวจสอบ | `obj instanceof String`| การจับคู่รูปแบบด้วย (Java 16+) |
### ตัวดำเนินการ Bitwise
| ตัวดำเนินการ | ชื่อ | ตัวอย่าง | หมายเหตุ |
|----------|-|---------|-------|
| `&`| และ | `5 & 3`| `1`|
| `\|`| หรือ | `5 \| 3`| `7`|
| `^`| แฮคเกอร์ | `5 ^ 3`| `6`|
| `~`| ส่วนประกอบ | `~5`| `-6`|
| `<<`| เลื่อนซ้าย | `5 << 1`| `10`|
| `>>`| ลงนาม Shift ขวา | `-5 >> 1`| `-3`|
| `>>>`| Shift ขวาที่ไม่ได้ลงนาม | `-1 >>> 0`| `4294967295`|
### ลำดับความสำคัญของตัวดำเนินการ (สูงสุดไปต่ำสุด)
| ลำดับความสำคัญ | ตัวดำเนินการ |
|------------|-----------|
| 1 (สูงสุด) | โปรแกรมแก้ไขภายหลัง:`expr++``expr--` |
| 2 | อูนารี:`++expr``--expr``+expr``-expr``~``!` |
| 3 | นักแสดง:`(Type)expr`|
| 4 | การคูณ:`*``/``%`|
| 5 | สารเติมแต่ง:`+``-` |
| 6 | ชิฟต์:`<<``>>``>>>`|
| 7 | ความสัมพันธ์:`<``>``<=``>=``instanceof`|
| 8 | ความเท่าเทียมกัน:`==``!=` |
| 9 | ระดับบิตและ:`&`|
| 10 | XOR ระดับบิต:`^`|
| 11 | บิตหรือ:`\|`|
| 12 | ตรรกะและ:`&&`|
| 13 | ตรรกะ หรือ:`\|\|`|
| 14 | ประกอบไปด้วย:`? :`|
| 15 | การมอบหมาย:`=``+=``-=`ฯลฯ |
---

## การควบคุมการไหล
### แถลงการณ์แบบมีเงื่อนไข
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

### ลูป
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

## ฟังก์ชั่น (วิธีการ)
### ไวยากรณ์วิธีการ
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

### Lambdas และอินเทอร์เฟซการทำงาน
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

## การเขียนโปรแกรมเชิงวัตถุ
### คลาสและมรดก
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

## โครงสร้างข้อมูล
### กรอบคอลเลกชัน
| อินเตอร์เฟซ | การนำไปปฏิบัติ | สั่งซื้อ | ตัวแปรที่ปลอดภัยสำหรับเธรด |
|----------|----------------|---------|---------------------|
| `List`| `ArrayList`,`LinkedList`| ใช่ | `CopyOnWriteArrayList`|
| `Set`| `HashSet`,`TreeSet`,`LinkedHashSet`| ต่างกันไป | `CopyOnWriteArraySet`|
| `Map`| `HashMap`,`TreeMap`,`LinkedHashMap`| ต่างกันไป | `ConcurrentHashMap`|
| `Queue`| `ArrayDeque`,`PriorityQueue`| ต่างกันไป | `ConcurrentLinkedQueue`|
| `Deque`| `ArrayDeque`| ปลายทั้งสองข้าง | `ConcurrentLinkedDeque`|
### รายการ
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

### แผนที่
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

## ทั่วไป
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

## การจัดการข้อผิดพลาด
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

## เห็นพ้องต้องกัน
### เธรดและผู้บริหาร
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

### การซิงโครไนซ์
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

## โมดูลและแพ็คเกจ
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

## สรุป
ไวยากรณ์ของ Java มีการพัฒนาอย่างมากจากต้นกำเนิดในปี 1995 Java สมัยใหม่ (21+) มีฟีเจอร์บันทึก คลาสที่ปิดผนึก การจับคู่รูปแบบ เธรดเสมือน และเทมเพลตสตริง — ทำให้กระชับและแสดงออกได้มากกว่าที่เคย ไวยากรณ์หลักยังคงคุ้นเคย (เหมือน C, พิมพ์อย่างยิ่ง, อิงคลาส) แต่การเพิ่ม lambdas, Stream API และ`var`ได้ลดขนาดสำเร็จรูปลงอย่างมาก จุดแข็งของภาษาอยู่ที่ระบบนิเวศขนาดใหญ่ การรับประกันความเข้ากันได้แบบย้อนหลัง และการเพิ่มประสิทธิภาพการทำงานของ JVM ผ่านการรวบรวม JIT