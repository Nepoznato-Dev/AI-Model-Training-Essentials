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

# স্কালা — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্ন
এই নথিটি সংশোধন সহ স্কালাতে সবচেয়ে সাধারণ ভুল, ফাঁদ এবং অ্যান্টি-প্যাটার্নগুলি ক্যাটালগ করে।
---

## 1.`val`এর পরিবর্তে`var`ব্যবহার করা
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

## 2. সিল করা প্রকারের জন্য প্যাটার্ন ম্যাচিং ব্যবহার করা হচ্ছে না
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

## 3. সংগ্রহ কর্মক্ষমতা
```scala
// ❌ WRONG — using List for random access
val list = List(1, 2, 3, 4, 5)
list(3)  // O(n) — traverses the list

// ✅ CORRECT — use Vector for indexed access
val vec = Vector(1, 2, 3, 4, 5)
vec(3)  // O(log32 n) — nearly constant
```

---

## 4. ভবিষ্যত কলব্যাক হেল
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

## 5. অন্তর্নিহিত রূপান্তর অপব্যবহার
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

## 6.`Option`সঠিকভাবে পরিচালনা করা হচ্ছে না
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

## 7. অ্যান্টি-প্যাটার্ন: স্কালায় শূন্য
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

## 8. জেনেরিক দিয়ে ইরেজার টাইপ করুন
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

## সারাংশ
স্কালার ক্ষমতা দায়িত্বের সাথে আসে:`var`এর চেয়ে`val`পছন্দ করুন, সিল করা প্রকারের জন্য প্যাটার্ন ম্যাচিং ব্যবহার করুন,`Option`সঠিকভাবে পরিচালনা করুন (কখনও`.get`কল করবেন না), নেস্টেড ফিউচারের পরিবর্তে বোঝার জন্য ব্যবহার করুন এবং শূন্য এড়িয়ে চলুন। স্কালা 3 এই প্যাটার্নগুলির অনেকগুলিকে এনাম, এক্সটেনশন পদ্ধতি এবং ইউনিয়নের প্রকারগুলি দিয়ে সরল করে। মূল নীতি: যদি কম্পাইলার এটি পরীক্ষা করতে পারে তবে কম্পাইলারকে এটি পরীক্ষা করতে দিন।