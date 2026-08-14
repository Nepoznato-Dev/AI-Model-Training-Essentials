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
# কোটলিন — সিনট্যাক্স রেফারেন্স
এই নথিটি কোটলিন (2.0+) এর জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, নাল সেফটি, কোরোটিন এবং কোটলিন ইডিয়মগুলিতে ফোকাস করে মূল কোটলিন রেফারেন্সের পরিপূরক।
---

## অপারেটর এবং এক্সপ্রেশন
### মূল অপারেটর
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `+``-``*``/``%`| পাটিগণিত | `a + b`| |
| `..`| পরিসীমা | `1..10`| অন্তর্ভুক্ত পরিসর |
| `until`| অর্ধ-খোলা পরিসীমা | `1 until 10`| `1..9`|
| `downTo`| অবরোহী পরিসীমা | `10 downTo 1`| |
| `==``!=` | কাঠামোগত সমতা | `a == b`|`.equals()`| কল করে
| `===``!==` | রেফারেন্সিয়াল সমতা | `a === b`| একই উদাহরণ |
| `<``>``<=``>=` | তুলনা | `a >= b`| প্রয়োজন`Comparable`|
| `&&``\|\|``!`| যৌক্তিক | `a && b`| শর্ট সার্কিট |
| `?:`| এলভিস অপারেটর | `a ?: b`|`a`শূন্য হলে`b`ফেরত দেয় |
| `?.`| নিরাপদ কল | `a?.b`| যদি`a`শূন্য হয় |
| `!!`| অ-শূন্য দাবী | `a!!`| শূন্য হলে NPE নিক্ষেপ করে |
| `as`| কাস্ট | `a as String`| ClassCastException নিক্ষেপ করে |
| `as?`| নিরাপদ কাস্ট | `a as? String`| ব্যর্থ হলে শূন্য ফেরত দেয় |
| `in`| সদস্যপদ | `x in list`| |
| `!in`| সদস্য নয় | `x !in list`| |
| `is`| টাইপ চেক | `x is String`| চেকের পরে স্মার্ট কাস্ট |
| `!is`| টাইপ না | `x !is String`| |
### অপারেটর ওভারলোডিং
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

## নিয়ন্ত্রণ প্রবাহ
### অভিব্যক্তি
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

### স্মার্ট কাস্ট
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

## ক্লাস এবং অবজেক্ট
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

## করুটিন এবং প্রবাহ
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

## জেনেরিক এবং টাইপ সিস্টেম
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

## স্কোপ ফাংশন
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

## সারাংশ
কোটলিনের সিনট্যাক্স সংক্ষিপ্ত, নিরাপদ এবং জাভার সাথে ইন্টারঅপারেবল। নাল সেফটি কম্পাইলের সময় পুরো ক্লাসের বাগ দূর করে। Coroutines অ্যাসিঙ্ক্রোনাস কোড লেখার একটি প্রাকৃতিক উপায় প্রদান করে। সিল করা ক্লাস, ডেটা ক্লাস, এবং এক্সটেনশন ফাংশন এক্সপ্রেসিভ ডোমেন মডেলিং সক্ষম করে। ভাষার শক্তি তার বৈশিষ্ট্যগুলির ইন্টারপ্লে থেকে আসে — স্কোপ ফাংশন, ডিএসএল, ইনলাইন ক্লাস এবং রিফাইড জেনেরিকগুলিকে একত্রিত করে এমন কোড তৈরি করে যা লেখার জন্য নিরাপদ এবং আনন্দদায়ক।