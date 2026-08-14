---
# Metadata
title: "Scala"
description: "Comprehensive reference for the Scala programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# اسکیلا
اسکالا (اسکیل ایبل لینگویج) ایک مستحکم طور پر ٹائپ شدہ، مرتب کردہ پروگرامنگ لینگویج ہے جو آبجیکٹ اورینٹڈ اور فنکشنل پروگرامنگ پیراڈائمز کو یکجا کرتی ہے۔ مارٹن اوڈرسکی کے ذریعہ تخلیق کیا گیا اور پہلی بار 2004 میں ریلیز ہوا، اسکالا JVM پر چلتا ہے (جاوا اسکرپٹ اور اسکالا مقامی کے لیے بھی Scala.js)۔ یہ جاوا کی مکمل مداخلت کو برقرار رکھتے ہوئے جاوا کی فعلیت کو حل کرنے کے لیے ڈیزائن کیا گیا تھا۔
اسکالا Apache Spark (بڑے ڈیٹا پروسیسنگ فریم ورک) کے پیچھے کی زبان ہے، اور یہ ڈیٹا انجینئرنگ، تقسیم شدہ نظام، اور بیک اینڈ سروسز میں بڑے پیمانے پر استعمال ہوتی ہے۔ ٹویٹر (اب X)، LinkedIn، Netflix، اور The Guardian جیسی کمپنیاں Scala استعمال کرتی ہیں۔
---

## اسکالا کیوں اہمیت رکھتا ہے۔
- **فنکشنل + او او پی ہائبرڈ**: ایک ہی زبان میں دونوں نمونوں میں سے بہترین کو یکجا کرتا ہے۔
- **مختصر**: جاوا کے مقابلے میں نمایاں طور پر کم لفظی - پیٹرن کی مماثلت، کیس کلاسز، قسم کا اندازہ۔
- **Apache Spark**: Spark پر مبنی بڑی ڈیٹا پروسیسنگ کے لیے بنیادی زبان۔
- **ٹائپ سسٹم**: اعلی درجے کی خصوصیات جیسے مضمرات، قسم کی کلاسیں، اور الجبری ڈیٹا کی اقسام۔
- **JVM مطابقت**: تمام جاوا لائبریریوں کا استعمال کرتا ہے؛ اسی JVM پر چلتا ہے۔
- **Akka/Pekko**: کنکرنٹ، تقسیم شدہ نظاموں کی تعمیر کے لیے مقبول فریم ورک۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **پیچیدگی** | زبان کی بہت سی خصوصیات ہیں۔ مہارت حاصل کرنا مشکل ہو سکتا ہے | "اچھے حصوں" کے ساتھ شروع کریں؛ حد سے زیادہ ہوشیار کوڈ سے بچیں |
| ** مرتب اوقات** | جاوا سے سست، خاص طور پر پیچیدہ اقسام کے ساتھ | اضافی تالیف کا استعمال کریں (Bloop, sbt) |
| **سیکھنے کا وکر** | جاوا یا ازگر سے زیادہ تیز | وقت کی سرمایہ کاری؛ ادائیگی اہم ہے |
| **چھوٹی جاب مارکیٹ** | جاوا یا ازگر سے کم کردار | ڈیٹا انجینئرنگ اور بیک اینڈ رولز میں مضبوط |
| **متضاد انداز** | مختلف ٹیمیں بہت مختلف Scala لکھتی ہیں۔ کمیونٹی اسٹائل گائیڈز پر عمل کریں |
---

## نحوی بنیادی باتیں
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

## اعلی درجے کی نحو اور نمونے۔
### قسم کی کلاسز (بذریعہ مضمرات)
Scala 2 قسم کی کلاسوں کو انکوڈ کرنے کے لیے مضمر پیرامیٹرز کا استعمال کرتا ہے۔ Scala 3 نے مقامی`given`/`using`نحو متعارف کرایا ہے۔
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

