---
# Metadata
title: "Java — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in Java that catch even experienced developers, with explanations and corrections."
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
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [java, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Java — 常見錯誤與反模式
本文檔列出了 Java 中最常見的錯誤、陷阱和反模式。每個條目都會顯示錯誤的方法，解釋其失敗的原因，並提供正確的解決方案。
---

## 1. 物件的`equals()`與 `==`
```java
// ❌ WRONG — == compares references, not values
String a = new String("hello");
String b = new String("hello");
a == b        // false — different objects
a.equals(b)   // true — same content

// ❌ WRONG — NullPointerException if a is null
a.equals(b)   // throws NPE if a is null

// ✅ CORRECT — use Objects.equals()
Objects.equals(a, b)  // null-safe

// ✅ CORRECT — constant on left
"hello".equals(a)  // never throws NPE
```

---

## 2. 在迭代期間修改集合
```java
// ❌ WRONG — ConcurrentModificationException
List<String> list = new ArrayList<>(Arrays.asList("a", "b", "c"));
for (String item : list) {
    if ("b".equals(item)) {
        list.remove(item);  // throws ConcurrentModificationException
    }
}

// ✅ CORRECT — use Iterator.remove()
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    if ("b".equals(it.next())) {
        it.remove();
    }
}

// ✅ CORRECT — use removeIf (Java 8+)
list.removeIf(item -> "b".equals(item));
```

---

## 3. 不關閉資源（Try-with-Resources）
```java
// ❌ WRONG — resource leak on exception
BufferedReader reader = new BufferedReader(new FileReader("data.txt"));
String line = reader.readLine();
reader.close();  // never reached if readLine() throws

// ✅ CORRECT — try-with-resources (Java 7+)
try (BufferedReader reader = new BufferedReader(new FileReader("data.txt"))) {
    String line = reader.readLine();
}  // automatically closed, even on exception
```

---

## 4. 整數自動裝箱陷阱
```java
// ❌ WRONG — autoboxing creates Integer objects
Integer a = 128;
Integer b = 128;
a == b  // false! (Integer cache is -128 to 127)
a.equals(b)  // true

// ❌ WRONG — autoboxing in loops (performance)
int[] numbers = {1, 2, 3, 4, 5};
List<Integer> list = new ArrayList<>();
for (int n : numbers) {
    list.add(n);  // autoboxes each int → Integer
}

// ✅ CORRECT — use IntStream for primitives
IntStream.of(1, 2, 3, 4, 5).sum();
```

---

## 5. 反模式：上帝類
```java
// ❌ WRONG — class doing everything
public class UserManager {
    public void createUser(...) { ... }
    public void sendEmail(...) { ... }
    public void generateReport(...) { ... }
    public void connectToDatabase(...) { ... }
    public void processPayment(...) { ... }
}

// ✅ CORRECT — single responsibility principle
public class UserService {
    public void createUser(...) { ... }
}
public class EmailService {
    public void sendEmail(...) { ... }
}
public class ReportGenerator {
    public void generateReport(...) { ... }
}
```

---

## 6. 循環中的字串連接
```java
// ❌ WRONG — creates new String object each iteration
String result = "";
for (String word : words) {
    result += word + " ";  // O(n²) — very slow for large lists
}

// ✅ CORRECT — use StringBuilder
StringBuilder sb = new StringBuilder();
for (String word : words) {
    sb.append(word).append(" ");
}
String result = sb.toString();

// ✅ CORRECT — use String.join()
String result = String.join(" ", words);
```

---

## 7. 不處理 InterruptedException
```java
// ❌ WRONG — swallowing interrupt
try {
    Thread.sleep(1000);
} catch (InterruptedException e) {
    // ignored! Thread interrupt status is lost
}

// ✅ CORRECT — restore interrupt status
try {
    Thread.sleep(1000);
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();  // restore interrupt flag
    throw new RuntimeException("Interrupted", e);
}
```

---

## 8. 傳回 Null 而不是空集合
```java
// ❌ WRONG — forces null checks on callers
public List<User> getUsers() {
    List<User> users = findUsers();
    if (users == null) {
        return null;  // caller must check for null
    }
    return users;
}

// ✅ CORRECT — return empty collection
public List<User> getUsers() {
    List<User> users = findUsers();
    if (users == null) {
        return Collections.emptyList();
    }
    return users;
}
```

---

## 9. 可變物件作為 HashMap 鍵
```java
// ❌ WRONG — modifying key after insertion
class Key {
    String name;
    int hash;
    // equals/hashCode based on name
}

Map<Key, String> map = new HashMap<>();
Key k = new Key("original");
map.put(k, "value");
k.name = "modified";  // breaks the map! get() won't find it
```

---

## 10. 反模式：捕捉`Exception`或 `Throwable`
```java
// ❌ WRONG — catches everything including Errors
try {
    doSomething();
} catch (Exception e) {
    // catches NullPointerException, IOException, etc.
    // also catches things you shouldn't catch
}

// ❌ WORSE — catches OutOfMemoryError, StackOverflowError
try {
    doSomething();
} catch (Throwable t) {
    // NEVER do this
}

// ✅ CORRECT — catch specific exceptions
try {
    doSomething();
} catch (IOException e) {
    logger.error("IO error", e);
} catch (SQLException e) {
    logger.error("Database error", e);
}
```

---

## 11. 覆蓋`equals`時不覆寫 `hashCode`
```java
// ❌ WRONG — breaks HashMap/HashSet contract
class User {
    String name;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof User)) return false;
        return name.equals(((User) o).name);
    }
    // Missing hashCode() — equal objects have different hash codes!
}

// ✅ CORRECT — always override both
@Override
public int hashCode() {
    return Objects.hash(name);
}
```

---

## 12. 雙重檢查鎖定的競爭條件
```java
// ❌ WRONG — broken without volatile (pre-Java 5)
private static Singleton instance;

public static Singleton getInstance() {
    if (instance == null) {
        synchronized (Singleton.class) {
            if (instance == null) {
                instance = new Singleton();  // not safe without volatile
            }
        }
    }
    return instance;
}

// ✅ CORRECT — use volatile or enum
private static volatile Singleton instance;

// ✅ BEST — use enum (thread-safe by design)
public enum Singleton {
    INSTANCE;
}
```

---

＃＃ 概括
Java 的冗長可以隱藏微妙的錯誤：`==`與`equals()`、並發修改、資源洩漏、自動裝箱性能陷阱以及 equals/hashCode 契約。現代Java方法是：使用`Objects.equals()`進行空安全比較，始終使用try-with-resources，返回空集合而不是null，捕獲特定異常，並遵循單一責任原則。 Java 8+ 功能（串流、可選、方法引用）減少了樣板文件，同時使程式碼更安全、更具表現力。