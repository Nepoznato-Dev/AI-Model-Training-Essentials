---
# Metadata
title: "Kotlin"
description: "Comprehensive reference for the Kotlin programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

#কোটলিন
কোটলিন হল একটি স্ট্যাটিকলি টাইপ করা, কম্পাইল করা প্রোগ্রামিং ল্যাঙ্গুয়েজ যা জেটব্রেইন্স দ্বারা ডেভেলপ করা হয়েছে এবং প্রথম প্রকাশিত হয়েছে 2011 সালে (2016 সালে 1.0)। এটি জাভা ভার্চুয়াল মেশিনে (JVM) চলে এবং জাভার সাথে সম্পূর্ণ আন্তঃঅপারেবল — যার অর্থ আপনি কোটলিন থেকে যেকোন জাভা লাইব্রেরি ব্যবহার করতে পারেন এবং জাভা থেকে কোটলিন কোডকে কোনো মোড়ক ছাড়াই কল করতে পারেন। 2017 সালে, গুগল অ্যান্ড্রয়েড ডেভেলপমেন্টের জন্য পছন্দের ভাষা হিসাবে কোটলিনকে ঘোষণা করেছিল এবং তখন থেকেই এটি প্রভাবশালী অ্যান্ড্রয়েড ভাষা হয়ে উঠেছে।
Kotlin জাভা এর ব্যথা পয়েন্ট ঠিক করার জন্য ডিজাইন করা হয়েছে: verbosity, নাল পয়েন্টার ব্যতিক্রম, এবং অনুপস্থিত আধুনিক বৈশিষ্ট্য. ফলাফল হল এমন একটি ভাষা যা একটি আধুনিক জাভা - সংক্ষিপ্ত, নিরাপদ এবং অভিব্যক্তিপূর্ণ - বিশাল জাভা ইকোসিস্টেমের সাথে সম্পূর্ণ সামঞ্জস্য বজায় রাখার মতো অনুভব করে৷
---

## কেন কোটলিন গুরুত্বপূর্ণ
- **Android মান**: Android এর জন্য Google এর পছন্দের ভাষা। বেশিরভাগ নতুন অ্যান্ড্রয়েড কোড কোটলিন।
- **100% জাভা-সামঞ্জস্যপূর্ণ**: প্রতিটি জাভা লাইব্রেরি, ফ্রেমওয়ার্ক এবং টুল ব্যবহার করুন। ধীরে ধীরে মাইগ্রেট করুন।
- **নাল নিরাপত্তা**: টাইপ সিস্টেম কম্পাইলের সময় নাল পয়েন্টার ব্যতিক্রম প্রতিরোধ করে।
- **সংক্ষিপ্ত**: জাভা থেকে উল্লেখযোগ্যভাবে কম বয়লারপ্লেট — ডেটা ক্লাস, এক্সটেনশন ফাংশন, স্মার্ট কাস্ট।
- **করোটিন**: অ্যাসিঙ্ক প্রোগ্রামিংয়ের জন্য হালকা থ্রেড — জাভা এর কমপ্লেটেবল ফিউচার বা কলব্যাকের চেয়ে সহজ।
- **মাল্টিপ্ল্যাটফর্ম**: কোটলিন মাল্টিপ্ল্যাটফর্ম আপনাকে Android, iOS, ওয়েব এবং ব্যাকএন্ডের মধ্যে কোড শেয়ার করতে দেয়।
- **সার্ভার-সাইড**: Ktor, স্প্রিং বুট (সম্পূর্ণ কোটলিন সমর্থন), এবং এক্সপোজড ব্যাকএন্ডের জন্য কোটলিনকে কার্যকর করে তোলে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **JVM নির্ভরতা** | JVM (অথবা নন-JVM লক্ষ্যগুলির জন্য কোটলিন/নেটিভ) প্রয়োজন ছোট স্থাপনার জন্য GraalVM নেটিভ ইমেজ ব্যবহার করুন |
| **সংকলনের গতি** | বড় প্রকল্পের জন্য জাভা থেকে ধীর | ক্রমবর্ধমান সংকলন ব্যবহার করুন; Kotlin 2.0 এটিকে উন্নত করে |
| **জাভা ডেভের জন্য শেখার কার্ভ** | এক্সটেনশন ফাংশন, কোরোটিন, ডিএসএল হল নতুন ধারণা | ধীরে ধীরে গ্রহণ; বেশিরভাগ জাভা প্যাটার্ন এখনও কাজ করে |
| **জাভার থেকে ছোট সম্প্রদায়** | কম কোটলিন-নির্দিষ্ট সংস্থান এবং লাইব্রেরি | জাভা এর বিশাল বাস্তুতন্ত্রের সুবিধা নিন |
| **কোটলিন মাল্টিপ্ল্যাটফর্ম পরিপক্কতা** | এখনও উৎপাদন iOS শেয়ারিং জন্য বিকশিত | শেয়ার্ড ব্যবসায়িক যুক্তির জন্য ব্যবহার করুন; UI নেটিভ রাখুন |
---

