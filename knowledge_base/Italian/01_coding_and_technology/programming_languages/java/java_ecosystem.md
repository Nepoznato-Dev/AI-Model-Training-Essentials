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
# Java: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, i framework e l'infrastruttura essenziali nell'ecosistema Java.
---

## Strumenti di creazione
| Strumento | Digitare | Ideale per |
|------|------|----------|
| **Maven** | Basato su XML | Enterprise, convenzione sulla configurazione |
| **Gradle** | Groovy/Kotlin DSL | Flessibile, Android, grandi progetti |
| **Formica** | Basato su XML | Progetti legacy |
| **Bazel** | Multilingue | Monorepos, su scala Google |
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

## Quadri
### Web/Impresa
| Quadro | Digitare | Ideale per |
|-----------|------|----------|
| **Stivale primaverile** | Stack completo | Impresa, microservizi |
| **Quarku** | Nativo del cloud | GraalVM, avvio veloce |
| **Micronauta** | AOT compilato | Memoria insufficiente, senza server |
| **Giacarta EE** | Norma | Standard Java aziendale |
| **Vert.x** | Reattivo | Concorrenza elevata |
| **Giavalin** | Leggero | App Web semplici |
### Ecosistema chiave della primavera
| Modulo | Scopo |
|--------|---------|
| **Web primaverile** | API REST, MVC |
| **Dati primaverili** | Accesso al database (JPA, MongoDB, Redis) |
| **Sicurezza di primavera** | Autenticazione, autorizzazione |
| **Nuvola di primavera** | Microservizi (configurazione, rilevamento, gateway) |
| **Lotto primaverile** | Elaborazione batch |
| **AMQP primaverile** | Code di messaggi |
---

## Test
| Quadro | Scopo |
|-----------|---------|
| **JUnità 5** | Quadro di prova standard |
| **Mockito** | Beffardo |
| **AffermareJ** | Affermazioni fluenti |
| **Contenitori di prova** | Test di integrazione basati su Docker |
| **WireMock** | Mocking API HTTP |
| **UnitàArch** | Prove di architettura |
| **RESTO ASSICURATO** | Test dell'API REST |
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

##Banca dati
| Tecnologia | Digitare |
|------------|------|
| **JDBC** | Accesso SQL di basso livello |
| **JPA / Ibernazione** | Norma ORM |
| **jOOQ** | Generatore SQL indipendente dai tipi |
| **Volo** | Migrazioni del database |
| **Liquibase** | Migrazioni del database |
| **HikariCP** | Pool di connessioni |
---

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **Stile di controllo** | Applicazione delle norme di codifica |
| **SpotBugs** | Rilevamento di modelli di bug |
| **PMD** | Analisi statica |
| **Pone a errori** | Plug-in del compilatore di Google |
| **SonarQube** | Piattaforma di qualità del codice |
| **JaCoCo** | Copertura del codice |
| **Immacolato** | Formattazione del codice |
| **Formato Java di Google** | Lo stile di Google |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **IDEA IntelliJ** | IDE Java dominante (Community + Ultimate) |
| **Eclissi** | Open source, ecosistema plug-in |
| **Codice VS** | Leggero con estensioni Java |
| **NetBeans** | Mantenuto da Apache |
---

## Distribuzione
| Metodo | Strumento |
|--------|------|
| **VASETTO** | `java -jar app.jar`|
| **GUERRA** | Distribuisci a Tomcat, Jetty |
| **GraalVM** | Compilazione di immagini native |
| **Docker** | Containerizzato (Eclipse Temurin, Amazon Corretto) |
| **Kubernetes** | Orchestrazione |
| **Server delle applicazioni** | WildFly, Tomcat, Jetty |
---

## Distribuzioni JDK
| Distribuzione | Fornitore |
|-------------|----------|
| **Temurin** | Eclipse/Adoptium (consigliato) |
| **Corretto** | Amazzonia |
| **Zulù** | Azul |
| **GraalVM** | Oracle (immagine nativa, poliglotta) |
| **Liberica** | BellSoft |
---

## Riepilogo
L'ecosistema Java è il più maturo nel campo dell'informatica aziendale. Lo stack standard è: **Gradle** o **Maven** per build, **Spring Boot** per Web/microservizi, **JUnit 5 + Mockito** per test, **Hibernate** per ORM, **IntelliJ IDEA** come IDE e **Docker** per la distribuzione. La forza di Java è il suo enorme ecosistema, il supporto aziendale e la compatibilità con le versioni precedenti. Java moderno (17+) con record, classi sigillate, corrispondenza di modelli e thread virtuali sta rivitalizzando il linguaggio.