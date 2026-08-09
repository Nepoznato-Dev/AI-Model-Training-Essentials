---
# मेटाडेटा
शीर्षक: "जावा"
विवरण: "जावा प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स बुनियादी बातें, पारिस्थितिकी तंत्र और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [जावा, प्रोग्रामिंग-भाषा, सिंटैक्स, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का समय: "30 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# जावा
जावा एक सांख्यिकीय रूप से टाइप की गई, ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग भाषा है, जिसे सन माइक्रोसिस्टम्स में जेम्स गोस्लिंग द्वारा बनाया गया था और 1995 में जारी किया गया था। इसका डिज़ाइन दर्शन - "एक बार लिखें, कहीं भी चलाएं" (WORA) - जावा वर्चुअल मशीन (JVM) के माध्यम से प्राप्त किया जाता है, जो संकलित जावा कोड को JVM कार्यान्वयन वाले किसी भी प्लेटफ़ॉर्म पर चलाने की अनुमति देता है। जावा इतिहास में सबसे व्यापक रूप से उपयोग की जाने वाली प्रोग्रामिंग भाषाओं में से एक है, जो एंटरप्राइज़ बैकएंड, एंड्रॉइड ऐप्स, बड़े डेटा सिस्टम और वित्तीय सेवाओं को सशक्त बनाती है।
लगभग 30 वर्ष पुराना होने के बावजूद, जावा का विकास जारी है। आधुनिक जावा (संस्करण 17+) में रिकॉर्ड, सीलबंद कक्षाएं, पैटर्न मिलान, आभासी धागे और एक बढ़ता हुआ पारिस्थितिकी तंत्र शामिल है जो नई भाषाओं के साथ प्रतिस्पर्धा करता है।
---

## जावा क्यों मायने रखता है
- **एंटरप्राइज़ मानक**: फॉर्च्यून 500 बैकएंड की रीढ़ - बैंकिंग, बीमा, ई-कॉमर्स, स्वास्थ्य सेवा।
- **एंड्रॉइड विकास**: एंड्रॉइड के लिए प्राथमिक भाषा (कोटलिन के साथ)।
- **बिग डेटा इकोसिस्टम**: अपाचे हडूप, स्पार्क, काफ्का, इलास्टिक्सर्च - सभी जावा या स्काला में लिखे गए हैं (जो जेवीएम पर चलता है)।
- **विशाल पारिस्थितिकी तंत्र**: मावेन सेंट्रल पर 500,000 से अधिक पुस्तकालय; हर जरूरत के लिए परिपक्व टूलींग।
- **प्रदर्शन**: JVM का JIT कंपाइलर रनटाइम पर अत्यधिक अनुकूलित मशीन कोड तैयार करता है, जो अक्सर लंबे समय तक चलने वाले अनुप्रयोगों के लिए C++ से मेल खाता है।
- **बैकवर्ड अनुकूलता**: जावा 1.0 (1996) के लिए लिखा गया कोड अभी भी आधुनिक जेवीएम पर चलता है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **वाचालता** | Python,kotlin, या Go | की तुलना में अधिक बॉयलरप्लेट की आवश्यकता होती है लोम्बोक, रिकॉर्ड्स (जावा 16+), और आधुनिक आईडीई का उपयोग करें |
| **मेमोरी उपयोग** | जेवीएम ओवरहेड का मतलब है उच्च बेसलाइन मेमोरी | जेवीएम झंडे ट्यून करें; छोटी तैनाती के लिए GraalVM मूल छवियों का उपयोग करें |
| **स्टार्टअप समय** | अल्पकालिक प्रक्रियाओं के लिए जेवीएम वार्म-अप धीमा हो सकता है | GraalVM नेटिव-इमेज, या CLI टूल्स के लिए C/Go का उपयोग करें |
| **चेक किए गए अपवाद** | उन अपवादों को संभालने के लिए बाध्य करता है जिन्हें पुनर्प्राप्त नहीं किया जा सकता है | अनियंत्रित अपवादों या`Optional`पैटर्न का उपयोग करें |
| **कोई मूल्य प्रकार नहीं** | हर चीज़ एक वस्तु है (वल्लाह परियोजना तक) | आदिम-विशिष्ट संग्रह (एक्लिप्स कलेक्शन, ट्रोव) का उपयोग करें |
---

