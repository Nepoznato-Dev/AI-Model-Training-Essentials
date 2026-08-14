<!--
---
# Metadata
title: "Scala — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Scala ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Scala – Ökosystem- und Tooling-Leitfaden
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im Scala-Ökosystem.
---

## Scala-Versionen und Laufzeiten
| Version | Notizen |
|---------|-------|
| **Scala 3** | Aktuelle, saubere Syntax, neue Funktionen |
| **Scala 2.13** | Weit verbreitet, ausgereift |
| **Scala.js** | In JavaScript kompilieren |
| **Scala Native** | In nativen Code kompilieren |
| **JVM** | Primäre Laufzeit (Java-Interop) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## Build-Tools
| Werkzeug | Geben Sie | ein Am besten für |
|------|------|----------|
| **sbt** | Standard | Die meisten Scala-Projekte |
| **Mühle** | Modern | Schnelle, einfachere Konfiguration |
| **Gradle** | Java-Interop | Gemischtes Java/Scala |
| **scala-cli** | Leicht | Skripte, kleine Projekte |
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

## Web-Frameworks
| Rahmen | Geben Sie | ein Am besten für |
|-----------|------|----------|
| **http4s** | Funktional | Typsicheres HTTP (Katzeneffekt) |
| **Pekko HTTP** | Schauspielerbasiert | Apache Pekko (Akka-Gabel) |
| **Play Framework** | Full-Stack | Reaktive Web-Apps |
| **ZIO HTTP** | ZIO-basiert | Funktional, leistungsstark |
| **Finatra** | Twitter | Microservices |
| **Tapir** | Endpunkt-DSL | Typsichere API-Beschreibungen |
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

## Big Data und Datentechnik
| Technologie | Zweck |
|------------|---------|
| **Apache Spark** | Verteilte Datenverarbeitung (Scala-nativ) |
| **Apache Kafka** | Ereignis-Streaming (Scala-Client) |
| **Apache Flink** | Stream-Verarbeitung |
| **Apache Pekko Streams** | Reaktive Ströme |
| **Akka-Streams** | Reaktive Streams (Legacy) |
| **Scio** | Google Cloud Dataflow (Spotify) |
| **Vulkanier** | Entwicklung des Avro-Schemas |
---

## Datenbank und ORM
| Technologie | Geben Sie | ein
|------------|------|
| **Doobie** | Funktioneller JDBC (Katzeneffekt) |
| **Slick** | Funktional relational |
| **Feder** | Anführungszeichen zur Kompilierungszeit |
| **Anorm** | Einfacher SQL-Zugriff (Play) |
| **Stinktier** | PostgreSQL (Katzeneffekt, NIO) |
| **Caliban** | GraphQL |
| **Sangria** | GraphQL |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **MUnit** | Einfach, modern (empfohlen) |
| **ScalaTest** | Reich an Funktionen, viele Stile |
| **Weber** | Funktional, unveränderlich |
| **Munit-Cats-Effekt** | Testen des Katzeneffekts |
| **Mockito-Scala** | Spott |
| **Scalacheck** | Eigenschaftsbasiertes Testen |
| **testcontainers-scala** | Docker-basierte Integration |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **scalafmt** | Codeformatierung |
| **Scalafix** | Linting und Refactoring |
| **Warzenentferner** | Linter zur Kompilierungszeit |
| **Sündenbock** | Statische Analyse |
| **sbt-tpolecat** | Strikte Compileroptionen |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## Funktionale Programmierbibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **Katzen** | Funktionale Abstraktionen (Typklassen) |
| **Katzeneffekt** | E/A-Monade, asynchrone Laufzeit |
| **ZIO** | Wirkungssystem, vollständiges Ökosystem |
| **Formlos** | Generische Programmierung (Scala 2) |
| **Kätzchen** | Abgeleitete Typklasseninstanzen |
| **Monokel** | Optikbibliothek |
---

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **Circe** | JSON-Bibliothek (Katzen) |
| **upickle** | JSON-Serialisierung |
| **ZIO JSON** | Schnelles JSON (ZIO) |
| **fs2** | Funktionsströme |
| **Tapir** | Typsichere API-Endpunkte |
| **Caliban** | GraphQL-Server |
| **Log4cats** | Funktionale Protokollierung |
| **Ablehnen** | CLI-Argumentanalyse |
| **Squants** | Typsichere Mengen |
| **Enumeratum** | Erweiterte Aufzählungen |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **IntelliJ IDEA + Scala-Plugin** | Beste Scala-IDE |
| **Metalle** | Sprachserver (Multi-Editor) |
| **VS-Code + Metalle** | Leichtgewicht mit LSP |
| **Neovim + Metalle** | Terminalbasiert |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Fett JAR** | `sbt assembly`|
| **Docker** | Mehrstufige Builds |
| **GraalVM Native** | Natives Bild (begrenzt) |
| **Kubernetes** | Orchestrierung |
| **AWS EMR** | Spark auf AWS |
| **Datenbausteine** | Spark-Plattform |
---

## Zusammenfassung
Das Ökosystem von Scala umfasst Unternehmen, funktionale Programmierung und Big Data. Der Standard-Stack ist: **sbt** für Builds, **Scala 3** für die Sprache, **http4s + cats-effect** oder **ZIO** für funktionale Webdienste, **Doobie** oder **Slick** für Datenbankzugriff, **MUnit** für Tests, **scalafmt** für Formatierung und **IntelliJ + Metals** für IDE-Unterstützung. Scala dominiert bei Big Data (Apache Spark ist in Scala geschrieben), Streaming (Pekko Streams) und überall dort, wo JVM-Leistung auf funktionale Programmierung trifft. Die sauberere Syntax, Aufzählungen und Schnittmengentypen von Scala 3 machen die Sprache zugänglicher.