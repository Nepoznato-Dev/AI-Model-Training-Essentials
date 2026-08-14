---
# Metadata
title: "Kotlin — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Kotlin ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [kotlin, ecosystem, tooling, android, jvm, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "16 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# কোটলিন — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি কোটলিন ইকোসিস্টেমের প্রয়োজনীয় টুলস, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## টুলচেইন
| টুল | উদ্দেশ্য |
|------|---------|
| **কোটলিঙ্ক** | কোটলিন কম্পাইলার |
| **Gradle + Kotlin DSL** | সিস্টেম তৈরি করুন (প্রস্তাবিত) |
| **মাভেন** | বিকল্প নির্মাণ |
| **কোটলিনক্স** | অফিসিয়াল কোটলিন লাইব্রেরি |
| **কোটলিন/নেটিভ** | নেটিভ বাইনারিতে কম্পাইল করুন |
| **কোটলিন/জেএস** | জাভাস্ক্রিপ্টে কম্পাইল |
| **কোটলিন মাল্টিপ্ল্যাটফর্ম** | প্ল্যাটফর্ম জুড়ে শেয়ার করা কোড |
| **kscript** | কোটলিন স্ক্রিপ্টিং |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## বিল্ড টুলস
| টুল | প্রকার | জন্য সেরা |
|------|------|----------|
| **Gradle (Kotlin DSL)** | প্রাথমিক | অ্যান্ড্রয়েড, মাল্টি-মডিউল |
| **Gradle (Groovy DSL)** | উত্তরাধিকার | পুরানো প্রকল্প |
| **মাভেন** | XML-ভিত্তিক | এন্টারপ্রাইজ |
```kotlin
// build.gradle.kts
plugins {
    kotlin("jvm") version "2.0.0"
    application
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("io.ktor:ktor-server-core:2.3.0")
    implementation("io.ktor:ktor-server-netty:2.3.0")
    implementation("org.jetbrains.exposed:exposed-core:0.50.0")
    testImplementation(kotlin("test"))
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.0")
}

application {
    mainClass.set("com.example.MainKt")
}
```

---

## ওয়েব ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **Ktor** | কোটলিন-নেটিভ | লাইটওয়েট, অ্যাসিঙ্ক |
| **স্প্রিং বুট** | জাভা ইন্টারপ | এন্টারপ্রাইজ, ফুল-স্ট্যাক |
| **http4k** | কার্যকরী | সার্ভারহীন, HTTP |
| **জাভালিন** | লাইটওয়েট | সহজ ওয়েব অ্যাপস |
| **বসন্ত ওয়েবফ্লাক্স** | প্রতিক্রিয়াশীল | উচ্চ-সঙ্গতি |
```kotlin
// Ktor example
fun main() {
    embeddedServer(Netty, port = 8080) {
        routing {
            get("/hello") {
                call.respondText("Hello, World!")
            }
            get("/users/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                    ?: return@get call.respond(HttpStatusCode.BadRequest)
                val user = userService.findById(id)
                call.respond(user ?: HttpStatusCode.NotFound)
            }
        }
    }.start(wait = true)
}
```

---

## অ্যান্ড্রয়েড ডেভেলপমেন্ট
| প্রযুক্তি | উদ্দেশ্য |
|------------|---------|
| **জেটপ্যাক রচনা** | আধুনিক ঘোষণামূলক UI |
| **Android SDK** | প্ল্যাটফর্ম APIs |
| **রুম** | SQLite ORM |
| **রেট্রোফিট** | HTTP ক্লায়েন্ট |
| **OkHttp** | HTTP ইঞ্জিন |
| **করোটিন + প্রবাহ** | অ্যাসিঙ্ক প্রোগ্রামিং |
| **হিল্ট/কোইন** | নির্ভরতা ইনজেকশন |
| **নেভিগেশন উপাদান** | স্ক্রীন নেভিগেশন |
| **ওয়ার্ক ম্যানেজার** | পটভূমির কাজ |
| **ডেটাস্টোর** | পছন্দ প্রতিস্থাপন |
```kotlin
// Jetpack Compose example
@Composable
fun UserCard(user: User) {
    Card(modifier = Modifier.padding(8.dp)) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text(text = user.name, style = MaterialTheme.typography.headlineSmall)
            Text(text = user.email, style = MaterialTheme.typography.bodyMedium)
        }
    }
}
```

