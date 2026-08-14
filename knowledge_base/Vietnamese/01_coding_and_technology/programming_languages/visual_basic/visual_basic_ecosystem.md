---
# Metadata
title: "Visual Basic — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Visual Basic ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [visual-basic, vbnet, ecosystem, tooling, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Visual Basic — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái Visual Basic (.NET).
---

## Phiên bản Visual Basic
| Phiên bản | Ghi chú |
|----------|-------|
| **VB.NET (Visual Basic 2022)** | Hiện tại, .NET 8+ |
| **VB6** | Visual Basic cổ điển (cũ) |
| **VBA** | Visual Basic cho Ứng dụng (Office) |
| **VBScript** | Ngôn ngữ kịch bản (không được dùng nữa) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## Công cụ xây dựng
| Công cụ | Mục đích |
|------|----------|
| **dotnet CLI** | .NET xây dựng, thử nghiệm, xuất bản |
| **MSBuild** | Xây dựng động cơ |
| **VisualStudio** | IDE đầy đủ |
| **NuGet** | Quản lý trọn gói |
```xml
<!-- .vbproj (SDK-style) -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <RootNamespace>MyApp</RootNamespace>
    <TargetFramework>net8.0</TargetFramework>
    <OptionStrict>On</OptionStrict>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
  </ItemGroup>
</Project>
```

---

## Khung web
| Khung | Loại | Tốt nhất cho |
|----------|------|----------|
| **Lõi ASP.NET** | Toàn ngăn xếp | API, MVC, Trang dao cạo |
| **API tối thiểu** | Nhẹ | API đơn giản |
| **Blazor** | Giao diện người dùng web | Giao diện người dùng dựa trên thành phần |
| **Tín hiệuR** | Thời gian thực | WebSockets |
```vb
' ASP.NET Core Minimal API
Imports Microsoft.AspNetCore.Builder
Imports Microsoft.Extensions.DependencyInjection

Dim builder = WebApplication.CreateBuilder(args)
Dim app = builder.Build()

app.MapGet("/hello", Function() "Hello, World!")

app.MapGet("/users/{id}", Async Function(id As Integer)
    Dim user = Await UserService.FindById(id)
    If user Is Nothing Then
        Return Results.NotFound()
    End If
    Return Results.Ok(user)
End Function)

app.Run()
```

---

## Cơ sở dữ liệu
| Công nghệ | Loại |
|----------||------|
| **Lõi khung thực thể** | ORM đầy đủ |
| **Bảnh bao** | Micro-ORM |
| **ADO.NET** | Truy cập dữ liệu cấp thấp |
| **OleDb** | Truy cập dữ liệu kế thừa |
| **MySql.Data** | Trình kết nối MySQL |
| **Npgsql** | Trình kết nối PostgreSQL |
```vb
' Dapper example
Imports Dapper
Imports System.Data.SqlClient

Using conn As New SqlConnection("connection-string")
    Dim users = Await conn.QueryAsync(Of User)(
        "SELECT Id, Name, Email FROM Users WHERE Age > @Age",
        New With {.Age = 18}
    )
    For Each user In users
        Console.WriteLine($"{user.Name} ({user.Email})")
    Next
End Using
```

---

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **xUnit** | Khung kiểm tra |
| **NUnit** | Khung kiểm tra |
| **MSTest** | Khung kiểm tra của Microsoft |
| **Moq** | Chế giễu |
| **NThay thế** | Chế giễu |
| **Khẳng định trôi chảy** | Khẳng định trôi chảy |
| **Điểm chuẩnDotNet** | Điểm chuẩn |
```vb
' xUnit test
Imports Xunit
Imports NSubstitute

Public Class UserServiceTests
    <Fact>
    Public Async Function FindUser_ReturnsUser() As Task
        ' Arrange
        Dim repo = Substitute.For(Of IUserRepository)()
        repo.GetByIdAsync(1).Returns(New User("Alice"))
        Dim service = New UserService(repo)

        ' Act
        Dim user = Await service.FindByIdAsync(1)

        ' Assert
        Assert.Equal("Alice", user.Name)
    End Function
End Class
```

