---
# Metadata
title: "Java — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern Java code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Java — 慣用模式與最佳實踐
本指南涵蓋了編寫乾淨、現代 Java (17+) 程式碼的慣用模式和最佳實務。
---

## 現代 Java 語法
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

## 集合和串流
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

## 錯誤處理
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

## 介面與設計
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

## 並行
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

## 模組和封裝設計
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

## 測試
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

＃＃ 概括
現代Java慣用語強調：資料記錄、層次結構密封類別、模式匹配、開關表達式、文字區塊、集合處理流程、可選缺席、try-with-resources清理、虛擬執行緒並發和依賴注入。遵循 Google Java 樣式指南，使用`javafmt`或`Spotless`進行格式化，並使用 Error Prone 或 Checkstyle 進行 linting。現代 Java (17-21+) 具有記錄、密封類別、模式匹配和虛擬線程，簡潔且富有表現力 — 擁抱新功能。