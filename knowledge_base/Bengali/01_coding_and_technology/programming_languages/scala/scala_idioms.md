---
# Metadata
title: "Scala — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, functional Scala code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# স্ক্যালা — ইডিওম্যাটিক প্যাটার্নস এবং সেরা অনুশীলন
এই নির্দেশিকাটি পরিষ্কার, কার্যকরী স্কালা 3 কোড লেখার জন্য বাহাদুরিমূলক নিদর্শন এবং সর্বোত্তম অনুশীলনগুলি কভার করে।
---

## স্কেলা 3 সিনট্যাক্স
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

## প্যাটার্ন ম্যাচিং
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

## বিকল্প এবং হয়
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

## সংগ্রহ এবং কার্যকরী
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

## অন্তর্নিহিত এবং দেওয়া (স্ক্যালা 3)
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

## সামঞ্জস্য
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

## সারাংশ
স্কালা ইডিয়মগুলি জোর দেয়: অপরিবর্তনীয়তা ( `val`), প্যাটার্ন ম্যাচিং, সিল করা প্রকার, বিকল্প/হয় নিরাপত্তার জন্য, বোঝার জন্য, কার্যকরী সংগ্রহ এবং টাইপ ক্লাস (স্কলা 3-এ দেওয়া/ব্যবহার করা)। স্কালা স্টাইল নির্দেশিকা অনুসরণ করুন, বিন্যাসের জন্য scalafmt এবং linting এর জন্য scalafix ব্যবহার করুন। Scala 3 এর ক্লিনার সিনট্যাক্স, enums, অস্বচ্ছ প্রকার এবং এক্সটেনশন পদ্ধতি ভাষাটিকে এর কার্যকরী শক্তি ধরে রাখার সাথে সাথে আরও সহজলভ্য করে তোলে।