### مہر بند خصلتیں اور شماریات (Scala 3 Enums)
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

### اعلی درجے کی قسم کے نظام کی خصوصیات
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

## ہم آہنگی اور ہم آہنگی
### مستقبل اور وعدے۔
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

### ZIO - جدید اثر کا نظام
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

### اکا/پیکو اداکار
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ (sbt)
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

### تعمیر کنفیگریشن (build.sbt)
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

### کلیدی بلڈ کمانڈز
| کمانڈ | تفصیل |
|---------|---------------|
| `sbt new scala/scala3.g8`| ٹیمپلیٹ سے نیا Scala 3 پروجیکٹ بنائیں |
| `sbt compile`| اہم ذرائع کو مرتب کریں |
| `sbt test`| تمام ٹیسٹ چلائیں |
| `sbt run`| مین کلاس چلائیں |
| `sbt runMain com.example.App`| ایک مخصوص مین کلاس چلائیں |
| `sbt console`| کلاس پاتھ پر پروجیکٹ کے ساتھ REPL شروع کریں۔
| `sbt clean`| صاف مرتب شدہ آؤٹ پٹ |
| `sbt assembly`| چربی والا جار بنائیں (ایس بی ٹی اسمبلی پلگ ان کے ساتھ) |
| `sbt scalafmt`| Scalafmt کے ساتھ فارمیٹ کوڈ |
| `sbt scalafmtCheck`| کوڈ فارمیٹنگ چیک کریں |
| `sbt ~compile`| مسلسل تالیف (تبدیلی پر دوبارہ مرتب کریں) |
### کوڈ فارمیٹنگ (.scalafmt.conf)
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

### CI/CD پائپ لائن (GitHub ایکشنز)
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

## ٹیسٹنگ
### اسکیل ٹیسٹ - جامع جانچ
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

### ScalaCheck — پراپرٹی پر مبنی ٹیسٹنگ
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

### ZIO ٹیسٹ
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

## انٹرآپریبلٹی
### JVM انٹرآپریبلٹی
Scala کو جاوا کی تمام لائبریریوں تک بغیر کسی رکاوٹ کے رسائی حاصل ہے۔
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

### Native Interop (Scala Native)
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

## ڈیزائن پیٹرن
### بلیوں کے ساتھ ٹیگ لیس فائنل
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

### ZIO پرت کا پیٹرن
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

### خرابی سے نمٹنے کے ساتھ ریپوزٹری پیٹرن
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
| ٹول | مقصد | استعمال |
|------|---------|------|
| **JMH** | مائیکرو بینچ مارکنگ | `sbt-jmh`پلگ ان |
| **بصری وی ایم** | JVM پروفائلنگ اور نگرانی | `jvisualvm`کمانڈ |
| **Async پروفائلر** | کم اوور ہیڈ CPU/میموری پروفائلنگ | JVM چلانے کے ساتھ منسلک کریں |
| **YourKit** | کمرشل پروفائلر | IDE انضمام |
| **sbt-scoverage** | کوڈ کوریج | `sbt coverage test coverageReport`|
### JMH کے ساتھ بینچ مارکنگ
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

### اصلاح کی تکنیک
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

## تعیناتی۔
### موٹی جار بنانا
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

### ڈاکر کی تعیناتی۔
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

### GraalVM مقامی تصویر
```scala
// build.sbt — enable Scala Native or use GraalVM
// For GraalVM native-image:
// native-image --static -jar target/scala-3.3.1/my-app.jar -o my-app
```

---

