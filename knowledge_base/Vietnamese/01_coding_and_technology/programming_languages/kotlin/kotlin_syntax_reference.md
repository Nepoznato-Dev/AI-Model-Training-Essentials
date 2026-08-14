---
# Metadata
title: "Kotlin — Syntax Reference"
description: "Detailed syntax reference for Kotlin covering null safety, control flow, classes, coroutines, generics, DSLs, and modern Kotlin features."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [kotlin, syntax-reference, null-safety, coroutines, oop, generics, dsl, coding-and-technology]
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
# Kotlin — Tham khảo cú pháp
Tài liệu này cung cấp tài liệu tham khảo cú pháp có cấu trúc và toàn diện cho Kotlin (2.0+). Nó bổ sung cho tài liệu tham khảo chính về Kotlin bằng cách tập trung vào các mẫu cú pháp đầy đủ, an toàn null, coroutine và thành ngữ Kotlin.
---

## Toán tử & Biểu thức
### Toán tử cốt lõi
| Nhà điều hành | Tên | Ví dụ | Ghi chú |
|----------|------|----------|-------|
| `+``-``*``/``%`| Số học | `a + b`| |
| `..`| Phạm vi | `1..10`| Phạm vi bao gồm |
| `until`| Phạm vi nửa mở | `1 until 10`| `1..9`|
| `downTo`| Phạm vi giảm dần | `10 downTo 1`| |
| `==``!=` | Bình đẳng về cơ cấu | `a == b`| Cuộc gọi`.equals()`|
| `===``!==` | Bình đẳng tham khảo | `a === b`| Cùng một trường hợp |
| `<``>``<=``>=` | So sánh | `a >= b`| Yêu cầu`Comparable`|
| `&&``\|\|``!`| Hợp lý | `a && b`| Đoản mạch |
| `?:`| Toán tử Elvis | `a ?: b`| Trả về`b`nếu`a`rỗng |
| `?.`| Cuộc gọi an toàn | `a?.b`| Trả về null nếu`a`là null |
| `!!`| Khẳng định không null | `a!!`| Ném NPE nếu null |
| `as`| Diễn viên | `a as String`| Ném ClassCastException |
| `as?`| Diễn viên an toàn | `a as? String`| Trả về null khi thất bại |
| `in`| Thành viên | `x in list`| |
| `!in`| Không phải thành viên | `x !in list`| |
| `is`| Kiểm tra kiểu | `x is String`| Diễn viên thông minh sau khi kiểm tra |
| `!is`| Không gõ | `x !is String`| |
### Quá tải toán tử
```kotlin
data class Vector2D(val x: Double, val y: Double) {
    operator fun plus(other: Vector2D) = Vector2D(x + other.x, y + other.y)
    operator fun minus(other: Vector2D) = Vector2D(x - other.x, y - other.y)
    operator fun times(scalar: Double) = Vector2D(x * scalar, y * scalar)
    operator fun unaryMinus() = Vector2D(-x, -y)
    operator fun component1() = x
    operator fun component2() = y
}

val v = Vector2D(1.0, 2.0) + Vector2D(3.0, 4.0)  // Vector2D(4.0, 6.0)
val (x, y) = v  // Destructuring via componentN
```

---

## Luồng điều khiển
### Biểu thức
```ksharp
// if is an expression
val max = if (a > b) a else b

// when is an expression
val description = when {
    x > 0 -> "positive"
    x < 0 -> "negative"
    else -> "zero"
}

// when with subject
val length = when (s) {
    is String -> s.length
    is Collection -> s.size
    is Array<*> -> s.size
    else -> -1
}
```

### Diễn viên thông minh
```kotlin
// Smart cast — compiler narrows type after check
fun process(obj: Any): String = when (obj) {
    is Int -> "Integer: $obj"          // obj is Int here
    is String -> "String(${obj.length})" // obj is String here
    is List<*> -> "List with ${obj.size} items"
    null -> "null"
    else -> "Unknown: ${obj::class}"
}

// Smart cast with &&
fun validate(x: Any?) {
    if (x != null && x is String) {
        println(x.length)  // Smart cast to String
    }
}
```

---

