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
# স্কালা — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি স্কালা ইকোসিস্টেমের প্রয়োজনীয় টুলস, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## স্কালা সংস্করণ এবং রানটাইম
| সংস্করণ | নোট |
|---------|---------|
| **স্ক্যালা 3** | বর্তমান, পরিষ্কার বাক্য গঠন, নতুন বৈশিষ্ট্য |
| **স্ক্যালা 2.13** | ব্যাপকভাবে ব্যবহৃত, পরিপক্ক |
| **Scala.js** | জাভাস্ক্রিপ্টে কম্পাইল |
| **স্ক্যালা নেটিভ** | নেটিভ কোডে কম্পাইল |
| **JVM** | প্রাথমিক রানটাইম (জাভা ইন্টারপ) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## বিল্ড টুলস
| টুল | প্রকার | জন্য সেরা |
|------|------|----------|
| **sbt** | স্ট্যান্ডার্ড | সর্বাধিক স্কালা প্রকল্প |
| **মিল** | আধুনিক | দ্রুত, সহজ কনফিগার |
| **গ্রেডল** | জাভা ইন্টারপ | মিশ্র জাভা/স্ক্যালা |
| **স্ক্যালা-ক্লি** | লাইটওয়েট | স্ক্রিপ্ট, ছোট প্রকল্প |
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

## ওয়েব ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **http4s** | কার্যকরী | টাইপ-সেফ HTTP (বিড়াল-প্রভাব) |
| **পেকো HTTP** | অভিনেতা ভিত্তিক | Apache Pekko (আক্কা কাঁটা) |
| **প্লে ফ্রেমওয়ার্ক** | ফুল-স্ট্যাক | প্রতিক্রিয়াশীল ওয়েব অ্যাপস |
| **ZIO HTTP** | ZIO-ভিত্তিক | কার্যকরী, উচ্চ-কর্মক্ষমতা |
| **ফিনাট্রা** | টুইটার | মাইক্রোসার্ভিস |
| **তাপির** | এন্ডপয়েন্ট DSL | টাইপ-নিরাপদ API বিবরণ |
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

## বিগ ডেটা এবং ডেটা ইঞ্জিনিয়ারিং
| প্রযুক্তি | উদ্দেশ্য |
|------------|---------|
| **অ্যাপাচি স্পার্ক** | বিতরণকৃত ডেটা প্রসেসিং (স্ক্যালা-নেটিভ) |
| **অ্যাপাচি কাফকা** | ইভেন্ট স্ট্রিমিং (স্ক্যালা ক্লায়েন্ট) |
| **অ্যাপাচি ফ্লিঙ্ক** | স্ট্রিম প্রক্রিয়াকরণ |
| **অ্যাপাচি পেকো স্ট্রীম** | প্রতিক্রিয়াশীল প্রবাহ |
| **আক্কা প্রবাহ** | প্রতিক্রিয়াশীল স্ট্রীম (উত্তরাধিকার) |
| **Scio** | Google ক্লাউড ডেটাফ্লো (Spotify) |
| **ভলকান** | অভ্র স্কিমা বিবর্তন |
---