## Scala کب استعمال کریں۔
| منظر نامہ | سکالا کیوں | بہتر متبادل |
|------------|------------|-------------------|
| بڑا ڈیٹا (چنگاری) | بنیادی چنگاری زبان | Python (PySpark) آسان پائپ لائنوں کے لیے |
| تقسیم شدہ نظام (اکا) | بالغ کنکرنسی فریم ورک | Go, Erlang/Elixir |
| JVM بیک اینڈز | مختصر جاوا متبادل | جاوا، کوٹلن |
| JVM پر فنکشنل پروگرامنگ | بہترین FP + JVM مجموعہ | Clojure |
| عام درخواست کی ترقی | ممکنہ لیکن پیچیدہ | ازگر، گو، جاوا |
| ڈیٹا سائنس | ممکن ہے لیکن ماحولیاتی نظام نہیں | ازگر، آر |
---

## مصنوعی سوال و جواب
### Q1: Scala کی قسم کا اندازہ جاوا کے مقابلے بوائلر پلیٹ کو کیسے کم کرتا ہے؟
**A:** Scala کا کمپائلر`val`/`var`ڈیکلریشنز، طریقہ واپسی کی اقسام، اور گمنام فنکشنز کی اقسام کا اندازہ لگاتا ہے۔ یہ زیادہ تر معاملات میں واضح قسم کی تشریحات کی ضرورت کو ختم کرتا ہے:
```scala
// Java: explicit types everywhere
Map<String, List<Integer>> grouped = new HashMap<>();
// Scala: types inferred
val grouped = items.groupBy(_.category)
```

کمپائلر قسم کے پیرامیٹرز، واحد اظہار کے طریقوں کی واپسی کی اقسام، اور پیٹرن میچ کی اقسام کا بھی اندازہ لگاتا ہے۔ یہ حفاظت کی قربانی کے بغیر کوڈ کو جامع بناتا ہے۔
### Q2: مجھے`case class`بمقابلہ باقاعدہ`class`کب استعمال کرنا چاہیے؟
**A:** غیر تبدیل شدہ ڈیٹا کیریئرز کے لیے`case class`استعمال کریں — وہ `equals`، `hashCode`، `toString`، `copy`، اور پیٹرن کی مماثلت خود بخود سپورٹ فراہم کرتے ہیں:
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

انگوٹھے کا اصول: اگر آپ کی کلاس بنیادی طور پر ڈیٹا ہے تو`case class`استعمال کریں۔ اگر اس میں تغیر پذیر حالت یا پیچیدہ رویہ ہے، تو باقاعدہ`class`استعمال کریں۔
### Q3: میں اسکالا میں غلطیوں کو محاوراتی طور پر کیسے ہینڈل کروں؟
**A:** Scala واپسی کی قسموں کی حمایت کرتا ہے جیسے `Option`، `Either`، اور`Try`پھینکنے کے استثناء پر:
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

### Q4:`trait`اور`abstract class`میں کیا فرق ہے؟
**A:** خصلتیں متعدد وراثت کی حمایت کرتی ہیں اور ان میں قسم کے پیرامیٹرز اور ٹھوس طریقے ہوسکتے ہیں۔ خلاصہ کلاسوں میں کنسٹرکٹر پیرامیٹرز ہوسکتے ہیں لیکن صرف ایک ہی وراثت کی حمایت کرتے ہیں:
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

