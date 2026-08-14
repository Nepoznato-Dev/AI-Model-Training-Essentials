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
# Java — Các mẫu thành ngữ & các phương pháp hay nhất
Hướng dẫn này bao gồm các mẫu thành ngữ và các phương pháp hay nhất để viết mã Java (17+) hiện đại, rõ ràng.
---

## Cú pháp Java hiện đại
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

## Bộ sưu tập & Luồng
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

## Xử lý lỗi
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

## Giao diện & Thiết kế
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

## Đồng thời
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

## Thiết kế mô-đun & gói
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

##Thử nghiệm
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

## Bản tóm tắt
Các thành ngữ Java hiện đại nhấn mạnh: bản ghi dữ liệu, các lớp được niêm phong cho hệ thống phân cấp, khớp mẫu, biểu thức chuyển đổi, khối văn bản, luồng để xử lý bộ sưu tập, Tùy chọn khi vắng mặt, dùng thử tài nguyên để dọn dẹp, các luồng ảo để chạy đồng thời và chèn phụ thuộc. Làm theo Hướng dẫn về phong cách Java của Google, sử dụng`javafmt`hoặc`Spotless`để định dạng và Dễ bị lỗi hoặc Kiểu kiểm tra để tìm lỗi mã. Java hiện đại (17-21+) với các bản ghi, các lớp kín, khớp mẫu và các luồng ảo rất ngắn gọn và mang tính biểu cảm — nắm bắt các tính năng mới.