---
# Metadata
title: "C# — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the C# ecosystem including toolchains, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [csharp, ecosystem, tooling, dotnet, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# C# — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái C# / .NET.
---

## .NET SDK & Chuỗi công cụ
| Công cụ | Mục đích |
|------|----------|
| **dotnet CLI** | Xây dựng, chạy, thử nghiệm, xuất bản |
| **MSBuild** | Công cụ xây dựng cơ bản |
| **NuGet CLI** | Quản lý trọn gói |
| **định dạng dotnet** | Định dạng mã |
| **dotnet-ef** | Công cụ khung thực thể |
| **dotnet đã lỗi thời** | Tìm các gói lỗi thời |
| **dotnet-script** | Chạy tập lệnh C# (.csx) |
```bash
dotnet new webapi -n MyApp       # create project
dotnet build                      # build
dotnet run                        # run
dotnet test                       # run tests
dotnet publish -c Release         # publish for deployment
dotnet add package Newtonsoft.Json  # add NuGet package
```

---

## Thời gian chạy và triển khai
| Thời gian chạy | Ghi chú |
|----------|-------|
| **.NET 9/8** | LTS / STS hiện tại, đa nền tảng |
| **.NET Framework** | Chỉ dành cho Windows, cũ (4.8.x) |
| **Đơn sắc** | .NET Framework mã nguồn mở (Xamarin) |
| **Thống nhất (IL2CPP/Mono)** | Thời gian chạy công cụ trò chơi |
| **Godot (.NET)** | Công cụ trò chơi có hỗ trợ C# |
---

## Quản lý gói
| Nguồn | Mục đích |
|--------|----------|
| **NuGet.org** | Đăng ký gói chính thức |
| **gói thêm dotnet** | Cài đặt gói CLI |
| **Tham khảo gói** | Định dạng .csproj hiện đại |
| **Nguồn cấp dữ liệu riêng tư** | Tạo tác Azure, Gói GitHub, MyGet |
```xml
<!-- .csproj (SDK-style) -->
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Dapper" Version="2.1.0" />
  </ItemGroup>
</Project>
```

---

## Khung web
| Khung | Loại | Tốt nhất cho |
|----------|------|----------|
| **Lõi ASP.NET** | Web đầy đủ | API, MVC, Blazor |
| **API tối thiểu** | Nhẹ | API đơn giản |
| **Máy chủ Blazor** | Giao diện người dùng tương tác | SPA do máy chủ kết xuất |
| **Blazor WebAssembly** | Phía khách hàng | SPA dựa trên trình duyệt |
| **gRPC** | RPC | Dịch vụ hiệu suất cao |
| **Tín hiệuR** | Thời gian thực | WebSockets, đẩy |
| **OData** | Tiện ích mở rộng REST | API có thể truy vấn |
| **Điểm cuối nhanh** | Khung API | Bản soạn sẵn nhanh, tối thiểu |
```csharp
// Minimal API example
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/hello", () => "Hello, World!");
app.MapGet("/users/{id}", async (int id, UserDb db) =>
    await db.Users.FindAsync(id) is User u ? Results.Ok(u) : Results.NotFound());

app.Run();
```

---

## Cơ sở dữ liệu & ORM
| Công nghệ | Loại |
|----------||------|
| **Lõi khung thực thể** | ORM đầy đủ, di chuyển |
| **Bảnh bao** | Micro-ORM, SQL thô |
| **NHibernate** | ORM trưởng thành |
| **FreeSql** | ORM nhẹ |
| **Marten** | Cơ sở dữ liệu tài liệu PostgreSQL |
| **StackExchange.Redis** | Khách hàng Redis |
| **MongoDB.Driver** | Máy khách MongoDB |
| **Npgsql** | Trình điều khiển PostgreSQL |
| **MySqlConnector** | Trình điều khiển MySQL |
```csharp
// EF Core example
public class AppDbContext : DbContext
{
    public DbSet<User> Users => Set<User>();
    protected override void OnConfiguring(DbContextOptionsBuilder o)
        => o.UseSqlServer("connection-string");
}

var users = await db.Users
    .Where(u => u.Age > 18)
    .OrderBy(u => u.Name)
    .ToListAsync();
```

---

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **xUnit** | Khung kiểm tra phổ biến nhất |
| **NUnit** | Khung kiểm tra cổ điển |
| **MSTest** | Khung kiểm tra của Microsoft |
| **Moq** | Thư viện mô phỏng |
| **NThay thế** | Chế giễu thân thiện |
| **Khẳng định trôi chảy** | Khẳng định trôi chảy |
| **Nên** | Khẳng định có thể đọc được |
| **Không có thật** | Tạo dữ liệu giả mạo |
| **Tự động sửa lỗi** | Tự động hóa dữ liệu thử nghiệm |
| **Vùng chứa thử nghiệm** | Kiểm tra tích hợp dựa trên Docker |
| **Điểm chuẩnDotNet** | Đo điểm chuẩn vi mô |
| **khăn phủ bàn** | Bảo hiểm mã |
```csharp
// xUnit + FluentAssertions
public class UserServiceTests
{
    [Fact]
    public async Task Should_Find_User_By_Id()
    {
        var mockRepo = Substitute.For<IUserRepository>();
        mockRepo.GetByIdAsync(1).Returns(new User("Alice"));
        var service = new UserService(mockRepo);

        var user = await service.GetByIdAsync(1);

        user.Name.Should().Be("Alice");
    }
}
```

