---
# Metadatos
título: "Java"
descripción: "Referencia completa para el lenguaje de programación Java que cubre descripción general, compensaciones, fundamentos de sintaxis, ecosistema y cuándo usarlo".
categoría: "Codificación y tecnología"
versión: "1.0.0"
estado: "activo"
# Contribución
autores:
  - nombre: "Equipo de formación del modelo de IA"
    correo electrónico: ""
    rol: "autor_original"
colaboradores: []
registro de cambios:
  - versión: "1.0.0"
    fecha: "2026-08-05"
    autor: "Equipo de formación del modelo de IA"
    cambios: "Se agregaron metadatos de temas frontales de YAML para el seguimiento de los contribuyentes"
# Revisión
creado: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
review_by: "Equipo de base de conocimientos de codificación y tecnología"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [java, lenguaje-de-programación, sintaxis, ecosistema, codificación-y-tecnología]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "30 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
#Java
Java es un lenguaje de programación orientado a objetos de tipo estático creado por James Gosling en Sun Microsystems y lanzado en 1995. Su filosofía de diseño - "escribir una vez, ejecutar en cualquier lugar" (WORA) - se logra a través de la Máquina Virtual Java (JVM), que permite que el código Java compilado se ejecute en cualquier plataforma que tenga una implementación JVM. Java es uno de los lenguajes de programación más utilizados en la historia y potencia los backends empresariales, las aplicaciones de Android, los sistemas de big data y los servicios financieros.
A pesar de tener casi 30 años, Java sigue evolucionando. Java moderno (versiones 17+) incluye registros, clases selladas, coincidencia de patrones, subprocesos virtuales y un ecosistema en crecimiento que compite con lenguajes más nuevos.
---

## Por qué es importante Java
- **Estándar empresarial**: la columna vertebral de los backends de Fortune 500: banca, seguros, comercio electrónico y atención médica.
- **Desarrollo de Android**: el lenguaje principal para Android (junto con Kotlin).
- **Ecosistema de big data**: Apache Hadoop, Spark, Kafka, Elasticsearch, todos escritos en Java o Scala (que se ejecuta en JVM).
- **Ecosistema masivo**: Más de 500.000 bibliotecas en Maven Central; Herramientas maduras para cada necesidad.
- **Rendimiento**: el compilador JIT de JVM produce código de máquina altamente optimizado en tiempo de ejecución, que a menudo coincide con C++ para aplicaciones de larga ejecución.
- **Compatibilidad con versiones anteriores**: el código escrito para Java 1.0 (1996) todavía se ejecuta en JVM modernas.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **Verbosidad** | Requiere más texto estándar que Python, Kotlin o Go | Utilice Lombok, registros (Java 16+) e IDE modernos |
| **Uso de memoria** | La sobrecarga de JVM significa una mayor memoria base | Ajustar indicadores de JVM; utilice imágenes nativas de GraalVM para implementaciones pequeñas |
| **Hora de inicio** | El calentamiento de JVM puede ser lento para procesos de corta duración | Imagen nativa de GraalVM o utilice C/Go para herramientas CLI |
| **Excepciones marcadas** | Obliga el manejo de excepciones que pueden no ser recuperables | Utilice excepciones no marcadas o el patrón`Optional`|
| **Sin tipos de valores** | Todo es un objeto (hasta el proyecto Valhalla) | Utilice colecciones primitivas especializadas (Eclipse Collections, Trove) |
---

## Fundamentos de sintaxis
### Estructura básica
Java se basa en clases: todo vive dentro de una clase. El nombre del archivo debe coincidir con el nombre de la clase pública.
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

### Programación orientada a objetos
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

### Registros (Java 16+): clases de datos concisas
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

### Colecciones y transmisiones
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

### Manejo de excepciones
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

## Sintaxis y patrones avanzados
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

### Clases selladas y coincidencia de patrones (Java 17+)
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

### Anotaciones
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

### Interfaces funcionales y Lambdas
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

## Concurrencia y paralelismo
### Hilos virtuales (Java 21+)
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

### Subprocesos y sincronización tradicionales
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

## Configuración del proyecto y sistema de construcción
### Estructura del proyecto (Maven)
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

### Canalización de CI/CD
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

## Pruebas
### JUnit 5 con Mockito
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

## Interoperabilidad
### JNI (interfaz nativa de Java)
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

### Función externa y API de memoria (Java 22+)
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

