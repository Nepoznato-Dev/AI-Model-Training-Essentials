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

# Kotlin — przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, struktury i infrastrukturę w ekosystemie Kotlin.
---

## Łańcuch narzędzi
| Narzędzie | Cel |
|------|-------------|
| **kotlinc** | Kompilator Kotlina |
| **Gradle + Kotlin DSL** | Zbuduj system (zalecane) |
| **Maven** | Alternatywna kompilacja |
| **kotlinx** | Oficjalne biblioteki Kotlina |
| **Kotlin/Native** | Kompiluj do natywnych plików binarnych |
| **Kotlin/JS** | Kompiluj do JavaScript |
| **Kotlin wieloplatformowy** | Udostępniony kod na różnych platformach |
| **kscript** | Skrypty Kotlina |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## Narzędzia do tworzenia
| Narzędzie | Wpisz | Najlepsze dla |
|------|------|--------------|
| **Gradle (Kotlin DSL)** | Podstawowy | Android, wielomodułowy |
| **Gradle (Groovy DSL)** | Dziedzictwo | Starsze projekty |
| **Maven** | oparty na XML | Przedsiębiorstwo |
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

## Struktury internetowe
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **Ktor** | Natywny dla Kotlina | Lekki, asynchroniczny |
| **Wiosenny but** | Współpraca z Javą | Przedsiębiorstwo, pełny stos |
| **http4k** | Funkcjonalne | Bezserwerowy, HTTP |
| **Javalin** | Lekki | Proste aplikacje internetowe |
| **Wiosenny WebFlux** | Reaktywny | Wysoka współbieżność |
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

## Rozwój Androida
| Technologia | Cel |
|------------|------------|
| **Tworzenie Jetpacka** | Nowoczesny deklaratywny interfejs użytkownika |
| **SDK dla Androida** | Interfejsy API platformy |
| **Pokój** | SQLite ORM |
| **Modernizacja** | Klient HTTP |
| **OKHttp** | Silnik HTTP |
| **Współprogramy + przepływ** | Programowanie asynchroniczne |
| **Rękojeść / Moneta** | Zastrzyk zależności |
| **Element nawigacji** | Nawigacja ekranowa |
| **Menedżer pracy** | Zadania w tle |
| **Magazyn Danych** | Zamiana preferencji |
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

## Baza danych i ORM
| Technologia | Wpisz |
|------------|------|
| **Odsłonięte** | Biblioteka JetBrains Kotlin SQL |
| **Pokój** | Android SQLite ORM |
| **Hibernacja / JPA** | Java ORM (interoperacja z Kotlinem) |
| **jOOQ** | Konstruktor SQL z bezpiecznym typem |
| **Rozkosz SQL** | Wieloplatformowy SQL |
| **Kraina** | Mobilna baza danych |
| **kotysa** | SQL bezpieczny dla typu Kotlin |
---

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **kotlin.test** | Wbudowane narzędzia testowe |
| **Jednostka 5** | Standardowe ramy testów |
| **Mock** | Kpiny w języku Kotlin |
| **Mockito (kotlin)** | Java Mockito z obsługą Kotlina |
| **Kotest** | Framework testowy Kotlina (BDD, właściwość) |
| **Turbina** | Testowanie przepływu |
| **test-kotlinx-coroutines** | Testowanie współprogramowe |
| **kotlin-faker** | Fałszywe generowanie danych |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **wykryj** | Analiza statyczna Kotlina |
| **ktlint** | Linter i formater Kotlina |
| **Koron** | Pokrycie kodu (JetBrains) |
| **SonarQube** | Platforma jakości kodu |
| **Bez skazy + ktlint** | Formatowanie w Gradle |
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

## Serializacja
| Biblioteka | Cel |
|--------|---------|
| **kotlinx.serializacja** | Oficjalny, wieloplatformowy |
| **Jackson (moduł Kotlin)** | Java JSON z obsługą Kotlina |
| **Moshi (kotlin)** | Biblioteka JSON Square |
| **kotlinx.serializacja.json** | Obsługa JSON |
| **kotlinx.serializacja.protobuf** | Wsparcie Protobufa |
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

## Współprogramy i asynchronia
| Biblioteka | Cel |
|--------|---------|
| **kotlinx-coroutines-core** | Współprogramy podstawowe |
| **kotlinx-coroutines-android** | Dyspozytorzy Androida |
| **Przepływ** | Strumienie reaktywne |
| **Kanał** | Komunikacja współprogramowa |
| **StateFlow / SharedFlow** | Zarządzanie państwem |
---

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **kotlinx.korutyny** | Współprogramy i asynchronia |
| **kotlinx.serializacja** | Serializacja wieloplatformowa |
| **kotlinx.datagodzina** | Biblioteka daty/godziny |
| **Strzałka** | Programowanie funkcjonalne |
| **Koina** | Lekki DI |
| **Rękojeść** | Android DI (opakowanie Daggera) |
| **Modernizacja** | Klient HTTP |
| **OKHttp** | Silnik HTTP |
| **Rozkosz SQL** | Wieloplatformowy SQL |
| **Twórz wieloplatformowo** | Wspólny interfejs użytkownika na różnych platformach |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Pomysł IntelliJ** | Najlepsze wsparcie dla Kotlina (zbudowane przez JetBrains) |
| **Studio Androida** | Oficjalne IDE dla Androida (oparte na IntelliJ) |
| **Flota** | Lekki edytor JetBrains |
| **Kod VS + Kotlin** | Lekkie wsparcie |
---

## Wieloplatformowy Kotlin
| Cel | Notatki |
|------------|-------|
| **Android** | Pełna obsługa platformy |
| **iOS** | Przez Kotlin/Native |
| **JVM** | Komputer stacjonarny, serwer |
| **JS** | Przeglądarka, Node.js |
| **Rodzimy** | macOS, Windows, Linux |
| **Zespół sieciowy** | Eksperymentalny |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **SŁOIK** | `java -jar app.jar`|
| **Gruby SŁOik** | Wtyczka Shadow dla uber-jar |
| **Obraz natywny** | GraalVM (ograniczona obsługa Kotlina) |
| **Doker** | Wdrożenie kontenerowe |
| **Kotlin/Native** | Samodzielny plik binarny (bez JVM) |
| **Google Play** | Dystrybucja Androida |
---

## Streszczenie
Ekosystem Kotlina obejmuje JVM, Android, rozwój wieloplatformowy i po stronie serwera. Standardowy stos to: **Gradle (Kotlin DSL)** dla kompilacji, **IntelliJ IDEA** lub **Android Studio** jako IDE, **Ktor** dla serwera (lub **Spring Boot** dla przedsiębiorstw), **Jetpack Compose** dla interfejsu użytkownika Androida, **kotlinx.coroutines** dla asynchronii, **MockK** lub **Kotest** dla testowania, **detekt** dla lintingu, i **kotlinx.serializacja** dla JSON. Kotlin Multiplatform umożliwia udostępnianie logiki biznesowej pomiędzy systemami Android, iOS i backendem. Mocnymi stronami Kotlina są bezpieczeństwo zerowe, zwięzłość, asynchronizacja oparta na współprogramach i płynna współpraca w Javie.