## Lớp & Đối tượng
```kotlin
// Data class
data class User(val name: String, val email: String) {
    // Auto-generates: equals, hashCode, toString, copy, componentN
}

// Sealed class hierarchy
sealed class Result<out T> {
    data class Success<T>(val data: T) : Result<T>()
    data class Error(val exception: Throwable) : Result<Nothing>()
    object Loading : Result<Nothing>()
}

// Object — singleton
object AppConfig {
    val apiBaseUrl = "https://api.example.com"
    val timeout = 30_000
}

// Companion object — factory methods, static-like members
class Database private constructor(val url: String) {
    companion object {
        fun connect(url: String): Database = Database(url)
    }
}

// Enum with behavior
enum class Planet(val mass: Double, val radius: Double) {
    EARTH(5.97e24, 6.371e6),
    MARS(6.42e23, 3.390e6);

    fun surfaceGravity(): Double = 6.674e-11 * mass / (radius * radius)
}

// Value class — zero-overhead wrapper
@JvmInline
value class Email(val value: String) {
    init { require(value.contains("@")) { "Invalid email" } }
}

// Delegation
interface Printer { fun print() }
class ConsolePrinter : Printer { override fun print() = println("console") }
class Service(printer: Printer) : Printer by printer
```

---

## Coroutine & Flow
```kotlin
// Suspend function
suspend fun fetchUser(id: String): User = withContext(Dispatchers.IO) {
    httpClient.get("/api/users/$id").body()
}

// Coroutine builders
launch { }       // Fire and forget
async { }        // Returns Deferred<T>
runBlocking { }  // Blocks thread (for main/test)

// Structured concurrency
coroutineScope {
    val deferred1 = async { task1() }
    val deferred2 = async { task2() }
    val result = deferred1.await() + deferred2.await()
}

// Channels
val channel = Channel<Int>()
launch { repeat(5) { channel.send(it) }; channel.close() }
launch { for (value in channel) { println(value) } }

// Flow — cold async stream
fun numbers(): Flow<Int> = flow {
    for (i in 1..10) {
        delay(100)
        emit(i)
    }
}

// Flow operators
numbers()
    .filter { it % 2 == 0 }
    .map { it * it }
    .flowOn(Dispatchers.Default)
    .collect { println(it) }

// StateFlow — hot state holder
class ViewModel {
    private val _uiState = MutableStateFlow<UiState>(UiState.Loading)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()
}
```

---

## Hệ thống Generic & Loại
```kotlin
// Generic function
fun <T> listOf(item: T, vararg rest: T): List<T> = listOf(item, *rest)

// Generic class
class Stack<T> {
    private val items = mutableListOf<T>()
    fun push(item: T) = items.add(item)
    fun pop(): T = items.removeAt(items.lastIndex)
    fun peek(): T = items.last()
}

// Variance
interface Producer<out T> { fun produce(): T }   // Covariant — produces T
interface Consumer<in T> { fun consume(item: T) } // Contravariant — consumes T

// Type constraints
fun <T : Comparable<T>> sorted(a: T, b: T): List<T> =
    if (a <= b) listOf(a, b) else listOf(b, a)

// Reified type parameters (inline functions)
inline fun <reified T> Gson.fromJson(json: String): T =
    this.fromJson(json, T::class.java)

// Star projection
fun printAll(items: List<*>) {
    items.forEach { println(it) }
}
```

---

## Hàm phạm vi
```kotlin
// let — transform nullable, scope: 'it'
val length: Int? = name?.let { it.length }

// apply — configure object, scope: 'this', returns this
val user = User("Alice", "").apply {
    email = "alice@example.com"
}

// also — side effect, scope: 'it', returns this
val result = compute().also { log("Result: $it") }

// run — compute with context, scope: 'this', returns result
val description = user.run { "$name ($email)" }

// with — operate on object, scope: 'this', returns result
with(config) {
    println("Host: $host, Port: $port")
}
```

---

## Bản tóm tắt
Cú pháp của Kotlin ngắn gọn, an toàn và có thể tương tác với Java. An toàn không loại bỏ toàn bộ lớp lỗi tại thời điểm biên dịch. Coroutine cung cấp một cách tự nhiên để viết mã không đồng bộ. Các lớp kín, lớp dữ liệu và các hàm mở rộng cho phép lập mô hình miền biểu cảm. Sức mạnh của ngôn ngữ đến từ sự tương tác giữa các tính năng của nó - các hàm phạm vi, DSL, các lớp nội tuyến và các tổng quát thống nhất kết hợp với nhau để tạo ra mã vừa an toàn vừa thú vị khi viết.