---
# Metadata
title: "Delphi / Object Pascal — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Delphi ecosystem including IDEs, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [delphi, pascal, ecosystem, tooling, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Delphi / Object Pascal — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái Delphi / Object Pascal.
---

## Phiên bản và trình biên dịch Delphi
| Trình biên dịch | Nền tảng | Ghi chú |
|----------|----------|-------|
| **Delphi 12 Athens** | Đa nền tảng | Bản phát hành Embarcadero mới nhất |
| ** Pascal miễn phí (FPC)** | Đa nền tảng | Trình biên dịch Pascal mã nguồn mở |
| **Lazaro** | Đa nền tảng | IDE Pascal miễn phí (như Delphi) |
| **Cộng đồng Delphi** | Windows | Phiên bản miễn phí (có giới hạn) |
```bash
# Free Pascal
fpc -version              # check version
fpc program.pas           # compile
fpc -Mobjfpc program.pas  # Object Pascal mode

# DCC32/DCC64 (Delphi command-line)
dcc32 project.dpr         # 32-bit compile
dcc64 project.dpr         # 64-bit compile
```

---

## IDE
| IDE | Điểm mạnh |
|------|-------------|
| **Delphi IDE** | Công cụ RAD đầy đủ tính năng (Embarcadero) |
| **Lazaro** | Mã nguồn mở, miễn phí (FPC) |
| **Mã VS + Pascal** | Chỉnh sửa nhẹ |
---

## Khung GUI
| Khung | Loại | Tốt nhất cho |
|----------|------|----------|
| **VCL** | Windows gốc | Ứng dụng máy tính để bàn Windows |
| **FireMonkey (FMX)** | Đa nền tảng | Windows, macOS, iOS, Android |
| **LCL** | Đa nền tảng | Thư viện thành phần Lazarus |
| **DelphiMVC** | Web | Khung MVC |
| **Lõi web TMS** | Web | Ứng dụng web từ Delphi |
```pascal
// VCL example
procedure TForm1.Button1Click(Sender: TObject);
var
  UserName: string;
begin
  UserName := Edit1.Text;
  ShowMessage('Hello, ' + UserName + '!');
end;

// FireMonkey (cross-platform)
procedure TForm1.Button1Click(Sender: TObject);
begin
  ShowMessage('Hello from ' + TOSVersion.Platform.ToString);
end;
```

---

## Cơ sở dữ liệu
| Công nghệ | Loại |
|----------||------|
| **FireDAC** | Truy cập cơ sở dữ liệu toàn cầu (Embarcadero) |
| **dbExpress** | Cơ sở dữ liệu nhẹ |
| **ADO** | Đối tượng dữ liệu ActiveX |
| **ZeosLib** | Các thành phần cơ sở dữ liệu nguồn mở |
| **SQLite3** | Hỗ trợ SQLite tích hợp |
| **Liên cơ sở** | DB nhúng của Embarcadero |
| **IRIS hệ thống liên kết** | Cơ sở dữ liệu đối tượng |
```pascal
// FireDAC example
var
  FDConn: TFDConnection;
  FDQuery: TFDQuery;
begin
  FDConn := TFDConnection.Create(nil);
  FDConn.DriverName := 'SQLite';
  FDConn.Params.Database := 'mydb.sqlite';
  FDConn.Connected := True;

  FDQuery := TFDQuery.Create(nil);
  FDQuery.Connection := FDConn;
  FDQuery.SQL.Text := 'SELECT * FROM users WHERE age > :age';
  FDQuery.ParamByName('age').AsInteger := 18;
  FDQuery.Open;

  while not FDQuery.Eof do
  begin
    WriteLn(FDQuery.FieldByName('name').AsString);
    FDQuery.Next;
  end;
end;
```

---

