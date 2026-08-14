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

# 科特林
Kotlin 是一種靜態類型、編譯型程式語言，由 JetBrains 開發，於 2011 年首次發布（2016 年發布 1.0）。它在 Java 虛擬機器 (JVM) 上運行，並且與 Java 完全可互通——這意味著您可以使用 Kotlin 中的任何 Java 庫，並從 Java 呼叫 Kotlin 程式碼，而無需任何包裝器。 2017 年，Google 宣布 Kotlin 成為 Android 開發的首選語言，從此成為 Android 的主導語言。
Kotlin 旨在解決 Java 的痛點：冗長、空指標異常和缺乏現代功能。結果是一種感覺像是現代化 Java 的語言——簡潔、安全且富有表現力——同時保持與龐大的 Java 生態系統的完全相容性。
---

## 為什麼 Kotlin 很重要
- **Android 標準**：Google 的 Android 首選語言。大多數新的 Android 程式碼都是 Kotlin。
- **100% Java 相容**：使用每個 Java 函式庫、框架和工具。逐漸遷移。
- **空安全性**：類型系統在編譯時防止空指標異常。
- **簡潔**：比 Java 少得多的樣板程式碼 — 資料類別、擴充函數、智慧轉換。
- **協程**：用於非同步程式設計的輕量級執行緒 - 比 Java 的 CompletableFuture 或回呼更簡單。
- **多平台**：Kotlin 多平台可讓您在 Android、iOS、Web 和後端之間共用程式碼。
- **伺服器端**：Ktor、Spring Boot（完全支援 Kotlin）和 Exposed 使 Kotlin 適用於後端。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **JVM 依賴** |需要 JVM（對於非 JVM 目標則需要 Kotlin/Native）|使用 GraalVM 原生鏡像進行小型部署 |
| **編譯速度** |大型專案比Java慢|使用增量編譯；Kotlin 2.0 對此進行了改進 |
| **Java 開發人員的學習曲線** |擴充函數、協程、DSL 是新概念 |逐步採用；大多數 Java 模式仍然有效 |
| **比 Java 更小的社群** |更少的 Kotlin 特定資源和函式庫 |利用 Java 龐大的生態系統 |
| **Kotlin 多平台成熟度** |生產 iOS 共享仍在不斷發展 |用於共享業務邏輯；保持 UI 原生 |
---

## 文法基礎知識
### 變數和類型
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

### 空安全
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

### 資料類別和擴充函數
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

### 協程 — 非同步編程
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

### 密封類別和模式匹配
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

### 高階函數
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

## 進階語法和模式
### 泛型與型別參數
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

### 使用反射進行元編程
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

### 高階解構與模式匹配
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

### 運算子重載
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

### DSL 建立模式
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

## 並發與並行（深入探討）
### 協程調度程序和上下文
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

### 通道－協程之間的通信
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

### 流 — 反應流
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

### 結構化並發與錯誤處理
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

## 專案配置與建置系統
### 專案結構
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

### 建置配置（build.gradle.kts）
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

### 依賴管理命令
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

### CI/CD 管道 (GitHub Actions)
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

## 測試
### 測試框架和設置
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

### 使用模擬進行單元測試
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

### 測試協程
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

### 測試命令
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

## 互通性
### Java 互通性
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

### Kotlin/Native 和 C 互通
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

### Kotlin/JS 互通
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

## 設計模式
### 單例（預設執行緒安全性）
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

### 建構器模式（Kotlin 慣用語）
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

### 使用 Lambda 的策略模式
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

### 具有泛型的儲存庫模式
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

## 效能與最佳化
### 分析工具
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

### 優化技術
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

## 部署
### 附 Shadow 外掛的 Fat JAR
```kotlin
// build.gradle.kts
plugins {
    id("com.github.johnrengelman.shadow") version "8.1.1"
}
// Build: ./gradlew shadowJar
// Run:  java -jar build/libs/my-app-1.0.0-all.jar
```

### Docker 部署
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

### GraalVM 原生映像
```kotlin
// build.gradle.kts
plugins {
    id("org.graalvm.buildtools.native") version "0.10.2"
}
// Build native binary: ./gradlew nativeCompile
// Startup time: <100ms, Memory: ~30MB (vs ~300MB for JVM)
```

### Kotlin 多平台部署
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

## 生態系統
### 框架
|框架|域名 |
|------------|--------|
| **Jetpack Compose** |現代 Android UI 工具包 |
| **Ktor** |輕量級伺服器端Web框架|
| **Spring Boot** |對企業後端的全面 Kotlin 支援 |
| **Kotlin 多平台** |在 Android、iOS、Web、桌面之間共用程式碼 |
| **暴露** | Kotlin SQL 庫（類型安全性查詢）|
| **科因** |依賴注入框架|
### 建置工具
|工具|目的|
|------|---------|
| **Gradle (Kotlin DSL)** |建置系統－Kotlin 是首選建置腳本語言 |
| **IntelliJ IDEA** | JetBrains 的 IDE — 最佳 Kotlin 支援 |
---

## 何時使用 Kotlin
|場景|為什麼選擇 Kotlin |更好的選擇|
|----------|----------|--------------------|
|安卓開發| Google 的首選語言 | Java（用於遺留程式碼庫）|
| JVM 後端 |現代 Java 替代方案 | Java、Go |
|跨平台（共享邏輯）| Kotlin 多平台 | Flutter（用於 UI 共享）|
|桌面應用程式 | Compose Multiplatform 成為可能 | C#、Swift 原生 |
|通用 JVM 應用程式 |比 Java 更簡潔 |適用於大型團隊的 Java |
|非 JVM 系統程式設計 |不是首要目標 | Rust、Go、C |
|網頁前端 | Kotlin/JS 存在但有限 | TypeScript、JavaScript |
|資料科學/機器學習 |不是生態系| Python、R |
---

