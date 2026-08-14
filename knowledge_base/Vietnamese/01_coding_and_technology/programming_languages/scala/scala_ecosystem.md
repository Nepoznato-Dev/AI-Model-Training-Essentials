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
# Scala — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái Scala.
---

## Phiên bản Scala & Thời gian chạy
| Phiên bản | Ghi chú |
|----------|-------|
| **Scala 3** | Cú pháp hiện tại, rõ ràng, tính năng mới |
| **Scala 2.13** | Được sử dụng rộng rãi, trưởng thành |
| **Scala.js** | Biên dịch sang JavaScript |
| **Scala gốc** | Biên dịch sang mã gốc |
| **JVM** | Thời gian chạy chính (tương tác Java) |
```bash
scala -version            # check version
scala-cli run main.scala  # run with scala-cli
scala repl                # interactive REPL
```

---

## Công cụ xây dựng
| Công cụ | Loại | Tốt nhất cho |
|------|------|----------|
| **sbt** | Tiêu chuẩn | Hầu hết các dự án Scala |
| **Nhà máy** | Hiện đại | Cấu hình nhanh, đơn giản hơn |
| **Cấp độ** | Tương tác Java | Hỗn hợp Java/Scala |
| **scala-cli** | Nhẹ | Kịch bản, dự án nhỏ |
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

## Khung web
| Khung | Loại | Tốt nhất cho |
|----------|------|----------|
| **http4s** | Chức năng | HTTP an toàn loại (hiệu ứng mèo) |
| **Pekko HTTP** | Dựa trên diễn viên | Apache Pekko (ngã ba Akka) |
| **Khung chơi** | Toàn ngăn xếp | Ứng dụng web phản ứng |
| **ZIO HTTP** | Dựa trên ZIO | Chức năng, hiệu suất cao |
| **Finatra** | Twitter | Dịch vụ vi mô |
| **Tapir** | DSL điểm cuối | Mô tả API an toàn loại |
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

## Dữ liệu lớn & Kỹ thuật dữ liệu
| Công nghệ | Mục đích |
|----------||---------|
| **Tia lửa Apache** | Xử lý dữ liệu phân tán (Scala-native) |
| **Apache Kafka** | Truyền phát sự kiện (máy khách Scala) |
| **Liên kết Apache** | Xử lý luồng |
| **Luồng Apache Pekko** | Luồng phản ứng |
| **Dòng Akka** | Luồng phản ứng (cũ) |
| **Khoa học** | Luồng dữ liệu đám mây của Google (Spotify) |
| **Vulcan** | Tiến hóa lược đồ Avro |
---

## Cơ sở dữ liệu & ORM
| Công nghệ | Loại |
|----------||------|
| **Doobie** | JDBC chức năng (hiệu ứng mèo) |
| **Bóng bẩy** | Quan hệ chức năng |
| **Quỳnh** | Truy vấn được trích dẫn tại thời điểm biên dịch |
| **Anorm** | Truy cập SQL đơn giản (Play) |
| **Chồn hôi** | PostgreSQL (hiệu ứng mèo, NIO) |
| **Caliban** | Đồ thịQL |
| **Sangria** | Đồ thịQL |
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

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **MĐơn vị** | Đơn giản, hiện đại (được khuyến nghị) |
| **ScalaTest** | Tính năng phong phú, nhiều phong cách |
| **Thợ dệt** | Chức năng, bất biến |
| **munit-mèo-hiệu ứng** | Thử nghiệm hiệu ứng mèo |
| **mockito-scala** | Chế giễu |
| **kiểm tra quy mô** | Thử nghiệm dựa trên tài sản |
| **testcontainer-scala** | Tích hợp dựa trên Docker |
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

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| **scafmt** | Định dạng mã |
| **scalafix** | Linting và tái cấu trúc |
| **Loại bỏ mụn cóc** | Kẻ nói dối thời gian biên dịch |
| **vật tế thần** | Phân tích tĩnh |
| **sbt-tpolecat** | Tùy chọn trình biên dịch nghiêm ngặt |
```scala
// .scalafmt.conf
version = "3.8.0"
runner.dialect = scala3
maxColumn = 120
align.preset = more
```

---

## Thư viện lập trình chức năng
| Thư viện | Mục đích |
|----------|----------|
| **Mèo** | Trừu tượng chức năng (loại lớp) |
| **Hiệu ứng Mèo** | Đơn nguyên IO, thời gian chạy không đồng bộ |
| **ZIO** | Hệ thống hiệu ứng, hệ sinh thái đầy đủ |
| **Vô hình** | Lập trình chung (Scala 2) |
| **Mèo con** | Các thể hiện của lớp loại dẫn xuất |
| **Một mắt** | Thư viện quang học |
---

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **Circe** | Thư viện JSON (mèo) |
| **căng thẳng** | Tuần tự hóa JSON |
| **ZIO JSON** | JSON nhanh (ZIO) |
| **fs2** | Luồng chức năng |
| **Tapir** | Điểm cuối API an toàn loại |
| **Caliban** | Máy chủ GraphQL |
| **Log4cats** | Ghi nhật ký chức năng |
| **Từ chối** | Phân tích đối số CLI |
| **nghiêng lưng** | Số lượng an toàn loại |
| **Đếm** | enum nâng cao |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **Plugin IntelliJ IDEA + Scala** | IDE Scala tốt nhất |
| **Kim loại** | Máy chủ ngôn ngữ (đa biên tập) |
| **Mã VS + Kim loại** | Nhẹ với LSP |
| **Nevim + Kim loại** | Dựa trên thiết bị đầu cuối |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **JAR béo** | `sbt assembly`|
| **Docker** | Xây dựng nhiều giai đoạn |
| **Bản địa GraalVM** | Hình ảnh gốc (có giới hạn) |
| **Kubernetes** | Dàn nhạc |
| **AWS EMR** | Spark trên AWS |
| **Databricks** | Nền tảng Spark |
---

## Bản tóm tắt
Hệ sinh thái của Scala bao gồm doanh nghiệp, lập trình chức năng và dữ liệu lớn. Ngăn xếp tiêu chuẩn là: **sbt** cho các bản dựng, **Scala 3** cho ngôn ngữ, **http4s + cats-effect** hoặc **ZIO** cho các dịch vụ web chức năng, **Doobie** hoặc **Slick** để truy cập cơ sở dữ liệu, **MUnit** để thử nghiệm, **scalafmt** để định dạng và **IntelliJ + Metals** để hỗ trợ IDE. Scala thống trị về dữ liệu lớn (Apache Spark được viết bằng Scala), phát trực tuyến (Pekko Streams) và bất cứ nơi nào hiệu suất JVM đáp ứng được lập trình chức năng. Cú pháp, enum và kiểu giao cắt rõ ràng hơn của Scala 3 làm cho ngôn ngữ trở nên dễ tiếp cận hơn.