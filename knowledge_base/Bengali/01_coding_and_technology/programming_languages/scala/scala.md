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

# স্কালা
স্কালা (স্কেলেবল ল্যাঙ্গুয়েজ) হল একটি স্থিতিশীলভাবে টাইপ করা, সংকলিত প্রোগ্রামিং ভাষা যা অবজেক্ট-ওরিয়েন্টেড এবং কার্যকরী প্রোগ্রামিং প্যারাডাইমগুলিকে একত্রিত করে। মার্টিন ওডারস্কি দ্বারা তৈরি এবং 2004 সালে প্রথম প্রকাশিত, স্কালা JVM-এ চলে (এছাড়াও JavaScript এবং Scala নেটিভের জন্য Scala.js)। এটি সম্পূর্ণ জাভা ইন্টারঅপারেবিলিটি বজায় রাখার সময় জাভা এর ভারবোসিটি মোকাবেলা করার জন্য ডিজাইন করা হয়েছিল।
স্কালা হল অ্যাপাচি স্পার্ক (বড় ডেটা প্রসেসিং ফ্রেমওয়ার্ক) এর পিছনের ভাষা এবং এটি ডেটা ইঞ্জিনিয়ারিং, বিতরণ সিস্টেম এবং ব্যাকএন্ড পরিষেবাগুলিতে ব্যাপকভাবে ব্যবহৃত হয়। টুইটার (এখন এক্স), লিঙ্কডইন, নেটফ্লিক্স এবং দ্য গার্ডিয়ানের মতো কোম্পানিগুলি স্কালা ব্যবহার করে।
---

## কেন স্কেলা ব্যাপার
- **ফাংশনাল + ওওপি হাইব্রিড**: একটি একক ভাষায় উভয় দৃষ্টান্তের সেরাকে একত্রিত করে।
- **সংক্ষিপ্ত**: জাভা - প্যাটার্ন ম্যাচিং, কেস ক্লাস, টাইপ ইনফারেন্সের তুলনায় উল্লেখযোগ্যভাবে কম শব্দভাষা।
- **Apache Spark**: স্পার্ক-ভিত্তিক বিগ ডেটা প্রসেসিংয়ের প্রাথমিক ভাষা।
- **টাইপ সিস্টেম**: উন্নত বৈশিষ্ট্য যেমন অন্তর্নিহিত, টাইপ ক্লাস, এবং বীজগণিত ডেটা প্রকার।
- **JVM সামঞ্জস্য**: সমস্ত জাভা লাইব্রেরি ব্যবহার করে; একই JVM এ চলে।
- **আক্কা/পেকো**: সমসাময়িক, বিতরণ ব্যবস্থা তৈরির জন্য জনপ্রিয় কাঠামো।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **জটিলতা** | ভাষার অনেক বৈশিষ্ট্য আছে; আয়ত্ত করা কঠিন হতে পারে | "ভাল অংশ" দিয়ে শুরু করুন; অত্যধিক চতুর কোড এড়িয়ে চলুন |
| **সময় কম্পাইল** | জাভা থেকে ধীর, বিশেষ করে জটিল ধরনের সঙ্গে | ইনক্রিমেন্টাল কম্পাইলেশন ব্যবহার করুন (ব্লুপ, এসবিটি) |
| **লার্নিং কার্ভ** | জাভা বা পাইথনের চেয়ে খাড়া | সময় বিনিয়োগ করুন; বেতন উল্লেখযোগ্য |
| **ছোট চাকরীর বাজার** | জাভা বা পাইথনের চেয়ে কম ভূমিকা | ডেটা ইঞ্জিনিয়ারিং এবং ব্যাকএন্ড ভূমিকায় শক্তিশালী |
| **অসংলগ্ন শৈলী** | বিভিন্ন দল খুব আলাদা স্কালা লেখে | সম্প্রদায় শৈলী নির্দেশিকা অনুসরণ করুন |
---

## সিনট্যাক্স মৌলিক
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### টাইপ ক্লাস (অন্তর্ভুক্ত মাধ্যমে)
Scala 2 টাইপ ক্লাস এনকোড করতে অন্তর্নিহিত পরামিতি ব্যবহার করে। Scala 3 নেটিভ`given`/`using`সিনট্যাক্স প্রবর্তন করে।
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

