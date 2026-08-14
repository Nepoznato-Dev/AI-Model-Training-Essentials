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
# Kotlin — 構文リファレンス
このドキュメントは、Kotlin (2.0 以降) の包括的で構造化された構文リファレンスを提供します。網羅的な構文パターン、null 安全性、コルーチン、Kotlin イディオムに焦点を当て、メインの Kotlin リファレンスを補完します。
---

## 演算子と式
### コアオペレーター
|オペレーター |名前 |例 |メモ |
|----------|------|----------|----------|
| `+``-``*``/``%`|算数 | `a + b`| |
| `..`|範囲 | `1..10`|包含範囲 |
| `until`|半開範囲 | `1 until 10`| `1..9`|
| `downTo`|降順範囲 | `10 downTo 1`| |
| `==`|`!=`|構造的平等 | `a == b`|`.equals()`を呼び出します。
| `===`|`!==`|参照の等価性 | `a === b`|同じインスタンス |
| `<``>``<=``>=` |比較 | `a >= b`|`Comparable`が必要 |
| `&&``\|\|``!`|論理 | `a && b`|短絡 |
|  XQZマーカー30XQZ |エルヴィス オペレーター | `a ?: b`|`a`が null の場合は`b`を返します。
| `?.`|安全な通話 | `a?.b`|`a`が null の場合は null を返します。
| `!!`|非 null アサーション | `a!!`| null の場合は NPE をスローします。
| `as`|キャスト |  XQZマーカー40XQZ | ClassCastException をスローします。
| `as?`|安全なキャスト | `a as? String`|失敗した場合は null を返します。
| `in`|メンバーシップ | `x in list`| |
| `!in`|会員ではありません | `x !in list`| |
| `is`|タイプチェック | `x is String`|チェック後のスマートキャスト |
| `!is`| | と入力しないでください。  XQZマーカー50XQZ | |
### 演算子のオーバーロード
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

## 制御フロー
### 式
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

### スマートキャスト
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

## クラスとオブジェクト
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

## コルーチンとフロー
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

## ジェネリックスと型システム
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

## スコープ関数
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

＃＃ まとめ
Kotlin の構文は簡潔かつ安全で、Java と相互運用可能です。 Null 安全性は、コンパイル時にバグのクラス全体を排除します。コルーチンは、非同期コードを作成する自然な方法を提供します。シールされたクラス、データ クラス、および拡張関数により、表現力豊かなドメイン モデリングが可能になります。この言語の力は、その機能の相互作用によって生まれます。スコープ関数、DSL、インライン クラス、具体化されたジェネリックスが組み合わされて、安全で楽しく書けるコードが生成されます。