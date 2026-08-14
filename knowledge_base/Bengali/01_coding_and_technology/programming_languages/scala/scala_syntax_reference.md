<!--
---
# Metadata
title: "Scala — Syntax Reference"
description: "Detailed syntax reference for Scala covering pattern matching, traits, implicits, collections, type system, Akka, and functional programming patterns."
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [scala, syntax-reference, pattern-matching, traits, implicits, collections, functional, coding-and-technology]
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
# স্কেলা — সিনট্যাক্স রেফারেন্স
এই নথিটি স্কালার জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে (2.x পার্থক্যের উপর নোট সহ 3.x)। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, টাইপ সিস্টেম, কার্যকরী প্রোগ্রামিং কনস্ট্রাক্ট এবং স্কালা ইডিয়মগুলির উপর ফোকাস করে মূল স্কালা রেফারেন্সের পরিপূরক।
---

## অপারেটর এবং এক্সপ্রেশন
### মূল অপারেটর
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `+``-``*``/``%`| পাটিগণিত | `a + b`| |
| `**`| পাওয়ার (বিগডেসিমাল) | `BigDecimal(2) ** 10`| Int এর জন্য অন্তর্নির্মিত নয় |
| `==``!=` | সমতা | `a == b`|`.equals()`কল করে — নাল-সেফ |
| `eq``ne` | রেফারেন্স সমতা | `a eq b`| একই উদাহরণ |
| `<``>``<=``>=` | তুলনা | `a >= b`| প্রয়োজন`Ordered`|
| `&&``\|\|``!`| যৌক্তিক | `a && b`| শর্ট সার্কিট |
| `&``\|``^``~` | বিটওয়াইজ | `a & b`| |
| `<<``>>``>>>`| শিফট | `a << 2`| |
| `+:``:+``::``:::` | সংগ্রহ অপারেশন | `1 +: list`| ডান-সহযোগী যদি`:`| দিয়ে শেষ হয়
| `->`| Tuple সৃষ্টি | `"key" -> "value"`| `("key", "value")`|
| `=>`| ফাংশন/তীর | `x => x + 1`| ল্যাম্বডা বা টাইপ ম্যাপিং |
| `<-`| জেনারেটর | `x <- List(1,2,3)`| বোঝার জন্য |
### অপারেটরের নিয়ম
```scala
// Any method can be used as infix operator
val sum = 1.+(2)     // 3
val sum2 = 1 + 2     // same thing

// Right-associative: methods ending in : bind right-to-left
val list = 1 :: 2 :: 3 :: Nil       // List(1, 2, 3)
val list2 = 1 +: 2 +: 3 +: List()   // List(1, 2, 3)

// Custom infix operator
case class Vector2D(x: Double, y: Double) {
  def +(other: Vector2D) = Vector2D(x + other.x, y + other.y)
  def dot(other: Vector2D) = x * other.x + y * other.y
}
Vector2D(1, 2) + Vector2D(3, 4)  // Vector2D(4, 6)
```

---

## নিয়ন্ত্রণ প্রবাহ
### প্যাটার্ন ম্যাচিং
```scala
// Basic match
val description = value match {
  case 0          => "zero"
  case n if n > 0 => "positive"
  case n if n < 0 => "negative"
}

// Type matching with extraction
def process(obj: Any): String = obj match {
  case s: String          => s"String: ${s.length} chars"
  case i: Int if i > 0    => s"Positive int: $i"
  case List(0, _*)        => "List starting with 0"
  case h :: t             => s"Head: $h, Tail: ${t.take(3)}"
  case (a, b)             => s"Tuple: ($a, $b)"
  case null               => "null"
  case _                  => "unknown"
}

// Case class decomposition
sealed trait Shape
case class Circle(radius: Double) extends Shape
case class Rect(width: Double, height: Double) extends Shape

def area(s: Shape): Double = s match {
  case Circle(r)      => math.Pi * r * r
  case Rect(w, h)     => w * h
}

// Pattern guards
def classify(n: Int): String = n match {
  case x if x < 0    => "negative"
  case 0              => "zero"
  case x if x <= 10   => "small"
  case x if x <= 100  => "medium"
  case _              => "large"
}

// Scala 3: match as expression
val label = value match
  case 0 => "zero"
  case _ => "non-zero"

// Scala 3: inline match (exhaustiveness checking at compile time)
inline def show(s: Shape): String = inline s match
  case Circle(r)  => s"Circle($r)"
  case Rect(w, h) => s"Rect($w, $h)"
```

