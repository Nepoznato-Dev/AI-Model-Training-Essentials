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

# Kotlin
Kotlin là ngôn ngữ lập trình được biên dịch, gõ tĩnh do JetBrains phát triển và phát hành lần đầu tiên vào năm 2011 (1.0 vào năm 2016). Nó chạy trên Máy ảo Java (JVM) và hoàn toàn có thể tương tác với Java — nghĩa là bạn có thể sử dụng bất kỳ thư viện Java nào từ Kotlin và gọi mã Kotlin từ Java mà không cần bất kỳ trình bao bọc nào. Vào năm 2017, Google đã công bố Kotlin là ngôn ngữ ưa thích để phát triển Android và kể từ đó nó đã trở thành ngôn ngữ Android thống trị.
Kotlin được thiết kế để khắc phục các điểm yếu của Java: chi tiết, ngoại lệ con trỏ null và thiếu các tính năng hiện đại. Kết quả là một ngôn ngữ có cảm giác giống như Java được hiện đại hóa — ngắn gọn, an toàn và biểu cảm — trong khi vẫn duy trì khả năng tương thích hoàn toàn với hệ sinh thái Java khổng lồ.
---

## Tại sao Kotlin lại quan trọng
- **Tiêu chuẩn Android**: Ngôn ngữ ưa thích của Google dành cho Android. Hầu hết mã Android mới là Kotlin.
- **Tương thích 100% với Java**: Sử dụng mọi thư viện, khung và công cụ Java. Di cư dần dần.
- **Không an toàn**: Hệ thống loại ngăn chặn các ngoại lệ con trỏ null tại thời điểm biên dịch.
- **Súc tích**: Ít bản soạn sẵn hơn đáng kể so với Java — các lớp dữ liệu, hàm mở rộng, các biểu diễn thông minh.
- **Coroutines**: Các luồng nhẹ để lập trình không đồng bộ — đơn giản hơn CompleteableFuture hoặc các lệnh gọi lại của Java.
- **Đa nền tảng**: Kotlin Multiplatform cho phép bạn chia sẻ mã giữa Android, iOS, web và chương trình phụ trợ.
- **Phía máy chủ**: Ktor, Spring Boot (hỗ trợ đầy đủ Kotlin) và Exused giúp Kotlin trở nên khả thi cho các chương trình phụ trợ.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Phụ thuộc JVM** | Yêu cầu JVM (hoặc Kotlin/Native cho các mục tiêu không phải JVM) | Sử dụng hình ảnh gốc GraalVM cho các triển khai nhỏ |
| **Tốc độ biên dịch** | Chậm hơn Java cho các dự án lớn | Sử dụng biên dịch tăng dần; Kotlin 2.0 cải thiện điều này |
| **Đường cong học tập dành cho nhà phát triển Java** | Các hàm mở rộng, coroutine, DSL là những khái niệm mới | Áp dụng dần dần; hầu hết các mẫu Java vẫn hoạt động |
| **Cộng đồng nhỏ hơn Java** | Ít tài nguyên và thư viện dành riêng cho Kotlin hơn | Tận dụng hệ sinh thái khổng lồ của Java |
| **Sự trưởng thành về đa nền tảng của Kotlin** | Vẫn đang phát triển để chia sẻ iOS sản xuất | Sử dụng cho logic kinh doanh được chia sẻ; giữ nguyên giao diện người dùng |
---

##Cơ bản về cú pháp
### Biến và kiểu
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

### Không an toàn
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

### Lớp dữ liệu và hàm mở rộng
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

### Coroutine — Lập trình không đồng bộ
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

### Các lớp kín và khớp mẫu
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

### Hàm bậc cao hơn
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

## Cú pháp & Mẫu nâng cao
### Thông số chung và loại
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

### Lập trình meta với sự phản ánh
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

### Phá hủy nâng cao và khớp mẫu
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

### Quá tải toán tử
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

### Các mẫu tạo DSL
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

## Đồng thời & Song song (Đi sâu)
### Trình điều phối và bối cảnh của Coroutine
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

### Kênh — Giao tiếp giữa các coroutine
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

### Luồng — Luồng phản ứng
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

### Đồng thời có cấu trúc và xử lý lỗi
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án
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

### Cấu hình bản dựng (build.gradle.kts)
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

### Lệnh quản lý phụ thuộc
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

### Đường dẫn CI/CD (Hành động trên GitHub)
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

##Thử nghiệm
### Khung kiểm tra và thiết lập
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

### Unit Test với Mocking
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

### Kiểm thử Coroutine
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

### Lệnh kiểm tra
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

## Khả năng tương tác
### Khả năng tương tác Java
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

### Kotlin/Native và C Interop
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

### Tương tác Kotlin/JS
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

## Mẫu thiết kế
### Singleton (Theo mặc định là An toàn theo luồng)
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

### Mẫu trình tạo (Kotlin thành ngữ)
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

### Mẫu chiến lược với Lambdas
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

### Mẫu kho lưu trữ với Generics
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

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
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

### Kỹ thuật tối ưu hóa
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

