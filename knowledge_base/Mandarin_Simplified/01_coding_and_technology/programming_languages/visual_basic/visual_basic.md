<!--
---
# Metadata
title: "Visual Basic"
description: "Comprehensive reference for the Visual Basic programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [visual-basic, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "33 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# 视觉基础
Visual Basic (VB) 是 Microsoft 开发的一种编程语言。它已经发展了几代：最初的 Visual Basic (1991)、Visual Basic 6.0 (1998)、VB.NET（2002，.NET Framework 的一部分）和 Visual Basic ..NET（当前，现在简称为“Visual Basic”，作为 .NET 的一部分）。 VB 旨在方便初学者和快速应用程序开发 (RAD)，重点关注图形用户界面和事件驱动编程。
如今，VB.NET 继续与 C# 一起成为 .NET 生态系统的一部分，尽管 Microsoft 已表示 C# 是未来的主要语言。 VB 在企业环境中仍然广泛使用，特别是旧版 Windows 应用程序、办公自动化 (VBA) 和内部业务工具。
---

## 为什么 Visual Basic 很重要
- **初学者友好**：有史以来最平易近人的编程语言之一。类似英语的语法。
- **快速应用程序开发**：拖放式 GUI 构建器可以快速构建 Windows 表单。
- **VBA（Visual Basic for Applications）**：Microsoft Office 的宏语言 — 全球数百万商业用户使用。
- **企业遗留**：许多关键业务 Windows 应用程序都是用 VB6 或 VB.NET 编写的。
- **.NET 生态系统访问**：VB.NET 可以使用所有 .NET 库和框架。
## 权衡
|限制|详情 |典型解决方法|
|------------|---------|--------------------|
| **相关性下降** |微软优先考虑C#； VB 处于维护模式 |使用 C# 进行新项目 |
| **VB6 已过时** |不再支持；不能在现代.NET 上运行|迁移到 VB.NET 或 C# |
| **跨平台有限** |主要针对 Windows |使用C#或其他语言进行跨平台|
| **较小的社区** |新资源、图书馆或职位发布更少 |利用 .NET/C# 资源 |
| **VBA 限制** |与现代语言相比，VBA 已经过时且有局限性 |使用 Python 或 Office 脚本实现复杂的自动化 |
---

## 语法基础知识
### VB.NET 示例
```vb
' Variables and types
Dim name As String = "Alice"
Dim age As Integer = 30
Dim score As Double = 9.5
Dim active As Boolean = True

' String interpolation
Console.WriteLine($"Hello, {name}! Age: {age}")

' Conditional
If age >= 18 Then
    Console.WriteLine("Adult")
ElseIf age >= 13 Then
    Console.WriteLine("Teenager")
Else
    Console.WriteLine("Child")
End If

' Loop
For i As Integer = 1 To 10
    Console.WriteLine(i)
Next

For Each item In collection
    Console.WriteLine(item)
Next

' Function
Function Add(a As Integer, b As Integer) As Integer
    Return a + b
End Function

' Class
Public Class Animal
    Public Property Name As String
    
    Public Sub New(name As String)
        Me.Name = name
    End Sub
    
    Public Overridable Function Speak() As String
        Return $"{Name} makes a sound"
    End Function
End Class

Public Class Dog
    Inherits Animal
    
    Public Overrides Function Speak() As String
        Return $"{Name} says woof"
    End Function
End Class
```

### VBA 示例（办公自动化）
```vb
' Excel VBA — automate spreadsheet tasks
Sub FormatReport()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Data")
    
    ' Format header row
    With ws.Range("A1:D1")
        .Font.Bold = True
        .Interior.Color = RGB(0, 112, 192)
        .Font.Color = RGB(255, 255, 255)
    End With
    
    ' Auto-fit columns
    ws.Columns("A:D").AutoFit
    
    ' Add formula
    ws.Range("E2").Formula = "=SUM(C2:C100)"
    
    MsgBox "Report formatted successfully!", vbInformation
End Sub
```
---

