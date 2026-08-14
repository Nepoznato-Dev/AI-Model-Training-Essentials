<!--
---
# Metadata
title: "Visual Basic — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Visual Basic (VB.NET) with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [visual-basic, vbnet, common-mistakes, anti-patterns, pitfalls, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Visual Basic — распространенные ошибки и антишаблоны
В этом документе перечислены наиболее распространенные ошибки, ловушки и антишаблоны в Visual Basic (VB.NET) с исправлениями.
---

## 1. Не распоряжаться ресурсами
```vb
' ❌ WRONG — resource leak
Dim reader As New StreamReader("data.txt")
Dim data As String = reader.ReadToEnd()
reader.Close()  ' skipped if ReadToEnd throws

' ✅ CORRECT — Using block
Using reader As New StreamReader("data.txt")
    Dim data As String = reader.ReadToEnd()
End Using  ' automatically disposed
```

---

## 2.`=`и`Is`для сравнения объектов
```vb
' ❌ WRONG — = for reference comparison
Dim a As Object = "hello"
Dim b As Object = "hello"
If a = b Then  ' value comparison, not reference
If a Is b Then  ' reference comparison
End If

' ✅ CORRECT — use Is for reference, = for value
If name = "Alice" Then  ' string value comparison
If obj1 Is obj2 Then    ' same object?
If obj1 Is Nothing Then ' null check
End If
```

---

## 3. Опция «Строгое выключение»
```vb
' ❌ WRONG — late binding and implicit conversions
Option Strict Off
Dim x As Integer = "42"  ' implicit conversion
Dim obj As Object = "hello"
Dim len As Integer = obj.Length  ' late binding

' ✅ CORRECT — enable Option Strict
Option Strict On
Dim x As Integer = Integer.Parse("42")
Dim s As String = "hello"
Dim len As Integer = s.Length
```

---

## 4. Не использовать`Using`для подключений к базе данных
```vb
' ❌ WRONG — connection not closed on error
Dim conn As New SqlConnection(connString)
conn.Open()
Dim cmd As New SqlCommand("SELECT * FROM Users", conn)
Dim reader As SqlDataReader = cmd.ExecuteReader()
' ... use reader ...
conn.Close()  ' never reached on exception

' ✅ CORRECT — nested Using blocks
Using conn As New SqlConnection(connString)
    conn.Open()
    Using cmd As New SqlCommand("SELECT * FROM Users", conn)
        Using reader As SqlDataReader = cmd.ExecuteReader()
            ' ... use reader ...
        End Using
    End Using
End Using
```

---

## 5. Антипаттерн: бизнес-логика в обработчиках событий
```vb
' ❌ WRONG — everything in button click
Private Sub btnSave_Click(sender As Object, e As EventArgs)
    ' validation, database access, email, all here
End Sub

' ✅ CORRECT — separate concerns
Private Sub btnSave_Click(sender As Object, e As EventArgs)
    UserService.Save(txtName.Text, txtEmail.Text)
End Sub
```

---

## Краткое содержание
Ловушки VB.NET: всегда используйте`Using`для одноразовых ресурсов, отличайте`=`(значение) от`Is`(ссылка), включите `Option Strict On`, используйте блоки`Using`для подключений к базе данных и отделяйте бизнес-логику от обработчиков событий пользовательского интерфейса. Современный VB.NET — мощный язык .NET — используйте его возможности правильно.