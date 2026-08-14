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

# Scala — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Scala.
---

## Versi & Waktu Proses Scala
| Versi | Catatan |
|---------|-------|
| **Skala 3** | Sintaks terkini dan bersih, fitur baru |
| **Skala 2.13** | Banyak digunakan, dewasa |
| **Scala.js** | Kompilasi ke JavaScript |
| **Scala Asli** | Kompilasi ke kode asli |
| **JVM** | Waktu proses utama (interop Java) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## Alat Bangun
| Alat | Ketik | Terbaik Untuk |
|------|------|----------|
| **sbt** | Standar | Sebagian besar proyek Scala |
| **Pabrik** | Modern | Konfigurasi cepat dan sederhana |
| **Kelas** | Interop Java | Campuran Java/Scala |
| **scala-cli** | Ringan | Skrip, proyek kecil |
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

## Kerangka Web
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **http4s** | Fungsional | HTTP aman-ketik (efek kucing) |
| **Pekko HTTP** | Berbasis aktor | Apache Pekko (garpu Akka) |
| **Mainkan Kerangka** | Tumpukan penuh | Aplikasi web reaktif |
| **ZIOHTTP** | berbasis ZIO | Fungsional, berkinerja tinggi |
| **Finatra** | Twitter | Layanan mikro |
| **Tapir** | DSL Titik Akhir | Deskripsi API yang aman untuk tipe |
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

## Data Besar & Rekayasa Data
| Teknologi | Tujuan |
|------------|---------|
| **Apache Spark** | Pemrosesan data terdistribusi (Scala-asli) |
| **Apache Kafka** | Streaming acara (klien Scala) |
| **Apache Flink** | Pemrosesan aliran |
| **Aliran Apache Pekko** | Aliran reaktif |
| **Aliran Akka** | Aliran reaktif (warisan) |
| **Ilmu Pengetahuan** | Aliran Data Google Cloud (Spotify) |
| **Vulkan** | Evolusi skema Avro |
---

## Basis Data & ORM
| Teknologi | Ketik |
|------------|------|
| **Doobie** | JDBC fungsional (efek kucing) |
| **licin** | Relasional fungsional |
| **Pena bulu** | Kueri yang dikutip waktu kompilasi |
| **Anorm** | Akses SQL sederhana (Putar) |
| **Sigung** | PostgreSQL (efek kucing, NIO) |
| **Kaliban** | GrafikQL |
| **Sangria** | GrafikQL |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **Unit** | Sederhana, modern (disarankan) |
| **Tes Scala** | Kaya fitur, banyak gaya |
| **Penenun** | Fungsional, tidak dapat diubah |
| **efek-munit-kucing** | Pengujian efek kucing |
| **mockito-scala** | Mengejek |
| **pemeriksaan skala** | Pengujian berbasis properti |
| **skala wadah uji** | Integrasi berbasis Docker |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **scalafmt** | Pemformatan kode |
| **perbaikan skala** | Linting dan pemfaktoran ulang |
| **Penghilang Kutil** | Linter waktu kompilasi |
| **kambing hitam** | Analisis statis |
| **sbt-tpolecat** | Opsi kompiler yang ketat |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## Perpustakaan Pemrograman Fungsional
| Perpustakaan | Tujuan |
|---------|---------|
| **Kucing** | Abstraksi fungsional (kelas tipe) |
| **Efek Kucing** | IO monad, waktu proses asinkron |
| **ZIO** | Sistem efek, ekosistem lengkap |
| **Tak Berbentuk** | Pemrograman generik (Scala 2) |
| **Anak Kucing** | Contoh kelas tipe turunan |
| **Monokel** | Perpustakaan optik |
---

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **Lingkaran** | Perpustakaan JSON (kucing) |
| **upickle** | Serialisasi JSON |
| **ZIO JSON** | JSON Cepat (ZIO) |
| **fs2** | Aliran fungsional |
| **Tapir** | Titik akhir API yang aman untuk tipe |
| **Kaliban** | Server GraphQL |
| **Log4cat** | Pencatatan fungsional |
| **Tolak** | Penguraian argumen CLI |
| **Jumlah** | Jumlah yang aman untuk tipe |
| **Pencacahan** | Enum yang ditingkatkan |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **IntelliJ IDEA + plugin Scala** | IDE Scala Terbaik |
| **Logam** | Server bahasa (multi-editor) |
| **Kode VS + Logam** | Ringan dengan LSP |
| **Neovim + Logam** | Berbasis terminal |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **JAR Gemuk** | `sbt assembly`|
| **Buruh pelabuhan** | Pembangunan multi-tahap |
| **GraalVM Asli** | Gambar asli (terbatas) |
| **Kubernetes** | Orkestrasi |
| **AWS ESDM** | Percikan di AWS |
| **Databricks** | Platform percikan |
---

## Ringkasan
Ekosistem Scala mencakup perusahaan, pemrograman fungsional, dan data besar. Tumpukan standarnya adalah: **sbt** untuk build, **Scala 3** untuk bahasa, **http4s + cat-effect** atau **ZIO** untuk layanan web fungsional, **Doobie** atau **Slick** untuk akses database, **MUnit** untuk pengujian, **scalafmt** untuk pemformatan, dan **IntelliJ + Metals** untuk dukungan IDE. Scala mendominasi data besar (Apache Spark ditulis dalam Scala), streaming (Pekko Streams), dan di mana pun kinerja JVM bertemu dengan pemrograman fungsional. Sintaks, enum, dan tipe persimpangan Scala 3 yang lebih bersih membuat bahasa ini lebih mudah didekati.