### সিল করা বৈশিষ্ট্য এবং গণনা (স্ক্যালা 3 এনামস)
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

### অ্যাডভান্সড টাইপ সিস্টেম ফিচার
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

## সামঞ্জস্য এবং সমান্তরালতা
### ভবিষ্যত এবং প্রতিশ্রুতি
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

### ZIO — আধুনিক প্রভাব সিস্টেম
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

### আক্কা/পেকো অভিনেতা
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো (sbt)
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

### বিল্ড কনফিগারেশন (build.sbt)
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

### কী বিল্ড কমান্ড
| আদেশ | বর্ণনা |
|---------|---------------|
| `sbt new scala/scala3.g8`| টেমপ্লেট থেকে নতুন স্কালা 3 প্রকল্প তৈরি করুন |
| `sbt compile`| প্রধান উৎস কম্পাইল |
| `sbt test`| সমস্ত পরীক্ষা চালান |
| `sbt run`| মূল ক্লাস চালান |
| `sbt runMain com.example.App`| একটি নির্দিষ্ট প্রধান ক্লাস চালান |
| `sbt console`| ক্লাসপথে প্রকল্পের সাথে REPL শুরু করুন |
| `sbt clean`| ক্লিন কম্পাইল করা আউটপুট |
| `sbt assembly`| বিল্ড ফ্যাট JAR (এসবিটি-এসেম্বলি প্লাগইন সহ) |
| `sbt scalafmt`| Scalafmt দিয়ে কোড ফরম্যাট করুন |
| `sbt scalafmtCheck`| কোড ফরম্যাটিং চেক করুন |
| `sbt ~compile`| ক্রমাগত সংকলন (পরিবর্তনের উপর পুনরায় কম্পাইল) |
### কোড ফরম্যাটিং (.scalafmt.conf)
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

### CI/CD পাইপলাইন (GitHub অ্যাকশন)
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

## পরীক্ষা
### স্কেলাটেস্ট — ব্যাপক পরীক্ষা
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

### স্কেলাচেক — সম্পত্তি-ভিত্তিক পরীক্ষা
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

### ZIO পরীক্ষা
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

## ইন্টারঅপারেবিলিটি
### JVM ইন্টারঅপারেবিলিটি
স্কালার সমস্ত জাভা লাইব্রেরিতে বিরামহীন অ্যাক্সেস রয়েছে।
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

### নেটিভ ইন্টারপ (স্কেলা নেটিভ)
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

## ডিজাইন প্যাটার্ন
### বিড়ালদের সাথে ট্যাগলেস ফাইনাল
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

### ZIO লেয়ার প্যাটার্ন
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

### এরর হ্যান্ডলিং সহ রিপোজিটরি প্যাটার্ন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
| টুল | উদ্দেশ্য | ব্যবহার |
|------|---------|-------|
| **জেএমএইচ** | মাইক্রো-বেঞ্চমার্কিং | `sbt-jmh`প্লাগইন |
| **ভিজ্যুয়ালভিএম** | JVM প্রোফাইলিং এবং পর্যবেক্ষণ | `jvisualvm`কমান্ড |
| **অ্যাসিঙ্ক প্রোফাইলার** | লো-ওভারহেড CPU/মেমরি প্রোফাইলিং | চলমান JVM সংযুক্ত করুন |
| **আপনার কিট** | বাণিজ্যিক প্রোফাইলার | IDE ইন্টিগ্রেশন |
| **sbt-scoverage** | কোড কভারেজ | `sbt coverage test coverageReport`|
### JMH এর সাথে বেঞ্চমার্কিং
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

### অপ্টিমাইজেশন কৌশল
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

## স্থাপনা
### ফ্যাট জার তৈরি করা
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

### ডকার স্থাপনা
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

### GraalVM নেটিভ ইমেজ
```scala
// build.sbt — enable Scala Native or use GraalVM
// For GraalVM native-image:
// native-image --static -jar target/scala-3.3.1/my-app.jar -o my-app
```

---

