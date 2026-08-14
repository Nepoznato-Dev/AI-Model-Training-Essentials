<!--
---
# Metadata
title: "Java"
description: "Comprehensive reference for the Java programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [java, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Java
Java est un langage de programmation orienté objet à typage statique créé par James Gosling chez Sun Microsystems et publié en 1995. Sa philosophie de conception — « écrire une fois, exécuter n'importe où » (WORA) — est réalisée grâce à la machine virtuelle Java (JVM), qui permet au code Java compilé de s'exécuter sur n'importe quelle plate-forme dotée d'une implémentation JVM. Java est l'un des langages de programmation les plus utilisés de l'histoire, alimentant les backends d'entreprise, les applications Android, les systèmes Big Data et les services financiers.
Bien qu'il ait près de 30 ans, Java continue d'évoluer. Java moderne (versions 17+) comprend des enregistrements, des classes scellées, une correspondance de modèles, des threads virtuels et un écosystème croissant qui rivalise avec les langages plus récents.
---

## Pourquoi Java est important
- **Norme d'entreprise** : l'épine dorsale des backends Fortune 500 : banque, assurance, e-commerce, soins de santé.
- **Développement Android** : le langage principal pour Android (aux côtés de Kotlin).
- **Écosystème Big data** : Apache Hadoop, Spark, Kafka, Elasticsearch — tous écrits en Java ou Scala (qui s'exécute sur la JVM).
- **Écosystème massif** : plus de 500 000 bibliothèques sur Maven Central ; un outillage mature pour chaque besoin.
- **Performances** : le compilateur JIT de JVM produit un code machine hautement optimisé au moment de l'exécution, correspondant souvent au C++ pour les applications de longue durée.
- **Compatibilité ascendante** : le code écrit pour Java 1.0 (1996) fonctionne toujours sur les JVM modernes.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Verbosité** | Nécessite plus de passe-partout que Python, Kotlin ou Go | Utilisez Lombok, les enregistrements (Java 16+) et les IDE modernes |
| **Utilisation de la mémoire** | La surcharge de la JVM signifie une mémoire de base plus élevée | Ajustez les indicateurs JVM ; utiliser les images natives GraalVM pour les petits déploiements |
| **Heure de démarrage** | Le préchauffage de la JVM peut être lent pour les processus de courte durée | Image native GraalVM, ou utilisez C/Go pour les outils CLI |
| **Exceptions vérifiées** | Force la gestion des exceptions qui pourraient ne pas être récupérables | Utilisez des exceptions non vérifiées ou le modèle`Optional`|
| **Aucun type de valeur** | Tout est objet (jusqu'au projet Valhalla) | Utiliser des collections spécialisées en primitives (Eclipse Collections, Trove) |
---

## Fondamentaux de la syntaxe
### Structure de base
Java est basé sur les classes : tout vit dans une classe. Le nom de fichier doit correspondre au nom de la classe publique.
```java
// HelloWorld.java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        
        String name = "Alice";
        int age = 30;
        double score = 9.5;
        boolean active = true;
        
        String greeting = String.format("Hello, %s! You are %d years old.", name, age);
        System.out.println(greeting);
    }
}
```

### Programmation orientée objet
```java
public abstract class Animal {
    private final String name;
    
    protected Animal(String name) { this.name = name; }
    public String getName() { return name; }
    public abstract String speak();
}

public class Dog extends Animal {
    public Dog(String name) { super(name); }
    
    @Override
    public String speak() { return getName() + " says woof"; }
}

public interface Serializable {
    String toJson();
}

public class User implements Serializable, Comparable<User> {
    private final String name;
    private final int age;
    
    public User(String name, int age) { this.name = name; this.age = age; }
    
    @Override
    public String toJson() { return "{\"name\":\"" + name + "\",\"age\":" + age + "}"; }
    
    @Override
    public int compareTo(User other) { return Integer.compare(this.age, other.age); }
}
```

### Records (Java 16+) — Classes de données concises
```java
public record Point(double x, double y) {
    public Point {
        if (Double.isNaN(x) || Double.isNaN(y)) {
            throw new IllegalArgumentException("Coordinates cannot be NaN");
        }
    }
    
    public double distanceTo(Point other) {
        return Math.sqrt(Math.pow(x - other.x, 2) + Math.pow(y - other.y, 2));
    }
}

Point p1 = new Point(3.0, 4.0);
Point p2 = new Point(0.0, 0.0);
System.out.println(p1.distanceTo(p2));  // 5.0
```

### Collections et flux
```java
import java.util.*;
import java.util.stream.*;

List<String> names = new ArrayList<>(List.of("Alice", "Bob", "Charlie"));

// Stream API — functional-style data processing
List<String> filtered = names.stream()
    .filter(name -> name.length() > 3)
    .map(String::toUpperCase)
    .sorted()
    .collect(Collectors.toList());

// Grouping
Map<Integer, List<String>> byLength = names.stream()
    .collect(Collectors.groupingBy(String::length));

// Optional — avoid null pointer exceptions
Optional<String> findUser(String name) {
    return Optional.ofNullable(userDatabase.get(name));
}
```

### Gestion des exceptions
```java
public void readFile(String path) throws IOException {
    try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
    }
}

public class InsufficientFundsException extends Exception {
    private final double balance;
    private final double amount;
    
    public InsufficientFundsException(double balance, double amount) {
        super(String.format("Cannot withdraw $%.2f from $%.2f", amount, balance));
        this.balance = balance;
        this.amount = amount;
    }
}
```

---

## Syntaxe et modèles avancés
### Génériques
```java
// Generic class
public class Box<T> {
    private T value;
    
    public Box(T value) { this.value = value; }
    public T get() { return value; }
    public <U> Box<U> map(Function<T, U> mapper) {
        return new Box<>(mapper.apply(value));
    }
}

// Bounded type parameters
public <T extends Comparable<T>> T findMax(List<T> items) {
    return items.stream().reduce(items.get(0), (a, b) -> a.compareTo(b) >= 0 ? a : b);
}

// Wildcards
public static void printAll(List<?> items) {
    items.forEach(System.out::println);
}

// Generic method with multiple bounds
public <T extends Serializable & Comparable<T>> void store(T item) {
    // T must implement both Serializable and Comparable
}
```

### Classes scellées et correspondance de modèles (Java 17+)
```java
// Sealed classes — restrict which classes can extend
public sealed interface Shape permits Circle, Rectangle, Triangle {}

public record Circle(double radius) implements Shape {}
public record Rectangle(double width, double height) implements Shape {}
public record Triangle(double base, double height) implements Shape {}

// Pattern matching with switch (Java 21+)
public static double area(Shape shape) {
    return switch (shape) {
        case Circle c    -> Math.PI * c.radius() * c.radius();
        case Rectangle r -> r.width() * r.height();
        case Triangle t  -> 0.5 * t.base() * t.height();
    };
}

// Pattern matching for instanceof (Java 16+)
if (obj instanceof String s) {
    System.out.println("String of length: " + s.length());
}
```

### Annotations
```java
// Custom annotation
import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Retry {
    int maxAttempts() default 3;
    long delayMs() default 1000;
}

// Using the annotation
@Retry(maxAttempts = 5, delayMs = 500)
public void connectToDatabase() throws Exception {
    // Connection logic
}

// Processing annotations at runtime
public static void invokeWithRetry(Object target, Method method) throws Exception {
    Retry retry = method.getAnnotation(Retry.class);
    if (retry == null) {
        method.invoke(target);
        return;
    }
    
    for (int i = 0; i < retry.maxAttempts(); i++) {
        try {
            method.invoke(target);
            return;
        } catch (Exception e) {
            if (i == retry.maxAttempts() - 1) throw e;
            Thread.sleep(retry.delayMs());
        }
    }
}
```

### Interfaces fonctionnelles et Lambdas
```java
// Built-in functional interfaces
Function<String, Integer> parseLength = s -> s.length();
Predicate<Integer> isEven = n -> n % 2 == 0;
Consumer<String> printer = s -> System.out.println(s);
Supplier<List<String>> listFactory = ArrayList::new;
BiFunction<Integer, Integer, Integer> adder = Integer::sum;

// Method references
List<String> names = List.of("Alice", "Bob", "Charlie");
names.forEach(System.out::println);          // Reference to instance method
names.stream().map(String::toUpperCase);     // Reference to instance method
names.stream().map(Integer::valueOf);        // Reference to static method

// Custom functional interface
@FunctionalInterface
public interface Transformer<T, R> {
    R transform(T input);
    
    // Default method
    default <V> Transformer<T, V> andThen(Transformer<R, V> after) {
        return input -> after.transform(this.transform(input));
    }
}
```

---

## Concurrence et parallélisme
### Fils de discussion virtuels (Java 21+)
```java
// Virtual threads — lightweight, managed by the JVM (not OS)
// Can create millions of concurrent virtual threads
public void handleRequests(List<URL> urls) throws Exception {
    try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
        List<Future<String>> futures = urls.stream()
            .map(url -> executor.submit(() -> {
                try (var in = url.openStream()) {
                    return new String(in.readAllBytes());
                }
            }))
            .toList();
        
        for (var future : futures) {
            String html = future.get();
            System.out.println("Fetched " + html.length() + " bytes");
        }
    }
}

// Creating a single virtual thread
Thread.startVirtualThread(() -> {
    System.out.println("Running in virtual thread: " + Thread.currentThread());
});
```

### Threading et synchronisation traditionnels
```java
// Thread pool for CPU-bound tasks
ExecutorService cpuPool = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());

// CompletableFuture — composable async operations
CompletableFuture.supplyAsync(() -> fetchUser(1))
    .thenApplyAsync(user -> enrichUser(user))
    .thenAccept(user -> System.out.println(user))
    .exceptionally(ex -> {
        System.err.println("Failed: " + ex.getMessage());
        return null;
    });

// Combining futures
CompletableFuture<String> nameFuture = CompletableFuture.supplyAsync(() -> "Alice");
CompletableFuture<Integer> ageFuture = CompletableFuture.supplyAsync(() -> 30);

nameFuture.thenCombine(ageFuture, (name, age) -> name + " (age " + age + ")")
    .thenAccept(System.out::println);

// Synchronisation primitives
ReentrantLock lock = new ReentrantLock();
ConcurrentHashMap<String, Integer> cache = new ConcurrentHashMap<>();
CountDownLatch latch = new CountDownLatch(3);
Semaphore semaphore = new Semaphore(5);
```

---

## Configuration du projet et système de construction
### Structure du projet (Maven)
```
my-java-project/
├── src/
│   ├── main/
│   │   ├── java/com/example/
│   │   │   ├── Application.java
│   │   │   ├── model/
│   │   │   ├── service/
│   │   │   └── controller/
│   │   └── resources/
│   │       └── application.properties
│   └── test/java/com/example/
│       └── service/
├── pom.xml
├── .github/workflows/ci.yml
└── README.md
```

### pom.xml (Maven)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
            <version>32.1.3-jre</version>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

### build.gradle.kts (Gradle)
```kotlin
plugins {
    java
    application
}

group = "com.example"
version = "1.0.0"

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(21))
    }
}

repositories { mavenCentral() }

dependencies {
    implementation("com.google.guava:guava:32.1.3-jre")
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.1")
    testImplementation("org.mockito:mockito-core:5.7.0")
}

application {
    mainClass.set("com.example.Application")
}

tasks.test { useJUnitPlatform() }
```

### Pipeline CI/CD
```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: "temurin"
          java-version: "21"
          cache: "maven"
      - run: mvn verify
      - run: mvn package -DskipTests
```

---

## Tests
### JUnit 5 avec Mockito
```java
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class UserServiceTest {
    private UserRepository mockRepo;
    private UserService service;

    @BeforeEach
    void setUp() {
        mockRepo = mock(UserRepository.class);
        service = new UserService(mockRepo);
    }

    @Test
    @DisplayName("Should create user with valid data")
    void createUser_validData_success() {
        when(mockRepo.save(any(User.class))).thenAnswer(inv -> {
            User u = inv.getArgument(0);
            return new User(1, u.name(), u.email());
        });

        User user = service.create("Alice", "alice@example.com");

        assertEquals("Alice", user.name());
        verify(mockRepo).save(any(User.class));
    }

    @Test
    void findById_existingUser_returnsUser() {
        when(mockRepo.findById(1)).thenReturn(Optional.of(new User(1, "Alice", "a@b.com")));
        Optional<User> result = service.findById(1);
        assertTrue(result.isPresent());
        assertEquals("Alice", result.get().name());
    }

    @Test
    void findById_nonExisting_returnsEmpty() {
        when(mockRepo.findById(999)).thenReturn(Optional.empty());
        assertTrue(service.findById(999).isEmpty());
    }

    @ParameterizedTest
    @ValueSource(strings = {"", "  ", "a"})
    void create_invalidName_throws(String name) {
        assertThrows(IllegalArgumentException.class, () -> service.create(name, "a@b.com"));
    }
}
```

---

## Interopérabilité
### JNI (interface native Java)
```java
// Calling native C code from Java
public class NativeMath {
    static { System.loadLibrary("nativemath"); }
    
    public native int add(int a, int b);
    public native double sqrt(double value);
}

// Compile: javac -h . NativeMath.java
// Then compile the generated C header with your C implementation
```

### API de fonctions étrangères et de mémoire (Java 22+)
```java
// Modern alternative to JNI — no C header needed
try (var arena = Arena.ofConfined()) {
    // Load C standard library
    SymbolLookup stdlib = Linker.nativeLinker().defaultLookup();
    MethodHandle strlen = Linker.nativeLinker().downcallHandle(
        stdlib.find("strlen").orElseThrow(),
        FunctionDescriptor.of(JAVA_LONG, ADDRESS)
    );
    
    // Call C function
    MemorySegment str = arena.allocateFrom("Hello, World!");
    long length = (long) strlen.invoke(str);
    System.out.println("Length: " + length);  // 13
}
```

---

## Modèles de conception
### Modèle de constructeur
```java
public class HttpRequest {
    private final String method;
    private final String url;
    private final Map<String, String> headers;
    private final String body;

    private HttpRequest(Builder builder) {
        this.method = builder.method;
        this.url = builder.url;
        this.headers = Map.copyOf(builder.headers);
        this.body = builder.body;
    }

    public static class Builder {
        private String method = "GET";
        private String url = "";
        private final Map<String, String> headers = new HashMap<>();
        private String body = null;

        public Builder method(String m) { this.method = m; return this; }
        public Builder url(String u) { this.url = u; return this; }
        public Builder header(String k, String v) { headers.put(k, v); return this; }
        public Builder body(String b) { this.body = b; return this; }
        public HttpRequest build() { return new HttpRequest(this); }
    }
}

// Usage
HttpRequest request = new HttpRequest.Builder()
    .method("POST").url("/api/users")
    .header("Content-Type", "application/json")
    .body("{\"name\":\"Alice\"}")
    .build();
```

### Modèle d'observateur
```java
public interface EventListener<T> {
    void onEvent(T event);
}

public class EventBus<T> {
    private final List<EventListener<T>> listeners = new CopyOnWriteArrayList<>();

    public void subscribe(EventListener<T> listener) { listeners.add(listener); }
    public void unsubscribe(EventListener<T> listener) { listeners.remove(listener); }
    public void publish(T event) { listeners.forEach(l -> l.onEvent(event)); }
}
```

---

## Performances et optimisation
### Outils de profilage
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### Techniques d'optimisation
```java
// Use StringBuilder for string concatenation in loops
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append("item").append(i).append(",");
}
String result = sb.toString();

// Use primitive streams for numeric operations
int sum = IntStream.rangeClosed(1, 1_000_000).sum();

// Use EnumSet/EnumMap for enum-based collections
EnumSet<DayOfWeek> weekdays = EnumSet.range(DayOfWeek.MONDAY, DayOfWeek.FRIDAY);
```

---

## Déploiement
### Fichier Docker
```dockerfile
FROM eclipse-temurin:21-jdk-alpine AS builder
WORKDIR /app
COPY . .
RUN ./mvnw package -DskipTests

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=builder /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

## L'écosystème
### Outils de création
| Outil | Objectif | Remarques |
|------|---------|-------|
| **Maven** | Automatisation du build + gestion des dépendances | Basé sur XML (`pom.xml`); norme industrielle pour les entreprises |
| **Gradle** | Automatisation du build + gestion des dépendances | Groovy/Kotlin DSL ; plus rapide pour les grands projets ; utilisé par Android |
### Cadres
| Cadre | Domaine | Descriptif |
|---------------|--------|-------------|
| **Botte de printemps** | Web/entreprise | Le framework Java dominant — API REST, microservices, sécurité, accès aux données |
| **Jakarta EE** | Entreprise | Successeur de Java EE ; API d'entreprise standardisées |
| **Hiberner** | ORM | Mappage objet-relationnel ; la mise en œuvre standard du JPA |
| **Micronaut / Quarkus** | Natif du cloud | Démarrage rapide, faible mémoire — conçu pour le sans serveur et les conteneurs |
### Tests
| Outil | Objectif |
|------|--------------|
| **JUnité 5** | Cadre de tests unitaires |
| **Mockito** | Cadre moqueur |
| **AssertJ** | Affirmations fluides |
| **Conteneurs de test** | Tests d'intégration avec des bases de données réelles dans Docker |
---

## L'écosystème JVM
| Langage JVM | Relation avec Java |
|-------------|-----------|
| **Kotlin** | Alternative moderne à Java ; Langue Android préférée de Google ; 100% compatible Java |
| **Scala** | Hybride fonctionnel + POO ; alimente Apache Spark |
| **Clojure** | Dialecte Lisp sur la JVM ; programmation fonctionnelle |
| **Groovy** | Scripts dynamiques pour la JVM ; utilisé dans les fichiers de construction Gradle |
Tous ces éléments peuvent utiliser les bibliothèques Java, et Java peut utiliser leurs bibliothèques. La JVM est la plateforme, pas seulement Java.
---

## Versions Java
| Version | Année | Principales fonctionnalités |
|---------|------|-------------|
| Java8 | 2014 | **LTS** — Lambdas, API Stream, facultatif, méthodes par défaut. Encore largement utilisé. |
| Java11 | 2018 | **LTS** — API client HTTP,`var`pour variables locales, lanceur de source mono-fichier |
| Java17 | 2021 | **LTS** — Classes scellées, correspondance de modèles pour `instanceof`, enregistrements, blocs de texte |
| Java21 | 2023 | **LTS** — **Thèmes virtuels** (Project Loom), correspondance de modèles pour `switch`, modèles d'enregistrement |
| Java25 | 2025 | **LTS** — Modèles de chaînes, correspondance de modèles supplémentaire, API de fonction étrangère |
Les versions **LTS** (Long-Term Support) reçoivent des mises à jour pendant de nombreuses années. Pour la production, utilisez Java 21 ou version ultérieure.
---

## Quand utiliser Java
| Scénario | Pourquoi Java | Meilleure alternative |
|--------------|---------|-------------------|
| Backends d'entreprise | Écosystème massif, Spring Boot, éprouvé à grande échelle | Kotlin (même JVM, moins verbeux) |
| Développement Android | Base de code établie et énorme | Kotlin (le choix préféré de Google) |
| Mégadonnées (Hadoop, Spark, Kafka) | L'écosystème est construit sur Java/Scala | Python pour le côté science des données |
| Systèmes financiers | Performance + fiabilité + outillage mature | -- |
| Microservices | Spring Boot + frameworks cloud natifs | Optez pour des services plus simples |
| Scripts simples | Trop de cérémonie | Python, Coquille |
| Outils CLI | Démarrage lent | Allez, Rouille |
---

## Questions et réponses synthétiques
### Q1 : Quelle est la différence entre`==`et`.equals()`en Java ?
**A :**`==`compare les références d'objets (identité) : il vérifie si deux variables pointent vers le même objet en mémoire. `.equals()`compare le contenu de l'objet (égalité des valeurs). Pour les primitives (`int`,`double`),`==`compare directement les valeurs. Pour les objets (y compris`String`), utilisez toujours`.equals()`pour comparer le contenu. La seule exception concerne la comparaison avec`null`, où`==`est correct.
```java
String a = new String("hello");
String b = new String("hello");
System.out.println(a == b);       // false — different objects
System.out.println(a.equals(b));  // true — same content

// String pool — literals are interned
String c = "hello";
String d = "hello";
System.out.println(c == d);       // true — same pooled object

// Always use .equals() for value comparison, or Objects.equals() for null-safe comparison
Objects.equals(a, b);  // Handles nulls without NPE
```

### Q2 : Comment fonctionne le garbage collector JVM et lequel dois-je utiliser ?
**R :** Le GC récupère automatiquement la mémoire des objets qui ne sont plus accessibles. Les JVM modernes (21+) proposent plusieurs collecteurs : G1 (par défaut, équilibré), ZGC (temps de pause ultra-faibles, <1 ms) et Shenandoah (faible pause, OpenJDK). Pour la plupart des applications, le G1 par défaut convient. Pour les services sensibles à la latence, utilisez ZGC (`-XX:+UseZGC`). Pour un traitement par lots orienté débit, utilisez Parallel GC (`-XX:+UseParallelGC`).
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### Q3 : Quand dois-je utiliser`Stream API`par rapport aux boucles traditionnelles ?
**R :** Utilisez Streams lorsque l'opération est un pipeline clair (filtrer, mapper, réduire) : ils expriment mieux l'intention et se parallélisent facilement avec`.parallelStream()`. Utilisez des boucles traditionnelles pour des itérations simples, lorsque vous devez modifier un état externe, lorsque les performances sont critiques (les flux ont une surcharge) ou lorsque la logique implique un flux de contrôle complexe (interruption, continuation, retours multiples). Évitez les flux pour les opérations`for-each`simples.
```java
// Stream — clear pipeline, easy to read
List<String> names = people.stream()
    .filter(p -> p.age() > 18)
    .sorted(Comparator.comparing(Person::name))
    .map(Person::name)
    .toList();

// Traditional loop — better for complex logic or side effects
int maxAge = 0;
String oldestName = null;
for (Person p : people) {
    if (p.age() > maxAge) {
        maxAge = p.age();
        oldestName = p.name();
    }
}
```

### Q4 : Que sont les enregistrements, les classes scellées et la correspondance de modèles dans Java moderne ?
**R :** Les enregistrements (Java 16) sont des supports de données immuables : ils génèrent automatiquement des constructeurs, des getters,`equals`,`hashCode`et`toString`. Les classes scellées (Java 17) limitent les classes qui peuvent les étendre, ce qui est utile pour modéliser des hiérarchies de types finis. La correspondance de modèles (Java 21) permet aux expressions`switch`de déstructurer les types, les enregistrements et les valeurs, en remplacement des chaînes`instanceof`verbeuses.
```java
// Record — immutable data class
public record Point(int x, int y) {
    // Compact constructor for validation
    public Point {
        if (x < 0 || y < 0) throw new IllegalArgumentException();
    }
}

// Sealed interface + pattern matching
public sealed interface Shape permits Circle, Rectangle, Triangle {}
public record Circle(double radius) implements Shape {}
public record Rectangle(double width, double height) implements Shape {}
public record Triangle(double base, double height) implements Shape {}

// Pattern matching switch (Java 21)
static double area(Shape shape) {
    return switch (shape) {
        case Circle(var r)       -> Math.PI * r * r;
        case Rectangle(var w, var h) -> w * h;
        case Triangle(var b, var h) -> 0.5 * b * h;
    };
}
```

### Q5 : Comment gérer correctement les exceptions cochées et non cochées ?
**R :** Les exceptions vérifiées (`IOException`,`SQLException`) doivent être déclarées dans`throws`ou interceptées : elles représentent des conditions récupérables que l'appelant doit connaître. Les exceptions non vérifiées (sous-classes`RuntimeException`comme`NullPointerException`,`IllegalArgumentException`) représentent des bogues de programmation. Bonne pratique : utilisez les exceptions vérifiées avec parcimonie (elles créent un couplage), préférez`Optional`pour l'absence attendue et enveloppez les exceptions vérifiées dans les exceptions non vérifiées lorsque vous franchissez les limites de l'API.
```java
// Prefer Optional over checked exception for expected absence
public Optional<User> findUser(String id) {
    return Optional.ofNullable(userRepository.findById(id));
}

// Wrap checked exceptions for cleaner APIs
public User getUser(String id) {
    try {
        return findUser(id).orElseThrow(
            () -> new UserNotFoundException("User not found: " + id));
    } catch (IOException e) {
        throw new UncheckedIOException(e);
    }
}

// Try-with-resources — automatic resource cleanup
try (var conn = dataSource.getConnection();
     var stmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?")) {
    stmt.setString(1, id);
    try (var rs = stmt.executeQuery()) {
        if (rs.next()) return mapUser(rs);
    }
}
```

---

## Résolution de problèmes en chaîne de pensée
### Problème 1 : Créer un pipeline producteur-consommateur thread-safe
**Énoncé du problème :** Concevez un pipeline producteur-consommateur en Java dans lequel plusieurs producteurs génèrent des éléments de travail, plusieurs consommateurs les traitent simultanément et le système prend en charge un arrêt progressif avec drainage des éléments restants.
**Étape 1 — Comprendre le problème :**
Nous avons besoin de : (1) une file d'attente limitée pour mettre en tampon les éléments de travail entre les producteurs et les consommateurs, (2) plusieurs threads producteurs ajoutant des éléments, (3) plusieurs threads consommateurs traitant les éléments, (4) un mécanisme pour signaler l'arrêt et drainer les éléments restants. Le`BlockingQueue`de Java est spécialement conçu pour cela.
**Étape 2 — Identifiez l'approche :**
- Utilisez`ArrayBlockingQueue`(limité) pour empêcher une croissance illimitée de la mémoire.
- Utilisez un modèle de pilule empoisonnée pour la signalisation d'arrêt.
- Utilisez`ExecutorService`pour la gestion du pool de threads.
- Utilisez`CountDownLatch`pour attendre que tous les consommateurs aient fini de se vider.
**Étape 3 — Mettre en œuvre la solution :**
```java
import java.util.concurrent.*;

public class Pipeline<T> {
    private final BlockingQueue<T> queue;
    private final ExecutorService producers;
    private final ExecutorService consumers;
    private final CountDownLatch shutdownLatch;
    private static final Object POISON_PILL = new Object();

    public Pipeline(int producerCount, int consumerCount, int queueCapacity) {
        this.queue = new ArrayBlockingQueue<>(queueCapacity);
        this.producers = Executors.newFixedThreadPool(producerCount);
        this.consumers = Executors.newFixedThreadPool(consumerCount);
        this.shutdownLatch = new CountDownLatch(consumerCount);
    }

    public void start(Function<T, Void> processor) {
        // Start consumers
        for (int i = 0; i < shutdownLatch.getCount(); i++) {
            final int id = i;
            consumers.submit(() -> {
                try {
                    while (true) {
                        T item = queue.poll(1, TimeUnit.SECONDS);
                        if (item == null) continue;
                        if (item == POISON_PILL) break;
                        processor.apply(item);
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                } finally {
                    shutdownLatch.countDown();
                }
            });
        }
    }

    public void submit(T item) throws InterruptedException {
        queue.put(item);  // Blocks if queue is full
    }

    public void shutdown() throws InterruptedException {
        // Send poison pills — one per consumer
        for (int i = 0; i < shutdownLatch.getCount(); i++) {
            queue.put((T) POISON_PILL);
        }
        // Wait for all items to be processed
        shutdownLatch.await(30, TimeUnit.SECONDS);
        producers.shutdown();
        consumers.shutdown();
    }
}
```

**Étape 4 – Vérifier et optimiser :**
- La file d'attente limitée empêche le MOO :`ArrayBlockingQueue(1000)`limite la mémoire.
- Schéma de la pilule empoisonnée : chaque consommateur sort proprement après avoir reçu sa pilule.
-`poll(1, SECONDS)`avec timeout empêche les consommateurs de bloquer définitivement si les producteurs sont lents.
- Production : utilisez`LinkedBlockingQueue`pour les pipelines illimités ou`Disruptor`(LMAX) pour les pipelines à très faible latence.
### Problème 2 : implémenter un validateur personnalisé basé sur des annotations
**Énoncé du problème :** Créez un cadre de validation à l'aide d'annotations personnalisées. Les utilisateurs annotent les champs avec`@NotNull`,`@Min(0)`,`@Max(100)`,`@Size(min=1, max=50)`et appellent`Validator.validate(obj)`pour obtenir une liste des violations.
**Étape 1 — Comprendre le problème :**
Nous avons besoin de : (1) des annotations personnalisées avec des paramètres, (2) un validateur basé sur la réflexion qui lit les annotations au moment de l'exécution, (3) un objet de résultat contenant toutes les erreurs de validation. Cela démontre les capacités de traitement et de réflexion des annotations de Java.
**Étape 2 — Identifiez l'approche :**
- Définir des annotations avec`@Retention(RUNTIME)`et`@Target(FIELD)`.
- Utilisez`Class.getDeclaredFields()`pour itérer les champs.
- Utilisez`Field.getAnnotation()`pour lire les valeurs d'annotation.
- Comparez les valeurs des champs avec les contraintes d'annotation.
- Recueillir les violations dans une liste.
**Étape 3 — Mettre en œuvre la solution :**
```java
// Annotations
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
@interface NotNull { String message() default "must not be null"; }

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
@interface Min { long value(); String message() default "must be >= {value}"; }

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
@interface Max { long value(); String message() default "must be <= {value}"; }

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
@interface Size { int min() default 0; int max() default Integer.MAX_VALUE; }

// Violation record
record Violation(String field, String message) {}

// Validator
public class Validator {
    public static List<Violation> validate(Object obj) {
        List<Violation> violations = new ArrayList<>();
        for (Field field : obj.getClass().getDeclaredFields()) {
            field.setAccessible(true);
            try {
                Object value = field.get(obj);
                String name = field.getName();

                if (field.isAnnotationPresent(NotNull.class) && value == null) {
                    violations.add(new Violation(name, "must not be null"));
                }

                if (value instanceof Number num) {
                    Min min = field.getAnnotation(Min.class);
                    if (min != null && num.longValue() < min.value()) {
                        violations.add(new Violation(name,
                            "must be >= " + min.value()));
                    }
                    Max max = field.getAnnotation(Max.class);
                    if (max != null && num.longValue() > max.value()) {
                        violations.add(new Violation(name,
                            "must be <= " + max.value()));
                    }
                }

                if (value instanceof String str) {
                    Size size = field.getAnnotation(Size.class);
                    if (size != null) {
                        if (str.length() < size.min() || str.length() > size.max()) {
                            violations.add(new Violation(name,
                                "length must be between " + size.min() + " and " + size.max()));
                        }
                    }
                }
            } catch (IllegalAccessException e) {
                throw new RuntimeException(e);
            }
        }
        return violations;
    }
}

// Usage
public class UserForm {
    @NotNull
    String name;
    @Min(0) @Max(150)
    int age;
    @Size(min = 5, max = 100)
    String email;
}

List<Violation> errors = Validator.validate(new UserForm(null, -1, "ab"));
// [Violation[field=name, message=must not be null],
//  Violation[field=age, message=must be >= 0],
//  Violation[field=email, message=length must be between 5 and 100]]
```

**Étape 4 – Vérifier et optimiser :**
- Surcharge de réflexion : acceptable pour la validation (appelée une fois par requête). Pour les chemins chauds, mettez en cache les recherches de champs ou utilisez le traitement des annotations au moment de la compilation (comme Hibernate Validator).
- Extensibilité : ajoutez de nouvelles annotations en créant l'annotation + un bloc handler dans`validate()`.
- Production : utilisez`jakarta.validation`(Bean Validation 3.0) — il fait tout cela et bien plus encore, avec un traitement au moment de la compilation via des processeurs d'annotation.
### Problème 3 : Créer un client HTTP à débit limité avec nouvelle tentative
**Énoncé du problème :** Créez un wrapper client HTTP qui réessaye automatiquement les requêtes ayant échoué avec une interruption exponentielle, respecte les limites de débit et prend en charge la coupure de circuit (arrêtez d'appeler un service défaillant).
**Étape 1 — Comprendre le problème :**
Nous avons besoin de : (1) une logique de nouvelle tentative avec une interruption exponentielle et une gigue, (2) une limitation du débit pour éviter de surcharger le service cible, (3) un modèle de disjoncteur - après N échecs consécutifs, arrêtez d'appeler le service pendant une période de refroidissement. Ce sont trois préoccupations composables.
**Étape 2 — Identifiez l'approche :**
- Utilisez`java.net.http.HttpClient`(Java 11+) comme client de base.
- Implémentez une nouvelle tentative en tant que wrapper avec`Thread.sleep`pour l'interruption.
- Utilisez`Semaphore`pour la limitation du débit (ou`java.time`pour le compartiment de jetons).
- Implémenter le disjoncteur comme machine à états : FERMÉ → OUVERT → DEMI_OUVERT.
**Étape 3 — Mettre en œuvre la solution :**
```java
import java.net.http.*;
import java.time.Duration;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;

public class ResilientClient {
    private final HttpClient client;
    private final int maxRetries;
    private final Semaphore rateLimiter;
    private final AtomicInteger consecutiveFailures;
    private final AtomicLong openUntil;
    private final int failureThreshold;
    private final long cooldownMs;

    public ResilientClient(int maxRetries, int requestsPerSecond,
                           int failureThreshold, long cooldownMs) {
        this.client = HttpClient.newBuilder()
            .connectTimeout(Duration.ofSeconds(10))
            .build();
        this.maxRetries = maxRetries;
        this.rateLimiter = new Semaphore(requestsPerSecond);
        this.consecutiveFailures = new AtomicInteger(0);
        this.openUntil = new AtomicLong(0);
        this.failureThreshold = failureThreshold;
        this.cooldownMs = cooldownMs;

        // Replenish semaphore permits every second
        Executors.newSingleThreadScheduledExecutor(r -> {
            Thread t = new Thread(r, "rate-limiter");
            t.setDaemon(true);
            return t;
        }).scheduleAtFixedRate(() -> {
            int drain = requestsPerSecond - rateLimiter.availablePermits();
            if (drain > 0) rateLimiter.release(drain);
        }, 1, 1, TimeUnit.SECONDS);
    }

    public HttpResponse<String> send(HttpRequest request) throws Exception {
        // Circuit breaker check
        if (System.currentTimeMillis() < openUntil.get()) {
            throw new CircuitOpenException("Circuit breaker is open");
        }

        Exception lastException = null;
        for (int attempt = 0; attempt <= maxRetries; attempt++) {
            try {
                rateLimiter.acquire();  // Wait for rate limit permit
                HttpResponse<String> response = client.send(request,
                    HttpResponse.BodyHandlers.ofString());

                if (response.statusCode() >= 500) {
                    throw new ServerException("HTTP " + response.statusCode());
                }

                // Success — reset failure counter
                consecutiveFailures.set(0);
                return response;

            } catch (Exception e) {
                lastException = e;
                int failures = consecutiveFailures.incrementAndGet();

                if (failures >= failureThreshold) {
                    openUntil.set(System.currentTimeMillis() + cooldownMs);
                    throw new CircuitOpenException(
                        "Circuit opened after " + failures + " failures");
                }

                if (attempt < maxRetries) {
                    long delay = (long) Math.pow(2, attempt) * 100;
                    long jitter = ThreadLocalRandom.current().nextLong(0, delay / 2);
                    Thread.sleep(delay + jitter);
                }
            }
        }
        throw lastException;
    }
}
```

**Étape 4 – Vérifier et optimiser :**
- L'intervalle exponentiel avec gigue empêche le troupeau de tonnerre (toutes les tentatives frappent en même temps).
- Disjoncteur : après des échecs consécutifs de `failureThreshold`, le circuit s'ouvre pour`cooldownMs`— aucune requête n'est envoyée, protégeant le service défaillant.
- Limiteur de débit :`Semaphore`avec débit de bouchons de réapprovisionnement périodique.
- Production : utilisez`resilience4j`— il fournit les trois modèles (nouvelle tentative, limiteur de débit, disjoncteur) avec des implémentations, des métriques et une intégration Spring Boot appropriées.
---

## Résumé
Java est l'un des langages de programmation les plus importants jamais créés. Il gère les systèmes bancaires, les téléphones Android, les pipelines Big Data et les backends d'entreprise du monde entier. Java moderne (21+) est un langage très différent de Java 8 : il est plus concis, plus expressif et de plus en plus compétitif par rapport aux langages plus récents. L'écosystème JVM (Kotlin, Scala, Clojure) étend encore sa portée. Pour le développement d'entreprise, Java reste un choix sûr et puissant.