### বোঝার জন্য
```scala
// For-comprehension — desugars to map/flatMap/withFilter
val result = for {
  user  <- users
  order <- user.orders
  if order.total > 100
} yield (user.name, order.total)

// Equivalent to:
users.flatMap(u => u.orders.withFilter(_.total > 100).map(o => (u.name, o.total)))

// Side-effecting for
for {
  i <- 1 to 10
  if i % 2 == 0
} println(i)

// Nested generators
val pairs = for {
  x <- 1 to 3
  y <- 1 to 3
  if x != y
} yield (x, y)
// Vector((1,2), (1,3), (2,1), (2,3), (3,1), (3,2))
```

---

## ফাংশন এবং ক্লোজার
```scala
// Method definition
def add(x: Int, y: Int): Int = x + y

// Multiple parameter lists (currying)
def multiply(x: Int)(y: Int): Int = x * y
val double = multiply(2)_
double(5)  // 10

// Function values
val addFn: (Int, Int) => Int = _ + _
val addFn2: (Int, Int) => Int = (a, b) => a + b

// Higher-order functions
def applyTwice(f: Int => Int, x: Int): Int = f(f(x))
applyTwice(_ * 2, 3)  // 12

// Partial application
def greet(greeting: String, name: String): String = s"$greeting, $name!"
val hello = greet("Hello", _: String)
hello("Alice")  // "Hello, Alice!"

// By-name parameters (lazy evaluation)
def log(block: => Unit): Unit = {
  println("Before")
  block        // evaluated here
  println("After")
}

// By-name: enables control structures
def whileTrue(condition: => Boolean)(body: => Unit): Unit =
  if (condition) { body; whileTrue(condition)(body) }

// Implicit parameters (Scala 2) / given/using (Scala 3)
// Scala 2:
def sort[T](list: List[T])(implicit ord: Ordering[T]): List[T] = list.sorted
// Scala 3:
def sort3[T](list: List[T])(using ord: Ordering[T]): List[T] = list.sorted

// Extension methods (Scala 3)
extension (s: String)
  def isPalindrome: Boolean = s == s.reverse
  def shout: String = s.toUpperCase + "!"

"racecar".isPalindrome  // true
"hello".shout            // "HELLO!"
```

---

## ক্লাস এবং বৈশিষ্ট্য
```scala
// Case class — immutable data carrier
case class User(name: String, email: String, age: Int = 0) {
  def isAdult: Boolean = age >= 18
}
val alice = User("Alice", "alice@example.com")
val older = alice.copy(age = 31)

// Sealed trait hierarchy
sealed trait Result[+T]
case class Success[T](value: T) extends Result[T]
case class Failure(error: String) extends Result[Nothing]

// Trait with abstract and concrete members
trait Repository[T] {
  def find(id: Long): Option[T]
  def findAll: List[T]
  def save(entity: T): Unit
  
  // Concrete method with default implementation
  def count: Int = findAll.size
}

// Trait composition
trait Loggable {
  def log(msg: String): Unit = println(s"[LOG] $msg")
}

trait Serializable {
  def toJson: String
}

class UserService extends Repository[User] with Loggable with Serializable {
  def find(id: Long): Option[User] = ???
  def findAll: List[User] = ???
  def save(entity: User): Unit = ???
  def toJson: String = ???
}

// Abstract class with constructor parameters
abstract class BaseController(config: AppConfig) {
  protected def logger = LoggerFactory.getLogger(getClass)
  def handle(request: Request): Response
}

// Object — singleton
object AppConfig {
  val dbUrl = "jdbc:postgresql://localhost/mydb"
  val poolSize = 10
}

// Enum (Scala 3)
enum Color:
  case Red, Green, Blue
  case Custom(r: Int, g: Int, b: Int)

enum Planet(val mass: Double, val radius: Double):
  case Earth extends Planet(5.97e24, 6.371e6)
  case Mars  extends Planet(6.42e23, 3.390e6)
  def surfaceGravity: Double = 6.674e-11 * mass / (radius * radius)
```

---

## সংগ্রহ
```scala
// List — immutable linked list
val list = List(1, 2, 3, 4, 5)
list.map(_ * 2)           // List(2, 4, 6, 8, 10)
list.filter(_ > 3)        // List(4, 5)
list.foldLeft(0)(_ + _)   // 15
list.head                  // 1
list.tail                  // List(2, 3, 4, 5)

// Vector — indexed, immutable, fast random access
val vec = Vector(1, 2, 3)
vec(0)                     // 1
vec.updated(1, 99)         // Vector(1, 99, 3)

// Map
val map = Map("a" -> 1, "b" -> 2)
map("a")                   // 1
map.getOrElse("z", 0)      // 0
map.view.mapValues(_ * 10).toMap  // Map("a" -> 10, "b" -> 20)

// Set
val set = Set(1, 2, 3, 2, 1)  // Set(1, 2, 3)
set + 4                        // Set(1, 2, 3, 4)
set - 1                        // Set(2, 3)
set.intersect(Set(2, 3, 4))    // Set(2, 3)

// Option
val opt: Option[Int] = Some(42)
opt.map(_ * 2)            // Some(84)
opt.filter(_ > 50)         // None
opt.getOrElse(0)           // 42
opt.flatMap(x => Some(x.toString))  // Some("42")

// Either
val result: Either[String, Int] = Right(42)
result.map(_ * 2)           // Right(84)
result.left.map(_.toUpperCase)  // Right(42)

// GroupBy, partition, span
val grouped = List(1, 2, 3, 4, 5, 6).groupBy(_ % 2)
// Map(false -> List(2, 4, 6), true -> List(1, 3, 5))

val (evens, odds) = List(1, 2, 3, 4, 5).partition(_ % 2 == 0)

// LazyList (infinite sequences)
lazy val naturals: LazyList[Int] = 1 #:: naturals.map(_ + 1)
naturals.take(5).toList  // List(1, 2, 3, 4, 5)
```

