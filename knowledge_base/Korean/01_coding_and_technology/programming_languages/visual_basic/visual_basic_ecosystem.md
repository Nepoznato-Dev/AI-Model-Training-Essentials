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

# Visual Basic — 생태계 및 도구 가이드
이 가이드에서는 Visual Basic(.NET) 에코시스템의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## 비주얼 베이직 버전
| 버전 | 메모 |
|---------|---------|
| **VB.NET(비주얼 베이직 2022)** | 현재, .NET 8+ |
| **VB6** | 클래식 Visual Basic(레거시) |
| **VBA** | 응용 프로그램용 Visual Basic(Office) |
| **VB스크립트** | 스크립팅 언어(더 이상 사용되지 않음) |
```bash
dotnet new console -lang VB    # create VB project
dotnet build                    # build
dotnet run                      # run
dotnet publish -c Release       # publish
```

---

## 빌드 도구
| 도구 | 목적 |
|------|---------|
| **닷넷 CLI** | .NET 빌드, 테스트, 게시 |
| **MS빌드** | 엔진 빌드 |
| **비주얼 스튜디오** | 전체 IDE |
| **누겟** | 패키지 관리 |
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

## 웹 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **ASP.NET 코어** | 풀스택 | API, MVC, Razor 페이지 |
| **최소 API** | 경량 | 간단한 API |
| **블레이저** | 웹 UI | 컴포넌트 기반 UI |
| **시그널R** | 실시간 | 웹소켓 |
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

## 데이터베이스
| 기술 | 유형 |
|------------|------|
| **엔티티 프레임워크 코어** | 전체 ORM |
| **멋쟁이** | 마이크로ORM |
| **ADO.NET** | 낮은 수준의 데이터 액세스 |
| **OleDb** | 레거시 데이터 액세스 |
| **MySql.Data** | MySQL 커넥터 |
| **NPGSQL** | PostgreSQL 커넥터 |
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

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **x유닛** | 테스트 프레임워크 |
| **NUnit** | 테스트 프레임워크 |
| **MS테스트** | Microsoft 테스트 프레임워크 |
| **모크** | 조롱 |
| **N대체** | 조롱 |
| **FluentAssertions** | 유창한 주장 |
| **BenchmarkDotNet** | 벤치마킹 |
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

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **Roslyn 분석기** | 내장 분석 |
| **소나분석기** | SonarQube 규칙 |
| **닷넷 형식** | 코드 서식 |
| **편집기 구성** | 일관된 스타일 |
| **소나큐브** | 코드 품질 플랫폼 |
---

## 데스크탑(WinForms/WPF)
| 프레임워크 | 목적 |
|------------|---------|
| **윈폼** | 클래식 Windows 양식 |
| **WPF** | 최신 Windows UI(XAML) |
| **마우이** | 크로스 플랫폼(Xamarin의 후속 버전) |
| **아발로니아** | 크로스 플랫폼 WPF와 유사한 |
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

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **시스템.텍스트.Json** | JSON 직렬화 |
| **뉴턴소프트.Json** | JSON(레거시) |
| **세리로그** | 로깅 |
| **폴리** | 탄력성 정책 |
| **AutoMapper** | 객체 매핑 |
| **Fluent검증** | 검증 |
| **대중교통** | 메시지 버스 |
| **행파이어** | 백그라운드 작업 |
| **Spectre.콘솔** | 콘솔 UI |
---

## 사무 자동화(VBA)
| 기술 | 목적 |
|------------|---------|
| **엑셀 VBA** | 엑셀 자동화 |
| **단어 VBA** | 단어 자동화 |
| **VBA에 액세스** | 액세스 자동화 |
| **아웃룩 VBA** | 전망 자동화 |
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

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **비주얼 스튜디오** | 전체 VB.NET IDE(커뮤니티/Pro/Enterprise) |
| **VS 코드** | .NET 확장으로 경량화 |
| **VBA 편집기** | Office 앱에 내장 |
| **라이더** | JetBrains(제한된 VB 지원) |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **자체 포함** | .NET 런타임 번들 |
| **프레임워크에 따라 다름** | .NET 설치 필요 |
| **단일 파일** | `PublishSingleFile`|
| **도커** | 컨테이너화 |
| **MSI / ClickOnce** | Windows 설치 프로그램 |
| **Azure 앱 서비스** | 클라우드 호스팅 |
| **IIS** | Windows 호스팅 |
---

## 요약
Visual Basic의 생태계는 .NET의 방대한 인프라를 공유합니다. 표준 스택은 런타임으로 **.NET 8+**, IDE로 **Visual Studio**, 웹용 **ASP.NET Core**, 데이터 액세스용 **Entity Framework Core** 또는 **Dapper**, 테스트용 **xUnit**, 패키지용 **NuGet**입니다. VB.NET은 .NET 생태계에 액세스해야 하는 BASIC 구문에 익숙한 개발자에게 이상적입니다. **VBA**는 여전히 Office 자동화에 필수적입니다. 수백만 명의 비즈니스 사용자가 Excel 및 Access 매크로를 사용합니다. 에코시스템은 Windows 데스크톱 애플리케이션, Office 자동화 및 엔터프라이즈 LOB(기간 업무) 애플리케이션에 가장 적합합니다.