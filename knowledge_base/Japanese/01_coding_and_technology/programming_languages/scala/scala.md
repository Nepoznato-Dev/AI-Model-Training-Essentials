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

#スカラ
Scala (スケーラブル言語) は、オブジェクト指向と関数型プログラミングのパラダイムを組み合わせた、静的に型指定され、コンパイルされたプログラミング言語です。 Martin Odersky によって作成され、2004 年に最初にリリースされた Scala は、JVM (JavaScript および Scala Native 用の Scala.js も) 上で実行されます。これは、Java の完全な相互運用性を維持しながら、Java の冗長性に対処するように設計されました。
Scala は、Apache Spark (ビッグ データ処理フレームワーク) の背後にある言語であり、データ エンジニアリング、分散システム、バックエンド サービスで広く使用されています。 Twitter (現在は X)、LinkedIn、Netflix、The Guardian などの企業が Scala を使用しています。
---

## Scala が重要な理由
- **関数型 + OOP ハイブリッド**: 両方のパラダイムの長所を 1 つの言語に組み合わせます。
- **簡潔**: Java よりも大幅に冗長ではありません (パターン マッチング、ケース クラス、型推論)。
- **Apache Spark**: Spark ベースのビッグ データ処理のための主要言語。
- **型システム**: 暗黙的、型クラス、代数データ型などの高度な機能。
- **JVM 互換性**: すべての Java ライブラリを使用します。同じ JVM 上で実行されます。
- **Akka / Pekko**: 同時分散システムを構築するための人気のあるフレームワーク。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **複雑さ** |この言語には多くの機能があります。マスターするのは難しいかもしれません | 「良い部分」から始めましょう。過度に巧妙なコードを避ける |
| **コンパイル時間** |特に複雑な型の場合、Java よりも遅い |インクリメンタル コンパイル (Bloop、sbt) を使用する |
| **学習曲線** | Java や Python より急勾配 |時間を投資してください。見返りは大きい |
| **小規模な雇用市場** | Java や Python よりもロールが少ない |データエンジニアリングとバックエンドの役割に強い |
| **一貫性のないスタイル** |チームが異なれば、非常に異なる Scala を作成します。コミュニティのスタイルガイドに従ってください |
---

## 構文の基礎
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

## 高度な構文とパターン
### 型クラス (暗黙的経由)
Scala 2 は、暗黙的なパラメーターを使用して型クラスをエンコードします。 Scala 3 では、ネイティブ`given`/`using`構文が導入されています。
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

### シールされた特性と列挙型 (Scala 3 列挙型)
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

### 高度な型システムの機能
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

## 同時実行性と並列処理
### 将来と約束
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

### ZIO — モダンなエフェクト システム
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

### アッカ/ペッコの俳優
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

## プロジェクトの構成とシステムの構築
### プロジェクト構造 (sbt)
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

### ビルド構成 (build.sbt)
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

### 主要なビルド コマンド
|コマンド |説明 |
|----------|---------------|
| `sbt new scala/scala3.g8`|テンプレートから新しい Scala 3 プロジェクトを作成する |
| `sbt compile`|主要なソースをコンパイルする |
| `sbt test`|すべてのテストを実行する |
| `sbt run`|メインクラスを実行します |
| `sbt runMain com.example.App`|特定のメインクラスを実行する |
| `sbt console`|クラスパス上のプロジェクトで REPL を開始します |
| `sbt clean`|クリーンなコンパイル済み出力 |
| `sbt assembly`| fat JAR をビルドする (sbt-assembly プラグインを使用) |
| `sbt scalafmt`| Scalafmt でコードをフォーマットする |
| `sbt scalafmtCheck`|コードのフォーマットをチェックする |
| `sbt ~compile`|継続的コンパイル (変更時に再コンパイル) |
### コードのフォーマット (.scalafmt.conf)
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

### CI/CD パイプライン (GitHub アクション)
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

## テスト
### ScalaTest — 包括的なテスト
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

### ScalaCheck — プロパティベースのテスト
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

### ZIO テスト
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

## 相互運用性
### JVM の相互運用性
Scala はすべての Java ライブラリにシームレスにアクセスできます。
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

### ネイティブ相互運用性 (Scala ネイティブ)
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

## デザインパターン
### Catsとのタグレス決勝戦
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

### ZIO レイヤー パターン
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

### エラー処理を伴うリポジトリ パターン
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

## パフォーマンスと最適化
### プロファイリングツール
|ツール |目的 |使い方 |
|------|-------|------|
| **JMH** |マイクロベンチマーク | `sbt-jmh`プラグイン |
| **VisualVM** | JVM プロファイリングとモニタリング | `jvisualvm`コマンド |
| **非同期プロファイラー** |低オーバーヘッドの CPU/メモリ プロファイリング |実行中の JVM に接続する |
| **あなたのキット** |商用プロファイラー | IDE の統合 |
| **sbt-scoverage** |コードカバレッジ | `sbt coverage test coverageReport`|
### JMH によるベンチマーク
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

### 最適化手法
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

## デプロイメント
### Fat JAR の構築
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

### Docker のデプロイメント
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

### GraalVM ネイティブ イメージ
```scala
// build.sbt — enable Scala Native or use GraalVM
// For GraalVM native-image:
// native-image --static -jar target/scala-3.3.1/my-app.jar -o my-app
```