---

## ডাটাবেস এবং ওআরএম
| প্রযুক্তি | প্রকার |
|------------|------|
| **উন্মুক্ত** | JetBrains' Kotlin SQL লাইব্রেরি |
| **রুম** | অ্যান্ড্রয়েড SQLite ORM |
| **হাইবারনেট / JPA** | জাভা ওআরএম (কোটলিন ইন্টারপ) |
| **jOOQ** | টাইপ-নিরাপদ SQL নির্মাতা |
| **এসকিউএলডিলাইট** | মাল্টিপ্ল্যাটফর্ম এসকিউএল |
| **রাজত্ব** | মোবাইল ডাটাবেস |
| **কোটিসা** | কোটলিন টাইপ-নিরাপদ SQL |
---

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **kotlin.test** | অন্তর্নির্মিত পরীক্ষা ইউটিলিটি |
| **জুনিট ৫** | স্ট্যান্ডার্ড টেস্ট ফ্রেমওয়ার্ক |
| **মককে** | কোটলিন-নেটিভ ঠাট্টা |
| **মকিটো (কোটলিন)** | কোটলিন সমর্থন সহ জাভা মকিটো |
| **কোটেস্ট** | কোটলিন টেস্টিং ফ্রেমওয়ার্ক (বিডিডি, সম্পত্তি) |
| **টারবাইন** | প্রবাহ পরীক্ষা |
| **কোটলিনক্স-করোটিনস-টেস্ট** | করুটিন টেস্টিং |
| **কোটলিন-ফেকার** | জাল ডেটা জেনারেশন |
```kotlin
// Kotest example
class UserServiceTest : StringSpec({
    "should find user by id" {
        val repo = mockk<UserRepository>()
        coEvery { repo.findById(1) } returns User("Alice")
        val service = UserService(repo)

        val user = service.findById(1)

        user.name shouldBe "Alice"
    }

    "should throw when user not found" {
        val repo = mockk<UserRepository>()
        coEvery { repo.findById(any()) } throws NotFoundException()
        val service = UserService(repo)

        shouldThrow<NotFoundException> {
            service.findById(999)
        }
    }
})
```

---

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **ডিটেক্ট** | কোটলিন স্ট্যাটিক বিশ্লেষণ |
| **ktlint** | কোটলিন লিন্টার এবং ফরম্যাটার |
| **কোভার** | কোড কভারেজ (JetBrains) |
| **সোনারকিউব** | কোড মানের প্ল্যাটফর্ম |
| **দাগহীন + ktlint** | Gradle এ ফরম্যাটিং |
```kotlin
// detekt configuration (detekt.yml)
build:
  maxIssues: 0

complexity:
  LongMethod:
    threshold: 60
  TooManyFunctions:
    thresholdInClasses: 15

style:
  MaxLineLength:
    maxLineLength: 120
```

---

## সিরিয়ালাইজেশন
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **kotlinx.serialization** | অফিসিয়াল, মাল্টিপ্ল্যাটফর্ম |
| **জ্যাকসন (কটলিন-মডিউল)** | Kotlin সমর্থন সহ Java JSON |
| **মোশি (কোটলিন)** | স্কোয়ারের JSON লাইব্রেরি |
| **kotlinx.serialization.json** | JSON সমর্থন |
| **kotlinx.serialization.protobuf** | প্রোটোবাফ সমর্থন |
```kotlin
@Serializable
data class User(
    val id: Long,
    val name: String,
    val email: String,
    val role: Role = Role.USER
)

enum class Role { USER, ADMIN }

// Usage
val json = Json.encodeToString(user)
val user = Json.decodeFromString<User>(jsonString)
```

---

