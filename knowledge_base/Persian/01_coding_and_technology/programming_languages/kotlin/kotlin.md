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
# کاتلین
Kotlin یک زبان برنامه نویسی تایپ شده و کامپایل شده است که توسط JetBrains توسعه یافته و اولین بار در سال 2011 منتشر شد (1.0 در سال 2016). این برنامه بر روی ماشین مجازی جاوا (JVM) اجرا می شود و به طور کامل با جاوا سازگار است - به این معنی که شما می توانید از هر کتابخانه جاوا از Kotlin استفاده کنید و کد Kotlin را از جاوا بدون هیچ پوششی فراخوانی کنید. در سال 2017، گوگل کاتلین را به عنوان زبان ترجیحی برای توسعه اندروید معرفی کرد و از آن زمان به زبان غالب اندروید تبدیل شده است.
Kotlin برای رفع نقاط درد جاوا طراحی شده است: پرحرفی، استثناهای اشاره گر تهی، و ویژگی های مدرن از دست رفته. نتیجه زبانی است که شبیه یک جاوا مدرن شده است - مختصر، ایمن و رسا - در حالی که سازگاری کامل با اکوسیستم عظیم جاوا را حفظ می کند.
---

## چرا کاتلین مهم است
- **استاندارد اندروید**: زبان برگزیده گوگل برای اندروید. بیشتر کدهای جدید اندروید Kotlin هستند.
- **100% سازگار با جاوا **: از هر کتابخانه، چارچوب و ابزار جاوا استفاده کنید. به تدریج مهاجرت کنید.
- ** امنیت تهی **: سیستم نوع از استثناء اشاره گر تهی در زمان کامپایل جلوگیری می کند.
- ** مختصر **: دیگ بخار به طور قابل توجهی کمتر از جاوا - کلاس های داده، توابع افزودنی، ریخته گری هوشمند.
- **Coroutines**: رشته های سبک برای برنامه نویسی همگام - ساده تر از CompletableFuture جاوا یا callbacks.
- ** Multiplatform **: Kotlin Multiplatform به شما امکان می دهد کد را بین Android، iOS، وب و باطن به اشتراک بگذارید.
- **سمت سرور**: Ktor، Spring Boot (پشتیبانی کامل از Kotlin)، و Exposur باعث می شود کاتلین برای backendها قابل اجرا باشد.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **وابستگی JVM** | به JVM (یا Kotlin/Native برای اهداف غیر JVM) نیاز دارد | استفاده از تصویر اصلی GraalVM برای استقرارهای کوچک |
| **سرعت تدوین** | کندتر از جاوا برای پروژه های بزرگ | استفاده از کامپایل افزایشی؛ Kotlin 2.0 این |
| **منحنی یادگیری برای توسعه دهندگان جاوا** | توابع افزونه، کوروتین ها، DSL مفاهیم جدیدی هستند | پذیرش تدریجی؛ بیشتر الگوهای جاوا هنوز کار می کنند |
| **جامعه کوچکتر از جاوا** | منابع و کتابخانه های مختص کاتلین کمتر | از اکوسیستم عظیم جاوا استفاده کنید |
| **سررسید چند پلتفرمی کاتلین** | هنوز برای تولید به اشتراک گذاری iOS در حال تکامل است | استفاده برای منطق تجاری مشترک؛ حفظ UI بومی |
---

## اصول نحو
### متغیرها و انواع
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

### ایمنی پوچ
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

### کلاس های داده و توابع پسوند
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

### کوروتین ها — برنامه نویسی همگام
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

### کلاس های مهر و موم شده و تطبیق الگو
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

### توابع مرتبه بالاتر
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

## نحو و الگوهای پیشرفته
### ژنریک و پارامترهای نوع
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

### فرابرنامه نویسی با بازتاب
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

### تخریب پیشرفته و تطبیق الگو
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

### بارگذاری بیش از حد اپراتور
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