## सिंटेक्स बुनियादी बातें
### बुनियादी संरचना
जावा क्लास-आधारित है - सब कुछ एक क्लास के अंदर रहता है। फ़ाइल नाम सार्वजनिक वर्ग के नाम से मेल खाना चाहिए।
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

### ऑब्जेक्ट ओरिएंटेड प्रोग्रामिंग
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

### रिकॉर्ड्स (जावा 16+) - संक्षिप्त डेटा कक्षाएं
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

### संग्रह और धाराएँ
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

### एक्सेप्शन हेंडलिंग
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

## उन्नत सिंटैक्स और पैटर्न
### जेनेरिक
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

### सीलबंद कक्षाएं और पैटर्न मिलान (जावा 17+)
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

### एनोटेशन
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

### कार्यात्मक इंटरफेस और लैम्ब्डा
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

## समवर्ती एवं समांतरता
### वर्चुअल थ्रेड्स (जावा 21+)
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

### पारंपरिक थ्रेडिंग और सिंक्रोनाइज़ेशन
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना (मावेन)
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

### pom.xml (मावेन)
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

### build.gradle.kts (ग्रैडल)
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

### सीआई/सीडी पाइपलाइन
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

## परीक्षण
### मॉकिटो के साथ जुनिट 5
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

## अंतरसंचालनीयता
### जेएनआई (जावा नेटिव इंटरफ़ेस)
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

### विदेशी फ़ंक्शन और मेमोरी एपीआई (जावा 22+)
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

## डिज़ाइन पैटर्न
### बिल्डर पैटर्न
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

### प्रेक्षक पैटर्न
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
```bash
# JFR — Java Flight Recorder (built-in, low overhead)
java -XX:StartFlightRecording=duration=60s,filename=recording.jfr -jar app.jar

# JVisualVM — GUI profiler
jvisualvm

# GC logging
java -Xlog:gc*:file=gc.log -jar app.jar

# JMH — Java Microbenchmark Harness
```

### अनुकूलन तकनीकें
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

## तैनाती
### डॉकरफ़ाइल
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

## पारिस्थितिकी तंत्र
### उपकरण बनाएँ
| उपकरण | उद्देश्य | नोट्स |
|------|------|-------|
| **मेवेन** | स्वचालन + निर्भरता प्रबंधन बनाएं | XML-आधारित (`pom.xml`); उद्यम के लिए उद्योग मानक |
| **ग्रैडल** | स्वचालन + निर्भरता प्रबंधन बनाएं | ग्रूवी/कोटलिन डीएसएल; बड़ी परियोजनाओं के लिए तेज़; एंड्रॉइड द्वारा उपयोग किया जाता है |
### ढाँचे
| ढाँचा | डोमेन | विवरण |
|----|-------|----|
| **स्प्रिंग बूट** | वेब/उद्यम | प्रमुख जावा फ्रेमवर्क - REST API, माइक्रोसर्विसेज, सुरक्षा, डेटा एक्सेस |
| **जकार्ता ईई** | उद्यम | जावा ईई के उत्तराधिकारी; मानकीकृत उद्यम एपीआई |
| **हाइबरनेट** | ओआरएम | वस्तु-संबंधपरक मानचित्रण; मानक जेपीए कार्यान्वयन |
| **माइक्रोनॉट/क्वार्कस** | बादल-मूल | तेज़ स्टार्टअप, कम मेमोरी - सर्वर रहित और कंटेनरों के लिए डिज़ाइन किया गया |
### परीक्षण
| उपकरण | उद्देश्य |
|------|---------|
| **जूनिट 5** | इकाई परीक्षण रूपरेखा |
| **मॉकिटो** | मॉकिंग फ्रेमवर्क |
| **AssertJ** | धाराप्रवाह दावे |
| **टेस्टकंटेनर** | डॉकर में वास्तविक डेटाबेस के साथ एकीकरण परीक्षण |
---

