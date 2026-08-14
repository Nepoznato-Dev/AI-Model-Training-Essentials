<!--
---
# Metadata
title: "Kotlin"
description: "Comprehensive reference for the Kotlin programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [kotlin, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "48 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
#कोटलिन
कोटलिन एक स्थिर रूप से टाइप की गई, संकलित प्रोग्रामिंग भाषा है जिसे JetBrains द्वारा विकसित किया गया है और पहली बार 2011 में जारी किया गया था (2016 में 1.0)। यह जावा वर्चुअल मशीन (जेवीएम) पर चलता है और जावा के साथ पूरी तरह से इंटरऑपरेबल है - जिसका अर्थ है कि आप कोटलिन से किसी भी जावा लाइब्रेरी का उपयोग कर सकते हैं और बिना किसी रैपर के जावा से कोटलिन कोड को कॉल कर सकते हैं। 2017 में, Google ने एंड्रॉइड विकास के लिए कोटलिन को पसंदीदा भाषा के रूप में घोषित किया, और तब से यह प्रमुख एंड्रॉइड भाषा बन गई है।
कोटलिन को जावा के समस्या बिंदुओं को ठीक करने के लिए डिज़ाइन किया गया था: शब्दाडंबर, अशक्त सूचक अपवाद, और अनुपलब्ध आधुनिक सुविधाएँ। परिणाम एक ऐसी भाषा है जो आधुनिक जावा की तरह महसूस होती है - संक्षिप्त, सुरक्षित और अभिव्यंजक - विशाल जावा पारिस्थितिकी तंत्र के साथ पूर्ण अनुकूलता बनाए रखते हुए।
---

## कोटलिन क्यों मायने रखता है
- **एंड्रॉइड मानक**: एंड्रॉइड के लिए Google की पसंदीदा भाषा। सबसे नया एंड्रॉइड कोड कोटलिन है।
- **100% जावा-संगत**: प्रत्येक जावा लाइब्रेरी, फ्रेमवर्क और टूल का उपयोग करें। धीरे-धीरे प्रवास करें.
- **शून्य सुरक्षा**: प्रकार प्रणाली संकलन समय पर शून्य सूचक अपवादों को रोकती है।
- **संक्षिप्त**: जावा की तुलना में काफी कम बॉयलरप्लेट - डेटा क्लास, एक्सटेंशन फ़ंक्शन, स्मार्ट कास्ट।
- **कोरआउटिंस**: एसिंक प्रोग्रामिंग के लिए हल्के धागे - जावा के कंप्लीटेबलफ्यूचर या कॉलबैक की तुलना में सरल।
- **मल्टीप्लेटफ़ॉर्म**: कोटलिन मल्टीप्लेटफ़ॉर्म आपको एंड्रॉइड, आईओएस, वेब और बैकएंड के बीच कोड साझा करने देता है।
- **सर्वर-साइड**: Ktor, स्प्रिंग बूट (पूर्ण कोटलिन समर्थन), और एक्सपोज़ड कोटलिन को बैकएंड के लिए व्यवहार्य बनाते हैं।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **जेवीएम निर्भरता** | JVM (या गैर-JVM लक्ष्यों के लिए कोटलिन/नेटिव) की आवश्यकता है | छोटी तैनाती के लिए GraalVM मूल छवि का उपयोग करें |
| **संकलन गति** | बड़ी परियोजनाओं के लिए जावा से धीमी | वृद्धिशील संकलन का प्रयोग करें; कोटलिन 2.0 इसमें सुधार करता है |
| **जावा डेवलपर्स के लिए सीखने की अवस्था** | एक्सटेंशन फ़ंक्शंस, कोरआउट्स, डीएसएल नई अवधारणाएँ हैं | धीरे-धीरे गोद लेना; अधिकांश जावा पैटर्न अभी भी काम करते हैं |
| **जावा से छोटा समुदाय** | कम कोटलिन-विशिष्ट संसाधन और पुस्तकालय | जावा के विशाल पारिस्थितिकी तंत्र का लाभ उठाएं |
| **कोटलिन मल्टीप्लेटफ़ॉर्म परिपक्वता** | उत्पादन iOS साझाकरण के लिए अभी भी विकास हो रहा है | साझा व्यावसायिक तर्क के लिए उपयोग करें; यूआई को मूल रखें |
---

## सिंटेक्स बुनियादी बातें
### चर और प्रकार
```kotlin
// Immutable (val) — preferred by default
val name = "Alice"
val age = 30
val score = 9.5
val active = true

// Mutable (var)
var count = 0
count++

// Type annotations (optional — compiler infers)
val greeting: String = "Hello"
val numbers: List<Int> = listOf(1, 2, 3)

// String templates
println("Hello, $name! Age: $age, Score: $score")
println("Length: ${name.length}")
```

### अशक्त सुरक्षा
```kotlin
// Non-nullable by default
var name: String = "Alice"
// name = null  // COMPILE ERROR

// Nullable types — must explicitly allow null
var nickname: String? = "Al"
nickname = null  // OK

// Safe call (?.) — returns null instead of crashing
val length = nickname?.length  // Int? — null if nickname is null

// Elvis operator (?:) — default value for null
val displayLength = nickname?.length ?: 0

// Safe cast (as?) — returns null instead of ClassCastException
val number = someValue as? Int

// Non-null assertion (!!): use only when you're certain
// val forced = nickname!!  // Crashes if null — avoid

// let with safe call — execute block only if not null
nickname?.let {
    println("Nickname is: $it")
}
```

### डेटा क्लासेस और एक्सटेंशन फ़ंक्शंस
```kotlin
// Data class — automatic equals(), hashCode(), toString(), copy()
data class User(val name: String, val age: Int, val email: String)

val alice = User("Alice", 30, "alice@example.com")
val olderAlice = alice.copy(age = 31)
println(alice)  // User(name=Alice, age=30, email=alice@example.com)

// Destructuring
val (name, age, email) = alice

// Extension functions — add methods to existing classes
fun String.isEmail(): Boolean = this.contains("@") && this.contains(".")
fun List<Int>.median(): Double {
    val sorted = this.sorted()
    val mid = size / 2
    return if (size % 2 == 0) (sorted[mid - 1] + sorted[mid]) / 2.0
           else sorted[mid].toDouble()
}

"alice@example.com".isEmail()  // true
listOf(3, 1, 4, 1, 5).median()  // 3.0
```

