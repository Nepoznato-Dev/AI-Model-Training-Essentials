---
# Metadata
title: "Scala"
description: "Comprehensive reference for the Scala programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [scala, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Scala
Scala (Ngôn ngữ có thể mở rộng) là ngôn ngữ lập trình được biên dịch, gõ tĩnh, kết hợp các mô hình lập trình hướng đối tượng và chức năng. Được tạo bởi Martin Odersky và phát hành lần đầu tiên vào năm 2004, Scala chạy trên JVM (cũng là Scala.js cho JavaScript và Scala Native). Nó được thiết kế để giải quyết tính dài dòng của Java trong khi vẫn duy trì khả năng tương tác Java đầy đủ.
Scala là ngôn ngữ đằng sau Apache Spark (khung xử lý dữ liệu lớn) và nó được sử dụng rộng rãi trong kỹ thuật dữ liệu, hệ thống phân tán và dịch vụ phụ trợ. Các công ty như Twitter (nay là X), LinkedIn, Netflix và The Guardian đều sử dụng Scala.
---

## Tại sao Scala lại quan trọng
- **Chức năng + OOP kết hợp**: Kết hợp những gì tốt nhất của cả hai mô hình trong một ngôn ngữ duy nhất.
- **Súc tích**: Ít dài dòng hơn đáng kể so với Java — khớp mẫu, lớp chữ hoa chữ thường, suy luận kiểu.
- **Apache Spark**: Ngôn ngữ chính để xử lý dữ liệu lớn dựa trên Spark.
- **Hệ thống kiểu**: Các tính năng nâng cao như ẩn ý, ​​lớp kiểu và kiểu dữ liệu đại số.
- **Khả năng tương thích với JVM**: Sử dụng tất cả các thư viện Java; chạy trên cùng một JVM.
- **Akka / Pekko**: Framework phổ biến để xây dựng các hệ thống phân tán, đồng thời.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Độ phức tạp** | Ngôn ngữ có nhiều tính năng; có thể khó thành thạo | Bắt đầu với "những phần tốt"; tránh mã quá thông minh |
| **Số lần biên dịch** | Chậm hơn Java, đặc biệt với các kiểu phức tạp | Sử dụng trình biên dịch tăng dần (Bloop, sbt) |
| **Đường cong học tập** | Dốc hơn Java hoặc Python | Đầu tư thời gian; phần thưởng đáng kể |
| **Thị trường việc làm nhỏ hơn** | Ít vai trò hơn Java hoặc Python | Mạnh về kỹ thuật dữ liệu và vai trò phụ trợ |
| **Phong cách không nhất quán** | Các nhóm khác nhau viết Scala rất khác nhau | Thực hiện theo hướng dẫn về phong cách cộng đồng |
---

##Cơ bản về cú pháp
```scala
// Variables
val name = "Alice"        // Immutable
var count = 0             // Mutable

// Case classes — immutable data carriers with pattern matching
case class User(name: String, age: Int)

val user = User("Alice", 30)
user match {
  case User("Alice", age) => println(s"Alice is $age")
  case User(n, _) => println(s"User: $n")
}

// Collections and functional operations
val numbers = List(1, 2, 3, 4, 5)
val doubled = numbers.map(_ * 2)
val evens = numbers.filter(_ % 2 == 0)
val sum = numbers.reduce(_ + _)

// Option — avoid null
def findUser(id: Int): Option[User] = {
  if (id > 0) Some(User("Alice", 30)) else None
}

findUser(1) match {
  case Some(user) => println(user.name)
  case None => println("Not found")
}

// For-comprehensions (syntactic sugar for map/flatMap/withFilter)
val result = for {
  user <- findUser(1)
  if user.age >= 18
} yield user.name

// Traits (interfaces with implementations)
trait Animal {
  def name: String
  def speak(): String
}

class Dog(val name: String) extends Animal {
  def speak(): String = s"$name says woof"
}

// Implicit conversions and type classes (advanced)
implicit class StringOps(val s: String) extends AnyVal {
  def isEmail: Boolean = s.contains("@") && s.contains(".")
}
"alice@example.com".isEmail  // true
```

---

