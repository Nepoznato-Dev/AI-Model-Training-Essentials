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
# ویژوال بیسیک - اشتباهات رایج و ضد الگوها
این سند رایج ترین اشتباهات، تله ها و ضد الگوها در ویژوال بیسیک (VB.NET) را با اصلاحات فهرست می کند.
---

## 1. عدم استفاده از منابع
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

## 2.`=`در مقابل`Is`برای مقایسه شی
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

## 3. گزینه Strict Off
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

## 4. عدم استفاده از`Using`برای اتصالات پایگاه داده
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

## 5. ضد الگو: منطق کسب و کار در مدیریت رویداد
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

## خلاصه
تله‌های VB.NET: همیشه از`Using`برای منابع دور ریختنی استفاده کنید،`=`(مقدار) را از`Is`(مرجع) متمایز کنید،`Option Strict On`را فعال کنید، از بلوک‌های`Using`برای اتصالات پایگاه داده استفاده کنید، و منطق رویدادهای تجاری را از UI جدا کنید. VB.NET مدرن یک زبان دات نت قدرتمند است — از ویژگی های آن به درستی استفاده کنید.