## সিনট্যাক্স মৌলিক
### ভেরিয়েবল এবং প্রকার
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

### শূন্য নিরাপত্তা
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

### ডেটা ক্লাস এবং এক্সটেনশন ফাংশন
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

### করোটিনস — অ্যাসিঙ্ক প্রোগ্রামিং
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

### সিল করা ক্লাস এবং প্যাটার্ন ম্যাচিং
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

### উচ্চ ক্রম ফাংশন
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### জেনেরিক এবং টাইপ প্যারামিটার
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

### প্রতিফলন সহ মেটাপ্রোগ্রামিং
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

### অ্যাডভান্সড ডিস্ট্রাকচারিং এবং প্যাটার্ন ম্যাচিং
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

### অপারেটর ওভারলোডিং
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

### ডিএসএল তৈরির ধরণ
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

## সামঞ্জস্য এবং সমান্তরালতা (গভীর ডুব)
### করোটিন প্রেরণকারী এবং প্রসঙ্গ
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

### চ্যানেলগুলি — কোরোটিনের মধ্যে যোগাযোগ
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

### প্রবাহ — প্রতিক্রিয়াশীল প্রবাহ
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

### স্ট্রাকচার্ড কনকারেন্সি এবং এরর হ্যান্ডলিং
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো
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

### বিল্ড কনফিগারেশন (build.gradle.kts)
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

### নির্ভরতা ব্যবস্থাপনা কমান্ড
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

### CI/CD পাইপলাইন (GitHub অ্যাকশন)
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

## পরীক্ষা
### টেস্টিং ফ্রেমওয়ার্ক এবং সেটআপ
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

### মকিং সহ ইউনিট পরীক্ষা
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

### টেস্টিং করোটিন
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

### টেস্ট কমান্ড
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

## ইন্টারঅপারেবিলিটি
### জাভা ইন্টারঅপারেবিলিটি
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

### কোটলিন/নেটিভ এবং সি ইন্টারপ
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

### কোটলিন/জেএস ইন্টারপ
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

## ডিজাইন প্যাটার্ন
### সিঙ্গেলটন (ডিফল্টভাবে থ্রেড-সেফ)
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

### নির্মাতা প্যাটার্ন (ইডিওম্যাটিক কোটলিন)
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

### ল্যাম্বডাসের সাথে কৌশল প্যাটার্ন
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

### জেনেরিক সহ রিপোজিটরি প্যাটার্ন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
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

### অপ্টিমাইজেশন কৌশল
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

## স্থাপনা
### শ্যাডো প্লাগইন সহ ফ্যাট জার
```kotlin
// build.gradle.kts
plugins {
    id("com.github.johnrengelman.shadow") version "8.1.1"
}
// Build: ./gradlew shadowJar
// Run:  java -jar build/libs/my-app-1.0.0-all.jar
```

### ডকার স্থাপনা
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

### GraalVM নেটিভ ইমেজ
```kotlin
// build.gradle.kts
plugins {
    id("org.graalvm.buildtools.native") version "0.10.2"
}
// Build native binary: ./gradlew nativeCompile
// Startup time: <100ms, Memory: ~30MB (vs ~300MB for JVM)
```

### কোটলিন মাল্টিপ্ল্যাটফর্ম স্থাপনা
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