## Cú pháp & Mẫu nâng cao
### Loại các lớp (thông qua Ẩn ý)
Scala 2 sử dụng các tham số ngầm định để mã hóa các lớp kiểu. Scala 3 giới thiệu cú pháp`given`/`using`gốc.
```scala
// Scala 2 style: implicit-based type classes
trait Show[A] {
  def show(a: A): String
}

object Show {
  def apply[A](implicit ev: Show[A]): Show[A] = ev

  implicit val intShow: Show[Int] = (i: Int) => i.toString
  implicit val stringShow: Show[String] = (s: String) => s""""$s""""

  implicit def listShow[A](implicit sa: Show[A]): Show[List[A]] =
    (as: List[A]) => as.map(sa.show).mkString("[", ", ", "]")
}

object ShowSyntax {
  implicit class ShowOps[A](val a: A) extends AnyVal {
    def show(implicit sa: Show[A]): String = sa.show(a)
  }
}

import ShowSyntax._
42.show              // "42"
List(1, 2, 3).show   // "[1, 2, 3]"
```

```scala
// Scala 3 style: native type classes with given/using
trait Show[A]:
  def show(a: A): String

object Show:
  def apply[A](using ev: Show[A]): Show[A] = ev

  given Show[Int] with
    def show(a: Int): String = a.toString

  given Show[String] with
    def show(a: String): String = s""""$a""""

  given [A](using sa: Show[A]): Show[List[A]] with
    def show(as: List[A]): String = as.map(sa.show).mkString("[", ", ", "]")

extension [A](a: A)
  def show(using sa: Show[A]): String = sa.show(a)

42.show              // "42"
List(1, 2, 3).show   // "[1, 2, 3]"
```

### Các đặc điểm và liệt kê được niêm phong (Scala 3 Enums)
```scala
// Scala 3 enums — algebraic data types
enum Color:
  case Red, Green, Blue
  case Custom(r: Int, g: Int, b: Int)

  def hex: String = this match
    case Red => "#FF0000"
    case Green => "#00FF00"
    case Blue => "#0000FF"
    case Custom(r, g, b) => f"#$r%02X$g%02X$b%02X"

// Sealed trait hierarchy with exhaustiveness checking
sealed trait PaymentResult
case class Success(transactionId: String) extends PaymentResult
case class Failure(reason: String, retryable: Boolean) extends PaymentResult
case object Pending extends PaymentResult

def handlePayment(result: PaymentResult): String = result match
  case Success(txId) => s"Payment successful: $txId"
  case Failure(reason, _) => s"Payment failed: $reason"
  case Pending => "Payment pending"
  // Compiler warns if any case is missing
```

### Tính năng hệ thống loại nâng cao
```scala
// Dependent types with path-dependent types
trait Database:
  type Record
  def find(id: String): Option[Record]
  def insert(record: Record): Unit

val pg: Database = new PostgresDB
val record: pg.Record = pg.find("user-1").get  // type depends on pg instance

// Type-level programming with match types (Scala 3)
type Elem[X] = X match
  case String => Char
  case List[t] => t
  case Array[t] => t

type Test1 = Elem[String]   // Char
type Test2 = Elem[List[Int]] // Int

// Extension methods (Scala 3)
extension (s: String)
  def isEmail: Boolean = s.contains("@") && s.contains(".")
  def words: List[String] = s.split("\\s+").toList

"hello world".words  // List("hello", "world")

// Opaque types for zero-cost abstractions (Scala 3)
object UserId:
  opaque type UserId = Long
  def apply(value: Long): UserId = value
  extension (id: UserId)
    def value: Long = id

val userId = UserId(42L)  // Type-safe, no runtime overhead
```

---

## Đồng thời & Song song
### Tương lai và lời hứa
```scala
import scala.concurrent.{Future, Promise}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration._
import scala.util.{Success, Failure}

// Basic Future usage
val futureResult: Future[Int] = Future {
  Thread.sleep(1000) // Simulate work
  42
}

futureResult.onComplete {
  case Success(value) => println(s"Got: $value")
  case Failure(ex) => println(s"Failed: ${ex.getMessage}")
}

// Composing futures with for-comprehensions
def fetchUser(id: Int): Future[String] = Future { s"User-$id" }
def fetchOrders(user: String): Future[List[String]] = Future {
  List(s"$user-order-1", s"$user-order-2")
}

val userOrders: Future[List[String]] = for {
  user <- fetchUser(1)
  orders <- fetchOrders(user)
} yield orders

// Combining multiple futures
val futures: List[Future[Int]] = (1 to 10).map(i => Future(i * 2)).toList
val allResults: Future[List[Int]] = Future.sequence(futures)

// Timeout handling
import scala.concurrent.Await
val result = Await.result(futureResult, 5.seconds)
```