### الگوهای ایجاد DSL
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

## همزمانی و موازی (شیرجه عمیق)
### توزیع‌کنندگان و زمینه‌های کوروتین
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

کانال های ### - ارتباط بین برنامه ها
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

### جریان - جریان های واکنشی
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

### همزمانی ساختاریافته و مدیریت خطا
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه
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

### پیکربندی ساخت (build.gradle.kts)
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

### دستورات مدیریت وابستگی
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

### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### تست چارچوب ها و راه اندازی
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

### تست واحد با تمسخر
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

### مراحل تست
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

### دستورات تست
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

## قابلیت همکاری
### قابلیت همکاری جاوا
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

### Kotlin/Native و C Interop
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

### Kotlin/JS Interop
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

## الگوهای طراحی
### Singleton (Thread-Safe به طور پیش فرض)
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

### Builder Pattern (Idiomatic Kotlin)
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

### الگوی استراتژی با Lambdas
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

### الگوی مخزن با Generics
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
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

### تکنیک های بهینه سازی
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

## استقرار
### Fat JAR با پلاگین Shadow
```kotlin
// build.gradle.kts
plugins {
    id("com.github.johnrengelman.shadow") version "8.1.1"
}
// Build: ./gradlew shadowJar
// Run:  java -jar build/libs/my-app-1.0.0-all.jar
```

### استقرار داکر
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

### GraalVM Native Image
```kotlin
// build.gradle.kts
plugins {
    id("org.graalvm.buildtools.native") version "0.10.2"
}
// Build native binary: ./gradlew nativeCompile
// Startup time: <100ms, Memory: ~30MB (vs ~300MB for JVM)
```

### استقرار چند پلتفرم Kotlin
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

## اکوسیستم
### چارچوب
| چارچوب | دامنه |
|-----------|--------|
| **Jetpack Compose** | جعبه ابزار مدرن UI اندروید |
| **Ktor** | چارچوب وب سبک سمت سرور |
| **چکمه بهاره** | پشتیبانی کامل کاتلین برای باطن های سازمانی |
| **مولتی پلتفرم کاتلین** | اشتراک گذاری کد بین اندروید، iOS، وب، دسکتاپ |
| **معرض** | کتابخانه Kotlin SQL (پرس و جوهای ایمن تایپ) |
| **کوین** | چارچوب تزریق وابستگی |
### ابزارهای ساخت
| ابزار | هدف |
|------|---------|
| **Gradle (Kotlin DSL)** | سیستم ساخت — کاتلین زبان اسکریپت ساخت ترجیحی است |
| **IntelliJ IDEA** | IDE توسط JetBrains — بهترین پشتیبانی Kotlin |
---

## چه زمانی از Kotlin استفاده کنیم
| سناریو | چرا کاتلین | جایگزین بهتر |
|----------|----------|------------------|
| توسعه اندروید | زبان برگزیده گوگل | جاوا (برای پایگاه های کد قدیمی) |
| پشتیبان های JVM | جایگزین جاوا مدرن | جاوا، برو |
| کراس پلتفرم (منطق مشترک) | چند پلتفرم کاتلین | فلاتر (برای اشتراک گذاری رابط کاربری) |
| برنامه های دسکتاپ | ممکن است با Compose Multiplatform | سی شارپ، سوئیفت برای بومی |
| برنامه های عمومی JVM | پرمخاطب تر از جاوا | جاوا برای تیم های بزرگتر |
| برنامه نویسی سیستم های غیر JVM | هدف اصلی نیست | زنگ زدگی، برو، سی |
| وب سایت | Kotlin/JS وجود دارد اما محدود است | TypeScript, JavaScript |
| علم داده / ML | نه اکوسیستم | پایتون، R |
---