## ইকোসিস্টেম
### ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | ডোমেন |
|------------|---------|
| **জেটপ্যাক রচনা** | আধুনিক অ্যান্ড্রয়েড UI টুলকিট |
| **Ktor** | লাইটওয়েট সার্ভার-সাইড ওয়েব ফ্রেমওয়ার্ক |
| **স্প্রিং বুট** | এন্টারপ্রাইজ ব্যাকএন্ডের জন্য সম্পূর্ণ কোটলিন সমর্থন |
| **কোটলিন মাল্টিপ্ল্যাটফর্ম** | Android, iOS, ওয়েব, ডেস্কটপের মধ্যে কোড শেয়ার করুন |
| **উন্মুক্ত** | কোটলিন এসকিউএল লাইব্রেরি (টাইপ-সেফ কোয়েরি) |
| **কোইন** | নির্ভরতা ইনজেকশন ফ্রেমওয়ার্ক |
### বিল্ড টুলস
| টুল | উদ্দেশ্য |
|------|---------|
| **Gradle (Kotlin DSL)** | বিল্ড সিস্টেম — কোটলিন হল পছন্দের বিল্ড স্ক্রিপ্ট ভাষা |
| **ইন্টেলিজ আইডিয়া** | JetBrains দ্বারা IDE — সেরা Kotlin সমর্থন |
---

## কখন কোটলিন ব্যবহার করবেন
| দৃশ্যকল্প | কেন কোটলিন | ভাল বিকল্প |
|------------|------------|---------|
| অ্যান্ড্রয়েড উন্নয়ন | Google এর পছন্দের ভাষা | জাভা (লেগেসি কোডবেসের জন্য) |
| JVM ব্যাকএন্ড | আধুনিক জাভা বিকল্প | জাভা, যান |
| ক্রস-প্ল্যাটফর্ম (ভাগ করা যুক্তি) | কোটলিন মাল্টিপ্ল্যাটফর্ম | ফ্লটার (UI শেয়ার করার জন্য) |
| ডেস্কটপ অ্যাপস | কম্পোজ মাল্টিপ্ল্যাটফর্মের সাথে সম্ভব | C#, নেটিভের জন্য সুইফট |
| সাধারণ JVM অ্যাপ্লিকেশন | জাভা থেকে কম শব্দভাষা | বড় দলের জন্য জাভা |
| নন-জেভিএম সিস্টেম প্রোগ্রামিং | প্রাথমিক লক্ষ্য নয় | মরিচা, গো, সি |
| ওয়েব ফ্রন্টএন্ড | কোটলিন/জেএস বিদ্যমান কিন্তু সীমিত | টাইপস্ক্রিপ্ট, জাভাস্ক্রিপ্ট |
| ডেটা সায়েন্স / এমএল | বাস্তুতন্ত্র নয় | পাইথন, আর |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: কোটলিনের শূন্য নিরাপত্তা বৈশিষ্ট্যগুলি আসলে কীভাবে কাজ করে?
**A:** Kotlin কম্পাইলের সময় nullable (`String?`) এবং অ nullable (`String`) প্রকারের মধ্যে পার্থক্য করে৷ কম্পাইলার আপনাকে নাল চেক ছাড়াই বাতিলযোগ্য ধরনের কলিং পদ্ধতি থেকে বাধা দেয়। নিরাপদ কল (`?.`), এলভিস অপারেটর (`?:`), এবং নন-নাল অ্যাসারশন (`!!`) বিভিন্ন কৌশল প্রদান করে৷ শূন্য চেক করার পরে স্মার্ট কাস্ট স্বয়ংক্রিয়ভাবে সংকীর্ণ প্রকার।
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

### প্রশ্ন 2: কোরোটিনগুলি কী এবং কীভাবে তারা থ্রেড থেকে আলাদা?
**A:** Coroutines হল হালকা ওজনের, সহযোগিতামূলক কাজ যা থ্রেডে চলে। তারা মৃত্যুদন্ড স্থগিত করতে পারে (থ্রেড ব্লক না করে) এবং পরে আবার শুরু করতে পারে। কয়েক থ্রেডে লক্ষ লক্ষ করোটিন চলতে পারে। `suspend`ফাংশন শুধুমাত্র coroutines বা অন্যান্য সাসপেন্ড ফাংশন থেকে কল করা যেতে পারে। করোটিন স্কোপগুলি জীবনচক্র নিয়ন্ত্রণ করে — যখন একটি স্কোপ বাতিল করা হয়, তখন তার সমস্ত করোটিন বাতিল করা হয়।
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

