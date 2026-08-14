---
# Metadata
title: "Visual Basic — Cheat Sheet"
description: "Quick-reference cheat sheet for Visual Basic (.NET) syntax and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [visual-basic, vb-net, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Visual Basic — Aide-mémoire
## Bases
```vb
Option Strict On
Option Infer On

' Variables
Dim name As String = "Alice"
Dim age As Integer = 30
Dim pi As Double = 3.14159
Dim active As Boolean = True
Dim inferred = "hello"     ' type inferred
Const MAX As Integer = 100

' Nullable
Dim email As String? = Nothing
Dim count As Integer? = Nothing
Dim value = email ?? "default"   ' null coalescing

' String interpolation
$"Hello, {name}!"
$"Age: {age}"
$"Pi: {pi:F2}"

' String methods
name.Length
name.ToUpper()
name.ToLower()
name.Trim()
name.Contains("lic")
name.Replace("Alice", "Bob")
name.Substring(0, 3)
name.Split(" "c)
String.Join(", ", items)
String.Format("Hello, {0}!", name)
```

## Structures de données
```vb
' Array
Dim arr() As Integer = {1, 2, 3}
arr(0)
arr.Length
Array.Sort(arr)

' List(Of T)
Dim list As New List(Of String) From {"Alice", "Bob"}
list.Add("Charlie")
list(0)
list.Count
list.Remove("Bob")
list.Where(Function(x) x.Length > 3).ToList()

' Dictionary(Of K, V)
Dim dict As New Dictionary(Of String, Integer)
dict("alice") = 90
dict.Add("bob", 85)
dict.ContainsKey("alice")
dict.GetValueOrDefault("unknown", 0)
dict.Keys
dict.Values

' HashSet
Dim set As New HashSet(Of Integer) From {1, 2, 3}
set.Add(4)
set.Contains(2)

' Tuple
Dim t = (1, "hello")
t.Item1
Dim (x, s) = (1, "hello")    ' deconstruct
```

## Flux de contrôle
```vb
' If
If condition Then
    ' ...
ElseIf other Then
    ' ...
Else
    ' ...
End If

' Ternary
Dim result = If(condition, "yes", "no")

' Select Case
Select Case day
    Case "Monday", "Tuesday"
        Console.WriteLine("early week")
    Case "Wednesday"
        Console.WriteLine("midweek")
    Case Else
        Console.WriteLine("later")
End Select

' Loops
For Each item In collection
    Console.WriteLine(item)
Next

For i As Integer = 0 To 9
    Console.WriteLine(i)
Next

For i As Integer = 9 To 0 Step -1
    Console.WriteLine(i)
Next

While condition
    ' ...
End While

Do
    ' ...
Loop While condition
```

## Cours
```vb
' Class
Public Class User
    Public Property Name As String
    Public Property Age As Integer

    Public Sub New(name As String, age As Integer)
        Me.Name = name
        Me.Age = age
    End Sub

    Public Function Greet() As String
        Return $"Hi, I'm {Name}"
    End Function
End Class

' Record (VB 15+)
Public Record Point(X As Double, Y As Double)

' Interface
Public Interface IRenderable
    Function Render() As String
End Interface

' Inheritance
Public Class Admin
    Inherits User
    Public Property Permissions As String()
End Class
```

##LINQ
```vb
' Query syntax
Dim adults = From u In users
             Where u.Age >= 18
             Order By u.Name
             Select u.Name

' Method syntax
Dim names = users _
    .Where(Function(u) u.Age >= 18) _
    .OrderBy(Function(u) u.Name) _
    .Select(Function(u) u.Name) _
    .ToList()

' Aggregation
Dim total = items.Sum(Function(i) i.Price)
Dim avg = items.Average(Function(i) i.Rating)
Dim groups = items.GroupBy(Function(i) i.Category)
Dim exists = items.Any(Function(i) i.Active)
Dim first = items.First(Function(i) i.Active)
```

## Async/Attendre
```vb
' Async method
Public Async Function GetUserAsync(id As Integer) As Task(Of User)
    Using client As New HttpClient()
        Dim response = Await client.GetAsync($"/api/users/{id}")
        response.EnsureSuccessStatusCode()
        Return Await response.Content.ReadFromJsonAsync(Of User)()
    End Using
End Function

' Parallel async
Dim task1 = FetchUsersAsync()
Dim task2 = FetchPostsAsync()
Await Task.WhenAll(task1, task2)
```

## Gestion des erreurs
```vb
Try
    Dim result = RiskyOperation()
Catch ex As InvalidOperationException
    Console.WriteLine($"Bad operation: {ex.Message}")
Catch ex As Exception
    Console.WriteLine($"Error: {ex.Message}")
Finally
    Cleanup()
End Try

Throw New ArgumentException("Invalid input")
```

## Modèles courants
```vb
' Using block
Using reader As New StreamReader("data.txt")
    Dim content = reader.ReadToEnd()
End Using

' With block
With employee
    .Name = "Alice"
    .Department = "Engineering"
End With

' If operator
Dim name = If(user?.Name, "Unknown")

' Pattern matching (VB 15+)
Select Case shape
    Case c As Circle
        area = Math.PI * c.Radius ^ 2
    Case r As Rectangle
        area = r.Width * r.Height
End Select

' Extension method
<Extension()>
Function IsEmail(s As String) As Boolean
    Return s.Contains("@")
End Function
```
