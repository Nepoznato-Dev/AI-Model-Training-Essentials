<!--
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

-->
# जावा - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ जावा में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है। प्रत्येक प्रविष्टि गलत दृष्टिकोण दिखाती है, बताती है कि यह विफल क्यों होता है, और सही समाधान प्रदान करती है।
---

## 1. वस्तुओं के लिए`equals()`बनाम `==`
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

## 2. पुनरावृत्ति के दौरान संग्रह को संशोधित करना
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

## 3. संसाधनों को बंद न करना (संसाधनों के साथ प्रयास करें)
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

## 4. पूर्णांक ऑटोबॉक्सिंग नुकसान
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

## 5. विरोधी प्रतिमान: ईश्वर वर्ग
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

## 6. लूप्स में स्ट्रिंग कॉन्सटेनेशन
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

## 7. InterptedException को हैंडल नहीं करना
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

## 8. खाली संग्रह के बजाय शून्य लौटना
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

## 9. हैशमैप कुंजी के रूप में परिवर्तनशील वस्तुएं
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

## 10. एंटी-पैटर्न:`Exception`या`Throwable`को पकड़ना
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

## 11.`equals`को ओवरराइड करते समय`hashCode`को ओवरराइड नहीं करना
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

## 12. डबल-चेक लॉकिंग के साथ रेस की स्थिति
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

## सारांश
जावा की वर्बोसिटी सूक्ष्म बग को छिपा सकती है:`==`बनाम `equals()`, समवर्ती संशोधन, संसाधन लीक, ऑटोबॉक्सिंग प्रदर्शन जाल, और बराबर/हैशकोड अनुबंध। आधुनिक जावा दृष्टिकोण है: शून्य-सुरक्षित तुलना के लिए`Objects.equals()`का उपयोग करें, हमेशा संसाधनों के साथ प्रयास करें का उपयोग करें, शून्य के बजाय खाली संग्रह लौटाएं, विशिष्ट अपवाद पकड़ें, और एकल जिम्मेदारी सिद्धांत का पालन करें। जावा 8+ सुविधाएँ (स्ट्रीम, वैकल्पिक, विधि संदर्भ) कोड को सुरक्षित और अधिक अभिव्यंजक बनाते हुए बॉयलरप्लेट को कम करती हैं।