### कॉरआउटिंस - एसिंक प्रोग्रामिंग
```kotlin
import kotlinx.coroutines.*

// Suspend function — can be paused and resumed
suspend fun fetchUser(id: Int): User {
    delay(1000)  // Simulates network call
    return User("Alice", 30, "alice@example.com")
}

// Launch — fire and forget
CoroutineScope(Dispatchers.IO).launch {
    val user = fetchUser(1)
    println("Got user: $user")
}

// Async/await pattern
suspend fun loadDashboard(): Dashboard {
    val userDeferred = async { fetchUser(1) }
    val postsDeferred = async { fetchPosts(1) }

    val user = userDeferred.await()
    val posts = postsDeferred.await()

    return Dashboard(user, posts)
}

// Structured concurrency — automatically cancels children
suspend fun processAll() = coroutineScope {
    val jobs = (1..100).map { id ->
        launch { processItem(id) }
    }
    jobs.forEach { it.join() }
}
```

### मुहरबंद कक्षाएं और पैटर्न मिलान
```kotlin
// Sealed class — restricted class hierarchy (like enums with data)
sealed class Result<out T> {
    data class Success<T>(val data: T) : Result<T>()
    data class Error(val message: String, val cause: Throwable? = null) : Result<Nothing>()
    data object Loading : Result<Nothing>()
}

// When expression — exhaustive pattern matching
fun <T> Result<T>.describe(): String = when (this) {
    is Result.Success -> "Got data: $data"
    is Result.Error -> "Error: $message"
    is Result.Loading -> "Loading..."
}

// Smart casts — compiler automatically casts after type check
fun processValue(value: Any): String = when (value) {
    is String -> "String of length ${value.length}"
    is Int -> "Integer: $value"
    is List<*> -> "List with ${value.size} elements"
    else -> "Unknown type"
}
```

### उच्च-क्रम के कार्य
```kotlin
// Lambda expressions
val doubled = listOf(1, 2, 3).map { it * 2 }
val adults = users.filter { it.age >= 18 }
val total = users.sumOf { it.age }

// Group by
val byDepartment = users.groupBy { it.department }

// Chaining
val result = users
    .filter { it.age >= 18 }
    .sortedBy { it.name }
    .map { it.name }
    .joinToString(", ")

// Scope functions — idiomatic Kotlin
val config = Config().apply {
    apiUrl = "https://api.example.com"
    timeout = 30
    retries = 3
}

val json = user.let {
    """{"name": "${it.name}", "age": ${it.age}}"""
}
```

---

## उन्नत सिंटैक्स और पैटर्न
### जेनेरिक और प्रकार पैरामीटर
```kotlin
// Generic function with type constraint
fun <T : Comparable<T>> List<T>.sorted(): List<T> =
    this.toMutableList().apply { java.util.Collections.sort(this) }

// Generic class with variance annotations
interface Repository<T> {
    fun findById(id: Long): T?
    fun findAll(): List<T>
    fun save(entity: T): T
}

// Covariance (out) — producer: can return T but not accept T
interface Producer<out T> {
    fun produce(): T
}

// Contravariance (in) — consumer: can accept T but not return T
interface Consumer<in T> {
    fun consume(item: T)
}

// Reified type parameters — access type info at runtime (inline functions only)
inline fun <reified T> Gson.fromJson(json: String): T =
    this.fromJson(json, T::class.java)

val user: User = gson.fromJson<User>(jsonString)

// Generic constraints
fun <T> clone(item: T): T where T : Cloneable, T : Serializable {
    @Suppress("UNCHECKED_CAST")
    return item.clone() as T
}

// Star projection — when type parameter is unknown
fun printAll(items: List<*>) {
    items.forEach { println(it) }
}
```

### प्रतिबिंब के साथ मेटाप्रोग्रामिंग
```kotlin
import kotlin.reflect.*
import kotlin.reflect.full.*

// Class reflection
val klass = User::class
println(klass.simpleName)           // "User"
println(klass.memberProperties)     // [name, age, email]

// Calling functions reflectively
val constructor = klass.constructors.first()
val instance = constructor.call("Alice", 30, "alice@example.com")

// Accessing properties
val nameProp = klass.memberProperties.first { it.name == "name" }
val value = nameProp.get(instance)  // "Alice"

// Type checking at runtime with reified generics
inline fun <reified T> Any.castOrNull(): T? = this as? T

// Annotations and custom processing
annotation class Column(val name: String, val nullable: Boolean = false)

data class Employee(
    @Column("emp_name") val name: String,
    @Column("emp_age") val age: Int,
)

// Processing annotations at runtime
fun getColumnName(prop: KProperty<*>): String {
    return prop.findAnnotation<Column>()?.name ?: prop.name
}
```

### उन्नत डिस्ट्रक्चरिंग और पैटर्न मिलान
```kotlin
// Destructuring in lambdas
val map = mapOf("alice" to 30, "bob" to 25)
map.forEach { (key, value) ->
    println("$key is $value years old")
}

// Destructuring declarations with componentN
data class Point(val x: Int, val y: Int, val z: Int)

// Nested destructuring
data class Line(val start: Point, val end: Point)
val line = Line(Point(0, 0, 0), Point(1, 1, 1))
val (Point(x1, y1, _), Point(x2, y2, _)) = line

// Exhaustive when with sealed interfaces (Kotlin 1.7+)
sealed interface Shape
data class Circle(val radius: Double) : Shape
data class Rectangle(val width: Double, val height: Double) : Shape
data class Triangle(val base: Double, val height: Double) : Shape

fun area(shape: Shape): Double = when (shape) {
    is Circle -> Math.PI * shape.radius * shape.radius
    is Rectangle -> shape.width * shape.height
    is Triangle -> 0.5 * shape.base * shape.height
}

// When with complex conditions
fun classify(number: Int) = when {
    number < 0 -> "Negative"
    number == 0 -> "Zero"
    number in 1..9 -> "Single digit"
    number in 10..99 -> "Double digit"
    else -> "Large number"
}
```

### ऑपरेटर ओवरलोडिंग
```kotlin
data class Vector2D(val x: Double, val y: Double) {
    operator fun plus(other: Vector2D) =
        Vector2D(x + other.x, y + other.y)

    operator fun minus(other: Vector2D) =
        Vector2D(x - other.x, y - other.y)

    operator fun unaryMinus() = Vector2D(-x, -y)

    operator fun times(scalar: Double) =
        Vector2D(x * scalar, y * scalar)

    infix fun dot(other: Vector2D): Double =
        x * other.x + y * other.y

    operator fun component1() = x
    operator fun component2() = y
}

val v1 = Vector2D(1.0, 2.0)
val v2 = Vector2D(3.0, 4.0)
val sum = v1 + v2            // Vector2D(4.0, 6.0)
val scaled = v1 * 3.0        // Vector2D(3.0, 6.0)
val dotProduct = v1 dot v2   // 11.0
val (x, y) = v1              // Destructuring: x=1.0, y=2.0
```