## 高级语法和模式
### LINQ（语言集成查询）
```vb
' LINQ lets you query collections, databases, and XML with SQL-like syntax

' Query data from a list
Dim employees As New List(Of Employee) From {
    New Employee With {.Name = "Alice", .Department = "IT", .Salary = 85000},
    New Employee With {.Name = "Bob", .Department = "HR", .Salary = 65000},
    New Employee With {.Name = "Charlie", .Department = "IT", .Salary = 95000},
    New Employee With {.Name = "Diana", .Department = "IT", .Salary = 75000}
}

' Query syntax (SQL-like)
Dim itEmployees = From emp In employees
                  Where emp.Department = "IT"
                  Where emp.Salary > 80000
                  Order By emp.Salary Descending
                  Select emp.Name, emp.Salary

' Method syntax (lambda expressions)
Dim highEarners = employees _
    .Where(Function(e) e.Department = "IT" AndAlso e.Salary > 80000) _
    .OrderByDescending(Function(e) e.Salary) _
    .Select(Function(e) $"{e.Name}: ${e.Salary:N0}")

' Group by
Dim byDepartment = From emp In employees
                   Group By emp.Department Into DeptGroup = Group
                   Select Department, Count = DeptGroup.Count(), AvgSalary = DeptGroup.Average(Function(e) e.Salary)

' Aggregation
Dim totalSalary = employees.Sum(Function(e) e.Salary)
Dim avgSalary = employees.Average(Function(e) e.Salary)
Dim maxSalary = employees.Max(Function(e) e.Salary)
Dim topEarners = employees.Take(3).OrderByDescending(Function(e) e.Salary)

' Join two collections
Dim departments As New List(Of Department) From {
    New Department With {.Name = "IT", .Floor = 3},
    New Department With {.Name = "HR", .Floor = 1}
}

Dim empWithFloor = From emp In employees
                   Join dept In departments On emp.Department Equals dept.Name
                   Select emp.Name, dept.Floor, emp.Department
```

### 异步/等待
```vb
' Asynchronous programming in VB.NET
Imports System.Net.Http
Imports System.Threading.Tasks

Public Class DataService
    Private ReadOnly _client As New HttpClient()

    ' Async function returns Task(Of T)
    Async Function FetchUserDataAsync(userId As String) As Task(Of User)
        Dim url As String = $"https://api.example.com/users/{userId}"
        
        Try
            Dim response As HttpResponseMessage = Await _client.GetAsync(url)
            response.EnsureSuccessStatusCode()
            
            Dim json As String = Await response.Content.ReadAsStringAsync()
            Dim user As User = JsonSerializer.Deserialize(Of User)(json)
            Return user
        Catch ex As HttpRequestException
            Console.WriteLine($"HTTP error: {ex.Message}")
            Return Nothing
        Catch ex As JsonException
            Console.WriteLine($"JSON parse error: {ex.Message}")
            Return Nothing
        End Try
    End Function

    ' Multiple async operations in parallel
    Async Function FetchAllUsersAsync(userIds As IEnumerable(Of String)) As Task(Of List(Of User))
        Dim tasks As IEnumerable(Of Task(Of User)) =
            userIds.Select(Function(id) FetchUserDataAsync(id))
        
        Dim results As User() = Await Task.WhenAll(tasks)
        Return results.Where(Function(u) u IsNot Nothing).ToList()
    End Function

    ' Async with cancellation
    Async Function DownloadWithCancelAsync(url As String, ct As CancellationToken) As Task(Of String)
        Dim response As HttpResponseMessage = Await _client.GetAsync(url, ct)
        Return Await response.Content.ReadAsStringAsync()
    End Function
End Class

' Calling async code
Sub Main()
    Dim service As New DataService()
    Dim user As User = service.FetchUserDataAsync("123").Result
    
    ' Or in an async context:
    ' Dim user = Await service.FetchUserDataAsync("123")
End Sub
```

### 我的命名空间
```vb
' The My namespace provides quick access to common .NET functionality

' File system operations
My.Computer.FileSystem.WriteAllText("log.txt", "Hello, World!", True)
Dim content As String = My.Computer.FileSystem.ReadAllText("config.ini")
Dim files = My.Computer.FileSystem.GetFiles("C:\Data", FileIO.SearchOption.SearchAllSubDirectories)

' Network
If My.Computer.Network.IsAvailable Then
    Dim pingResult As Boolean = My.Computer.Network.Ping("www.google.com")
End If

' Application info
Dim version As String = My.Application.Info.Version.ToString()
Dim appDir As String = My.Application.Info.DirectoryPath

' User and environment
Dim userName As String = My.User.Name
Dim isAuth As Boolean = My.User.IsAuthenticated()

' Resources
Dim icon As Drawing.Icon = My.Resources.AppIcon
Dim connString As String = My.Settings.ConnectionString
```

