<!--
---
# Metadata
title: "Visual Basic — Syntax Reference"
description: "Detailed syntax reference for Visual Basic (VB.NET) covering operators, control flow, classes, LINQ, async/await, event handling, generics, and .NET integration patterns."
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
tags: [visual-basic, vbnet, syntax-reference, oop, linq, async, dotnet, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# ভিজ্যুয়াল বেসিক — সিনট্যাক্স রেফারেন্স
এই নথিটি ভিজ্যুয়াল বেসিক (VB.NET) এর জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, OOP বৈশিষ্ট্য, LINQ, async/await, এবং .NET ইন্টিগ্রেশন ইডিয়মগুলিতে ফোকাস করে মূল ভিজ্যুয়াল বেসিক রেফারেন্সের পরিপূরক।
---

## অপারেটর এবং এক্সপ্রেশন
| বিভাগ | অপারেটর | বর্ণনা | উদাহরণ |
|----------|----------|---------------|---------|
| **পাটিগণিত** | `+`| সংযোজন | `a + b`|
| | `-`| বিয়োগ | `a - b`|
| | `*`| গুণ | `a * b`|
| | `/`| বিভাগ (ডবল ফেরত) | `a / b`|
| | `\`| পূর্ণসংখ্যা বিভাজন | `a \ b`|
| | `Mod`| মডুলাস | `a Mod b`|
| | `^`| ব্যাখ্যা | `a ^ b`|
| **তুলনা** | `=`| সমান | `a = b`|
| | `<>`| সমান নয় | `a <> b`|
| | `<`| কম | `a < b`|
| | `>`| এর চেয়ে বড় | `a > b`|
| | `<=`| কম বা সমান | `a <= b`|
| | `>=`| বৃহত্তর বা সমান | `a >= b`|
| **যৌক্তিক** | `AndAlso`| শর্ট সার্কিট এবং | `a AndAlso b`|
| | `OrElse`| শর্ট সার্কিট বা | `a OrElse b`|
| | `Not`| যৌক্তিক নয় | `Not a`|
| | `And`| বিটওয়াইজ এবং | `a And b`|
| | `Or`| বিটওয়াইজ বা | `a Or b`|
| | `Xor`| বিটওয়াইজ XOR | `a Xor b`|
| **স্ট্রিং** | `&`| সংযুক্তি | `"Hello" & " " & "World"`|
| | `+=`| যুক্ত করুন | `s &= " more"`|
| **অ্যাসাইনমেন্ট** | `=`| বরাদ্দ | `x = 42`|
| **শূন্য** | `Is`| রেফারেন্স সমতা | `obj Is Nothing`|
| | `IsNot`| রেফারেন্স অসমতা | `obj IsNot Nothing`|
| **টাইপ** | `TryCast`| নিরাপদ কাস্ট (কিছুই ফেরত দেয় না) | `TryCast(obj, String)`|
| | `CType`| রূপান্তর | `CType(obj, Integer)`|
| | `DirectCast`| সরাসরি কাস্ট (ব্যর্থতার উপর নিক্ষেপ) | `DirectCast(obj, String)`|
---

## নিয়ন্ত্রণ প্রবাহ
```vb
' If-Then-Else
If x > 0 Then
    Console.WriteLine("Positive")
ElseIf x = 0 Then
    Console.WriteLine("Zero")
Else
    Console.WriteLine("Negative")
End If

' Single-line If
If x > 0 Then Console.WriteLine("Positive")

' Select Case (switch)
Select Case grade
    Case "A"
        Console.WriteLine("Excellent")
    Case "B", "C"
        Console.WriteLine("Good")
    Case "D"
        Console.WriteLine("Pass")
    Case "F"
        Console.WriteLine("Fail")
    Case Else
        Console.WriteLine("Invalid")
End Select

' For loop
For i As Integer = 1 To 10
    Console.WriteLine(i)
Next

For i As Integer = 10 To 1 Step -1
    Console.WriteLine(i)
Next

' For Each loop
For Each item In collection
    Console.WriteLine(item)
Next

' While loop
While x > 0
    Console.WriteLine(x)
    x -= 1
End While

' Do-While loop
Do While x > 0
    Console.WriteLine(x)
    x -= 1
Loop

' Do-Until loop
Do Until x = 0
    Console.WriteLine(x)
    x -= 1
Loop

' Inline If (ternary)
Dim result = If(x > 0, "Positive", "Non-positive")

' Null-coalescing
Dim name = If(userName, "Default")
```

---

## ডেটা টাইপ এবং ভেরিয়েবল
```vb
' Value types
Dim b As Boolean = True
Dim i As Integer = 42
Dim l As Long = 1000000000L
Dim s As Short = 32000
Dim byt As Byte = 255
Dim d As Double = 3.14159
Dim dec As Decimal = 99.99D
Dim c As Char = "A"c
Dim dt As Date = #8/9/2026#

' Reference types
Dim str As String = "Hello"
Dim obj As Object = 42

' Nullable types
Dim nullableInt As Integer? = Nothing
Dim nullableDate As Date? = #1/1/2026#

' Type inference (Option Infer On)
Dim x = 42              ' Integer
Dim name = "Alice"       ' String
Dim items = New List(Of String)()

' Constants
Const PI As Double = 3.14159265
Const MAX_SIZE As Integer = 100

' Arrays
Dim numbers() As Integer = {1, 2, 3, 4, 5}
Dim matrix(,) As Integer = {{1, 2}, {3, 4}}
Dim empty As String() = New String(9) {}  ' 10 elements

' Tuples
Dim point = (1, "hello")
Dim (x, y) = point
Dim named As (Name As String, Age As Integer) = ("Alice", 30)

' Enumerations
Enum Season
    Spring = 1
    Summer = 2
    Autumn = 3
    Winter = 4
End Enum

Dim current As Season = Season.Summer
```

---

## ক্লাস এবং ওওপি
```vb
' Base class
Public Class Animal
    ' Properties
    Public Property Name As String
    Public ReadOnly Property Species As String
    
    ' Fields
    Private _age As Integer
    Protected _isAlive As Boolean = True
    
    ' Constructor
    Public Sub New(name As String, species As String)
        Me.Name = name
        _Species = species
        _age = 0
    End Sub
    
    ' Methods
    Public Overridable Function Speak() As String
        Return $"{Name} makes a sound"
    End Function
    
    ' Property with custom logic
    Public Property Age As Integer
        Get
            Return _age
        End Get
        Set(value As Integer)
            If value >= 0 Then
                _age = value
            Else
                Throw New ArgumentException("Age cannot be negative")
            End If
        End Set
    End Property
End Class

' Inheritance
Public Class Dog
    Inherits Animal
    
    Public Sub New(name As String)
        MyBase.New(name, "Canine")
    End Sub
    
    Public Overrides Function Speak() As String
        Return $"{Name} says woof"
    End Function
End Class

' Abstract class
Public MustInherit Class Shape
    Public MustOverride Function Area() As Double
    Public Overridable Sub Describe()
        Console.WriteLine($"I am a {GetType().Name}")
    End Sub
End Class

' Interface
Public Interface ISerializable
    Function Serialize() As String
    Sub Deserialize(data As String)
End Interface

' Implementing interface
Public Class Document
    Implements ISerializable
    
    Public Function Serialize() As String Implements ISerializable.Serialize
        Return $"Document data"
    End Function
    
    Public Sub Deserialize(data As String) Implements ISerializable.Deserialize
        ' Parse data
    End Sub
End Class
```

---

## জেনেরিক এবং সংগ্রহ
```vb
' Generic class
Public Class Repository(Of T As {Class, New})
    Private _items As New List(Of T)()
    
    Public Sub Add(item As T)
        _items.Add(item)
    End Sub
    
    Public Function Find(predicate As Func(Of T, Boolean)) As T
        Return _items.Find(predicate)
    End Function
    
    Public ReadOnly Property Count As Integer
        Get
            Return _items.Count
        End Get
    End Property
End Class

' Generic method
Public Class Utilities
    Public Shared Function Max(Of T As IComparable(Of T))(a As T, b As T) As T
        If a.CompareTo(b) >= 0 Then Return a
        Return b
    End Function
    
    Public Shared Sub Swap(Of T)(ByRef a As T, ByRef b As T)
        Dim temp = a
        a = b
        b = temp
    End Sub
End Class

' Collection types
Dim list As New List(Of String) From {"a", "b", "c"}
Dim dict As New Dictionary(Of String, Integer) From {
    {"Alice", 95}, {"Bob", 87}, {"Charlie", 92}
}
Dim hashSet As New HashSet(Of Integer) From {1, 2, 3, 4, 5}
Dim queue As New Queue(Of String)()
Dim stack As New Stack(Of Integer)()
```

---

## LINQ (ভাষা সমন্বিত প্রশ্ন)
```vb
' Query syntax (SQL-like)
Dim scores = {85, 92, 78, 95, 88, 72, 91}

Dim highScores = From s In scores
                 Where s > 80
                 Order By s Descending
                 Select s

' Method syntax (lambda)
Dim topScores = scores _
    .Where(Function(s) s > 80) _
    .OrderByDescending(Function(s) s) _
    .Take(3)

' Group by
Dim employees = GetEmployees()
Dim byDept = From emp In employees
             Group By emp.Department Into DeptGroup = Group
             Select Department,
                    Count = DeptGroup.Count(),
                    AvgSalary = DeptGroup.Average(Function(e) e.Salary)

' Aggregation
Dim total = numbers.Sum()
Dim avg = numbers.Average()
Dim max = numbers.Max()
Dim min = numbers.Min()
Dim count = numbers.Count()

' Join
Dim result = From emp In employees
             Join dept In departments
             On emp.DepartmentId Equals dept.Id
             Select emp.Name, dept.Name

' Any / All / Contains
Dim hasNegatives = numbers.Any(Function(n) n < 0)
Dim allPositive = numbers.All(Function(n) n > 0)
```

---

## অ্যাসিঙ্ক/অপেক্ষা করুন
```vb
' Async function
Public Async Function FetchDataAsync(url As String) As Task(Of String)
    Using client As New HttpClient()
        Dim response = Await client.GetStringAsync(url)
        Return response
    End Using
End Function

' Async with error handling
Public Async Function GetUserAsync(id As String) As Task(Of User)
    Try
        Dim response = Await _client.GetAsync($"api/users/{id}")
        response.EnsureSuccessStatusCode()
        Dim json = Await response.Content.ReadAsStringAsync()
        Return JsonSerializer.Deserialize(Of User)(json)
    Catch ex As HttpRequestException
        _logger.LogError(ex, "HTTP error fetching user {Id}", id)
        Return Nothing
    End Try
End Function

' Parallel async operations
Public Async Function FetchAllAsync(urls As IEnumerable(Of String)) As Task(Of String())
    Dim tasks = urls.Select(Function(url) FetchDataAsync(url))
    Return Await Task.WhenAll(tasks)
End Function

' Async with cancellation
Public Async Function DownloadAsync(url As String, ct As CancellationToken) As Task(Of Byte())
    Using client As New HttpClient()
        Return Await client.GetByteArrayAsync(url, ct)
    End Using
End Function
```

---

## ব্যতিক্রম হ্যান্ডলিং
```vb
' Try-Catch-Finally
Try
    Dim result = Divide(a, b)
    Console.WriteLine($"Result: {result}")
Catch ex As DivideByZeroException
    Console.WriteLine($"Cannot divide by zero: {ex.Message}")
Catch ex As OverflowException
    Console.WriteLine($"Number too large: {ex.Message}")
Catch ex As Exception
    Console.WriteLine($"Unexpected error: {ex.Message}")
Finally
    Console.WriteLine("Cleanup complete")
End Try

' Throw
If value < 0 Then
    Throw New ArgumentOutOfRangeException(NameOf(value), "Must be non-negative")
End If

' Using statement (auto-dispose)
Using reader As New StreamReader("file.txt")
    Dim content = reader.ReadToEnd()
End Using
' reader is automatically disposed here

' Throw expression (VB 15+)
Dim value = If(x > 0, x, Throw New ArgumentException("Must be positive"))
```

---

## ইভেন্ট এবং প্রতিনিধি
```vb
' Define event
Public Class OrderService
    Public Event OrderPlaced As EventHandler(Of OrderEventArgs)
    Public Event OrderCancelled As EventHandler(Of OrderEventArgs)
    
    Public Sub PlaceOrder(order As Order)
        ' Process order...
        RaiseEvent OrderPlaced(Me, New OrderEventArgs(order))
    End Sub
End Class

' Subscribe with AddHandler
AddHandler service.OrderPlaced, Sub(sender, e)
    Console.WriteLine($"Order {e.Order.Id} placed")
End Sub

' Subscribe with Handles keyword
Private Sub OnOrderPlaced(sender As Object, e As OrderEventArgs) _
    Handles service.OrderPlaced
    Console.WriteLine($"Order received: {e.Order.Id}")
End Sub

' Custom delegate
Public Delegate Function Calculator(a As Integer, b As Integer) As Integer

Dim add As Calculator = Function(a, b) a + b
Dim result = add(3, 5)  ' 8

' Action and Func
Dim greet As Action(Of String) = Sub(name) Console.WriteLine($"Hello, {name}")
Dim square As Func(Of Integer, Integer) = Function(x) x * x
```

---

## সারাংশ
ভিজ্যুয়াল বেসিকের সিনট্যাক্স পরিষ্কার এবং ইংরেজির মতো, এটিকে সবচেয়ে পঠনযোগ্য প্রোগ্রামিং ভাষাগুলির মধ্যে একটি করে তুলেছে। VB.NET .NET ইকোসিস্টেমে সম্পূর্ণ অ্যাক্সেস প্রদান করে যার মধ্যে রয়েছে ডাটা কোয়েরির জন্য LINQ, সমসাময়িক ক্রিয়াকলাপের জন্য async/অপেক্ষা, টাইপ নিরাপত্তার জন্য জেনেরিক, এবং ক্লাস, ইন্টারফেস এবং উত্তরাধিকার সহ ব্যাপক OOP। ভাষার কেস-সংবেদনশীলতা এবং ভারবোস কীওয়ার্ড (এন্ড ইফ, এন্ড সাব, এন্ড ক্লাস) পঠনযোগ্যতা বাড়ায়। এন্টারপ্রাইজ উইন্ডোজ অ্যাপ্লিকেশনের জন্য, অফিস অটোমেশন (VBA), এবং .NET-এর মধ্যে দ্রুত প্রোটোটাইপিং, VB.NET একটি উত্পাদনশীল এবং সক্ষম ভাষা হিসাবে রয়ে গেছে।