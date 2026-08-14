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
# Scala
Scala (Ölçeklenebilir Dil), nesne yönelimli ve işlevsel programlama paradigmalarını birleştiren statik olarak yazılmış, derlenmiş bir programlama dilidir. Martin Odersky tarafından oluşturulan ve ilk olarak 2004'te piyasaya sürülen Scala, JVM (aynı zamanda JavaScript ve Scala Native için Scala.js) üzerinde çalışır. Tam Java birlikte çalışabilirliğini korurken Java'nın ayrıntılarını gidermek için tasarlanmıştır.
Scala, Apache Spark'ın (büyük veri işleme çerçevesi) arkasındaki dildir ve veri mühendisliğinde, dağıtılmış sistemlerde ve arka uç hizmetlerinde yaygın olarak kullanılır. Twitter (şimdi X), LinkedIn, Netflix ve The Guardian gibi şirketler Scala'yı kullanıyor.
---

## Scala Neden Önemlidir
- **İşlevsel + OOP hibrit**: Her iki paradigmanın en iyi yönlerini tek bir dilde birleştirir.
- **Kısa**: Java'dan önemli ölçüde daha az ayrıntı içerir — kalıp eşleştirme, vaka sınıfları, tür çıkarımı.
- **Apache Spark**: Spark tabanlı büyük veri işleme için birincil dil.
- **Tür sistemi**: Örtülüler, tür sınıfları ve cebirsel veri türleri gibi gelişmiş özellikler.
- **JVM uyumluluğu**: Tüm Java kitaplıklarını kullanır; aynı JVM üzerinde çalışır.
- **Akka / Pekko**: Eşzamanlı, dağıtılmış sistemler oluşturmaya yönelik popüler çerçeve.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Karmaşıklık** | Dilin birçok özelliği vardır; ustalaşması zor olabilir | "İyi kısımlarla" başlayın; aşırı akıllı kodlardan kaçının |
| **Derleme zamanları** | Özellikle karmaşık türlerde Java'dan daha yavaş | Artımlı derlemeyi kullanın (Bloop, sbt) |
| **Öğrenme eğrisi** | Java veya Python'dan daha dik | Zamana yatırım yapın; getirisi önemli |
| **Daha küçük iş piyasası** | Java veya Python'dan daha az rol | Veri mühendisliği ve arka uç rollerinde güçlü |
| **Tutarsız stil** | Farklı takımlar çok farklı Scala yazıyor | Topluluk stili kılavuzlarını takip edin |
---

## Söz Diziminin Temelleri
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

## Gelişmiş Sözdizimi ve Desenler
### Sınıfları Yazın (örtükler yoluyla)
Scala 2, tür sınıflarını kodlamak için örtülü parametreler kullanır. Scala 3, yerel`given`/`using`sözdizimini sunar.
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

### Mühürlü Özellikler ve Numaralandırmalar (Scala 3 Numaralandırmaları)
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

### Gelişmiş Tip Sistem Özellikleri
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

## Eşzamanlılık ve Paralellik
### Vadeli İşlemler ve Vaatler
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

### ZIO — Modern Efekt Sistemi
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

### Akka/Pekko Aktörleri
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı (sbt)
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

### Yapı Yapılandırması (build.sbt)
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

### Anahtar Oluşturma Komutları
| Komut | Açıklama |
|-----------|------------|
| `sbt new scala/scala3.g8`| Şablondan yeni Scala 3 projesi oluşturun |
| `sbt compile`| Ana kaynakları derleyin |
| `sbt test`| Tüm testleri çalıştırın |
| `sbt run`| Ana sınıfı çalıştırın |
| `sbt runMain com.example.App`| Belirli bir ana sınıfı çalıştırın |
| `sbt console`| REPL'i sınıf yolundaki projeyle başlatın |
| `sbt clean`| Derlenmiş çıktıyı temizle |
| `sbt assembly`| Fat JAR oluşturun (sbt-derleme eklentisi ile) |
| `sbt scalafmt`| Kodu Scalafmt ile biçimlendirme |
| `sbt scalafmtCheck`| Kod biçimlendirmesini kontrol edin |
| `sbt ~compile`| Sürekli derleme (değişimde yeniden derleme) |
### Kod Biçimlendirmesi (.scalafmt.conf)
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

