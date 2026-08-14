---
# Metadata
title: "Kotlin — Cheat Sheet"
description: "Quick-reference cheat sheet for Kotlin syntax, null safety, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [kotlin, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Kotlin – Spickzettel
## Grundlagen
```kotlin
// Variables
var name = "Alice"       // mutable, type inferred
val age = 30             // immutable (read-only)
val pi: Double = 3.14159
val active: Boolean = true
const val MAX = 100      // compile-time constant

// Nullable types
var email: String? = null
val phone: String? = "555-1234"

// String templates
"Hello, $name!"
"Age: ${age + 1}"
"Pi: ${"%.2f".format(pi)}"

// String methods
name.length
name.uppercase()
name.lowercase()
name.trim()
name.contains("lic")
name.replace("Alice", "Bob")
name.split("")
name.take(3)       // "Ali"
name.dropLast(2)
```

## Null Sicherheit
```kotlin
// Safe call
val len = email?.length  // null if email is null

// Elvis operator
val value = email ?: "default"
val len = email?.length ?: 0

// Not-null assertion (avoid)
val forced = email!!  // NPE if null

// let with safe call
email?.let { println(it) }  // runs only if not null

// Safe cast
val str: String? = obj as? String

// require / check
fun process(input: String?) {
    val name = input ?: throw IllegalArgumentException("null input")
    require(name.isNotEmpty()) { "empty name" }
    check(name.length < 100) { "too long" }
}
```

## Datenstrukturen
```kotlin
// List
val list = listOf(1, 2, 3)
val mutable = mutableListOf(1, 2, 3)
mutable.add(4)
mutable[0]
mutable.filter { it > 2 }
mutable.map { it * 2 }
mutable.reduce(0) { acc, x -> acc + x }
mutable.forEach { println(it) }
mutable.sorted()
mutable.firstOrNull { it > 5 }
mutable.groupBy { it % 2 }

// Map
val map = mapOf("alice" to 90, "bob" to 85)
val mutableMap = mutableMapOf<String, Int>()
mutableMap["charlie"] = 78
mutableMap["alice"]
mutableMap.getOrDefault("unknown", 0)
mutableMap.keys
mutableMap.values
mutableMap.filter { it.value >= 90 }
mutableMap.mapValues { it.value * 2 }

// Set
val set = setOf(1, 2, 3)
val mutableSet = mutableSetOf(1, 2, 3)
mutableSet.add(4)
mutableSet.contains(2)

// Array
val arr = intArrayOf(1, 2, 3)
val arr2 = arrayOf("a", "b", "c")
arr.size
arr[0]
```

## Kontrollfluss
```kotlin
if (condition) {
    // ...
} else if (other) {
    // ...
} else {
    // ...
}

// Expression (if returns value)
val result = if (condition) "yes" else "no"

// When (switch replacement)
when (value) {
    0 -> println("zero")
    in 1..9 -> println("single digit")
    is String -> println("string: $value")
    null -> println("null")
    else -> println("other")
}

// When as expression
val label = when {
    score >= 90 -> "A"
    score >= 80 -> "B"
    else -> "C"
}

// Loops
for (item in collection) { ... }
for ((i, item) in collection.withIndex()) { ... }
for (i in 0 until 10) { ... }    // 0..9
for (i in 0..10) { ... }         // 0..10
for (i in 10 downTo 1) { ... }
for (i in 0 until 100 step 5) { ... }
while (condition) { ... }
collection.forEach { ... }
```

## Datenklassen und versiegelt
```kotlin
// Data class
data class User(val name: String, val age: Int)
val user = User("Alice", 30)
val (name, age) = user  // destructuring
val copy = user.copy(age = 31)

// Sealed class/interface
sealed interface Shape {
    fun area(): Double
}
data class Circle(val radius: Double) : Shape {
    override fun area() = Math.PI * radius * radius
}
data class Rectangle(val w: Double, val h: Double) : Shape {
    override fun area() = w * h
}

// Enum
enum class Direction { NORTH, SOUTH, EAST, WEST }
enum class Color(val hex: String) {
    RED("#FF0000"), GREEN("#00FF00"), BLUE("#0000FF")
}

// Object (singleton)
object Config {
    val apiUrl = "https://api.example.com"
}

// Value class
@JvmInline
value class UserId(val value: String)
```

## Funktionen und Lambdas
```kotlin
// Function
fun greet(name: String, greeting: String = "Hello"): String =
    "$greeting, $name!"

// Extension function
fun String.isEmail(): Boolean = contains("@") && contains(".")

// Lambda
val square: (Int) -> Int = { it * it }
val add: (Int, Int) -> Int = { a, b -> a + b }

// Higher-order function
fun <T> List<T>.myFilter(predicate: (T) -> Boolean): List<T> {
    val result = mutableListOf<T>()
    for (item in this) if (predicate(item)) result.add(item)
    return result
}

// Scope functions
user.apply { age = 31 }          // returns user
user.also { log(it) }            // returns user
user.let { it.name }             // returns result
with(user) { name }              // returns result
user.run { name }                // returns result

// Inline function
inline fun <T> measure(block: () -> T): T {
    val start = System.currentTimeMillis()
    return block().also { println("Took ${System.currentTimeMillis() - start}ms") }
}
```

## Coroutinen
```kotlin
import kotlinx.coroutines.*

// Suspend function
suspend fun fetchUser(id: Int): User = withContext(Dispatchers.IO) {
    // network call
}

// Launch (fire and forget)
val job = CoroutineScope(Dispatchers.Main).launch {
    val user = fetchUser(1)
    updateUI(user)
}
job.cancel()

// Async (returns result)
val deferred = CoroutineScope(Dispatchers.IO).async {
    fetchUser(1)
}
val user = deferred.await()

// Flow
fun numbers(): Flow<Int> = flow {
    for (i in 1..100) {
        delay(100)
        emit(i)
    }
}

numbers()
    .filter { it % 2 == 0 }
    .map { it * it }
    .collect { println(it) }

// Channel
val channel = Channel<Int>()
launch { channel.send(42) }
launch { println(channel.receive()) }
```

## Fehlerbehandlung
```kotlin
try {
    val result = riskyOperation()
} catch (e: IOException) {
    log("IO error", e)
} catch (e: Exception) {
    log("Error", e)
} finally {
    cleanup()
}

// RunCatching
val result = runCatching { riskyOperation() }
    .getOrElse { defaultValue }

result.onSuccess { println("OK: $it") }
result.onFailure { log("Failed", it) }

// Custom exception
class NotFoundException(id: String) :
    RuntimeException("Not found: $id")
```
