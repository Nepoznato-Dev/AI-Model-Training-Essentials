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
#Java
Java é uma linguagem de programação orientada a objetos de tipo estaticamente criada por James Gosling na Sun Microsystems e lançada em 1995. Sua filosofia de design - "escrever uma vez, executar em qualquer lugar" (WORA) - é alcançada por meio da Java Virtual Machine (JVM), que permite que o código Java compilado seja executado em qualquer plataforma que tenha uma implementação JVM. Java é uma das linguagens de programação mais utilizadas na história, potencializando back-ends empresariais, aplicativos Android, sistemas de big data e serviços financeiros.
Apesar de ter quase 30 anos, Java continua a evoluir. O Java moderno (versões 17+) inclui registros, classes seladas, correspondência de padrões, threads virtuais e um ecossistema crescente que compete com linguagens mais recentes.
---

## Por que Java é importante
- **Padrão empresarial**: a espinha dorsal dos back-ends da Fortune 500 — bancos, seguros, comércio eletrônico, saúde.
- **Desenvolvimento Android**: a linguagem principal do Android (junto com Kotlin).
- **Ecossistema de big data**: Apache Hadoop, Spark, Kafka, Elasticsearch — todos escritos em Java ou Scala (que roda na JVM).
- **Ecossistema massivo**: Mais de 500.000 bibliotecas no Maven Central; ferramentas maduras para cada necessidade.
- **Desempenho**: o compilador JIT da JVM produz código de máquina altamente otimizado em tempo de execução, geralmente combinando com C++ para aplicativos de longa execução.
- **Compatibilidade com versões anteriores**: o código escrito para Java 1.0 (1996) ainda funciona em JVMs modernas.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Verbosidade** | Requer mais padrões do que Python, Kotlin ou Go | Use Lombok, registros (Java 16+) e IDEs modernos |
| **Uso de memória** | Sobrecarga de JVM significa maior memória de linha de base | Ajustar sinalizadores JVM; use imagens nativas do GraalVM para pequenas implantações |
| **Hora de inicialização** | O aquecimento da JVM pode ser lento para processos de curta duração | Imagem nativa GraalVM ou use C/Go para ferramentas CLI |
| **Exceções verificadas** | Força o tratamento de exceções que podem não ser recuperáveis ​​| Use exceções não verificadas ou o padrão`Optional`|
| **Sem tipos de valor** | Tudo é objeto (até projeto Valhalla) | Use coleções especializadas em primitivos (Eclipse Collections, Trove) |
---

## Fundamentos de sintaxe
### Estrutura Básica
Java é baseado em classes – tudo vive dentro de uma classe. O nome do arquivo deve corresponder ao nome da classe pública.
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

### Programação Orientada a Objetos
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

### Registros (Java 16+) — Classes de dados concisas
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

### Coleções e fluxos
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

### Tratamento de exceções
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

## Sintaxe e padrões avançados
### Genéricos
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

### Classes seladas e correspondência de padrões (Java 17+)
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

### Anotações
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

### Interfaces Funcionais e Lambdas
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

## Simultaneidade e paralelismo
### Threads Virtuais (Java 21+)
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

### Threading e sincronização tradicionais
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

## Configuração do projeto e sistema de construção
### Estrutura do Projeto (Maven)
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

### Pipeline de CI/CD
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

## Teste
### JUnit 5 com Mockito
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

## Interoperabilidade
### JNI (interface nativa Java)
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

### Função estrangeira e API de memória (Java 22+)
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

## Padrões de Projeto
### Padrão do Construtor
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

### Padrão Observador
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

## Desempenho e otimização
### Ferramentas de criação de perfil
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### Técnicas de otimização
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

## Implantação
### Dockerfile
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

## O Ecossistema
### Ferramentas de construção
| Ferramenta | Finalidade | Notas |
|------|---------|-------|
| **Maven** | Automação de build + gerenciamento de dependências | Baseado em XML (`pom.xml`); padrão da indústria para empresas |
| **Gradle** | Automação de build + gerenciamento de dependências | DSL bacana/Kotlin; mais rápido para grandes projetos; usado pelo Android |
### Estruturas
| Estrutura | Domínio | Descrição |
|-----------|--------|-------------|
| **Bota de primavera** | Web/empresa | A estrutura Java dominante — APIs REST, microsserviços, segurança, acesso a dados |
| **Jacarta EE** | Empresa | Sucessor do Java EE; APIs empresariais padronizadas |
| **Hibernar** | ORM | Mapeamento objeto-relacional; a implementação padrão do JPA |
| **Micronauta / Quarkus** | Nativo da nuvem | Inicialização rápida, pouca memória — projetado para contêineres e sem servidor |
### Teste
| Ferramenta | Finalidade |
|------|---------|
| **JUnit 5** | Estrutura de testes unitários |
| **Mockito** | Estrutura de simulação |
| **AfirmarJ** | Afirmações fluentes |
| **Contêineres de teste** | Testes de integração com bancos de dados reais em Docker |
---