## Patrones de diseño
### Patrón de constructor
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

### Patrón de observador
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

## Rendimiento y optimización
### Herramientas de creación de perfiles
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### Técnicas de optimización
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

## Implementación
### Archivo Docker
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

## El ecosistema
### Herramientas de construcción
| Herramienta | Propósito | Notas |
|------|---------|-------|
| **Maven** | Automatización de compilación + gestión de dependencias | Basado en XML (`pom.xml`); estándar de la industria para empresas |
| **Gradle** | Automatización de compilación + gestión de dependencias | Groovy/Kotlin DSL; más rápido para proyectos grandes; utilizado por Android |
### Marcos
| Marco | Dominio | Descripción |
|-----------|--------|-------------|
| **Bota de primavera** | Web / empresa | El marco Java dominante: API REST, microservicios, seguridad, acceso a datos |
| **Yakarta EE** | Empresa | Sucesor de Java EE; API empresariales estandarizadas |
| **Hibernar** | ORM | Mapeo relacional de objetos; la implementación estándar de JPA |
| **Micronauta / Quarkus** | Nativo de la nube | Inicio rápido, poca memoria: diseñado para contenedores y sin servidor |
### Pruebas
| Herramienta | Propósito |
|------|---------|
| **JUnidad 5** | Marco de pruebas unitarias |
| **Mockito** | Marco burlón |
| **AfirmarJ** | Afirmaciones fluidas |
| **Contenedores de prueba** | Pruebas de integración con bases de datos reales en Docker |
---

## El ecosistema JVM
| Lenguaje JVM | Relación con Java |
|-------------|---------------------|
| **Kotlin** | Alternativa moderna a Java; El idioma Android preferido de Google; 100% compatible con Java |
| **Escala** | Híbrido funcional + programación orientada a objetos; potencia Apache Spark |
| **Clojure** | Dialecto Lisp en la JVM; programación funcional |
| **Maravilloso** | Secuencias de comandos dinámicas para JVM; utilizado en archivos de compilación de Gradle |
Todos estos pueden usar bibliotecas de Java y Java puede usar sus bibliotecas. La JVM es la plataforma, no sólo Java.
---

## Versiones de Java
| Versión | Año | Características clave |
|---------|------|-------------|
| Java 8 | 2014 | **LTS**: Lambdas, Stream API, opcional, métodos predeterminados. Todavía muy utilizado. |
| Java 11 | 2018 | **LTS** — API de cliente HTTP,`var`para variables locales, iniciador de código fuente de un solo archivo |
| Java 17 | 2021 | **LTS** — Clases selladas, coincidencia de patrones para `instanceof`, registros, bloques de texto |
| Java 21 | 2023 | **LTS** — **Hilos virtuales** (Project Loom), coincidencia de patrones para `switch`, registrar patrones |
| Java 25 | 2025 | **LTS** — Plantillas de cadenas, mayor coincidencia de patrones, API de funciones externas |
Las versiones **LTS** (soporte a largo plazo) reciben actualizaciones durante muchos años. Para producción, utilice Java 21 o posterior.
---

## Cuándo utilizar Java
| Escenario | Por qué Java | Mejor alternativa |
|----------|---------|-------------------|
| Servicios de backend empresarial | Ecosistema masivo, Spring Boot, probado a escala | Kotlin (misma JVM, menos detallado) |
| Desarrollo de Android | Base de código enorme y establecida | Kotlin (la opción preferida de Google) |
| Grandes datos (Hadoop, Spark, Kafka) | El ecosistema está construido sobre Java/Scala | Python para la ciencia de datos |
| Sistemas financieros | Rendimiento + confiabilidad + herramientas maduras | -- |
| Microservicios | Spring Boot + marcos nativos de la nube | Opte por servicios más simples |
| Guiones simples | Demasiada ceremonia | Pitón, concha |
| Herramientas CLI | Inicio lento | Vamos, óxido |
---

## Resumen
Java es uno de los lenguajes de programación más importantes jamás creados. Gestiona los sistemas bancarios, los teléfonos Android, los canales de big data y los backends empresariales del mundo. Modern Java (21+) es un lenguaje muy diferente de Java 8: es más conciso, más expresivo y cada vez más competitivo con los lenguajes más nuevos. El ecosistema JVM (Kotlin, Scala, Clojure) amplía aún más su alcance. Para el desarrollo empresarial, Java sigue siendo una opción segura y potente.