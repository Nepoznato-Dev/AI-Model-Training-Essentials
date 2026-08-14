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
# Scala — Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais do ecossistema Scala.
---

## Versões e tempos de execução do Scala
| Versão | Notas |
|--------|-------|
| **Escala 3** | Sintaxe atual e limpa, novos recursos |
| ** Escala 2.13 ** | Amplamente utilizado, maduro |
| **Scala.js** | Compilar para JavaScript |
| **Scala Nativo** | Compilar para código nativo |
| **JVM** | Tempo de execução primário (interoperabilidade Java) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## Ferramentas de construção
| Ferramenta | Tipo | Melhor para |
|------|------|----------|
| **sbt** | Padrão | A maioria dos projetos Scala |
| **Moinho** | Moderno | Configuração rápida e mais simples |
| **Gradle** | Interoperabilidade Java | Java/Scala misto |
| **scala-cli** | Leve | Scripts, pequenos projetos |
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

## Estruturas Web
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **http4s** | Funcional | HTTP de tipo seguro (efeito gatos) |
| **Pekko HTTP** | Baseado em ator | Apache Pekko (garfo Akka) |
| **Estrutura do jogo** | Pilha completa | Aplicativos web reativos |
| **ZIOHTTP** | Baseado em ZIO | Funcional, de alto desempenho |
| **Finatra** | Twitter | Microsserviços |
| **Anta** | Ponto final DSL | Descrições de API com segurança de tipo |
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

## Big Data e Engenharia de Dados
| Tecnologia | Finalidade |
|------------|---------|
| **Apache Spark** | Processamento de dados distribuídos (nativo de Scala) |
| **Apache Kafka** | Streaming de eventos (cliente Scala) |
| **Apache Flink** | Processamento de fluxo |
| **Transmissões do Apache Pekko** | Fluxos reativos |
| **Akka Streams** | Fluxos reativos (herdados) |
| **Scio** | Fluxo de dados do Google Cloud (Spotify) |
| **Vulcano** | Evolução do esquema Avro |
---

## Banco de dados e ORM
| Tecnologia | Tipo |
|------------|------|
| **Doobie** | JDBC funcional (efeito gatos) |
| **Liso** | Funcional relacional |
| **Pena** | Consultas citadas em tempo de compilação |
| **Anorma** | Acesso SQL simples (Play) |
| **gambá** | PostgreSQL (efeito gatos, NIO) |
| **Caliban** | GráficoQL |
| **Sangria** | GráficoQL |
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

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **MUunidade** | Simples, moderno (recomendado) |
| **ScalaTest** | Rico em recursos, muitos estilos |
| **Tecelão** | Funcional, imutável |
| **efeito munit-cats** | Teste de efeito de gatos |
| **mockito-scala** | Zombando |
| **scalacheck** | Testes baseados em propriedades |
| **testcontainers-scala** | Integração baseada em Docker |
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

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **escalafmt** | Formatação de código |
| **scalafix** | Linting e refatoração |
| **Removedor de verrugas** | Linter em tempo de compilação |
| **bode expiatório** | Análise estática |
| **sbt-tpolecat** | Opções restritas do compilador |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## Bibliotecas de programação funcional
| Biblioteca | Finalidade |
|--------|---------|
| **Gatos** | Abstrações funcionais (classes de tipo) |
| **Efeito Gatos** | Mônada IO, tempo de execução assíncrono |
| **ZIO** | Sistema de efeitos, ecossistema completo |
| **Sem forma** | Programação genérica (Scala 2) |
| **Gatinhos** | Instâncias de classe de tipo derivado |
| **Monóculo** | Biblioteca óptica |
---

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **Circe** | Biblioteca JSON (gatos) |
| **agitação** | Serialização JSON |
| **ZIO JSON** | JSON rápido (ZIO) |
| **fs2** | Fluxos funcionais |
| **Anta** | Terminais de API com segurança de tipo |
| **Caliban** | Servidor GraphQL |
| **Log4cats** | Registro funcional |
| **Declínio** | Análise de argumento CLI |
| **Squants** | Quantidades de tipo seguro |
| **Enumerato** | Enums aprimorados |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Plugin IntelliJ IDEA + Scala** | Melhor IDE Scala |
| **Metais** | Servidor de idiomas (multieditor) |
| **Código VS + Metais** | Leve com LSP |
| **Neovim + Metais** | Baseado em terminal |
---

## Implantação
| Método | Notas |
|-------|-------|
| **JAR de gordura** | `sbt assembly`|
| **Docker** | Construções em vários estágios |
| **GraalVM nativo** | Imagem nativa (limitada) |
| **Kubernetes** | Orquestração |
| **AWSEMR** | Faísca na AWS |
| **Tijolos de dados** | Plataforma Spark |
---

## Resumo
O ecossistema do Scala abrange programação empresarial, funcional e big data. A pilha padrão é: **sbt** para compilações, **Scala 3** para a linguagem, **http4s + cats-effect** ou **ZIO** para serviços web funcionais, **Doobie** ou **Slick** para acesso ao banco de dados, **MUnit** para testes, **scalafmt** para formatação e **IntelliJ + Metals** para suporte IDE. Scala domina big data (o Apache Spark é escrito em Scala), streaming (Pekko Streams) e em qualquer lugar em que o desempenho da JVM encontra a programação funcional. A sintaxe, enumerações e tipos de interseção mais limpos do Scala 3 tornam a linguagem mais acessível.