### COM 互操作
```vb
' Interact with COM objects (Office, Windows Shell, etc.)
Imports Excel = Microsoft.Office.Interop.Excel

Public Class ExcelAutomation
    Public Sub GenerateReport()
        Dim excelApp As New Excel.Application
        excelApp.Visible = False
        
        Try
            Dim workbook As Excel.Workbook = excelApp.Workbooks.Add()
            Dim sheet As Excel.Worksheet = workbook.Sheets(1)
            
            ' Write data
            sheet.Cells(1, 1).Value = "Name"
            sheet.Cells(1, 2).Value = "Score"
            sheet.Cells(2, 1).Value = "Alice"
            sheet.Cells(2, 2).Value = 95
            
            ' Format
            sheet.Range("A1:B1").Font.Bold = True
            sheet.Columns.AutoFit()
            
            ' Save
            workbook.SaveAs("C:\Reports\output.xlsx")
            workbook.Close(False)
        Finally
            excelApp.Quit()
            Runtime.InteropServices.Marshal.ReleaseComObject(excelApp)
        End Try
    End Sub
End Class
```
---

## 深入探讨核心功能
### Windows 窗体模式
```vb
' Windows Forms: event-driven GUI programming
Public Class MainForm
    Inherits Form

    Private WithEvents _btnSubmit As New Button()
    Private _txtInput As New TextBox()
    Private _lblResult As New Label()

    Public Sub New()
        Text = "My Application"
        Size = New Drawing.Size(400, 300)
        StartPosition = FormStartPosition.CenterScreen

        _txtInput.Location = New Drawing.Point(20, 20)
        _txtInput.Size = New Drawing.Size(200, 25)

        _btnSubmit.Text = "Submit"
        _btnSubmit.Location = New Drawing.Point(230, 18)

        _lblResult.Location = New Drawing.Point(20, 60)
        _lblResult.AutoSize = True

        Controls.AddRange({_txtInput, _btnSubmit, _lblResult})
    End Sub

    Private Sub BtnSubmit_Click(sender As Object, e As EventArgs) Handles _btnSubmit.Click
        Dim input As String = _txtInput.Text.Trim()
        If String.IsNullOrEmpty(input) Then
            MessageBox.Show("Please enter a value.", "Validation",
                MessageBoxButtons.OK, MessageBoxIcon.Warning)
            Return
        End If
        _lblResult.Text = $"You entered: {input}"
    End Sub
End Class
```

### 数据库连接 (ADO.NET)
```vb
Imports System.Data.SqlClient

Public Class DataAccess
    Private ReadOnly _connStr As String =
        "Server=localhost;Database=MyApp;Trusted_Connection=True;TrustServerCertificate=True"

    ' Read data
    Function GetUsers() As List(Of User)
        Dim users As New List(Of User)
        
        Using conn As New SqlConnection(_connStr)
            Dim cmd As New SqlCommand("SELECT Id, Name, Email FROM Users WHERE Active = @active", conn)
            cmd.Parameters.AddWithValue("@active", True)
            
            conn.Open()
            Using reader As SqlDataReader = cmd.ExecuteReader()
                While reader.Read()
                    users.Add(New User With {
                        .Id = reader.GetInt32(0),
                        .Name = reader.GetString(1),
                        .Email = reader.GetString(2)
                    })
                End While
            End Using
        End Using
        
        Return users
    End Function

    ' Write data with transaction
    Sub CreateUser(name As String, email As String)
        Using conn As New SqlConnection(_connStr)
            conn.Open()
            Using transaction = conn.BeginTransaction()
                Try
                    Dim cmd As New SqlCommand(
                        "INSERT INTO Users (Name, Email, CreatedAt) VALUES (@name, @email, GETDATE())",
                        conn, transaction)
                    cmd.Parameters.AddWithValue("@name", name)
                    cmd.Parameters.AddWithValue("@email", email)
                    cmd.ExecuteNonQuery()
                    
                    transaction.Commit()
                Catch ex As Exception
                    transaction.Rollback()
                    Throw
                End Try
            End Using
        End Using
    End Sub
End Class
```