### डीएसएल निर्माण पैटर्न
```kotlin
// Type-safe builder pattern (Kotlin's signature DSL approach)
@DslMarker
annotation class HtmlDsl

@HtmlDsl
class PageBuilder {
    private var title = ""
    private val bodyContent = mutableListOf<String>()

    fun title(text: String) { title = text }
    fun h1(text: String) { bodyContent.add("<h1>$text</h1>") }
    fun p(text: String) { bodyContent.add("<p>$text</p>") }

    fun build(): String = """
        <html>
        <head><title>$title</title></head>
        <body>${bodyContent.joinToString("\n")}</body>
        </html>
    """.trimIndent()
}

// DSL entry point
fun html(block: PageBuilder.() -> Unit): String =
    PageBuilder().apply(block).build()

// Usage — reads like a declarative language
val page = html {
    title("My Page")
    h1("Welcome")
    p("This is Kotlin DSL")
}
```
---

## समवर्ती एवं समांतरता (गहरा गोता)
### कोरटाइन डिस्पैचर्स और संदर्भ
```kotlin
import kotlinx.coroutines.*

// Dispatchers control which thread pool coroutines run on
suspend fun example() = coroutineScope {
    // Dispatchers.Main — UI thread (Android/Swing)
    launch(Dispatchers.Main) {
        updateUI()  // Must be on main thread
    }

    // Dispatchers.IO — shared pool for blocking I/O (network, disk)
    launch(Dispatchers.IO) {
        val data = readFromDatabase()
    }

    // Dispatchers.Default — CPU-intensive work (shared pool)
    launch(Dispatchers.Default) {
        val result = heavyComputation()
    }
}

// Switching contexts mid-coroutine
suspend fun fetchDataAndProcess(): String = withContext(Dispatchers.IO) {
    val raw = fetchFromNetwork()
    withContext(Dispatchers.Default) {
        processData(raw)
    }
}
```

### चैनल - कॉरआउट्स के बीच संचार
```kotlin
import kotlinx.coroutines.channels.*
import kotlinx.coroutines.*

// Channel — thread-safe queue for coroutine communication
suspend fun producerConsumer() = coroutineScope {
    val channel = Channel<Int>(capacity = Channel.BUFFERED)

    // Producer
    launch {
        for (i in 1..100) {
            channel.send(i)
            delay(50)
        }
        channel.close()
    }

    // Consumer
    launch {
        for (value in channel) {
            println("Received: $value")
        }
    }
}

// Fan-out / Fan-in pattern
suspend fun fanOutFanIn() = coroutineScope {
    val requests = Channel<Int>(Channel.UNLIMITED)
    val responses = Channel<String>(Channel.UNLIMITED)

    // Multiple workers
    val workers = (1..5).map { id ->
        launch(Dispatchers.Default) {
            for (request in requests) {
                val result = "Worker $id processed $request"
                responses.send(result)
            }
        }
    }

    // Send work
    launch {
        (1..20).forEach { requests.send(it) }
        requests.close()
    }

    // Collect results
    launch {
        for (response in responses) {
            println(response)
        }
    }
}
```

### प्रवाह - प्रतिक्रियाशील धाराएँ
```kotlin
import kotlinx.coroutines.flow.*

// Flow — cold asynchronous stream of values
fun numberFlow(): Flow<Int> = flow {
    for (i in 1..10) {
        delay(100)
        emit(i)
    }
}

// Collecting and transforming flows
suspend fun flowExample() {
    numberFlow()
        .filter { it % 2 == 0 }
        .map { it * it }
        .onEach { println("Processing: $it") }
        .take(3)
        .collect { println("Result: $it") }
}

// StateFlow — hot, state-holding flow (like LiveData)
class DashboardViewModel {
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()

    fun loadData() {
        viewModelScope.launch {
            _uiState.value = UiState.Loading
            try {
                val data = repository.fetch()
                _uiState.value = UiState.Success(data)
            } catch (e: Exception) {
                _uiState.value = UiState.Error(e.message ?: "Unknown error")
            }
        }
    }
}

sealed interface UiState {
    data object Loading : UiState
    data class Success(val data: List<Item>) : UiState
    data class Error(val message: String) : UiState
}

// SharedFlow — hot broadcast flow
class EventBus {
    private val _events = MutableSharedFlow<AppEvent>(replay = 0)
    val events = _events.asSharedFlow()

    suspend fun emit(event: AppEvent) {
        _events.emit(event)
    }
}
```

### संरचित समवर्ती और त्रुटि प्रबंधन
```kotlin
// SupervisorJob — child failure does not cancel siblings
suspend fun resilientWork() = supervisorScope {
    val job1 = launch {
        throw RuntimeException("Job 1 failed")
    }
    val job2 = launch {
        delay(100)
        println("Job 2 still runs")  // This still executes
    }
    joinAll(job1, job2)
}

// CoroutineExceptionHandler
val handler = CoroutineExceptionHandler { _, exception ->
    println("Caught: ${exception.message}")
}

// Timeout
suspend fun withTimeoutExample() {
    try {
        val result = withTimeout(5000) {
            fetchFromNetwork()
        }
        println(result)
    } catch (e: TimeoutCancellationException) {
        println("Request timed out")
    }
}

// Cancellation is cooperative
suspend fun cancellableWork() = coroutineScope {
    val job = launch {
        repeat(1000) { i ->
            println("Working $i...")
            delay(100)
            ensureActive()
        }
    }
    delay(500)
    job.cancelAndJoin()
}
```
---

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना
```
my-kotlin-project/
├── build.gradle.kts
├── settings.gradle.kts
├── gradle.properties
├── gradle/
│   └── wrapper/
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── src/
│   ├── main/
│   │   ├── kotlin/
│   │   │   └── com/example/
│   │   │       ├── Application.kt
│   │   │       ├── models/
│   │   │       ├── services/
│   │   │       └── controllers/
│   │   └── resources/
│   │       ├── application.yml
│   │       └── logback.xml
│   └── test/
│       └── kotlin/
│           └── com/example/
│               ├── services/
│               └── controllers/
└── gradlew, gradlew.bat
```

### कॉन्फ़िगरेशन बनाएँ (build.gradle.kts)
```kotlin
plugins {
    kotlin("jvm") version "2.0.0"
    kotlin("plugin.serialization") version "2.0.0"
    application
}

group = "com.example"
version = "1.0.0"

repositories {
    mavenCentral()
}

dependencies {
    implementation(kotlin("stdlib"))
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.8.1")
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.1")
    implementation("io.ktor:ktor-server-core:2.3.12")
    implementation("io.ktor:ktor-server-netty:2.3.12")
    implementation("ch.qos.logback:logback-classic:1.5.6")

    testImplementation(kotlin("test"))
    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.8.1")
    testImplementation("io.mockk:mockk:1.13.12")
}

application {
    mainClass.set("com.example.ApplicationKt")
}

tasks.test {
    useJUnitPlatform()
}

kotlin {
    jvmToolchain(21)
}
```

