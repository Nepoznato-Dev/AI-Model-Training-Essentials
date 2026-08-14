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
# ڈیلفی / آبجیکٹ پاسکل - ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ ڈیلفی / آبجیکٹ پاسکل ایکو سسٹم میں ضروری ٹولز، فریم ورک اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## ڈیلفی ورژن اور مرتب کرنے والے
| مرتب کرنے والا | پلیٹ فارم | نوٹس |
|------------|---------|-------|
| **ڈیلفی 12 ایتھنز** | کراس پلیٹ فارم | تازہ ترین Embarcadero ریلیز |
| **مفت پاسکل (FPC)** | کراس پلیٹ فارم | اوپن سورس پاسکل کمپائلر |
| **لزارس** | کراس پلیٹ فارم | مفت پاسکل IDE (جیسے ڈیلفی) |
| **ڈیلفی کمیونٹی** | ونڈوز | مفت ایڈیشن (محدود) |
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

## IDEs
| IDE | طاقتیں |
|------|------------|
| **ڈیلفی IDE** | مکمل خصوصیات والا RAD ٹول (Embarcadero) |
| **لزارس** | مفت، اوپن سورس (FPC) |
| **VS کوڈ + پاسکل** | ہلکا پھلکا ترمیم |
---

## GUI فریم ورک
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **VCL** | ونڈوز مقامی | ونڈوز ڈیسک ٹاپ ایپس |
| **FireMonkey (FMX)** | کراس پلیٹ فارم | Windows, macOS, iOS, Android |
| **LCL** | کراس پلیٹ فارم | Lazarus اجزاء کی لائبریری |
| **DelphiMVC** | ویب | MVC فریم ورک |
| **TMS ویب کور** | ویب | ڈیلفی سے ویب ایپس |
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

## ڈیٹا بیس
| ٹیکنالوجی | قسم |
|------------|------|
| **FireDAC** | یونیورسل ڈیٹا بیس تک رسائی (Embarcadero) |
| **dbExpress** | ہلکا پھلکا ڈیٹا بیس |
| **ADO** | ActiveX ڈیٹا آبجیکٹ |
| **ZeosLib** | اوپن سورس ڈیٹا بیس کے اجزاء |
| **SQLite3** | بلٹ ان SQLite سپورٹ |
| **انٹربیس** | Embarcadero کی ایمبیڈڈ DB |
| **انٹر سسٹمز IRIS** | آبجیکٹ ڈیٹا بیس |
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

## ویب ڈویلپمنٹ
| ٹیکنالوجی | قسم |
|------------|------|
| **DelphiMVC** | MVC ویب فریم ورک |
| **TMS ویب کور** | ڈیلفی سے ویب ایپس |
| **انٹرا ویب** | ویب ایپلیکیشنز |
| **مور موٹ** | REST/SOA فریم ورک |
| **Delphi-WebRTC** | ریئل ٹائم مواصلات |
| **انڈی** | انٹرنیٹ کے اجزاء (HTTP, SMTP, وغیرہ) |
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

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **DUnit** | یونٹ ٹیسٹنگ (بلٹ ان) |
| **DUnitX** | جدید ٹیسٹنگ فریم ورک |
| **موک فیکٹری** | طنز |
| **ڈیلفی موک** | طنزیہ لائبریری |
| **فائنل بلڈر** | آٹومیشن بنائیں |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **ڈیلفی کوڈ کوریج** | کوڈ کوریج |
| **پاسکل تجزیہ کار** | جامد تجزیہ |
| **جی ماہرین** | IDE ماہر ٹولز |
| **ڈیلفی لِنٹ** | لنٹنگ |
---

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **System.SysUtils** | سٹرنگ، تاریخ کی افادیت |
| **سسٹم کلاسز** | سلسلے، مجموعہ |
| **System.Generics** | عام اقسام |
| **سسٹم تھریڈنگ** | متوازی پروگرامنگ |
| **انڈی** | انٹرنیٹ پروٹوکول |
| ** Synapse** | نیٹ ورک لائبریری |
| **Spring4D** | یوٹیلیٹی لائبریری (جیسے بوسٹ) |
| **DWScript** | سکرپٹ انجن |
| **JCL/JVCL** | Jedi لائبریری |
| **گرافکس32** | گرافکس لائبریری |
| **السینو** | اجزاء کی لائبریری |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **مقامی ونڈوز** | .exe فائلیں |
| **macOS** | FireMonkey ایپس |
| **iOS / Android** | FireMonkey موبائل |
| **لینکس** | سرور سائیڈ ڈیلفی |
| **ڈوکر** | کنٹینرائزڈ |
| **انو سیٹ اپ** | ونڈوز انسٹالر |
| **NSIS** | ونڈوز انسٹالر |
---

## خلاصہ
ڈیلفی کا ماحولیاتی نظام ڈیسک ٹاپ، موبائل اور ویب کے لیے تیز رفتار ایپلی کیشن ڈویلپمنٹ (RAD) پر مرکوز ہے۔ معیاری اسٹیک یہ ہے: **Delphi 12** بطور IDE/compiler، **VCL** ونڈوز ڈیسک ٹاپ کے لیے، **FireMonkey** کراس پلیٹ فارم کے لیے، **FireDAC** ڈیٹا بیس تک رسائی کے لیے، **DUnitX** ٹیسٹنگ کے لیے، اور **Spring4D** یوٹیلیٹیز کے لیے۔ مفت متبادل **فری پاسکل** + **لزارس** ہے۔ ڈیلفی ونڈوز ڈیسک ٹاپ ایپلی کیشنز، ڈیٹا بیس ایپلی کیشنز، اور تیز رفتار پروٹو ٹائپنگ میں بہترین ہے۔ انٹرپرائز، ہیلتھ کیئر، اور سرکاری شعبوں میں ڈیلفی ایپلی کیشنز کے وسیع انسٹال بیس کو برقرار رکھنے کے لیے ماحولیاتی نظام ضروری ہے۔