## 綜合問答
### Q1：Kotlin 的 null 安全功能實際上是如何運作的？
**A:** Kotlin 在編譯時區分可為 null (`String?`) 和不可為 null (`String`) 型別。編譯器會阻止您在沒有 null 檢查的情況下呼叫可為 null 類型的方法。安全呼叫 (`?.`)、Elvis 運算子 (`?:`) 和非空斷言 (`!!`) 提供不同的策略。智慧轉換會在空檢查後自動縮小類型範圍。
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

### Q2：什麼是協程，它們與執行緒有何不同？
**答：** 協程是在執行緒上執行的輕量級協作任務。它們可以暫停執行（不阻塞線程）並稍後恢復。數百萬個協程可以在幾個執行緒上運行。 `suspend`函數只能從協程或其他暫停函數呼叫。協程作用域控制生命週期－當一個作用域被取消時，它的所有協程都會被取消。
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

### Q3：什麼是資料類別、密封類別和值類別？
**A:** 資料類別會自動產生`equals`、`hashCode`、`toString`、`copy`和`componentN`函數 - 非常適合資料持有者。密封類別限制繼承 - 所有子類別必須位於同一檔案中 - 啟用詳盡的`when`表達式。值類別在運行時以零開銷包裝單一值（內聯類別）。
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

### Q4：擴充函數如何運作，它們有哪些限制？
**A:** 擴充函數會為現有型別新增方法，無需繼承或修改。它們是靜態解析的（基於宣告的類型，而不是執行時間類型）。他們無法存取私人成員。擴展屬性的工作原理類似。它們廣泛應用於 Kotlin 的標準庫和 Android 開發中。
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

### Q5：什麼是 Kotlin Multiplatform，什麼時候該使用它？
**答：** Kotlin Multiplatform (KMP) 可讓您在平台（Android、iOS、Web、桌面、伺服器）之間共用程式碼，同時保留特定於平台的 UI。業務邏輯、網路、資料層可以共享； UI 保持原生。當您的團隊了解 Kotlin 並且希望最大化程式碼共用而不需要完全跨平台（如 Flutter）時，請使用它。
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

## 解決問題的思路
### 問題 1：建構型別安全的 Builder DSL
**問題陳述：** 建立一個 Kotlin DSL，用於建立具有編譯時安全性的 HTML 文件。 DSL 應強制執行有效的 HTML 結構（例如，`<head>`僅在`<html>`內，`<li>`僅在`<ul>`或`<ol>`內）。
**第 1 步 — 了解問題：**
我們需要：(1) 具有`@DslMarker`的建構器函數以防止範圍洩漏，(2) 基於接收器的 DSL 語法，(3) 編譯時強制執行有效巢狀。 Kotlin 的型別安全建構器和`@DslMarker`註解就是為此而設計的。
**第 2 步 — 確定方法：**
- 使用`@DslMarker`建立範圍控制註解。
- 每個 HTML 元素都是一個類，其有效子元素具有建構器方法。
-`@HtmlTagMarker`阻止存取子作用域內的父作用域方法。
- 使用`invoke`運算子來實作簡潔的語法。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 類型安全：`@DslMarker`防止範圍洩漏 -`title()`在`body {}`內部不可存取。
- 編譯器在編譯時強制執行有效巢狀－無需執行時間檢查。
- 可擴充性：透過建立具有適當子方法的類別來新增元素。
- 生產：使用`kotlinx.html`取得全面的、經過良好測試的 HTML DSL。
### 問題 2：使用協程實現狀態機
**問題陳述：** 為遊戲角色建立一個基於協程的狀態機，用於處理輸入事件、狀態之間的轉換並支援動畫回調。
**第 1 步 — 了解問題：**
我們需要：（1）具有進入/退出操作的狀態，（2）事件驅動的轉換，（3）基於協程的處理循環，（4）狀態轉換的動畫回呼。狀態機作為長壽命協程運行，消耗來自通道的事件。
**第 2 步 — 確定方法：**
- 對狀態和事件使用密封類別。
- 使用`Channel`進行事件傳遞。
- 狀態機循環使用`for (event in channel)`事件。
- 轉換觸發退出/進入回呼。
**第 3 步 — 實施解決方案：**
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

**第 4 步 — 驗證與最佳化：**
- 類型安全：密封類別確保所有狀態和事件都得到處理。編譯器捕獲丟失的轉換。
- 基於協程：事件依序處理，無阻塞。通道提供背壓。
- 生命週期：取消作用域會完全停止狀態機。
- 生產：對於複雜的狀態機，使用`tinder-statemachine`或使用正式的狀態機庫對狀態進行建模。
---

＃＃ 概括
Kotlin 是現代 Java 的完美體現。它在 JVM 上運行，使用所有 Java 庫，但消除了空指針異常，減少了樣板文件，並添加了協程、擴展函數和密封類等現代功能。對於 Android 開發，Kotlin 是明智的選擇。對於 JVM 後端，它是 Java 的一個引人注目的替代方案。 Kotlin Multiplatform 將其影響範圍擴展到 iOS 及其他地區。如果您已經了解 Java，那麼學習 Kotlin 是自然而然且有益的下一步。