## जेवीएम पारिस्थितिकी तंत्र
| जेवीएम भाषा | जावा से संबंध |
|---|----||
| **कोटलिन** | जावा का आधुनिक विकल्प; Google की पसंदीदा Android भाषा; 100% जावा-संगत |
| **स्कैला** | कार्यात्मक + ओओपी हाइब्रिड; शक्तियां अपाचे स्पार्क |
| **क्लोजर** | जेवीएम पर लिस्प बोली; कार्यात्मक प्रोग्रामिंग |
| **ग्रूवी** | जेवीएम के लिए गतिशील स्क्रिप्टिंग; ग्रैडल बिल्ड फ़ाइलों में उपयोग किया जाता है |
ये सभी जावा लाइब्रेरीज़ का उपयोग कर सकते हैं, और जावा अपनी लाइब्रेरीज़ का उपयोग कर सकता है। जेवीएम सिर्फ जावा ही नहीं, बल्कि एक प्लेटफॉर्म है।
---

## जावा संस्करण
| संस्करण | वर्ष | प्रमुख विशेषताएँ |
|------|------|----------------|
| जावा 8 | 2014 | **एलटीएस** - लैम्ब्डा, स्ट्रीम एपीआई, वैकल्पिक, डिफ़ॉल्ट तरीके। अभी भी व्यापक रूप से उपयोग किया जाता है। |
| जावा 11 | 2018 | **एलटीएस** - HTTP क्लाइंट एपीआई, स्थानीय चर के लिए `var`, एकल-फ़ाइल स्रोत लॉन्चर |
| जावा 17 | 2021 | **एलटीएस** - सीलबंद कक्षाएं,`instanceof`के लिए पैटर्न मिलान, रिकॉर्ड, टेक्स्ट ब्लॉक |
| जावा 21 | 2023 | **एलटीएस** - **वर्चुअल थ्रेड्स** (प्रोजेक्ट लूम),`switch`के लिए पैटर्न मिलान, रिकॉर्ड पैटर्न |
| जावा 25 | 2025 | **एलटीएस** - स्ट्रिंग टेम्पलेट्स, आगे पैटर्न मिलान, विदेशी फ़ंक्शन एपीआई |
**एलटीएस** (दीर्घकालिक समर्थन) संस्करण कई वर्षों तक अपडेट प्राप्त करते हैं। उत्पादन के लिए, जावा 21 या बाद के संस्करण का उपयोग करें।
---

## जावा का उपयोग कब करें
| परिदृश्य | जावा क्यों | बेहतर विकल्प |
|---|---|-----|
| एंटरप्राइज़ बैकएंड | विशाल पारिस्थितिकी तंत्र, स्प्रिंग बूट, पैमाने पर सिद्ध | कोटलिन (वही जेवीएम, कम वर्बोज़) |
| एंड्रॉइड विकास | स्थापित, विशाल कोडबेस | कोटलिन (गूगल की पसंदीदा पसंद) |
| बड़ा डेटा (हडूप, स्पार्क, काफ्का) | पारिस्थितिकी तंत्र जावा/स्कैला | पर बनाया गया है डेटा विज्ञान पक्ष के लिए पायथन |
| वित्तीय प्रणालियाँ | प्रदर्शन + विश्वसनीयता + परिपक्व टूलींग | -- |
| माइक्रोसर्विसेज | स्प्रिंग बूट + क्लाउड-नेटिव फ्रेमवर्क | सरल सेवाओं के लिए जाएं |
| सरल स्क्रिप्ट | बहुत ज्यादा समारोह | अजगर, शैल |
| सीएलआई उपकरण | धीमा स्टार्टअप | जाओ, जंग |
---

## सारांश
जावा अब तक बनी सबसे महत्वपूर्ण प्रोग्रामिंग भाषाओं में से एक है। यह दुनिया की बैंकिंग प्रणाली, एंड्रॉइड फोन, बड़ी डेटा पाइपलाइन और एंटरप्राइज़ बैकएंड चलाता है। आधुनिक जावा (21+) जावा 8 से बहुत अलग भाषा है - यह अधिक संक्षिप्त, अधिक अभिव्यंजक और नई भाषाओं के साथ तेजी से प्रतिस्पर्धी है। जेवीएम पारिस्थितिकी तंत्र (कोटलिन, स्काला, क्लोजर) अपनी पहुंच को और आगे बढ़ाता है। उद्यम विकास के लिए, जावा एक सुरक्षित और शक्तिशाली विकल्प बना हुआ है।