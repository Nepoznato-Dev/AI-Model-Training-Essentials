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

# Scala — 常见错误和反模式
本文档列出了 Scala 中最常见的错误、陷阱和反模式，并进行了更正。
---

## 1. 使用`var`代替 `val`
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

## 2. 不对密封类型使用模式匹配
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

## 3.集合性能
```scala
// ❌ WRONG — using List for random access
val list = List(1, 2, 3, 4, 5)
list(3)  // O(n) — traverses the list

// ✅ CORRECT — use Vector for indexed access
val vec = Vector(1, 2, 3, 4, 5)
vec(3)  // O(log32 n) — nearly constant
```

---

## 4. 未来回调地狱
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

## 5. 隐式转换滥用
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

## 6. 未正确处理 `Option`
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

## 7. 反模式：Scala 中的 Null
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

## 8. 使用泛型进行类型擦除
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

＃＃ 概括
Scala 的力量伴随着责任：更喜欢`val`而不是`var`，对密封类型使用模式匹配，正确处理`Option`（永远不要调用`.get`），使用 for 推导式而不是嵌套 Future，并避免 null。 Scala 3 通过枚举、扩展方法和联合类型简化了其中许多模式。关键原则：如果编译器能检查，就让编译器检查。