### निर्भरता प्रबंधन आदेश
```bash
# Build and run
./gradlew build
./gradlew run

# Dependency insights
./gradlew dependencies --configuration runtimeClasspath

# Clean and rebuild
./gradlew clean build

# Run specific tests
./gradlew test --tests "com.example.services.UserServiceTest"

# Generate Gradle wrapper
./gradlew wrapper --gradle-version 8.8
```

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
```yaml
# .github/workflows/ci.yml
name: Kotlin CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up JDK 21
        uses: actions/setup-java@v4
        with:
          java-version: '21'
          distribution: 'temurin'
          cache: gradle

      - name: Setup Gradle
        uses: gradle/actions/setup-gradle@v3

      - name: Build
        run: ./gradlew build

      - name: Run Tests
        run: ./gradlew test

      - name: Run Detekt (Static Analysis)
        run: ./gradlew detekt

      - name: Code Coverage
        run: ./gradlew jacocoTestReport

      - name: Upload Coverage
        uses: codecov/codecov-action@v4
        with:
          file: build/reports/jacoco/test/jacocoTestReport.xml
```

---

## परीक्षण
### परीक्षण ढाँचे और सेटअप
```kotlin
// build.gradle.kts — testing dependencies
dependencies {
    testImplementation(kotlin("test"))
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.3")
    testImplementation("io.mockk:mockk:1.13.12")
    testImplementation("org.assertj:assertj-core:3.26.0")
    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.8.1")
}
```

### मॉकिंग के साथ यूनिट टेस्ट
```kotlin
import org.junit.jupiter.api.*
import org.junit.jupiter.api.Assertions.*
import io.mockk.*

class UserServiceTest {

    private val userRepository = mockk<UserRepository>()
    private val userService = UserService(userRepository)

    @BeforeEach
    fun setup() {
        clearAllMocks()
    }

    @Test
    fun `should create user with valid data`() {
        // Given
        val request = CreateUserRequest("Alice", 30)
        every { userRepository.save(any()) } returns User(1, "Alice", 30)

        // When
        val result = userService.createUser(request)

        // Then
        assertEquals("Alice", result.name)
        assertEquals(30, result.age)
        verify(exactly = 1) { userRepository.save(any()) }
    }

    @Test
    fun `should throw when name is blank`() {
        val request = CreateUserRequest("", 30)

        assertThrows<IllegalArgumentException> {
            userService.createUser(request)
        }
    }

    @Test
    fun `should find user by id`() {
        every { userRepository.findById(1) } returns User(1, "Alice", 30)

        val user = userService.findById(1)

        assertNotNull(user)
        assertEquals("Alice", user!!.name)
    }
}
```

### कोरटाइन का परीक्षण
```kotlin
import kotlinx.coroutines.test.*
import org.junit.jupiter.api.Test

class CoroutineServiceTest {

    @Test
    fun `should fetch data concurrently`() = runTest {
        val repository = mockk<DataRepository>()
        coEvery { repository.fetchUsers() } returns listOf(User(1, "Alice", 30))
        coEvery { repository.fetchPosts() } returns listOf(Post(1, "Hello"))

        val service = DashboardService(repository)
        val result = service.loadDashboard()

        assertEquals(1, result.users.size)
        assertEquals(1, result.posts.size)
    }
}
```

### टेस्ट कमांड
```bash
# Run all tests
./gradlew test

# Run with coverage report
./gradlew test jacocoTestReport

# Run specific test class
./gradlew test --tests "com.example.UserServiceTest"

# Continuous testing (rerun on changes)
./gradlew test --continuous
```
---

## अंतरसंचालनीयता
### जावा इंटरऑपरेबिलिटी
```kotlin
// Calling Java from Kotlin — seamless
val list = java.util.ArrayList<String>()
list.add("Hello")
val size = list.size

// Handling Java nullability (platform types)
val javaString: String! = javaClass.getNullableString()
val safeLength = javaString?.length  // Safe call recommended

// @JvmOverloads — generates overloaded methods for Java callers
@JvmOverloads
fun configure(host: String, port: Int = 8080, secure: Boolean = true) {
    // ...
}

// SAM conversions (Java functional interfaces)
val runnable = Runnable { println("Running") }
val comparator = Comparator<String> { a, b -> a.length - b.length }

// @JvmStatic — expose as static method for Java
class Config {
    companion object {
        @JvmStatic
        fun getDefault(): Config = Config()
    }
}
// Java: Config.getDefault()

// @JvmField — expose property as field
class Constants {
    companion object {
        @JvmField
        val MAX_SIZE = 100
    }
}
// Java: Constants.MAX_SIZE
```

### कोटलिन/नेटिव और सी इंटरऑप
```kotlin
// Kotlin/Native can call C libraries directly via cinterop
// interop.def file:
// headers = zlib.h
// package = zlib

import zlib.*
import kotlinx.cinterop.*

fun compressData(data: ByteArray): ByteArray {
    val compressedSize = compressBound(data.size.toULong())
    val output = ByteArray(compressedSize.toInt())
    // ... interop calls via cinterop bindings
    return output
}
```

### कोटलिन/जेएस इंटरऑप
```kotlin
// External declarations for JavaScript libraries
@JsModule("lodash")
@JsNonModule
external object Lodash {
    fun <T> chunk(array: Array<T>, size: Int): Array<Array<T>>
    fun <T> uniq(array: Array<T>): Array<T>
    fun camelCase(string: String): String
}

// Using dynamic type for untyped JS
fun callJsLibrary() {
    val lib: dynamic = js("require('some-js-library')")
    lib.doSomething("arg")
}
```

---

## डिज़ाइन पैटर्न
### सिंगलटन (डिफ़ॉल्ट रूप से थ्रेड-सुरक्षित)
```kotlin
// Kotlin object — thread-safe singleton by language design
object DatabaseConnection {
    private var connection: Connection? = null

    fun getConnection(): Connection {
        return connection ?: synchronized(this) {
            connection ?: createConnection().also { connection = it }
        }
    }

    private fun createConnection(): Connection {
        return DriverManager.getConnection("jdbc:postgresql://localhost/mydb")
    }
}

// Usage
val conn = DatabaseConnection.getConnection()
```

