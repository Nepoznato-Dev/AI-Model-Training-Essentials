---
# Metadata
title: "Scala — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Scala with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [scala, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Scala - Makosa ya Kawaida & Miundo ya Kupambana
Hati hii inaorodhesha makosa ya kawaida, mitego, na mifumo ya kuzuia katika Scala na masahihisho.
---

## 1. Kutumia`var`Badala ya `val`
```scala
// ❌ WRONG — mutable by default
var name = "Alice"
var count = 0

// ✅ CORRECT — immutable by default
val name = "Alice"
val count = 0
// Only use var when mutation is truly necessary
```

---

## 2. Kutotumia Ulinganishaji wa Miundo kwa Aina Zilizofungwa
```scala
// ❌ WRONG — if/else chain
def describe(shape: Shape): String = {
  if (shape.isInstanceOf[Circle]) s"Circle(${shape.asInstanceOf[Circle].r})"
  else if (shape.isInstanceOf[Rectangle]) "Rectangle"
  else "Unknown"
}

// ✅ CORRECT — pattern matching
sealed trait Shape
case class Circle(r: Double) extends Shape
case class Rectangle(w: Double, h: Double) extends Shape

def describe(shape: Shape): String = shape match {
  case Circle(r) => s"Circle($r)"
  case Rectangle(w, h) => s"Rectangle($w, $h)"
}
```

---

## 3. Utendaji wa Makusanyo
```scala
// ❌ WRONG — using List for random access
val list = List(1, 2, 3, 4, 5)
list(3)  // O(n) — traverses the list

// ✅ CORRECT — use Vector for indexed access
val vec = Vector(1, 2, 3, 4, 5)
vec(3)  // O(log32 n) — nearly constant
```

---

## 4. Future Callback Hell
```scala
// ❌ WRONG — nested Future callbacks
getUser(id).map { user =>
  getPosts(user).map { posts =>
    getComments(posts.head).map { comments =>
      println(comments)
    }
  }
}

// ✅ CORRECT — for-comprehension
val result = for {
  user <- getUser(id)
  posts <- getPosts(user)
  comments <- getComments(posts.head)
} yield comments
```

---

## 5. Matumizi Mabaya ya Uongofu
```scala
// ❌ WRONG — too many implicit conversions
implicit def stringToInt(s: String): Int = s.toInt
implicit def intToString(i: Int): String = i.toString
// Confusing and error-prone

// ✅ CORRECT — use extension methods (Scala 3) or explicit conversion
extension (s: String)
  def toIntSafe: Option[Int] = scala.util.Try(s.toInt).toOption
```

---

## 6. Kutoshughulikia`Option`Vizuri
```scala
// ❌ WRONG — calling .get without checking
val user: Option[User] = findUser(id)
println(user.get.name)  // NoSuchElementException if None!

// ✅ CORRECT — pattern match or map
user match {
  case Some(u) => println(u.name)
  case None => println("Not found")
}

// ✅ CORRECT — use getOrElse, map, flatMap
val name = user.map(_.name).getOrElse("Unknown")
```

---

## 7. Anti-Pattern: Null in Scala
```scala
// ❌ WRONG — using null
def findUser(id: Int): User = {
  if (id > 0) getUser(id)
  else null
}

// ✅ CORRECT — use Option
def findUser(id: Int): Option[User] = {
  if (id > 0) Some(getUser(id))
  else None
}
```

---

## 8. Andika Futa kwa kutumia Jenerali
```scala
// ❌ WRONG — pattern matching on generic type
def process(list: List[Any]): String = list match {
  case _: List[String] => "strings"  // always matches!
  case _: List[Int] => "ints"        // never reached
}

// ✅ CORRECT — use TypeTag or ClassTag
import scala.reflect.ClassTag
def process[T: ClassTag](list: List[T]): String = {
  val tag = implicitly[ClassTag[T]]
  tag.toString match {
    case "java.lang.String" => "strings"
    case "int" => "ints"
    case _ => "unknown"
  }
}
```

---

## Muhtasari
Nguvu ya Scala inakuja na jukumu: pendelea`val`kuliko`var`, tumia ulinganishaji wa muundo kwa aina zilizofungwa, shughulikia`Option`ipasavyo (usipige simu kamwe`.get`), tumia ufahamu badala ya Futures zilizowekwa na epuka kubatilisha. Scala 3 hurahisisha mifumo mingi hii kwa kutumia enum, mbinu za upanuzi, na aina za muungano. Kanuni kuu: ikiwa mkusanyaji anaweza kuiangalia, wacha mkusanyaji aangalie.