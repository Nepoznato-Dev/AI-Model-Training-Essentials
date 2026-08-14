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

# स्काला - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ सुधार के साथ स्काला में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है।
---

## 1.`val`के स्थान पर`var`का उपयोग करना
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

## 2. सीलबंद प्रकारों के लिए पैटर्न मिलान का उपयोग नहीं करना
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

## 3. संग्रह प्रदर्शन
```scala
// ❌ WRONG — using List for random access
val list = List(1, 2, 3, 4, 5)
list(3)  // O(n) — traverses the list

// ✅ CORRECT — use Vector for indexed access
val vec = Vector(1, 2, 3, 4, 5)
vec(3)  // O(log32 n) — nearly constant
```

---

## 4. भविष्य का कॉलबैक नरक
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

## 5. अन्तर्निहित धर्मान्तरण का दुरुपयोग
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

## 6.`Option`को ठीक से न संभालना
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

## 7. एंटी-पैटर्न: स्काला में शून्य
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

## 8. जेनेरिक के साथ इरेज़र टाइप करें
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

## सारांश
स्काला की शक्ति जिम्मेदारी के साथ आती है:`var`के बजाय`val`को प्राथमिकता दें, सीलबंद प्रकारों के लिए पैटर्न मिलान का उपयोग करें,`Option`को ठीक से संभालें (कभी भी`.get`को कॉल न करें), नेस्टेड फ्यूचर्स के बजाय फॉर-कॉम्प्रिहेंशन का उपयोग करें, और शून्य से बचें। स्काला 3 इनमें से कई पैटर्न को एनम, एक्सटेंशन विधियों और यूनियन प्रकारों के साथ सरल बनाता है। मुख्य सिद्धांत: यदि कंपाइलर इसकी जांच कर सकता है, तो कंपाइलर को इसकी जांच करने दें।