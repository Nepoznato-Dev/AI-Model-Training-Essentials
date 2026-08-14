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
# कोटलिन - मुहावरेदार पैटर्न और सर्वोत्तम प्रथाएँ
यह मार्गदर्शिका स्वच्छ, मुहावरेदार कोटलिन कोड लिखने के लिए मुहावरेदार पैटर्न और सर्वोत्तम प्रथाओं को शामिल करती है।
---

## अशक्त सुरक्षा
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

## डेटा क्लासेस और सीलबंद
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

## कार्यक्षेत्र कार्य
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

## विस्तार कार्य
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

## संग्रह और लैम्ब्डा
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

## कोरटाइन्स
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

## मुहावरेदार कोटलिन
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

## सारांश
कोटलिन मुहावरे जोर देते हैं: अशक्त सुरक्षा, डेटा वर्ग, सीलबंद प्रकार, स्कोप फ़ंक्शंस, एक्सटेंशन फ़ंक्शंस, कोरआउट्स और अभिव्यक्ति-उन्मुख कोड। कोटलिन कोडिंग कन्वेंशन का पालन करें, फ़ॉर्मेटिंग के लिए ktlint का उपयोग करें, और स्थैतिक विश्लेषण के लिए डिटेक्ट का उपयोग करें। कोटलिन संक्षिप्तता और अभिव्यक्ति को महत्व देता है - कम बॉयलरप्लेट लिखें, मानक लाइब्रेरी को अपनाएं, और डिफ़ॉल्ट रूप से`val`का उपयोग करें।