## O ecossistema JVM
| Linguagem JVM | Relacionamento com Java |
|------------|----------|
| **Kotlin** | Alternativa moderna ao Java; O idioma Android preferido do Google; 100% compatível com Java |
| **Escala** | Híbrido funcional + OOP; alimenta o Apache Spark |
| **Clojure** | Dialeto Lisp na JVM; programação funcional |
| **Incrível** | Scripting dinâmico para JVM; usado em arquivos de compilação do Gradle |
Todos eles podem usar bibliotecas Java, e Java pode usar suas bibliotecas. A JVM é a plataforma, não apenas Java.
---

## Versões Java
| Versão | Ano | Principais recursos |
|--------|------|---------|
| Java 8 | 2014 | **LTS** — Lambdas, Stream API, Opcional, métodos padrão. Ainda amplamente utilizado. |
| Java 11 | 2018 | **LTS** — API do cliente HTTP,`var`para variáveis ​​locais, inicializador de origem de arquivo único |
| Java 17 | 2021 | **LTS** — Classes seladas, correspondência de padrões para`instanceof`, registros, blocos de texto |
| Java 21 | 2023 | **LTS** — **Threads virtuais** (Project Loom), correspondência de padrões para`switch`, padrões de registro |
| Java 25 | 2025 | **LTS** — Modelos de string, correspondência adicional de padrões, API de função estrangeira |
As versões **LTS** (suporte de longo prazo) recebem atualizações por muitos anos. Para produção, use Java 21 ou posterior.
---

## Quando usar Java
| Cenário | Por que Java | Melhor Alternativa |
|----------|---------|-------------------|
| Back-ends empresariais | Enorme ecossistema, Spring Boot, comprovado em escala | Kotlin (mesma JVM, menos detalhado) |
| Desenvolvimento Android | Base de código enorme e estabelecida | Kotlin (escolha preferida do Google) |
| Big data (Hadoop, Spark, Kafka) | O ecossistema é construído em Java/Scala | Python para o lado da ciência de dados |
| Sistemas financeiros | Desempenho + confiabilidade + ferramentas maduras | -- |
| Microsserviços | Spring Boot + estruturas nativas da nuvem | Opte por serviços mais simples |
| Scripts simples | Muita cerimônia | Python, Concha |
| Ferramentas CLI | Inicialização lenta | Vá, Ferrugem |
---

## Perguntas e respostas sintéticas
### Q1: Qual é a diferença entre`==`e`.equals()`em Java?
**R:**`==`compara referências de objetos (identidade) — verifica se duas variáveis ​​apontam para o mesmo objeto na memória. `.equals()`compara o conteúdo do objeto (igualdade de valores). Para primitivos (`int`,`double`),`==`compara valores diretamente. Para objetos (incluindo`String`), sempre use`.equals()`para comparar o conteúdo. A única exceção é a comparação com`null`, onde`==`está correto.
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

### Q2: Como funciona o coletor de lixo JVM e qual devo usar?
**R:** O GC recupera automaticamente a memória de objetos que não estão mais acessíveis. JVMs modernas (21+) oferecem vários coletores: G1 (padrão, balanceado), ZGC (tempos de pausa ultrabaixos, <1ms) e Shenandoah (pausa baixa, OpenJDK). Para a maioria dos aplicativos, o G1 padrão é adequado. Para serviços sensíveis à latência, use ZGC (`-XX:+UseZGC`). Para processamento em lote orientado ao rendimento, use GC Paralelo (`-XX:+UseParallelGC`).
```bash
# JVM flags for GC tuning
java -XX:+UseZGC -Xmx4g -Xms4g -jar app.jar

# Monitor GC activity
java -Xlog:gc*:file=gc.log:time,tags:filecount=5,filesize=10M -jar app.jar
```

### Q3: Quando devo usar`Stream API`versus loops tradicionais?
**R:** Use Streams quando a operação for um pipeline claro (filtrar, mapear, reduzir) — eles expressam melhor a intenção e paralelizam facilmente com`.parallelStream()`. Use loops tradicionais para iterações simples, quando precisar modificar o estado externo, quando o desempenho for crítico (streams têm sobrecarga) ou quando a lógica envolver fluxo de controle complexo (interrupção, continuação, retornos múltiplos). Evite fluxos para operações`for-each`simples.
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

### Q4: O que são registros, classes seladas e correspondência de padrões no Java moderno?
**R:** Registros (Java 16) são portadores de dados imutáveis ​​— eles geram automaticamente construtores, getters,`equals`,`hashCode`e`toString`. Classes seladas (Java 17) restringem quais classes podem estendê-las – útil para modelar hierarquias de tipos finitos. A correspondência de padrões (Java 21) permite que expressões`switch`desestruturam tipos, registros e valores – substituindo cadeias detalhadas `instanceof`.
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

### Q5: Como lidar corretamente com exceções verificadas e não verificadas?
**R:** Exceções verificadas (`IOException`,`SQLException`) devem ser declaradas em`throws`ou capturadas — elas representam condições recuperáveis ​​que o chamador deve conhecer. Exceções não verificadas (subclasses`RuntimeException`como `NullPointerException`, `IllegalArgumentException`) representam bugs de programação. Prática recomendada: use exceções verificadas com moderação (elas criam acoplamento), prefira`Optional`para ausência esperada e envolva exceções verificadas em exceções não verificadas ao cruzar os limites da API.
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