## করুটিন এবং অ্যাসিঙ্ক
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **kotlinx-coroutines-core** | করুটিন আদিম |
| **kotlinx-coroutines-android** | অ্যান্ড্রয়েড প্রেরক |
| **প্রবাহ** | প্রতিক্রিয়াশীল প্রবাহ |
| **চ্যানেল** | নিয়মিত যোগাযোগ |
| **স্টেটফ্লো / শেয়ার্ডফ্লো** | রাষ্ট্র পরিচালনা |
---

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **kotlinx.coroutines** | Coroutines এবং async |
| **kotlinx.serialization** | মাল্টিপ্ল্যাটফর্ম সিরিয়ালাইজেশন |
| **kotlinx.datetime** | তারিখ/সময় লাইব্রেরি |
| **তীর** | কার্যকরী প্রোগ্রামিং |
| **কোইন** | লাইটওয়েট DI |
| **হিল্ট** | অ্যান্ড্রয়েড ডিআই (ড্যাগার র্যাপার) |
| **রেট্রোফিট** | HTTP ক্লায়েন্ট |
| **OkHttp** | HTTP ইঞ্জিন |
| **এসকিউএলডিলাইট** | মাল্টিপ্ল্যাটফর্ম এসকিউএল |
| **মাল্টিপ্ল্যাটফর্ম রচনা করুন** | প্ল্যাটফর্ম জুড়ে শেয়ার করা UI |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **ইন্টেলিজ আইডিয়া** | সেরা Kotlin সমর্থন (JetBrains দ্বারা নির্মিত) |
| **অ্যান্ড্রয়েড স্টুডিও** | অফিসিয়াল অ্যান্ড্রয়েড IDE (IntelliJ-ভিত্তিক) |
| **বহর** | JetBrains লাইটওয়েট সম্পাদক |
| **ভিএস কোড + কোটলিন** | লাইটওয়েট সমর্থন |
---

## কোটলিন মাল্টিপ্ল্যাটফর্ম
| লক্ষ্য | নোট |
|---------|-------|
| **Android** | সম্পূর্ণ প্ল্যাটফর্ম সমর্থন |
| **iOS** | কোটলিন/নেটিভের মাধ্যমে |
| **JVM** | ডেস্কটপ, সার্ভার |
| **জেএস** | ব্রাউজার, Node.js |
| **নেটিভ** | macOS, Windows, Linux |
| **ওয়েব অ্যাসেম্বলি** | পরীক্ষামূলক |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **জার** | `java -jar app.jar`|
| **ফ্যাট জার** | উবার-জারের জন্য ছায়া প্লাগইন |
| **নেটিভ ইমেজ** | GraalVM (সীমিত কোটলিন সমর্থন) |
| **ডকার** | কন্টেইনারাইজড স্থাপনা |
| **কোটলিন/নেটিভ** | স্বতন্ত্র বাইনারি (কোন JVM) |
| **গুগল প্লে** | অ্যান্ড্রয়েড বিতরণ |
---

## সারাংশ
কোটলিনের ইকোসিস্টেম JVM, Android, মাল্টিপ্ল্যাটফর্ম, এবং সার্ভার-সাইড ডেভেলপমেন্টে বিস্তৃত। স্ট্যান্ডার্ড স্ট্যাক হল: **বিল্ডের জন্য **Gradle (Kotlin DSL)**, **IntelliJ IDEA** বা **Android Studio** IDE হিসেবে, **Ktor** সার্ভার-সাইডের জন্য (অথবা **স্প্রিং বুট** এন্টারপ্রাইজের জন্য), **জেটপ্যাক কম্পোজ** Android UI এর জন্য, **kotlinx.coroutines** এর জন্য **Kotlinx.coroutines**, **Kotlinx পরীক্ষা, লিনটিং এর জন্য **detekt** এবং JSON এর জন্য **kotlinx.serialization**। কোটলিন মাল্টিপ্ল্যাটফর্ম অ্যান্ড্রয়েড, আইওএস এবং ব্যাকএন্ড জুড়ে ব্যবসার যুক্তি ভাগ করে নেওয়া সক্ষম করে। কোটলিনের শক্তিগুলি হল শূন্য নিরাপত্তা, সংক্ষিপ্ততা, কোরোটিন-ভিত্তিক অ্যাসিঙ্ক এবং বিজোড় জাভা ইন্টারপ।