## Phát triển web
| Công nghệ | Loại |
|----------||------|
| **DelphiMVC** | Khung web MVC |
| **Lõi web TMS** | Ứng dụng web từ Delphi |
| **IntraWeb** | Ứng dụng web |
| **mORMot** | Khung REST/SOA |
| **Delphi-WebRTC** | Giao tiếp thời gian thực |
| **Indy** | Các thành phần Internet (HTTP, SMTP, v.v.) |
```pascal
// DelphiMVC controller
type
  [MVCPath('/api')]
  TUserController = class(TController)
  public
    [MVCPath('/users')]
    [MVCHTTPMethods([httpGET])]
    procedure GetUsers(Ctx: THttpContextBase);

    [MVCPath('/users/($id)')]
    [MVCHTTPMethods([httpGET])]
    procedure GetUser(Ctx: THttpContextBase);
  end;

procedure TUserController.GetUsers(Ctx: THttpContextBase);
var
  Users: TObjectList<TUser>;
begin
  Users := UserService.GetAll;
  Ctx.RenderObject(Users);
end;
```

---

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **Đơn vị** | Kiểm tra đơn vị (tích hợp sẵn) |
| **DUnitX** | Khung thử nghiệm hiện đại |
| **MockFactory** | Chế giễu |
| **DelphiMock** | Thư viện mô phỏng |
| **Người xây dựng cuối cùng** | Xây dựng tự động hóa |
```pascal
// DUnitX example
uses DUnitX.TestFramework;

type
  [TestFixture]
  TUserServiceTest = class
  public
    [Test]
    procedure TestFindUser;
    [Test]
    procedure TestUserNotFound;
  end;

procedure TUserServiceTest.TestFindUser;
var
  Service: TUserService;
  User: TUser;
begin
  Service := TUserService.Create;
  try
    User := Service.Find(1);
    Assert.AreEqual('Alice', User.Name);
  finally
    Service.Free;
  end;
end;
```

---

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| **Phạm vi bảo hiểm của mã Delphi** | Bảo hiểm mã |
| **Máy phân tích Pascal** | Phân tích tĩnh |
| **GChuyên gia** | Công cụ chuyên môn IDE |
| **DelphiLint** | Lining |
---

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **System.SysUtils** | Tiện ích chuỗi, ngày tháng |
| **System.Classes** | Luồng, bộ sưu tập |
| **System.Generics** | Các loại chung |
| **System.Threading** | Lập trình song song |
| **Indy** | Giao thức Internet |
| **Khớp thần kinh** | Thư viện mạng |
| **Spring4D** | Thư viện tiện ích (như Boost) |
| **DWScript** | Công cụ viết kịch bản |
| **JCL/JVCL** | Thư viện Jedi |
| **Đồ họa32** | Thư viện đồ họa |
| **Alcinoe** | Thư viện thành phần |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Windows gốc** | tập tin .exe |
| **macOS** | Ứng dụng FireMonkey |
| **iOS / Android** | FireMonkey di động |
| **Linux** | Delphi phía máy chủ |
| **Docker** | Được đóng gói |
| **Thiết lập Inno** | Trình cài đặt Windows |
| **NSIS** | Trình cài đặt Windows |
---

## Bản tóm tắt
Hệ sinh thái của Delphi tập trung vào phát triển ứng dụng nhanh chóng (RAD) cho máy tính để bàn, thiết bị di động và web. Ngăn xếp tiêu chuẩn là: **Delphi 12** làm IDE/trình biên dịch, **VCL** cho máy tính để bàn Windows, **FireMonkey** cho đa nền tảng, **FireDAC** để truy cập cơ sở dữ liệu, **DUnitX** để thử nghiệm và **Spring4D** cho các tiện ích. Giải pháp thay thế miễn phí là **Pascal miễn phí** + **Lazarus**. Delphi vượt trội về các ứng dụng máy tính để bàn Windows, ứng dụng cơ sở dữ liệu và tạo mẫu nhanh. Hệ sinh thái này rất cần thiết để duy trì cơ sở ứng dụng Delphi được cài đặt rộng rãi trong các lĩnh vực doanh nghiệp, y tế và chính phủ.