### CI/CD İşlem Hattı (GitHub Eylemleri)
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

## Test etme
### ScalaTest — Kapsamlı Test
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

### ScalaCheck — Özellik Tabanlı Test
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

### ZIO Testi
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

## Birlikte Çalışabilirlik
### JVM Birlikte Çalışabilirliği
Scala'nın tüm Java kitaplıklarına kesintisiz erişimi vardır.
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

### Yerel Birlikte Çalışma (Scala Yerel)
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

## Tasarım Desenleri
### Kedilerle Etiketsiz Final
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

### ZIO Katman Deseni
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

### Hata İşleme ile Depo Modeli
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

## Performans ve Optimizasyon
### Profil Oluşturma Araçları
| Araç | Amaç | Kullanım |
|------|------------|-------|
| **JMH** | Mikro kıyaslama | `sbt-jmh`eklentisi |
| **GörselVM** | JVM profil oluşturma ve izleme | `jvisualvm`komutu |
| **Async Profiler** | Düşük maliyetli CPU/bellek profili oluşturma | Çalışan JVM'ye ekle |
| **Kitiniz** | Ticari profil oluşturucu | IDE entegrasyonu |
| **sbt kapsamı** | Kod kapsamı | `sbt coverage test coverageReport`|
### JMH ile kıyaslama
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

### Optimizasyon Teknikleri
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

## Dağıtım
### Yağ JAR'ları Oluşturmak
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

### Docker Dağıtımı
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

### GraalVM Yerel Görüntüsü
```scala
// build.sbt — enable Scala Native or use GraalVM
// For GraalVM native-image:
// native-image --static -jar target/scala-3.3.1/my-app.jar -o my-app
```

---

## Scala Ne Zaman Kullanılmalı?
| Senaryo | Neden Scala | Daha İyi Alternatif |
|----------|----------|----------|
| Büyük veri (Spark) | Birincil Spark dili | Daha basit işlem hatları için Python (PySpark) |
| Dağıtık sistemler (Akka) | Olgun eşzamanlılık çerçevesi | Git, Erlang/İksir |
| JVM arka uçları | Kısa Java alternatifi | Java, Kotlin |
| JVM'de fonksiyonel programlama | En iyi FP + JVM kombinasyonu | Clojure |
| Genel uygulama geliştirme | Mümkün ama karmaşık | Python, Git, Java |
| Veri bilimi | Mümkün ama ekosistem değil | Python, R |
---

## Sentetik Soru-Cevap
### S1: Scala'nın tür çıkarımı, Java'ya kıyasla ortak metni nasıl azaltır?
**C:** Scala'nın derleyicisi,`val`/`var`bildirimleri, yöntem dönüş türleri ve anonim işlevler için türler çıkarır. Bu, çoğu durumda açık tür açıklamalarına olan ihtiyacı ortadan kaldırır:
```scala
// Java: explicit types everywhere
Map<String, List<Integer>> grouped = new HashMap<>();
// Scala: types inferred
val grouped = items.groupBy(_.category)
```

Derleyici ayrıca tür parametrelerini, tek ifadeli yöntemlerin dönüş türlerini ve kalıp eşleşme türlerini de çıkarır. Bu, güvenlikten ödün vermeden kodun kısa olmasını sağlar.
### S2: `case class`'yi normal `class`'ye karşı ne zaman kullanmalıyım?
**C:** Değişmez veri taşıyıcılar için`case class`kullanın —`equals`,`hashCode`,`toString`,`copy`ve desen eşleştirme desteğini otomatik olarak sağlarlar:
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

Temel kural: Sınıfınız öncelikle veriden oluşuyorsa`case class`kullanın. Değişken durumu veya karmaşık davranışı varsa normal bir`class`kullanın.
### S3: Scala'da hataları deyimsel olarak nasıl ele alabilirim?
**C:** Scala, istisnaları atmak yerine`Option`,`Either`ve`Try`gibi geri dönen türleri tercih eder:
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

