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
# Scala — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, frameworki i infrastrukturę w ekosystemie Scala.
---

## Wersje i środowiska wykonawcze Scala
| Wersja | Notatki |
|--------|-------|
| **Scala 3** | Obecna, czysta składnia, nowe funkcje |
| **Scala 2.13** | Powszechnie stosowane, dojrzałe |
| **Scala.js** | Kompiluj do JavaScript |
| **Natywna Scala** | Kompiluj do kodu natywnego |
| **JVM** | Podstawowe środowisko wykonawcze (interoperacja Java) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## Narzędzia do tworzenia
| Narzędzie | Wpisz | Najlepsze dla |
|------|------|--------------|
| **sb** | Standardowe | Większość projektów Scala |
| **Młyn** | Nowoczesne | Szybka, prostsza konfiguracja |
| **Stopnie** | Współpraca z Javą | Mieszana Java/Scala |
| **scala-cli** | Lekki | Skrypty, małe projekty |
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

## Struktury internetowe
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **http4s** | Funkcjonalne | Bezpieczny typ HTTP (efekt kotów) |
| **Pekko HTTP** | Oparta na aktorach | Apache Pekko (widelec Akka) |
| **Graj w Framework** | Pełny stos | Reaktywne aplikacje internetowe |
| **ZIO HTTP** | oparty na ZIO | Funkcjonalne, wydajne |
| **Finatra** | Twitterze | Mikrousługi |
| **Tapir** | Punkt końcowy DSL | Opisy API bezpiecznego typu |
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

## Big Data i inżynieria danych
| Technologia | Cel |
|------------|------------|
| **Iskra Apache** | Rozproszone przetwarzanie danych (natywna skala) |
| **Apache Kafka** | Przesyłanie strumieniowe zdarzeń (klient Scala) |
| **Apache Flink** | Przetwarzanie strumieniowe |
| **Strumienie Apache Pekko** | Strumienie reaktywne |
| **Strumienie Akki** | Strumienie reaktywne (starsze) |
| **Scio** | Przepływ danych w chmurze Google (Spotify) |
| **Wulkan** | Ewolucja schematu Avro |
---

## Baza danych i ORM
| Technologia | Wpisz |
|------------|------|
| **Doobie** | Funkcjonalny JDBC (efekt kota) |
| **Ślicznotka** | Funkcjonalne relacyjne |
| **Pióro** | Zapytania cytowane w czasie kompilacji |
| **Anorma** | Prosty dostęp SQL (Play) |
| **Skunk** | PostgreSQL (efekt kotów, NIO) |
| **Kaliban** | WykresQL |
| **Sangria** | WykresQL |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **MUjednostka** | Prosty, nowoczesny (zalecany) |
| **Test Scala** | Bogate w funkcje, wiele stylów |
| **Tkacz** | Funkcjonalne, niezmienne |
| **efekt-munit-cats** | Testowanie efektu kotów |
| **mockito-scala** | Kpiąco |
| **scalacheck** | Testowanie oparte na właściwościach |
| **testkontenery-scala** | Integracja oparta na Dockerze |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **skala** | Formatowanie kodu |
| **scalafix** | Linting i refaktoryzacja |
| **Usuwanie brodawek** | Linter w czasie kompilacji |
| **kozioł ofiarny** | Analiza statyczna |
| **sbt-tpolecat** | Ścisłe opcje kompilatora |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## Biblioteki programowania funkcjonalnego
| Biblioteka | Cel |
|--------|---------|
| **Koty** | Abstrakcje funkcjonalne (klasy typów) |
| **Efekt kota** | Monada IO, środowisko wykonawcze asynchroniczne |
| **ZIO** | System efektów, pełny ekosystem |
| **Bezkształtny** | Programowanie ogólne (Scala 2) |
| **Kotki** | Instancje klasy typu pochodnego |
| **Monokl** | Biblioteka optyki |
---

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **Cyrk** | Biblioteka JSON (koty) |
| **pikle** | Serializacja JSON |
| **ZIO JSON** | Szybki JSON (ZIO) |
| **fs2** | Strumienie funkcjonalne |
| **Tapir** | Punkty końcowe API z bezpiecznym typem |
| **Kaliban** | Serwer GraphQL |
| **Log4cats** | Logowanie funkcjonalne |
| **Odrzuć** | Analiza argumentów CLI |
| **Skwanty** | Ilości bezpieczne dla typu |
| **Wyliczenie** | Ulepszone wyliczenia |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **IntelliJ IDEA + wtyczka Scala** | Najlepsze IDE Scala |
| **Metale** | Serwer językowy (multiedytor) |
| **Kod VS + Metale** | Lekki z LSP |
| **Neovim + Metale** | Oparte na terminalu |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Gruby SŁOik** | `sbt assembly`|
| **Doker** | Kompilacje wieloetapowe |
| **Natywny GraalVM** | Obraz natywny (ograniczony) |
| **Kubernetes** | Orkiestracja |
| **AWS EMR** | Iskra na AWS |
| **Kostki danych** | Platforma Spark |
---

## Streszczenie
Ekosystem Scali obejmuje przedsiębiorstwa, programowanie funkcjonalne i duże zbiory danych. Standardowy stos to: **sbt** dla kompilacji, **Scala 3** dla języka, **http4s + cat-efekt** lub **ZIO** dla funkcjonalnych usług internetowych, **Doobie** lub **Slick** dla dostępu do bazy danych, **MUnit** dla testowania, **scalafmt** dla formatowania i **IntelliJ + Metals** dla obsługi IDE. Scala dominuje w big data (Apache Spark jest napisany w Scali), streamingu (Pekko Streams) i wszędzie tam, gdzie wydajność JVM spotyka się z programowaniem funkcjonalnym. Czystsza składnia, wyliczenia i typy przecięć Scali 3 sprawiają, że język jest bardziej przystępny.