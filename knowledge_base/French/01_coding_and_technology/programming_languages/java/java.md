---
# Métadonnées
titre : "Java"
description : "Référence complète sur le langage de programmation Java couvrant la présentation, les compromis, les principes fondamentaux de la syntaxe, l'écosystème et quand l'utiliser."
catégorie : "Codage et technologie"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de base de connaissances en matière de codage et de technologie"
next_review : "2027-08-05"
#Classement
balises : [java, langage de programmation, syntaxe, écosystème, codage et technologie]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "30 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Java
Java est un langage de programmation orienté objet à typage statique créé par James Gosling chez Sun Microsystems et publié en 1995. Sa philosophie de conception — « écrire une fois, exécuter n'importe où » (WORA) — est réalisée grâce à la machine virtuelle Java (JVM), qui permet au code Java compilé de s'exécuter sur n'importe quelle plate-forme dotée d'une implémentation JVM. Java est l'un des langages de programmation les plus utilisés de l'histoire, alimentant les backends d'entreprise, les applications Android, les systèmes Big Data et les services financiers.
Malgré ses près de 30 ans, Java continue d'évoluer. Java moderne (versions 17+) comprend des enregistrements, des classes scellées, une correspondance de modèles, des threads virtuels et un écosystème croissant qui rivalise avec les langages plus récents.
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
### Génériques
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
|-------------|---------------------|
| **Kotlin** | Alternative moderne à Java ; La langue Android préférée de Google ; 100% compatible Java |
| **Scala** | Hybride fonctionnel + POO ; alimente Apache Spark |
| **Clojure** | Dialecte Lisp sur la JVM ; programmation fonctionnelle |
| **Groovy** | Scripts dynamiques pour la JVM ; utilisé dans les fichiers de construction Gradle |
Tous ces éléments peuvent utiliser les bibliothèques Java, et Java peut utiliser leurs bibliothèques. La JVM est la plateforme, pas seulement Java.
---

## Versions Java
| Version | Année | Principales fonctionnalités |
|---------|------|-------------|
| Java8 | 2014 | **LTS** — Lambdas, API Stream, facultatif, méthodes par défaut. Encore largement utilisé. |
| Java11 | 2018 | **LTS** — API client HTTP,`var`pour les variables locales, lanceur de source mono-fichier |
| Java17 | 2021 | **LTS** — Classes scellées, correspondance de modèles pour`instanceof`, enregistrements, blocs de texte |
| Java21 | 2023 | **LTS** — **Thèmes virtuels** (Project Loom), correspondance de modèles pour`switch`, modèles d'enregistrement |
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

## Résumé
Java est l'un des langages de programmation les plus importants jamais créés. Il gère les systèmes bancaires, les téléphones Android, les pipelines Big Data et les backends d'entreprise du monde entier. Java moderne (21+) est un langage très différent de Java 8 : il est plus concis, plus expressif et de plus en plus compétitif par rapport aux langages plus récents. L'écosystème JVM (Kotlin, Scala, Clojure) étend encore sa portée. Pour le développement d'entreprise, Java reste un choix sûr et puissant.