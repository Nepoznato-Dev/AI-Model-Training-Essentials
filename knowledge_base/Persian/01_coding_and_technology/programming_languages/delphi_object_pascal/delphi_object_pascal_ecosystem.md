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

# Delphi / Object Pascal - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم دلفی/ابجکت پاسکال را پوشش می‌دهد.
---

## نسخه ها و کامپایلرهای دلفی
| کامپایلر | پلت فرم | یادداشت ها |
|----------|----------|-------|
| **دلفی 12 آتن** | کراس پلتفرم | آخرین نسخه Embarcadero |
| **پاسکال رایگان (FPC)** | کراس پلتفرم | کامپایلر پاسکال منبع باز |
| **لازاروس** | کراس پلتفرم | رایگان پاسکال IDE (مانند دلفی) |
| **جامعه دلفی** | ویندوز | نسخه رایگان (محدود) |
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
| IDE | نقاط قوت |
|-----|-----------|
| **دلفی IDE** | ابزار RAD با امکانات کامل (Embarcadero) |
| **لازاروس** | رایگان، منبع باز (FPC) |
| ** کد VS + پاسکال** | ویرایش سبک |
---

## چارچوب های رابط کاربری گرافیکی
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **VCL** | ویندوز بومی | برنامه های دسکتاپ ویندوز |
| **FireMonkey (FMX)** | کراس پلتفرم | ویندوز، macOS، iOS، اندروید |
| **LCL** | کراس پلتفرم | کتابخانه مؤلفه لازاروس |
| **DelphiMVC** | وب | چارچوب MVC |
| **TMS Web Core** | وب | برنامه های وب از دلفی |
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

## پایگاه داده
| فناوری | نوع |
|------------|------|
| **FireDAC** | دسترسی به پایگاه داده جهانی (Embarcadero) |
| **dbExpress** | پایگاه داده سبک |
| **ADO** | ActiveX Data Objects |
| **ZeosLib** | اجزای پایگاه داده منبع باز |
| **SQLite3** | پشتیبانی داخلی SQLite |
| **اینتربیس** | Embarcadero's Embedded DB |
| **InterSystems IRIS** | پایگاه داده شی |
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

## توسعه وب
| فناوری | نوع |
|------------|------|
| **DelphiMVC** | چارچوب وب MVC |
| **TMS Web Core** | برنامه های وب از دلفی |
| **اینتروب** | برنامه های کاربردی وب |
| **mORMot** | چارچوب REST/SOA |
| **Delphi-WebRTC** | ارتباط بلادرنگ |
| **ایندی** | اجزای اینترنت (HTTP، SMTP و غیره) |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **DUnit** | تست واحد (توکار) |
| **DUnitX** | چارچوب تست مدرن |
| **MockFactory** | تمسخر |
| **DelphiMock** | کتابخانه تمسخر آمیز |
| **FinalBuilder** | اتوماسیون ساخت |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **پوشش کد دلفی** | پوشش کد |
| **آنالایزر پاسکال** | تجزیه و تحلیل استاتیک |
| **GEexperts** | ابزار تخصصی IDE |
| **DelphiLint** | پرز زدن |
---

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **System.SysUtils** | ابزارهای رشته، تاریخ |
| **سیستم.کلاس** | جریان ها، مجموعه ها |
| **سیستم.جنریک** | انواع ژنریک |
| **System.Threading** | برنامه نویسی موازی |
| **ایندی** | پروتکل های اینترنت |
| **سیناپس** | کتابخانه شبکه |
| **Spring4D** | کتابخانه ابزار (مانند Boost) |
| **DWScript** | موتور اسکریپت |
| **JCL/JVCL** | کتابخانه جدی |
| **Graphics32** | کتابخانه گرافیک |
| **Alcinoe** | کتابخانه کامپوننت |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **ویندوز بومی** | فایل های exe |
| **macOS** | برنامه های FireMonkey |
| **iOS / Android** | موبایل FireMonkey |
| **لینوکس** | دلفی سمت سرور |
| **داکر** | کانتینری |
| ** راه اندازی Inno ** | نصب کننده ویندوز |
| **NSIS** | نصب کننده ویندوز |
---

## خلاصه
اکوسیستم دلفی بر توسعه سریع اپلیکیشن (RAD) برای دسکتاپ، موبایل و وب متمرکز است. پشته استاندارد عبارتند از: **Delphi 12** به عنوان IDE/کامپایلر، **VCL** برای دسکتاپ ویندوز، **FireMonkey** برای کراس پلتفرم، **FireDAC** برای دسترسی به پایگاه داده، **DUnitX** برای آزمایش، و **Spring4D** برای ابزارهای کاربردی. جایگزین رایگان **پاسکال رایگان** + **لازاروس** است. دلفی در برنامه های دسکتاپ ویندوز، برنامه های کاربردی پایگاه داده و نمونه سازی سریع سرآمد است. اکوسیستم برای حفظ پایگاه نصب شده گسترده برنامه های کاربردی دلفی در بخش های سازمانی، مراقبت های بهداشتی و دولتی ضروری است.