## কখন স্কালা ব্যবহার করবেন
| দৃশ্যকল্প | কেন স্কালা | ভাল বিকল্প |
|------------|------------|---------|
| বিগ ডেটা (স্পার্ক) | প্রাথমিক স্পার্ক ভাষা | সহজ পাইপলাইনের জন্য পাইথন (PySpark) |
| বিতরণ ব্যবস্থা (আক্কা) | পূর্ণবয়স্ক সঙ্গতি কাঠামো | যান, এরলাং/এলিক্সির |
| JVM ব্যাকএন্ড | সংক্ষিপ্ত জাভা বিকল্প | জাভা, কোটলিন |
| JVM এ কার্যকরী প্রোগ্রামিং | সেরা FP + JVM সমন্বয় | ক্লোজার |
| সাধারণ অ্যাপ্লিকেশন বিকাশ | সম্ভাব্য কিন্তু জটিল | পাইথন, গো, জাভা |
| তথ্য বিজ্ঞান | সম্ভব কিন্তু ইকোসিস্টেম নয় | পাইথন, আর |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: জাভার তুলনায় স্কালার টাইপ ইনফারেন্স কীভাবে বয়লারপ্লেট কমায়?
**A:** স্কালার কম্পাইলার`val`/`var`ঘোষণা, পদ্ধতি রিটার্নের ধরন এবং বেনামী ফাংশনের জন্য প্রকারগুলি অনুমান করে৷ এটি বেশিরভাগ ক্ষেত্রে স্পষ্ট টাইপ টীকাগুলির প্রয়োজনীয়তা দূর করে:
```scala
// Java: explicit types everywhere
Map<String, List<Integer>> grouped = new HashMap<>();
// Scala: types inferred
val grouped = items.groupBy(_.category)
```

কম্পাইলার টাইপ প্যারামিটার, একক-প্রকাশ পদ্ধতির রিটার্ন প্রকার এবং প্যাটার্ন ম্যাচের ধরনগুলিও অনুমান করে। এটি নিরাপত্তার ত্যাগ ছাড়াই কোডকে সংক্ষিপ্ত করে তোলে।
### প্রশ্ন 2: কখন আমার`case class`বনাম নিয়মিত`class`ব্যবহার করা উচিত?
**A:** অপরিবর্তনীয় ডেটা ক্যারিয়ারের জন্য`case class`ব্যবহার করুন — তারা`equals`,`hashCode`,`toString`,`copy`এবং প্যাটার্ন ম্যাচিং সমর্থন স্বয়ংক্রিয়ভাবে প্রদান করে:
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

অঙ্গুষ্ঠের নিয়ম: আপনার ক্লাস প্রাথমিকভাবে ডেটা হলে,`case class`ব্যবহার করুন। যদি এটির পরিবর্তনযোগ্য অবস্থা বা জটিল আচরণ থাকে তবে একটি নিয়মিত`class`ব্যবহার করুন।
### প্রশ্ন 3: আমি কীভাবে স্কালাতে মূর্খতার সাথে ত্রুটিগুলি পরিচালনা করব?
**A:** স্কালা থ্রো করার ব্যতিক্রমের চেয়ে `Option`, `Either`, এবং`Try`এর মত রিটার্নিং ধরনের সমর্থন করে:
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

### প্রশ্ন 4:`trait`এবং`abstract class`এর মধ্যে পার্থক্য কী?
**A:** বৈশিষ্ট্য একাধিক উত্তরাধিকার সমর্থন করে এবং টাইপ প্যারামিটার এবং কংক্রিট পদ্ধতি থাকতে পারে। বিমূর্ত ক্লাসে কনস্ট্রাক্টর প্যারামিটার থাকতে পারে তবে শুধুমাত্র একক উত্তরাধিকার সমর্থন করে:
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

