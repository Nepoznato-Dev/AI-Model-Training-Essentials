---
# Metadata
title: "Kotlin — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in Kotlin that catch even experienced developers, with explanations and corrections."
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
# Kotlin - Makosa ya Kawaida & Miundo ya Kupambana
Hati hii inaorodhesha makosa ya kawaida, mitego, na mifumo ya kupingana huko Kotlin. Kila ingizo linaonyesha njia isiyo sahihi, inaelezea kwa nini inashindwa, na hutoa suluhisho sahihi.
---

## 1. Aina za Jukwaa na NullPointerException
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

## 2.`lateinit`Matumizi Mabaya
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

## 3.`data class`Bila Sahihi`equals`/ `hashCode`
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

## 4. Kutotumia Kazi za Upeo kwa Usahihi
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

## 5. Coroutines: Sio Kushughulikia Kughairi
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

## 6. Anti-Pattern: Java-Sinema Kotlin
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

## 7. Ukamilifu wa Darasa uliofungwa
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

## 8. Kivuli cha Kazi ya Kiendelezi
```kotlin
// ❌ WRONG — extension function hidden by member
fun String.length(): Int = 42  // never called!
"hello".length()  // returns 5 (member function wins)

// ✅ CORRECT — use unique names or different receiver
fun String.wordCount(): Int = split(" ").size
```

---

## 9. Kutotumia`by lazy`kwa Uanzishaji Ghali
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

## 10. Flow vs LiveData Confusion
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

## Muhtasari
Ufupi wa Kotlin unaweza kuficha masuala fiche: aina za jukwaa kutoka Java interop,`lateinit`kuacha kufanya kazi, mikusanyiko ya data inayoweza kubadilika, kuvunja mikusanyiko na kughairi utaratibu. Njia ya Kotlin ni: kukumbatia usalama tupu (usitumie kamwe`!!`), tumia kitendakazi cha wigo sahihi (`let`kwa mabadiliko,`apply`kwa usanidi,`also`kwa athari mbaya), tumia madarasa yaliyotiwa muhuri na ushughulikiaji kamili wa maandishi ya XQZQZMARKER, 5. Kotlin (sio Java iliyo na syntax ya Kotlin). Mkusanyaji ndiye mwongozo wako - ikiwa inaonya, sikiliza.