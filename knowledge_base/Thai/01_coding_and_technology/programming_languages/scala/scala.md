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
#สกาล่า
Scala (Scalable Language) เป็นภาษาการเขียนโปรแกรมแบบคอมไพล์ที่พิมพ์คงที่ ซึ่งรวมกระบวนทัศน์การเขียนโปรแกรมเชิงวัตถุและเชิงฟังก์ชันเข้าด้วยกัน Scala สร้างโดย Martin Odersky และเปิดตัวครั้งแรกในปี 2004 ทำงานบน JVM (เช่น Scala.js สำหรับ JavaScript และ Scala Native) ได้รับการออกแบบมาเพื่อจัดการกับคำฟุ่มเฟือยของ Java ในขณะที่ยังคงความสามารถในการทำงานร่วมกันของ Java ได้อย่างสมบูรณ์
Scala เป็นภาษาเบื้องหลัง Apache Spark (เฟรมเวิร์กการประมวลผลข้อมูลขนาดใหญ่) และมีการใช้อย่างแพร่หลายในด้านวิศวกรรมข้อมูล ระบบแบบกระจาย และบริการแบ็กเอนด์ บริษัทต่างๆ เช่น Twitter (ปัจจุบันคือ X), LinkedIn, Netflix และ The Guardian ใช้ Scala
---

## ทำไมสกาล่าจึงมีความสำคัญ
- **ฟังก์ชันการทำงาน + OOP ไฮบริด**: รวมสิ่งที่ดีที่สุดของทั้งสองกระบวนทัศน์ไว้ในภาษาเดียว
- **กระชับ**: มีรายละเอียดน้อยกว่า Java อย่างเห็นได้ชัด — การจับคู่รูปแบบ คลาสเคส การอนุมานประเภท
- **Apache Spark**: ภาษาหลักสำหรับการประมวลผลข้อมูลขนาดใหญ่บน Spark
- **ระบบประเภท**: คุณสมบัติขั้นสูง เช่น นัย คลาสประเภท และประเภทข้อมูลพีชคณิต
- **ความเข้ากันได้ของ JVM**: ใช้ไลบรารี Java ทั้งหมด ทำงานบน JVM เดียวกัน
- **Akka / Pekko**: เฟรมเวิร์กยอดนิยมสำหรับการสร้างระบบแบบกระจายพร้อมกัน
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ความซับซ้อน** | ภาษามีคุณสมบัติมากมาย อาจเป็นเรื่องยากที่จะเชี่ยวชาญ | เริ่มต้นด้วย "ส่วนที่ดี"; หลีกเลี่ยงโค้ดที่ฉลาดเกินไป |
| **เวลาในการคอมไพล์** | ช้ากว่า Java โดยเฉพาะกับประเภทที่ซับซ้อน | ใช้การคอมไพล์แบบเพิ่มหน่วย (Bloop, sbt) |
| **เส้นโค้งการเรียนรู้** | ชันกว่า Java หรือ Python | ลงทุนเวลา; ผลตอบแทนมีนัยสำคัญ |
| **ตลาดงานเล็กลง** | บทบาทน้อยกว่า Java หรือ Python | แข็งแกร่งในด้านวิศวกรรมข้อมูลและบทบาทแบ็กเอนด์ |
| **สไตล์ไม่สอดคล้องกัน** | ทีมต่างๆ เขียน Scala | ที่แตกต่างกันมาก ปฏิบัติตามคำแนะนำสไตล์ชุมชน |
---

## พื้นฐานไวยากรณ์
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

## ไวยากรณ์และรูปแบบขั้นสูง
### ประเภทคลาส (ผ่านนัย)
Scala 2 ใช้พารามิเตอร์โดยนัยในการเข้ารหัสคลาสประเภท Scala 3 แนะนำไวยากรณ์`given`/`using`ดั้งเดิม
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

### ลักษณะและการแจงนับที่ปิดผนึก (Scala 3 Enums)
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

### คุณสมบัติระบบประเภทขั้นสูง
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

