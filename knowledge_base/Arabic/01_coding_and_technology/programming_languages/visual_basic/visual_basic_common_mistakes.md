---
# Metadata
title: "Visual Basic — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Visual Basic (VB.NET) with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# فيجوال بيسك — الأخطاء الشائعة والأنماط المضادة
يقوم هذا المستند بفهرسة الأخطاء والتراكيب والأنماط المضادة الأكثر شيوعًا في Visual Basic (VB.NET) مع التصحيحات.
---

## 1. عدم التصرف في الموارد
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

## 2.`=`مقابل`Is`لمقارنة الكائنات
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

## 3. خيار إيقاف صارم
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

## 4. عدم استخدام`Using`لاتصالات قاعدة البيانات
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

## 5. النمط المضاد: منطق الأعمال في معالجات الأحداث
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

## ملخص
اعتراضات VB.NET: استخدم دائمًا`Using`للموارد التي يمكن التخلص منها، وتمييز`=`(القيمة) عن`Is`(المرجع)، وتمكين `Option Strict On`، واستخدام كتل`Using`لاتصالات قاعدة البيانات، وفصل منطق الأعمال عن معالجات أحداث واجهة المستخدم. تعد لغة VB.NET الحديثة إحدى لغات .NET القوية — استخدم ميزاتها بشكل صحيح.