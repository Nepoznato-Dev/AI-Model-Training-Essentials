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
# ডেলফি / অবজেক্ট প্যাসকেল — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি ডেলফি/অবজেক্ট প্যাসকেল ইকোসিস্টেমের প্রয়োজনীয় টুল, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## ডেলফি সংস্করণ এবং কম্পাইলার
| কম্পাইলার | প্ল্যাটফর্ম | নোট |
|----------|----------|-------|
| **ডেলফি 12 এথেন্স** | ক্রস-প্ল্যাটফর্ম | সর্বশেষ Embarcadero প্রকাশ |
| **ফ্রি প্যাসকেল (FPC)** | ক্রস-প্ল্যাটফর্ম | ওপেন সোর্স প্যাসকেল কম্পাইলার |
| **লাজারস** | ক্রস-প্ল্যাটফর্ম | ফ্রি প্যাসকেল IDE (যেমন ডেলফি) |
| **ডেলফি সম্প্রদায়** | উইন্ডোজ | বিনামূল্যে সংস্করণ (সীমিত) |
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

## আইডিই
| IDE | শক্তি |
|------|------------|
| **ডেলফি আইডিই** | সম্পূর্ণ বৈশিষ্ট্যযুক্ত RAD টুল (Embarcadero) |
| **লাজারস** | বিনামূল্যে, ওপেন সোর্স (FPC) |
| **ভিএস কোড + প্যাসকেল** | লাইটওয়েট সম্পাদনা |
---

## GUI ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **ভিসিএল** | উইন্ডোজ নেটিভ | উইন্ডোজ ডেস্কটপ অ্যাপস |
| **FireMonkey (FMX)** | ক্রস-প্ল্যাটফর্ম | Windows, macOS, iOS, Android |
| **এলসিএল** | ক্রস-প্ল্যাটফর্ম | লাজারাস কম্পোনেন্ট লাইব্রেরি |
| **ডেলফিএমভিসি** | ওয়েব | MVC ফ্রেমওয়ার্ক |
| **TMS ওয়েব কোর** | ওয়েব | ডেলফি থেকে ওয়েব অ্যাপস |
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

## ডাটাবেস
| প্রযুক্তি | প্রকার |
|------------|------|
| **FireDAC** | ইউনিভার্সাল ডাটাবেস অ্যাক্সেস (Embarcadero) |
| **dbExpress** | লাইটওয়েট ডাটাবেস |
| **ADO** | ActiveX ডেটা অবজেক্ট |
| **ZeosLib** | ওপেন সোর্স ডাটাবেস উপাদান |
| **SQLite3** | অন্তর্নির্মিত SQLite সমর্থন |
| **ইন্টারবেস** | Embarcadero এর এমবেডেড DB |
| **ইন্টারসিস্টেম IRIS** | অবজেক্ট ডাটাবেস |
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

## ওয়েব ডেভেলপমেন্ট
| প্রযুক্তি | প্রকার |
|------------|------|
| **ডেলফিএমভিসি** | MVC ওয়েব ফ্রেমওয়ার্ক |
| **TMS ওয়েব কোর** | ডেলফি থেকে ওয়েব অ্যাপস |
| **ইন্ট্রাওয়েব** | ওয়েব অ্যাপ্লিকেশন |
| **মরমোট** | REST/SOA ফ্রেমওয়ার্ক |
| **ডেলফি-ওয়েবআরটিসি** | রিয়েল-টাইম যোগাযোগ |
| **ইন্ডি** | ইন্টারনেট উপাদান (HTTP, SMTP, ইত্যাদি) |
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

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **DUnit** | ইউনিট টেস্টিং (বিল্ট-ইন) |
| **DUnitX** | আধুনিক পরীক্ষার কাঠামো |
| **মকফ্যাক্টরি** | উপহাস |
| **ডেলফিমক** | উপহাস লাইব্রেরী |
| **ফাইনাল বিল্ডার** | অটোমেশন তৈরি করুন |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **ডেলফি কোড কভারেজ** | কোড কভারেজ |
| **পাসকেল বিশ্লেষক** | স্ট্যাটিক বিশ্লেষণ |
| **জি এক্সপার্ট** | IDE বিশেষজ্ঞ টুলস |
| **ডেলফিলিন্ট** | লিন্টিং |
---

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **System.SysUtils** | স্ট্রিং, তারিখ ইউটিলিটি |
| **সিস্টেম।ক্লাস** | প্রবাহ, সংগ্রহ |
| **সিস্টেম।জেনারিকস** | জেনেরিক প্রকার |
| **সিস্টেম।থ্রেডিং** | সমান্তরাল প্রোগ্রামিং |
| **ইন্ডি** | ইন্টারনেট প্রোটোকল |
| **সিনাপ্স** | নেটওয়ার্ক লাইব্রেরি |
| **Spring4D** | ইউটিলিটি লাইব্রেরি (বুস্টের মতো) |
| **DWScript** | স্ক্রিপ্টিং ইঞ্জিন |
| **JCL/JVCL** | জেডি লাইব্রেরি |
| **গ্রাফিক্স32** | গ্রাফিক্স লাইব্রেরি |
| **আলকিনো** | কম্পোনেন্ট লাইব্রেরি |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **নেটিভ উইন্ডোজ** | .exe ফাইল |
| **macOS** | FireMonkey অ্যাপস |
| **iOS / Android** | FireMonkey মোবাইল |
| **লিনাক্স** | সার্ভার-সাইড ডেলফি |
| **ডকার** | কন্টেইনারাইজড |
| **ইনো সেটআপ** | উইন্ডোজ ইনস্টলার |
| **NSIS** | উইন্ডোজ ইনস্টলার |
---

## সারাংশ
ডেলফির ইকোসিস্টেম ডেস্কটপ, মোবাইল এবং ওয়েবের জন্য দ্রুত অ্যাপ্লিকেশন ডেভেলপমেন্ট (RAD) কেন্দ্রিক। স্ট্যান্ডার্ড স্ট্যাক হল: IDE/কম্পাইলার হিসেবে **Delphi 12**, Windows ডেস্কটপের জন্য **VCL**, ক্রস-প্ল্যাটফর্মের জন্য **FireMonkey**, ডাটাবেস অ্যাক্সেসের জন্য **FireDAC**, পরীক্ষার জন্য **DUnitX** এবং ইউটিলিটিগুলির জন্য **Spring4D**। বিনামূল্যের বিকল্প হল **ফ্রি প্যাসকেল** + **লাজারাস**। উইন্ডোজ ডেস্কটপ অ্যাপ্লিকেশন, ডাটাবেস অ্যাপ্লিকেশন, এবং দ্রুত প্রোটোটাইপিং-এ ডেলফি পারদর্শী। এন্টারপ্রাইজ, স্বাস্থ্যসেবা এবং সরকারী খাতে ডেলফি অ্যাপ্লিকেশনগুলির বিশাল ইনস্টল বেস বজায় রাখার জন্য বাস্তুতন্ত্র অপরিহার্য।