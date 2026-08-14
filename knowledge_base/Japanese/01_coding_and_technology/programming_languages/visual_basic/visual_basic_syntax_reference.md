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
# Visual Basic — 構文リファレンス
このドキュメントは、Visual Basic (VB.NET) の包括的で構造化された構文リファレンスを提供します。これは、網羅的な構文パターン、OOP 機能、LINQ、async/await、および .NET 統合イディオムに焦点を当て、メインの Visual Basic リファレンスを補完します。
---

## 演算子と式
|カテゴリー |オペレーター |説明 |例 |
|----------|----------|---------------|----------|
| **算術** | `+`|追加 | `a + b`|
| | `-`|減算 | `a - b`|
| | `*`|乗算 | `a * b`|
| | `/`|除算 (Double を返します) | `a / b`|
| | `\`|整数の除算 | `a \ b`|
| | `Mod`|弾性率 | `a Mod b`|
| | `^`|べき乗 | `a ^ b`|
| **比較** | `=`|等しい | `a = b`|
| | `<>`|等しくない | `a <> b`|
| | `<`| | より小さい `a < b`|
| | `>`| | より大きい `a > b`|
| | `<=`|以下 | `a <= b`|
| | `>=`|以上 | `a >= b`|
| **論理的** | `AndAlso`|短絡AND | `a AndAlso b`|
| | `OrElse`|短絡OR | `a OrElse b`|
| |  XQZマーカー30XQZ |論理否定 | `Not a`|
| | `And`|ビット単位の AND | `a And b`|
| | `Or`|ビットごとの OR | `a Or b`|
| | `Xor`|ビットごとの XOR | `a Xor b`|
| **文字列** | `&`|連結 | `"Hello" & " " & "World"`|
| |  XQZマーカー40XQZ |追加 | `s &= " more"`|
| **割り当て** | `=`|割り当て | `x = 42`|
| **ヌル** | `Is`|参照の等価性 | `obj Is Nothing`|
| | `IsNot`|参照不等式 | `obj IsNot Nothing`|
| **タイプ** | `TryCast`|安全なキャスト (何も返さない) | `TryCast(obj, String)`|
| |  XQZマーカー50XQZ |変換 | `CType(obj, Integer)`|
| | `DirectCast`|ダイレクト キャスト (失敗時にスロー) | `DirectCast(obj, String)`|
---

## 制御フロー
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

## データ型と変数
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

## クラスと OOP
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

## ジェネリックとコレクション
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

## LINQ (言語統合クエリ)
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

## 非同期/待機
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

## 例外処理
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

## イベントと参加者
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

＃＃ まとめ
Visual Basic の構文は簡潔で英語に似ており、最も読みやすいプログラミング言語の 1 つです。 VB.NET は、データ クエリのための LINQ、同時操作のための async/await、タイプ セーフティのためのジェネリックス、クラス、インターフェイス、継承を備えた包括的な OOP を含む .NET エコシステムへの完全なアクセスを提供します。この言語の大文字と小文字は区別されず、冗長なキーワード (End If、End Sub、End Class) により読みやすさが向上します。エンタープライズ Windows アプリケーション、オフィス オートメーション (VBA)、および .NET 内でのラピッド プロトタイピングにとって、VB.NET は依然として生産的で有能な言語です。