### Q5: میں JVM پر پرفارمنٹ اسکالا کوڈ کیسے لکھ سکتا ہوں؟
**A:** کلیدی مشقیں:
- مطابقت پذیری سے بچنے کے لیے`case class`اور ناقابل تغیر ڈیٹا استعمال کریں۔
- ساختی اشتراک کے لیے `Vector`،`Map`(غیر متغیر) کو ترجیح دیں
- ٹیل کال آپٹیمائزیشن کو یقینی بنانے کے لیے`@tailrec`تشریح کا استعمال کریں۔
- ضرورت سے زیادہ باکسنگ سے پرہیز کریں - `Int`،`Double`قدیم استعمال کریں
- مہنگے حساب کے لیے`lazy val`استعمال کریں۔
- بڑے سلسلے کے لیے`Stream`/`LazyList`کو ترجیح دیں
- JMH کے ساتھ پروفائل - اسکالا کے تجریدوں کو موثر بائیک کوڈ پر مرتب کرنا چاہئے۔
---

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: ٹائپ سیف ایکسپریشن ایویلیویٹر کو لاگو کرنا
**مرحلہ 1: مسئلہ کو سمجھیں**
ہمیں متغیرات، معاون اضافے، ضرب، اور متغیر تلاش کے ساتھ ریاضیاتی اظہار کا اندازہ کرنے کی ضرورت ہے۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
ایکسپریشن ٹری کو ماڈل کرنے کے لیے الجبری ڈیٹا کی اقسام (سیل شدہ ٹریٹ + کیس کلاسز) کا استعمال کریں، پھر اندازہ کرنے کے لیے پیٹرن میچ کریں۔
**مرحلہ 3: نافذ کریں**```scala
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

**مرحلہ 4: تصدیق کریں اور توسیع کریں**
`Div` ,`Pow`,`Neg`کیسز شامل کریں۔ مہر بند خصوصیت اس بات کو یقینی بناتی ہے کہ کمپائلر غیر مکمل میچوں کے بارے میں خبردار کرتا ہے۔
### مسئلہ 2: HTML جنریشن کے لیے ایک سادہ DSL بنانا
**مرحلہ 1: مسئلہ کو سمجھیں**
ایک قسم سے محفوظ DSL بنائیں جو Scala کے نحو کا استعمال کرتے ہوئے HTML سٹرنگز تیار کرے۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
HTML عناصر کے لیے کیس کلاسز اور فطری نحو کے لیے مضمر تبادلوں کا استعمال کریں۔
**مرحلہ 3: نافذ کریں**```scala
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

**مرحلہ 4: تصدیق کریں**
DSL ٹائپ سیف ہے — آپ غلطی سے غیر HTML مواد کو پاس نہیں کر سکتے۔`HtmlNode`پر پیٹرن میچنگ مکمل رینڈرنگ کو یقینی بناتی ہے۔
### مسئلہ 3: اکا اسٹریمز کے ساتھ ہم آہنگ الفاظ کی گنتی
**مرحلہ 1: مسئلہ کو سمجھیں**
متعدد بڑی فائلوں میں بیک وقت الفاظ کی تعدد کو شمار کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
سمورتی پروسیسنگ کے لیے Scala کے متوازی مجموعے یا اکا اسٹریمز کا استعمال کریں، پھر نتائج کو ضم کریں۔
**مرحلہ 3: نافذ کریں**```scala
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

**مرحلہ 4: بہتر بنائیں**
بہت بڑے ڈیٹاسیٹس کے لیے، بیک پریشر کے ساتھ اکا اسٹریمز کا استعمال کریں:```scala
Source(fileList)
  .mapAsync(4)(file => Future(Source.fromFile(file).getLines().toList))
  .mapConcat(identity)
  .groupBy(256, _.toLowerCase)
  .fold(0)((count, _) => count + 1)
  .mergeSubstreams
  .runWith(Sink.seq)
```

---

## خلاصہ
اسکالا ایک طاقتور زبان ہے جو JVM میں فنکشنل پروگرامنگ لاتی ہے۔ یہ Apache Spark کی زبان ہے اور ڈیٹا انجینئرنگ، ڈسٹری بیوٹڈ سسٹمز، اور بیک اینڈ سروسز کے لیے ایک مضبوط انتخاب ہے۔ سیکھنے کا منحنی خطوط حقیقی ہے، لیکن ادائیگی ایک ایسی زبان ہے جو اظہار اور کارکردگی دونوں ہے۔ JVM ماحولیاتی نظام میں پہلے سے سرمایہ کاری کر چکی ٹیموں کے لیے، Scala جاوا کا ایک زیادہ مختصر اور طاقتور متبادل پیش کرتا ہے۔