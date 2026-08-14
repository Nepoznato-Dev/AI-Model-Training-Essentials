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
# Kotlin – Guia de ecossistema e ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais do ecossistema Kotlin.
---

## Conjunto de ferramentas
| Ferramenta | Finalidade |
|------|---------|
| **kotlinc** | Compilador Kotlin |
| **Gradle + Kotlin DSL** | Sistema de construção (recomendado) |
| **Maven** | Construção alternativa |
| **kotlinx** | Bibliotecas oficiais Kotlin |
| **Kotlin/Nativo** | Compilar para binários nativos |
| **Kotlin/JS** | Compilar para JavaScript |
| **Multiplataforma Kotlin** | Código compartilhado entre plataformas |
| **kscript** | Scripts Kotlin |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## Ferramentas de construção
| Ferramenta | Tipo | Melhor para |
|------|------|----------|
| **Gradle (DSL Kotlin)** | Primário | Android, multimódulo |
| **Gradle (DSL bacana)** | Legado | Projetos mais antigos |
| **Maven** | Baseado em XML | Empresa |
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

## Estruturas Web
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **Ktor** | Nativo de Kotlin | Leve, assíncrono |
| **Bota de primavera** | Interoperabilidade Java | Empresarial, full-stack |
| **http4k** | Funcional | Sem servidor, HTTP |
| **Javalino** | Leve | Aplicativos web simples |
| **Spring WebFlux** | Reativo | Alta simultaneidade |
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

## Desenvolvimento Android
| Tecnologia | Finalidade |
|------------|---------|
| **Jetpack Compose** | UI declarativa moderna |
| **SDK Android** | APIs de plataforma |
| **Quarto** | SQLite ORM |
| **Retrofit** | Cliente HTTP |
| **OkHttp** | Mecanismo HTTP |
| **Corrotinas + Fluxo** | Programação assíncrona |
| **Cabo / Koin** | Injeção de dependência |
| **Componente de navegação** | Navegação na tela |
| **WorkManager** | Tarefas em segundo plano |
| **Armazém de Dados** | Substituição de preferências |
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

## Banco de dados e ORM
| Tecnologia | Tipo |
|------------|------|
| **Exposto** | Biblioteca SQL Kotlin da JetBrains |
| **Quarto** | Android SQLite ORM |
| **Hibernar/JPA** | Java ORM (interoperabilidade Kotlin) |
| **jOOQ** | Construtor SQL com segurança de tipo |
| **SQLDelight** | SQL multiplataforma |
| **Reino** | Banco de dados móvel |
| **kotysa** | SQL com segurança de tipo Kotlin |
---

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **kotlin.teste** | Utilitários de teste integrados |
| **JUnit 5** | Estrutura de teste padrão |
| **MockK** | Zombaria nativa de Kotlin |
| **Mockito (kotlin)** | Java Mockito com suporte Kotlin |
| **Kotest** | Estrutura de teste Kotlin (BDD, propriedade) |
| **Turbina** | Teste de fluxo |
| **kotlinx-coroutines-test** | Testes de rotina |
| **kotlin-faker** | Geração de dados falsos |
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

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **detecção** | Análise estática Kotlin |
| **ktlint** | Linter e formatador Kotlin |
| **Kover** | Cobertura de código (JetBrains) |
| **SonarQube** | Plataforma de qualidade de código |
| **Impecável + ktlint** | Formatando no Gradle |
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

## Serialização
| Biblioteca | Finalidade |
|--------|---------|
| **kotlinx.serialização** | Oficial, multiplataforma |
| **Jackson (módulo kotlin)** | Java JSON com suporte Kotlin |
| **Moshi (kotlin)** | Biblioteca JSON da Square |
| **kotlinx.serialization.json** | Suporte JSON |
| **kotlinx.serialization.protobuf** | Suporte protobuf |
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

## Corrotinas e assíncronas
| Biblioteca | Finalidade |
|--------|---------|
| **kotlinx-coroutines-core** | Primitivas de co-rotina |
| **kotlinx-coroutines-android** | Despachantes Android |
| **Fluxo** | Fluxos reativos |
| **Canal** | Comunicação de rotina |
| **StateFlow/SharedFlow** | Gestão do Estado |
---

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **kotlinx.coroutines** | Corrotinas e assíncronas |
| **kotlinx.serialização** | Serialização multiplataforma |
| **kotlinx.datetime** | Biblioteca de data/hora |
| **Seta** | Programação funcional |
| **Moeda** | DI leve |
| **Cabo** | Android DI (invólucro de punhal) |
| **Retrofit** | Cliente HTTP |
| **OkHttp** | Mecanismo HTTP |
| **SQLDelight** | SQL multiplataforma |
| **Compose Multiplataforma** | UI compartilhada entre plataformas |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **IDEIA IntelliJ** | Melhor suporte Kotlin (desenvolvido pela JetBrains) |
| **Estúdio Android** | IDE oficial do Android (baseado em IntelliJ) |
| **Frota** | Editor leve JetBrains |
| **Código VS + Kotlin** | Suporte leve |
---

## Multiplataforma Kotlin
| Alvo | Notas |
|-------|-------|
| **Android** | Suporte completo à plataforma |
| **iOS** | Via Kotlin/Nativo |
| **JVM** | Desktop, servidor |
| **JS** | Navegador, Node.js |
| **Nativo** | MacOS, Windows, Linux |
| **WebAssembly** | Experimental |
---

## Implantação
| Método | Notas |
|-------|-------|
| **JAR** | `java -jar app.jar`|
| **JAR de gordura** | Plug-in Shadow para uber-jar |
| **Imagem nativa** | GraalVM (suporte limitado a Kotlin) |
| **Docker** | Implantação em contêineres |
| **Kotlin/Nativo** | Binário independente (sem JVM) |
| **Google Play** | Distribuição Android |
---

## Resumo
O ecossistema do Kotlin abrange JVM, Android, multiplataforma e desenvolvimento no lado do servidor. A pilha padrão é: **Gradle (Kotlin DSL)** para compilações, **IntelliJ IDEA** ou **Android Studio** como IDE, **Ktor** para lado do servidor (ou **Spring Boot** para empresas), **Jetpack Compose** para Android UI, **kotlinx.coroutines** para assíncrono, **MockK** ou **Kotest** para testes, **detekt** para linting e **kotlinx.serialization** para JSON. Kotlin Multiplatform permite compartilhar lógica de negócios em Android, iOS e back-end. Os pontos fortes do Kotlin são segurança nula, concisão, assíncrona baseada em corrotinas e interoperabilidade Java contínua.