### बिल्डर पैटर्न (मुहावरेदार कोटलिन)
```kotlin
class HttpRequest private constructor(
    val url: String,
    val method: String,
    val headers: Map<String, String>,
    val body: String?,
    val timeout: Int,
) {
    class Builder(private val url: String) {
        var method: String = "GET"
        var timeout: Int = 30_000
        private val headers = mutableMapOf<String, String>()
        private var body: String? = null

        fun header(key: String, value: String) = apply { headers[key] = value }
        fun body(content: String) = apply { this.body = content }
        fun build() = HttpRequest(url, method, headers.toMap(), body, timeout)
    }
}

// Usage
val request = HttpRequest.Builder("https://api.example.com/users")
    .apply {
        method = "POST"
        header("Content-Type", "application/json")
        header("Authorization", "Bearer token123")
        body("""{"name": "Alice"}""")
        timeout = 5000
    }
    .build()
```

### लैम्बडास के साथ रणनीति पैटर्न
```kotlin
// Kotlin makes strategy pattern trivial with function types
class Sorter<T>(private val comparator: (T, T) -> Int) {
    fun sort(list: List<T>): List<T> = list.sortedWith(Comparator(comparator))
}

// Usage — strategies are just lambdas
val byName = Sorter<User> { a, b -> a.name.compareTo(b.name) }
val byAge = Sorter<User> { a, b -> a.age - b.age }

val users = listOf(User("Charlie", 25), User("Alice", 30), User("Bob", 20))
println(byName.sort(users))
println(byAge.sort(users))
```

### जेनेरिक के साथ रिपॉजिटरी पैटर्न
```kotlin
interface Repository<T, ID> {
    suspend fun findById(id: ID): T?
    suspend fun findAll(): List<T>
    suspend fun save(entity: T): T
    suspend fun deleteById(id: ID)
}

class UserRepository(
    private val database: Database
) : Repository<User, Long> {

    override suspend fun findById(id: Long): User? =
        database.query { it.selectFrom(users).where(users.id eq id) }

    override suspend fun findAll(): List<User> =
        database.query { it.selectFrom(users).fetchAll() }

    override suspend fun save(entity: User): User {
        database.execute { it.insertInto(users).values(entity.toMap()) }
        return entity
    }

    override suspend fun deleteById(id: Long) {
        database.execute { it.deleteFrom(users).where(users.id eq id) }
    }
}
```

---

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
```bash
# JVM profiling with VisualVM
./gradlew run &
visualvm  # Attach to the running process

# Async Profiler (low-overhead CPU and allocation profiling)
java -agentpath:/path/to/libasyncProfiler.so=start,event=cpu,file=profile.html \
    -jar build/libs/my-app.jar

# JMH benchmarks for micro-benchmarking
dependencies {
    implementation("org.openjdk.jmh:jmh-core:1.37")
    annotationProcessor("org.openjdk.jmh:jmh-generator-annprocess:1.37")
}
```

### अनुकूलन तकनीकें
```kotlin
// 1. Inline functions — eliminate lambda allocation overhead
inline fun <T> List<T>.customEach(action: (T) -> Unit) {
    for (item in this) action(item)
}

// 2. Sequence for large collections — lazy evaluation
val result = largeList
    .asSequence()
    .filter { it.isActive }
    .map { it.transform() }
    .take(10)
    .toList()  // Only processes until 10 items found

// 3. Primitive arrays — avoid boxing overhead
val intArray = intArrayOf(1, 2, 3, 4, 5)
val doubleArray = DoubleArray(1000) { it * 0.1 }

// 4. Value classes (inline classes) — zero runtime overhead wrappers
@JvmInline
value class UserId(val value: Long)

@JvmInline
value class Email(val value: String) {
    init { require(value.contains("@")) { "Invalid email" } }
}

// Compiled to primitive types at runtime — no allocation
fun findUser(id: UserId): User? { /* ... */ }
```

---

## तैनाती
### शैडो प्लगइन के साथ मोटा जार
```kotlin
// build.gradle.kts
plugins {
    id("com.github.johnrengelman.shadow") version "8.1.1"
}
// Build: ./gradlew shadowJar
// Run:  java -jar build/libs/my-app-1.0.0-all.jar
```

### डॉकर परिनियोजन
```dockerfile
# Multi-stage Dockerfile
FROM gradle:8.8-jdk21 AS builder
WORKDIR /app
COPY build.gradle.kts settings.gradle.kts ./
COPY src ./src
RUN gradle shadowJar --no-daemon

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=builder /app/build/libs/*-all.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### GraalVM मूल छवि
```kotlin
// build.gradle.kts
plugins {
    id("org.graalvm.buildtools.native") version "0.10.2"
}
// Build native binary: ./gradlew nativeCompile
// Startup time: <100ms, Memory: ~30MB (vs ~300MB for JVM)
```

### कोटलिन मल्टीप्लेटफ़ॉर्म परिनियोजन
```kotlin
// build.gradle.kts — Multiplatform setup
plugins {
    kotlin("multiplatform") version "2.0.0"
}