＃＃＃ 反射
```vb
Imports System.Reflection

Public Class ReflectionHelper
    ' Inspect types at runtime
    Sub InspectType(obj As Object)
        Dim t As Type = obj.GetType()
        
        Console.WriteLine($"Type: {t.FullName}")
        Console.WriteLine($"Assembly: {t.Assembly.GetName().Name}")
        
        ' List properties
        For Each prop As PropertyInfo In t.GetProperties()
            Console.WriteLine($"  Property: {prop.Name} ({prop.PropertyType.Name})")
        Next
        
        ' List methods
        For Each method As MethodInfo In t.GetMethods(BindingFlags.Public Or BindingFlags.Instance)
            If Not method.IsSpecialName Then
                Console.WriteLine($"  Method: {method.Name}({String.Join(", ", method.GetParameters().Select(Function(p) p.ParameterType.Name))})")
            End If
        Next
    End Sub

    ' Create instances dynamically
    Function CreateInstance(assemblyName As String, typeName As String) As Object
        Dim asm As Assembly = Assembly.Load(assemblyName)
        Dim t As Type = asm.GetType(typeName)
        Return Activator.CreateInstance(t)
    End Function
End Class
```
---

## 项目配置和构建系统
### .vbproj 文件结构
```xml
<!-- MyApp.vbproj - Visual Basic project file -->
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <RootNamespace>MyApp</RootNamespace>
    <AssemblyName>MyApp</AssemblyName>
    <TargetFramework>net8.0</TargetFramework>
    <Version>1.0.0</Version>
    <Authors>Development Team</Authors>
    <Description>My Visual Basic Application</Description>
    <OptionStrict>On</OptionStrict>
    <OptionInfer>On</OptionInfer>
  </PropertyGroup>

  <!-- NuGet packages -->
  <ItemGroup>
    <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
    <PackageReference Include="Microsoft.Data.SqlClient" Version="5.1.2" />
    <PackageReference Include="Serilog" Version="3.1.1" />
  </ItemGroup>

  <!-- Project references -->
  <ItemGroup>
    <ProjectReference Include="..\SharedLib\SharedLib.vbproj" />
  </ItemGroup>

</Project>
```

### 解决方案文件
```
# MyApp.sln - Visual Studio solution file
Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
Project("{F184B08F-C81C-45F6-A57F-5ABD9991F28F}") = "MyApp", "src\MyApp\MyApp.vbproj", "{GUID1}"
EndProject
Project("{F184B08F-C81C-45F6-A57F-5ABD9991F28F}") = "SharedLib", "src\SharedLib\SharedLib.vbproj", "{GUID2}"
EndProject
Global
    GlobalSection(SolutionConfigurationPlatforms) = preSolution
        Debug|Any CPU = Debug|Any CPU
        Release|Any CPU = Release|Any CPU
    EndGlobalSection
EndGlobal
```

### NuGet 配置
```xml
<!-- nuget.config -->
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <packageSources>
    <add key="nuget.org" value="https://api.nuget.org/v3/index.json" />
    <add key="PrivateFeed" value="https://pkgs.dev.azure.com/myorg/_packaging/myfeed/nuget/v3/index.json" />
  </packageSources>
  <packageRestore>
    <add key="enabled" value="True" />
    <add key="automatic" value="True" />
  </packageRestore>
</configuration>
```

---

## 测试
### MS测试
```vb
Imports Microsoft.VisualStudio.TestTools.UnitTesting

<TestClass()>
Public Class CalculatorTests

    Private calc As Calculator

    <TestInitialize()>
    Public Sub Setup()
        calc = New Calculator()
    End Sub

    <TestMethod()>
    Public Sub Add_TwoPositiveNumbers_ReturnsSum()
        Dim result = calc.Add(2, 3)
        Assert.AreEqual(5, result)
    End Sub

    <TestMethod()>
    Public Sub Divide_ByZero_ThrowsException()
        Assert.ThrowsException(Of ArgumentException)(
            Sub()
                calc.Divide(10, 0)
            End Sub)
    End Sub

    <TestMethod()>
    <DataRow(1, 2, 3)>
    <DataRow(-1, 1, 0)>
    <DataRow(0, 0, 0)>
    <DataRow(100, 200, 300)>
    Public Sub Add_VariousInputs_ReturnsExpected(a As Integer, b As Integer, expected As Integer)
        Assert.AreEqual(expected, calc.Add(a, b))
    End Sub
End Class
```

