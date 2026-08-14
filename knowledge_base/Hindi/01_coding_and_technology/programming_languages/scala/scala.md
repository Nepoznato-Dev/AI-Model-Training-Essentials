<!--
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

-->
# स्काला
स्काला (स्केलेबल लैंग्वेज) एक सांख्यिकीय रूप से टाइप की गई, संकलित प्रोग्रामिंग भाषा है जो ऑब्जेक्ट-ओरिएंटेड और कार्यात्मक प्रोग्रामिंग प्रतिमानों को जोड़ती है। मार्टिन ओडरस्की द्वारा निर्मित और पहली बार 2004 में रिलीज़ किया गया, स्काला JVM (जावास्क्रिप्ट और स्काला नेटिव के लिए Scala.js भी) पर चलता है। इसे पूर्ण जावा इंटरऑपरेबिलिटी को बनाए रखते हुए जावा की वर्बोसिटी को संबोधित करने के लिए डिज़ाइन किया गया था।
स्काला अपाचे स्पार्क (बड़ा डेटा प्रोसेसिंग ढांचा) के पीछे की भाषा है, और इसका उपयोग डेटा इंजीनियरिंग, वितरित सिस्टम और बैकएंड सेवाओं में बड़े पैमाने पर किया जाता है। ट्विटर (अब एक्स), लिंक्डइन, नेटफ्लिक्स और द गार्जियन जैसी कंपनियां स्काला का उपयोग करती हैं।
---

## स्काला क्यों मायने रखता है
- **कार्यात्मक + ओओपी हाइब्रिड**: एक ही भाषा में दोनों प्रतिमानों के सर्वश्रेष्ठ को संयोजित करता है।
- **संक्षिप्त**: जावा की तुलना में काफी कम क्रियात्मकता - पैटर्न मिलान, केस क्लास, प्रकार अनुमान।
- **अपाचे स्पार्क**: स्पार्क-आधारित बड़े डेटा प्रोसेसिंग के लिए प्राथमिक भाषा।
- **प्रकार प्रणाली**: अंतर्निहित, प्रकार वर्ग और बीजगणितीय डेटा प्रकार जैसी उन्नत सुविधाएँ।
- **जेवीएम अनुकूलता**: सभी जावा लाइब्रेरी का उपयोग करता है; उसी JVM पर चलता है.
- **अक्का/पेक्को**: समवर्ती, वितरित प्रणालियों के निर्माण के लिए लोकप्रिय ढांचा।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **जटिलता** | भाषा में अनेक विशेषताएँ होती हैं; महारत हासिल करना कठिन हो सकता है | "अच्छे भागों" से प्रारंभ करें; अत्यधिक चतुर कोड से बचें |
| **संकलन समय** | जावा से धीमा, विशेष रूप से जटिल प्रकारों के साथ | वृद्धिशील संकलन (ब्लूप, एसबीटी) का उपयोग करें |
| **सीखने की अवस्था** | जावा या पायथन से भी तेज़ | निवेश का समय; अदायगी महत्वपूर्ण है |
| **छोटा नौकरी बाज़ार** | जावा या पायथन की तुलना में कम भूमिकाएँ | डेटा इंजीनियरिंग और बैकएंड भूमिकाओं में मजबूत |
| **असंगत शैली** | अलग-अलग टीमें बहुत अलग स्काला लिखती हैं | सामुदायिक शैली दिशानिर्देशों का पालन करें |
---

## सिंटेक्स बुनियादी बातें
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

## उन्नत सिंटैक्स और पैटर्न
### प्रकार की कक्षाएं (अंतर्निहित के माध्यम से)
स्काला 2 प्रकार की कक्षाओं को एन्कोड करने के लिए अंतर्निहित पैरामीटर का उपयोग करता है। स्काला 3 मूल`given`/`using`सिंटैक्स का परिचय देता है।
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

### सीलबंद लक्षण और गणना (स्कैला 3 एनम्स)
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

### उन्नत प्रकार की सिस्टम सुविधाएँ
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

## समवर्ती एवं समांतरता
### भविष्य और वादे
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

### ZIO - आधुनिक प्रभाव प्रणाली
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

### अक्का/पेक्को अभिनेता
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना (एसबीटी)
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

### बिल्ड कॉन्फ़िगरेशन (बिल्ड.एसबीटी)
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

### कुंजी निर्माण आदेश
| आदेश | विवरण |
|---------|-----------------|
| `sbt new scala/scala3.g8`| टेम्पलेट से नया स्काला 3 प्रोजेक्ट बनाएं |
| `sbt compile`| मुख्य स्त्रोत संकलित करें |
| `sbt test`| सभी परीक्षण चलाएँ |
| `sbt run`| मुख्य कक्षा चलाएं |
| `sbt runMain com.example.App`| एक विशिष्ट मुख्य वर्ग चलाएँ |
| `sbt console`| क्लासपाथ | पर प्रोजेक्ट के साथ आरईपीएल प्रारंभ करें
| `sbt clean`| स्वच्छ संकलित आउटपुट |
| `sbt assembly`| फैट जार बनाएं (एसबीटी-असेंबली प्लगइन के साथ) |
| `sbt scalafmt`| Scalafmt | के साथ कोड प्रारूपित करें
| `sbt scalafmtCheck`| कोड फ़ॉर्मेटिंग की जाँच करें |
| `sbt ~compile`| सतत संकलन (परिवर्तन पर पुनः संकलन) |
### कोड फ़ॉर्मेटिंग (.scaleafmt.conf)
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

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### स्कैलाटेस्ट - व्यापक परीक्षण
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

