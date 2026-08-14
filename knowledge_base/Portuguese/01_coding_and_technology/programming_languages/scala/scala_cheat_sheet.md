---
# Metadata
title: "Scala — Cheat Sheet"
description: "Quick-reference cheat sheet for Scala syntax, collections, and functional patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [scala, functional, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Scala – Folha de dicas
## Básico
```scala
// Variables
val name = "Alice"       // immutable
var age = 30             // mutable
val pi: Double = 3.14159
val active: Boolean = true
lazy val computed = expensiveOp()  // evaluated on first use

// Types
val i: Int = 42
val l: Long = 100L
val d: Double = 3.14
val b: Boolean = true
val c: Char = 'A'
val s: String = "hello"
val u: Unit = ()         // void equivalent

// String interpolation
s"Hello, $name!"
s"Age: ${age + 1}"
f"Pi: $pi%.2f"
raw"No \n escaping"

// Multiline string
val text = """
  |Hello,
  |World!
  """.stripMargin
```

## Coleções
```scala
// List
val list = List(1, 2, 3)
list :+ 4                // append
0 +: list                // prepend
list.head                // 1
list.tail                // List(2, 3)
list.map(_ * 2)
list.filter(_ > 2)
list.reduce(_ + _)
list.foldLeft(0)(_ + _)
list.foreach(println)

// Vector (indexed, immutable)
val vec = Vector(1, 2, 3)

// Map
val map = Map("alice" -> 90, "bob" -> 85)
map("alice")             // 90
map.getOrElse("charlie", 0)
map + ("charlie" -> 78)
map.keys
map.values
map.map { case (k, v) => (k.toUpperCase, v * 2) }

// Set
val set = Set(1, 2, 3)
set + 4
set.contains(2)
set.union(Set(4, 5))

// Seq, Iterable
val seq: Seq[Int] = Seq(1, 2, 3)

// Mutable collections
import scala.collection.mutable
val buf = mutable.Buffer[Int]()
val mMap = mutable.Map[String, Int]()
```

## Fluxo de controle
```scala
if (condition) { ... }
else if (other) { ... }
else { ... }

// if is an expression
val result = if (condition) "yes" else "no"

// Pattern matching
val label = value match {
  case 0           => "zero"
  case n if n > 0  => "positive"
  case n if n < 0  => "negative"
  case _           => "unknown"
}

// Loops
for (item <- collection) { ... }
for (i <- 0 until 10) { ... }       // 0 to 9
for (i <- 0 to 10) { ... }          // 0 to 10
for (i <- 0 until 10 if i % 2 == 0) { ... }  // guard
for {
  x <- list1
  y <- list2
} yield (x, y)  // for-comprehension

// While
while (condition) { ... }
```

## Classes e Enums de Caso
```scala
// Case class
case class User(name: String, age: Int)
val user = User("Alice", 30)
val User(name, age) = user  // destructure
val copy = user.copy(age = 31)

// Enum (Scala 3)
enum Color:
  case Red, Green, Blue

enum Shape:
  case Circle(radius: Double)
  case Rectangle(width: Double, height: Double)

  def area: Double = this match
    case Circle(r) => Math.PI * r * r
    case Rectangle(w, h) => w * h

// Sealed trait (Scala 2)
sealed trait Animal
case class Dog(name: String) extends Animal
case class Cat(name: String) extends Animal

// Object (singleton)
object MathUtils:
  def factorial(n: Int): Int =
    if (n <= 1) 1 else n * factorial(n - 1)
```

## Funções e correspondência de padrões
```scala
// Function
def add(a: Int, b: Int): Int = a + b

// Default & named params
def greet(name: String, greeting: String = "Hello"): String =
  s"$greeting, $name!"
greet(name = "Alice", greeting = "Hi")

// Higher-order function
def applyTwice(f: Int => Int, x: Int): Int = f(f(x))

// Partial function
val isEven: PartialFunction[Int, String] = {
  case n if n % 2 == 0 => s"$n is even"
}

// Currying
def multiply(x: Int)(y: Int): Int = x * y
val double = multiply(2)_

// Underscore shorthand
List(1, 2, 3).map(_ * 2)
List(1, 2, 3).reduce(_ + _)

// Extension methods (Scala 3)
extension (s: String)
  def isEmail: Boolean = s.contains("@")
```

## Opção e qualquer uma
```scala
// Option
val opt: Option[Int] = Some(42)
opt.map(_ * 2)          // Some(84)
opt.getOrElse(0)        // 42
opt.filter(_ > 10)      // Some(42)
opt.flatMap(n => Some(n.toString))

// Either
val result: Either[String, Int] = Right(42)
result.map(_ * 2)       // Right(84)
result.getOrElse(0)
result match
  case Right(value) => println(s"OK: $value")
  case Left(error)  => println(s"Error: $error")

// For-comprehension
val combined = for
  a <- findUser(id)
  b <- findOrders(a)
yield (a, b)
```

## Características e classes de tipo
```scala
// Trait
trait Printable:
  def print: String

trait Show[A]:
  def show(a: A): String

// Given/Using (Scala 3)
given Show[Int] with
  def show(a: Int): String = a.toString

def display[A](a: A)(using s: Show[A]): String = s.show(a)

// Extension (Scala 3)
extension [A](list: List[A])
  def second: Option[A] = list.drop(1).headOption
```

## Tratamento de erros
```scala
// Try
import scala.util.{Try, Success, Failure}

val result = Try(riskyOperation())
result match
  case Success(value) => println(value)
  case Failure(ex)    => println(ex.getMessage)

result.getOrElse(default)
result.toOption

// Future (async)
import scala.concurrent.Future
import scala.concurrent.ExecutionContext.Implicits.global

val future = Future {
  expensiveOperation()
}
future.map(result => process(result))
future.onComplete {
  case Success(v) => println(v)
  case Failure(e) => println(e)
}
```
