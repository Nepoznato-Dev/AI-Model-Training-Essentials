---
# Metadata
title: "Visual Basic — Syntax Reference"
description: "Detailed syntax reference for Visual Basic (VB.NET) covering operators, control flow, classes, LINQ, async/await, event handling, generics, and .NET integration patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "AI Model Training Team"
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

# Visual Basic — Informacje o składni
Ten dokument zawiera kompleksowe, uporządkowane informacje o składni języka Visual Basic (VB.NET). Uzupełnia główne odniesienia do języka Visual Basic, koncentrując się na wyczerpujących wzorcach składni, funkcjach OOP, LINQ, async/await i idiomach integracji .NET.
---

## Operatory i wyrażenia
| Kategoria | Operator | Opis | Przykład |
|---------|----------|------------|-------------|
| **Arytmetyka** | `+`| Dodatek | `a + b`|
| | `-`| Odejmowanie | `a - b`|
| | `*`| Mnożenie | `a * b`|
| | `/`| Dzielenie (zwraca Double) | `a / b`|
| | `\`| Dzielenie całkowite | `a \ b`|
| | `Mod`| Moduł | `a Mod b`|
| | `^`| Potęgowanie | `a ^ b`|
| **Porównanie** | `=`| Równe | `a = b`|
| | `<>`| Nie równe | `a <> b`|
| | `<`| Mniej niż | `a < b`|
| | `>`| Większe niż | `a > b`|
| | `<=`| Mniej lub równo | `a <= b`|
| | `>=`| Większy lub równy | `a >= b`|
| **Logiczne** | `AndAlso`| Zwarcie ORAZ | `a AndAlso b`|
| | `OrElse`| Zwarcie LUB | `a OrElse b`|
| | `Not`| Logiczne NIE | `Not a`|
| | `And`| Bitowe ORAZ | `a And b`|
| | `Or`| Bitowe LUB | `a Or b`|
| | `Xor`| Bitowy XOR | `a Xor b`|
| **Ciąg** | `&`| Konkatenacja | `"Hello" & " " & "World"`|
| | `+=`| Dołącz | `s &= " more"`|
| **Zadanie** | `=`| Przypisz | `x = 42`|
| **Nuta** | `Is`| Równość odniesienia | `obj Is Nothing`|
| | `IsNot`| Nierówność odniesienia | `obj IsNot Nothing`|
| **Wpisz** | `TryCast`| Bezpieczne rzutowanie (nie zwraca nic) | `TryCast(obj, String)`|
| | `CType`| Konwertuj | `CType(obj, Integer)`|
| | `DirectCast`| Rzucanie bezpośrednie (rzuca w przypadku niepowodzenia) | `DirectCast(obj, String)`|
---

## Kontroluj przepływ
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

## Typy danych i zmienne
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

## Zajęcia i OOP
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

## Ogólne i kolekcje
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

## LINQ (zapytanie zintegrowane z językiem)
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

## Asynchronizacja/Oczekiwanie
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

## Obsługa wyjątków
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

## Wydarzenia i delegaci
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

## Streszczenie
Składnia Visual Basic jest czysta i przypomina angielską, co czyni go jednym z najbardziej czytelnych języków programowania. VB.NET zapewnia pełny dostęp do ekosystemu .NET, w tym LINQ do wykonywania zapytań o dane, async/await dla współbieżnych operacji, generyczne zabezpieczenia typów i kompleksowe OOP z klasami, interfejsami i dziedziczeniem. Zastosowane w tym języku nieuwzględnianie wielkości liter i szczegółowe słowa kluczowe (End If, End Sub, End Class) zwiększają czytelność. W przypadku korporacyjnych aplikacji Windows, automatyzacji pakietu Office (VBA) i szybkiego prototypowania w .NET, VB.NET pozostaje produktywnym i wydajnym językiem.