### ZIO — Hệ thống hiệu ứng hiện đại
```scala
import zio._

// ZIO effects: ZIO[Env, Err, Success]
val readLine: ZIO[Any, Nothing, String] =
  Console.readLine.orDie

val greet: ZIO[Any, Nothing, Unit] = for {
  name <- readLine
  _ <- Console.printLine(s"Hello, $name!")
} yield ()

// Error handling with typed errors
sealed trait AppError
case class NotFound(id: String) extends AppError
case class Unauthorized(msg: String) extends AppError

def findUser(id: String): ZIO[Any, NotFound, String] =
  if (id.nonEmpty) ZIO.succeed(s"User-$id")
  else ZIO.fail(NotFound(id))

// Fiber-based concurrency
val program: ZIO[Any, Nothing, (Int, Int)] = for {
  fiber1 <- ZIO.succeed(42).fork
  fiber2 <- ZIO.succeed(84).fork
  r1 <- fiber1.join
  r2 <- fiber2.join
} yield (r1, r2)

// Resource safety with ZIO.acquireRelease
def withDatabase[A](use: Database => ZIO[Any, Throwable, A]) =
  ZIO.acquireRelease(
    Database.connect("localhost")
  )(db => db.close.orDie).flatMap(use)
```

### Diễn viên Akka/Pekko
```scala
import org.apache.pekko.actor.typed.{ActorSystem, Behavior}
import org.apache.pekko.actor.typed.scaladsl.{Behaviors, ActorContext}

// Define messages
sealed trait Command
case class Greet(name: String, replyTo: ActorRef[Greeted]) extends Command
case class Greeted(from: String, message: String)

// Define actor behavior
object Greeter:
  def apply(): Behavior[Command] = Behaviors.receive { (context, message) =>
    message match
      case Greet(name, replyTo) =>
        context.log.info(s"Greeting $name")
        replyTo ! Greeted("Greeter", s"Hello, $name!")
        Behaviors.same
  }

// Spawn and communicate
val system: ActorSystem[Command] = ActorSystem(Greeter(), "greeter-system")
```


---

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án (sbt)
```
my-scala-project/
├── project/
│   ├── build.properties       # sbt version
│   ├── plugins.sbt            # sbt plugins
│   └── Dependencies.scala     # Dependency definitions
├── src/
│   ├── main/
│   │   ├── scala/
│   │   │   └── com/example/
│   │   │       ├── Main.scala
│   │   │       ├── models/
│   │   │       └── services/
│   │   └── resources/
│   │       └── application.conf
│   └── test/
│       └── scala/
│           └── com/example/
│               └── services/
├── build.sbt                  # Main build definition
├── .scalafmt.conf             # Code formatter config
└── README.md
```

### Cấu hình bản dựng (build.sbt)
```scala
// build.sbt
val scala3Version = "3.3.1"

lazy val root = project
  .in(file("."))
  .settings(
    name := "my-scala-project",
    version := "0.1.0-SNAPSHOT",
    scalaVersion := scala3Version,

    // Compiler options
    scalacOptions ++= Seq(
      "-deprecation",
      "-feature",
      "-unchecked",
      "-Xfatal-warnings",
      "-Wunused:all"
    ),

    // Dependencies
    libraryDependencies ++= Seq(
      "org.typelevel" %% "cats-core" % "2.10.0",
      "dev.zio" %% "zio" % "2.0.19",
      "dev.zio" %% "zio-http" % "3.0.0-RC2",
      "com.typesafe" % "config" % "1.4.3",
      "ch.qos.logback" % "logback-classic" % "1.4.11",

      // Test dependencies
      "org.scalatest" %% "scalatest" % "3.2.17" % Test,
      "org.scalacheck" %% "scalacheck" % "1.17.0" % Test,
      "dev.zio" %% "zio-test" % "2.0.19" % Test,
      "dev.zio" %% "zio-test-sbt" % "2.0.19" % Test
    ),

    // Test framework
    testFrameworks += new TestFramework("zio.test.sbt.ZTestFramework")
  )
```

