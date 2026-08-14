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
# Kotlin - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم کاتلین را پوشش می‌دهد.
---

## زنجیره ابزار
| ابزار | هدف |
|------|---------|
| **kotlinc** | کامپایلر کاتلین |
| **Gradle + Kotlin DSL** | سیستم ساخت (توصیه می شود) |
| **ماون** | ساخت جایگزین |
| **kotlinx** | کتابخانه های رسمی کاتلین |
| **کاتلین/بومی** | کامپایل به باینری های بومی |
| **Kotlin/JS** | کامپایل به جاوا اسکریپت |
| **مولتی پلتفرم کاتلین** | کد مشترک در پلتفرم ها |
| **kscript** | اسکریپت نویسی کاتلین |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## ابزارهای ساخت
| ابزار | نوع | بهترین برای |
|------|------|----------|
| **Gradle (Kotlin DSL)** | اولیه | اندروید مولتی ماژول |
| **Gradle (Groovy DSL)** | میراث | پروژه های قدیمی |
| **ماون** | مبتنی بر XML | شرکت |
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

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **Ktor** | کاتلین بومی | سبک، ناهمگام |
| **چکمه بهاره** | جاوا interop | سازمانی، تمام پشته |
| **http4k** | عملکردی | بدون سرور، HTTP |
| **جاوالین** | سبک | برنامه های وب ساده |
| **اسپرینگ وب فلاکس** | واکنشی | همزمانی بالا |
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

## توسعه اندروید
| فناوری | هدف |
|------------|---------|
| **Jetpack Compose** | رابط کاربری مدرن اعلامی |
| **Android SDK** | API های پلتفرم |
| **اتاق** | SQLite ORM |
| **بهسازی** | سرویس گیرنده HTTP |
| **OkHttp** | موتور HTTP |
| **Coroutines + Flow** | برنامه نویسی Async |
| **هلت / کوین** | تزریق وابستگی |
| **کامپوننت ناوبری** | ناوبری صفحه نمایش |
| **WorkManager** | وظایف پس زمینه |
| **DataStore** | جایگزینی ترجیحات |
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

## پایگاه داده و ORM
| فناوری | نوع |
|------------|------|
| **معرض** | کتابخانه Kotlin SQL JetBrains |
| **اتاق** | اندروید SQLite ORM |
| **Hibernate / JPA** | Java ORM (Interop Kotlin) |
| **jOOQ** | سازنده SQL ایمن |
| **SQLDelight** | SQL چند پلتفرمی |
| **قلمرو** | پایگاه داده موبایل |
| **کوتیسا** | SQL ایمن نوع کاتلین |
---

## تست
| چارچوب | هدف |
|-----------|---------|
| **kotlin.test** | ابزارهای تست داخلی |
| **واحد 5** | چارچوب آزمون استاندارد |
| **MockK** | تمسخر بومی کاتلین |
| **موکیتو (کوتلین)** | Java Mockito با پشتیبانی Kotlin |
| **کوتست** | چارچوب تست کاتلین (BDD، ویژگی) |
| **توربین** | تست جریان |
| **تست kotlinx-coroutines** | تست کوروتین |
| **kotlin-faker** | تولید داده های جعلی |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **دتکت** | تجزیه و تحلیل استاتیک کاتلین |
| **ktlint** | لینتر و فرمت کاتلین |
| **کاور** | پوشش کد (JetBrains) |
| **SonarQube** | پلت فرم کیفیت کد |
| **لکه + ktlint** | قالب بندی در Gradle |
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

## سریال سازی
| کتابخانه | هدف |
|---------|---------|
| **kotlinx.serialization** | رسمی، چند پلتفرمی |
| **جکسون (kotlin-module)** | جاوا JSON با پشتیبانی Kotlin |
| **موشی (کوتلین)** | کتابخانه JSON Square |
| **kotlinx.serialization.json** | پشتیبانی JSON |
| **kotlinx.serialization.protobuf** | پشتیبانی Protobuf |
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
| کتابخانه | هدف |
|---------|---------|
| **kotlinx-coroutines-core** | اصول اولیه کوروتین |
| **kotlinx-coroutines-android** | دیسپاچرهای اندروید |
| **جریان** | جریان های واکنشی |
| **کانال** | ارتباط کوروتین |
| **StateFlow / SharedFlow** | مدیریت دولتی |
---

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **kotlinx.coroutines** | Coroutines و async |
| **kotlinx.serialization** | سریال سازی چند پلتفرمی |
| **kotlinx.datetime** | کتابخانه تاریخ/زمان |
| **پیکان** | برنامه نویسی کاربردی |
| **کوین** | سبک وزن DI |
| **هلت** | اندروید DI (خنجر لفاف) |
| **بهسازی** | سرویس گیرنده HTTP |
| **OkHttp** | موتور HTTP |
| **SQLDelight** | SQL چند پلتفرمی |
| **نوشتن چند پلتفرم** | رابط کاربری مشترک بین پلتفرم ها |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **IntelliJ IDEA** | بهترین پشتیبانی Kotlin (ساخته شده توسط JetBrains) |
| **اندروید استودیو** | IDE رسمی اندروید (مبتنی بر IntelliJ) |
| **ناوگان** | ویرایشگر سبک وزن JetBrains |
| **VS Code + Kotlin** | پشتیبانی سبک |
---

## کاتلین چند پلتفرم
| هدف | یادداشت ها |
|--------|-------|
| **اندروید** | پشتیبانی کامل از پلتفرم |
| **iOS** | Via Kotlin/Native |
| **JVM** | دسکتاپ، سرور |
| **JS** | مرورگر، Node.js |
| **بومی** | macOS، Windows، Linux |
| **WebAssembly** | تجربی |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **جار** | `java -jar app.jar`|
| **شیشه چربی** | پلاگین سایه برای uber-jar |
| **تصویر بومی** | GraalVM (پشتیبانی محدود Kotlin) |
| **داکر** | استقرار کانتینری |
| **کاتلین/بومی** | باینری مستقل (بدون JVM) |
| **گوگل پلی** | توزیع اندروید |
---

## خلاصه
اکوسیستم کاتلین شامل JVM، اندروید، چند پلتفرم و توسعه سمت سرور است. پشته استاندارد عبارت است از: **Gradle (Kotlin DSL)** برای ساخت ها، **IntelliJ IDEA** یا **Android Studio** به عنوان IDE، **Ktor** برای سمت سرور (یا **Spring Boot** برای سازمانی)، **Jetpack Compose** برای رابط کاربری اندروید، **kotlinx.coroutines ******Mock برای تست، تست برای asy **detekt** برای linting و **kotlinx.serialization** برای JSON. Kotlin Multiplatform به اشتراک گذاری منطق کسب و کار را در اندروید، iOS و باطن امکان پذیر می کند. نقاط قوت کاتلین عبارتند از: ایمنی پوچ، مختصر بودن، همگام سازی مبتنی بر کوروتین، و تعامل یکپارچه جاوا.