---

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| **Máy phân tích Roslyn** | Phân tích tích hợp |
| **Bộ phân tích Sonar** | Quy tắc SonarQube |
| **định dạng dotnet** | Định dạng mã |
| **Cấu hình biên tập** | Phong cách nhất quán |
| **SonarQube** | Nền tảng chất lượng mã |
---

## Máy tính để bàn (WinForms / WPF)
| Khung | Mục đích |
|----------||----------|
| **WinForms** | Biểu mẫu Windows cổ điển |
| **WPF** | Giao diện người dùng Windows hiện đại (XAML) |
| **MAUI** | Đa nền tảng (kế thừa Xamarin) |
| **Avalonia** | Giống như WPF đa nền tảng |
```vb
' WinForms example
Public Class MainForm
    Inherits Form

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim name = TextBox1.Text
        MessageBox.Show($"Hello, {name}!", "Greeting")
    End Sub
End Class
```

---

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **System.Text.Json** | Tuần tự hóa JSON |
| **Newtonsoft.Json** | JSON (cũ) |
| **Serilog** | Ghi nhật ký |
| **Poly** | Chính sách kiên cường |
| **AutoMapper** | Ánh xạ đối tượng |
| **Xác thực thông thạo** | Xác thực |
| **Giao thông công cộng** | Xe buýt tin nhắn |
| **Hỏa hoạn** | Công việc nền tảng |
| **Spectre.Console** | Giao diện người dùng bảng điều khiển |
---

## Tự động hóa văn phòng (VBA)
| Công nghệ | Mục đích |
|----------||---------|
| **VBA Excel** | Tự động hóa Excel |
| **Từ VBA** | Tự động hóa từ |
| **Truy cập VBA** | Truy cập tự động hóa |
| **VBA Outlook** | Tự động hóa Outlook |
```vb
' Excel VBA example
Sub FormatReport()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Data")
    
    ws.Range("A1:D1").Font.Bold = True
    ws.Range("A1:D1").Interior.Color = RGB(0, 112, 192)
    
    ws.Columns("A:D").AutoFit
    
    MsgBox "Report formatted successfully!"
End Sub
```

---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **VisualStudio** | VB.NET IDE đầy đủ (Cộng đồng/Pro/Doanh nghiệp) |
| **Mã VS** | Nhẹ với phần mở rộng .NET |
| **Trình soạn thảo VBA** | Được tích hợp vào ứng dụng Office |
| **Người lái** | JetBrains (hỗ trợ VB hạn chế) |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Tự túc** | Gói thời gian chạy .NET |
| **Phụ thuộc vào khung** | Yêu cầu cài đặt .NET |
| **Tệp đơn** | `PublishSingleFile`|
| **Docker** | Được đóng gói |
| **MSI / ClickOnce** | Trình cài đặt Windows |
| **Dịch vụ ứng dụng Azure** | Lưu trữ đám mây |
| **IIS** | Lưu trữ Windows |
---

## Bản tóm tắt
Hệ sinh thái của Visual Basic chia sẻ cơ sở hạ tầng rộng lớn của .NET. Ngăn xếp tiêu chuẩn là: **.NET 8+** làm thời gian chạy, **Visual Studio** làm IDE, **ASP.NET Core** cho web, **Entity Framework Core** hoặc **Dapper** để truy cập dữ liệu, **xUnit** để thử nghiệm và **NuGet** cho các gói. VB.NET lý tưởng cho các nhà phát triển quen với cú pháp BASIC, những người cần truy cập vào hệ sinh thái .NET. **VBA** vẫn cần thiết cho quá trình tự động hóa Office — hàng triệu người dùng doanh nghiệp dựa vào macro Excel và Access. Hệ sinh thái này phù hợp nhất cho các ứng dụng máy tính để bàn Windows, tự động hóa Office và các ứng dụng kinh doanh dành cho doanh nghiệp.