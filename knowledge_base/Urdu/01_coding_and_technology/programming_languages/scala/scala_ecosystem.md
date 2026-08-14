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

# اسکیلا - ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ Scala ایکو سسٹم میں ضروری ٹولز، فریم ورک، اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## اسکیلا ورژنز اور رن ٹائمز
| ورژن | نوٹس |
|---------|---------|
| **اسکالہ 3** | موجودہ، صاف نحو، نئی خصوصیات |
| **اسکالہ 2.13** | بڑے پیمانے پر استعمال کیا جاتا ہے، بالغ |
| **Scala.js** | جاوا اسکرپٹ پر مرتب کریں |
| **اسکالا مقامی** | مقامی کوڈ پر مرتب کریں |
| **JVM** | پرائمری رن ٹائم (جاوا انٹراپ) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## ٹولز بنائیں
| ٹول | قسم | کے لیے بہترین |
|------|------|---------|
| **sbt** | معیاری | زیادہ تر اسکیلا پروجیکٹس |
| **مل** | جدید | تیز، آسان ترتیب |
| **گریڈل** | جاوا انٹراپ | مخلوط Java/Scala |
| **scala-cli** | ہلکا پھلکا | سکرپٹ، چھوٹے منصوبے |
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

## ویب فریم ورک
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **http4s** | فنکشنل | ٹائپ سیف HTTP (بلیوں کا اثر) |
| **Pekko HTTP** | اداکار پر مبنی | اپاچی پیکو (اکا کانٹا) |
| **پلے فریم ورک** | مکمل اسٹیک | ری ایکٹیو ویب ایپس |
| **ZIO HTTP** | ZIO پر مبنی | فنکشنل، اعلی کارکردگی |
| **فناترا** | ٹویٹر | مائیکرو سروسز |
| **تاپر** | اختتامی نقطہ DSL | ٹائپ سیف API کی تفصیل |
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

## بگ ڈیٹا اور ڈیٹا انجینئرنگ
| ٹیکنالوجی | مقصد |
|------------|---------|
| **اپاچی اسپارک** | تقسیم شدہ ڈیٹا پروسیسنگ (اسکالا مقامی) |
| **اپاچی کافکا** | ایونٹ اسٹریمنگ (اسکالا کلائنٹ) |
| **اپاچی فلنک** | سٹریم پروسیسنگ |
| **اپاچی پیکو اسٹریمز** | رد عمل کے سلسلے |
| **اکا اسٹریمز** | رد عمل والے سلسلے (وراثت) |
| **Scio** | Google Cloud Dataflow (Spotify) |
| **ولکن** | ایورو سکیما ارتقاء |
---

## ڈیٹا بیس اور ORM
| ٹیکنالوجی | قسم |
|------------|------|
| **ڈوبی** | فنکشنل JDBC (بلیوں کا اثر) |
| **سلک** | فنکشنل رشتہ دار |
| **کوئل** | مرتب وقت کے حوالے سے سوالات |
| **انورم** | سادہ SQL رسائی (پلے) |
| **سکنک** | PostgreSQL (بلیوں کا اثر، NIO) |
| **کیلیبان** | گراف کیو ایل |
| **سانگریہ** | گراف کیو ایل |
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

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **MUnit** | سادہ، جدید (تجویز کردہ) |
| **ScalaTest** | خصوصیت سے بھرپور، بہت سے انداز |
| **ویور** | فعال، ناقابل تغیر |
| **munit-cats-effect** | کیٹس ایفیکٹ ٹیسٹنگ |
| **موکیٹو اسکیلا** | طنز |
| ** اسکیل چیک** | جائیداد کی بنیاد پر جانچ |
| ** testcontainers-scala** | ڈاکر پر مبنی انضمام |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **scalafmt** | کوڈ فارمیٹنگ |
| **اسکالافکس** | لنٹنگ اور ریفیکٹرنگ |
| **وارٹ ریموور** | مرتب وقت لنٹر |
| **قربانی کا بکرا** | جامد تجزیہ |
| **sbt-tpolecat** | سخت کمپائلر اختیارات |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## فنکشنل پروگرامنگ لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **بلیاں** | فنکشنل تجریدات (قسم کی کلاسز) |
| **بلیوں کا اثر** | IO monad، async رن ٹائم |
| **ZIO** | اثر کا نظام، مکمل ماحولیاتی نظام |
| **بے ​​شکل** | عام پروگرامنگ (Scala 2) |
| **بلی کے بچے** | ماخوذ قسم کی کلاس مثالیں |
| **مونوکل** | آپٹکس لائبریری |
---

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **سرس** | JSON لائبریری (بلیوں) |
| **اچار** | JSON سیریلائزیشن |
| **ZIO JSON** | فاسٹ JSON (ZIO) |
| **fs2** | فنکشنل اسٹریمز |
| **تاپر** | ٹائپ سیف API اینڈ پوائنٹس |
| **کیلیبان** | گراف کیو ایل سرور |
| **Log4cats** | فنکشنل لاگنگ |
| **انکار** | CLI دلیل کی تجزیہ |
| **سکونٹس** | ٹائپ سیف مقداریں |
| ** گنتی** | بہتر enums |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **IntelliJ IDEA + Scala پلگ ان** | بہترین اسکیلا IDE |
| ** دھاتیں** | زبان کا سرور (ملٹی ایڈیٹر) |
| **VS کوڈ + دھاتیں** | LSP کے ساتھ ہلکا پھلکا |
| **نیوم + دھاتیں** | ٹرمینل پر مبنی |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **موٹی جار** | `sbt assembly`|
| **ڈوکر** | ملٹی اسٹیج بناتا ہے |
| **GraalVM مقامی** | مقامی تصویر (محدود) |
| **Kubernetes** | آرکیسٹریشن |
| **AWS EMR** | AWS پر چنگاری |
| **ڈیٹا برکس** | چنگاری پلیٹ فارم |
---

## خلاصہ
Scala کا ماحولیاتی نظام انٹرپرائز، فنکشنل پروگرامنگ، اور بڑے ڈیٹا پر محیط ہے۔ معیاری اسٹیک یہ ہے: تعمیرات کے لیے **sbt**، زبان کے لیے **Scala 3**، **http4s + cats-effect** یا **ZIO** فنکشنل ویب سروسز کے لیے، **Doobie** یا **Slick** ڈیٹابیس تک رسائی کے لیے، **MUnit** ٹیسٹنگ کے لیے، **scalafmt** فارمیٹنگ کے لیے، اور ID+E کے لیے سپورٹ +** بڑے ڈیٹا (Apache Spark Scala میں لکھا جاتا ہے)، سٹریمنگ (Pekko Streams)، اور کہیں بھی JVM کی کارکردگی فنکشنل پروگرامنگ سے ملتی ہے۔ Scala 3 کی کلینر ترکیب، enums، اور intersection کی قسمیں زبان کو زیادہ قابل رسائی بناتی ہیں۔