---

## টাইপ সিস্টেম
```scala
// Generic class
class Stack[T] {
  private var items: List[T] = Nil
  def push(item: T): Unit = items = item :: items
  def pop(): T = { val h = items.head; items = items.tail; h }
  def peek: T = items.head
}

// Type bounds
def max[T <: Comparable[T]](a: T, b: T): T = if (a.compareTo(b) >= 0) a else b

// Covariance (+T) — Producer[Dog] <: Producer[Animal]
trait Producer[+T] { def produce: T }

// Contravariance (-T) — Consumer[Animal] <: Consumer[Dog]
trait Consumer[-T] { def consume(item: T): Unit }

// Invariance — no subtyping relationship
trait Mutable[T] { var value: T }

// Existential types / wildcards
def printAll(items: List[_]): Unit = items.foreach(println)

// Type aliases
type UserID = Long
type Callback = String => Unit

// Opaque types (Scala 3) — zero-cost abstraction
opaque type Meter = Double
object Meter:
  def apply(value: Double): Meter = value
  extension (m: Meter)
    def value: Double = m
    def +(other: Meter): Meter = m + other

// Given instances (Scala 3) / implicits (Scala 2)
given Ordering[User] = Ordering.by(_.name)

// Context bounds
def largest[T: Ordering](items: List[T]): T = items.max
```

---

## ত্রুটি হ্যান্ডলিং
```scala
// Try — computation that may fail
import scala.util.{Try, Success, Failure}

val result = Try("42".toInt)
result match {
  case Success(value) => println(s"Got: $value")
  case Failure(ex)    => println(s"Error: ${ex.getMessage}")
}

// Chaining Try
val computed = for {
  a <- Try("10".toInt)
  b <- Try("20".toInt)
} yield a + b

// Option — value may be absent
def findUser(id: Long): Option[User] = ...

// Chaining Options
val email = for {
  user <- findUser(id)
  addr <- user.email
} yield addr

// Either — value or error (for error reporting)
def parseAge(input: String): Either[String, Int] =
  Try(input.toInt) match {
    case Success(n) if n >= 0 => Right(n)
    case Success(n)           => Left(s"Negative age: $n")
    case Failure(_)           => Left(s"Not a number: $input")
  }

// Throwing exceptions (last resort)
def legacyMethod(): String = throw new UnsupportedOperationException("TODO")

// NonFatal matching
import scala.util.control.NonFatal
try { riskyOp() } catch { case NonFatal(e) => log.error("Failed", e) }
```

---

## সারাংশ
স্কালার সিনট্যাক্স একটি শক্তিশালী টাইপ সিস্টেমের অধীনে অবজেক্ট-ওরিয়েন্টেড এবং কার্যকরী প্রোগ্রামিংকে একীভূত করে। প্যাটার্ন ম্যাচিং, অনুধাবনের জন্য, এবং কেস ক্লাসগুলি অভিব্যক্তিপূর্ণ ডেটা মডেলিং প্রদান করে। বৈশিষ্ট্য একক-উত্তরাধিকার সীমাবদ্ধতা ছাড়াই নমনীয় রচনা সক্ষম করে। টাইপ সিস্টেম — জেনেরিক, ভ্যারিয়েন্স, টাইপ বাউন্ড এবং অস্বচ্ছ প্রকারের সাথে — শূন্য-খরচ বিমূর্ততা সক্ষম করার সময় কম্পাইলের সময় ত্রুটিগুলি ধরে। স্কালা 3 এনাম, এক্সটেনশন পদ্ধতি, প্রদত্ত/ব্যবহার এবং অস্বচ্ছ প্রকারের সাহায্যে ভাষাটিকে সরল করে, ভাষাটিকে তার সম্পূর্ণ শক্তি বজায় রেখে আরও সহজলভ্য করে তোলে।