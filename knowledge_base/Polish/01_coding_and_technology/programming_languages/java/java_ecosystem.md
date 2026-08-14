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
# Java — przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, frameworki i infrastrukturę w ekosystemie Java.
---

## Narzędzia do tworzenia
| Narzędzie | Wpisz | Najlepsze dla |
|------|------|--------------|
| **Maven** | oparty na XML | Przedsiębiorstwo, konwencja dotycząca konfiguracji |
| **Stopnie** | Groovy/Kotlin DSL | Elastyczny, Android, duże projekty |
| **Mrówka** | oparty na XML | Starsze projekty |
| **Bazel** | Wielojęzyczny | Monorepos, skala Google |
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

## Ramy
### Sieć / przedsiębiorstwo
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **Wiosenny but** | Pełny stos | Przedsiębiorstwo, mikrousługi |
| **Kwarkus** | Natywny w chmurze | GraalVM, szybkie uruchamianie |
| **Mikronauta** | AOT skompilowany | Mało pamięci, bez serwera |
| **Dżakarta,EE** | Standardowe | Standard Java dla przedsiębiorstw |
| **Pion.x** | Reaktywny | Wysoka współbieżność |
| **Javalin** | Lekki | Proste aplikacje internetowe |
### Ekosystem Key Spring
| Moduł | Cel |
|------------|--------|
| **Wiosenna sieć** | API REST, MVC |
| **Dane wiosenne** | Dostęp do baz danych (JPA, MongoDB, Redis) |
| **Wiosenna ochrona** | Uwierzytelnianie, autoryzacja |
| **Wiosenna Chmura** | Mikrousługi (konfiguracja, wykrywanie, brama) |
| **Wiosenna partia** | Przetwarzanie wsadowe |
| **Wiosenny AMQP** | Kolejki wiadomości |
---

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **Jednostka 5** | Standardowe ramy testów |
| **Mockito** | Kpiąco |
| **TwierdźJ** | Płynne twierdzenia |
| **Kontenery testowe** | Testy integracyjne oparte na Dockerze |
| **WireMock** | Wyśmiewanie API HTTP |
| **ArchUnit** | Testy architektury |
| **Odpoczywaj ** | Testowanie API REST |
| **JMH** | Mikrobenchmarking |
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

## Baza danych
| Technologia | Wpisz |
|------------|------|
| **JDBC** | Dostęp SQL niskiego poziomu |
| **JPA / Hibernacja** | standard ORM |
| **jOOQ** | Konstruktor SQL z bezpiecznym typem |
| **Trasa przelotowa** | Migracje baz danych |
| **Likwibaza** | Migracje baz danych |
| **HikariCP** | Pula połączeń |
---

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **Styl sprawdzania** | Egzekwowanie standardów kodowania |
| **SpotBug** | Wykrywanie wzorców błędów |
| **PMD** | Analiza statyczna |
| **Podatne na błędy** | Wtyczka kompilatora Google |
| **SonarQube** | Platforma jakości kodu |
| **JaCoCo** | Pokrycie kodu |
| **Bez skazy** | Formatowanie kodu |
| **Format Google Java** | Styl Google |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Pomysł IntelliJ** | Dominujące środowisko Java IDE (Społeczność + Ultimate) |
| **Zaćmienie** | Open source, ekosystem wtyczek |
| **Kod VS** | Lekki z rozszerzeniami Java |
| **NetBeans** | Utrzymywany przez Apache |
---

## Zastosowanie
| Metoda | Narzędzie |
|------------|------|
| **SŁOIK** | `java -jar app.jar`|
| **WOJNA** | Wdróż w Tomcat, Jetty |
| **GraalVM** | Natywna kompilacja obrazów |
| **Doker** | Kontenerowe (Eclipse Temurin, Amazon Corretto) |
| **Kubernetes** | Orkiestracja |
| **Serwery aplikacji** | WildFly, Tomcat, Molo |
---

## Dystrybucje JDK
| Dystrybucja | Dostawca |
|------------|---------|
| **Temuryn** | Zaćmienie/Adopcja (zalecane) |
| **Korekta** | Amazonka |
| **Zulus** | Azul |
| **GraalVM** | Oracle (obraz natywny, poliglota) |
| **Liberyka** | BellSoft |
---

## Streszczenie
Ekosystem Java jest najbardziej dojrzały w informatyce korporacyjnej. Standardowy stos to: **Gradle** lub **Maven** do kompilacji, **Spring Boot** do sieci/mikroserwisów, **JUnit 5 + Mockito** do testowania, **Hibernate** do ORM, **IntelliJ IDEA** jako IDE i **Docker** do wdrożenia. Siłą Java jest jej ogromny ekosystem, wsparcie dla przedsiębiorstw i kompatybilność wsteczna. Nowoczesna Java (17+) z rekordami, zapieczętowanymi klasami, dopasowywaniem wzorców i wirtualnymi wątkami ożywia język.