### প্রশ্ন 3: ডেটা ক্লাস, সিল করা ক্লাস এবং ভ্যালু ক্লাস কী?
**A:** ডেটা ক্লাসগুলি`equals`,`hashCode`,`toString`,`copy`, এবং`componentN`ফাংশনগুলি স্বয়ংক্রিয়ভাবে তৈরি করে — ডেটা হোল্ডারদের জন্য আদর্শ৷ সিল করা ক্লাসগুলি উত্তরাধিকারকে সীমাবদ্ধ করে — সমস্ত সাবক্লাস একই ফাইলে থাকতে হবে — সম্পূর্ণ`when`এক্সপ্রেশনগুলি সক্ষম করে৷ মান ক্লাস রানটাইমে শূন্য ওভারহেড দিয়ে একটি একক মান মোড়ানো (ইনলাইন ক্লাস)।
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

### প্রশ্ন 4: এক্সটেনশন ফাংশনগুলি কীভাবে কাজ করে এবং তাদের সীমাবদ্ধতাগুলি কী কী?
**A:** এক্সটেনশন ফাংশন উত্তরাধিকার বা পরিবর্তন ছাড়াই বিদ্যমান প্রকারে পদ্ধতি যোগ করে। এগুলি স্থিরভাবে সমাধান করা হয় (ঘোষিত প্রকারের উপর ভিত্তি করে, রানটাইম টাইপ নয়)। তারা ব্যক্তিগত সদস্যদের অ্যাক্সেস করতে পারে না। এক্সটেনশন বৈশিষ্ট্য একইভাবে কাজ করে। এগুলি কোটলিনের স্ট্যান্ডার্ড লাইব্রেরি এবং অ্যান্ড্রয়েড বিকাশে ব্যাপকভাবে ব্যবহৃত হয়।
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

