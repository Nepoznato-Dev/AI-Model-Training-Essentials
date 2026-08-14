<!--
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

-->
# Java — Modèles idiomatiques et meilleures pratiques
Ce guide couvre les modèles idiomatiques et les meilleures pratiques pour écrire du code Java (17+) propre et moderne.
---

## Syntaxe Java moderne
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

## Collections et flux
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

## Gestion des erreurs
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

##Interfaces et conception
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

## Concurrence
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

## Conception de modules et de packages
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

## Tests
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

## Résumé
Les idiomes Java modernes mettent l'accent sur : les enregistrements pour les données, les classes scellées pour les hiérarchies, la correspondance de modèles, les expressions de commutation, les blocs de texte, les flux pour le traitement de la collection, facultatif pour l'absence, l'essai avec les ressources pour le nettoyage, les threads virtuels pour la concurrence et l'injection de dépendances. Suivez le guide de style Google Java, utilisez`javafmt`ou`Spotless`pour le formatage et Error Prone ou Checkstyle pour le peluchage. Java moderne (17-21+) avec des enregistrements, des classes scellées, une correspondance de modèles et des threads virtuels est concis et expressif : adoptez les nouvelles fonctionnalités.