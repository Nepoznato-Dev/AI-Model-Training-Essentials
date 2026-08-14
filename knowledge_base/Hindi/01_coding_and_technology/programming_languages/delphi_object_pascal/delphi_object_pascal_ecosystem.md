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
# डेल्फ़ी / ऑब्जेक्ट पास्कल - पारिस्थितिकी तंत्र और टूलींग गाइड
यह गाइड डेल्फ़ी/ऑब्जेक्ट पास्कल पारिस्थितिकी तंत्र में आवश्यक उपकरण, ढांचे और बुनियादी ढांचे को शामिल करता है।
---

## डेल्फ़ी संस्करण और कंपाइलर
| संकलक | प्लेटफार्म | नोट्स |
|---|-------|-------|
| **डेल्फ़ी 12 एथेंस** | क्रॉस-प्लेटफ़ॉर्म | नवीनतम एम्बरकेडेरो रिलीज |
| **निःशुल्क पास्कल (एफपीसी)** | क्रॉस-प्लेटफ़ॉर्म | ओपन-सोर्स पास्कल कंपाइलर |
| **लाजर** | क्रॉस-प्लेटफ़ॉर्म | मुफ़्त पास्कल आईडीई (डेल्फ़ी की तरह) |
| **डेल्फ़ी समुदाय** | खिड़कियाँ | निःशुल्क संस्करण (सीमित) |
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

## आईडीई
| आईडीई | ताकतें |
|----|-----|
| **डेल्फ़ी आईडीई** | पूर्ण विशेषताओं वाला आरएडी टूल (एम्बार्केडरो) |
| **लाजर** | मुफ़्त, ओपन-सोर्स (एफपीसी) |
| **वीएस कोड + पास्कल** | हल्का संपादन |
---

## जीयूआई फ्रेमवर्क
| ढाँचा | प्रकार | के लिए सर्वश्रेष्ठ |
|--------|------|-------|
| **वीसीएल** | विंडोज़ मूल | विंडोज़ डेस्कटॉप ऐप्स |
| **फायरमंकी (एफएमएक्स)** | क्रॉस-प्लेटफ़ॉर्म | विंडोज़, मैकओएस, आईओएस, एंड्रॉइड |
| **एलसीएल** | क्रॉस-प्लेटफ़ॉर्म | लाजर कंपोनेंट लाइब्रेरी |
| **डेल्फ़ीएमवीसी** | वेब | एमवीसी ढांचा |
| **टीएमएस वेब कोर** | वेब | डेल्फ़ी से वेब ऐप्स |
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

## डेटाबेस
| प्रौद्योगिकी | प्रकार |
|------|------|
| **फ़ायरडीएसी** | यूनिवर्सल डेटाबेस एक्सेस (एम्बार्केडरो) |
| **डीबीएक्सप्रेस** | हल्का डेटाबेस |
| **एडीओ** | ActiveX डेटा ऑब्जेक्ट |
| **ज़ीओसलिब** | ओपन-सोर्स डेटाबेस घटक |
| **SQLite3** | अंतर्निहित SQLite समर्थन |
| **इंटरबेस** | एम्बरकैडेरो का एम्बेडेड डीबी |
| **इंटरसिस्टम्स आईरिस** | ऑब्जेक्ट डेटाबेस |
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

## वेब विकास
| प्रौद्योगिकी | प्रकार |
|------|------|
| **डेल्फ़ीएमवीसी** | एमवीसी वेब फ्रेमवर्क |
| **टीएमएस वेब कोर** | डेल्फ़ी से वेब ऐप्स |
| **इंट्रावेब** | वेब अनुप्रयोग |
| **मोर्मोट** | रेस्ट/एसओए ढांचा |
| **डेल्फ़ी-वेबआरटीसी** | वास्तविक समय संचार |
| **इंडी** | इंटरनेट घटक (HTTP, SMTP, आदि) |
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

## परीक्षण
| ढाँचा | उद्देश्य |
|----|----|
| **डीयूनिट** | यूनिट परीक्षण (अंतर्निहित) |
| **DUnitX** | आधुनिक परीक्षण ढांचा |
| **मॉकफैक्ट्री** | उपहास |
| **डेल्फ़ीमॉक** | पुस्तकालय का उपहास |
| **फाइनलबिल्डर** | स्वचालन बनाएँ |
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

## कोड गुणवत्ता
| उपकरण | उद्देश्य |
|------|---------|
| **डेल्फ़ी कोड कवरेज** | कोड कवरेज |
| **पास्कल विश्लेषक** | स्थैतिक विश्लेषण |
| **GExperts** | आईडीई विशेषज्ञ उपकरण |
| **डेल्फ़िलिंट** | लिंटिंग |
---

## प्रमुख पुस्तकालय
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **System.SysUtils** | स्ट्रिंग, दिनांक उपयोगिताएँ |
| **सिस्टम.क्लासेस** | धाराएँ, संग्रह |
| **सिस्टम.जेनेरिक्स** | सामान्य प्रकार |
| **सिस्टम.थ्रेडिंग** | समानांतर प्रोग्रामिंग |
| **इंडी** | इंटरनेट प्रोटोकॉल |
| **सिनैप्स** | नेटवर्क लाइब्रेरी |
| **स्प्रिंग4डी** | यूटिलिटी लाइब्रेरी (जैसे बूस्ट) |
| **DWस्क्रिप्ट** | स्क्रिप्टिंग इंजन |
| **जेसीएल/जेवीसीएल** | जेडी लाइब्रेरी |
| **ग्राफिक्स32** | ग्राफ़िक्स लाइब्रेरी |
| **अलसीनो** | घटक पुस्तकालय |
---

## तैनाती
| विधि | नोट्स |
|-------|-------|
| **नेटिव विंडोज़** | .exe फ़ाइलें |
| **मैकओएस** | फायरमंकी ऐप्स |
| **आईओएस/एंड्रॉइड** | फायरमंकी मोबाइल |
| **लिनक्स** | सर्वर-साइड डेल्फ़ी |
| **डॉकर** | कंटेनरीकृत |
| **इनो सेटअप** | विंडोज़ इंस्टालर |
| **एनएसआईएस** | विंडोज़ इंस्टालर |
---

## सारांश
डेल्फ़ी का पारिस्थितिकी तंत्र डेस्कटॉप, मोबाइल और वेब के लिए तीव्र अनुप्रयोग विकास (आरएडी) पर केंद्रित है। मानक स्टैक है: आईडीई/कंपाइलर के रूप में **डेल्फ़ी 12**, विंडोज़ डेस्कटॉप के लिए **वीसीएल**, क्रॉस-प्लेटफ़ॉर्म के लिए **फ़ायरमंकी**, डेटाबेस एक्सेस के लिए **फ़ायरडीएसी**, परीक्षण के लिए **DUnitX**, और उपयोगिताओं के लिए **स्प्रिंग4डी**। मुफ़्त विकल्प **फ़्री पास्कल** + **लाज़र** है। डेल्फ़ी विंडोज़ डेस्कटॉप एप्लिकेशन, डेटाबेस एप्लिकेशन और रैपिड प्रोटोटाइपिंग में उत्कृष्ट है। उद्यम, स्वास्थ्य देखभाल और सरकारी क्षेत्रों में डेल्फ़ी अनुप्रयोगों के विशाल स्थापित आधार को बनाए रखने के लिए पारिस्थितिकी तंत्र आवश्यक है।