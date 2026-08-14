---
# Metadata
title: "Delphi / Object Pascal — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Delphi ecosystem including IDEs, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Delphi / Object Pascal — 生态系统和工具指南
本指南涵盖了 Delphi/Object Pascal 生态系统中的基本工具、框架和基础设施。
---

## Delphi 版本和编译器
|编译器|平台|笔记|
|----------|----------|--------|
| **德尔福 12 雅典** |跨平台|最新 Embarcadero 版本 |
| **自由帕斯卡 (FPC)** |跨平台|开源 Pascal 编译器 |
| **拉撒路** |跨平台|免费 Pascal IDE（如 Delphi）|
| **德尔福社区** |窗户|免费版（限量）|
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
| IDE |优势 |
|-----|------------|
| **德尔福集成开发环境** |全功能 RAD 工具 (Embarcadero) |
| **拉撒路** |免费、开源 (FPC) |
| **VS Code + Pascal** |轻量级编辑 |
---

## 图形用户界面框架
|框架|类型 |最适合 |
|------------|------|----------|
| **VCL** | Windows 原生 | Windows 桌面应用程序 |
| **FireMonkey (FMX)** |跨平台| Windows、macOS、iOS、Android |
| **拼箱** |跨平台| Lazarus 组件库 |
| **DelphiMVC** |网页 | MVC框架|
| **TMS 网络核心** |网页 | Delphi 的 Web 应用程序 |
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

＃＃ 数据库
|技术 |类型 |
|------------|------|
| **FireDAC** |通用数据库访问（Embarcadero）|
| **dbExpress** |轻量级数据库 |
| **阿多** | ActiveX 数据对象 |
| **ZeosLib** |开源数据库组件|
| **SQLite3** |内置 SQLite 支持 |
| **InterBase** | Embarcadero 的嵌入式数据库 |
| **InterSystems IRIS** |对象数据库|
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

## 网页开发
|技术 |类型 |
|------------|------|
| **DelphiMVC** | MVC Web 框架 |
| **TMS 网络核心** | Delphi 的 Web 应用程序 |
| **IntraWeb** |网络应用程序|
| **mORMot** | REST/SOA 框架 |
| **Delphi-WebRTC** |实时沟通 |
| **印地** |互联网组件（HTTP、SMTP 等）|
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

## 测试
|框架|目的|
|------------|---------|
| **DUnit** |单元测试（内置）|
| **DUnitX** |现代测试框架|
| **模拟工厂** |嘲笑|
| **DelphiMock** |模拟库 |
| **最终生成器** |构建自动化|
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

## 代码质量
|工具|目的|
|------|---------|
| **Delphi 代码覆盖率** |代码覆盖率|
| **帕斯卡分析仪** |静态分析|
| **G专家** | IDE专家工具|
| **DelphiLint** |绒毛 |
---

## 关键库
|图书馆 |目的|
|---------|---------|
| **系统.SysUtils** |字符串、日期实用程序 |
| **系统类** |流、集合 |
| **系统.泛型** |通用类型 |
| **系统线程** |并行编程|
| **印地** |互联网协议|
| **突触** |网络图书馆|
| **Spring4D** |实用程序库（如Boost） |
| **DWScript** |脚本引擎|
| **JCL/JVCL** |绝地图书馆 |
| **图形32** |图形库|
| **阿尔西诺** |元件库|
---

## 部署
|方法|笔记|
|--------|--------|
| **本机 Windows** | .exe 文件 |
| **macOS** | FireMonkey 应用程序 |
| **iOS / 安卓** | FireMonkey 移动 |
| **Linux** | Delphi 服务器端 |
| **码头工人** |集装箱式|
| **创新设置** | Windows 安装程序 |
| **NSIS** | Windows 安装程序 |
---

＃＃ 概括
Delphi 的生态系统以桌面、移动和 Web 的快速应用程序开发 (RAD) 为中心。标准堆栈是：**Delphi 12** 作为 IDE/编译器、**VCL** 用于 Windows 桌面、**FireMonkey** 用于跨平台、**FireDAC** 用于数据库访问、**DUnitX** 用于测试以及 **Spring4D** 用于实用程序。免费的替代方案是**Free Pascal** + **Lazarus**。 Delphi 擅长 Windows 桌面应用程序、数据库应用程序和快速原型设计。该生态系统对于维护德尔福应用程序在企业、医疗保健和政府部门的庞大安装基础至关重要。