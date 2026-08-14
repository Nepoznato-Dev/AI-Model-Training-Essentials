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
# دلفي / أوبجيكت باسكال – دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والأطر والبنية التحتية الأساسية في النظام البيئي Delphi/Object Pascal.
---

## إصدارات ومجمعات دلفي
| مترجم | منصة | ملاحظات |
|----------|---------|-------|
| **دلفي 12 أثينا** | عبر منصة | أحدث إصدار من إمباركاديرو |
| ** باسكال مجاني (FPC) ** | عبر منصة | مترجم باسكال مفتوح المصدر |
| **لعازر** | عبر منصة | مجاني باسكال IDE (مثل دلفي) |
| ** مجتمع دلفي ** | ويندوز | طبعة مجانية (محدودة) |
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

## بيئة تطوير متكاملة
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **دلفي IDE** | أداة RAD كاملة المواصفات (Embarcadero) |
| **لعازر** | مجاني ومفتوح المصدر (FPC) |
| ** كود VS + باسكال ** | تحرير خفيف الوزن |
---

## أطر واجهة المستخدم الرسومية
| الإطار | اكتب | الأفضل لـ |
|-----------|------|----------|
| **في سي إل** | ويندوز الأصلي | تطبيقات سطح المكتب ويندوز |
| **فايرمونكي (FMX)** | عبر منصة | ويندوز، ماك، آي أو إس، أندرويد |
| **LCL** | عبر منصة | مكتبة مكونات لازاروس |
| **دلفيMVC** | ويب | إطار عمل MVC |
| **TMS ويب كور** | ويب | تطبيقات الويب من دلفي |
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

##قاعدة البيانات
| تكنولوجيا | اكتب |
|------------|------|
| ** فايرداك ** | الوصول إلى قاعدة البيانات العالمية (إمباركاديرو) |
| ** دي بي اكسبريس ** | قاعدة بيانات خفيفة الوزن |
| ** اللغط ** | كائنات بيانات ActiveX |
| **زيوسليب** | مكونات قاعدة البيانات مفتوحة المصدر |
| **SQLite3** | دعم SQLite المدمج |
| **إنترباس** | قاعدة بيانات Embarcadero المضمنة |
| **إنترسيستمز آيريس** | قاعدة بيانات الكائنات |
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

## تطوير الويب
| تكنولوجيا | اكتب |
|------------|------|
| **دلفيMVC** | إطار عمل الويب MVC |
| **TMS ويب كور** | تطبيقات الويب من دلفي |
| **إنتراويب** | تطبيقات الويب |
| **مورموت** | إطار عمل REST/SOA |
| **دلفي-WebRTC** | التواصل في الوقت الحقيقي |
| ** إندي ** | مكونات الإنترنت (HTTP، SMTP، إلخ) |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **الوحدة** | اختبار الوحدة (مدمج) |
| **دونيتكس** | إطار الاختبار الحديث |
| ** موك فاكتوري ** | استهزاء |
| ** دلفي موك ** | المكتبة الساخرة |
| ** فاينل بيلدر ** | بناء الأتمتة |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| ** تغطية كود دلفي ** | تغطية الكود |
| **محلل باسكال** | التحليل الساكن |
| **جي اكسبرتس** | أدوات خبراء IDE |
| **دلفي لينت** | البطانة |
---

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **System.SysUtils** | سلسلة، مرافق التاريخ |
| **System.Classes** | تيارات ومجموعات |
| **System.Generics** | أنواع عامة |
| **System.Threading** | البرمجة المتوازية |
| ** إندي ** | بروتوكولات الانترنت |
| **المشبك** | مكتبة الشبكة |
| **Spring4D** | مكتبة المرافق (مثل Boost) |
| **دوسكريبت** | محرك البرمجة النصية |
| **جكل/جفكل** | مكتبة جدي |
| **الرسومات32** | مكتبة الرسومات |
| **السينو** | مكتبة المكونات |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **النوافذ الأصلية** | ملفات .exe |
| **ماك** | تطبيقات فايرمونكي |
| **iOS/أندرويد** | فايرمونكي موبايل |
| **لينكس** | دلفي من جانب الخادم |
| ** عامل الميناء ** | في حاويات |
| ** إعداد إينو ** | مثبت ويندوز |
| **إن إس آي إس** | مثبت ويندوز |
---

## ملخص
يتركز نظام دلفي البيئي على التطوير السريع للتطبيقات (RAD) لسطح المكتب والهاتف المحمول والويب. المكدس القياسي هو: **Delphi 12** كـ IDE/مترجم، **VCL** لسطح مكتب Windows، **FireMonkey** للمنصات المشتركة، **FireDAC** للوصول إلى قاعدة البيانات، **DUnitX** للاختبار، و **Spring4D** للأدوات المساعدة. البديل المجاني هو **Free Pascal** + **Lazarus**. تتفوق دلفي في تطبيقات سطح مكتب Windows، وتطبيقات قواعد البيانات، والنماذج الأولية السريعة. يعد النظام البيئي ضروريًا للحفاظ على القاعدة الواسعة المثبتة لتطبيقات دلفي في قطاعات المؤسسات والرعاية الصحية والحكومة.