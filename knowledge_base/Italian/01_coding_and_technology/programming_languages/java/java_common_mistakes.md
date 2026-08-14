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

# Java: errori comuni e anti-pattern
Questo documento cataloga gli errori, le trappole e gli anti-pattern più comuni in Java. Ogni voce mostra l'approccio errato, spiega perché fallisce e fornisce la soluzione corretta.
---

## 1.`equals()`vs`==`per Oggetti
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

## 2. Modifica di una raccolta durante l'iterazione
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

## 3. Non chiudere le risorse (Try-with-Resources)
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

## 4. Insidie ​​​​dell'autoboxing intero
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

## 5. Anti-modello: classi di Dio
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

## 6. Concatenazione di stringhe nei loop
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

## 7. Non gestire l'eccezione Interrupted
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

## 8. Restituzione di valori nulli anziché di raccolte vuote
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

## 9. Oggetti mutabili come chiavi HashMap
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

## 10. Anti-pattern: catturare`Exception`o `Throwable`
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

## 11. Non sovrascrivere`hashCode`quando si sovrascrive `equals`
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

## 12. Condizioni di gara con bloccaggio a doppio controllo
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

## Riepilogo
La verbosità di Java può nascondere bug sottili:`==`vs`equals()`, modifiche simultanee, perdite di risorse, trappole delle prestazioni di autoboxing e il contratto equals/hashCode. L'approccio Java moderno è: utilizzare`Objects.equals()`per il confronto null-safe, utilizzare sempre try-with-resources, restituire raccolte vuote anziché null, rilevare eccezioni specifiche e seguire il principio di responsabilità unica. Le funzionalità Java 8+ (flussi, facoltativi, riferimenti ai metodi) riducono il boilerplate rendendo il codice più sicuro ed espressivo.