---

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| **Máy phân tích Roslyn** | Phân tích mã tích hợp |
| **SonarAnalyzer.CSharp** | Quy tắc SonarQube |
| **StyleCop** | Thực thi phong cách mã hóa |
| **định dạng dotnet** | Định dạng mã |
| **Cấu hình biên tập** | Tính nhất quán giữa các biên tập viên |
| **SonarQube / SonarCloud** | Nền tảng chất lượng mã |
| **Sắc nét lại** | Phân tích JetBrains + tái cấu trúc |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **VisualStudio** | Windows IDE đầy đủ tính năng (Cộng đồng/Pro/Doanh nghiệp) |
| **Người lái** | JetBrains C# IDE đa nền tảng |
| **Mã VS + Bộ công cụ phát triển C#** | Nhẹ, tiện ích mở rộng của Microsoft |
| **Visual Studio cho Mac** | Đang nghỉ hưu (dùng Rider hoặc VS Code) |
---

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **System.Text.Json** | Tuần tự hóa JSON tích hợp |
| **Newtonsoft.Json** | JSON kế thừa (vẫn được sử dụng rộng rãi) |
| **Serilog** | Ghi nhật ký có cấu trúc |
| **NLog** | Khung ghi nhật ký |
| **Poly** | Chính sách về khả năng phục hồi và thử lại |
| **MediatR** | Mẫu hòa giải (CQRS) |
| **AutoMapper** | Ánh xạ đối tượng tới đối tượng |
| **Xác thực thông thạo** | Thư viện xác thực |
| **Giao thông công cộng** | Xe buýt tin nhắn (RabbitMQ, Azure SB) |
| **Hỏa hoạn** | Xử lý công việc nền |
| **Quartz.NET** | Lập kế hoạch công việc |
| **Spectre.Console** | Ứng dụng bảng điều khiển đẹp |
| **CommandLineParser** | Phân tích đối số CLI |
---

## Tích hợp đám mây và Azure
| Dịch vụ | Mục đích |
|----------|----------|
| **Hàm Azure** | Không có máy chủ |
| **Azure SDK dành cho .NET** | Tất cả dịch vụ Azure |
| **AWS SDK cho .NET** | dịch vụ AWS |
| **Google Cloud .NET** | Dịch vụ GCP |
| **Azure Cosmos DB** | Cơ sở dữ liệu NoSQL |
| **Xe buýt dịch vụ Azure** | Nhắn tin |
| **Kho khóa Azure** | Quản lý bí mật |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Tự túc** | Gói thời gian chạy .NET |
| **Phụ thuộc vào khung** | Yêu cầu cài đặt .NET |
| **Xuất bản một tệp** | `dotnet publish /p:PublishSingleFile=true`|
| **AOT bản địa** | `PublishAot=true`(không cần JIT) |
| **Docker** | `mcr.microsoft.com/dotnet/aspnet`|
| **Dịch vụ ứng dụng Azure** | Triển khai PaaS |
| **AWS Lambda** | Không có máy chủ |
| **IIS** | Lưu trữ Windows |
| **Kestrel** | Máy chủ web đa nền tảng tích hợp |
```bash
dotnet publish -c Release -r linux-x64 --self-contained
dotnet publish -c Release /p:PublishAot=true   # Native AOT
```

---

## Bản tóm tắt
C# và .NET cung cấp một trong những hệ sinh thái hiệu quả nhất. Ngăn xếp tiêu chuẩn là: **.NET 8+** làm thời gian chạy, **ASP.NET Core** cho web, **Entity Framework Core** hoặc **Dapper** để truy cập dữ liệu, **xUnit + Moq** để thử nghiệm, **Visual Studio** hoặc **Rider** cho IDE và **NuGet** cho các gói. C# hiện đại với các bản ghi, khớp mẫu, các loại tham chiếu có thể rỗng và các API tối thiểu rất ngắn gọn và mang tính biểu cảm. **Trình biên dịch AOT gốc** cho phép khởi động nhanh chóng và các tệp nhị phân nhỏ. Hệ sinh thái này vượt trội trong các lĩnh vực doanh nghiệp, đám mây (Azure), phát triển trò chơi (Unity, Godot) và các ứng dụng đa nền tảng.