kotlin {
    jvm()
    iosX64(); iosArm64(); iosSimulatorArm64()

    sourceSets {
        val commonMain by getting {
            dependencies {
                implementation("io.ktor:ktor-client-core:2.3.12")
                implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.8.1")
            }
        }
        val jvmMain by getting {
            dependencies {
                implementation("io.ktor:ktor-client-cio:2.3.12")
            }
        }
        val iosMain by creating {
            dependsOn(commonMain)
            dependencies {
                implementation("io.ktor:ktor-client-darwin:2.3.12")
            }
        }
    }
}
```

---

## पारिस्थितिकी तंत्र
### ढाँचे
| ढाँचा | डोमेन |
|--------|-------|
| **जेटपैक कंपोज़** | आधुनिक एंड्रॉइड यूआई टूलकिट |
| **केटोर** | हल्के सर्वर-साइड वेब फ्रेमवर्क |
| **स्प्रिंग बूट** | एंटरप्राइज़ बैकएंड के लिए पूर्ण कोटलिन समर्थन |
| **कोटलिन मल्टीप्लेटफ़ॉर्म** | एंड्रॉइड, आईओएस, वेब, डेस्कटॉप के बीच कोड साझा करें |
| **उजागर** | कोटलिन एसक्यूएल लाइब्रेरी (प्रकार-सुरक्षित प्रश्न) |
| **कोइन** | निर्भरता इंजेक्शन ढांचा |
### उपकरण बनाएँ
| उपकरण | उद्देश्य |
|------|---------|
| **ग्रैडल (कोटलिन डीएसएल)** | बिल्ड सिस्टम - कोटलिन पसंदीदा बिल्ड स्क्रिप्ट भाषा है |
| **इंटेलिजे आइडिया** | JetBrains द्वारा IDE - सर्वोत्तम कोटलिन समर्थन |
---

## कोटलिन का उपयोग कब करें
| परिदृश्य | क्यों कोटलिन | बेहतर विकल्प |
|---|----|-----|
| एंड्रॉइड विकास | गूगल की पसंदीदा भाषा | जावा (विरासत कोडबेस के लिए) |
| जेवीएम बैकएंड | आधुनिक जावा विकल्प | जावा, जाओ |
| क्रॉस-प्लेटफ़ॉर्म (साझा तर्क) | कोटलिन मल्टीप्लेटफ़ॉर्म | स्पंदन (यूआई साझाकरण के लिए) |
| डेस्कटॉप ऐप्स | कंपोज़ मल्टीप्लेटफ़ॉर्म के साथ संभव | सी#, मूल निवासी के लिए स्विफ्ट |
| सामान्य जेवीएम अनुप्रयोग | जावा से कम वर्बोज़ | बड़ी टीमों के लिए जावा |
| गैर-जेवीएम सिस्टम प्रोग्रामिंग | प्राथमिक लक्ष्य नहीं | जंग, जाओ, सी |
| वेब फ्रंटएंड | कोटलिन/जेएस मौजूद है लेकिन सीमित है | टाइपस्क्रिप्ट, जावास्क्रिप्ट |
| डेटा साइंस/एमएल | पारिस्थितिकी तंत्र नहीं | पायथन, आर |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: कोटलिन की शून्य सुरक्षा सुविधाएँ वास्तव में कैसे काम करती हैं?
**ए:** कोटलिन संकलन समय पर निरर्थक (`String?`) और गैर-शून्य (`String`) प्रकारों के बीच अंतर करता है। कंपाइलर आपको शून्य जांच के बिना शून्य प्रकारों पर कॉल करने के तरीकों से रोकता है। सुरक्षित कॉल (`?.`), एल्विस ऑपरेटर (`?:`), और गैर-शून्य दावा (`!!`) अलग-अलग रणनीतियाँ प्रदान करते हैं। शून्य जांच के बाद स्मार्ट कास्ट स्वचालित रूप से संकीर्ण प्रकार के होते हैं।
```kotlin
var name: String? = null

// Safe call — returns null if name is null
val length: Int? = name?.length

// Elvis operator — provide default
val display: String = name ?: "Anonymous"

// Smart cast — compiler narrows type after check
fun process(user: String?) {
    if (user != null) {
        println(user.length)  // Smart cast to String (non-null)
    }
}

// let with safe call
name?.let {
    println("Name is $it")  // Only runs if name is not null
}

// Non-null assertion — crashes if null (avoid in production)
val forced: String = name!!  // Throws NullPointerException if null
```

### Q2: कॉरआउटिन क्या हैं, और वे थ्रेड से कैसे भिन्न हैं?
**ए:** कोरूटाइन हल्के, सहयोगी कार्य हैं जो धागों पर चलते हैं। वे निष्पादन को निलंबित कर सकते हैं (थ्रेड को अवरुद्ध किए बिना) और बाद में फिर से शुरू कर सकते हैं। कुछ धागों पर लाखों कोरआउटिन चल सकते हैं। `suspend`फ़ंक्शंस को केवल कोरआउट्स या अन्य सस्पेंड फ़ंक्शंस से कॉल किया जा सकता है। कोरआउटिन स्कोप जीवनचक्र को नियंत्रित करते हैं - जब कोई स्कोप रद्द कर दिया जाता है, तो उसके सभी कोरआउटाइन रद्द कर दिए जाते हैं।
```kotlin
import kotlinx.coroutines.*

// Basic coroutine
CoroutineScope(Dispatchers.Main).launch {
    val user = withContext(Dispatchers.IO) {
        fetchUserFromNetwork()  // Suspends, doesn't block
    }
    textView.text = user.name   // Back on Main thread
}

// Concurrent execution
suspend fun loadDashboard(): Dashboard {
    coroutineScope {
        val userDeferred = async { fetchUser() }
        val postsDeferred = async { fetchPosts() }
        val user = userDeferred.await()
        val posts = postsDeferred.await()
        Dashboard(user, posts)
    }
}

// Flow — cold async stream
fun observePrices(): Flow<Double> = flow {
    while (true) {
        emit(fetchCurrentPrice())
        delay(1000)
    }
}

// Collect flow
lifecycleScope.launch {
    observePrices()
        .filter { it > 100.0 }
        .collect { price -> updateUI(price) }
}
```

### Q3: डेटा क्लास, सीलबंद क्लास और वैल्यू क्लास क्या हैं?
**ए:** डेटा कक्षाएं स्वचालित रूप से`equals`,`hashCode`,`toString`,`copy`, और`componentN`फ़ंक्शंस उत्पन्न करती हैं - डेटा धारकों के लिए आदर्श। सीलबंद वर्ग वंशानुक्रम को प्रतिबंधित करते हैं - सभी उपवर्ग एक ही फ़ाइल में होने चाहिए - संपूर्ण`when`अभिव्यक्तियों को सक्षम करना। मान वर्ग रनटाइम (इनलाइन क्लास) पर शून्य ओवरहेड के साथ एकल मान लपेटते हैं।
```kotlin
// Data class — auto-generates equals/hashCode/toString/copy
data class User(val name: String, val email: String, val age: Int)

val alice = User("Alice", "alice@example.com", 30)
val bob = alice.copy(name = "Bob")
val (name, email, age) = alice  // Destructuring

// Sealed class — exhaustive when
sealed class Result<out T> {
    data class Success<T>(val data: T) : Result<T>()
    data class Error(val exception: Throwable) : Result<Nothing>()
    data object Loading : Result<Nothing>()
}

fun handle(result: Result<User>) = when (result) {
    is Result.Success -> showUser(result.data)
    is Result.Error -> showError(result.exception)
    is Result.Loading -> showSpinner()
    // No 'else' needed — compiler knows all cases are covered
}

// Value class — zero-overhead wrapper
@JvmInline
value class UserId(val value: String)
fun getUser(id: UserId) { /* ... */ }
// At runtime, UserId is just a String — no object allocation
```

### Q4: एक्सटेंशन फ़ंक्शंस कैसे काम करते हैं, और उनकी सीमाएँ क्या हैं?
**ए:** एक्सटेंशन फ़ंक्शंस विरासत या संशोधन के बिना मौजूदा प्रकारों में विधियाँ जोड़ते हैं। उन्हें स्थिर रूप से हल किया जाता है (घोषित प्रकार के आधार पर, रनटाइम प्रकार के आधार पर नहीं)। वे निजी सदस्यों तक नहीं पहुंच सकते. एक्सटेंशन गुण समान रूप से कार्य करते हैं. कोटलिन की मानक लाइब्रेरी और एंड्रॉइड विकास में इनका बड़े पैमाने पर उपयोग किया जाता है।
```kotlin
// Extension function
fun String.isEmail(): Boolean = contains("@") && contains(".")
fun Int.toOrdinal(): String = "${this}${when (this % 10) {
    1 -> "st"; 2 -> "nd"; 3 -> "rd"; else -> "th"
}}"

