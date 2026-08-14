---
# Metadata
title: "Kotlin — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in Kotlin that catch even experienced developers, with explanations and corrections."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [kotlin, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "20 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Kotlin: errores comunes y antipatrones
Este documento cataloga los errores, trampas y antipatrones más comunes en Kotlin. Cada entrada muestra el enfoque incorrecto, explica por qué falla y proporciona la solución correcta.
---

## 1. Tipos de plataforma y NullPointerException
```kotlin
// ❌ WRONG — trusting Java interop types
fun processName(user: JavaUser) {
    val name: String = user.getName()  // platform type String!
    println(name.length)  // NPE if getName() returns null!
}

// ✅ CORRECT — explicitly handle nullability
fun processName(user: JavaUser) {
    val name: String? = user.getName()
    println(name?.length ?: "Unknown")
}
```

---

## 2. Mal uso de `lateinit`
```kotlin
// ❌ WRONG — accessing before initialization
class MyFragment : Fragment() {
    lateinit var viewModel: MyViewModel
    // if accessed before assignment: UninitializedPropertyAccessException
}

// ✅ CORRECT — check initialization or use nullable
class MyFragment : Fragment() {
    lateinit var viewModel: MyViewModel

    fun doWork() {
        if (::viewModel.isInitialized) {
            viewModel.process()
        }
    }
}

// ✅ CORRECT — use nullable for truly optional dependencies
class MyFragment : Fragment() {
    var viewModel: MyViewModel? = null
}
```

---

## 3.`data class`sin`equals`/`hashCode`adecuados
```kotlin
// ❌ WRONG — data class with mutable property
data class User(var name: String, var score: Int)

val user = User("Alice", 100)
val set = hashSetOf(user)
user.score = 200  // breaks HashSet! Can't find user anymore
set.contains(user)  // false!

// ✅ CORRECT — use val in data classes
data class User(val name: String, val score: Int)
```

---

## 4. No utilizar correctamente las funciones de alcance
```kotlin
// ❌ WRONG — using let when apply is more appropriate
val user = User("Alice", 25).let {
    it.name = "Bob"  // confusing: let is for transformations
    it
}

// ✅ CORRECT — apply for configuration
val user = User("Alice", 25).apply {
    name = "Bob"
}

// ✅ CORRECT — let for transformations
val length = "Hello".let { it.length }

// ✅ CORRECT — also for side effects
val users = fetchUsers().also { log("Fetched ${it.size} users") }

// ✅ CORRECT — run for blocks returning value
val result = run {
    val x = computeX()
    val y = computeY()
    x + y
}
```

---

## 5. Corrutinas: No manejar cancelaciones
```kotlin
// ❌ WRONG — blocking inside coroutine
viewModelScope.launch {
    Thread.sleep(1000)  // blocks the thread!
    val data = repository.getData()
}

// ✅ CORRECT — use suspend functions
viewModelScope.launch {
    delay(1000)  // non-blocking
    val data = repository.getData()
}

// ✅ CORRECT — check cancellation in long computations
viewModelScope.launch {
    for (i in 0..1000000) {
        ensureActive()  // throws CancellationException if cancelled
        compute(i)
    }
}
```

---

## 6. Antipatrón: Kotlin estilo Java
```kotlin
// ❌ WRONG — writing Java in Kotlin
class UserManager {
    private var instance: UserManager? = null

    fun getInstance(): UserManager {
        if (instance == null) {
            instance = UserManager()
        }
        return instance!!
    }
}

// ✅ CORRECT — Kotlin idioms
object UserManager  // singleton built-in

// ✅ CORRECT — use companion object for factory
class User private constructor(val name: String) {
    companion object {
        fun create(name: String) = User(name)
    }
}
```

---

## 7. Exhaustividad de la clase sellada
```kotlin
// ❌ WRONG — not handling all cases
sealed class Result {
    data class Success(val data: String) : Result()
    data class Error(val message: String) : Result()
    object Loading : Result()
}

fun handle(result: Result) {
    when (result) {
        is Result.Success -> println(result.data)
        // forgot Error and Loading — no compiler error!
    }
}

// ✅ CORRECT — exhaustive when (compiler checks)
fun handle(result: Result): String = when (result) {
    is Result.Success -> result.data
    is Result.Error -> result.message
    Result.Loading -> "Loading..."
}
```

---

## 8. Función de extensión de sombreado
```kotlin
// ❌ WRONG — extension function hidden by member
fun String.length(): Int = 42  // never called!
"hello".length()  // returns 5 (member function wins)

// ✅ CORRECT — use unique names or different receiver
fun String.wordCount(): Int = split(" ").size
```

---

## 9. No utilizar`by lazy`para una inicialización costosa
```kotlin
// ❌ WRONG — eager initialization
class Repository {
    val database = connectToDatabase()  // called on construction
}

// ✅ CORRECT — lazy delegate
class Repository {
    val database by lazy { connectToDatabase() }  // deferred until first use
}
```

---

## 10. Confusión entre flujo y LiveData
```kotlin
// ❌ WRONG — collecting Flow without lifecycle awareness
lifecycleScope.launch {
    viewModel.data.collect {  // collects forever, even when paused
        updateUI(it)
    }
}

// ✅ CORRECT — use repeatOnLifecycle
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.data.collect { updateUI(it) }
    }
}
```

---

## Resumen
La concisión de Kotlin puede ocultar problemas sutiles: tipos de plataforma de interoperabilidad de Java, fallas de `lateinit`, clases de datos mutables que rompen colecciones y cancelación de rutinas. La forma de Kotlin es: adoptar la seguridad nula (nunca use `!!`), usar la función de alcance correcta (`let` para transformaciones,`apply`para configuración,`also`para efectos secundarios), usar clases selladas con`when`exhaustivo, manejar la cancelación de rutinas y escribir Kotlin idiomático (no Java con sintaxis de Kotlin). El compilador es su guía; si advierte, escuche.