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
# Kotlin: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, i framework e le infrastrutture essenziali nell'ecosistema Kotlin.
---

## Catena di strumenti
| Strumento | Scopo |
|------|---------|
| **kotlinc** | Compilatore Kotlin |
| **Gradle + Kotlin DSL** | Sistema di compilazione (consigliato) |
| **Maven** | Costruzione alternativa |
| **kotlinx** | Biblioteche ufficiali di Kotlin |
| **Kotlin/Nativo** | Compilare in binari nativi |
| **Kotlin/JS** | Compila in JavaScript |
| **Kotlin multipiattaforma** | Codice condiviso su più piattaforme |
| **kscript** | Scripting Kotlin |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## Strumenti di creazione
| Strumento | Digitare | Ideale per |
|------|------|----------|
| **Gradle (Kotlin DSL)** | Primario | Android, multimodulo |
| **Gradle (Groovy DSL)** | Eredità | Progetti più vecchi |
| **Maven** | Basato su XML | Impresa |
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

## Framework Web
| Quadro | Digitare | Ideale per |
|-----------|------|----------|
| **Ktor** | Nativo di Kotlin | Leggero, asincrono |
| **Stivale primaverile** | Interoperabilità Java | Azienda, stack completo |
| **http4k** | Funzionale | Senza server, HTTP |
| **Giavalin** | Leggero | App Web semplici |
| **WebFlux primaverile** | Reattivo | Concorrenza elevata |
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

## Sviluppo Android
| Tecnologia | Scopo |
|------------|---------|
| **Composizione Jetpack** | Moderna interfaccia utente dichiarativa |
| **SDK Android** | API della piattaforma |
| **Camera** | ORM SQLite |
| **Retrofit** | Client HTTP |
| **OkHttp** | Motore HTTP |
| **Coroutine + Flusso** | Programmazione asincrona |
| **Elsa / Koin** | Inserimento delle dipendenze |
| **Componente di navigazione** | Navigazione sullo schermo |
| **GestoreLavoro** | Attività in background |
| **Archivio dati** | Sostituzione delle preferenze |
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

## Database e ORM
| Tecnologia | Digitare |
|------------|------|
| **Esposto** | Libreria SQL Kotlin di JetBrains |
| **Camera** | ORM SQLite per Android |
| **Ibernazione/JPA** | Java ORM (interoperabilità Kotlin) |
| **jOOQ** | Generatore SQL indipendente dai tipi |
| **SQLDelight** | SQL multipiattaforma |
| **Regno** | Banca dati mobile |
| **kotysa** | SQL indipendente dai tipi Kotlin |
---

## Test
| Quadro | Scopo |
|-----------|---------|
| **kotlin.test** | Utilità di test integrate |
| **JUnità 5** | Quadro di prova standard |
| **MockK** | Beffardo nativo di Kotlin |
| **Mockito (kotlin)** | Java Mockito con supporto Kotlin |
| **Kotest** | Framework di test Kotlin (BDD, proprietà) |
| **Turbina** | Prova di flusso |
| **test-kotlinx-coroutine** | Test di coroutine |
| **kotlin-faker** | Generazione di dati falsi |
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

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **rilevato** | Analisi statica Kotlin |
| **ktlint** | Linter e formattatore Kotlin |
| **Kover** | Copertura del codice (JetBrains) |
| **SonarQube** | Piattaforma di qualità del codice |
| **Immacolato + ktlint** | Formattazione in Gradle |
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

## Serializzazione
| Biblioteca | Scopo |
|---------|---------|
| **kotlinx.serializzazione** | Ufficiale, multipiattaforma |
| **Jackson (modulo kotlin)** | Java JSON con supporto Kotlin |
| **Moshi (kotlin)** | Libreria JSON di Square |
| **kotlinx.serialization.json** | Supporto JSON |
| **kotlinx.serialization.protobuf** | Supporto Protobuff |
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

## Coroutine e asincrono
| Biblioteca | Scopo |
|---------|---------|
| **kotlinx-coroutines-core** | Primitive della coroutine |
| **kotlinx-coroutines-android** | Dispatcher Android |
| **Flusso** | Flussi reattivi |
| **Canale** | Comunicazione coroutine |
| **StateFlow / SharedFlow** | Gestione statale |
---

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **kotlinx.coroutines** | Coroutine e asincroni |
| **kotlinx.serializzazione** | Serializzazione multipiattaforma |
| **kotlinx.datetime** | Libreria data/ora |
| **Freccia** | Programmazione funzionale |
| **Koin** | DI leggero |
| **Elsa** | Android DI (involucro del pugnale) |
| **Retrofit** | Client HTTP |
| **OkHttp** | Motore HTTP |
| **SQLDelight** | SQL multipiattaforma |
| **Componi multipiattaforma** | Interfaccia utente condivisa su più piattaforme |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **IDEA IntelliJ** | Miglior supporto Kotlin (creato da JetBrains) |
| **AndroidStudio** | IDE Android ufficiale (basato su IntelliJ) |
| **Flotta** | Editor leggero di JetBrains |
| **Codice VS + Kotlin** | Supporto leggero |
---

## Multipiattaforma Kotlin
| Obiettivo | Note |
|--------|-------|
| **Android** | Supporto completo della piattaforma |
| **iOS** | Via Kotlin/Nativo |
| **JVM** | Desktop, server |
| **JS** | Browser, Node.js |
| **Nativo** | macOS, Windows, Linux |
| **WebAssembly** | Sperimentale |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **VASETTO** | `java -jar app.jar`|
| **VASETTO grasso** | Plugin ombra per uber-jar |
| **Immagine nativa** | GraalVM (supporto Kotlin limitato) |
| **Docker** | Distribuzione in contenitori |
| **Kotlin/Nativo** | Binario autonomo (senza JVM) |
| **Google Play** | Distribuzione Android |
---

## Riepilogo
L'ecosistema di Kotlin abbraccia JVM, Android, multipiattaforma e sviluppo lato server. Lo stack standard è: **Gradle (Kotlin DSL)** per build, **IntelliJ IDEA** o **Android Studio** come IDE, **Ktor** per lato server (o **Spring Boot** per aziende), **Jetpack Compose** per interfaccia utente Android, **kotlinx.coroutines** per asincrono, **MockK** o **Kotest** per test, **detekt** per linting e **kotlinx.serialization** per JSON. Kotlin Multiplatform consente la condivisione della logica aziendale su Android, iOS e backend. I punti di forza di Kotlin sono la sicurezza nulla, la concisione, l'asincronia basata su coroutine e l'interoperabilità Java senza soluzione di continuità.