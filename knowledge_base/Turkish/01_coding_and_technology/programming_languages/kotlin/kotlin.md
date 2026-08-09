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
#Kotlin
Kotlin, JetBrains tarafından geliştirilen ve ilk olarak 2011'de piyasaya sürülen (2016'da 1.0) statik olarak yazılmış, derlenmiş bir programlama dilidir. Java Sanal Makinesi (JVM) üzerinde çalışır ve Java ile tamamen birlikte çalışabilir; bu, Kotlin'deki herhangi bir Java kitaplığını kullanabileceğiniz ve herhangi bir sarmalayıcı olmadan Java'dan Kotlin kodunu çağırabileceğiniz anlamına gelir. Google, 2017 yılında Kotlin'i Android geliştirme için tercih edilen dil olarak duyurdu ve o zamandan beri baskın Android dili haline geldi.
Kotlin, Java'nın sorunlu noktalarını düzeltmek için tasarlandı: ayrıntı, boş işaretçi istisnaları ve eksik modern özellikler. Sonuç, devasa Java ekosistemiyle tam uyumluluğu korurken, modernleştirilmiş bir Java hissi veren (özlü, güvenli ve etkileyici) bir dildir.
---

## Kotlin Neden Önemlidir
- **Android standardı**: Google'ın Android için tercih ettiği dil. En yeni Android kodu Kotlin'dir.
- **%100 Java uyumlu**: Tüm Java kitaplıklarını, çerçevelerini ve araçlarını kullanın. Yavaş yavaş göç edin.
- **Boş güvenlik**: Tür sistemi, derleme zamanında boş işaretçi istisnalarını önler.
- **Kısa**: Veri sınıfları, uzantı işlevleri, akıllı yayınlar gibi Java'ya göre çok daha az standart.
- **Coroutines**: Eşzamansız programlama için hafif iş parçacıkları — Java'nın CompletableFuture veya geri aramalarından daha basittir.
- **Multiplatform**: Kotlin Multiplatform, Android, iOS, web ve arka uç arasında kod paylaşmanıza olanak tanır.
- **Sunucu tarafı**: Ktor, Spring Boot (tam Kotlin desteği) ve Exposed, Kotlin'i arka uçlar için uygun hale getirir.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **JVM bağımlılığı** | JVM (veya JVM olmayan hedefler için Kotlin/Native) gerektirir | Küçük dağıtımlar için GraalVM yerel görüntüsünü kullanın |
| **Derleme hızı** | Büyük projeler için Java'dan daha yavaş | Artımlı derlemeyi kullanın; Kotlin 2.0 bunu geliştiriyor |
| **Java geliştiricileri için öğrenme eğrisi** | Uzantı işlevleri, eşyordamlar, DSL'ler yeni kavramlardır | Kademeli evlat edinme; çoğu Java modeli hala çalışıyor |
| **Java'dan daha küçük topluluk** | Daha az Kotlin'e özgü kaynak ve kitaplık | Java'nın devasa ekosisteminden yararlanın |
| **Kotlin Çoklu Platform olgunluğu** | Üretim iOS paylaşımı için gelişmeye devam ediliyor | Paylaşılan iş mantığı için kullanın; kullanıcı arayüzünü yerel tut |
---

## Söz Diziminin Temelleri
### Değişkenler ve Türler
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

### Sıfır Güvenlik
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

### Veri Sınıfları ve Uzantı İşlevleri
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

### Eşyordamlar — Zaman Uyumsuz Programlama
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

### Mühürlü Sınıflar ve Desen Eşleştirme
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

### Yüksek Dereceli Fonksiyonlar
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

## Gelişmiş Sözdizimi ve Desenler
### Jenerikler ve Tür Parametreleri
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

### Yansımayla Metaprogramlama
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

### Gelişmiş Yıkım ve Desen Eşleştirme
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

### Operatör Aşırı Yüklemesi
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

### DSL Oluşturma Modelleri
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

## Eşzamanlılık ve Paralellik (Derin İnceleme)
### Eşyordam Göndericileri ve İçerikleri
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

### Kanallar — Eşyordamlar Arasındaki İletişim
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

### Akış — Reaktif Akışlar
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

### Yapılandırılmış Eşzamanlılık ve Hata İşleme
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı
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

### Yapı Yapılandırması (build.gradle.kts)
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