### Lệnh xây dựng chính
| Lệnh | Mô tả |
|----------|-------------|
| `sbt new scala/scala3.g8`| Tạo dự án Scala 3 mới từ mẫu |
| `sbt compile`| Tổng hợp nguồn chính |
| `sbt test`| Chạy tất cả các bài kiểm tra |
| `sbt run`| Chạy lớp chính |
| `sbt runMain com.example.App`| Chạy một lớp chính cụ thể |
| `sbt console`| Bắt đầu REPL với dự án trên đường dẫn lớp |
| `sbt clean`| Đầu ra được biên dịch sạch |
| `sbt assembly`| Xây dựng JAR béo (với plugin sbt-assembly) |
| `sbt scalafmt`| Mã định dạng với Scalafmt |
| `sbt scalafmtCheck`| Kiểm tra định dạng mã |
| `sbt ~compile`| Biên dịch liên tục (biên dịch lại khi thay đổi) |
### Định dạng mã (.scalafmt.conf)
```
# .scalafmt.conf
version = 3.7.14
runner.dialect = scala3
maxColumn = 100
align.preset = more
continuationIndent.defnSite = 2
assumeStandardLibraryStripMargin = true
docstrings.style = Asterisk
lineEndings = preserve
indentOperator.topLevelOnly = true
```

### Đường dẫn CI/CD (Hành động trên GitHub)
```yaml
# .github/workflows/scala.yml
name: Scala CI
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup JDK
        uses: actions/setup-java@v3
        with:
          distribution: temurin
          java-version: '21'
          cache: sbt

      - name: Setup sbt
        uses: sbt/setup-sbt@v1

      - name: Compile
        run: sbt compile

      - name: Format Check
        run: sbt scalafmtCheck

      - name: Test
        run: sbt test

      - name: Package
        run: sbt assembly
```


---

##Thử nghiệm
### ScalaTest — Kiểm tra toàn diện
```scala
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers
import org.scalatest.wordspec.AnyWordSpec

// FlatSpec style (BDD-like)
class CalculatorSpec extends AnyFlatSpec with Matchers {
  "A Calculator" should "add two numbers" in {
    Calculator.add(2, 3) shouldBe 5
  }

  it should "handle negative numbers" in {
    Calculator.add(-1, -2) shouldBe -3
  }

  it should "throw on overflow" in {
    an [ArithmeticException] should be thrownBy {
      Calculator.add(Int.MaxValue, 1)
    }
  }
}

// WordSpec style
class UserServiceSpec extends AnyWordSpec with Matchers {
  "UserService" when {
    "finding an existing user" should {
      "return Some(user)" in {
        val service = new UserService()
        service.find(1) shouldBe Some(User("Alice", 30))
      }
    }
    "finding a non-existent user" should {
      "return None" in {
        val service = new UserService()
        service.find(-1) shouldBe None
      }
    }
  }
}
```

### ScalaCheck — Kiểm tra dựa trên thuộc tính
```scala
import org.scalatest.flatspec.AnyFlatSpec
import org.scalatestplus.scalacheck.ScalaCheckPropertyChecks
import org.scalacheck.{Gen, Prop, Arbitrary}

class PropertySpec extends AnyFlatSpec with ScalaCheckPropertyChecks {

  // Simple property
  "List.reverse" should "be involutive" in {
    forAll { (xs: List[Int]) =>
      xs.reverse.reverse shouldBe xs
    }
  }

  // Custom generators
  val genEmail: Gen[String] = for {
    user <- Gen.alphaLowerStr.suchThat(_.nonEmpty)
    domain <- Gen.alphaLowerStr.suchThat(_.nonEmpty)
  } yield s"$user@$domain.com"

  "Email validation" should "accept valid emails" in {
    forAll(genEmail) { email =>
      EmailValidator.isValid(email) shouldBe true
    }
  }

  // Conditional properties
  "Sorted list" should "maintain length" in {
    forAll { (xs: List[Int]) =>
      xs.nonEmpty ==> (xs.sorted.length == xs.length)
    }
  }
}
```

###Kiểm tra ZIO
```scala
import zio.test._
import zio.test.Assertion._

object CalculatorSpec extends ZIOSpecDefault {
  def spec = suite("Calculator")(
    test("adds two numbers") {
      assert(Calculator.add(2, 3))(equalTo(5))
    },
    test("handles zero") {
      assert(Calculator.add(0, 5))(equalTo(5))
    },
    test("handles negative numbers") {
      assert(Calculator.add(-3, 7))(equalTo(4))
    }
  )
}
```

---

