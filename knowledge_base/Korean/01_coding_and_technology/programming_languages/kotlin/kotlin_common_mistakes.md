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

# Kotlin — 일반적인 실수 및 안티 패턴
이 문서에는 Kotlin에서 가장 흔히 발생하는 실수, 함정, 안티패턴이 나열되어 있습니다. 각 항목은 잘못된 접근 방식을 보여주고, 실패 이유를 설명하며, 올바른 솔루션을 제공합니다.
---

## 1. 플랫폼 유형 및 NullPointerException
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

## 2.`lateinit`오용
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

## 3. 적절한`equals`/ `hashCode`가 없는 `data class`
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

## 4. 범위 기능을 올바르게 사용하지 않음
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

## 5. 코루틴: 취소를 처리하지 않음
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

## 6. 안티 패턴: Java 스타일 Kotlin
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

## 7. 봉인된 클래스의 완전성
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

## 8. 확장 기능 섀도잉
```kotlin
// ❌ WRONG — extension function hidden by member
fun String.length(): Int = 42  // never called!
"hello".length()  // returns 5 (member function wins)

// ✅ CORRECT — use unique names or different receiver
fun String.wordCount(): Int = split(" ").size
```

---

## 9. 값비싼 초기화를 위해 `by lazy`를 사용하지 않음
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

## 10. 흐름과 LiveData의 혼동
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

## 요약
Kotlin의 간결함은 Java 상호 운용성의 플랫폼 유형,`lateinit`충돌, 컬렉션을 중단하는 변경 가능한 데이터 클래스, 코루틴 취소 등 미묘한 문제를 숨길 수 있습니다. Kotlin 방식은 null 안전을 수용하고(`!!`를 절대 사용하지 않음) 올바른 범위 함수를 사용하고(변환을 위해 `let`, 구성을 위해 `apply`, 부작용을 위해 `also`), 철저한 `when`가 있는 봉인된 클래스를 사용하고, 코루틴 취소를 처리하고, 관용적인 Kotlin을 작성합니다(Kotlin 구문을 사용하는 Java가 아님). 컴파일러는 여러분의 가이드입니다. 경고가 나오면 들어보세요.