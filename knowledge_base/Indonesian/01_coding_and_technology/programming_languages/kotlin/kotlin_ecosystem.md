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

# Kotlin — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Kotlin.
---

## Rantai Alat
| Alat | Tujuan |
|------|---------|
| **kotlinc** | Kompiler Kotlin |
| **Gradle + Kotlin DSL** | Bangun sistem (disarankan) |
| **Maven** | Pembangunan alternatif |
| **kotlinx** | Library resmi Kotlin |
| **Kotlin/Asli** | Kompilasi ke biner asli |
| **Kotlin/JS** | Kompilasi ke JavaScript |
| **Multiplatform Kotlin** | Kode bersama di seluruh platform |
| **skrip** | Skrip Kotlin |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## Alat Bangun
| Alat | Ketik | Terbaik Untuk |
|------|------|----------|
| **Gradle (Kotlin DSL)** | Utama | Android, multi-modul |
| **Gradle (DSL Asyik)** | Warisan | Proyek lama |
| **Maven** | Berbasis XML | Perusahaan |
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

## Kerangka Web
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Ktor** | Kotlin-asli | Ringan, asinkron |
| **Sepatu Musim Semi** | Interop Java | Perusahaan, tumpukan penuh |
| **http4k** | Fungsional | Tanpa server, HTTP |
| **Javalin** | Ringan | Aplikasi web sederhana |
| **WebFlux Musim Semi** | Reaktif | Konkurensi tinggi |
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

## Pengembangan Android
| Teknologi | Tujuan |
|------------|---------|
| **Penulisan Jetpack** | UI deklaratif modern |
| **SDK Android** | API Platform |
| **Kamar** | SQLite ORM |
| **Retrofit** | Klien HTTP |
| **OkeHttp** | Mesin HTTP |
| **Coroutine + Aliran** | Pemrograman asinkron |
| **Gagang / Koin** | Injeksi ketergantungan |
| **Komponen Navigasi** | Navigasi layar |
| **Manajer Kerja** | Tugas latar belakang |
| **Penyimpanan Data** | Penggantian preferensi |
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

## Basis Data & ORM
| Teknologi | Ketik |
|------------|------|
| **Terkena** | Pustaka SQL Kotlin JetBrains |
| **Kamar** | Android SQLite ORM |
| **Hibernasi / JPA** | ORM Java (interop Kotlin) |
| **jOOQ** | Pembuat SQL yang aman untuk tipe |
| **SQLDelight** | SQL multiplatform |
| **Alam** | Basis data seluler |
| **kotysa** | SQL aman untuk tipe Kotlin |
---

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **kotlin.test** | Utilitas pengujian bawaan |
| **5 JUNI** | Kerangka uji standar |
| **MockK** | Ejekan asli Kotlin |
| **Mockito (kotlin)** | Java Mockito dengan dukungan Kotlin |
| **Kotes** | Kerangka pengujian Kotlin (BDD, properti) |
| **Turbin** | Pengujian aliran |
| **uji-kotlinx-coroutine** | Pengujian coroutine |
| **pemalsu kotlin** | Pembuatan data palsu |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **deteksi** | Analisis statis Kotlin |
| **ktlint** | Linter dan pemformat Kotlin |
| **Kover** | Cakupan kode (JetBrains) |
| **SonarQube** | Platform kualitas kode |
| **Tanpa Noda + ktlint** | Memformat dalam Gradle |
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

## Serialisasi
| Perpustakaan | Tujuan |
|---------|---------|
| **kotlinx.serialisasi** | Resmi, multiplatform |
| **Jackson (kotlin-modul)** | Java JSON dengan dukungan Kotlin |
| **Moshi (kotlin)** | Perpustakaan JSON Square |
| **kotlinx.serialisasi.json** | dukungan JSON |
| **kotlinx.serialisasi.protobuf** | Dukungan Protobuf |
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

## Coroutine & Asinkron
| Perpustakaan | Tujuan |
|---------|---------|
| **kotlinx-coroutine-core** | Primitif coroutine |
| **kotlinx-coroutine-android** | Operator Android |
| **Aliran** | Aliran reaktif |
| **Saluran** | Komunikasi coroutine |
| **StateFlow / SharedFlow** | Pengelolaan negara |
---

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **kotlinx.coroutine** | Coroutine dan async |
| **kotlinx.serialisasi** | Serialisasi multiplatform |
| **kotlinx.datetime** | Perpustakaan tanggal/waktu |
| **Panah** | Pemrograman fungsional |
| **Koin** | DI Ringan |
| **Gagang** | Android DI (Pembungkus belati) |
| **Retrofit** | Klien HTTP |
| **OkeHttp** | Mesin HTTP |
| **SQLDelight** | SQL multiplatform |
| **Tulis Multiplatform** | UI Bersama di seluruh platform |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **IDE IntelliJ** | Dukungan Kotlin terbaik (dibuat oleh JetBrains) |
| **Android Studio** | IDE Android Resmi (berbasis IntelliJ) |
| **Armada** | Editor ringan JetBrains |
| **Kode VS + Kotlin** | Dukungan ringan |
---

## Multiplatform Kotlin
| Sasaran | Catatan |
|--------|-------|
| **Android** | Dukungan platform penuh |
| **iOS** | Melalui Kotlin/Asli |
| **JVM** | Desktop, server |
| **JS** | Peramban, Node.js |
| **Asli** | macOS, Windows, Linux |
| **Perakitan Web** | Eksperimental |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **JAR** | `java -jar app.jar`|
| **JAR Gemuk** | Plugin bayangan untuk uber-jar |
| **Gambar asli** | GraalVM (dukungan Kotlin terbatas) |
| **Buruh pelabuhan** | Penerapan dalam container |
| **Kotlin/Asli** | Biner mandiri (tanpa JVM) |
| **Google Play** | Distribusi Android |
---

## Ringkasan
Ekosistem Kotlin mencakup JVM, Android, multiplatform, dan pengembangan sisi server. Tumpukan standarnya adalah: **Gradle (Kotlin DSL)** untuk build, **IntelliJ IDEA** atau **Android Studio** sebagai IDE, **Ktor** untuk sisi server (atau **Spring Boot** untuk perusahaan), **Jetpack Compose** untuk UI Android, **kotlinx.coroutines** untuk async, **MockK** atau **Kotest** untuk pengujian, **detekt** untuk linting, dan **kotlinx.serialization** untuk JSON. Multiplatform Kotlin memungkinkan berbagi logika bisnis di Android, iOS, dan backend. Kekuatan Kotlin adalah keamanan nol, keringkasan, asinkron berbasis coroutine, dan interop Java yang lancar.