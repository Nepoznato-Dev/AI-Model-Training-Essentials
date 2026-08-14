---
# Metadata
title: "Java — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern Java code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [java, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# জাভা — ইডিওম্যাটিক প্যাটার্নস এবং সর্বোত্তম অনুশীলন
এই নির্দেশিকাটি পরিচ্ছন্ন, আধুনিক জাভা (17+) কোড লেখার জন্য ইডিওম্যাটিক প্যাটার্ন এবং সর্বোত্তম অনুশীলনগুলি কভার করে।
---

## আধুনিক জাভা সিনট্যাক্স
```java
// ✅ var for local variables (when type is obvious)
var users = new ArrayList<User>();
var stream = Files.lines(path);
var response = client.send(request, BodyHandlers.ofString());

// ✅ Records for data carriers
public record User(String name, String email, int age) {}

var user = new User("Alice", "alice@example.com", 30);
var name = user.name();  // accessor, not getName()

// ✅ Sealed classes for restricted hierarchies
public sealed interface Shape permits Circle, Rectangle, Triangle {}
public record Circle(double radius) implements Shape {}
public record Rectangle(double width, double height) implements Shape {}

// ✅ Pattern matching (instanceof)
if (obj instanceof String s) {
    System.out.println(s.length());
}

// ✅ Switch expressions
String label = switch (status) {
    case ACTIVE   -> "Active";
    case INACTIVE -> "Inactive";
    case PENDING  -> "Pending Review";
};

// ✅ Text blocks
String json = """
        {
            "name": "Alice",
            "email": "alice@example.com"
        }
        """;
```

---

## সংগ্রহ ও প্রবাহ
```java
// ✅ Stream API for transformations
List<String> names = users.stream()
    .filter(User::isActive)
    .map(User::name)
    .sorted()
    .toList();  // Java 16+ immutable list

// ✅ Collectors
Map<Role, List<User>> byRole = users.stream()
    .collect(Collectors.groupingBy(User::role));

Set<String> uniqueNames = users.stream()
    .map(User::name)
    .collect(Collectors.toUnmodifiableSet());

// ✅ Optional patterns
Optional<User> user = repository.findById(id);
user.ifPresent(u -> sendEmail(u));
String name = user.map(User::name).orElse("Unknown");
User found = user.orElseThrow(() -> new NotFoundException("User " + id));

// ✅ Map operations
map.computeIfAbsent("key", k -> new ArrayList<>()).add("value");
map.merge("count", 1, Integer::sum);
```

---

## ত্রুটি হ্যান্ডলিং
```java
// ✅ Custom exceptions
public class ValidationException extends RuntimeException {
    private final String field;
    
    public ValidationException(String field, String message) {
        super(field + ": " + message);
        this.field = field;
    }
    
    public String field() { return field; }
}

// ✅ Try-with-resources
try (var conn = dataSource.getConnection();
     var stmt = conn.prepareStatement(sql);
     var rs = stmt.executeQuery()) {
    while (rs.next()) {
        // process
    }
}

// ✅ Catch specific exceptions
try {
    var result = service.process(data);
} catch (ValidationException e) {
    log.warn("Validation failed: {}", e.field());
} catch (DatabaseException e) {
    log.error("Database error", e);
    throw new ServiceException("Processing failed", e);
}
```

---

## ইন্টারফেস এবং ডিজাইন
```java
// ✅ Interface for abstraction
public interface UserRepository {
    Optional<User> findById(long id);
    List<User> findAll();
    User save(User user);
}

// ✅ Prefer composition over inheritance
public class UserService {
    private final UserRepository repository;
    private final EmailService emailService;
    
    public UserService(UserRepository repository, EmailService emailService) {
        this.repository = repository;
        this.emailService = emailService;
    }
}

// ✅ Builder pattern (or use Lombok)
public class Config {
    private final String host;
    private final int port;
    
    private Config(Builder builder) {
        this.host = builder.host;
        this.port = builder.port;
    }
    
    public static Builder builder() { return new Builder(); }
    
    public static class Builder {
        private String host = "localhost";
        private int port = 8080;
        
        public Builder host(String host) { this.host = host; return this; }
        public Builder port(int port) { this.port = port; return this; }
        public Config build() { return new Config(this); }
    }
}
```

---

## সামঞ্জস্য
```java
// ✅ Virtual threads (Java 21+)
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    IntStream.range(0, 10_000).forEach(i ->
        executor.submit(() -> {
            Thread.sleep(Duration.ofSeconds(1));
            return i;
        })
    );
}

// ✅ CompletableFuture
CompletableFuture<User> userFuture = CompletableFuture
    .supplyAsync(() -> userService.findById(id))
    .thenApply(user -> user.withLastSeen(Instant.now()));

// ✅ CompletableFuture composition
CompletableFuture<Dashboard> dashboard = CompletableFuture
    .allOf(usersFuture, ordersFuture, statsFuture)
    .thenApply(v -> new Dashboard(
        usersFuture.join(),
        ordersFuture.join(),
        statsFuture.join()
    ));

// ✅ Concurrent collections
ConcurrentHashMap<String, Integer> counters = new ConcurrentHashMap<>();
counters.merge("key", 1, Integer::sum);
```

---

## মডিউল এবং প্যাকেজ ডিজাইন
```java
// ✅ Package naming
com.example.userservice
com.example.userservice.domain
com.example.userservice.repository
com.example.userservice.service

// ✅ Module system (Java 9+)
module com.example.userservice {
    requires java.sql;
    requires com.example.common;
    
    exports com.example.userservice.service;
    exports com.example.userservice.domain;
}

// ✅ Package-private by default
class InternalHelper { }  // not public
```

---

## পরীক্ষা
```java
// ✅ JUnit 5 + AssertJ
@Test
void shouldFindUserById() {
    // given
    when(repository.findById(1L)).thenReturn(Optional.of(new User("Alice")));
    
    // when
    var user = service.findById(1L);
    
    // then
    assertThat(user.name()).isEqualTo("Alice");
}

// ✅ Parameterized tests
@ParameterizedTest
@ValueSource(strings = {"Alice", "Bob", "Charlie"})
void shouldAcceptValidNames(String name) {
    assertThatCode(() -> service.validate(name))
        .doesNotThrowAnyException();
}
```

---

## সারাংশ
আধুনিক জাভা ইডিয়মগুলি জোর দেয়: ডেটার জন্য রেকর্ড, শ্রেণিবিন্যাসগুলির জন্য সিল করা ক্লাস, প্যাটার্ন ম্যাচিং, সুইচ এক্সপ্রেশন, টেক্সট ব্লক, সংগ্রহ প্রক্রিয়াকরণের জন্য স্ট্রীম, অনুপস্থিতির জন্য ঐচ্ছিক, পরিচ্ছন্নতার জন্য সম্পদের সাথে চেষ্টা করুন, একযোগে ভার্চুয়াল থ্রেড এবং নির্ভরতা ইনজেকশন। গুগল জাভা স্টাইল গাইড অনুসরণ করুন, ফর্ম্যাটিংয়ের জন্য`javafmt`বা`Spotless`এবং লিন্টিংয়ের জন্য ত্রুটি প্রবণ বা চেকস্টাইল ব্যবহার করুন। রেকর্ড, সিল করা ক্লাস, প্যাটার্ন ম্যাচিং এবং ভার্চুয়াল থ্রেড সহ আধুনিক জাভা (17-21+) সংক্ষিপ্ত এবং অভিব্যক্তিপূর্ণ — নতুন বৈশিষ্ট্যগুলিকে আলিঙ্গন করুন।