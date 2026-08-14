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
# Scala — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz Scala ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Scala Sürümleri ve Çalışma Zamanları
| Sürüm | Notlar |
|-----------|----------|
| **Skala 3** | Güncel, temiz sözdizimi, yeni özellikler |
| **Skala 2.13** | Yaygın olarak kullanılan, olgun |
| **Scala.js** | JavaScript'e Derle |
| **Scala Yerlisi** | Yerel koda derleme |
| **JVM** | Birincil çalışma zamanı (Java birlikte çalışma) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## Oluşturma Araçları
| Araç | Tür | En İyisi |
|------|----------|----------|
| **sbt** | Standart | Çoğu Scala projesi |
| **Değirmen** | Modern | Hızlı, daha basit yapılandırma |
| **Kepçe** | Java birlikte çalışma | Karma Java/Scala |
| **scala-cli** | Hafif | Komut dosyaları, küçük projeler |
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

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **http4'ler** | Fonksiyonel | Tür açısından güvenli HTTP (kedi etkisi) |
| **Pekko HTTP** | Aktör bazlı | Apache Pekko (Akka çatalı) |
| **Oyun Çerçevesi** | Tam yığın | Reaktif web uygulamaları |
| **ZIO HTTP** | ZIO tabanlı | Fonksiyonel, yüksek performanslı |
| **Finatra** | Heyecan | Mikro hizmetler |
| **Tapir** | Uç Nokta DSL | Tür açısından güvenli API açıklamaları |
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

## Büyük Veri ve Veri Mühendisliği
| Teknoloji | Amaç |
|---------------|-----------|
| **Apache Spark** | Dağıtılmış veri işleme (Scala-yerel) |
| **Apache Kafka** | Olay akışı (Scala istemcisi) |
| **Apache Flink** | Akış işleme |
| **Apache Pekko Yayınları** | Reaktif akışlar |
| **Akka Akarsuları** | Reaktif akışlar (eski) |
| **Scio** | Google Bulut Veri Akışı (Spotify) |
| **Vulkan** | Avro şema gelişimi |
---

## Veritabanı ve ORM
| Teknoloji | Tür |
|---------------|------|
| **Doobie** | İşlevsel JDBC (kedi efekti) |
| **kaygan** | İşlevsel ilişkisel |
| **Tüyrek** | Derleme zamanında alıntılanan sorgular |
| **Anormallik** | Basit SQL erişimi (Oynat) |
| **Kokarca** | PostgreSQL (kedi etkisi, NIO) |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **Birim** | Basit, modern (önerilen) |
| **ScalaTest** | Zengin özelliklere sahip, birçok stil |
| **Dokumacı** | İşlevsel, değişmez |
| **munit-kedi etkisi** | Kedi etkisi testi |
| **mockito-scala** | Alaycı |
| **scalacheck** | Mülkiyet bazlı testler |
| **testcontainers-scala** | Docker tabanlı entegrasyon |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **scalafmt** | Kod biçimlendirme |
| **scalafix** | Linting ve yeniden düzenleme |
| **Siğil Giderici** | Derleme zamanı linter |
| **günah keçisi** | Statik analiz |
| **sbt-tpolecat** | Sıkı derleyici seçenekleri |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## Fonksiyonel Programlama Kütüphaneleri
| Kütüphane | Amaç |
|-----------|-----------|
| **Kediler** | İşlevsel soyutlamalar (tip sınıfları) |
| **Kediler Etkisi** | IO monad, eşzamansız çalışma zamanı |
| **ZIO** | Efekt sistemi, tam ekosistem |
| **Şekilsiz** | Genel programlama (Scala 2) |
| **Yavru kediler** | Türetilmiş tür sınıfı örnekleri |
| **Tek gözlük** | Optik kütüphanesi |
---

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **Çember** | JSON kitaplığı (kediler) |
| **turşu** | JSON serileştirme |
| **ZIO JSON** | Hızlı JSON (ZIO) |
| **fs2** | İşlevsel akışlar |
| **Tapir** | Tür açısından güvenli API uç noktaları |
| **Caliban** | GraphQL sunucusu |
| **Log4cats** | İşlevsel günlük kaydı |
| **Reddet** | CLI bağımsız değişkeni ayrıştırma |
| **boğuluyor** | Tip güvenli miktarlar |
| **Sıralama** | Gelişmiş numaralandırmalar |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **IntelliJ IDEA + Scala eklentisi** | En İyi Scala IDE |
| **Metaller** | Dil sunucusu (çoklu düzenleyici) |
| **VS Kodu + Metaller** | LSP ile Hafif |
| **Neovim + Metaller** | Terminal tabanlı |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Şişman JAR** | `sbt assembly`|
| **Docker** | Çok aşamalı yapılar |
| **GraalVM Yerel** | Yerel resim (sınırlı) |
| **Kubernetes** | Orkestrasyon |
| **AWS EMR** | AWS'de Spark |
| **Databricks** | Kıvılcım platformu |
---

## Özet
Scala'nın ekosistemi kurumsal, işlevsel programlama ve büyük verileri kapsar. Standart yığın şu şekildedir: derlemeler için **sbt**, dil için **Scala 3**, işlevsel web hizmetleri için **http4s + cats-fect** veya **ZIO**, veritabanı erişimi için **Doobie** veya **Slick**, test için **MUnit**, biçimlendirme için **scalafmt** ve IDE desteği için **IntelliJ + Metals**. Scala, büyük veride (Apache Spark, Scala'da yazılmıştır), akışta (Pekko Streams) ve JVM performansının işlevsel programlamayla buluştuğu her yerde hakimdir. Scala 3'ün daha temiz sözdizimi, numaralandırmaları ve kesişim türleri dili daha ulaşılabilir hale getirir.