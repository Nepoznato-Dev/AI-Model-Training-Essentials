<!--
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

-->
# Delphi / Object Pascal — 生態系統與工具指南
本指南涵蓋了 Delphi/Object Pascal 生態系統中的基本工具、框架和基礎設施。
---

## Delphi 版本和編譯器
|編譯器|平台|筆記|
|----------|----------|--------|
| **德爾福 12 雅典** |跨平台|最新 Embarcadero 版本 |
| **自由帕斯卡 (FPC)** |跨平台|開源 Pascal 編譯器 |
| **拉撒路** |跨平台|免費 Pascal IDE（如 Delphi）|
| **德爾福社區** |窗戶|免費版（限量）|
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
| IDE |優勢 |
|-----|------------|
| **德爾福整合開發環境** |全功能 RAD 工具 (Embarcadero) |
| **拉撒路** |免費、開源 (FPC) |
| **VS Code + Pascal** |輕量級編輯 |
---

## 圖形使用者介面框架
|框架|類型 |最適合 |
|------------|------|----------|
| **VCL** | Windows 原生 | Windows 桌面應用程式 |
| **FireMonkey (FMX)** |跨平台| Windows、macOS、iOS、Android |
| **拼箱** |跨平台| Lazarus 元件庫 |
| **DelphiMVC** |網頁 | MVC框架|
| **TMS 網路核心** |網頁 | Delphi 的 Web 應用程式 |
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

## 資料庫
|技術 |類型 |
|------------|------|
| **FireDAC** |通用資料庫存取（Embarcadero）|
| **dbExpress** |輕量級資料庫 |
| **阿多** | ActiveX 資料物件 |
| **ZeosLib** |開源資料庫元件|
| **SQLite3** |內建 SQLite 支援 |
| **InterBase** | Embarcadero 的嵌入式資料庫 |
| **InterSystems IRIS** |物件資料庫|
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

## 網頁開發
|技術 |類型 |
|------------|------|
| **DelphiMVC** | MVC Web 框架 |
| **TMS 網路核心** | Delphi 的 Web 應用程式 |
| **IntraWeb** |網頁應用程式|
| **mORMot** | REST/SOA 框架 |
| **Delphi-WebRTC** |即時溝通 |
| **印地** |網際網路組件（HTTP、SMTP 等）|
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

## 測試
|框架|目的|
|------------|---------|
| **DUnit** |單元測試（內建）|
| **DUnitX** |現代測試框架|
| **模擬工廠** |嘲笑|
| **DelphiMock** |模擬庫 |
| **最終生成器** |建立自動化|
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

## 程式碼品質
|工具|目的|
|------|---------|
| **Delphi 程式碼覆蓋率** |程式碼覆蓋率|
| **帕斯卡分析儀** |靜態分析|
| **G專家** | IDE專家工具|
| **DelphiLint** |絨毛 |
---

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **系統.SysUtils** |字串、日期實用程式 |
| **系統類別** |流、集合 |
| **系統.泛型** |通用型別 |
| **系統執行緒** |並行程式設計|
| **印地** |網際網路協定|
| **突觸** |網路圖書館|
| **Spring4D** |實用程式庫（如Boost） |
| **DWScript** |腳本引擎|
| **JCL/JVCL** |絕地圖書館 |
| **圖形32** |圖形庫|
| **阿爾西諾** |元件庫|
---

## 部署
|方法|筆記|
|--------|--------|
| **本機 Windows** | .exe 檔案 |
| **macOS** | FireMonkey 應用程式 |
| **iOS / 安卓** | FireMonkey 移動 |
| **Linux** | Delphi 伺服器端 |
| **碼頭工人** |貨櫃式|
| **創新設定** | Windows 安裝程式 |
| **NSIS** | Windows 安裝程式 |
---

＃＃ 概括
Delphi 的生態系統以桌面、行動和 Web 的快速應用程式開發 (RAD) 為中心。標準堆疊是：**Delphi 12** 作為 IDE/編譯器、**VCL** 用於 Windows 桌面、**FireMonkey** 用於跨平台、**FireDAC** 用於資料庫存取、**DUnitX** 用於測試以及 **Spring4D** 用於實用程式。免費的替代方案是**Free Pascal** + **Lazarus**。 Delphi 擅長 Windows 桌面應用程式、資料庫應用程式和快速原型設計。該生態系統對於維護德爾福應用程式在企業、醫療保健和政府部門的龐大安裝基礎至關重要。