### स्कैलाचेक - संपत्ति-आधारित परीक्षण
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

### ZIO टेस्ट
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

## अंतरसंचालनीयता
### जेवीएम इंटरऑपरेबिलिटी
स्काला के पास सभी जावा लाइब्रेरीज़ तक निर्बाध पहुंच है।
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

### नेटिव इंटरऑप (स्कैला नेटिव)
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

## डिज़ाइन पैटर्न
### बिल्लियों के साथ टैग रहित फ़ाइनल
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

### ZIO परत पैटर्न
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

### त्रुटि प्रबंधन के साथ रिपॉजिटरी पैटर्न
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
| उपकरण | उद्देश्य | उपयोग |
|------|------|-------|
| **जेएमएच** | माइक्रो-बेंचमार्किंग | `sbt-jmh`प्लगइन |
| **विजुअलवीएम** | जेवीएम प्रोफाइलिंग और निगरानी | `jvisualvm`कमांड |
| **एसिंक प्रोफाइलर** | लो-ओवरहेड सीपीयू/मेमोरी प्रोफाइलिंग | चल रहे JVM से संलग्न करें |
| **आपकी किट** | वाणिज्यिक प्रोफाइलर | आईडीई एकीकरण |
| **एसबीटी-कवरेज** | कोड कवरेज | `sbt coverage test coverageReport`|
### जेएमएच के साथ बेंचमार्किंग
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

### अनुकूलन तकनीकें
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

## तैनाती
### मोटे जार का निर्माण
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

### डॉकर परिनियोजन
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

### GraalVM मूल छवि
```scala
// build.sbt — enable Scala Native or use GraalVM
// For GraalVM native-image:
// native-image --static -jar target/scala-3.3.1/my-app.jar -o my-app
```

---

## स्काला का उपयोग कब करें
| परिदृश्य | स्काला क्यों | बेहतर विकल्प |
|---|---|-----|
| बिग डेटा (स्पार्क) | प्राथमिक स्पार्क भाषा | सरल पाइपलाइनों के लिए पायथन (पायस्पार्क) |
| वितरित सिस्टम (अक्का) | परिपक्व समवर्ती रूपरेखा | जाओ, एरलांग/एलिक्सिर |
| जेवीएम बैकएंड | संक्षिप्त जावा विकल्प | जावा, कोटलिन |
| जेवीएम पर कार्यात्मक प्रोग्रामिंग | सर्वोत्तम एफपी + जेवीएम संयोजन | क्लोजर |
| सामान्य अनुप्रयोग विकास | संभव लेकिन जटिल | पायथन, गो, जावा |
| डेटा विज्ञान | संभव है लेकिन पारिस्थितिकी तंत्र नहीं | पायथन, आर |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: स्काला का प्रकार अनुमान जावा की तुलना में बॉयलरप्लेट को कैसे कम करता है?
**ए:** स्काला का कंपाइलर`val`/`var`घोषणाओं, विधि रिटर्न प्रकारों और अनाम कार्यों के प्रकारों का अनुमान लगाता है। यह अधिकांश मामलों में स्पष्ट प्रकार के एनोटेशन की आवश्यकता को समाप्त कर देता है:
```scala
// Java: explicit types everywhere
Map<String, List<Integer>> grouped = new HashMap<>();
// Scala: types inferred
val grouped = items.groupBy(_.category)
```

कंपाइलर प्रकार के पैरामीटर, एकल-अभिव्यक्ति विधियों के रिटर्न प्रकार और पैटर्न मिलान प्रकारों का भी अनुमान लगाता है। यह सुरक्षा से समझौता किए बिना कोड को संक्षिप्त बनाता है।
### Q2: मुझे`case class`बनाम नियमित`class`का उपयोग कब करना चाहिए?
**ए:** अपरिवर्तनीय डेटा वाहक के लिए`case class`का उपयोग करें - वे `equals`, `hashCode`, `toString`, `copy`, और पैटर्न मिलान समर्थन स्वचालित रूप से प्रदान करते हैं:
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

सामान्य नियम: यदि आपकी कक्षा मुख्य रूप से डेटा है, तो`case class`का उपयोग करें। यदि इसकी परिवर्तनशील स्थिति या जटिल व्यवहार है, तो नियमित`class`का उपयोग करें।
### Q3: मैं स्काला में त्रुटियों को मुहावरेदार तरीके से कैसे संभालूं?
**ए:** स्काला अपवादों को छोड़कर`Option`,`Either`, और`Try`जैसे प्रकारों को वापस करने का पक्षधर है:
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

