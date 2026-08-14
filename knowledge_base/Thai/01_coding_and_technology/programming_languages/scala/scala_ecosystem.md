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

# Scala - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่จำเป็นในระบบนิเวศ Scala
---

## เวอร์ชันและรันไทม์ของ Scala
| เวอร์ชั่น | หมายเหตุ |
|---------|-------|
| **สกาล่า 3** | ปัจจุบัน ไวยากรณ์ที่สะอาด คุณลักษณะใหม่ |
| **สกาล่า 2.13** | ใช้กันอย่างแพร่หลาย เป็นผู้ใหญ่ |
| **Scala.js** | คอมไพล์เป็น JavaScript |
| **สกาล่าพื้นเมือง** | คอมไพล์เป็นโค้ดเนทีฟ |
| **เจวีเอ็ม** | รันไทม์หลัก (Java interop) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## สร้างเครื่องมือ
| เครื่องมือ | พิมพ์ | ดีที่สุดสำหรับ |
|------|-|---------|
| **sbt** | มาตรฐาน | โครงการ Scala ส่วนใหญ่ |
| **โรงสี** | ทันสมัย ​​| รวดเร็วและง่ายกว่าการกำหนดค่า |
| **เกรเดิล** | การทำงานร่วมกันของ Java | Java/Scala แบบผสม |
| **สกาลา-cli** | น้ำหนักเบา | สคริปต์โปรเจ็กต์ขนาดเล็ก |
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

## กรอบงานเว็บ
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **http4s** | ฟังก์ชั่น | HTTP แบบปลอดภัย (เอฟเฟกต์แมว) |
| **เพกโกะ HTTP** | ตามนักแสดง | Apache Pekko (อาก้า ส้อม) |
| **กรอบการเล่น** | เต็มกอง | แอปพลิเคชันเว็บแบบโต้ตอบ |
| **ZIO HTTP** | ที่ใช้ ZIO | ฟังก์ชันประสิทธิภาพสูง |
| **ฟินาตร้า** | ทวิตเตอร์ | ไมโครเซอร์วิส |
| **สมเสร็จ** | จุดสิ้นสุด DSL | คำอธิบาย API ที่ปลอดภัยสำหรับประเภท |
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

## ข้อมูลขนาดใหญ่และวิศวกรรมข้อมูล
| เทคโนโลยี | วัตถุประสงค์ |
|------------|---------|
| **Apache Spark** | การประมวลผลข้อมูลแบบกระจาย (Scala-native) |
| **Apache Kafka** | การสตรีมเหตุการณ์ (ไคลเอนต์ Scala) |
| **Apache Flink** | การประมวลผลสตรีม |
| **Apache Pekko Streams** | กระแสปฏิกิริยา |
| **อักก้าสตรีม** | กระแสปฏิกิริยา (ดั้งเดิม) |
| **วิทยาศาสตร์** | Google Cloud Dataflow (Spotify) |
| **วัลแคน** | วิวัฒนาการสคีรรว์ |
---

