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
# Scala - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم اسکالا را پوشش می‌دهد.
---

## نسخه‌ها و زمان‌های اجرا Scala
| نسخه | یادداشت ها |
|---------|-------|
| **اسکالا 3** | فعلی، نحو تمیز، ویژگی های جدید |
| **اسکالا 2.13** | به طور گسترده استفاده می شود، بالغ |
| **Scala.js** | کامپایل به جاوا اسکریپت |
| **اسکالا نیتیو** | کامپایل به کد بومی |
| **JVM** | زمان اجرا اولیه (جاوا interop) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## ابزارهای ساخت
| ابزار | نوع | بهترین برای |
|------|------|----------|
| **sbt** | استاندارد | اکثر پروژه های اسکالا |
| **آسیاب** | مدرن | پیکربندی سریع و ساده تر |
| **گرادل** | جاوا interop | جاوا/اسکالای مختلط |
| **اسکالا-کلی** | سبک | اسکریپت، پروژه های کوچک |
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

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **http4s** | عملکردی | نوع ایمن HTTP (اثر گربه ها) |
| **Pekko HTTP** | بازیگر محور | آپاچی پکو (چنگال آکا) |
| **فریم ورک بازی** | تمام پشته | برنامه های وب واکنشی |
| **ZIO HTTP** | مبتنی بر ZIO | عملکردی با کارایی بالا |
| **فیناترا** | توییتر | میکروسرویس |
| **تپیر** | نقطه پایانی DSL | توضیحات API ایمن نوع |
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

## مهندسی داده های بزرگ و داده ها
| فناوری | هدف |
|------------|---------|
| **آپاچی اسپارک** | پردازش داده های توزیع شده (Scala-native) |
| **آپاچی کافکا** | پخش رویداد (کلینت اسکالا) |
| **Apache Flink** | پردازش جریان |
| **آپاچی پکو استریمز** | جریان های واکنشی |
| **آکا استریمز** | جریان های واکنشی (میراث) |
| **علمی** | Google Cloud Dataflow (Spotify) |
| **Vulcan** | تکامل طرحواره Avro |
---

## پایگاه داده و ORM
| فناوری | نوع |
|------------|------|
| **دوبی** | JDBC کاربردی (اثر گربه ها) |
| **لیک** | تابعی رابطه ای |
| **کویل** | پرس و جوهای نقل شده در زمان کامپایل |
| **ناهنجار** | دسترسی ساده SQL (بازی) |
| **اسکانک** | PostgreSQL (cats-effect، NIO) |
| **کالیبان** | GraphQL |
| **سنگریا** | GraphQL |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **MUnit** | ساده، مدرن (توصیه می شود) |
| **ScalaTest** | دارای ویژگی های غنی، سبک های متعدد |
| **بافنده** | عملکردی، تغییرناپذیر |
| **مونیت-گربه-اثر** | تست اثر گربه |
| **mockito-scala** | تمسخر |
| **اسکالچک** | تست مبتنی بر اموال |
| **testcontainers-scala** | ادغام مبتنی بر داکر |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **scalafmt** | قالب بندی کد |
| **اسکالفیکس** | پرده سازی و بازسازی |
| **Wart Remover** | لینتر زمان کامپایل |
| **بزغاله** | تجزیه و تحلیل استاتیک |
| **sbt-tpolecat** | گزینه های دقیق کامپایلر |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## کتابخانه های برنامه نویسی کاربردی
| کتابخانه | هدف |
|---------|---------|
| **گربه** | انتزاعات تابعی (کلاس های نوع) |
| **اثر گربه** | IO monad، زمان اجرا غیر همگام |
| **ZIO** | سیستم اثر، اکوسیستم کامل |
| **بی شکل** | برنامه نویسی عمومی (Scala 2) |
| **گربه** | نمونه های کلاس نوع مشتق شده |
| **مونوکل** | کتابخانه اپتیک |
---

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **سیرسه** | کتابخانه JSON (گربه ها) |
| **پیکل** | سریال سازی JSON |
| **ZIO JSON** | سریع JSON (ZIO) |
| **fs2** | جریان های کاربردی |
| **تپیر** | نقاط پایانی API ایمن نوع |
| **کالیبان** | سرور GraphQL |
| **Log4cats** | ورود به سیستم عملکردی |
| **رد ** | تجزیه آرگومان CLI |
| **اسکوانت** | مقادیر ایمن نوع |
| **Enumeratum** | enums پیشرفته |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| ** افزونه IntelliJ IDEA + Scala** | بهترین Scala IDE |
| **فلزات** | سرور زبان (چند ویرایشگر) |
| **VS Code + Metals** | سبک با LSP |
| **Neovim + Metals** | مبتنی بر ترمینال |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **شیشه چربی** | `sbt assembly`|
| **داکر** | ساخت های چند مرحله ای |
| **GraalVM Native** | تصویر بومی (محدود) |
| **Kubernetes** | ارکستراسیون |
| **AWS EMR** | جرقه در AWS |
| **داده های** | سکوی جرقه |
---

## خلاصه
اکوسیستم اسکالا شامل سازمانی، برنامه نویسی کاربردی و کلان داده است. پشته استاندارد عبارتند از: **sbt** برای ساخت‌ها، **Scala 3** برای زبان، **http4s + cats-effect** یا **ZIO** برای سرویس‌های وب کاربردی، **Doobie** یا **Slick** برای دسترسی به پایگاه داده، **MUnit** برای آزمایش، **scalafmt** برای قالب‌بندی، و پشتیبانی از I DE. Scala در کلان داده ها (Apache Spark در Scala نوشته شده است)، استریمینگ (Pekko Streams) و هر جایی که عملکرد JVM با برنامه نویسی کاربردی مطابقت داشته باشد، غالب است. نحو تمیزتر Scala 3، enums و انواع تقاطع، زبان را قابل دسترس تر می کند.