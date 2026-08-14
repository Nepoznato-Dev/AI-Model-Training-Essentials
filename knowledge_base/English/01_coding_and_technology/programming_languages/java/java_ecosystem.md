<!--
---
# Metadata
title: "Java — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Java ecosystem including build tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [java, ecosystem, tooling, maven, gradle, spring, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Java — Ecosystem & Tooling Guide

This guide covers the essential tools, frameworks, and infrastructure in the Java ecosystem.

---

## Build Tools

| Tool | Type | Best For |
|------|------|----------|
| **Maven** | XML-based | Enterprise, convention over config |
| **Gradle** | Groovy/Kotlin DSL | Flexible, Android, large projects |
| **Ant** | XML-based | Legacy projects |
| **Bazel** | Multi-language | Monorepos, Google-scale |

```bash
# Maven
mvn clean install               # build
mvn test                        # run tests
mvn package                     # create JAR/WAR

# Gradle
./gradlew build                 # build
./gradlew test                  # run tests
./gradlew bootRun               # run Spring Boot app
```

---

## Frameworks

### Web / Enterprise

| Framework | Type | Best For |
|-----------|------|----------|
| **Spring Boot** | Full-stack | Enterprise, microservices |
| **Quarkus** | Cloud-native | GraalVM, fast startup |
| **Micronaut** | AOT compiled | Low memory, serverless |
| **Jakarta EE** | Standard | Enterprise Java standard |
| **Vert.x** | Reactive | High-concurrency |
| **Javalin** | Lightweight | Simple web apps |

### Key Spring Ecosystem

| Module | Purpose |
|--------|---------|
| **Spring Web** | REST APIs, MVC |
| **Spring Data** | Database access (JPA, MongoDB, Redis) |
| **Spring Security** | Authentication, authorization |
| **Spring Cloud** | Microservices (config, discovery, gateway) |
| **Spring Batch** | Batch processing |
| **Spring AMQP** | Message queues |

---

## Testing

| Framework | Purpose |
|-----------|---------|
| **JUnit 5** | Standard test framework |
| **Mockito** | Mocking |
| **AssertJ** | Fluent assertions |
| **Testcontainers** | Docker-based integration tests |
| **WireMock** | HTTP API mocking |
| **ArchUnit** | Architecture tests |
| **REST Assured** | REST API testing |
| **JMH** | Microbenchmarking |

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    @Mock UserRepository repo;
    @InjectMocks UserService service;

    @Test
    void shouldFindUserById() {
        when(repo.findById(1L)).thenReturn(Optional.of(new User("Alice")));
        var user = service.findById(1L);
        assertThat(user.name()).isEqualTo("Alice");
    }
}
```

---

## Database

| Technology | Type |
|------------|------|
| **JDBC** | Low-level SQL access |
| **JPA / Hibernate** | ORM standard |
| **jOOQ** | Type-safe SQL builder |
| **Flyway** | Database migrations |
| **Liquibase** | Database migrations |
| **HikariCP** | Connection pool |

---

## Code Quality

| Tool | Purpose |
|------|---------|
| **Checkstyle** | Coding standard enforcement |
| **SpotBugs** | Bug pattern detection |
| **PMD** | Static analysis |
| **Error Prone** | Google's compiler plugin |
| **SonarQube** | Code quality platform |
| **JaCoCo** | Code coverage |
| **Spotless** | Code formatting |
| **Google Java Format** | Google's style |

---

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **IntelliJ IDEA** | Dominant Java IDE (Community + Ultimate) |
| **Eclipse** | Open source, plugin ecosystem |
| **VS Code** | Lightweight with Java extensions |
| **NetBeans** | Apache-maintained |

---

## Deployment

| Method | Tool |
|--------|------|
| **JAR** | `java -jar app.jar` |
| **WAR** | Deploy to Tomcat, Jetty |
| **GraalVM** | Native image compilation |
| **Docker** | Containerized (Eclipse Temurin, Amazon Corretto) |
| **Kubernetes** | Orchestration |
| **App Servers** | WildFly, Tomcat, Jetty |

---

## JDK Distributions

| Distribution | Provider |
|-------------|----------|
| **Temurin** | Eclipse/Adoptium (recommended) |
| **Corretto** | Amazon |
| **Zulu** | Azul |
| **GraalVM** | Oracle (native image, polyglot) |
| **Liberica** | BellSoft |

---

## Summary

Java's ecosystem is the most mature in enterprise computing. The standard stack is: **Gradle** or **Maven** for builds, **Spring Boot** for web/microservices, **JUnit 5 + Mockito** for testing, **Hibernate** for ORM, **IntelliJ IDEA** as IDE, and **Docker** for deployment. Java's strength is its massive ecosystem, enterprise support, and backwards compatibility. Modern Java (17+) with records, sealed classes, pattern matching, and virtual threads is revitalizing the language.