## Triển khai
### Fat JAR với Shadow Plugin
```kotlin
// build.gradle.kts
plugins {
    id("com.github.johnrengelman.shadow") version "8.1.1"
}
// Build: ./gradlew shadowJar
// Run:  java -jar build/libs/my-app-1.0.0-all.jar
```

### Triển khai Docker
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

### Hình ảnh gốc GraalVM
```kotlin
// build.gradle.kts
plugins {
    id("org.graalvm.buildtools.native") version "0.10.2"
}
// Build native binary: ./gradlew nativeCompile
// Startup time: <100ms, Memory: ~30MB (vs ~300MB for JVM)
```

### Triển khai đa nền tảng Kotlin
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

## Hệ sinh thái
### Khung
| Khung | Tên miền |
|----------||--------|
| **Jetpack Soạn** | Bộ công cụ giao diện người dùng Android hiện đại |
| **Ktor** | Khung web phía máy chủ nhẹ |
| **Khởi động mùa xuân** | Hỗ trợ đầy đủ Kotlin cho chương trình phụ trợ doanh nghiệp |
| **Đa nền tảng Kotlin** | Chia sẻ mã giữa Android, iOS, web, máy tính để bàn |
| **Lộ trần** | Thư viện SQL Kotlin (truy vấn loại an toàn) |
| **Koin** | Khung tiêm phụ thuộc |
### Công cụ xây dựng
| Công cụ | Mục đích |
|------|----------|
| **Gradle (Kotlin DSL)** | Hệ thống xây dựng — Kotlin là ngôn ngữ tập lệnh xây dựng được ưa thích |
| **Ý TƯỞNG IntelliJ** | IDE của JetBrains — hỗ trợ Kotlin tốt nhất |
---

## Khi nào nên sử dụng Kotlin
| Kịch bản | Tại sao lại sử dụng Kotlin | Thay thế tốt hơn |
|----------|-------------|-------------------|
| Phát triển Android | Ngôn ngữ ưa thích của Google | Java (dành cho các cơ sở mã cũ) |
| Phụ trợ JVM | Thay thế Java hiện đại | Java, Đi |
| Đa nền tảng (logic chia sẻ) | Đa nền tảng Kotlin | Flutter (để chia sẻ giao diện người dùng) |
| Ứng dụng máy tính để bàn | Có thể thực hiện được với Compose Multiplatform | C#, Swift cho bản địa |
| Các ứng dụng JVM chung | Ít dài dòng hơn Java | Java cho các nhóm lớn hơn |
| Lập trình hệ thống không phải JVM | Không phải mục tiêu chính | Rust, Đi, C |
| Giao diện web | Kotlin/JS tồn tại nhưng bị giới hạn | TypeScript, JavaScript |
| Khoa học dữ liệu / ML | Không phải hệ sinh thái | Python, R |
---

## Hỏi đáp tổng hợp
### Câu hỏi 1: Tính năng an toàn null của Kotlin thực sự hoạt động như thế nào?
**A:** Kotlin phân biệt giữa loại có thể rỗng (`String?`) và loại không thể rỗng (`String`) tại thời điểm biên dịch. Trình biên dịch ngăn bạn gọi các phương thức trên các loại nullable mà không cần kiểm tra null. Lệnh gọi an toàn (`?.`), toán tử Elvis (`?:`) và xác nhận không null (`!!`) cung cấp các chiến lược khác nhau. Các diễn viên thông minh tự động thu hẹp các loại sau khi kiểm tra null.
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

### Câu 2: Coroutine là gì và chúng khác với thread như thế nào?
**A:** Coroutine là các tác vụ nhẹ, có tính hợp tác chạy trên các luồng. Họ có thể tạm dừng thực thi (mà không chặn luồng) và tiếp tục lại sau. Hàng triệu coroutine có thể chạy trên một vài luồng.  Các hàm`suspend`chỉ có thể được gọi từ coroutine hoặc các hàm tạm ngưng khác. Vòng đời kiểm soát phạm vi coroutine — khi một phạm vi bị hủy, tất cả các coroutine của phạm vi đó cũng bị hủy.
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

### Câu 3: Lớp dữ liệu, lớp niêm phong và lớp giá trị là gì?
**A:** Các lớp dữ liệu tự động tạo các hàm`equals`,`hashCode`,`toString`,`copy`và`componentN`— lý tưởng cho chủ sở hữu dữ liệu. Các lớp kín hạn chế tính kế thừa — tất cả các lớp con phải nằm trong cùng một tệp — cho phép biểu thức`when`đầy đủ. Các lớp giá trị bao bọc một giá trị duy nhất với chi phí bằng 0 khi chạy (lớp nội tuyến).
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

### Q4: Các chức năng mở rộng hoạt động như thế nào và những hạn chế của chúng là gì?
**A:** Hàm mở rộng thêm phương thức vào các loại hiện có mà không cần kế thừa hoặc sửa đổi. Chúng được giải quyết tĩnh (dựa trên loại được khai báo, không phải loại thời gian chạy). Họ không thể truy cập các thành viên tư nhân. Thuộc tính mở rộng hoạt động tương tự. Chúng được sử dụng rộng rãi trong thư viện tiêu chuẩn của Kotlin và hoạt động phát triển Android.
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