### Bağımlılık Yönetimi Komutları
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

### CI/CD İşlem Hattı (GitHub Eylemleri)
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

## Test etme
### Çerçeveleri ve Kurulumu Test Etme
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

### Mocking ile Birim Testleri
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

### Eşyordamları Test Etme
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

### Test Komutları
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

## Birlikte Çalışabilirlik
### Java Birlikte Çalışabilirliği
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

### Kotlin/Yerel ve C Birlikte Çalışma
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

### Kotlin/JS Birlikte Çalışma
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

## Tasarım Desenleri
### Singleton (Varsayılan Olarak İş Parçacığı Güvenli)
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

### Oluşturucu Kalıbı (Deyimsel Kotlin)
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

### Lambda'larla Strateji Modeli
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

### Jeneriklerle Depo Modeli
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

## Performans ve Optimizasyon
### Profil Oluşturma Araçları
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

### Optimizasyon Teknikleri
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

## Dağıtım
### Gölge Eklentili Fat JAR
```kotlin
// build.gradle.kts
plugins {
    id("com.github.johnrengelman.shadow") version "8.1.1"
}
// Build: ./gradlew shadowJar
// Run:  java -jar build/libs/my-app-1.0.0-all.jar
```

### Docker Dağıtımı
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

### GraalVM Yerel Görüntüsü
```kotlin
// build.gradle.kts
plugins {
    id("org.graalvm.buildtools.native") version "0.10.2"
}
// Build native binary: ./gradlew nativeCompile
// Startup time: <100ms, Memory: ~30MB (vs ~300MB for JVM)
```

### Kotlin Çoklu Platform Dağıtımı
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

## Ekosistem
### Çerçeveler
| Çerçeve | Etki Alanı |
|-----------|-----------|
| **Jetpack Oluşturma** | Modern Android kullanıcı arayüzü araç seti |
| **Ktor** | Hafif sunucu tarafı web çerçevesi |
| **Bahar Çizme** | Kurumsal arka uçlar için tam Kotlin desteği |
| **Kotlin Çoklu Platform** | Kodu Android, iOS, web, masaüstü arasında paylaşın |
| **Açığa çıkan** | Kotlin SQL kitaplığı (tür güvenli sorgular) |
| **Koin** | Bağımlılık enjeksiyon çerçevesi |
### Oluşturma Araçları
| Araç | Amaç |
|------|------------|
| **Gradle (Kotlin DSL)** | Derleme sistemi — Kotlin, tercih edilen derleme komut dosyası dilidir |
| **IntelliJ FİKİRİ** | JetBrains'ten IDE — en iyi Kotlin desteği |
---

## Kotlin Ne Zaman Kullanılmalı?
| Senaryo | Neden Kotlin | Daha İyi Alternatif |
|----------|-----------|-----------|
| Android geliştirme | Google'ın tercih ettiği dil | Java (eski kod tabanları için) |
| JVM arka uçları | Modern Java alternatifi | Java, Git |
| Çapraz platform (paylaşılan mantık) | Kotlin Çoklu Platform | Flutter (kullanıcı arayüzü paylaşımı için) |
| Masaüstü uygulamaları | Compose Multiplatform ile Mümkün | Yerel dil için C#, Swift |
| Genel JVM uygulamaları | Java'dan daha az ayrıntılı | Daha büyük ekipler için Java |
| JVM dışı sistem programlama | Birincil hedef değil | Pas, Git, C |
| Web arayüzü | Kotlin/JS var ama sınırlı | TypeScript, JavaScript |
| Veri bilimi / ML | Ekosistem değil | Python, R |
---

## Özet
Kotlin, modern Java'nın doğru şekilde kullanılmasıdır. JVM üzerinde çalışır, tüm Java kitaplıklarını kullanır, ancak boş işaretçi istisnalarını ortadan kaldırır, ortak metinleri azaltır ve eşyordamlar, uzantı işlevleri ve mühürlü sınıflar gibi modern özellikler ekler. Android geliştirme için Kotlin net bir seçimdir. JVM arka uçları için Java'ya ilgi çekici bir alternatiftir. Kotlin Multiplatform, erişimini iOS ve ötesine genişletiyor. Java'yı zaten biliyorsanız Kotlin'i öğrenmek doğal ve ödüllendirici bir sonraki adımdır.