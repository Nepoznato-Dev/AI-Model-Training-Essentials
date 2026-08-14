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
# Scala - Mfumo wa ikolojia na Mwongozo wa zana
Mwongozo huu unashughulikia zana muhimu, mifumo, na miundombinu katika mfumo ikolojia wa Scala.
---

## Matoleo ya Scala & Nyakati za Kuendesha
| Toleo | Vidokezo |
|---------|-------|
| **Scala 3** | Sintaksia ya sasa, safi, vipengele vipya |
| **Scala 2.13** | Inatumika sana, iliyokomaa |
| **Scala.js** | Unganisha kwa JavaScript |
| **Mzaliwa wa Scala** | Unganisha kwa msimbo asilia |
| **JVM** | Muda wa msingi wa utekelezaji (Java interop) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## Zana za Kujenga
| Zana | Andika | Bora Kwa |
|------|------|----------|
| **sbt** | Kawaida | Miradi mingi ya Scala |
| **Kinu** | Kisasa | Usanidi wa haraka na rahisi zaidi |
| **Gradle** | Java interop | Java/Scala Mchanganyiko |
| **scala-cli** | Nyepesi | Hati, miradi midogo |
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

## Mifumo ya Wavuti
| Mfumo | Andika | Bora Kwa |
|-----------|------|-----------|
| **http4s** | Inafanya kazi | HTTP ya aina-salama (athari ya paka) |
| **Pekko HTTP** | Kulingana na mwigizaji | Apache Pekko (uma wa Akka) |
| **Mfumo wa Cheza** | Rafu kamili | Programu tendaji za wavuti |
| **ZIO HTTP** | ZIO-msingi | Inafanya kazi, utendakazi wa hali ya juu |
| **Finatra** | Twitter | Huduma ndogo |
| **Tapir** | Mwisho wa DSL | Maelezo ya API ya aina-salama |
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

## Uhandisi Kubwa wa Data na Data
| Teknolojia | Kusudi |
|------------|---------|
| **Apache Spark** | Usindikaji wa data uliosambazwa (Scala-asili) |
| **Apache Kafka** | Utiririshaji wa hafla (mteja wa Scala) |
| **Apache Flink** | Uchakataji wa mtiririko |
| **Mipasho ya Apache Pekko** | Mitiririko tendaji |
| **Mipasho ya Akka** | Mitiririko tendaji (urithi) |
| **Scio** | Google Cloud Dataflow (Spotify) |
| **Vulcan** | Mageuzi ya schema ya Avro |
---

## Hifadhidata & ORM
| Teknolojia | Andika |
|------------|------|
| **Doobie** | JDBC inayofanya kazi (athari ya paka) |
| **Mjanja** | Uhusiano wa kiutendaji |
| **Kielelezo** | Kusanya maswali yaliyonukuliwa ya muda |
| **Anorm** | Ufikiaji rahisi wa SQL (Cheza) |
| **Mcheshi** | PostgreSQL (athari ya paka, NIO) |
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

##Upimaji
| Mfumo | Kusudi |
|-----------|---------|
| **MUni** | Rahisi, ya kisasa (inapendekezwa) |
| **ScalaTest** | Feature-tajiri, mitindo mingi |
| **Mfumaji** | Inafanya kazi, isiyobadilika |
| **munit-paka-athari** | Upimaji wa athari za paka |
| **mockito-scala** | Mzaha |
| **Scalacheck** | Upimaji kulingana na mali |
| **majaribio-scala** | Ujumuishaji wa msingi wa Docker |
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

## Ubora wa Kanuni
| Zana | Kusudi |
|------|----------|
| **scaafmt** | Uumbizaji wa msimbo |
| **scalafix** | Uwekaji na urekebishaji upya |
| **WartRemover** | Linter ya wakati wa kukusanya |
| **mbuzi wa Azazeli** | Uchambuzi tuli |
| **sbt-tpolecat** | Chaguzi kali za mkusanyaji |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## Maktaba Zinazofanya Kazi za Kuandaa
| Maktaba | Kusudi |
|---------|---------|
| **Paka** | Vifupisho vya kazi (aina ya madarasa) |
| **Athari ya Paka** | IO monad, async wakati wa kukimbia |
| **ZIO** | Mfumo wa madoido, mfumo kamili wa ikolojia |
| **Bila umbo** | Utayarishaji wa kawaida (Scala 2) |
| **Paka** | Mifano ya aina inayotokana |
| **Monocle** | Maktaba ya macho |
---

## Maktaba Muhimu
| Maktaba | Kusudi |
|---------|---------|
| **Mzunguko** | Maktaba ya JSON (paka) |
| **upickle** | Usajili wa JSON |
| **ZIO JSON** | Haraka JSON (ZIO) |
| **fs2** | Mitiririko inayofanya kazi |
| **Tapir** | Aina-salama za mwisho za API |
| **Caliban** | Seva ya GraphQL |
| **Log4cats** | Uwekaji miti unaofanya kazi |
| **Kataa** | Uchanganuzi wa hoja ya CLI |
| **Michezo** | Aina-salama kiasi |
| **Enumeratum** | Enum zilizoimarishwa |
---

## Vitambulisho na Vihariri
| ID | Nguvu |
|-----|------------|
| **IntelliJ IDEA + programu-jalizi ya Scala** | IDE bora ya Scala |
| **Vyuma** | Seva ya lugha (wahariri wengi) |
| **VS Code + Vyuma** | Nyepesi na LSP |
| **Neovim + Vyuma** | Kulingana na terminal |
---

## Usambazaji
| Mbinu | Vidokezo |
|--------|-------|
| **NYUZI NZURI** | `sbt assembly`|
| **Docker** | Miundo ya hatua nyingi |
| **Mzaliwa wa GraalVM** | Picha asili (mdogo) |
| **Kubernetes** | Okestra |
| **AWS EMR** | Cheche kwenye AWS |
| **matofali ya data** | Jukwaa la cheche |
---

## Muhtasari
Mfumo wa ikolojia wa Scala unahusisha biashara, upangaji programu, na data kubwa. Rafu ya kawaida ni: **sbt** kwa miundo, **Scala 3** kwa lugha, **http4s + cats-effect** au **ZIO** kwa huduma zinazofanya kazi za wavuti, **Doobie** au **Slick** kwa ufikiaji wa hifadhidata, **MUnit** ya majaribio, **scalafmt** ya uumbizaji, na **IntelliJ + Metal support. Scala inatawala katika data kubwa (Apache Spark imeandikwa kwa Scala), utiririshaji (Mitiririko ya Pekko), na popote utendaji wa JVM hukutana na utendakazi wa programu. Sintaksia safi zaidi ya Scala 3, enum, na aina za makutano hufanya lugha ifikike zaidi.