### Câu 5: Kotlin Multiplatform là gì và khi nào tôi nên sử dụng nó?
**Đáp:** Kotlin Multiplatform (KMP) cho phép bạn chia sẻ mã giữa các nền tảng (Android, iOS, web, máy tính để bàn, máy chủ) trong khi vẫn giữ giao diện người dùng dành riêng cho nền tảng. Các lớp logic nghiệp vụ, mạng và dữ liệu có thể được chia sẻ; Giao diện người dùng vẫn nguyên bản. Hãy sử dụng nó khi bạn có một nhóm hiểu biết về Kotlin và muốn tối đa hóa việc chia sẻ mã mà không cần sử dụng đa nền tảng (như Flutter).
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

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Xây dựng DSL Type-Safe Builder
**Báo cáo vấn đề:** Tạo Kotlin DSL để xây dựng tài liệu HTML một cách an toàn trong thời gian biên dịch. DSL phải thực thi cấu trúc HTML hợp lệ (ví dụ: chỉ`<head>`bên trong`<html>`,`<li>`chỉ bên trong`<ul>`hoặc`<ol>`).
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần: (1) các hàm xây dựng với`@DslMarker`để ngăn chặn rò rỉ phạm vi, (2) cú pháp DSL dựa trên máy thu, (3) thực thi việc lồng hợp lệ trong thời gian biên dịch. Trình tạo an toàn loại và chú thích`@DslMarker`của Kotlin được thiết kế cho việc này.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng`@DslMarker`để tạo chú thích kiểm soát phạm vi.
- Mỗi phần tử HTML là một lớp có các phương thức xây dựng cho các phần tử con hợp lệ của nó.
-`@HtmlTagMarker`ngăn chặn việc truy cập các phương thức phạm vi cha mẹ bên trong phạm vi con.
- Sử dụng toán tử`invoke`để có cú pháp rõ ràng.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- An toàn về loại:`@DslMarker`ngăn chặn rò rỉ phạm vi -`title()`không thể truy cập được bên trong`body {}`.
- Trình biên dịch thực thi việc lồng hợp lệ tại thời điểm biên dịch — không cần kiểm tra thời gian chạy.
- Khả năng mở rộng: thêm các phần tử mới bằng cách tạo các lớp với các phương thức con thích hợp.
- Sản xuất: sử dụng`kotlinx.html`cho DSL HTML toàn diện, được thử nghiệm tốt.
### Vấn đề 2: Triển khai State Machine với Coroutines
**Báo cáo vấn đề:** Xây dựng một máy trạng thái dựa trên coroutine cho nhân vật trong trò chơi để xử lý các sự kiện đầu vào, chuyển đổi giữa các trạng thái và hỗ trợ lệnh gọi lại hoạt ảnh.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần: (1) trạng thái có hành động vào/ra, (2) chuyển đổi theo hướng sự kiện, (3) vòng lặp xử lý dựa trên coroutine, (4) lệnh gọi lại hoạt ảnh khi chuyển đổi trạng thái. Máy trạng thái chạy như một sự kiện tiêu thụ coroutine kéo dài từ một kênh.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng lớp seal cho các trạng thái và sự kiện.
- Sử dụng`Channel`để chuyển sự kiện.
- Vòng lặp máy trạng thái tiêu thụ các sự kiện với`for (event in channel)`.
- Quá trình chuyển đổi kích hoạt lệnh gọi lại thoát/nhập.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- Loại an toàn: các lớp kín đảm bảo mọi trạng thái và sự kiện đều được xử lý. Trình biên dịch bắt các chuyển tiếp bị thiếu.
- Coroutine-based: các sự kiện được xử lý tuần tự mà không bị chặn. Kênh cung cấp áp suất ngược.
- Vòng đời: việc hủy phạm vi sẽ dừng máy trạng thái một cách sạch sẽ.
- Sản xuất: đối với các máy trạng thái phức tạp, sử dụng`tinder-statemachine`hoặc mô hình hóa các trạng thái bằng thư viện máy trạng thái hình thức.
---

## Bản tóm tắt
Kotlin là Java hiện đại được thực hiện đúng cách. Nó chạy trên JVM, sử dụng tất cả các thư viện Java, nhưng loại bỏ các ngoại lệ con trỏ null, giảm bản soạn sẵn và thêm các tính năng hiện đại như coroutine, hàm mở rộng và các lớp kín. Để phát triển Android, Kotlin là sự lựa chọn rõ ràng. Đối với các chương trình phụ trợ JVM, đây là một giải pháp thay thế hấp dẫn cho Java. Kotlin Multiplatform mở rộng phạm vi tiếp cận của mình sang iOS và hơn thế nữa. Nếu bạn đã biết Java thì học Kotlin là bước tiếp theo tự nhiên và bổ ích.