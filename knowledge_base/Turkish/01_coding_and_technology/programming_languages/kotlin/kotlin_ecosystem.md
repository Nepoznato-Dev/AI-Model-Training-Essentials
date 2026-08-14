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

# Kotlin — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz Kotlin ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Alet Zinciri
| Araç | Amaç |
|------|------------|
| **kotlinc** | Kotlin derleyicisi |
| **Gradle + Kotlin DSL** | Derleme sistemi (önerilen) |
| **Maven** | Alternatif yapı |
| **kotlinx** | Resmi Kotlin kütüphaneleri |
| **Kotlin/Yerli** | Yerel ikili dosyalara derleme |
| **Kotlin/JS** | JavaScript'e Derle |
| **Kotlin Çoklu Platform** | Platformlar arasında paylaşılan kod |
| **kscript** | Kotlin komut dosyası oluşturma |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## Oluşturma Araçları
| Araç | Tür | En İyisi |
|------|----------|----------|
| **Gradle (Kotlin DSL)** | Birincil | Android, çoklu modül |
| **Gradle (Groovy DSL)** | Eski | Daha eski projeler |
| **Maven** | XML tabanlı | Kurumsal |
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

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **Ktor** | Kotlin'in yerlisi | Hafif, asenkron |
| **Bahar Çizme** | Java birlikte çalışma | Kurumsal, tam yığın |
| **http4k** | Fonksiyonel | Sunucusuz, HTTP |
| **Javalin** | Hafif | Basit web uygulamaları |
| **Bahar WebFlux** | Reaktif | Yüksek eşzamanlılık |
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

## Android Geliştirme
| Teknoloji | Amaç |
|---------------|-----------|
| **Jetpack Oluşturma** | Modern bildirimsel kullanıcı arayüzü |
| **Android SDK'sı** | Platform API'leri |
| **Oda** | SQLite ORM |
| **Yenileme** | HTTP istemcisi |
| **TamamHttp** | HTTP motoru |
| **Eşrutinler + Akış** | Asenkron programlama |
| **Kabza / Para** | Bağımlılık enjeksiyonu |
| **Gezinme Bileşeni** | Ekranda gezinme |
| **İş Yöneticisi** | Arka plan görevleri |
| **Veri Deposu** | Tercihlerin değiştirilmesi |
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

## Veritabanı ve ORM
| Teknoloji | Tür |
|---------------|------|
| **Açığa çıkan** | JetBrains'in Kotlin SQL kütüphanesi |
| **Oda** | Android SQLite ORM |
| **Hazırda Beklet / JPA** | Java ORM (Kotlin birlikte çalışma) |
| **jOOQ** | Tip güvenli SQL oluşturucu |
| **SQLDelight** | Çoklu Platform SQL |
| **Bölge** | Mobil veritabanı |
| **kotysa** | Kotlin türü açısından güvenli SQL |
---

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **kotlin.test** | Yerleşik test yardımcı programları |
| **JÜnite 5** | Standart test çerçevesi |
| **SahteK** | Kotlin yerlisi alaycı |
| **Mockito (kotlin)** | Kotlin destekli Java Mockito |
| **Kotest** | Kotlin test çerçevesi (BDD, özellik) |
| **Türbin** | Akış testi |
| **kotlinx-coroutines-testi** | Koroutin testi |
| **kotlin-faker** | Sahte veri üretimi |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **algılama** | Kotlin statik analizi |
| **ktlint** | Kotlin linter ve formatlayıcı |
| **Kover** | Kod kapsamı (JetBrains) |
| **SonarQube** | Kod kalitesi platformu |
| **Lekesiz + tüysüz** | Gradle'da Biçimlendirme |
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

## Serileştirme
| Kütüphane | Amaç |
|-----------|-----------|
| **kotlinx.serileştirme** | Resmi, çoklu platform |
| **Jackson (kotlin modülü)** | Kotlin destekli Java JSON |
| **Moshi (kotlin)** | Square'in JSON kütüphanesi |
| **kotlinx.serialization.json** | JSON desteği |
| **kotlinx.serialization.protobuf** | Protobuf desteği |
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

## Eşyordamlar ve Eşzamansız
| Kütüphane | Amaç |
|-----------|-----------|
| **kotlinx-coroutines-core** | Koroutin ilkelleri |
| **kotlinx-coroutines-android** | Android dağıtıcıları |
| **Akış** | Reaktif akışlar |
| **Kanal** | Koroutin iletişimi |
| **StateFlow / SharedFlow** | Devlet yönetimi |
---

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **kotlinx.coroutines** | Eşyordamlar ve eşzamansız |
| **kotlinx.serileştirme** | Çoklu platform serileştirme |
| **kotlinx.datetime** | Tarih/saat kitaplığı |
| **Ok** | Fonksiyonel programlama |
| **Koin** | Hafif DI |
| **Kabza** | Android DI (Hançer sarmalayıcı) |
| **Yenileme** | HTTP istemcisi |
| **TamamHttp** | HTTP motoru |
| **SQLDelight** | Çoklu Platform SQL |
| **Çoklu Platform Oluşturun** | Platformlar arasında paylaşılan kullanıcı arayüzü |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **IntelliJ FİKİRİ** | En iyi Kotlin desteği (JetBrains tarafından oluşturulmuştur) |
| **Android Stüdyosu** | Resmi Android IDE (IntelliJ tabanlı) |
| **Filo** | JetBrains hafif düzenleyici |
| **VS Kodu + Kotlin** | Hafif destek |
---

## Kotlin Çoklu Platform
| Hedef | Notlar |
|----------|----------|
| **Android** | Tam platform desteği |
| **iOS** | Kotlin aracılığıyla/Yerel |
| **JVM** | Masaüstü, sunucu |
| **JS** | Tarayıcı, Node.js |
| **Yerli** | macOS, Windows, Linux |
| **Web Montajı** | Deneysel |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **JAR** | `java -jar app.jar`|
| **Şişman JAR** | uber-jar için gölge eklentisi |
| **Yerel resim** | GraalVM (sınırlı Kotlin desteği) |
| **Docker** | Konteynerli dağıtım |
| **Kotlin/Yerli** | Bağımsız ikili (JVM yok) |
| **Google Play** | Android dağıtımı |
---

## Özet
Kotlin'in ekosistemi JVM, Android, çoklu platform ve sunucu tarafı geliştirmeyi kapsar. Standart yığın şunlardır: Derlemeler için **Gradle (Kotlin DSL)**, IDE olarak **IntelliJ IDEA** veya **Android Studio**, sunucu tarafı için **Ktor** (veya kurumsal için **Spring Boot**), Android kullanıcı arayüzü için **Jetpack Compose**, eşzamansız için **kotlinx.coroutines**, test için **MockK** veya **Kotest**, linting için **detekt** ve **kotlinx.serialization** JSON için. Kotlin Multiplatform, iş mantığının Android, iOS ve arka uçta paylaşılmasına olanak tanır. Kotlin'in güçlü yönleri sıfır güvenliği, kısa ve öz olması, eşyordam tabanlı eşzamansız olması ve kesintisiz Java birlikte çalışmasıdır.