### Q4:`trait`और`abstract class`के बीच क्या अंतर है?
**ए:** लक्षण एकाधिक वंशानुक्रम का समर्थन करते हैं और इसमें प्रकार के पैरामीटर और ठोस तरीके हो सकते हैं। सार वर्गों में कंस्ट्रक्टर पैरामीटर हो सकते हैं लेकिन केवल एकल वंशानुक्रम का समर्थन करते हैं:
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

### Q5: मैं जेवीएम पर परफॉर्मेंट स्काला कोड कैसे लिखूं?
**ए:** मुख्य अभ्यास:
- सिंक्रनाइज़ेशन से बचने के लिए`case class`और अपरिवर्तनीय डेटा का उपयोग करें
- संरचनात्मक साझाकरण के लिए `Vector`,`Map`(अपरिवर्तनीय) को प्राथमिकता दें
- टेल-कॉल ऑप्टिमाइज़ेशन सुनिश्चित करने के लिए`@tailrec`एनोटेशन का उपयोग करें
- अत्यधिक मुक्केबाजी से बचें -`Int`,`Double`आदिम का उपयोग करें
- महंगी गणनाओं के लिए`lazy val`का उपयोग करें
- बड़े अनुक्रमों के लिए`Stream`/`LazyList`को प्राथमिकता दें
- जेएमएच के साथ प्रोफाइल - स्काला के सार को कुशल बाइटकोड में संकलित किया जाना चाहिए
---

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: एक प्रकार-सुरक्षित अभिव्यक्ति मूल्यांकनकर्ता को लागू करना
**चरण 1: समस्या को समझें**
हमें जोड़, गुणा और चर लुकअप का समर्थन करते हुए चर के साथ गणितीय अभिव्यक्तियों का मूल्यांकन करने की आवश्यकता है।
**चरण 2: दृष्टिकोण को पहचानें**
अभिव्यक्ति वृक्ष को मॉडल करने के लिए बीजगणितीय डेटा प्रकारों (सीलबंद विशेषता + केस वर्ग) का उपयोग करें, फिर मूल्यांकन करने के लिए पैटर्न मिलान करें।
**चरण 3: कार्यान्वयन**```scala
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

**चरण 4: सत्यापित करें और विस्तार करें**
`Div` ,`Pow`,`Neg`मामले जोड़ें। सीलबंद विशेषता यह सुनिश्चित करती है कि संकलक गैर-विस्तृत मिलानों के बारे में चेतावनी दे।
### समस्या 2: HTML जेनरेशन के लिए एक सरल डीएसएल बनाना
**चरण 1: समस्या को समझें**
एक प्रकार-सुरक्षित डीएसएल बनाएं जो स्काला के सिंटैक्स का उपयोग करके HTML स्ट्रिंग उत्पन्न करता है।
**चरण 2: दृष्टिकोण को पहचानें**
HTML तत्वों के लिए केस क्लास और प्राकृतिक सिंटैक्स के लिए अंतर्निहित रूपांतरण का उपयोग करें।
**चरण 3: कार्यान्वयन**```scala
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

**चरण 4: सत्यापित करें**
डीएसएल टाइप-सुरक्षित है - आप गलती से गैर-एचटीएमएल सामग्री पास नहीं कर सकते।`HtmlNode`पर पैटर्न मिलान संपूर्ण रेंडरिंग सुनिश्चित करता है।
### समस्या 3: अक्का स्ट्रीम के साथ समवर्ती शब्द गणना
**चरण 1: समस्या को समझें**
एक साथ कई बड़ी फ़ाइलों में शब्द आवृत्तियों की गणना करें।
**चरण 2: दृष्टिकोण को पहचानें**
समवर्ती प्रसंस्करण के लिए स्काला के समानांतर संग्रह या अक्का स्ट्रीम का उपयोग करें, फिर परिणामों को मर्ज करें।
**चरण 3: कार्यान्वयन**```scala
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

**चरण 4: अनुकूलन करें**
बहुत बड़े डेटासेट के लिए, बैकप्रेशर के साथ अक्का स्ट्रीम का उपयोग करें:```scala
Source(fileList)
  .mapAsync(4)(file => Future(Source.fromFile(file).getLines().toList))
  .mapConcat(identity)
  .groupBy(256, _.toLowerCase)
  .fold(0)((count, _) => count + 1)
  .mergeSubstreams
  .runWith(Sink.seq)
```

---

## सारांश
स्काला एक शक्तिशाली भाषा है जो जेवीएम में कार्यात्मक प्रोग्रामिंग लाती है। यह अपाचे स्पार्क की भाषा है और डेटा इंजीनियरिंग, वितरित सिस्टम और बैकएंड सेवाओं के लिए एक मजबूत विकल्प है। सीखने की अवस्था वास्तविक है, लेकिन भुगतान एक ऐसी भाषा है जो अभिव्यंजक और प्रदर्शनकारी दोनों है। JVM पारिस्थितिकी तंत्र में पहले से ही निवेशित टीमों के लिए, स्काला जावा का अधिक संक्षिप्त और शक्तिशाली विकल्प प्रदान करता है।