---

## Scala を使用する場合
|シナリオ |なぜスカラなのか |より良い代替案 |
|----------|----------|----------|
|ビッグデータ (Spark) |主要な Spark 言語 |より単純なパイプラインのための Python (PySpark) |
|分散システム (Akka) |成熟した同時実行フレームワーク |行く、Erlang/Elixir |
| JVM バックエンド |簡潔な Java 代替案 | Java、Kotlin |
| JVM での関数型プログラミング | FP + JVM の最適な組み合わせ |クロジュア |
|一般的なアプリケーション開発 |可能だが複雑 | Python、Go、Java |
|データサイエンス |可能だがエコシステムでは不可能 |パイソン、R |
---

## 総合的な Q&A
### Q1: Scala の型推論は Java と比較してどのように定型句を削減しますか?
**A:** Scala のコンパイラは、`val` /`var`宣言、メソッドの戻り値の型、および匿名関数の型を推論します。これにより、ほとんどの場合、明示的な型アノテーションが不要になります。
```scala
// Java: explicit types everywhere
Map<String, List<Integer>> grouped = new HashMap<>();
// Scala: types inferred
val grouped = items.groupBy(_.category)
```

コンパイラは、型パラメーター、単一式メソッドの戻り型、およびパターン一致型も推論します。これにより、安全性を犠牲にすることなくコードが簡潔になります。
### Q2: 通常の`class`ではなく、どのような場合に`case class`を使用する必要がありますか?
**A:** 不変データ キャリアには`case class`を使用します。これらは、`equals`、`hashCode`、`toString`、`copy`、およびパターン マッチング サポートを自動的に提供します。
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

経験則: クラスが主にデータである場合は、`case class`を使用します。変更可能な状態または複雑な動作がある場合は、通常の`class`を使用します。
### Q3: Scala でエラーを慣用的に処理するにはどうすればよいですか?
**A:** Scala は、例外をスローするよりも、`Option`、`Either`、`Try`のような型を返すことを優先します。
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

### Q4:`trait`と`abstract class`の違いは何ですか?
**A:** 特性は多重継承をサポートしており、型パラメーターと具象メソッドを持つことができます。抽象クラスはコンストラクター パラメーターを持つことができますが、単一の継承のみをサポートします。
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

### Q5: JVM 上でパフォーマンスの高い Scala コードを記述するにはどうすればよいですか?
**A:** 主な実践方法:
- 同期を回避するには、`case class` と不変データを使用します。
- 構造共有には`Vector`、`Map`(不変) を優先します
-`@tailrec`アノテーションを使用して末尾呼び出しの最適化を保証します
- 過度のボックス化を避け、`Int`、`Double`プリミティブを使用します。
- 高価な計算には`lazy val`を使用します
- 大きなシーケンスには`Stream`/`LazyList`を優先します
- JMH によるプロファイル — Scala の抽象化は効率的なバイトコードにコンパイルされる必要があります
---

## 思考連鎖による問題解決
### 問題 1: タイプセーフな式評価器の実装
**ステップ 1: 問題を理解する**
変数を使用して数式を評価し、加算、乗算、変数の検索をサポートする必要があります。
**ステップ 2: アプローチを特定する**
代数データ型 (シールされた特性 + ケース クラス) を使用して式ツリーをモデル化し、パターン マッチで評価します。
**ステップ 3: 実装**```scala
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

**ステップ 4: 検証と拡張**
`Div` 、`Pow`、`Neg`のケースを追加します。 sealed 特性により、コンパイラーは非完全な一致について警告を発します。
### 問題 2: HTML 生成用の単純な DSL の構築
**ステップ 1: 問題を理解する**
Scala の構文を使用して HTML 文字列を生成するタイプセーフ DSL を作成します。
**ステップ 2: アプローチを特定する**
HTML 要素のユースケース クラスと自然な構文の暗黙的な変換。
**ステップ 3: 実装**```scala
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

**ステップ 4: 確認**
DSL はタイプセーフです。誤って非 HTML コンテンツを渡すことはできません。`HtmlNode`のパターン マッチングにより、徹底的なレンダリングが保証されます。
### 問題 3: Akka ストリームでの同時ワード数
**ステップ 1: 問題を理解する**
複数の大きなファイルの単語頻度を同時にカウントします。
**ステップ 2: アプローチを特定する**
Scala の並列コレクションまたは Akka Streams を同時処理に使用し、結果をマージします。
**ステップ 3: 実装**```scala
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

**ステップ 4: 最適化**
非常に大規模なデータセットの場合は、バックプレッシャーを備えた Akka Streams を使用します。```scala
Source(fileList)
  .mapAsync(4)(file => Future(Source.fromFile(file).getLines().toList))
  .mapConcat(identity)
  .groupBy(256, _.toLowerCase)
  .fold(0)((count, _) => count + 1)
  .mergeSubstreams
  .runWith(Sink.seq)
```

---

＃＃ まとめ
Scala は、JVM に関数型プログラミングをもたらす強力な言語です。これは Apache Spark の言語であり、データ エンジニアリング、分散システム、バックエンド サービスにとって強力な選択肢です。学習には時間がかかりますが、その成果は表現力とパフォーマンスの両方を備えた言語です。すでに JVM エコシステムに投資しているチームにとって、Scala は Java のより簡潔で強力な代替手段を提供します。