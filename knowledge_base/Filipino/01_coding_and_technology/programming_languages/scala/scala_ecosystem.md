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
# Scala — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, framework, at imprastraktura sa Scala ecosystem.
---

## Mga Bersyon at Runtime ng Scala
| Bersyon | Mga Tala |
|---------|-------|
| **Scala 3** | Kasalukuyan, malinis na syntax, mga bagong feature |
| **Scala 2.13** | Malawakang ginagamit, mature |
| **Scala.js** | Mag-compile sa JavaScript |
| **Scala Native** | Mag-compile sa native code |
| **JVM** | Pangunahing runtime (Java interop) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## Bumuo ng Mga Tool
| Tool | Uri | Pinakamahusay Para sa |
|------|------|----------|
| **sbt** | Pamantayan | Karamihan sa mga proyekto ng Scala |
| **Mill** | Moderno | Mabilis, mas simpleng config |
| **Gradle** | Java interop | Mixed Java/Scala |
| **scala-cli** | Magaan | Mga script, maliliit na proyekto |
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

## Mga Web Framework
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **http4s** | Nagagamit | Type-safe na HTTP (cats-effect) |
| **Pekko HTTP** | Batay sa aktor | Apache Pekko (Akka tinidor) |
| **Play Framework** | Full-stack | Mga reaktibong web app |
| **ZIO HTTP** | Nakabatay sa ZIO | Functional, mataas ang pagganap |
| **Finatra** | Twitter | Mga Microservice |
| **Tapir** | Endpoint DSL | Mga paglalarawan ng API na ligtas sa uri |
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

## Big Data at Data Engineering
| Teknolohiya | Layunin |
|------------|---------|
| **Apache Spark** | Ibinahagi ang pagproseso ng data (Scala-native) |
| **Apache Kafka** | Pag-stream ng kaganapan (Scala client) |
| **Apache Flink** | Pagproseso ng stream |
| **Mga Stream ng Apache Pekko** | Mga reaktibong stream |
| **Mga Agos ng Akka** | Mga reaktibong stream (legacy) |
| **Scio** | Google Cloud Dataflow (Spotify) |
| **Vulcan** | Avro schema evolution |
---

## Database at ORM
| Teknolohiya | Uri |
|------------|------|
| **Doobie** | Functional na JDBC (cats-effect) |
| **Makinis** | Functional relational |
| **Quill** | Compile-time na naka-quote na mga query |
| **Anorm** | Simpleng SQL access (Play) |
| **Skunk** | PostgreSQL (cats-effect, NIO) |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **MUnit** | Simple, moderno (inirerekomenda) |
| **ScalaTest** | Mayaman sa tampok, maraming istilo |
| **Weaver** | Nagagamit, hindi nababago |
| **munit-cats-effect** | Pagsubok sa epekto ng pusa |
| **mockito-scala** | Nanunuya |
| **scalacheck** | Pagsubok na nakabatay sa ari-arian |
| **testcontainers-scala** | Pagsasama na nakabatay sa docker |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **scalafmt** | Pag-format ng code |
| **scalafix** | Linting at refactoring |
| **WartRemover** | Compile-time linter |
| **scapegoat** | Static na pagsusuri |
| **sbt-tpolecat** | Mahigpit na pagpipilian sa compiler |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## Functional Programming Libraries
| Aklatan | Layunin |
|---------|---------|
| **Mga Pusa** | Mga functional abstraction (mga uri ng klase) |
| **Epekto ng Pusa** | IO monad, async runtime |
| **ZIO** | Effect system, buong ecosystem |
| **Walang hugis** | Generic na programming (Scala 2) |
| **Mga Kuting** | Mga instance ng klase ng nagmula na uri |
| **Monocle** | Optics library |
---

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **Circe** | JSON library (mga pusa) |
| **upickle** | JSON serialization |
| **ZIO JSON** | Mabilis na JSON (ZIO) |
| **fs2** | Mga functional na stream |
| **Tapir** | Mga endpoint ng API na ligtas sa uri |
| **Caliban** | GraphQL server |
| **Log4cats** | Functional na pag-log |
| **Tanggihan** | CLI argument parsing |
| **Squants** | Uri-ligtas na dami |
| **Enumeratum** | Mga pinahusay na enum |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **IntelliJ IDEA + Scala plugin** | Pinakamahusay na Scala IDE |
| **Mga Metal** | Server ng wika (multi-editor) |
| **VS Code + Mga Metal** | Magaan sa LSP |
| **Neovim + Metals** | Nakabatay sa terminal |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Fat JAR** | `sbt assembly`|
| **Docker** | Multi-stage build |
| **GraalVM Native** | Katutubong larawan (limitado) |
| **Kubernetes** | Orkestrasyon |
| **AWS EMR** | Spark sa AWS |
| **Mga Databrick** | Spark platform |
---

## Buod
Ang ecosystem ng Scala ay sumasaklaw sa enterprise, functional programming, at malaking data. Ang karaniwang stack ay: **sbt** para sa mga build, **Scala 3** para sa wika, **http4s + cats-effect** o **ZIO** para sa mga functional na serbisyo sa web, **Doobie** o **Slick** para sa access sa database, **MUnit** para sa pagsubok, **scalafmt** para sa pag-format, at **IntelliJ + Metals** para sa suporta sa IDE. Nangibabaw ang Scala sa malaking data (Ang Apache Spark ay nakasulat sa Scala), streaming (Pekko Stream), at kahit saan ang pagganap ng JVM ay nakakatugon sa functional programming. Ang mas malinis na syntax, enum, at mga uri ng intersection ng Scala 3 ay ginagawang mas madaling lapitan ang wika.