## การเห็นพ้องต้องกันและความเท่าเทียม
### อนาคตและคำสัญญา
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

### ZIO — ระบบเอฟเฟกต์สมัยใหม่
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

### นักแสดงอัคคา/เป็กโก
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างโครงการ (sbt)
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

### การกำหนดค่าบิวด์ (build.sbt)
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

### คำสั่งสร้างคีย์
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `sbt new scala/scala3.g8`| สร้างโครงการ Scala 3 ใหม่จากเทมเพลต |
| `sbt compile`| รวบรวมแหล่งที่มาหลัก |
| `sbt test`| ทำการทดสอบทั้งหมด |
| `sbt run`| รันคลาสหลัก |
| `sbt runMain com.example.App`| รันคลาสหลักเฉพาะ |
| `sbt console`| เริ่ม REPL ด้วยโปรเจ็กต์บน classpath |
| `sbt clean`| เอาต์พุตที่คอมไพล์แล้วสะอาด |
| `sbt assembly`| สร้าง JAR ไขมัน (พร้อมปลั๊กอิน sbt-assembly) |
| `sbt scalafmt`| จัดรูปแบบโค้ดด้วย Scalafmt |
| `sbt scalafmtCheck`| ตรวจสอบการจัดรูปแบบโค้ด |
| `sbt ~compile`| การคอมไพล์อย่างต่อเนื่อง (คอมไพล์ใหม่เมื่อมีการเปลี่ยนแปลง) |
### การจัดรูปแบบโค้ด (.scalafmt.conf)
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

### ไปป์ไลน์ CI/CD (การดำเนินการ GitHub)
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

## การทดสอบ
### ScalaTest — การทดสอบที่ครอบคลุม
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

### ScalaCheck — การทดสอบตามคุณสมบัติ
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

### การทดสอบ ZIO
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

## การทำงานร่วมกัน
### การทำงานร่วมกันของ JVM
Scala สามารถเข้าถึงไลบรารี Java ทั้งหมดได้อย่างราบรื่น
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

### การทำงานร่วมกันแบบเนทีฟ (Scala Native)
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

## รูปแบบการออกแบบ
### รอบชิงชนะเลิศแบบไร้แท็กกับ Cats
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

### รูปแบบเลเยอร์ ZIO
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

### รูปแบบพื้นที่เก็บข้อมูลพร้อมการจัดการข้อผิดพลาด
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### เครื่องมือสร้างโปรไฟล์
| เครื่องมือ | วัตถุประสงค์ | การใช้งาน |
|------|---------|-------|
| **เจเอ็มเอช** | การเปรียบเทียบแบบไมโคร |  ปลั๊กอิน`sbt-jmh`|
| **VisualVM** | การทำโปรไฟล์ JVM และการมอนิเตอร์ |  คำสั่ง`jvisualvm`|
| **ตัวสร้างโปรไฟล์ Async** | การทำโปรไฟล์ CPU/หน่วยความจำโอเวอร์เฮดต่ำ | แนบกับการรัน JVM |
| **YourKit** | เครื่องมือสร้างโปรไฟล์เชิงพาณิชย์ | บูรณาการ IDE |
| **sbt-scoverage** | ความครอบคลุมของโค้ด | `sbt coverage test coverageReport`|
### การเปรียบเทียบด้วย JMH
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

### เทคนิคการเพิ่มประสิทธิภาพ
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

## การปรับใช้
### สร้าง JAR ไขมัน
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

### การปรับใช้นักเทียบท่า
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

### รูปภาพเนทิฟ GraalVM
```scala
// build.sbt — enable Scala Native or use GraalVM
// For GraalVM native-image:
// native-image --static -jar target/scala-3.3.1/my-app.jar -o my-app
```

---

