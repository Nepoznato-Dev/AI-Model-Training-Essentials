<!--
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

-->
# Kotlin - การอ้างอิงไวยากรณ์
เอกสารนี้ให้การอ้างอิงไวยากรณ์ที่มีโครงสร้างและครอบคลุมสำหรับ Kotlin (2.0+) มันช่วยเสริมการอ้างอิง Kotlin หลักโดยมุ่งเน้นไปที่รูปแบบไวยากรณ์ที่ละเอียดถี่ถ้วน ความปลอดภัยแบบ null, coroutines และสำนวน Kotlin
---

## ตัวดำเนินการและนิพจน์
### ผู้ประกอบการหลัก
| ตัวดำเนินการ | ชื่อ | ตัวอย่าง | หมายเหตุ |
|----------|-|---------|-------|
| `+``-``*``/``%`| เลขคณิต | `a + b`| |
| `..`| พิสัย | `1..10`| ช่วงรวม |
| `until`| ช่วงเปิดครึ่ง | `1 until 10`| `1..9`|
| `downTo`| จากมากไปน้อย | `10 downTo 1`| |
| `==``!=` | ความเท่าเทียมกันทางโครงสร้าง | `a == b`| เรียก`.equals()`|
| `===``!==` | ความเท่าเทียมกันในการอ้างอิง | `a === b`| อินสแตนซ์เดียวกัน |
| `<``>``<=``>=` | การเปรียบเทียบ | `a >= b`| ต้องใช้`Comparable`|
| `&&``\|\|``!`| ตรรกะ | `a && b`| ลัดวงจร |
| `?:`| ตัวดำเนินการเอลวิส | `a ?: b`| ส่งกลับ`b`ถ้า`a`เป็น null |
| `?.`| โทรอย่างปลอดภัย | `a?.b`| ส่งกลับค่า null ถ้า`a`เป็น null |
| `!!`| การยืนยันที่ไม่เป็นโมฆะ | `a!!`| พ่น NPE ถ้าเป็นโมฆะ |
| `as`| นักแสดง | `a as String`| พ่น ClassCastException |
| `as?`| โยนอย่างปลอดภัย | `a as? String`| ส่งคืนค่าว่างเมื่อล้มเหลว |
| `in`| สมาชิก | `x in list`| |
| `!in`| ไม่เป็นสมาชิก | `x !in list`| |
| `is`| พิมพ์เช็ค | `x is String`| สมาร์ทแคสต์หลังตรวจสอบ |
| `!is`| ไม่พิมพ์ | `x !is String`| |
### โอเปอเรเตอร์โอเวอร์โหลด
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

## การควบคุมการไหล
### การแสดงออก
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

### แคสต์อัจฉริยะ
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

## คลาสและวัตถุ
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

## โครูทีนและโฟลว์
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

## ข้อมูลทั่วไป & ระบบประเภท
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

## ฟังก์ชั่นขอบเขต
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

## สรุป
ไวยากรณ์ของ Kotlin นั้นกระชับ ปลอดภัย และใช้งานร่วมกับ Java ได้ ความปลอดภัยแบบ Null จะกำจัดข้อผิดพลาดทั้งคลาสในขณะคอมไพล์ Coroutines มอบวิธีที่เป็นธรรมชาติในการเขียนโค้ดแบบอะซิงโครนัส คลาสที่ปิดผนึก คลาสข้อมูล และฟังก์ชันส่วนขยายช่วยให้สามารถสร้างโมเดลโดเมนที่แสดงออกได้ พลังของภาษามาจากการทำงานร่วมกันของฟีเจอร์ต่างๆ เช่น ฟังก์ชันขอบเขต, DSL, คลาสแบบอินไลน์ และชื่อสามัญที่ได้รับการปรับปรุงใหม่ รวมกันเพื่อสร้างโค้ดที่ทั้งปลอดภัยและสนุกสนานในการเขียน