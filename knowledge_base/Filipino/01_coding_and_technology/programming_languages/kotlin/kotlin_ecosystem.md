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
# Kotlin — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, framework, at imprastraktura sa Kotlin ecosystem.
---

## Toolchain
| Tool | Layunin |
|------|---------|
| **kotlinc** | Kotlin compiler |
| **Gradle + Kotlin DSL** | Bumuo ng system (inirerekomenda) |
| **Maven** | Alternatibong build |
| **kotlinx** | Opisyal na mga aklatan ng Kotlin |
| **Kotlin/Native** | Mag-compile sa mga katutubong binary |
| **Kotlin/JS** | Mag-compile sa JavaScript |
| **Kotlin Multiplatform** | Nakabahaging code sa mga platform |
| **kscript** | Kotlin scripting |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## Bumuo ng Mga Tool
| Tool | Uri | Pinakamahusay Para sa |
|------|------|----------|
| **Gradle (Kotlin DSL)** | Pangunahin | Android, multi-module |
| **Gradle (Groovy DSL)** | Legacy | Mga lumang proyekto |
| **Maven** | Nakabatay sa XML | Enterprise |
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

## Mga Web Framework
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **Ktor** | Kotlin-native | Magaan, async |
| **Spring Boot** | Java interop | Enterprise, full-stack |
| **http4k** | Nagagamit | Walang server, HTTP |
| **Javalin** | Magaan | Mga simpleng web app |
| **Spring WebFlux** | Reaktibo | High-concurrency |
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

## Pag-unlad ng Android
| Teknolohiya | Layunin |
|------------|---------|
| **Jetpack Compose** | Modernong deklaratibong UI |
| **Android SDK** | Mga Platform API |
| **Kwarto** | SQLite ORM |
| **Retrofit** | HTTP client |
| **OkHttp** | HTTP engine |
| **Mga Coroutine + Daloy** | Async programming |
| **Hilt / Koin** | Dependency injection |
| **Navigation Component** | Screen navigation |
| **WorkManager** | Mga gawain sa background |
| **DataStore** | Pagpapalit ng mga kagustuhan |
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

## Database at ORM
| Teknolohiya | Uri |
|------------|------|
| **Nakalantad** | Kotlin SQL library ng JetBrains |
| **Kwarto** | Android SQLite ORM |
| **Hibernate / JPA** | Java ORM (Kotlin interop) |
| **jOOQ** | Uri-ligtas na tagabuo ng SQL |
| **SQLDelight** | Multiplatform SQL |
| **Realm** | Mobile database |
| **kotysa** | Kotlin type-safe SQL |
---

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **kotlin.test** | Mga built-in na kagamitan sa pagsubok |
| **JUnit 5** | Standard na balangkas ng pagsubok |
| **MockK** | Kotlin-native na panunuya |
| **Mockito (kotlin)** | Java Mockito na may suporta sa Kotlin |
| **Kotest** | Kotlin testing framework (BDD, property) |
| **Turbine** | Pagsubok sa daloy |
| **kotlinx-coroutines-test** | Pagsusuri sa coroutine |
| **kotlin-faker** | Pagbuo ng pekeng data |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **detekt** | Kotlin static na pagsusuri |
| **ktlint** | Kotlin linter at formatter |
| **Kover** | Saklaw ng code (JetBrains) |
| **SonarQube** | Platform ng kalidad ng code |
| **Spotless + ktlint** | Pag-format sa Gradle |
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

## Serialization
| Aklatan | Layunin |
|---------|---------|
| **kotlinx.serialization** | Opisyal, multiplatform |
| **Jackson (kotlin-module)** | Java JSON na may suporta sa Kotlin |
| **Moshi (kotlin)** | JSON library ng Square |
| **kotlinx.serialization.json** | Suporta sa JSON |
| **kotlinx.serialization.protobuf** | Suporta sa Protobuf |
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

## Mga Coroutine at Async
| Aklatan | Layunin |
|---------|---------|
| **kotlinx-coroutines-core** | Coroutine primitives |
| **kotlinx-coroutines-android** | Mga dispatser ng Android |
| **Daloy** | Mga reaktibong stream |
| **Channel** | Coroutine na komunikasyon |
| **StateFlow / SharedFlow** | Pamamahala ng estado |
---

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **kotlinx.coroutines** | Mga Coroutine at async |
| **kotlinx.serialization** | Multiplatform serialization |
| **kotlinx.datetime** | aklatan ng petsa/oras |
| **Arrow** | Functional na programming |
| **Koin** | Magaang DI |
| **Hilt** | Android DI (Dagger wrapper) |
| **Retrofit** | HTTP client |
| **OkHttp** | HTTP engine |
| **SQLDelight** | Multiplatform SQL |
| **Bumuo ng Multiplatform** | Nakabahaging UI sa mga platform |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **IntelliJ IDEA** | Pinakamahusay na suporta sa Kotlin (na binuo ng JetBrains) |
| **Android Studio** | Opisyal na Android IDE (IntelliJ-based) |
| **Fleet** | JetBrains lightweight editor |
| **VS Code + Kotlin** | Magaan na suporta |
---

## Kotlin Multiplatform
| Target | Mga Tala |
|--------|-------|
| **Android** | Buong suporta sa platform |
| **iOS** | Sa pamamagitan ng Kotlin/Native |
| **JVM** | Desktop, server |
| **JS** | Browser, Node.js |
| **Katutubo** | macOS, Windows, Linux |
| **WebAssembly** | Eksperimental |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **JAR** | `java -jar app.jar`|
| **Fat JAR** | Shadow plugin para sa uber-jar |
| **Katutubong larawan** | GraalVM (limitadong suporta sa Kotlin) |
| **Docker** | Containerized deployment |
| **Kotlin/Native** | Standalone na binary (walang JVM) |
| **Google Play** | Pamamahagi ng Android |
---

## Buod
Ang ecosystem ng Kotlin ay sumasaklaw sa JVM, Android, multiplatform, at server-side development. Ang karaniwang stack ay: **Gradle (Kotlin DSL)** para sa mga build, **IntelliJ IDEA** o **Android Studio** bilang IDE, **Ktor** para sa server-side (o **Spring Boot** para sa enterprise), **Jetpack Compose** para sa Android UI, **kotlinx.coroutines** para sa async, **MockK** o **Kotesttrialization para sa****, **lint. JSON. Ang Kotlin Multiplatform ay nagbibigay-daan sa pagbabahagi ng lohika ng negosyo sa Android, iOS, at backend. Ang mga kalakasan ni Kotlin ay null na kaligtasan, pagiging maikli, coroutine-based na async, at tuluy-tuloy na Java interop.