## ডাটাবেস এবং ওআরএম
| প্রযুক্তি | প্রকার |
|------------|------|
| **ডুবি** | কার্যকরী JDBC (বিড়াল-প্রভাব) |
| **স্লিক** | ক্রিয়ামূলক সম্পর্কীয় |
| **কুইল** | কম্পাইল-সময় উদ্ধৃত প্রশ্ন |
| **অনর্ম** | সাধারণ এসকিউএল অ্যাক্সেস (প্লে) |
| **স্কঙ্ক** | PostgreSQL (cats-effect, NIO) |
| **ক্যালিবান** | গ্রাফকিউএল |
| **সাংরিয়া** | গ্রাফকিউএল |
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

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **MUnit** | সহজ, আধুনিক (প্রস্তাবিত) |
| **স্ক্যালাটেস্ট** | বৈশিষ্ট্য সমৃদ্ধ, অনেক শৈলী |
| **তাঁতি** | কার্যকরী, অপরিবর্তনীয় |
| **মুনিট-বিড়াল-প্রভাব** | বিড়াল-প্রভাব পরীক্ষা |
| **মকিটো-স্ক্যালা** | উপহাস |
| **স্কেলচেক** | সম্পত্তি ভিত্তিক পরীক্ষা |
| **পরীক্ষা কন্টেইনার-স্ক্যালা** | ডকার-ভিত্তিক ইন্টিগ্রেশন |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **স্ক্যাল্যাফমটি** | কোড ফরম্যাটিং |
| **স্ক্যালাফিক্স** | লিন্টিং এবং রিফ্যাক্টরিং |
| **ওয়ার্ট রিমুভার** | কম্পাইল-টাইম লিন্টার |
| **বলির পাঁঠা** | স্ট্যাটিক বিশ্লেষণ |
| **sbt-tpolecat** | কঠোর কম্পাইলার বিকল্প |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## কার্যকরী প্রোগ্রামিং লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **বিড়াল** | কার্যকরী বিমূর্ততা (টাইপ ক্লাস) |
| **বিড়াল প্রভাব** | IO monad, async রানটাইম |
| **ZIO** | প্রভাব সিস্টেম, সম্পূর্ণ বাস্তুতন্ত্র |
| **আকৃতিহীন** | জেনেরিক প্রোগ্রামিং (স্ক্যালা 2) |
| **বিড়ালছানা** | প্রাপ্ত টাইপ শ্রেণীর উদাহরণ |
| **মনোকল** | অপটিক্স লাইব্রেরি |
---

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **বৃত্ত** | JSON লাইব্রেরি (বিড়াল) |
| **পিকল** | JSON সিরিয়ালাইজেশন |
| **ZIO JSON** | দ্রুত JSON (ZIO) |
| **fs2** | কার্যকরী স্ট্রীম |
| **তাপির** | টাইপ-সেফ API এন্ডপয়েন্ট |
| **ক্যালিবান** | গ্রাফকিউএল সার্ভার |
| **Log4cats** | কার্যকরী লগিং |
| **অস্বীকৃতি** | CLI যুক্তি পার্সিং |
| **স্কোয়ান্টস** | টাইপ-নিরাপদ পরিমাণ |
| **গণনা** | বর্ধিত enums |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **IntelliJ IDEA + স্কালা প্লাগইন** | সেরা স্কালা IDE |
| **ধাতু** | ভাষা সার্ভার (মাল্টি-এডিটর) |
| **VS কোড + ধাতু** | LSP সহ লাইটওয়েট |
| **নিওভিম + ধাতু** | টার্মিনাল ভিত্তিক |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **ফ্যাট জার** | `sbt assembly`|
| **ডকার** | মাল্টি-স্টেজ বিল্ড |
| **GraalVM নেটিভ** | নেটিভ ইমেজ (সীমিত) |
| **কুবারনেটস** | অর্কেস্ট্রেশন |
| **AWS EMR** | AWS এ স্পার্ক |
| **ডেটাব্রিক্স** | স্পার্ক প্ল্যাটফর্ম |
---

## সারাংশ
স্কালার ইকোসিস্টেম এন্টারপ্রাইজ, কার্যকরী প্রোগ্রামিং এবং বড় ডেটাকে বিস্তৃত করে। স্ট্যান্ডার্ড স্ট্যাক হল: বিল্ডের জন্য **sbt**, ভাষার জন্য **Scala 3**, **http4s + cats-effect** বা **ZIO** কার্যকরী ওয়েব পরিষেবার জন্য, **Doobie** বা **Slick** ডাটাবেস অ্যাক্সেসের জন্য, **MUnit** পরীক্ষার জন্য, **scalafmt** ফরম্যাটিং-এর জন্য, এবং ID**E++E সমর্থনের জন্য। স্কালা বড় ডেটাতে আধিপত্য বিস্তার করে (অ্যাপাচি স্পার্ক স্কালায় লেখা হয়), স্ট্রিমিং (পেকো স্ট্রীমস) এবং যেকোনও জায়গায় JVM কর্মক্ষমতা কার্যকরী প্রোগ্রামিংয়ের সাথে মিলিত হয়। Scala 3 এর ক্লিনার সিনট্যাক্স, enums, এবং ইন্টারসেকশনের ধরন ভাষাটিকে আরও সহজলভ্য করে তোলে।