## Resolução de problemas por cadeia de pensamento
### Problema 1: Construir um pipeline produtor-consumidor seguro para threads
**Declaração do problema:** Projete um pipeline produtor-consumidor em Java onde vários produtores geram itens de trabalho, vários consumidores os processam simultaneamente e o sistema oferece suporte ao desligamento normal com drenagem dos itens restantes.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) uma fila limitada para armazenar itens de trabalho entre produtores e consumidores, (2) múltiplos threads produtores adicionando itens, (3) múltiplos threads consumidores processando itens, (4) um mecanismo para sinalizar o desligamento e drenar os itens restantes. O`BlockingQueue`do Java foi desenvolvido especificamente para isso.
**Etapa 2 — Identifique a abordagem:**
- Use`ArrayBlockingQueue`(limitado) para evitar o crescimento ilimitado de memória.
- Use um padrão de pílula venenosa para sinalização de desligamento.
- Use`ExecutorService`para gerenciamento do conjunto de encadeamentos.
- Use`CountDownLatch`para aguardar que todos os consumidores terminem a drenagem.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- A fila limitada impede OOM:`ArrayBlockingQueue(1000)`limita a memória.
- Padrão de pílula venenosa: cada consumidor sai limpo após receber sua pílula.
-`poll(1, SECONDS)`com timeout evita que os consumidores bloqueiem para sempre se os produtores forem lentos.
- Produção: use`LinkedBlockingQueue`para ilimitado ou`Disruptor`(LMAX) para pipelines de latência ultrabaixa.
### Problema 2: Implementar um validador baseado em anotação personalizada
**Declaração do problema:** Crie uma estrutura de validação usando anotações personalizadas. Os usuários anotam os campos com`@NotNull`,`@Min(0)`,`@Max(100)`,`@Size(min=1, max=50)`e chamam`Validator.validate(obj)`para obter uma lista de violações.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) anotações personalizadas com parâmetros, (2) um validador baseado em reflexão que leia anotações em tempo de execução, (3) um objeto de resultado contendo todos os erros de validação. Isso demonstra os recursos de processamento e reflexão de anotações do Java.
**Etapa 2 — Identifique a abordagem:**
- Defina anotações com`@Retention(RUNTIME)`e`@Target(FIELD)`.
- Use`Class.getDeclaredFields()`para iterar campos.
- Use`Field.getAnnotation()`para ler valores de anotação.
- Compare os valores dos campos com as restrições de anotação.
- Colete as violações em uma lista.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Sobrecarga de reflexão: aceitável para validação (chamado uma vez por solicitação). Para hot paths, armazene pesquisas de campo em cache ou use processamento de anotação em tempo de compilação (como Hibernate Validator).
- Extensibilidade: adicione novas anotações criando a anotação + um bloco manipulador em`validate()`.
- Produção: use`jakarta.validation`(Bean Validation 3.0) — ele faz tudo isso e muito mais, com processamento em tempo de compilação via processadores de anotação.
### Problema 3: Construa um cliente HTTP com taxa limitada com nova tentativa
**Declaração do problema:** Crie um wrapper de cliente HTTP que tente novamente solicitações com falha com espera exponencial, respeite os limites de taxa e ofereça suporte à quebra de circuito (pare de chamar um serviço com falha).
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) lógica de repetição com espera exponencial e jitter, (2) limitação de taxa para evitar sobrecarregar o serviço de destino, (3) padrão de disjuntor - após N falhas consecutivas, parar de chamar o serviço por um período de espera. Essas são três preocupações combináveis.
**Etapa 2 — Identifique a abordagem:**
- Use`java.net.http.HttpClient`(Java 11+) como cliente base.
- Implemente a nova tentativa como um wrapper com`Thread.sleep`para espera.
- Use`Semaphore`para limitação de taxa (ou`java.time`para token bucket).
- Implementar o disjuntor como máquina de estados: CLOSED → OPEN → HALF_OPEN.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- A espera exponencial com jitter evita o rebanho trovejante (todas as novas tentativas atingem ao mesmo tempo).
- Disjuntor: após falhas consecutivas de `failureThreshold`, o circuito abre para`cooldownMs`— nenhuma solicitação é enviada, protegendo o serviço com falha.
- Limitador de taxa:`Semaphore`com capacidade de limite de reabastecimento periódico.
- Produção: use`resilience4j`— ele fornece todos os três padrões (nova tentativa, limitador de taxa, disjuntor) com implementações, métricas e integração Spring Boot adequadas.
---

## Resumo
Java é uma das linguagens de programação mais importantes já criadas. Ele executa os sistemas bancários, telefones Android, pipelines de big data e back-ends empresariais do mundo todo. O Java moderno (21+) é uma linguagem muito diferente do Java 8 — é mais conciso, mais expressivo e cada vez mais competitivo com linguagens mais recentes. O ecossistema JVM (Kotlin, Scala, Clojure) amplia ainda mais seu alcance. Para o desenvolvimento empresarial, Java continua sendo uma escolha segura e poderosa.