## پرسش و پاسخ مصنوعی
### Q1: ویژگی های ایمنی پوچ کاتلین واقعا چگونه کار می کنند؟
**A:** کاتلین در زمان کامپایل بین انواع پوچ (`String?`) و غیر قابل تهی (`String`) تمایز قائل می شود. کامپایلر شما را از فراخوانی متدها بر روی انواع پوچ بدون بررسی پوچ جلوگیری می کند. تماس‌های ایمن (`?.`)، اپراتور الویس (`?:`) و ادعای غیر تهی (`!!`) استراتژی‌های مختلفی را ارائه می‌کنند. کست های هوشمند به طور خودکار انواع را پس از بررسی های پوچ محدود می کند.
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

### Q2: کوروتین ها چیست و چه تفاوتی با رشته ها دارند؟
**A:** کوروتین ها کارهای سبک وزن و مشارکتی هستند که روی رشته ها اجرا می شوند. آنها می توانند اجرا را به حالت تعلیق درآورند (بدون مسدود کردن رشته) و بعداً از سر بگیرند. میلیون ها کوروتین می توانند روی چند رشته اجرا شوند.  توابع`suspend`را فقط می توان از کوروتین ها یا سایر توابع تعلیق فراخوانی کرد. دامنه‌های کوروتین چرخه عمر را کنترل می‌کنند - وقتی یک محدوده لغو می‌شود، همه موارد اولیه آن لغو می‌شوند.
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

### Q3: کلاس های داده، کلاس های مهر و موم شده و کلاس های ارزش چیست؟
**A:** کلاس های داده عملکردهای `equals`، `hashCode`، `toString`، `copy`، و`componentN`را به طور خودکار تولید می کنند - ایده آل برای دارندگان داده. کلاس های مهر و موم شده وراثت را محدود می کنند - همه زیر کلاس ها باید در یک فایل باشند - عبارات جامع`when`را فعال می کند. کلاس های ارزش یک مقدار را با سربار صفر در زمان اجرا (کلاس درون خطی) می پوشانند.
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

### Q4: توابع افزونه چگونه کار می کنند و محدودیت های آنها چیست؟
**A:** توابع برنامه افزودنی روشها را به انواع موجود بدون وراثت یا اصلاح اضافه می کنند. آنها به صورت ایستا حل می شوند (بر اساس نوع اعلام شده، نه نوع زمان اجرا). آنها نمی توانند به اعضای خصوصی دسترسی داشته باشند. ویژگی های افزونه به طور مشابه کار می کنند. آنها به طور گسترده در کتابخانه استاندارد Kotlin و توسعه اندروید استفاده می شوند.
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

### Q5: Kotlin Multiplatform چیست و چه زمانی باید از آن استفاده کنم؟
**A:** Kotlin Multiplatform (KMP) به شما امکان می دهد کد را بین پلتفرم ها (اندروید، iOS، وب، دسکتاپ، سرور) به اشتراک بگذارید و در عین حال رابط کاربری مخصوص پلتفرم را حفظ کنید. منطق کسب و کار، شبکه و لایه های داده را می توان به اشتراک گذاشت. UI بومی می ماند. زمانی از آن استفاده کنید که تیمی دارید که کاتلین را می‌شناسد و می‌خواهد اشتراک‌گذاری کد را بدون استفاده از کراس پلتفرم کامل (مانند Flutter) به حداکثر برساند.
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

