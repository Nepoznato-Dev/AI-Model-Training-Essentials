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
# Java – Erros comuns e antipadrões
Este documento cataloga os erros, armadilhas e antipadrões mais comuns em Java. Cada entrada mostra a abordagem incorreta, explica por que ela falha e fornece a solução correta.
---

## 1.`equals()`vs`==`para objetos
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

## 2. Modificando uma coleção durante a iteração
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

## 3. Não fechar recursos (tentar com recursos)
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

## 4. Armadilhas do Autoboxing Inteiro
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

## 5. Antipadrão: Classes de Deus
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

## 6. Concatenação de Strings em Loops
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

## 7. Não tratando InterruptedException
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

## 8. Retornando nulos em vez de coleções vazias
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

## 9. Objetos mutáveis ​​como chaves HashMap
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

## 10. Antipadrão: Capturando`Exception`ou `Throwable`
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

## 11. Não substituindo`hashCode`ao substituir `equals`
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

## 12. Condições de corrida com bloqueio verificado duas vezes
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

## Resumo
A verbosidade do Java pode ocultar bugs sutis:`==`vs`equals()`, modificação simultânea, vazamentos de recursos, armadilhas de desempenho de autoboxing e o contrato equals/hashCode. A abordagem Java moderna é: usar`Objects.equals()`para comparação segura de nulos, sempre usar try-with-resources, retornar coleções vazias em vez de nulas, capturar exceções específicas e seguir o princípio de responsabilidade única. Os recursos do Java 8+ (fluxos, opcionais, referências de métodos) reduzem o clichê e tornam o código mais seguro e expressivo.