## เมื่อใดจึงควรใช้สกาล่า
| สถานการณ์ | ทำไมต้องสกาล่า | ทางเลือกที่ดีกว่า |
|----------|----------|-------------------|
| ข้อมูลขนาดใหญ่ (Spark) | ภาษา Spark หลัก | Python (PySpark) สำหรับไปป์ไลน์ที่ง่ายกว่า |
| ระบบกระจาย (Akka) | กรอบการทำงานพร้อมกันที่สมบูรณ์ | ไปเถอะ เออร์แลง/เอลิเซียร์ |
| แบ็กเอนด์ JVM | ทางเลือก Java แบบกระชับ | ชวา, Kotlin |
| การเขียนโปรแกรมฟังก์ชั่นบน JVM | ชุดค่าผสม FP + JVM ที่ดีที่สุด | ปิดบัง |
| การพัฒนาแอพพลิเคชั่นทั่วไป | เป็นไปได้แต่ซับซ้อน | Python, Go, Java |
| วิทยาศาสตร์ข้อมูล | เป็นไปได้แต่ไม่ใช่ระบบนิเวศ | หลาม, อาร์ |
---

## คำถามและคำตอบสังเคราะห์
### คำถามที่ 1: การอนุมานประเภทของ Scala ลดขนาดสำเร็จรูปเมื่อเทียบกับ Java ได้อย่างไร
**A:** คอมไพเลอร์ของ Scala สรุปประเภทของการประกาศ`val`/`var`ประเภทการส่งคืนเมธอด และฟังก์ชันที่ไม่ระบุชื่อ ซึ่งช่วยลดความจำเป็นในการมีคำอธิบายประกอบประเภทที่ชัดเจนในกรณีส่วนใหญ่:
```scala
// Java: explicit types everywhere
Map<String, List<Integer>> grouped = new HashMap<>();
// Scala: types inferred
val grouped = items.groupBy(_.category)
```

คอมไพเลอร์ยังอนุมานพารามิเตอร์ประเภท ประเภทส่งคืนของวิธีนิพจน์เดี่ยว และประเภทการจับคู่รูปแบบ ทำให้โค้ดมีความกระชับโดยไม่กระทบต่อความปลอดภัย
### Q2: เมื่อใดที่ฉันควรใช้`case class`เทียบกับ`class`ปกติ
**A:** ใช้`case class`สำหรับผู้ให้บริการข้อมูลที่ไม่เปลี่ยนรูปแบบ — โดยจะมี`equals`,`hashCode`,`toString`,`copy`และรองรับการจับคู่รูปแบบโดยอัตโนมัติ:
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

หลักทั่วไป: หากชั้นเรียนของคุณเน้นข้อมูลเป็นหลัก ให้ใช้`case class`หากมีสถานะที่ไม่แน่นอนหรือมีพฤติกรรมที่ซับซ้อน ให้ใช้`class`ปกติ
### Q3: ฉันจะจัดการกับข้อผิดพลาดตามสำนวนใน Scala ได้อย่างไร
**A:** Scala นิยมส่งคืนประเภทเช่น`Option`,`Either`และ`Try`มากกว่าการส่งข้อยกเว้น:
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

### Q4: อะไรคือความแตกต่างระหว่าง`trait`และ`abstract class`?
**ตอบ:** ลักษณะรองรับการสืบทอดหลายรายการและสามารถมีพารามิเตอร์ประเภทและวิธีการที่เป็นรูปธรรมได้ คลาสนามธรรมสามารถมีพารามิเตอร์คอนสตรัคเตอร์ได้ แต่รองรับเฉพาะการสืบทอดเดียวเท่านั้น:
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

### คำถามที่ 5: ฉันจะเขียนโค้ด Scala ที่มีประสิทธิภาพบน JVM ได้อย่างไร
**ก:** แนวทางปฏิบัติหลัก:
- ใช้`case class`และข้อมูลที่ไม่เปลี่ยนรูปเพื่อหลีกเลี่ยงการซิงโครไนซ์
- ต้องการ`Vector`,`Map`(ไม่เปลี่ยนรูป) สำหรับการแชร์โครงสร้าง
- ใช้คำอธิบายประกอบ`@tailrec`เพื่อให้แน่ใจว่าการเรียกหางจะเหมาะสมที่สุด
- หลีกเลี่ยงการชกมากเกินไป — ใช้`Int`,`Double`primitives
- ใช้`lazy val`สำหรับการคำนวณราคาแพง
- ต้องการ`Stream`/`LazyList`สำหรับลำดับขนาดใหญ่
- โปรไฟล์ด้วย JMH - นามธรรมของ Scala ควรคอมไพล์เป็นไบต์โค้ดที่มีประสิทธิภาพ
---

