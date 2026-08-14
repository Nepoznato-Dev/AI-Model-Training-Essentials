---
# Metadata
title: "Scala — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Scala ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [scala, ecosystem, tooling, sbt, spark, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Scala — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, платформы и инфраструктура экосистемы Scala.
---

## Версии и среды выполнения Scala
| Версия | Заметки |
|---------|-------|
| **Скала 3** | Текущий, чистый синтаксис, новые функции |
| **Скала 2.13** | Широко используется, зрелый |
| **Scala.js** | Компилировать в JavaScript |
| **Скала Native** | Компилировать в собственный код |
| **JVM** | Основная среда выполнения (взаимодействие с Java) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## Инструменты сборки
| Инструмент | Тип | Лучшее для |
|------|------|----------|
| **что** | Стандарт | Большинство проектов Scala |
| **Мельница** | Современный | Быстрая и простая настройка |
| **Грейдл** | Java-взаимодействие | Смешанная Java/Scala |
| **скала-кли** | Легкий | Скрипты, небольшие проекты |
```scala
// build.sbt
lazy val root = (project in file("."))
  .settings(
    name := "myapp",
    version := "0.1.0",
    scalaVersion := "3.4.0",
    libraryDependencies ++= Seq(
      "org.http4s" %% "http4s-dsl" % "0.23.25",
      "org.http4s" %% "http4s-ember-server" % "0.23.25",
      "org.typelevel" %% "cats-effect" % "3.5.4",
      "org.scalameta" %% "munit" % "1.0.0" % Test
    )
  )
```

```bash
sbt compile               # compile
sbt test                  # run tests
sbt run                   # run application
sbt package               # create JAR
sbt assembly              # fat JAR (sbt-assembly)
```

---

## Веб-фреймворки
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **http4s** | Функциональный | Типобезопасный HTTP (кошачий эффект) |
| **Пекко HTTP** | Актерский | Апач Пекко (вилка Акка) |
| **Игровая платформа** | Полный стек | Реактивные веб-приложения |
| **ЗИО HTTP** | на базе ЗИО | Функциональный, высокопроизводительный |
| **Финатра** | Твиттер | Микросервисы |
| **Тапир** | Конечная точка DSL | Описания типобезопасного API |
```scala
// http4s + cats-effect example
import cats.effect.*
import org.http4s.*
import org.http4s.dsl.io.*
import org.http4s.ember.server.*

object HelloWorld extends IOApp.Simple {
  val routes = HttpRoutes.of[IO] {
    case GET -> Root / "hello" => Ok("Hello, World!")
    case GET -> Root / "users" / IntVar(id) =>
      UserService.find(id).flatMap {
        case Some(user) => Ok(user.asJson)
        case None       => NotFound()
      }
  }.orNotFound

  def run = EmberServerBuilder
    .default[IO]
    .withHost(ipv4"0.0.0.0")
    .withPort(port"8080")
    .withHttpApp(routes)
    .build
    .useForever
}
```

---

## Большие данные и инженерия данных
| Технология | Цель |
|------------|---------|
| **Apache Spark** | Распределенная обработка данных (Scala-native) |
| **Апач Кафка** | Потоковая передача событий (клиент Scala) |
| **Apache Flink** | Потоковая обработка |
| **Потоки Apache Pekko** | Реактивные потоки |
| **Потоки Акка** | Реактивные потоки (устаревшие версии) |
| **Наука** | Облачный поток данных Google (Spotify) |
| **Вулкан** | Эволюция схемы Avro |
---

## База данных и ORM
| Технология | Тип |
|------------|------|
| **Дуби** | Функциональный JDBC (кошачий эффект) |
| **Ловкий** | Функциональный реляционный |
| **Перо** | Запросы с цитированием во время компиляции |
| **Анорма** | Простой доступ SQL (Играть) |
| **Скунс** | PostgreSQL (кошачий эффект, NIO) |
| **Калибан** | ГрафQL |
| **Сангрия** | ГрафQL |
```scala
// Doobie example
import doobie.*
import doobie.implicits.*

def findUser(id: Long): ConnectionIO[Option[User]] =
  sql"SELECT id, name, email FROM users WHERE id = $id"
    .query[User]
    .option
```

---

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **МУнит** | Простой, современный (рекомендуется) |
| **СкалаТест** | Многофункциональный, множество стилей |
| **Ткач** | Функциональный, неизменный |
| **эффект мунит-кошек** | Тестирование на эффект кошек |
| **мокито-скала** | Издевательство |
| **скалачек** | Тестирование на основе свойств |
| **testcontainers-скала** | Интеграция на основе Docker |
```scala
// MUnit example
class UserServiceSuite extends munit.FunSuite {
  test("find user by id") {
    val repo = new InMemoryUserRepo
    repo.insert(User(1, "Alice"))
    val service = new UserService(repo)

    val result = service.find(1).unsafeRunSync()

    assertEquals(result.map(_.name), Some("Alice"))
  }
}
```

---

## Качество кода
| Инструмент | Цель |
|------|---------|
| **скалафмт** | Форматирование кода |
| **скалафикс** | Линтинг и рефакторинг |
| **Удаление бородавок** | Линтер времени компиляции |
| **козел отпущения** | Статический анализ |
| **sbt-tpolecat** | Строгие параметры компилятора |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## Библиотеки функционального программирования
| Библиотека | Цель |
|---------|---------|
| **Кошки** | Функциональные абстракции (классы типов) |
| **Эффект кошки** | Монада ввода-вывода, асинхронная среда выполнения |
| **ЗИО** | Система эффектов, полная экосистема |
| **Бесформенный** | Общее программирование (Scala 2) |
| **Котята** | Экземпляры классов производных типов |
| **Монокль** | Библиотека оптики |
---

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **Цирцея** | Библиотека JSON (коты) |
| **огурец** | Сериализация JSON |
| **ЗИО JSON** | Быстрый JSON (ZIO) |
| **fs2** | Функциональные потоки |
| **Тапир** | Типобезопасные конечные точки API |
| **Калибан** | Сервер GraphQL |
| **Log4cats** | Функциональное журналирование |
| **Отказ** | Анализ аргументов CLI |
| **Скванты** | Типобезопасные количества |
| **Перечисление** | Расширенные перечисления |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **Плагин IntelliJ IDEA + Scala** | Лучшая Scala IDE |
| **Металлы** | Языковой сервер (мультиредактор) |
| **Код VS + Металлы** | Облегченный с ЛСП |
| **Неовим + Металлы** | На базе терминала |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Жирная банка** | `sbt assembly`|
| **Докер** | Многоэтапные сборки |
| **Встроенный GraalVM** | Исходное изображение (ограничено) |
| **Кубернетес** | Оркестровка |
| **AWS EMR** | Искра на AWS |
| **Блок данных** | Искра платформа |
---

## Краткое содержание
Экосистема Scala охватывает корпоративное программное обеспечение, функциональное программирование и большие данные. Стандартный стек: **sbt** для сборок, **Scala 3** для языка, **http4s + Cats-effect** или **ZIO** для функциональных веб-сервисов, **Doobie** или **Slick** для доступа к базе данных, **MUnit** для тестирования, **scalafmt** для форматирования и **IntelliJ + Metals** для поддержки IDE. Scala доминирует в области больших данных (Apache Spark написан на Scala), потоковой передачи (Pekko Streams) и везде, где производительность JVM соответствует функциональному программированию. Более чистый синтаксис Scala 3, перечисления и типы пересечений делают язык более доступным.