## ฐานข้อมูลและ ORM
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **ดูบี้** | JDBC ที่ใช้งานได้ (เอฟเฟกต์แมว) |
| **เนียน** | เชิงฟังก์ชัน |
| **ปากกาขนนก** | แบบสอบถามที่ยกมาเวลาคอมไพล์ |
| **ผิดปกติ** | การเข้าถึง SQL อย่างง่าย (เล่น) |
| **สกั๊งค์** | PostgreSQL (เอฟเฟกต์แมว, NIO) |
| **คาลิบาน** | GraphQL |
| **แซงเกรีย** | GraphQL |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **หน่วย** | เรียบง่าย ทันสมัย ​​(แนะนำ) |
| **สกาล่าเทส** | หลากหลายสไตล์ |
| **ช่างทอผ้า** | ใช้งานได้จริงไม่เปลี่ยนรูป |
| **munit-แมว-เอฟเฟกต์** | การทดสอบผลกระทบของแมว |
| **ม็อคโต-สกาล่า** | ล้อเลียน |
| **สกาลาเช็ค** | การทดสอบตามคุณสมบัติ |
| **testcontainers-สกาล่า** | การบูรณาการโดยใช้นักเทียบท่า |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **scalafmt** | การจัดรูปแบบโค้ด |
| **สกาลาฟิกซ์** | Linting และการปรับโครงสร้างใหม่ |
| **กำจัดหูด** | linter เวลาคอมไพล์ |
| **แพะรับบาป** | การวิเคราะห์แบบคงที่ |
| **sbt-tpolecat** | ตัวเลือกคอมไพเลอร์ที่เข้มงวด |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## ไลบรารีการเขียนโปรแกรมเชิงฟังก์ชัน
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **แมว** | นามธรรมเชิงฟังก์ชัน (คลาสประเภท) |
| **เอฟเฟ็กต์แมว** | IO monad, รันไทม์แบบอะซิงก์ |
| **ซีไอโอ** | ระบบเอฟเฟกต์ระบบนิเวศเต็มรูปแบบ |
| **ไร้รูปทรง** | การเขียนโปรแกรมทั่วไป (Scala 2) |
| **ลูกแมว** | อินสแตนซ์คลาสประเภทที่ได้รับ |
| **แว่นข้างเดียว** | ห้องสมุดทัศนศาสตร์ |
---

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **เซอร์ซี** | ไลบรารี JSON (แมว) |
| **อูพิเคิล** | การทำให้เป็นอนุกรม JSON |
| **ZIO JSON** | JSON ที่รวดเร็ว (ZIO) |
| **fs2** | กระแสการทำงาน |
| **สมเสร็จ** | จุดสิ้นสุด API ที่ปลอดภัยสำหรับประเภท |
| **คาลิบาน** | เซิร์ฟเวอร์ GraphQL |
| **Log4cats** | การบันทึกการทำงาน |
| **ปฏิเสธ** | การแยกวิเคราะห์อาร์กิวเมนต์ CLI |
| **นั่งยองๆ** | ปริมาณที่ปลอดภัยต่อการพิมพ์ |
| **แจงนับ** | ปรับปรุง enums |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **ปลั๊กอิน IntelliJ IDEA + Scala** | สุดยอด Scala IDE |
| **โลหะ** | เซิร์ฟเวอร์ภาษา (ตัวแก้ไขหลายตัว) |
| **VS Code + โลหะ** | น้ำหนักเบาด้วย LSP |
| **นีโอวิม + โลหะ** | บนเทอร์มินัล |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **จาร์อ้วน** | `sbt assembly`|
| **นักเทียบท่า** | การสร้างแบบหลายขั้นตอน |
| **GraalVM เนทิฟ** | รูปภาพดั้งเดิม (จำกัด ) |
| **Kubernetes** | การเรียบเรียง |
| **AWS EMR** | จุดประกายบน AWS |
| **ดาต้าบริคส์** | แพลตฟอร์มสปาร์ค |
---

## สรุป
ระบบนิเวศของ Scala ครอบคลุมทั้งระดับองค์กร การเขียนโปรแกรมเชิงฟังก์ชัน และข้อมูลขนาดใหญ่ สแต็กมาตรฐานคือ: **sbt** สำหรับบิลด์, **Scala 3** สำหรับภาษา, **http4s + เอฟเฟกต์แมว** หรือ **ZIO** สำหรับบริการเว็บที่ใช้งานได้, **Doobie** หรือ **Slick** สำหรับการเข้าถึงฐานข้อมูล, **MUnit** สำหรับการทดสอบ, **scalafmt** สำหรับการจัดรูปแบบ และ **IntelliJ + Metals** สำหรับการรองรับ IDE Scala ครอบงำข้อมูลขนาดใหญ่ (Apache Spark เขียนด้วย Scala) การสตรีม (Pekko Streams) และทุกที่ที่ประสิทธิภาพของ JVM ตรงตามการเขียนโปรแกรมเชิงฟังก์ชัน ไวยากรณ์ที่สะอาดกว่า การแจงนับ และประเภททางแยกของ Scala 3 ทำให้ภาษาเข้าถึงได้ง่ายขึ้น