### NUnit
```vb
Imports NUnit.Framework

<TestFixture()>
Public Class UserServiceTests

    Private _service As UserService
    Private _mockRepo As MockUserRepository

    <SetUp()>
    Public Sub Setup()
        _mockRepo = New MockUserRepository()
        _service = New UserService(_mockRepo)
    End Sub

    <Test()>
    Public Async Function GetUser_WithValidId_ReturnsUser() As Task
        ' Arrange
        _mockRepo.Setup_GetUser("1", New User With {.Id = 1, .Name = "Alice"})
        
        ' Act
        Dim result = Await _service.GetUserAsync("1")
        
        ' Assert
        Assert.That(result, Is.Not.Null)
        Assert.That(result.Name, Is.EqualTo("Alice"))
    End Function

    <Test()>
    Public Sub CreateUser_WithDuplicateEmail_ThrowsException()
        _mockRepo.Setup_GetUserByEmail("test@mail.com", New User())
        
        Assert.ThrowsAsync(Of DuplicateUserException)(
            Async Function()
                Await _service.CreateUserAsync("test@mail.com", "Test")
            End Function)
    End Sub
End Class
```
---

## 互操作性
### C# 互操作
```vb
' VB.NET and C# are fully interoperable within .NET
' You can reference C# assemblies from VB.NET and vice versa

' Calling a C# library from VB.NET:
' C# defines: public class UserService { public async Task<User> GetUserAsync(int id) { ... } }

' VB.NET consumes it directly:
Dim service As New UserService()
Dim user As User = Await service.GetUserAsync(42)

' Using C# records from VB.NET:
' C# record: public record UserDto(string Name, string Email);
Dim dto As New UserDto("Alice", "alice@mail.com")
Console.WriteLine($"Name: {dto.Name}, Email: {dto.Email}")
```

### .NET 生态系统集成
```vb
' Using any NuGet package from the .NET ecosystem
Imports System.Text.Json
Imports Microsoft.Extensions.Logging
Imports Serilog

' JSON serialization
Dim user As New User With {.Name = "Alice", .Email = "alice@mail.com"}
Dim json As String = JsonSerializer.Serialize(user, New JsonSerializerOptions With {
    .WriteIndented = True,
    .PropertyNamingPolicy = JsonNamingPolicy.CamelCase
})

' Logging with Serilog
Log.Logger = New LoggerConfiguration() _
    .MinimumLevel.Information() _
    .WriteTo.Console() _
    .WriteTo.File("logs/app-.log", rollingInterval:=RollingInterval.Day) _
    .CreateLogger()

Log.Information("Application started")
Log.Warning("Low disk space: {SpaceMB}MB remaining", 150)

Try
    Throw New InvalidOperationException("Test error")
Catch ex As Exception
    Log.Error(ex, "An error occurred during processing")
End Try
```

---

## 设计模式
### 模式 1：单例
```vb
Public NotInheritable Class AppConfig
    Private Shared _instance As Lazy(Of AppConfig) =
        New Lazy(Of AppConfig)(Function() New AppConfig())

    Public Shared ReadOnly Property Instance As AppConfig
        Get
            Return _instance.Value
        End Get
    End Property

    Public Property ConnectionString As String
    Public Property LogLevel As String = "Information"

    Private Sub New()
        ' Load configuration
        ConnectionString = My.Settings.ConnectionString
    End Sub
End Class
```

### 模式 2：观察者（事件驱动）
```vb
Public Class OrderService
    Public Event OrderPlaced As EventHandler(Of OrderEventArgs)
    Public Event OrderCancelled As EventHandler(Of OrderEventArgs)

    Public Sub PlaceOrder(order As Order)
        ' Process order...
        RaiseEvent OrderPlaced(Me, New OrderEventArgs(order))
    End Sub

    Public Sub CancelOrder(orderId As Integer)
        ' Cancel order...
        RaiseEvent OrderCancelled(Me, New OrderEventArgs(orderId))
    End Sub
End Class

' Subscribe to events
Dim service As New OrderService()
AddHandler service.OrderPlaced, Sub(sender, e)
    Console.WriteLine($"Order {e.Order.Id} placed at {DateTime.Now}")
End Sub
```

