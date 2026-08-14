---
# Metadata
title: "Visual Basic — Version History & Evolution"
description: "Comprehensive version history and evolution of Visual Basic from VB 1.0 to modern VB.NET."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [visual-basic, vb6, vbdotnet, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Visual Basic — Lịch sử phiên bản & Tiến hóa
## Dòng thời gian
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| CƠ BẢN | 1964 | **CƠ BẢN gốc** (Kemeny & Kurtz, Dartmouth) |
| GW-CƠ BẢN | 1983 | BASIC của Microsoft dành cho PC IBM |
| QuickBASIC | 1985 | Cấu trúc BASIC, IDE, trình biên dịch |
| VB 1.0 | 1991 | **Visual Basic 1.0** — lập trình trực quan cho Windows |
| VB 2.0 | 1992 | Các biểu mẫu dựa trên đối tượng nhanh hơn |
| VB 3.0 | 1993 | **Hỗ trợ cơ sở dữ liệu** (Kiểm soát dữ liệu), Động cơ phản lực |
| VB 4.0 | 1995 | 32-bit, các lớp (không kế thừa) |
| VB 5.0 | 1997 | **Thành phần COM**, điều khiển do người dùng vẽ |
| VB 6.0 | 1998 | **Chuyên ngành**: COM, ADO, DCOM, WebClass — VB cổ điển |
| VB.NET | 2002 | **Chuyên ngành**: .NET Framework — OOP, kế thừa, GC |
| VB.NET 2003 | 2003 | .NET 1.1, IDE cải tiến |
| VB 2005 | 2005 | **Không gian tên của tôi**,`Using`,`Continue`, chỉnh sửa và tiếp tục |
| VB 2008 | 2008 | **LINQ**, chữ XML, kiểu ẩn danh, toán tử`If`|
| VB 2010 | 2010 | Lambda nhiều dòng, động, đồng phương sai |
| VB 2012 | 2012 | `Async`/`Await`, trình vòng lặp |
| VB 2015 | 2015 | Nội suy chuỗi`$""`,`?.`vô điều kiện , nameof |
| VB 2017 | 2017 | Bộ dữ liệu, trả về ref, khớp mẫu |
| VB 15.3 | 2017 | Giải cấu trúc không tuple |
| VB 15.5 | 2017 | Tham khảo người dân địa phương, thành viên chỉ đọc |
| VB 16.0 | 2019 | **Các loại tham chiếu có thể rỗng**, biểu thức`Switch`|
| VB 16.9 | 2021 |  Cải tiến`OrElse`|
| VB 17.0 | 2022 | **Chuỗi ký tự thô**, cấu trúc mặc định tự động, cải tiến`Module`|
| VB 17.7 | 2024 | Cải tiến thêm |
## Các cột mốc quan trọng
### Nguồn gốc CƠ BẢN (1964–1990)
- **1964**: John Kemeny & Thomas Kurtz tạo ra BASIC tại Đại học Dartmouth
- **Mục tiêu**: Giúp sinh viên không chuyên về khoa học có thể tiếp cận chương trình
- **1983**: GW-BASIC — BASIC của Microsoft dành cho PC IBM
- **1985**: QuickBASIC — lập trình có cấu trúc, IDE, trình biên dịch
- Các tính năng chính:`GOTO`,`GOSUB`,`LET`,`INPUT`,`PRINT`,`FOR`/ `NEXT`
### Visual Basic 1–6: Kỷ nguyên cổ điển (1991–2001)
- **1.0 (1991)**: Lập trình trực quan — trình tạo GUI kéo và thả cho Windows
- **2.0 (1992)**: Biểu mẫu dựa trên đối tượng, nhanh hơn
- **3.0 (1993)**: Hỗ trợ cơ sở dữ liệu — Kiểm soát dữ liệu, Động cơ phản lực
- **4.0 (1995)**: 32-bit (Windows 95), các lớp
- **5.0 (1997)**: Thành phần COM, điều khiển do người dùng vẽ
- **6.0 (1998)**: **VB cổ điển** — COM, ADO, DCOM, WebClass
  - Phiên bản được sử dụng rộng rãi nhất
  - Phát triển ứng dụng nhanh (RAD)
  - Vẫn chạy hàng triệu ứng dụng cũ
### VB.NET: Cuộc cách mạng .NET (2002–nay)
- **2002**: VB.NET — viết lại hoàn toàn trên .NET Framework
  - True OOP - kế thừa, giao diện, đa hình
  - Thu gom rác
  - Truy cập vào toàn bộ thư viện lớp .NET
- **2005**: Không gian tên`My`(dễ dàng truy cập vào các thao tác thông thường)
- **2008**: **LINQ** — cú pháp truy vấn được tích hợp vào ngôn ngữ
- **2012**:`Async`/`Await`— lập trình không đồng bộ
- **2015**: Nội suy chuỗi`$""`,`?.`vô điều kiện 
- **2017**: Bộ dữ liệu, khớp mẫu
- **2019**: Các loại tham chiếu có thể rỗng
- **2022**: Chuỗi ký tự thô, cú pháp hiện đại
## Tiến hóa cú pháp
```vb
' GW-BASIC (1983): Line numbers, GOTO
10 INPUT "Name: "; N$
20 PRINT "Hello, "; N$
30 GOTO 10

' QuickBASIC (1985): Structured programming
INPUT "Name: "; N$
PRINT "Hello, "; N$
FOR I = 1 TO 10
    PRINT I
NEXT I

' Visual Basic 6.0 (1998): Event-driven, GUI
Private Sub Command1_Click()
    Dim name As String
    name = Text1.Text
    MsgBox "Hello, " & name & "!"
End Sub

' VB.NET 2002: OOP, .NET
Class Person
    Public Name As String
    Public Age As Integer

    Sub New(ByVal n As String, ByVal a As Integer)
        Name = n
        Age = a
    End Sub
End Class

' VB 2008: LINQ
Dim query = From p In people
            Where p.Age > 18
            Select p.Name

' VB 2015: String interpolation, null-conditional
Dim message = $"Hello, {person?.Name ?? "Unknown"}!"

' VB 2017: Tuples, pattern matching
Dim result = (Name:="Alice", Age:=30)
Select Case result
    Case ("Alice", 30)
        Console.WriteLine("Found Alice!")
End Select

' VB 17.0 (2022): Raw string literals
Dim json = """
    {
        "name": "Alice",
        "age": 30
    }
    """

' Modern VB.NET: Async/Await
Async Function GetDataAsync() As Task(Of String)
    Dim client As New HttpClient()
    Dim result = Await client.GetStringAsync("https://api.example.com/data")
    Return result
End Function
```

## Tiến hóa tính năng
```
BASIC (1964):    INPUT, PRINT, LET, FOR/NEXT, GOTO, GOSUB
QuickBASIC (1985): Structured programming, SUB/FUNCTION, TYPE
VB 1.0 (1991):   Visual programming, event-driven, GUI builder
VB 3.0 (1993):   Database (Data Control, Jet)
VB 4.0 (1995):   32-bit, classes
VB 6.0 (1998):   COM, ADO, DCOM, WebClass
VB.NET (2002):   OOP, GC, .NET Framework
VB 2005:         My namespace, Using, edit-and-continue
VB 2008:         LINQ, XML literals, anonymous types
VB 2012:         Async/Await, iterators
VB 2015:         String interpolation, null-conditional
VB 2017:         Tuples, pattern matching
VB 16.0 (2019):  Nullable reference types
VB 17.0 (2022):  Raw string literals, auto-default structs
```

## Nguyên tắc thiết kế chính
```
1. "Accessible" — easy to learn, beginner-friendly
2. "Visual" — drag-and-drop GUI design
3. "Productive" — rapid application development
4. "Readable" — English-like syntax
5. "Evolving" — from BASIC to modern .NET language
6. "Compatible" — backward compatible within each era
```

## Tăng trưởng hệ sinh thái
```
1964: BASIC created at Dartmouth College
1983: GW-BASIC — Microsoft BASIC for PC
1985: QuickBASIC — structured programming
1991: Visual Basic 1.0 — visual programming
1998: VB 6.0 — classic VB, COM, ADO
2002: VB.NET — .NET Framework, OOP
2008: VB 2008 — LINQ
2012: VB 2012 — async/await
2022: VB 17.0 — raw string literals, modern syntax
2025: Visual Basic (.NET) used in:
       - Windows desktop applications (WinForms, WPF)
       - Legacy VB6 applications (still running in businesses)
       - Office automation (VBA — Visual Basic for Applications)
       - ASP.NET web applications
       Microsoft continues VB.NET alongside C# on .NET
       VBA still embedded in Excel, Word, Access, Outlook
```
