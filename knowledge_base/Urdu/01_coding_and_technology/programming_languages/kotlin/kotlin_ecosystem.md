---
# Metadata
title: "Kotlin — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Kotlin ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# کوٹلن — ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ کوٹلن ایکو سسٹم میں ضروری ٹولز، فریم ورک، اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## ٹول چین
| ٹول | مقصد |
|------|---------|
| **کوٹلنک** | کوٹلن کمپائلر |
| **گریڈل + کوٹلن DSL** | سسٹم بنائیں (تجویز کردہ) |
| **ماون** | متبادل تعمیر |
| **kotlinx** | کوٹلن کی سرکاری لائبریریاں |
| **کوٹلن/آبائی** | مقامی بائنریز میں مرتب کریں |
| **کوٹلن/جے ایس** | جاوا اسکرپٹ پر مرتب کریں |
| **کوٹلن ملٹی پلیٹ فارم** | پلیٹ فارمز پر مشترکہ کوڈ |
| **kscript** | کوٹلن اسکرپٹنگ |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## ٹولز بنائیں
| ٹول | قسم | کے لیے بہترین |
|------|------|---------|
| **گریڈل (کوٹلن ڈی ایس ایل)** | پرائمری | اینڈرائیڈ، ملٹی ماڈیول |
| **گریڈل (گرووی ڈی ایس ایل)** | میراث | پرانے منصوبے |
| **ماون** | XML پر مبنی | انٹرپرائز |
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

## ویب فریم ورک
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **Ktor** | کوٹلن مقامی | ہلکا پھلکا، async |
| **اسپرنگ بوٹ** | جاوا انٹراپ | انٹرپرائز، مکمل اسٹیک |
| **http4k** | فنکشنل | سرور لیس، HTTP |
| **جاولین** | ہلکا پھلکا | سادہ ویب ایپس |
| **بہار WebFlux** | رد عمل | اعلی ہم آہنگی |
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

## اینڈرائیڈ ڈویلپمنٹ
| ٹیکنالوجی | مقصد |
|------------|---------|
| **جیٹ پیک کمپوز** | جدید اعلانیہ UI |
| **Android SDK** | پلیٹ فارم APIs |
| **کمرہ** | SQLite ORM |
| **ریٹروفٹ** | HTTP کلائنٹ |
| **OkHttp** | HTTP انجن |
| **کورٹائنز + فلو** | Async پروگرامنگ |
| **ہلٹ/کوئن** | انحصار انجکشن |
| **نیویگیشن جزو** | اسکرین نیویگیشن |
| ** ورک مینیجر** | پس منظر کے کام |
| **ڈیٹا اسٹور** | ترجیحات کا متبادل |
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

## ڈیٹا بیس اور ORM
| ٹیکنالوجی | قسم |
|------------|------|
| **بے ​​نقاب** | جیٹ برینز کی کوٹلن ایس کیو ایل لائبریری |
| **کمرہ** | Android SQLite ORM |
| **ہائبرنیٹ / JPA** | Java ORM (Kotlin interop) |
| **jOOQ** | ٹائپ سیف ایس کیو ایل بلڈر |
| **SQLDelight** | ملٹی پلیٹ فارم SQL |
| **علاقہ** | موبائل ڈیٹا بیس |
| **کوٹیسا** | کوٹلن ٹائپ سیف ایس کیو ایل |
---

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **kotlin.test** | بلٹ ان ٹیسٹ یوٹیلیٹیز |
| **جونائٹ 5** | معیاری ٹیسٹ فریم ورک |
| **مک کے** | کوٹلن کا مقامی مذاق |
| **موکیٹو (کوٹلن)** | جاوا موکیٹو کوٹلن سپورٹ کے ساتھ |
| **کوٹیسٹ** | کوٹلن ٹیسٹنگ فریم ورک (BDD، پراپرٹی) |
| **ٹربائن** | بہاؤ کی جانچ |
| **kotlinx-coroutines-test** | کورٹین ٹیسٹنگ |
| **کوٹلن فیکر** | جعلی ڈیٹا جنریشن |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **ڈیٹیکٹ** | کوٹلن جامد تجزیہ |
| **ktlint** | کوٹلن لنٹر اور فارمیٹر |
| **کوور** | کوڈ کوریج (JetBrains) |
| **سونار کیوب** | کوڈ کوالٹی پلیٹ فارم |
| **بے ​​داغ + کیٹلنٹ** ​​| گریڈل میں فارمیٹنگ |
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

