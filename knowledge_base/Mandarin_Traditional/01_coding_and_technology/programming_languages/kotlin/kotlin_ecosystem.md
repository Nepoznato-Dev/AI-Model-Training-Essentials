<!--
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

-->
# Kotlin — 生態系與工具指南
本指南涵蓋了 Kotlin 生態系統中的基本工具、架構和基礎設施。
---

## 工具鏈
|工具|目的|
|------|---------|
| **科特林克** | Kotlin 編譯器 |
| **Gradle + Kotlin DSL** |建置系統（建議）|
| **Maven** |替代建置 |
| **kotlinx** |官方 Kotlin 庫 |
| **Kotlin/Native** |編譯為本機二進位 |
| **Kotlin/JS** |編譯為 JavaScript |
| **Kotlin 多平台** |跨平台共享程式碼 |
| **k腳本** | Kotlin 腳本 |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## 建置工具
|工具|類型 |最適合 |
|------|------|----------|
| **Gradle (Kotlin DSL)** |小學| Android，多模組|
| **Gradle (Groovy DSL)** |遺產|較舊的項目 |
| **Maven** |基於 XML 的 |企業 |
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

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **Ktor** | Kotlin 原生 |輕量級、非同步 |
| **Spring Boot** | Java 互通 |企業級全端|
| **http4k** |功能性|無伺服器、HTTP |
| **爪哇林** |輕量化|簡單的網頁應用程式 |
| **Spring WebFlux** |反應式|高並發|
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

## 安卓開發
|技術 |目的|
|------------|---------|
| **Jetpack Compose** |現代聲明式 UI |
| **Android SDK** |平台 API |
| **房間** | SQLite ORM |
| **改造** | HTTP 用戶端 |
| **OkHttp** | HTTP 引擎 |
| **協程+流程** |非同步程式設計|
| **刀柄/Koin** |依賴注入 |
| **導航組件** |螢幕導航|
| **工作經理** |後台任務|
| **資料儲存** |首選項更換 |
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

## 資料庫和 ORM
|技術 |類型 |
|------------|------|
| **暴露** | JetBrains 的 Kotlin SQL 函式庫 |
| **房間** | Android SQLite ORM |
| **休眠/JPA** | Java ORM（Kotlin 互通）|
| **jOOQ** |類型安全的 SQL 建構器 |
| **SQLDelight** |多平台 SQL |
| **領域** |行動資料庫|
| **科蒂薩** | Kotlin 類型安全 SQL |
---

## 測試
|框架|目的|
|------------|---------|
| **kotlin.測試** |內建測試實用程式 |
| **JUnit 5** |標準測試框架 |
| **模擬K** | Kotlin 原生模擬 |
| **Mockito (kotlin)** |具有 Kotlin 支援的 Java Mockito |
| **科測試** | Kotlin 測試框架（BDD、屬性） |
| **渦輪** |流量測試|
| **kotlinx 協程測試** |協程測試 |
| **kotlin-faker** |虛假資料產生 |
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

## 程式碼品質
|工具|目的|
|------|---------|
| **偵測** | Kotlin 靜態分析 |
| **克特林特** | Kotlin linter 與格式化程式 |
| **科弗** |代碼覆蓋率 (JetBrains) |
| **SonarQube** |程式碼品質平台|
| **一塵不染+ ktlint** |在 Gradle 中格式化 |
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

## 序列化
|圖書館 |目的|
|---------|---------|
| **kotlinx.序列化** |官方，多平台 |
| **Jackson（kotlin 模組）** |具有 Kotlin 支援的 Java JSON |
| **Moshi (kotlin)** | Square 的 JSON 庫 |
| **kotlinx.serialization.json** | JSON 支援 |
| **kotlinx.serialization.protobuf** | Protobuf 支援 |
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

## 協程與非同步
|圖書館 |目的|
|---------|---------|
| **kotlinx 協程核心** |協程原語 |
| **kotlinx-coroutines-android** | Android 調度員 |
| **流量** |反應流 |
| **頻道** |協程通訊 |
| **StateFlow / SharedFlow** |狀態管理|
---

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **kotlinx.coroutines** |協程與非同步 |
| **kotlinx.序列化** |多平台序列化 |
| **kotlinx.datetime** |日期/時間庫 |
| **箭頭** |函數式程式設計 |
| **科因** |輕量級DI |
| **刀柄** | Android DI（Dagger 包裝器）|
| **改造** | HTTP 用戶端 |
| **OkHttp** | HTTP 引擎 |
| **SQLDelight** |多平台 SQL |
| **撰寫多平台** |跨平台共享UI |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **IntelliJ IDEA** |最佳 Kotlin 支援（由 JetBrains 建置）|
| **Android Studio** |官方 Android IDE（基於 IntelliJ）|
| **艦隊** | JetBrains 輕量級編輯器 |
| **VS Code + Kotlin** |輕量級支撐|
---

## Kotlin 多平台
|目標|筆記|
|--------|--------|
| **安卓** |全平台支援|
| **iOS** |透過 Kotlin/Native |
| **JVM** |桌上型電腦、伺服器|
| **JS** |瀏覽器、Node.js |
| **本機** | macOS、Windows、Linux |
| **WebAssembly** |實驗|
---

## 部署
|方法|筆記|
|--------|--------|
| **罐子** |`java -jar app.jar`|
| **胖罐子** | uber-jar 的 Shadow 插件 |
| **原生影像** | GraalVM（有限的 Kotlin 支援）|
| **碼頭工人** |容器化部署|
| **Kotlin/Native** |獨立二進位（無 JVM）|
| **Google遊戲** |安卓發行|
---

＃＃ 概括
Kotlin 的生態系統涵蓋 JVM、Android、多平台和伺服器端開發。標準堆疊是：用於建構的 **Gradle (Kotlin DSL)**、作為 IDE 的 **IntelliJ IDEA** 或 **Android Studio**、用於伺服器端的 **Ktor**（或用於企業的 **Spring Boot**）、用於 Android UI 的 **Jetpack Compose**、用於非同步的 **kotlinx.test的 **kotlinx.serialization**。 Kotlin Multiplatform 支援跨 Android、iOS 和後端共享業務邏輯。 Kotlin 的優點是空安全性、簡潔性、基於協程的非同步和無縫 Java 互通。