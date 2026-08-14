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
# Java — 慣用的なパターンとベストプラクティス
このガイドでは、クリーンで最新の Java (17 以降) コードを作成するための慣用的なパターンとベスト プラクティスについて説明します。
---

## 最新の Java 構文
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

## コレクションとストリーム
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

## エラー処理
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

## インターフェースとデザイン
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

## 同時実行性
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

## モジュールとパッケージの設計
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

## テスト
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

＃＃ まとめ
最新の Java イディオムは、データのレコード、階層のシールされたクラス、パターン マッチング、switch 式、テキスト ブロック、コレクション処理のストリーム、不在のオプション、クリーンアップの try-with-resources、同時実行の仮想スレッド、および依存関係の注入を強調します。 Google Java スタイル ガイドに従い、書式設定には`javafmt`または`Spotless`を使用し、lint には Error Prone または Checkstyle を使用します。レコード、シールされたクラス、パターン マッチング、仮想スレッドを備えた最新の Java (17 ～ 21+) は、簡潔かつ表現力豊かで、新しい機能を取り入れています。