## Khả năng tương tác
### Khả năng tương tác JVM
Scala có quyền truy cập liền mạch vào tất cả các thư viện Java.
```scala
// Using Java classes directly
import java.time.{LocalDate, Duration}
import java.util.concurrent.ConcurrentHashMap
import java.io.{File, BufferedReader, FileReader}

val today = LocalDate.now()
val file = new File("/tmp/data.txt")

// Using Java collections and converting
import scala.jdk.CollectionConverters._

val javaMap = new ConcurrentHashMap[String, Int]()
javaMap.put("a", 1)
val scalaMap: Map[String, Int] = javaMap.asScala.toMap

val javaList = java.util.Arrays.asList(1, 2, 3)
val scalaList: List[Int] = javaList.asScala.toList

// Calling Java static methods
val encoded = java.util.Base64.getEncoder.encodeToString("hello".getBytes)

// Exposing Scala to Java
object ScalaUtils {
  // @static makes methods callable as Java static methods
  def process(data: String): String = data.toUpperCase
}
// Java: ScalaUtils.process("hello");
```

### Tương tác gốc (Scala Native)
```scala
// Scala Native — compile to native code without JVM
import scala.scalanative.unsafe._
import scala.scalanative.libc.stdio._

// Call C functions
@extern
object MyCLib {
  def custom_function(x: CInt): CInt = extern
}

Zone { implicit z =>
  val cString: CString = toCString("Hello from Scala Native")
  printf(c"%s\n", cString)
  val result = MyCLib.custom_function(42)
}
```


---

## Mẫu thiết kế
### Trận chung kết không gắn thẻ với Mèo
```scala
import cats.Monad
import cats.implicits._

// Define algebra (interface) as a type class
trait UserRepository[F[_]] {
  def findById(id: Long): F[Option[User]]
  def save(user: User): F[Unit]
  def delete(id: Long): F[Boolean]
}

// Business logic is polymorphic over the effect
class UserService[F[_]: Monad](repo: UserRepository[F]) {
  def promoteUser(id: Long): F[Either[String, User]] =
    repo.findById(id).flatMap {
      case None => Monad[F].pure(Left("User not found"))
      case Some(user) =>
        val promoted = user.copy(role = "admin")
        repo.save(promoted).map(_ => Right(promoted))
    }
}

// Live implementation (IO-based)
import cats.effect.IO

class LiveUserRepository extends UserRepository[IO] {
  def findById(id: Long): IO[Option[User]] =
    IO(database.query(s"SELECT * FROM users WHERE id = $id"))
  def save(user: User): IO[Unit] =
    IO(database.execute(s"INSERT INTO users ..."))
  def delete(id: Long): IO[Boolean] =
    IO(database.execute(s"DELETE FROM users WHERE id = $id"))
}

// Test implementation (pure, no IO)
import cats.Id

class TestUserRepository(data: Map[Long, User]) extends UserRepository[Id] {
  def findById(id: Long): Option[User] = data.get(id)
  def save(user: User): Unit = ()
  def delete(id: Long): Boolean = data.contains(id)
}
```

### Mẫu lớp ZIO
```scala
import zio._

// Define a service
trait UserService {
  def findById(id: Long): Task[Option[User]]
  def save(user: User): Task[Unit]
}

object UserService {
  // Accessor methods
  def findById(id: Long): ZIO[UserService, Throwable, Option[User]] =
    ZIO.serviceWithZIO[UserService](_.findById(id))

  // Live implementation as a Layer
  val live: ZLayer[Database, Nothing, UserService] =
    ZLayer.fromFunction((db: Database) => new UserServiceLive(db))
}

// Compose layers to build the application
val appLayer: ZLayer[Any, Throwable, UserService] =
  Database.live >>> UserService.live

// Run the application
val program: ZIO[UserService, Throwable, Unit] = for {
  user <- UserService.findById(1L)
  _ <- ZIO.foreach(user)(u => Console.printLine(s"Found: ${u.name}"))
} yield ()

program.provideLayer(appLayer)
```

### Mẫu kho lưu trữ có xử lý lỗi
```scala
import cats.data.EitherT
import cats.effect.IO

sealed trait AppError
case class NotFound(entity: String, id: Long) extends AppError
case class DatabaseError(cause: Throwable) extends AppError
case class ValidationError(message: String) extends AppError

type AppResult[A] = EitherT[IO, AppError, A]

class OrderService(repo: OrderRepository[IO]) {
  def placeOrder(order: Order): AppResult[OrderConfirmation] =
    for {
      _ <- EitherT.fromOption[IO](
        validate(order), ValidationError("Invalid order")
      )
      saved <- EitherT(repo.save(order).map(_.toRight(DatabaseError(
        new RuntimeException("Save failed")
      ))))
      confirmation = OrderConfirmation(saved.id, saved.total)
    } yield confirmation

  private def validate(order: Order): Option[Unit] =
    if (order.items.nonEmpty && order.total > 0) Some(()) else None
}
```

