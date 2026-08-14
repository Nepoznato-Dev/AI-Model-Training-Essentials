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

# Kotlin: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema de Kotlin.
---

## Cadena de herramientas
| Herramienta | Propósito |
|------|---------|
| **kotlinc** | Compilador Kotlin |
| **Gradle + Kotlin DSL** | Sistema de construcción (recomendado) |
| **Maven** | Construcción alternativa |
| **kotlinx** | Bibliotecas oficiales de Kotlin |
| **Kotlin/Nativo** | Compilar en binarios nativos |
| **Kotlin/JS** | Compilar en JavaScript |
| **Kotlin multiplataforma** | Código compartido entre plataformas |
| **kscript** | Secuencias de comandos Kotlin |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## Herramientas de construcción
| Herramienta | Tipo | Mejor para |
|------|------|----------|
| **Gradle (Kotlin DSL)** | Primaria | Android, multimódulo |
| **Gradle (DSL maravilloso)** | Legado | Proyectos más antiguos |
| **Maven** | Basado en XML | Empresa |
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

## Marcos web
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **Ktor** | Nativo de Kotlin | Ligero, asíncrono |
| **Bota de primavera** | Interoperabilidad de Java | Empresa, pila completa |
| **http4k** | Funcional | Sin servidor, HTTP |
| **Javalín** | Ligero | Aplicaciones web sencillas |
| **Flujo web de primavera** | Reactivo | Alta concurrencia |
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

## Desarrollo de Android
| Tecnología | Propósito |
|------------|---------|
| **Composición Jetpack** | UI declarativa moderna |
| **SDK de Android** | API de plataforma |
| **Habitación** | ORM de SQLite |
| **Reequipamiento** | Cliente HTTP |
| **ValeHttp** | Motor HTTP |
| **Corrutinas + Flujo** | Programación asíncrona |
| **Empuñadura/Koin** | Inyección de dependencia |
| **Componente de navegación** | Navegación en pantalla |
| **Administrador de trabajo** | Tareas en segundo plano |
| **Almacén de datos** | Reemplazo de preferencias |
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

## Base de datos y ORM
| Tecnología | Tipo |
|------------|------|
| **Expuesto** | Biblioteca SQL Kotlin de JetBrains |
| **Habitación** | ORM SQLite de Android |
| **Hibernar/JPA** | Java ORM (interoperabilidad con Kotlin) |
| **jOOQ** | Generador de SQL con seguridad de tipos |
| **SQLDelight** | SQL multiplataforma |
| **Reino** | Base de datos móvil |
| **kotysa** | SQL con seguridad de tipos de Kotlin |
---

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **prueba.kotlin** | Utilidades de prueba integradas |
| **JUnidad 5** | Marco de prueba estándar |
| **MockK** | Burla nativa de Kotlin |
| **Mockito (kotlin)** | Java Mockito con soporte Kotlin |
| **Prueba** | Marco de prueba de Kotlin (BDD, propiedad) |
| **Turbina** | Pruebas de flujo |
| **prueba-de-rutinas-kotlinx** | Pruebas de rutina |
| **kotlin-falso** | Generación de datos falsos |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **detecta** | Análisis estático de Kotlin |
| **ktlint** | Linter y formateador Kotlin |
| **Kover** | Cobertura de código (JetBrains) |
| **SónarQube** | Plataforma de calidad de código |
| **Impecable + ktlint** | Formateo en Gradle |
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

## Serialización
| Biblioteca | Propósito |
|---------|---------|
| **kotlinx.serialización** | Oficial, multiplataforma |
| **Jackson (módulo kotlin)** | Java JSON con soporte Kotlin |
| **Moshi (kotlin)** | Biblioteca JSON de Square |
| **kotlinx.serialización.json** | Soporte JSON |
| **kotlinx.serialización.protobuf** | Soporte de Protobuf |
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

## Corrutinas y asíncronos
| Biblioteca | Propósito |
|---------|---------|
| **kotlinx-coroutines-core** | Primitivas de rutina |
| **kotlinx-corrutinas-android** | Despachadores de Android |
| **Flujo** | Corrientes reactivas |
| **Canal** | Comunicación rutinaria |
| **Flujo de estado/Flujo compartido** | Gestión estatal |
---

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **kotlinx.coroutines** | Corrutinas y asíncronos |
| **kotlinx.serialización** | Serialización multiplataforma |
| **kotlinx.datetime** | Biblioteca de fecha/hora |
| **Flecha** | Programación funcional |
| **Moneda** | DI ligero |
| **Empuñadura** | Android DI (contenedor Dagger) |
| **Reequipamiento** | Cliente HTTP |
| **ValeHttp** | Motor HTTP |
| **SQLDelight** | SQL multiplataforma |
| **Redactar multiplataforma** | UI compartida entre plataformas |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **IDEA IntelliJ** | Mejor soporte para Kotlin (creado por JetBrains) |
| **Estudio Android** | IDE oficial de Android (basado en IntelliJ) |
| **Flota** | Editor ligero de JetBrains |
| **Código VS + Kotlin** | Soporte ligero |
---

## Kotlin multiplataforma
| Objetivo | Notas |
|--------|-------|
| **Android** | Soporte completo de plataforma |
| **iOS** | Vía Kotlin/Nativo |
| **JVM** | Escritorio, servidor |
| **JS** | Navegador, Node.js |
| **Nativo** | MacOS, Windows, Linux |
| **Asamblea web** | Experimentales |
---

## Implementación
| Método | Notas |
|--------|-------|
| **TARRO** | `java -jar app.jar`|
| **TARRO gordo** | Complemento de sombra para uber-jar |
| **Imagen nativa** | GraalVM (soporte limitado de Kotlin) |
| **Acoplador** | Implementación en contenedores |
| **Kotlin/Nativo** | Binario independiente (sin JVM) |
| **GooglePlay** | Distribución de Android |
---

## Resumen
El ecosistema de Kotlin abarca JVM, Android, multiplataforma y desarrollo del lado del servidor. La pila estándar es: **Gradle (Kotlin DSL)** para compilaciones, **IntelliJ IDEA** o **Android Studio** como IDE, **Ktor** para el lado del servidor (o **Spring Boot** para empresas), **Jetpack Compose** para la interfaz de usuario de Android, **kotlinx.coroutines** para async, **MockK** o **Kotest** para pruebas, **detekt** para linting y **kotlinx.serialization** para JSON. Kotlin Multiplatform permite compartir la lógica empresarial entre Android, iOS y backend. Los puntos fuertes de Kotlin son la seguridad nula, la concisión, la asincronía basada en rutinas y la interoperabilidad perfecta de Java.