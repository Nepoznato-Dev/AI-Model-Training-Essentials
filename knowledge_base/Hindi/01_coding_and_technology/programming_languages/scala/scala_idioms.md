---
# Metadata
title: "Scala — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, functional Scala code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [scala, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# स्काला - मुहावरेदार पैटर्न और सर्वोत्तम अभ्यास
यह मार्गदर्शिका स्वच्छ, कार्यात्मक स्काला 3 कोड लिखने के लिए मुहावरेदार पैटर्न और सर्वोत्तम प्रथाओं को शामिल करती है।
---

## स्काला 3 सिंटैक्स
```scala
// ✅ val by default, var only when needed
val name = "Alice"
var count = 0

// ✅ Indentation-based syntax (optional braces)
def greet(name: String): String =
  s"Hello, $name!"

// ✅ Enum (Scala 3)
enum Color:
  case Red, Green, Blue
  case Custom(r: Int, g: Int, b: Int)

// ✅ Opaque types (Scala 3)
opaque type UserId = Long
object UserId:
  def apply(value: Long): UserId = value

// ✅ Export (Scala 3)
class Database:
  private val connection = connect()
  export connection.{query, execute}
```

---

## पैटर्न मिलान
```scala
// ✅ Exhaustive pattern matching
def describe(x: Any): String = x match
  case i: Int if i > 0 => s"Positive: $i"
  case i: Int if i < 0 => s"Negative: $i"
  case 0               => "Zero"
  case s: String       => s"String: $s"
  case _               => "Unknown"

// ✅ Sealed types for exhaustive matching
sealed trait Shape
case class Circle(radius: Double) extends Shape
case class Rectangle(width: Double, height: Double) extends Shape

def area(shape: Shape): Double = shape match
  case Circle(r)       => math.Pi * r * r
  case Rectangle(w, h) => w * h

// ✅ Pattern matching in val
val (name, age) = person
val head :: tail = list
```

---

## विकल्प और कोई भी
```scala
// ✅ Option for optional values
def findUser(id: Long): Option[User] = ...

val name = user.map(_.name).getOrElse("Unknown")
val result = user.fold("not found")(_.name)

// ✅ For-comprehension for Option chaining
val result = for
  user <- findUser(id)
  order <- findOrder(user.orderId)
yield order.total

// ✅ Either for error handling
def parse(input: String): Either[String, Int] =
  input.toIntOption.toRight(s"Not a number: $input")

// ✅ Try for exceptions
import scala.util.{Try, Success, Failure}
val result = Try(riskyOperation()) match
  case Success(value) => value
  case Failure(ex)    => defaultValue
```

---

## संग्रह और कार्यात्मक
```scala
// ✅ Collection operations
val names = users
  .filter(_.active)
  .map(_.name)
  .sorted

val grouped = users.groupBy(_.role)
val total = users.map(_.salary).sum
val found = users.find(_.id == targetId)
val exists = users.exists(_.isAdmin)

// ✅ For-comprehension
val result = for
  user <- users if user.active
  order <- user.orders
  if order.total > 100
yield (user.name, order.total)

// ✅ Tail recursion
@annotation.tailrec
def factorial(n: Int, acc: BigInt = 1): BigInt =
  if n <= 1 then acc
  else factorial(n - 1, acc * n)
```

---

## अंतर्निहित एवं प्रदत्त (स्कैला 3)
```scala
// ✅ given/using (Scala 3)
given ExecutionContext = ExecutionContext.global

def process(using ec: ExecutionContext): Future[Result] = ...

// ✅ Extension methods (Scala 3)
extension (s: String)
  def isEmail: Boolean = s.contains("@")
  def wordCount: Int = s.split("\\s+").length

// ✅ Type classes with given
trait JsonEncoder[A]:
  def encode(a: A): String

given JsonEncoder[Int] with
  def encode(a: Int) = a.toString

given [A](using enc: JsonEncoder[A]): JsonEncoder[List[A]] with
  def encode(as: List[A]) = as.map(enc.encode).mkString("[", ",", "]")
```

---

## समवर्ती
```scala
// ✅ Cats Effect IO
import cats.effect.*

def fetchUser(id: Long): IO[User] =
  IO.blocking(database.find(id))
    .flatMap {
      case Some(user) => IO.pure(user)
      case None       => IO.raiseError(NotFound(id))
    }

// ✅ ZIO
import zio.*

def process: ZIO[Scope, AppError, Result] =
  for
    user <- UserService.find(id)
    orders <- OrderService.findByUser(user.id)
  yield Result(user, orders)
```

---

## सारांश
स्काला मुहावरे जोर देते हैं: अपरिवर्तनीयता (`val`), पैटर्न मिलान, सीलबंद प्रकार, सुरक्षा के लिए विकल्प/या तो, समझ के लिए, कार्यात्मक संग्रह, और प्रकार वर्ग (स्कैला 3 में दिए गए/उपयोग किए गए)। स्काला स्टाइल गाइड का पालन करें, फ़ॉर्मेटिंग के लिए स्कैलाफ़्मिट और लिंटिंग के लिए स्कैलाफ़िक्स का उपयोग करें। स्काला 3 के स्वच्छ वाक्यविन्यास, एनम्स, अपारदर्शी प्रकार और विस्तार विधियां भाषा की कार्यात्मक शक्ति को बरकरार रखते हुए इसे अधिक सुलभ बनाती हैं।