---

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
| Công cụ | Mục đích | Cách sử dụng |
|------|----------|-------|
| **JMH** | Đo điểm chuẩn vi mô |  Plugin`sbt-jmh`|
| **VisualVM** | Lập hồ sơ và giám sát JVM |  Lệnh`jvisualvm`|
| **Trình hồ sơ không đồng bộ** | Cấu hình CPU/bộ nhớ có chi phí thấp | Đính kèm với JVM đang chạy |
| **Bộ công cụ của bạn** | Hồ sơ thương mại | Tích hợp IDE |
| **phạm vi bảo hiểm sbt** | Bảo hiểm mã | `sbt coverage test coverageReport`|
### Đo điểm chuẩn với JMH
```scala
// Add to plugins.sbt: addSbtPlugin("pl.project13.scala" % "sbt-jmh" % "0.4.6")
import org.openjdk.jmh.annotations._

@State(Scope.Thread)
class CollectionBenchmark {
  @Param(Array("100", "1000", "10000"))
  var size: Int = _

  var data: List[Int] = _

  @Setup
  def setup(): Unit = {
    data = (1 to size).toList
  }

  @Benchmark
  def listSum: Int = data.sum

  @Benchmark
  def vectorSum: Int = data.toVector.sum

  @Benchmark
  def arraySum: Int = data.toArray.sum
}

// Run: sbt "Jmh/run -i 5 -wi 3 -f1"
```

### Kỹ thuật tối ưu hóa
```scala
// 1. Use Vector for indexed access (not List)
val vec = Vector(1, 2, 3, 4, 5)  // O(log32 n) access
val lst = List(1, 2, 3, 4, 5)    // O(n) access for index

// 2. Use lazy collections for expensive pipelines
val result = (1 to 1000000).iterator
  .filter(_ % 2 == 0)
  .map(_ * 3)
  .take(10)
  .toList

// 3. Avoid unnecessary boxing with @specialized
def max[@specialized(Int, Long, Double) T: Ordering](a: T, b: T): T =
  if (Ordering[T].compare(a, b) >= 0) a else b

// 4. Use parallel collections for CPU-bound work
val parallelSum = (1 to 1000000).par.map(_ * 2).sum

// 5. Use value classes to avoid allocations
extension (value: Long)
  def toUserId: UserId = UserId(value)
```

---

## Triển khai
### Xây dựng JAR béo
```scala
// project/plugins.sbt
addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.1.4")

// build.sbt
assembly / mainClass := Some("com.example.Main")
assembly / assemblyJarName := "my-app.jar"

// Merge strategy for conflicts
assembly / assemblyMergeStrategy := {
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case "reference.conf" => MergeStrategy.concat
  case x => MergeStrategy.first
}
```

### Triển khai Docker
```dockerfile
# Multi-stage build
FROM eclipse-temurin:21-jdk AS builder
WORKDIR /app
COPY . .
RUN sbt assembly

FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=builder /app/target/scala-3.3.1/my-app.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### Hình ảnh gốc GraalVM
```scala
// build.sbt — enable Scala Native or use GraalVM
// For GraalVM native-image:
// native-image --static -jar target/scala-3.3.1/my-app.jar -o my-app
```

---

## Khi nào nên sử dụng Scala
| Kịch bản | Tại sao Scala | Thay thế tốt hơn |
|----------|----------|-------------------|
| Dữ liệu lớn (Spark) | Ngôn ngữ Spark chính | Python (PySpark) cho các quy trình đơn giản hơn |
| Hệ thống phân tán (Akka) | Khung đồng thời trưởng thành | Đi, Erlang/Elixir |
| Phụ trợ JVM | Thay thế Java ngắn gọn | Java, Kotlin |
| Lập trình chức năng trên JVM | Sự kết hợp FP + JVM tốt nhất | Clojure |
| Phát triển ứng dụng chung | Có thể nhưng phức tạp | Python, Go, Java |
| Khoa học dữ liệu | Có thể nhưng không phải hệ sinh thái | Python, R |
---

## Hỏi đáp tổng hợp
### Q1: Suy luận kiểu của Scala giảm bản mẫu soạn sẵn như thế nào so với Java?
**A:** Trình biên dịch của Scala suy ra các kiểu cho khai báo`val`/ `var`, kiểu trả về phương thức và hàm ẩn danh. Điều này giúp loại bỏ sự cần thiết của các chú thích kiểu rõ ràng trong hầu hết các trường hợp:
```scala
// Java: explicit types everywhere
Map<String, List<Integer>> grouped = new HashMap<>();
// Scala: types inferred
val grouped = items.groupBy(_.category)
```

Trình biên dịch cũng suy ra các tham số kiểu, trả về kiểu của phương thức biểu thức đơn và kiểu khớp mẫu. Điều này làm cho mã ngắn gọn mà không ảnh hưởng đến sự an toàn.
### Câu 2: Khi nào tôi nên sử dụng`case class`so với`class`thông thường?
**Đáp:** Sử dụng`case class`cho các vật mang dữ liệu bất biến — chúng tự động cung cấp`equals`,`hashCode`,`toString`,`copy`và hỗ trợ khớp mẫu:
```scala
// Data carrier — case class
case class Point(x: Double, y: Double)
val p = Point(1, 2)
val moved = p.copy(x = 10)

