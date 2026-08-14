---
# Metadata
title: "Java — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in Java that catch even experienced developers, with explanations and corrections."
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
# Java — よくある間違いとアンチパターン
このドキュメントには、Java で最も一般的な間違い、罠、およびアンチパターンがカタログ化されています。各エントリは、間違ったアプローチを示し、それが失敗する理由を説明し、正しい解決策を提供します。
---

## 1. オブジェクトの`equals()`と `==`
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

## 2. 反復中のコレクションの変更
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

## 3. リソースを閉じない (Try-with-Resources)
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

## 4. 整数オートボクシングの落とし穴
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

## 5. アンチパターン: 神クラス
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

## 6. ループ内の文字列連結
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

## 7. InterruptedException を処理しない
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

## 8. 空のコレクションの代わりに Null を返す
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

## 9. HashMap キーとしての可変オブジェクト
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

## 10. アンチパターン:`Exception`または`Throwable`をキャッチする
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

## 11.`equals`をオーバーライドするときに`hashCode`をオーバーライドしない
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

## 12. 二重チェックされたロックによる競合状態
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

＃＃ まとめ
Java の冗長性により、微妙なバグが隠れる可能性があります。`==`と`equals()`、同時変更、リソース リーク、オートボクシング パフォーマンス トラップ、equals/hashCode コントラクトなどです。最新の Java アプローチは、null セーフ比較に`Objects.equals()`を使用し、常に try-with-resources を使用し、null の代わりに空のコレクションを返し、特定の例外をキャッチし、単一責任の原則に従うことです。 Java 8 以降の機能 (ストリーム、オプション、メソッド参照) により、定型文が削減され、コードがより安全で表現力豊かになります。