### 模式 3：具有工作单元的存储库
```vb
Public Interface IRepository(Of T)
    Function GetById(id As Integer) As T
    Function GetAll() As IEnumerable(Of T)
    Sub Add(entity As T)
    Sub Update(entity As T)
    Sub Delete(id As Integer)
End Interface

Public Class UnitOfWork
    Implements IDisposable
    Private ReadOnly _context As DbContext
    Private _userRepository As IRepository(Of User)
    Private _orderRepository As IRepository(Of Order)

    Public ReadOnly Property Users As IRepository(Of User)
        Get
            If _userRepository Is Nothing Then
                _userRepository = New UserRepository(_context)
            End If
            Return _userRepository
        End Get
    End Property

    Public Sub Save()
        _context.SaveChanges()
    End Sub

    Public Sub Dispose() Implements IDisposable.Dispose
        _context.Dispose()
    End Sub
End Class
```

### 模式 4：生成器 (VBA)
```vb
' VBA: Builder pattern for constructing complex objects
Public Function CreateReport() As Object
    Dim report As Object
    Set report = CreateObject("Scripting.Dictionary")
    
    report.Add "Title", "Monthly Sales Report"
    report.Add "GeneratedAt", Now
    report.Add "Sections", New Collection
    
    Dim section As Object
    Set section = CreateObject("Scripting.Dictionary")
    section.Add "Name", "Revenue"
    section.Add "Data", Array(1000, 1200, 1100)
    report("Sections").Add section
    
    Set CreateReport = report
End Function
```
---

## 性能与优化
```vb
' VB.NET performance tips:

' 1. Use StringBuilder for string concatenation in loops
Dim sb As New System.Text.StringBuilder()
For i As Integer = 0 To 10000
    sb.AppendLine($"Line {i}")
Next
Dim result As String = sb.ToString()

' 2. Use generics to avoid boxing/unboxing
Dim numbers As New List(Of Integer)()  ' Value type - no boxing
Dim items As New Dictionary(Of String, User)()  ' Fast lookups

' 3. Use async/await for I/O-bound operations
Async Function FetchDataAsync() As Task(Of String)
    Using client As New HttpClient()
        Return Await client.GetStringAsync("https://api.example.com/data")
    End Using
End Function

' 4. Use Parallel for CPU-bound work
Parallel.ForEach(largeDataSet, Sub(item)
    ProcessItem(item)  ' Runs on multiple threads
End Sub)

' 5. Use Span<T> for efficient memory operations (VB 16.9+)
Dim data As Byte() = File.ReadAllBytes("large_file.bin")
Dim span As ReadOnlySpan(Of Byte) = data
Dim searchResult As Integer = span.IndexOf(CByte(42))
```

---

## 部署
### Windows 部署选项
|方法|描述 |最适合 |
|--------|-------------|----------|
| **点击一次** |通过网络/文件共享进行自我更新部署 |内部企业应用程序 |
| **MSIX** |具有全新安装/卸载功能的现代打包应用程序 | Windows 应用商店、企业 |
| **Windows 安装程序 (MSI)** |完全控制的传统安装程序 |复杂的装置 |
| **独立** |将 .NET 运行时与应用程序捆绑在一起没有 .NET 的机器 |
| **单文件发布** |一切都在一个可执行文件中 |简单分布 |
```bash
# .NET CLI build and publish commands
dotnet build MyApp.vbproj -c Release
dotnet publish MyApp.vbproj -c Release -o ./publish

# Self-contained deployment (no .NET runtime needed on target)
dotnet publish MyApp.vbproj -c Release -r win-x64 --self-contained true

# Single-file executable
dotnet publish MyApp.vbproj -c Release -r win-x64 -p:PublishSingleFile=true

# ReadyToRun compilation (faster startup)
dotnet publish MyApp.vbproj -c Release -r win-x64 -p:PublishReadyToRun=true
```

---