## سیریلائزیشن
| لائبریری | مقصد |
|---------|---------|
| **kotlinx.serialization** | سرکاری، ملٹی پلیٹ فارم |
| **جیکسن (کوٹلن ماڈیول)** | جاوا JSON کوٹلن سپورٹ کے ساتھ |
| **موشی (کوٹلن)** | اسکوائر کی JSON لائبریری |
| **kotlinx.serialization.json** | JSON سپورٹ |
| **kotlinx.serialization.protobuf** | پروٹوبف سپورٹ |
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

## Coroutines & Async
| لائبریری | مقصد |
|---------|---------|
| **kotlinx-coroutines-core** | کوروٹین قدیم |
| **kotlinx-coroutines-android** | اینڈرائیڈ ڈسپیچرز |
| **بہاؤ** | رد عمل کے سلسلے |
| **چینل** | کورٹین مواصلات |
| **StateFlow/SharedFlow** | ریاستی انتظام |
---

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **kotlinx.coroutines** | Coroutines اور async |
| **kotlinx.serialization** | ملٹی پلیٹ فارم سیریلائزیشن |
| **kotlinx.datetime** | تاریخ/وقت لائبریری |
| **تیر** | فنکشنل پروگرامنگ |
| **کوئن** | ہلکا پھلکا DI |
| **ہلٹ** | اینڈرائیڈ ڈی آئی (خنجر ریپر) |
| **ریٹروفٹ** | HTTP کلائنٹ |
| **OkHttp** | HTTP انجن |
| **SQLDelight** | ملٹی پلیٹ فارم SQL |
| **ملٹی پلیٹ فارم تحریر کریں** | پلیٹ فارمز پر مشترکہ UI |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **انٹیلی جے آئیڈیا** | بہترین کوٹلن سپورٹ (جیٹ برینز کے ذریعہ بنایا گیا) |
| **Android اسٹوڈیو** | آفیشل اینڈرائیڈ IDE (انٹیلی جے پر مبنی) |
| **بیڑا** | JetBrains ہلکا پھلکا ایڈیٹر |
| **VS کوڈ + کوٹلن** | ہلکے وزن کی حمایت |
---

## کوٹلن ملٹی پلیٹ فارم
| ہدف | نوٹس |
|---------|-------|
| **Android** | مکمل پلیٹ فارم کی حمایت |
| **iOS** | کوٹلن/آبائی کے ذریعے |
| **JVM** | ڈیسک ٹاپ، سرور |
| **JS** | براؤزر، Node.js |
| **آبائی** | macOS, Windows, Linux |
| **ویب اسمبلی** | تجرباتی |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **جار** | `java -jar app.jar`|
| **موٹی جار** | uber-jar کے لیے شیڈو پلگ ان |
| **مقامی تصویر** | GraalVM (محدود کوٹلن سپورٹ) |
| **ڈوکر** | کنٹینرائزڈ تعیناتی |
| **کوٹلن/آبائی** | اسٹینڈ اسٹون بائنری (کوئی JVM نہیں) |
| **گوگل پلے** | اینڈرائیڈ ڈسٹری بیوشن |
---

## خلاصہ
کوٹلن کا ماحولیاتی نظام JVM، Android، ملٹی پلیٹ فارم، اور سرور سائیڈ ڈیولپمنٹ پر محیط ہے۔ معیاری اسٹیک یہ ہے: **Gradle (Kotlin DSL)** تعمیرات کے لیے، **IntelliJ IDEA** یا **Android اسٹوڈیو** بطور IDE، **Ktor** سرور سائیڈ کے لیے (یا **اسپرنگ بوٹ** انٹرپرائز کے لیے)، **Jetpack Compose** Android UI کے لیے، **kotlinx.coroutines** کے لیے **Kotlinx.coroutines** کے لیے** یا کے لیے** ٹیسٹنگ، linting کے لیے **detekt** اور JSON کے لیے **kotlinx.serialization**۔ کوٹلن ملٹی پلیٹ فارم اینڈرائیڈ، آئی او ایس اور بیک اینڈ پر کاروباری منطق کا اشتراک کرنے کا اہل بناتا ہے۔ کوٹلن کی طاقتیں صفر حفاظت، جامعیت، کورٹین پر مبنی async، اور سیملیس جاوا انٹراپ ہیں۔