## حل مسئله زنجیره ای از فکر
### مشکل 1: ساختن DSL نوع ایمن بسازید
**بیانیه مشکل:** یک Kotlin DSL برای ساخت اسناد HTML با ایمنی زمان کامپایل ایجاد کنید. DSL باید ساختار HTML معتبر را اعمال کند (به عنوان مثال،`<head>`فقط در داخل `<html>`،`<li>`فقط در داخل`<ul>`یا `<ol>`).
** مرحله 1 - مشکل را درک کنید:**
ما نیاز داریم: (1) توابع سازنده با`@DslMarker`برای جلوگیری از نشت دامنه، (2) نحو DSL مبتنی بر گیرنده، (3) اجرای تودرتو در زمان کامپایل. سازنده های ایمن کاتلین و حاشیه نویسی`@DslMarker`برای این کار طراحی شده اند.
** مرحله 2 - شناسایی رویکرد: **
- از`@DslMarker`برای ایجاد حاشیه نویسی کنترل دامنه استفاده کنید.
- هر عنصر HTML یک کلاس با متدهای سازنده برای فرزندان معتبر خود است.
-`@HtmlTagMarker`از دسترسی به روش های دامنه والد در محدوده فرزند جلوگیری می کند.
- از عملگر`invoke`برای نحو تمیز استفاده کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- ایمنی نوع:`@DslMarker`از نشت محدوده جلوگیری می کند -`title()`در داخل`body {}`قابل دسترسی نیست.
- کامپایلر تودرتوی معتبر را در زمان کامپایل اجرا می‌کند - بدون نیاز به بررسی زمان اجرا.
- توسعه پذیری: اضافه کردن عناصر جدید با ایجاد کلاس ها با متدهای فرزند مناسب.
- تولید: از`kotlinx.html`برای یک HTML DSL جامع و به خوبی آزمایش شده استفاده کنید.
### مشکل 2: یک ماشین حالت را با کوروتین ها پیاده سازی کنید
**بیانیه مشکل:** یک ماشین حالت مبتنی بر کوروتین برای یک شخصیت بازی بسازید که رویدادهای ورودی، انتقال بین حالت ها را پردازش می کند و از تماس های انیمیشن پشتیبانی می کند.
** مرحله 1 - مشکل را درک کنید:**
ما به این موارد نیاز داریم: (1) حالت‌هایی با اقدامات ورود/خروج، (2) انتقال‌های رویداد محور، (3) حلقه پردازش مبتنی بر روال، (4) تماس‌های متحرک در انتقال حالت. ماشین حالت به‌عنوان یک رویداد طولانی‌مدت مصرف کننده از یک کانال اجرا می‌شود.
** مرحله 2 - شناسایی رویکرد: **
- از کلاس مهر و موم شده برای حالت ها و رویدادها استفاده کنید.
- از`Channel`برای عبور رویداد استفاده کنید.
- حلقه ماشین حالت رویدادها را با`for (event in channel)`مصرف می کند.
- انتقال‌ها تماس‌های خروج/ورود را آغاز می‌کنند.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- ایمنی نوع: کلاس های مهر و موم شده اطمینان حاصل می کنند که همه حالت ها و رویدادها رسیدگی می شوند. کامپایلر انتقال های گم شده را می گیرد.
- مبتنی بر Coroutine: رویدادها به صورت متوالی و بدون مسدود کردن پردازش می شوند. کانال فشار برگشتی را فراهم می کند.
- چرخه حیات: لغو محدوده دستگاه حالت را به طور تمیز متوقف می کند.
- تولید: برای ماشین‌های حالت پیچیده، از`tinder-statemachine`استفاده کنید یا حالت‌ها را با یک کتابخانه ماشین دولتی رسمی مدل‌سازی کنید.
---

## خلاصه
Kotlin جاوای مدرنی است که به درستی انجام شده است. این برنامه روی JVM اجرا می‌شود، از تمام کتابخانه‌های جاوا استفاده می‌کند، اما استثناهای نشانگر تهی را حذف می‌کند، boilerplate را کاهش می‌دهد، و ویژگی‌های مدرنی مانند کوروتین‌ها، توابع افزونه و کلاس‌های مهر و موم شده را اضافه می‌کند. برای توسعه اندروید، Kotlin انتخاب واضحی است. برای پشتیبان‌های JVM، یک جایگزین قانع‌کننده برای جاوا است. Kotlin Multiplatform دسترسی خود را به iOS و فراتر از آن گسترش می دهد. اگر از قبل جاوا را می‌دانید، یادگیری Kotlin یک قدم طبیعی و ارزشمند است.