// Behavior-rich — regular class
class Counter {
  private var count = 0
  def increment(): Unit = count += 1
  def current: Int = count
}
```

Nguyên tắc nhỏ: nếu lớp của bạn chủ yếu là dữ liệu, hãy sử dụng`case class`. Nếu nó có trạng thái có thể thay đổi hoặc hành vi phức tạp, hãy sử dụng`class`thông thường.
### Câu 3: Làm cách nào để xử lý lỗi một cách rõ ràng trong Scala?
**A:** Scala ưu tiên các kiểu trả về như`Option`,`Either`và`Try`hơn là đưa ra các ngoại lệ:
```scala
// Option — value may be absent
def findUser(id: Int): Option[User] = ...

// Either — value or error
def parseAge(input: String): Either[String, Int] =
  try Right(input.toInt) catch { case _: NumberFormatException => Left(s"Invalid: $input") }

// Try — computation that may fail
import scala.util.Try
val result = Try(riskyOperation())

// For-comprehension to chain operations
val result = for {
  user <- findUser(id)
  age  <- parseAge(user.ageStr).toOption
} yield age
```

### Câu 4: Sự khác biệt giữa`trait`và`abstract class`là gì?
**A:** Các đặc điểm hỗ trợ nhiều kế thừa và có thể có các tham số loại cũng như phương thức cụ thể. Các lớp trừu tượng có thể có các tham số hàm tạo nhưng chỉ hỗ trợ kế thừa đơn:
```scala
// Trait — can mix in multiple
trait Printable { def print: String }
trait Serializable { def serialize: Array[Byte] }

class User extends Printable with Serializable {
  def print = s"User"
  def serialize = print.getBytes
}

// Abstract class — constructor params, single inheritance
abstract class BaseRepository(db: Database) {
  def find(id: Long): Option[Entity]
}
```

### Câu hỏi 5: Làm cách nào để viết mã Scala hiệu quả trên JVM?
**Đ:** Các phương pháp chính:
- Sử dụng`case class`và dữ liệu bất biến để tránh đồng bộ hóa
- Thích`Vector`,`Map`(không thay đổi) để chia sẻ cấu trúc
- Sử dụng chú thích`@tailrec`để đảm bảo tối ưu hóa cuộc gọi đuôi
- Tránh đấm bốc quá mức - sử dụng nguyên hàm`Int`, `Double`
- Sử dụng`lazy val`cho các tính toán tốn kém
- Ưu tiên`Stream`/`LazyList`cho các chuỗi lớn
- Cấu hình với JMH — Phần tóm tắt của Scala sẽ biên dịch thành mã byte hiệu quả
---

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Triển khai Trình đánh giá biểu thức an toàn kiểu
**Bước 1: Tìm hiểu vấn đề**
Chúng ta cần đánh giá các biểu thức toán học với các biến, hỗ trợ phép cộng, phép nhân và tra cứu biến.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng các kiểu dữ liệu đại số (các đặc điểm + lớp trường hợp được niêm phong) để lập mô hình cây biểu thức, sau đó so khớp mẫu để đánh giá.
**Bước 3: Thực hiện**```scala
sealed trait Expr
case class Num(value: Double) extends Expr
case class Add(left: Expr, right: Expr) extends Expr
case class Mul(left: Expr, right: Expr) extends Expr
case class Var(name: String) extends Expr

