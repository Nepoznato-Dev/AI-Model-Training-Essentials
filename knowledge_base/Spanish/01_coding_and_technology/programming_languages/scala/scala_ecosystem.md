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
# Scala: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema Scala.
---

## Versiones y tiempos de ejecución de Scala
| Versión | Notas |
|---------|-------|
| **Escala 3** | Sintaxis limpia y actual, nuevas funciones |
| **Escala 2.13** | Ampliamente utilizado, maduro |
| **Scala.js** | Compilar en JavaScript |
| **Scala nativo** | Compilar en código nativo |
| **JVM** | Tiempo de ejecución principal (interoperabilidad de Java) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## Herramientas de construcción
| Herramienta | Tipo | Mejor para |
|------|------|----------|
| **sbt** | Estándar | La mayoría de los proyectos de Scala |
| **Molino** | Moderno | Configuración rápida y sencilla |
| **Gradle** | Interoperabilidad de Java | Java/Scala mixtos |
| **scala-cli** | Ligero | Guiones, pequeños proyectos |
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

## Marcos web
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **http4s** | Funcional | HTTP con seguridad de tipos (efecto gatos) |
| **Pekko HTTP** | Basado en actores | Apache Pekko (bifurcación Akka) |
| **Marco de juego** | Pila completa | Aplicaciones web reactivas |
| **ZIO HTTP** | Basado en ZIO | Funcional, de alto rendimiento |
| **Finatra** | Gorjeo | Microservicios |
| **Tapir** | DSL de punto final | Descripciones de API con seguridad de tipos |
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

## Big Data e ingeniería de datos
| Tecnología | Propósito |
|------------|---------|
| **Apache Chispa** | Procesamiento de datos distribuidos (nativo de Scala) |
| **Apache Kafka** | Transmisión de eventos (cliente Scala) |
| **Apache Flink** | Procesamiento de flujo |
| **Transmisiones de Apache Pekko** | Corrientes reactivas |
| **Corrientes Akka** | Corrientes reactivas (heredadas) |
| **Scio** | Flujo de datos de la nube de Google (Spotify) |
| **Vulcano** | Evolución del esquema Avro |
---

## Base de datos y ORM
| Tecnología | Tipo |
|------------|------|
| **Doobie** | JDBC funcional (efecto gato) |
| **Resbaladizo** | Relacional funcional |
| **Pluma** | Consultas citadas en tiempo de compilación |
| **Norma** | Acceso SQL simple (Reproducir) |
| **Zorrillo** | PostgreSQL (efecto gatos, NIO) |
| **Calibán** | GráficoQL |
| **Sangría** | GráficoQL |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **Unidad MU** | Sencillo, moderno (recomendado) |
| **Prueba Scala** | Rico en funciones, muchos estilos |
| **Tejedor** | Funcional, inmutable |
| **efecto-gatos-munit** | Pruebas del efecto de los gatos |
| **mockito-scala** | Burlarse |
| **scalacheck** | Pruebas basadas en propiedades |
| **contenedores de prueba-scala** | Integración basada en Docker |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **escalafmt** | Formato de código |
| **scalafix** | Linting y refactorización |
| **Removedor de verrugas** | Linter en tiempo de compilación |
| **chivo expiatorio** | Análisis estático |
| **sbt-tpolecat** | Opciones estrictas del compilador |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## Bibliotecas de programación funcional
| Biblioteca | Propósito |
|---------|---------|
| **Gatos** | Abstracciones funcionales (clases de tipos) |
| **Efecto Gatos** | Mónada IO, tiempo de ejecución asíncrono |
| **ZIO** | Sistema de efectos, ecosistema completo |
| **Sin forma** | Programación genérica (Scala 2) |
| **Gatitos** | Instancias de clases de tipos derivados |
| **Monóculo** | Biblioteca de óptica |
---

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **Circe** | Biblioteca JSON (gatos) |
| **upickle** | Serialización JSON |
| **ZIO JSON** | JSON rápido (ZIO) |
| **fs2** | Corrientes funcionales |
| **Tapir** | Puntos finales API con seguridad de tipos |
| **Calibán** | Servidor GraphQL |
| **Log4cats** | Registro funcional |
| **Rechazar** | Análisis de argumentos CLI |
| **Squants** | Cantidades de tipo seguro |
| **Enumeración** | Enumeraciones mejoradas |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **IntelliJ IDEA + complemento Scala** | Mejor IDE de Scala |
| **Metales** | Servidor de idiomas (multieditor) |
| **Código VS + Metales** | Ligero con LSP |
| **Neovim + Metales** | Basado en terminal |
---

## Implementación
| Método | Notas |
|--------|-------|
| **TARRO gordo** | `sbt assembly`|
| **Acoplador** | Construcciones de varias etapas |
| **GraalVM Nativo** | Imagen nativa (limitada) |
| **Kubernetes** | Orquestación |
| **AWS EMR** | Chispa en AWS |
| **Ladrillos de datos** | Plataforma chispa |
---

## Resumen
El ecosistema de Scala abarca programación empresarial, funcional y big data. La pila estándar es: **sbt** para compilaciones, **Scala 3** para el lenguaje, **http4s + cats-effect** o **ZIO** para servicios web funcionales, **Doobie** o **Slick** para acceso a bases de datos, **MUnit** para pruebas, **scalafmt** para formateo e **IntelliJ + Metals** para compatibilidad con IDE. Scala domina en big data (Apache Spark está escrito en Scala), streaming (Pekko Streams) y en cualquier lugar donde el rendimiento de JVM se combine con la programación funcional. La sintaxis, las enumeraciones y los tipos de intersección más limpios de Scala 3 hacen que el lenguaje sea más accesible.