### প্রশ্ন 5: কোটলিন মাল্টিপ্ল্যাটফর্ম কী এবং কখন এটি ব্যবহার করব?
**A:** Kotlin Multiplatform (KMP) আপনাকে প্ল্যাটফর্ম-নির্দিষ্ট UI রাখার সময় প্ল্যাটফর্মের (Android, iOS, ওয়েব, ডেস্কটপ, সার্ভার) মধ্যে কোড শেয়ার করতে দেয়। ব্যবসায়িক যুক্তি, নেটওয়ার্কিং এবং ডেটা স্তরগুলি ভাগ করা যেতে পারে; UI নেটিভ থাকে। এটি ব্যবহার করুন যখন আপনার এমন একটি দল থাকে যারা কোটলিনকে জানে এবং সম্পূর্ণ ক্রস-প্ল্যাটফর্মে না গিয়ে (যেমন ফ্লাটার) কোড শেয়ারিং সর্বাধিক করতে চায়।
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

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি টাইপ-সেফ বিল্ডার ডিএসএল তৈরি করুন
**সমস্যা বিবৃতি:** কম্পাইল-টাইম সেফটি সহ HTML ডকুমেন্ট তৈরির জন্য একটি Kotlin DSL তৈরি করুন। DSL-এর উচিত বৈধ HTML কাঠামো (যেমন,`<head>`শুধুমাত্র`<html>`,`<li>`শুধুমাত্র`<ul>`বা`<ol>`এর ভিতরে)।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) স্কোপ ফাঁস রোধ করতে`@DslMarker`সহ নির্মাতা ফাংশন, (2) রিসিভার-ভিত্তিক ডিএসএল সিনট্যাক্স, (3) বৈধ নেস্টিংয়ের সংকলন-সময় প্রয়োগ। কোটলিনের টাইপ-সেফ বিল্ডার এবং`@DslMarker`টীকা এর জন্য ডিজাইন করা হয়েছে।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- একটি সুযোগ নিয়ন্ত্রণ টীকা তৈরি করতে`@DslMarker`ব্যবহার করুন৷
- প্রতিটি HTML উপাদান তার বৈধ শিশুদের জন্য নির্মাতা পদ্ধতি সহ একটি ক্লাস।
-`@HtmlTagMarker`চাইল্ড স্কোপের ভিতরে অভিভাবক স্কোপ পদ্ধতি অ্যাক্সেস করতে বাধা দেয়।
- পরিষ্কার বাক্য গঠনের জন্য`invoke`অপারেটর ব্যবহার করুন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- প্রকার নিরাপত্তা:`@DslMarker`সুযোগ ফাঁস প্রতিরোধ করে —`title()``body {}` এর ভিতরে অ্যাক্সেসযোগ্য নয়৷
- কম্পাইলার কম্পাইলের সময় বৈধ নেস্টিং প্রয়োগ করে — কোন রানটাইম চেকের প্রয়োজন নেই।
- এক্সটেনসিবিলিটি: উপযুক্ত শিশু পদ্ধতি সহ ক্লাস তৈরি করে নতুন উপাদান যোগ করুন।
- উত্পাদন: একটি ব্যাপক, ভাল-পরীক্ষিত HTML DSL এর জন্য`kotlinx.html`ব্যবহার করুন৷
### সমস্যা 2: Coroutines সহ একটি স্টেট মেশিন প্রয়োগ করুন
**সমস্যা বিবৃতি:** একটি গেম চরিত্রের জন্য একটি করটিন-ভিত্তিক স্টেট মেশিন তৈরি করুন যা ইনপুট ইভেন্টগুলি প্রক্রিয়া করে, রাজ্যগুলির মধ্যে রূপান্তর করে এবং অ্যানিমেশন কলব্যাকগুলিকে সমর্থন করে৷
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) এন্ট্রি/এক্সিট অ্যাকশন সহ স্টেটস, (2) ইভেন্ট-চালিত ট্রানজিশন, (3) কোরোটিন-ভিত্তিক প্রসেসিং লুপ, (4) স্টেট ট্রানজিশনে অ্যানিমেশন কলব্যাক। রাষ্ট্রীয় যন্ত্রটি একটি চ্যানেল থেকে দীর্ঘজীবী কোরোটিন গ্রাসকারী ঘটনা হিসাবে চলে।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- রাজ্য এবং ইভেন্টের জন্য সিল করা ক্লাস ব্যবহার করুন।
- ইভেন্ট পাস করার জন্য`Channel`ব্যবহার করুন।
- স্টেট মেশিন লুপ`for (event in channel)`এর সাথে ইভেন্টগুলি গ্রাস করে৷
- ট্রানজিশন প্রস্থান/প্রবেশ কলব্যাক ট্রিগার করে।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- টাইপ নিরাপত্তা: সিল করা ক্লাস নিশ্চিত করে যে সমস্ত রাজ্য এবং ইভেন্টগুলি পরিচালনা করা হয়। কম্পাইলার অনুপস্থিত রূপান্তর ক্যাচ.
- করোটিন-ভিত্তিক: ইভেন্টগুলিকে ব্লক না করেই ক্রমানুসারে প্রক্রিয়া করা হয়৷ চ্যানেল ব্যাক প্রেসার প্রদান করে।
- জীবনচক্র: সুযোগ বাতিল করা রাষ্ট্রের যন্ত্রটিকে পরিষ্কারভাবে বন্ধ করে দেয়।
- উত্পাদন: জটিল স্টেট মেশিনের জন্য,`tinder-statemachine`ব্যবহার করুন বা একটি আনুষ্ঠানিক স্টেট মেশিন লাইব্রেরি সহ রাজ্যগুলির মডেল করুন।
---

## সারাংশ
কোটলিন আধুনিক জাভা সঠিকভাবে সম্পন্ন হয়েছে। এটি JVM-এ চলে, সমস্ত জাভা লাইব্রেরি ব্যবহার করে, কিন্তু নাল পয়েন্টার ব্যতিক্রমগুলিকে বাদ দেয়, বয়লারপ্লেট হ্রাস করে এবং আধুনিক বৈশিষ্ট্যগুলি যেমন coroutines, এক্সটেনশন ফাংশন এবং সিল করা ক্লাস যুক্ত করে। অ্যান্ড্রয়েড ডেভেলপমেন্টের জন্য, কোটলিন স্পষ্ট পছন্দ। JVM ব্যাকএন্ডের জন্য, এটি জাভার একটি বাধ্যতামূলক বিকল্প। কোটলিন মাল্টিপ্ল্যাটফর্ম iOS এবং তার বাইরেও এর নাগাল প্রসারিত করে। আপনি যদি ইতিমধ্যে জাভা জানেন, কোটলিন শেখা একটি স্বাভাবিক এবং ফলপ্রসূ পরবর্তী পদক্ষেপ।