### প্রশ্ন 5: আমি কীভাবে JVM-এ পারফরম্যান্ট স্কালা কোড লিখব?
**A:** মূল অনুশীলন:
- সিঙ্ক্রোনাইজেশন এড়াতে`case class`এবং অপরিবর্তনীয় ডেটা ব্যবহার করুন
- কাঠামোগত ভাগ করার জন্য`Vector`,`Map`(অপরিবর্তনীয়) পছন্দ করুন
- টেল-কল অপ্টিমাইজেশান নিশ্চিত করতে`@tailrec`টীকা ব্যবহার করুন৷
- অতিরিক্ত বক্সিং এড়িয়ে চলুন - `Int`,`Double`আদিম ব্যবহার করুন
- ব্যয়বহুল গণনার জন্য`lazy val`ব্যবহার করুন
- বড় সিকোয়েন্সের জন্য`Stream`/`LazyList`পছন্দ করুন
- JMH-এর সাথে প্রোফাইল — স্কালার বিমূর্ততা দক্ষ বাইটকোডে কম্পাইল করা উচিত
---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি টাইপ-সেফ এক্সপ্রেশন ইভালুয়েটর প্রয়োগ করা
**ধাপ 1: সমস্যাটি বুঝুন**
আমাদেরকে ভেরিয়েবল, সাপোর্টিং যোগ, গুন এবং ভেরিয়েবল লুকআপ দিয়ে গাণিতিক এক্সপ্রেশন মূল্যায়ন করতে হবে।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
এক্সপ্রেশন ট্রি মডেল করার জন্য বীজগাণিতিক ডেটা টাইপ (সিল করা বৈশিষ্ট্য + কেস ক্লাস) ব্যবহার করুন, তারপর মূল্যায়ন করতে প্যাটার্ন ম্যাচ করুন।
**ধাপ 3: প্রয়োগ করুন**```scala
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

**ধাপ 4: যাচাই করুন এবং প্রসারিত করুন**
`Div` ,`Pow`,`Neg`ক্ষেত্রে যোগ করুন৷ সিল করা বৈশিষ্ট্যটি নিশ্চিত করে যে কম্পাইলার অ-সম্পূর্ণ মিল সম্পর্কে সতর্ক করে।
### সমস্যা 2: HTML জেনারেশনের জন্য একটি সাধারণ DSL তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি টাইপ-সেফ ডিএসএল তৈরি করুন যা স্কালার সিনট্যাক্স ব্যবহার করে HTML স্ট্রিং তৈরি করে।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
প্রাকৃতিক সিনট্যাক্সের জন্য HTML উপাদান এবং অন্তর্নিহিত রূপান্তরগুলির জন্য কেস ক্লাস ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```scala
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

**পদক্ষেপ 4: যাচাই করুন**
ডিএসএল টাইপ-সেফ — আপনি ভুলবশত এইচটিএমএল নয় এমন সামগ্রী পাস করতে পারবেন না। `HtmlNode`-এ প্যাটার্ন ম্যাচিং সম্পূর্ণ রেন্ডারিং নিশ্চিত করে।
### সমস্যা 3: আক্কা স্ট্রিমগুলির সাথে সমসাময়িক শব্দ গণনা
**ধাপ 1: সমস্যাটি বুঝুন**
একই সাথে একাধিক বড় ফাইল জুড়ে শব্দ ফ্রিকোয়েন্সি গণনা করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
সমসাময়িক প্রক্রিয়াকরণের জন্য স্কলার সমান্তরাল সংগ্রহ বা আক্কা স্ট্রীম ব্যবহার করুন, তারপর ফলাফলগুলি একত্রিত করুন।
**ধাপ 3: প্রয়োগ করুন**```scala
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

**ধাপ ৪: অপ্টিমাইজ**
খুব বড় ডেটাসেটের জন্য, ব্যাকপ্রেশার সহ আক্কা স্ট্রিমগুলি ব্যবহার করুন:```scala
Source(fileList)
  .mapAsync(4)(file => Future(Source.fromFile(file).getLines().toList))
  .mapConcat(identity)
  .groupBy(256, _.toLowerCase)
  .fold(0)((count, _) => count + 1)
  .mergeSubstreams
  .runWith(Sink.seq)
```

---

## সারাংশ
স্কালা একটি শক্তিশালী ভাষা যা JVM-এ কার্যকরী প্রোগ্রামিং নিয়ে আসে। এটি Apache Spark-এর ভাষা এবং ডেটা ইঞ্জিনিয়ারিং, ডিস্ট্রিবিউটেড সিস্টেম এবং ব্যাকএন্ড পরিষেবাগুলির জন্য একটি শক্তিশালী পছন্দ। শেখার বক্ররেখা বাস্তব, কিন্তু অর্থ প্রদান হল একটি ভাষা যা অভিব্যক্তিপূর্ণ এবং কার্যকারিতা উভয়ই। JVM ইকোসিস্টেমে ইতিমধ্যেই বিনিয়োগ করা দলগুলির জন্য, Scala জাভার আরও সংক্ষিপ্ত এবং শক্তিশালী বিকল্প অফার করে।