### S4:`trait`ile`abstract class`arasındaki fark nedir?
**C:** Özellikler çoklu kalıtımı destekler ve tür parametrelerine ve somut yöntemlere sahip olabilir. Soyut sınıflar yapıcı parametrelere sahip olabilir ancak yalnızca tekli mirası destekler:
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

### S5: Performanslı Scala kodunu JVM'ye nasıl yazarım?
**C:** Temel uygulamalar:
- Senkronizasyonu önlemek için`case class`ve değişmez verileri kullanın
- Yapısal paylaşım için `Vector`,`Map`(değişmez) tercih edin
- Kuyruk çağrısı optimizasyonunu sağlamak için`@tailrec`ek açıklamasını kullanın
- Aşırı bokstan kaçının —`Int`,`Double`temel öğelerini kullanın
- Pahalı hesaplamalar için`lazy val`kullanın
- Büyük sekanslar için`Stream`/ `LazyList`'yi tercih edin
- JMH ile profil — Scala'nın soyutlamaları verimli bayt koduna göre derlenmelidir
---

## Düşünce Zinciri Problem Çözme
### Sorun 1: Güvenli Tip İfade Değerlendiricisinin Uygulanması
**1. Adım: Sorunu Anlayın**
Toplama, çarpma ve değişken aramayı destekleyen değişkenlerle matematiksel ifadeleri değerlendirmemiz gerekiyor.
**2. Adım: Yaklaşımı Belirleyin**
İfade ağacını modellemek için cebirsel veri türlerini (mühürlü özellik + vaka sınıfları) kullanın, ardından değerlendirmek için desen eşleşmesini kullanın.
**3. Adım: Uygulama**```scala
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

**4. Adım: Doğrulayın ve Genişletin**
`Div` ,`Pow`,`Neg`kasalarını ekleyin. Mühürlü özellik, derleyicinin kapsamlı olmayan eşleşmeler hakkında uyarmasını sağlar.
### Sorun 2: HTML Oluşturma için Basit bir DSL Oluşturma
**1. Adım: Sorunu Anlayın**
Scala'nın sözdizimini kullanarak HTML dizeleri üreten, tür açısından güvenli bir DSL oluşturun.
**2. Adım: Yaklaşımı Belirleyin**
HTML öğeleri için vaka sınıflarını ve doğal bir sözdizimi için örtülü dönüşümleri kullanın.
**3. Adım: Uygulama**```scala
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

**4. Adım: Doğrulayın**
DSL tür açısından güvenlidir; yanlışlıkla HTML olmayan içeriği iletemezsiniz.`HtmlNode`üzerinde desen eşleştirme, kapsamlı işlemeyi garanti eder.
### Sorun 3: Akka Akışlarıyla Eşzamanlı Kelime Sayısı
**1. Adım: Sorunu Anlayın**
Birden fazla büyük dosyadaki kelime frekanslarını aynı anda sayın.
**2. Adım: Yaklaşımı Belirleyin**
Eşzamanlı işleme için Scala'nın paralel koleksiyonlarını veya Akka Streams'i kullanın, ardından sonuçları birleştirin.
**3. Adım: Uygulama**```scala
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

**4. Adım: Optimize edin**
Çok büyük veri kümeleri için karşı basınçla Akka Streams'i kullanın:```scala
Source(fileList)
  .mapAsync(4)(file => Future(Source.fromFile(file).getLines().toList))
  .mapConcat(identity)
  .groupBy(256, _.toLowerCase)
  .fold(0)((count, _) => count + 1)
  .mergeSubstreams
  .runWith(Sink.seq)
```

---

## Özet
Scala, JVM'ye işlevsel programlama getiren güçlü bir dildir. Apache Spark'ın dilidir ve veri mühendisliği, dağıtılmış sistemler ve arka uç hizmetleri için güçlü bir seçimdir. Öğrenme eğrisi gerçektir, ancak getirisi hem ifade edici hem de performanslı bir dildir. Zaten JVM ekosistemine yatırım yapmış ekipler için Scala, Java'ya daha kısa ve güçlü bir alternatif sunuyor.