## 何时使用 Visual Basic
|场景|为什么选择VB |更好的选择|
|----------|--------|--------------------|
| VBA/办公自动化| Office 的标准宏语言 | Python (openpyxl)、Office 脚本 |
|旧版 VB6 维护 |现有代码库 |迁移到 C# 或 VB.NET |
|简单的Windows工具|使用 WinForms 快速构建 | C# 与 WPF 或 WinUI |
|学习编程 |非常平易近人的语法| Python（更通用）|
| .NET 新开发 |可以，但首选 C# | C# |
|跨平台应用程序 |不适合| C#、Flutter、Web 技术 |
---

## 综合问答
### Q1：VB6、VB.NET 和 VBA 有什么区别？
**答：** 每个都有不同的目的：
- **VB6**：经典 Visual Basic — 基于 COM、仅限 Windows、旧版
- **VB.NET**：现代 .NET 语言 — 在 CLR 上运行，完整的 OOP，Visual Studio 的一部分
- **VBA**：Visual Basic for Applications — 嵌入在 Microsoft Office 中
### Q2：VBA 如何自动化 Excel？
**答：** VBA 可以操作单元格、范围和工作表：
```vb
Sub FormatReport()
    Dim ws As Worksheet
    Set ws = ActiveSheet

    ws.Range("A1").Value = "Total Sales"
    ws.Range("A1").Font.Bold = True
    ws.Range("B2:B100").NumberFormat = "$#,##0.00"

    Dim total As Double
    total = Application.WorksheetFunction.Sum(ws.Range("B2:B100"))
    ws.Range("B1").Value = total
End Sub
```

### Q3：如何在 VB.NET 中创建 Windows 窗体应用程序？
**答：** 使用 Visual Studio 设计器：
```vb
Public Class MainForm
    Private Sub btnCalculate_Click(sender As Object, e As EventArgs) Handles btnCalculate.Click
        Dim num1 = CDbl(txtNum1.Text)
        Dim num2 = CDbl(txtNum2.Text)
        lblResult.Text = (num1 + num2).ToString("F2")
    End Sub
End Class
```

### Q4：VB.NET 和 C# 之间的主要区别是什么？
**答：** 它们共享相同的运行时和库。语法差异：
- VB.NET：`Dim`、`Sub`、`Function`、`If...Then...End If` 
- C#：类型优先，`{}` 块，`;` 终止符
- VB.NET 不区分大小写； C# 区分大小写
### Q5：VB.NET还值得学吗？
**答：** 为了维护现有应用程序，是的。对于新项目，首选 C#。 VBA 对于办公自动化仍然至关重要。
---

## 解决问题的思路
### 问题 1：使用 VBA 自动生成 Excel 报告
**第 1 步：了解问题**
根据原始数据生成月度销售报告。
**第 2 步：确定方法**
使用 VBA 读取数据、计算摘要和格式化输出。
**步骤 3：实施**```vb
Sub GenerateReport()
    Dim wsData As Worksheet, wsReport As Worksheet
    Set wsData = Sheets("Data")
    Set wsReport = Sheets.Add
    wsReport.Name = "Monthly Report"

    ' Headers
    wsReport.Range("A1:D1").Value = Array("Month", "Sales", "Cost", "Profit")
    wsReport.Range("A1:D1").Font.Bold = True

    ' Process data
    Dim lastRow As Long
    lastRow = wsData.Cells(wsData.Rows.Count, 1).End(xlUp).Row

    Dim i As Long, reportRow As Long
    reportRow = 2
    For i = 2 To lastRow
        wsReport.Cells(reportRow, 1).Value = wsData.Cells(i, 1).Value
        wsReport.Cells(reportRow, 2).Value = wsData.Cells(i, 2).Value
        wsReport.Cells(reportRow, 3).Value = wsData.Cells(i, 3).Value
        wsReport.Cells(reportRow, 4).Formula = "=B" & reportRow & "-C" & reportRow
        reportRow = reportRow + 1
    Next i

    wsReport.Columns.AutoFit
End Sub
```

**第 4 步：扩展**
添加图表、条件格式和电子邮件传送。
---

＃＃ 概括
Visual Basic 是一种具有重要历史意义的语言，它使数百万人能够进行编程。 VB.NET 在 .NET 生态系统中仍然发挥作用，并且 VBA 继续为全球办公自动化提供支持。然而，对于新的开发，C# 是首选的 .NET 语言。 VB 的遗产因其对语言设计的影响而得以延续——它的易用性影响了 Swift 和 Kotlin 等现代语言。