// Extension with receiver
fun <T> List<T>.secondOrNull(): T? = if (size >= 2) this[1] else null

// Extension property
val String.wordCount: Int get() = split("\\s+".toRegex()).size

// Scoped extensions
class Database {
    fun query(sql: String): List<Row> = TODO()
}

fun Database.users() = query("SELECT * FROM users")

// Usage
"test@example.com".isEmail()  // true
42.toOrdinal()                // "42nd"
"hello world foo".wordCount   // 3
```

### Q5: कोटलिन मल्टीप्लेटफ़ॉर्म क्या है, और मुझे इसका उपयोग कब करना चाहिए?
**ए:** कोटलिन मल्टीप्लेटफ़ॉर्म (केएमपी) आपको प्लेटफ़ॉर्म-विशिष्ट यूआई रखते हुए प्लेटफ़ॉर्म (एंड्रॉइड, आईओएस, वेब, डेस्कटॉप, सर्वर) के बीच कोड साझा करने देता है। व्यावसायिक तर्क, नेटवर्किंग और डेटा परतें साझा की जा सकती हैं; यूआई मूल रहता है. इसका उपयोग तब करें जब आपके पास एक ऐसी टीम हो जो कोटलिन को जानती हो और पूर्ण क्रॉस-प्लेटफ़ॉर्म (जैसे फ़्लटर) पर जाए बिना कोड शेयरिंग को अधिकतम करना चाहती हो।
```kotlin
// commonMain — shared code
expect class Platform() {
    val name: String
}

// androidMain
actual class Platform {
    actual val name = "Android ${Build.VERSION.SDK_INT}"
}

// iosMain
actual class Platform {
    actual val name = UIDevice.currentDevice.systemName()
}

// Shared networking
interface ApiClient {
    suspend fun getUsers(): List<User>
}

class ApiClientImpl(private val httpClient: HttpClient) : ApiClient {
    override suspend fun getUsers(): List<User> {
        return httpClient.get("/api/users").body()
    }
}
```

---

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: एक टाइप-सेफ बिल्डर डीएसएल बनाएं
**समस्या कथन:** संकलन-समय सुरक्षा के साथ HTML दस्तावेज़ बनाने के लिए एक कोटलिन डीएसएल बनाएं। डीएसएल को वैध HTML संरचना लागू करनी चाहिए (उदाहरण के लिए,`<head>`केवल`<html>`के अंदर,`<li>`केवल`<ul>`या`<ol>`के अंदर)।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) स्कोप लीक को रोकने के लिए`@DslMarker`के साथ बिल्डर फ़ंक्शन, (2) रिसीवर-आधारित डीएसएल सिंटैक्स, (3) वैध नेस्टिंग का संकलन-समय प्रवर्तन। कोटलिन के टाइप-सेफ बिल्डर्स और`@DslMarker`एनोटेशन को इसके लिए डिज़ाइन किया गया है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- स्कोप कंट्रोल एनोटेशन बनाने के लिए`@DslMarker`का उपयोग करें।
- प्रत्येक HTML तत्व अपने मान्य बच्चों के लिए बिल्डर विधियों वाला एक वर्ग है।
-`@HtmlTagMarker`चाइल्ड स्कोप के अंदर पैरेंट स्कोप विधियों तक पहुंच को रोकता है।
- स्वच्छ सिंटैक्स के लिए`invoke`ऑपरेटर का उपयोग करें।
**चरण 3 - समाधान लागू करें:**
```kotlin
@DslMarker
annotation class HtmlTagMarker

@HtmlTagMarker
class HTML {
    private val children = mutableListOf<String>()

    fun head(init: HEAD.() -> Unit) {
        val head = HEAD().apply(init)
        children.add(head.render())
    }

    fun body(init: BODY.() -> Unit) {
        val body = BODY().apply(init)
        children.add(body.render())
    }

    fun render(): String = buildString {
        appendLine("<html>")
        children.forEach { appendLine("  $it") }
        appendLine("</html>")
    }
}

@HtmlTagMarker
class HEAD {
    private val children = mutableListOf<String>()

    fun title(text: String) { children.add("<title>$text</title>") }
    fun meta(name: String, content: String) {
        children.add("<meta name=\"$name\" content=\"$content\">")
    }

    fun render(): String = buildString {
        appendLine("<head>")
        children.forEach { appendLine("    $it") }
        appendLine("</head>")
    }
}

@HtmlTagMarker
class BODY {
    private val children = mutableListOf<String>()

    fun h1(text: String) { children.add("<h1>$text</h1>") }
    fun p(text: String) { children.add("<p>$text</p>") }
    fun div(init: DIV.() -> Unit) {
        children.add(DIV().apply(init).render())
    }
    fun ul(init: UL.() -> Unit) {
        children.add(UL().apply(init).render())
    }

    fun render(): String = buildString {
        appendLine("<body>")
        children.forEach { appendLine("    $it") }
        appendLine("</body>")
    }
}

@HtmlTagMarker
class DIV {
    private val children = mutableListOf<String>()
    var cssClass: String = ""
    fun p(text: String) { children.add("<p>$text</p>") }
    fun render(): String {
        val cls = if (cssClass.isNotEmpty()) " class=\"$cssClass\"" else ""
        return "<div$cls>${children.joinToString("")}</div>"
    }
}

@HtmlTagMarker
class UL {
    private val items = mutableListOf<String>()
    fun li(text: String) { items.add("<li>$text</li>") }
    fun render(): String = "<ul>${items.joinToString("")}</ul>"
}

fun html(init: HTML.() -> Unit): String = HTML().apply(init).render()