## การแก้ปัญหาลูกโซ่แห่งความคิด
### ปัญหาที่ 1: การใช้ตัวประเมินนิพจน์แบบปลอดภัย
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
เราจำเป็นต้องประเมินนิพจน์ทางคณิตศาสตร์ด้วยตัวแปร รองรับการบวก การคูณ และการค้นหาตัวแปร
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้ประเภทข้อมูลพีชคณิต (ลักษณะปิดผนึก + คลาสเคส) เพื่อสร้างโมเดลแผนผังนิพจน์ จากนั้นจึงจับคู่รูปแบบเพื่อประเมิน
**ขั้นตอนที่ 3: นำไปใช้**```scala
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

**ขั้นตอนที่ 4: ตรวจสอบและขยาย**
เพิ่มเคส`Div`,`Pow`,`Neg`ลักษณะที่ปิดผนึกช่วยให้คอมไพลเลอร์เตือนเกี่ยวกับการจับคู่โดยสังเขป
### ปัญหาที่ 2: การสร้าง DSL อย่างง่ายสำหรับการสร้าง HTML
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
สร้าง DSL ที่ปลอดภัยสำหรับประเภทที่สร้างสตริง HTML โดยใช้ไวยากรณ์ของ Scala
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้คลาส case สำหรับองค์ประกอบ HTML และการแปลงโดยนัยสำหรับไวยากรณ์ตามธรรมชาติ
**ขั้นตอนที่ 3: นำไปใช้**```scala
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

**ขั้นตอนที่ 4: ยืนยัน**
DSL นั้นปลอดภัยต่อการพิมพ์ — คุณไม่สามารถส่งเนื้อหาที่ไม่ใช่ HTML โดยไม่ได้ตั้งใจ การจับคู่รูปแบบบน`HtmlNode`ช่วยให้มั่นใจได้ถึงการเรนเดอร์ที่ละเอียดถี่ถ้วน
### ปัญหาที่ 3: การนับจำนวนคำพร้อมกันกับ Akka Streams
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
นับความถี่คำในไฟล์ขนาดใหญ่หลายไฟล์พร้อมกัน
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้คอลเลกชันแบบขนานของ Scala หรือ Akka Streams สำหรับการประมวลผลพร้อมกัน จากนั้นจึงรวมผลลัพธ์
**ขั้นตอนที่ 3: นำไปใช้**```scala
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

**ขั้นตอนที่ 4: เพิ่มประสิทธิภาพ**
สำหรับชุดข้อมูลที่มีขนาดใหญ่มาก ให้ใช้ Akka Streams ที่มีแรงดันย้อนกลับ:```scala
Source(fileList)
  .mapAsync(4)(file => Future(Source.fromFile(file).getLines().toList))
  .mapConcat(identity)
  .groupBy(256, _.toLowerCase)
  .fold(0)((count, _) => count + 1)
  .mergeSubstreams
  .runWith(Sink.seq)
```

---

## สรุป
Scala เป็นภาษาที่ทรงพลังที่นำการเขียนโปรแกรมเชิงฟังก์ชันมาสู่ JVM มันเป็นภาษาของ Apache Spark และเป็นตัวเลือกที่ดีสำหรับวิศวกรรมข้อมูล ระบบแบบกระจาย และบริการแบ็กเอนด์ เส้นโค้งการเรียนรู้นั้นมีอยู่จริง แต่ผลลัพธ์ที่ได้คือภาษาที่ทั้งแสดงออกและมีประสิทธิภาพ สำหรับทีมที่ลงทุนในระบบนิเวศ JVM แล้ว Scala เสนอทางเลือกที่กระชับและมีประสิทธิภาพมากกว่าสำหรับ Java