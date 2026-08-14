<!--
---
# Metadata
title: "Kotlin — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic Kotlin code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [kotlin, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# کاتلین - الگوهای اصطلاحی و بهترین شیوه ها
این راهنما الگوهای اصطلاحی و بهترین شیوه ها را برای نوشتن کدهای اصطلاحی و تمیز Kotlin پوشش می دهد.
---

## ایمنی پوچ
```kotlin
// ✅ Nullable types
var name: String? = null

// ✅ Safe call
val length = name?.length

// ✅ Elvis operator
val displayName = name ?: "Anonymous"

// ✅ let for nullable
name?.let {
    println("Hello, $it")
}

// ✅ require/check for preconditions
fun process(input: String) {
    require(input.isNotBlank()) { "Input must not be blank" }
    check(state == State.READY) { "Not in ready state" }
}
```

---

## کلاس های داده و مهر و موم شده
```kotlin
// ✅ Data class for data carriers
data class User(val name: String, val email: String, val age: Int)

// ✅ Destructuring
val (name, email, _) = user

// ✅ Sealed classes/interfaces for state
sealed interface Result<out T> {
    data class Success<T>(val data: T) : Result<T>
    data class Error(val exception: Throwable) : Result<Nothing>
    data object Loading : Result<Nothing>
}

// ✅ When with sealed types
fun handle(result: Result<User>) = when (result) {
    is Result.Success -> showUser(result.data)
    is Result.Error -> showError(result.exception)
    is Result.Loading -> showSpinner()
}
```

---

## توابع محدوده
```kotlin
// ✅ let — transform nullable
val length = name?.let { it.length } ?: 0

// ✅ apply — configure object
val intent = Intent().apply {
    action = ACTION_VIEW
    putExtra("id", userId)
}

// ✅ also — side effect
val user = createUser().also { log.info("Created: $it") }

// ✅ with — operate on object
with(config) {
    println("Host: $host")
    println("Port: $port")
}

// ✅ run — compute and return
val hash = input.run {
    // complex computation
    hashCode()
}
```

---

## توابع پسوند
```kotlin
// ✅ Extension functions
fun String.isEmail(): Boolean = contains("@") && contains(".")

fun List<User>.adults(): List<User> = filter { it.age >= 18 }

// ✅ Extension properties
val String.wordCount: Int get() = split("\\s+".toRegex()).size

// ✅ Scope with extensions
fun File.readLines(): List<String> = useLines { it.toList() }
```

---

## مجموعه و لامبدا
```kotlin
// ✅ Collection operations
val names = users
    .filter { it.isActive }
    .map { it.name }
    .sorted()

val grouped = users.groupBy { it.role }
val total = users.sumOf { it.salary }
val found = users.find { it.id == targetId }
val exists = users.any { it.isAdmin }
val allActive = users.all { it.isActive }

// ✅ Lambda shorthand
val doubled = numbers.map { it * 2 }

// ✅ Labeled returns
list.forEach outer@{ item ->
    if (item < 0) return@outer
    process(item)
}
```

---

## روتین ها
```kotlin
// ✅ suspend functions
suspend fun fetchUser(id: Long): User = withContext(Dispatchers.IO) {
    api.getUser(id)
}

// ✅ CoroutineScope
viewModelScope.launch {
    val users = repository.getUsers()
    _state.value = UiState.Success(users)
}

// ✅ Flow
fun observeUsers(): Flow<List<User>> = flow {
    while (true) {
        emit(repository.getAll())
        delay(5_000)
    }
}

// ✅ Collect with lifecycle
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.state.collect { state ->
            updateUI(state)
        }
    }
}
```

---

## کاتلین اصطلاحی
```kotlin
// ✅ val by default, var only when needed
val name = "Alice"
var count = 0

// ✅ Expression body
fun area(width: Int, height: Int) = width * height

// ✅ String templates
val message = "Hello, $name! You have ${items.size} items."

// ✅ when expression
val description = when (x) {
    0 -> "zero"
    in 1..9 -> "single digit"
    in 10..99 -> "double digit"
    else -> "large"
}

// ✅ Companion object for factory methods
class User private constructor(val name: String) {
    companion object {
        fun create(name: String) = User(name)
    }
}

// ✅ Destructuring in lambdas
map.forEach { (key, value) -> println("$key = $value") }
```

---

## خلاصه
اصطلاحات کاتلین تاکید دارند: ایمنی پوچ، کلاس‌های داده، انواع مهر و موم شده، توابع دامنه، توابع گسترش، روتین‌ها و کد بیان‌گرا. از قوانین کد نویسی Kotlin پیروی کنید، از ktlint برای قالب بندی و از detekt برای تجزیه و تحلیل استاتیک استفاده کنید. کاتلین برای مختصر و رسا بودن ارزش قائل است - کمتر بنویسید، از کتابخانه استاندارد استفاده کنید و به طور پیش فرض از`val`استفاده کنید.