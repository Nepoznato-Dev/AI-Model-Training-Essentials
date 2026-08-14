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
# Kotlin — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы Kotlin.
---

## Инструментальная цепочка
| Инструмент | Цель |
|------|---------|
| **котлинк** | Котлин-компилятор |
| **Gradle + Kotlin DSL** | Система сборки (рекомендуется) |
| **Мавен** | Альтернативная сборка |
| **котлинкс** | Официальные библиотеки Kotlin |
| **Котлин/Нативный** | Компилировать в собственные двоичные файлы |
| **Котлин/JS** | Компилировать в JavaScript |
| **Мультиплатформенность Kotlin** | Общий код на разных платформах |
| **кскрипт** | Котлин-скрипты |
```bash
kotlinc main.kt -include-runtime -d app.jar  # compile
kotlin app.jar                                # run
./gradlew build                               # Gradle build
./gradlew test                                # run tests
```

---

## Инструменты сборки
| Инструмент | Тип | Лучшее для |
|------|------|----------|
| **Gradle (Kotlin DSL)** | Первичный | Android, многомодульный |
| **Gradle (Groovy DSL)** | Наследие | Старые проекты |
| **Мавен** | на основе XML | Предприятие |
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

## Веб-фреймворки
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **Ктор** | Kotlin-родной | Легкий, асинхронный |
| **Весенние ботинки** | Java-взаимодействие | Предприятие, полный пакет |
| **http4k** | Функциональный | Бессерверное, HTTP |
| **Джавалин** | Легкий | Простые веб-приложения |
| **Весна WebFlux** | Реактивный | Высокий параллелизм |
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

## Разработка под Android
| Технология | Цель |
|------------|---------|
| **Создание реактивного ранца** | Современный декларативный пользовательский интерфейс |
| **SDK для Android** | API платформы |
| **Номер** | SQLite ORM |
| **Модернизация** | HTTP-клиент |
| **ОкHttp** | HTTP-движок |
| **Сопрограммы + Flow** | Асинхронное программирование |
| **Эфес/Монета** | Внедрение зависимостей |
| **Компонент навигации** | Экранная навигация |
| **Менеджер работ** | Фоновые задачи |
| **Хранилище данных** | Замена предпочтений |
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

## База данных и ORM
| Технология | Тип |
|------------|------|
| **Раскрыто** | Библиотека SQL Kotlin от JetBrains |
| **Номер** | Android SQLite ORM |
| **Спящий режим/JPA** | Java ORM (взаимодействие с Kotlin) |
| **jOOQ** | Типобезопасный построитель SQL |
| **SQLDelight** | Мультиплатформенный SQL |
| **Царство** | Мобильная база данных |
| **котиса** | Типобезопасный SQL в Котлине |
---

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **котлин.тест** | Встроенные тестовые утилиты |
| **Юнит 5** | Стандартная среда тестирования |
| **МокК** | Kotlin-родное издевательство |
| **Mockito (котлин)** | Java Mockito с поддержкой Kotlin |
| **Котест** | Среда тестирования Kotlin (BDD, свойство) |
| **Турбина** | Тестирование потока |
| **kotlinx-coroutines-test** | Сопрограммное тестирование |
| **котлин-фейкер** | Генерация фейковых данных |
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

## Качество кода
| Инструмент | Цель |
|------|---------|
| **детект** | Статический анализ Котлина |
| **ктлинт** | Линтер и форматтер Kotlin |
| **Ковер** | Покрытие кода (JetBrains) |
| **SonarQube** | Платформа качества кода |
| **Безупречный + ктлинт** | Форматирование в Gradle |
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

## Сериализация
| Библиотека | Цель |
|---------|---------|
| **kotlinx.сериализация** | Официальный, мультиплатформенный |
| **Джексон (котлин-модуль)** | Java JSON с поддержкой Kotlin |
| **Моши (котлин)** | Библиотека JSON Square |
| **kotlinx.serialization.json** | Поддержка JSON |
| **kotlinx.serialization.protobuf** | Поддержка Protobuf |
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

## Сопрограммы и асинхронность
| Библиотека | Цель |
|---------|---------|
| **kotlinx-coroutines-core** | Примитивы сопрограмм |
| **kotlinx-coroutines-android** | Android-диспетчеры |
| **Поток** | Реактивные потоки |
| **Канал** | Корутивная связь |
| **StateFlow/SharedFlow** | Государственное управление |
---

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **kotlinx.coroutines** | Сопрограммы и асинхронность |
| **kotlinx.сериализация** | Мультиплатформенная сериализация |
| **kotlinx.datetime** | Библиотека даты/времени |
| **Стрелка** | Функциональное программирование |
| **Коин** | Легкий ДИ |
| **Эфес** | Android DI (обертка Dagger) |
| **Модернизация** | HTTP-клиент |
| **ОкHttp** | HTTP-движок |
| **SQLDelight** | Мультиплатформенный SQL |
| **Создание мультиплатформы** | Общий пользовательский интерфейс на разных платформах |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **IntelliJ ИДЕЯ** | Лучшая поддержка Kotlin (создана JetBrains) |
| **Андроид-студия** | Официальная IDE для Android (на базе IntelliJ) |
| **Флот** | Облегченный редактор JetBrains |
| **VS-код + Котлин** | Легкая поддержка |
---

## Котлин Мультиплатформенность
| Цель | Заметки |
|--------|-------|
| **Андроид** | Полная поддержка платформы |
| **iOS** | Через Котлин/Родной |
| **JVM** | Десктоп, сервер |
| **JS** | Браузер, Node.js |
| **Родной** | macOS, Windows, Linux |
| **Веб-сборка** | Экспериментальный |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **БАНКА** | `java -jar app.jar`|
| **Жирная банка** | Теневой плагин для uber-jar |
| **Исходное изображение** | GraalVM (ограниченная поддержка Kotlin) |
| **Докер** | Контейнерное развертывание |
| **Котлин/Нативный** | Автономный двоичный файл (без JVM) |
| **Google Play** | Дистрибутив Android |
---

## Краткое содержание
Экосистема Kotlin охватывает JVM, Android, мультиплатформенную и серверную разработку. Стандартный стек: **Gradle (Kotlin DSL)** для сборок, **IntelliJ IDEA** или **Android Studio** в качестве IDE, **Ktor** для серверной части (или **Spring Boot** для предприятий), **Jetpack Compose** для пользовательского интерфейса Android, **kotlinx.coroutines** для асинхронной обработки, **MockK** или **Kotest** для тестирования, **detekt** для линтинг и **kotlinx.serialization** для JSON. Kotlin Multiplatform позволяет совместно использовать бизнес-логику между Android, iOS и серверной частью. Сильными сторонами Kotlin являются нулевая безопасность, лаконичность, асинхронность на основе сопрограмм и бесшовное взаимодействие с Java.