// Usage — compile-time safe
val page = html {
    head {
        title("My Page")
        meta("viewport", "width=device-width")
    }
    body {
        h1("Welcome")
        p("This is a type-safe HTML builder.")
        div {
            cssClass = "container"
            p("Inside a div")
        }
        ul {
            li("Item 1")
            li("Item 2")
            li("Item 3")
        }
    }
}
// title() is NOT accessible inside body {} — prevented by @DslMarker
// li() is NOT accessible inside body {} — only inside ul {}
```

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- प्रकार की सुरक्षा:`@DslMarker`स्कोप को लीक होने से रोकता है -`title()``body {}` के अंदर पहुंच योग्य नहीं है।
- कंपाइलर कंपाइल समय पर वैध नेस्टिंग लागू करता है - रनटाइम जांच की आवश्यकता नहीं है।
- विस्तारशीलता: उपयुक्त चाइल्ड विधियों के साथ कक्षाएं बनाकर नए तत्व जोड़ें।
- उत्पादन: व्यापक, अच्छी तरह से परीक्षण किए गए HTML DSL के लिए`kotlinx.html`का उपयोग करें।
### समस्या 2: कॉरआउट्स के साथ एक राज्य मशीन लागू करें
**समस्या कथन:** एक गेम चरित्र के लिए एक कोरआउटिन-आधारित राज्य मशीन बनाएं जो इनपुट घटनाओं, राज्यों के बीच संक्रमण को संसाधित करता है, और एनीमेशन कॉलबैक का समर्थन करता है।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) प्रवेश/निकास क्रियाओं वाले राज्य, (2) घटना-संचालित बदलाव, (3) कोरआउटिन-आधारित प्रोसेसिंग लूप, (4) राज्य बदलाव पर एनीमेशन कॉलबैक। राज्य मशीन एक चैनल से लंबे समय तक चलने वाली कोरटाइन उपभोग करने वाली घटनाओं के रूप में चलती है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- राज्यों और घटनाओं के लिए सीलबंद वर्ग का उपयोग करें।
- इवेंट पासिंग के लिए`Channel`का उपयोग करें।
- स्टेट मशीन लूप`for (event in channel)`के साथ घटनाओं का उपभोग करता है।
- परिवर्तन निकास/प्रवेश कॉलबैक को ट्रिगर करते हैं।
**चरण 3 - समाधान लागू करें:**
```kotlin
sealed class GameState {
    data object Idle : GameState()
    data object Walking : GameState()
    data object Running : GameState()
    data object Attacking : GameState()
    data class Dead(val cause: String) : GameState()
}

sealed class GameEvent {
    data object Move : GameEvent()
    data object Run : GameEvent()
    data object Attack : GameEvent()
    data object Stop : GameEvent()
    data class TakeDamage(val amount: Int) : GameEvent()
}

class CharacterStateMachine(
    private val scope: CoroutineScope,
    private val onStateChange: suspend (GameState) -> Unit
) {
    private var currentState: GameState = GameState.Idle
    private val eventChannel = Channel<GameEvent>(Channel.UNLIMITED)
    var health: Int = 100; private set

    init {
        scope.launch {
            onStateChange(currentState)
            for (event in eventChannel) {
                processEvent(event)
            }
        }
    }

    suspend fun send(event: GameEvent) {
        eventChannel.send(event)
    }

    private suspend fun processEvent(event: GameEvent) {
        val newState = when (currentState) {
            is GameState.Dead -> return  // No transitions from dead

            GameState.Idle -> when (event) {
                GameEvent.Move -> GameState.Walking
                GameEvent.Run -> GameState.Running
                GameEvent.Attack -> GameState.Attacking
                is GameEvent.TakeDamage -> handleDamage(event)
                else -> currentState
            }

            GameState.Walking -> when (event) {
                GameEvent.Stop -> GameState.Idle
                GameEvent.Run -> GameState.Running
                GameEvent.Attack -> GameState.Attacking
                is GameEvent.TakeDamage -> handleDamage(event)
                else -> currentState
            }

            GameState.Running -> when (event) {
                GameEvent.Stop -> GameState.Idle
                GameEvent.Move -> GameState.Walking
                GameEvent.Attack -> GameState.Attacking
                is GameEvent.TakeDamage -> handleDamage(event)
                else -> currentState
            }

            GameState.Attacking -> when (event) {
                GameEvent.Stop -> GameState.Idle
                GameEvent.Move -> GameState.Walking
                is GameEvent.TakeDamage -> handleDamage(event)
                else -> currentState
            }
        }

        if (newState != currentState) {
            currentState = newState
            onStateChange(newState)
        }
    }

    private suspend fun handleDamage(event: GameEvent.TakeDamage): GameState {
        health -= event.amount
        return if (health <= 0) GameState.Dead("Defeated") else currentState
    }
}

// Usage
val machine = CharacterStateMachine(
    scope = CoroutineScope(Dispatchers.Default)
) { state ->
    println("State changed to: $state")
    when (state) {
        GameState.Idle -> playAnimation("idle")
        GameState.Walking -> playAnimation("walk")
        GameState.Running -> playAnimation("run")
        GameState.Attacking -> playAnimation("attack")
        is GameState.Dead -> playAnimation("death")
    }
}

machine.send(GameEvent.Move)      // Walking
machine.send(GameEvent.Run)       // Running
machine.send(GameEvent.Attack)    // Attacking
machine.send(GameEvent.TakeDamage(120))  // Dead
```

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- प्रकार की सुरक्षा: सीलबंद कक्षाएं सुनिश्चित करती हैं कि सभी राज्यों और घटनाओं को नियंत्रित किया जाए। कंपाइलर गुम हुए ट्रांज़िशन को पकड़ लेता है।
- कॉरआउटिन-आधारित: घटनाओं को बिना अवरोध के क्रमिक रूप से संसाधित किया जाता है। चैनल बैकप्रेशर प्रदान करता है।
- जीवनचक्र: दायरा रद्द करने से राज्य मशीन साफ़ रूप से बंद हो जाती है।
- उत्पादन: जटिल राज्य मशीनों के लिए,`tinder-statemachine`का उपयोग करें या औपचारिक राज्य मशीन लाइब्रेरी के साथ राज्यों को मॉडल करें।
---

## सारांश
कोटलिन आधुनिक जावा है जो ठीक से तैयार किया गया है। यह जेवीएम पर चलता है, सभी जावा लाइब्रेरीज़ का उपयोग करता है, लेकिन नल पॉइंटर अपवादों को समाप्त करता है, बॉयलरप्लेट को कम करता है, और कॉरआउट्स, एक्सटेंशन फ़ंक्शंस और सीलबंद क्लासेस जैसी आधुनिक सुविधाएं जोड़ता है। Android विकास के लिए, कोटलिन स्पष्ट विकल्प है। जेवीएम बैकएंड के लिए, यह जावा का एक आकर्षक विकल्प है। कोटलिन मल्टीप्लेटफ़ॉर्म ने अपनी पहुंच आईओएस और उससे आगे तक बढ़ा दी है। यदि आप पहले से ही जावा जानते हैं, तो कोटलिन सीखना एक स्वाभाविक और फायदेमंद अगला कदम है।