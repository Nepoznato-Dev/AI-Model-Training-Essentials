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
# Delphi / Object Pascal - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่สำคัญในระบบนิเวศของ Delphi / Object Pascal
---

## รุ่น Delphi และคอมไพเลอร์
| คอมไพเลอร์ | แพลตฟอร์ม | หมายเหตุ |
|----------|----------|-------|
| **เดลฟี 12 เอเธนส์** | ข้ามแพลตฟอร์ม | Embarcadero รุ่นล่าสุด |
| **ฟรีปาสคาล (FPC)** | ข้ามแพลตฟอร์ม | โอเพ่นซอร์ส Pascal คอมไพเลอร์ |
| **ลาซารัส** | ข้ามแพลตฟอร์ม | ฟรี Pascal IDE (เช่น Delphi) |
| **ชุมชนเดลฟี** | หน้าต่าง | รุ่นฟรี (จำกัด) |
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
| ไอดี | จุดแข็ง |
|-----|-----------|
| **เดลฟี IDE** | เครื่องมือ RAD ที่มีคุณสมบัติครบถ้วน (Embarcadero) |
| **ลาซารัส** | ฟรี โอเพ่นซอร์ส (FPC) |
| **VS Code + ปาสคาล** | การแก้ไขแบบน้ำหนักเบา |
---

## กรอบงาน GUI
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **วีซีแอล** | Windows ดั้งเดิม | แอพเดสก์ท็อป Windows |
| **ไฟร์มังกี้ (FMX)** | ข้ามแพลตฟอร์ม | Windows, macOS, iOS, Android |
| **แอลซีแอล** | ข้ามแพลตฟอร์ม | ไลบรารีคอมโพเนนต์ของ Lazarus |
| **DelphiMVC** | เว็บ | กรอบงาน MVC |
| **TMS เว็บคอร์** | เว็บ | เว็บแอปจาก Delphi |
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

## ฐานข้อมูล
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **FireDAC** | การเข้าถึงฐานข้อมูลสากล (Embarcadero) |
| **dbExpress** | ฐานข้อมูลน้ำหนักเบา |
| **ADO** | วัตถุข้อมูล ActiveX |
| **ZeosLib** | ส่วนประกอบฐานข้อมูลโอเพ่นซอร์ส |
| **SQLite3** | รองรับ SQLite ในตัว |
| **อินเตอร์เบส** | DB แบบฝังของ Embarcadero |
| **อินเตอร์ซิสเต็มส์ ไอริส** | ฐานข้อมูลวัตถุ |
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

## การพัฒนาเว็บ
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **DelphiMVC** | กรอบงานเว็บ MVC |
| **TMS เว็บคอร์** | เว็บแอปจาก Delphi |
| **ภายในเว็บ** | เว็บแอปพลิเคชั่น |
| **มมอท** | กรอบงาน REST/SOA |
| **Delphi-WebRTC** | การสื่อสารแบบเรียลไทม์ |
| **อินดี้** | ส่วนประกอบอินเทอร์เน็ต (HTTP, SMTP ฯลฯ ) |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **ดูยูนิต** | การทดสอบหน่วย (ในตัว) |
| **DUnitX** | กรอบการทดสอบสมัยใหม่ |
| **MockFactory** | ล้อเลียน |
| **DelphiMock** | ห้องสมุดจำลอง |
| **ตัวสร้างขั้นสุดท้าย** | สร้างระบบอัตโนมัติ |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **การครอบคลุมโค้ด Delphi** | ความครอบคลุมของโค้ด |
| **เครื่องวิเคราะห์ปาสคาล** | การวิเคราะห์แบบคงที่ |
| **GExperts** | เครื่องมือผู้เชี่ยวชาญ IDE |
| **เดลฟีลินท์** | สำลี |
---

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **System.SysUtils** | สตริง, ยูทิลิตี้วันที่ |
| **System.คลาส** | สตรีมคอลเลกชัน |
| **ระบบทั่วไป** | ประเภททั่วไป |
| **ระบบเธรด** | การเขียนโปรแกรมแบบขนาน |
| **อินดี้** | โปรโตคอลอินเทอร์เน็ต |
| **ไซแนปส์** | ไลบรารีเครือข่าย |
| **สปริงโฟร์ดี** | ไลบรารียูทิลิตี้ (เช่น Boost) |
| **DWScript** | เอ็นจิ้นการเขียนสคริปต์ |
| **เจซีแอล/เจวีซีแอล** | ห้องสมุดเจได |
| **กราฟิก32** | ไลบรารีกราฟิก |
| **อัลซิโน** | ไลบรารีส่วนประกอบ |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| ** Windows ดั้งเดิม ** | ไฟล์ .exe |
| **macOS** | แอพ FireMonkey |
| **iOS / Android** | FireMonkey มือถือ |
| **ลินุกซ์** | Delphi ฝั่งเซิร์ฟเวอร์ |
| **นักเทียบท่า** | บรรจุในตู้คอนเทนเนอร์ |
| **การตั้งค่า Inno** | ตัวติดตั้ง Windows |
| **เอ็นซิส** | ตัวติดตั้ง Windows |
---

## สรุป
ระบบนิเวศของ Delphi มุ่งเน้นไปที่การพัฒนาแอปพลิเคชันอย่างรวดเร็ว (RAD) สำหรับเดสก์ท็อป อุปกรณ์เคลื่อนที่ และเว็บ สแตกมาตรฐานคือ: **Delphi 12** เป็น IDE/คอมไพเลอร์, **VCL** สำหรับเดสก์ท็อป Windows, **FireMonkey** สำหรับข้ามแพลตฟอร์ม, **FireDAC** สำหรับการเข้าถึงฐานข้อมูล, **DUnitX** สำหรับการทดสอบ และ **Spring4D** สำหรับยูทิลิตี้ ตัวเลือกฟรีคือ **ฟรี Pascal** + **Lazarus** Delphi เป็นเลิศในด้านแอปพลิเคชันเดสก์ท็อป Windows แอปพลิเคชันฐานข้อมูล และการสร้างต้นแบบอย่างรวดเร็ว ระบบนิเวศเป็นสิ่งจำเป็นสำหรับการรักษาฐานการติดตั้งแอปพลิเคชัน Delphi จำนวนมากในองค์กร การดูแลสุขภาพ และภาครัฐ