def eval(expr: Expr, env: Map[String, Double]): Option[Double] = expr match {
  case Num(v)        => Some(v)
  case Add(l, r)     => (eval(l, env), eval(r, env)).mapN(_ + _)
  case Mul(l, r)     => (eval(l, env), eval(r, env)).mapN(_ * _)
  case Var(name)     => env.get(name)
}

// Usage
val expr = Add(Mul(Var("x"), Num(2)), Num(3))
val env = Map("x" -> 5.0)
eval(expr, env) // Some(13.0)
```

**Bước 4: Xác minh và gia hạn**
Thêm các trường hợp`Div`,`Pow`, `Neg`. Đặc điểm kín đảm bảo trình biên dịch cảnh báo về các kết quả khớp không đầy đủ.
### Vấn đề 2: Xây dựng DSL đơn giản để tạo HTML
**Bước 1: Tìm hiểu vấn đề**
Tạo DSL an toàn loại để tạo chuỗi HTML bằng cú pháp của Scala.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng các lớp tình huống cho các phần tử HTML và chuyển đổi ngầm định để có cú pháp tự nhiên.
**Bước 3: Thực hiện**```scala
sealed trait HtmlNode {
  def render: String
}

case class Text(content: String) extends HtmlNode {
  def render = content
}

case class Element(tag: String, children: List[HtmlNode], attrs: Map[String, String] = Map.empty) extends HtmlNode {
  def render: String = {
    val attrStr = attrs.map { case (k, v) => s"""$k="$v"""" }.mkString(" ")
    val open = if (attrStr.isEmpty) s"<$tag>" else s"<$tag $attrStr>"
    s"$open${children.map(_.render).mkString}</$tag>"
  }
}

object HtmlDSL {
  def div(children: HtmlNode*): Element = Element("div", children.toList)
  def p(children: HtmlNode*): Element = Element("p", children.toList)
  def text(s: String): Text = Text(s)
  implicit def stringToText(s: String): Text = Text(s)
}

import HtmlDSL._
val page = div(
  p("Hello, World!"),
  p("Scala DSLs are powerful.")
)
println(page.render)
// <div><p>Hello, World!</p><p>Scala DSLs are powerful.</p></div>
```

**Bước 4: Xác minh**
DSL là loại an toàn — bạn không thể vô tình truyền nội dung không phải HTML. Khớp mẫu trên`HtmlNode`đảm bảo hiển thị toàn diện.
### Vấn đề 3: Đếm từ đồng thời với luồng Akka
**Bước 1: Tìm hiểu vấn đề**
Đếm tần số từ trên nhiều tệp lớn cùng một lúc.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng các bộ sưu tập song song của Scala hoặc Luồng Akka để xử lý đồng thời, sau đó hợp nhất các kết quả.
**Bước 3: Thực hiện**```scala
import scala.io.Source
import scala.collection.parallel.CollectionConverters._

def wordCount(files: List[String]): Map[String, Int] = {
  files.par
    .flatMap { file =>
      Source.fromFile(file).getLines()
        .flatMap(_.split("\\W+").filter(_.nonEmpty))
        .map(_.toLowerCase)
        .toList
    }
    .groupBy(identity)
    .map((k, v) => (k, v.size))
    .seq
}
```

**Bước 4: Tối ưu hóa**
Đối với các tập dữ liệu rất lớn, hãy sử dụng Luồng Akka có áp suất ngược:```scala
Source(fileList)
  .mapAsync(4)(file => Future(Source.fromFile(file).getLines().toList))
  .mapConcat(identity)
  .groupBy(256, _.toLowerCase)
  .fold(0)((count, _) => count + 1)
  .mergeSubstreams
  .runWith(Sink.seq)
```

---

## Bản tóm tắt
Scala là một ngôn ngữ mạnh mẽ mang lại khả năng lập trình chức năng cho JVM. Đó là ngôn ngữ của Apache Spark và là sự lựa chọn mạnh mẽ cho kỹ thuật dữ liệu, hệ thống phân tán và dịch vụ phụ trợ. Lộ trình học tập là có thật, nhưng phần thưởng xứng đáng là một ngôn ngữ vừa mang tính biểu cảm vừa mang tính biểu diễn. Đối với các nhóm đã đầu tư vào hệ sinh thái JVM, Scala cung cấp giải pháp thay thế ngắn gọn và mạnh mẽ hơn cho Java.