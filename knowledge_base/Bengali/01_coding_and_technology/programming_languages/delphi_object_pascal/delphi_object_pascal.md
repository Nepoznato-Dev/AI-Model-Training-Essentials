---
# Metadata
title: "Delphi / Object Pascal"
description: "Comprehensive reference for the Delphi/Object Pascal programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [delphi-object-pascal, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "44 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# ডেলফি / অবজেক্ট প্যাসকেল
ডেলফি হল প্যাসকেলের উপর ভিত্তি করে একটি অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং ভাষা, যা মূলত বোরল্যান্ড (পরে এমবারকাদেরো, এখন ইডেরা) দ্বারা তৈরি করা হয়েছিল। প্রথম 1995 সালে "ডেলফি 1" হিসাবে প্রকাশিত হয়েছিল, এটি উইন্ডোজ ডেস্কটপ অ্যাপ্লিকেশনগুলির দ্রুত অ্যাপ্লিকেশন বিকাশের (RAD) জন্য ডিজাইন করা হয়েছিল। ভাষাটি আনুষ্ঠানিকভাবে অবজেক্ট প্যাসকেল নামে পরিচিত, এবং ডেলফি আইডিই একটি ভিজ্যুয়াল ফর্ম ডিজাইনার, ইন্টিগ্রেটেড ডাটাবেস টুলস এবং একটি শক্তিশালী কম্পাইলার প্রদান করে।
1990-এর দশকের শেষের দিকে এবং 2000-এর দশকের প্রথম দিকে ডেলফি ছিল সবচেয়ে জনপ্রিয় উইন্ডোজ ডেভেলপমেন্ট টুলগুলির মধ্যে একটি। যদিও এর জনপ্রিয়তা উল্লেখযোগ্যভাবে হ্রাস পেয়েছে, এটি একটি ডেডিকেটেড ইউজার বেস বজায় রাখে, বিশেষ করে এন্টারপ্রাইজ ডেস্কটপ অ্যাপ্লিকেশন, ডাটাবেস ফ্রন্ট-এন্ড এবং লিগ্যাসি সিস্টেম রক্ষণাবেক্ষণে। আধুনিক ডেলফি (11/12) FireMonkey (FMX) ফ্রেমওয়ার্কের মাধ্যমে Windows, macOS, iOS এবং Android-এর জন্য ক্রস-প্ল্যাটফর্ম উন্নয়ন সমর্থন করে।
---

## কেন ডেলফি গুরুত্বপূর্ণ
- **দ্রুত অ্যাপ্লিকেশন ডেভেলপমেন্ট**: ভিজ্যুয়াল ফর্ম ডিজাইনার + নেটিভ কম্পাইলেশন উইন্ডোজ জিইউআই তৈরি করে অত্যন্ত দ্রুত।
- **নেটিভ পারফরম্যান্স**: সরাসরি মেশিন কোডে কম্পাইল করে — কোন রানটাইম বা VM এর প্রয়োজন নেই।
- **ডাটাবেস সংযোগ**: ঐতিহাসিকভাবে চমৎকার ডাটাবেস উপাদান (dbExpress, FireDAC, ADO)।
- **লিগেসি কোডবেস**: অনেক এন্টারপ্রাইজ অ্যাপ্লিকেশন এখনও ডেলফিতে চলে; রক্ষণাবেক্ষণ একটি বিশেষ দক্ষতা।
- **ক্রস-প্ল্যাটফর্ম (আধুনিক)**: FireMonkey ফ্রেমওয়ার্ক একটি একক কোডবেস থেকে Windows, macOS, iOS এবং Android কে লক্ষ্য করে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **পতনশীল সম্প্রদায়** | C#, Java, বা JavaScript সম্প্রদায়ের থেকে অনেক ছোট | সক্রিয় কিন্তু ছোট ফোরাম; Idera থেকে বাণিজ্যিক সহায়তা |
| **সীমিত ইকোসিস্টেম** | আধুনিক ভাষার তুলনায় তৃতীয় পক্ষের লাইব্রেরি কম | VCL/FMX কম্পোনেন্ট লাইব্রেরি ব্যবহার করুন; কাস্টম উপাদান লিখুন |
| **প্রাথমিকভাবে উইন্ডোজ-কেন্দ্রিক** | ক্রস-প্ল্যাটফর্ম সমর্থন (FMX) কম পরিপক্ক | সত্যিকারের ক্রস-প্ল্যাটফর্মের জন্য C#, ফ্লাটার বা ওয়েব প্রযুক্তি ব্যবহার করুন |
| **লাইসেন্স খরচ** | বাণিজ্যিক IDE এর জন্য একটি প্রদত্ত লাইসেন্স প্রয়োজন | ওপেন সোর্স বিকল্প: ফ্রি প্যাসকেল / লাজারাস |
| **নিয়োগ অসুবিধা** | কম ডেলফি ডেভেলপাররা বাজারে প্রবেশ করছে | বিদ্যমান সিস্টেম বজায় রাখা; আধুনিক স্ট্যাকগুলিতে নতুন বৈশিষ্ট্য স্থানান্তর করুন |
---

## সিনট্যাক্স মৌলিক
```pascal
program HelloWorld;

{$APPTYPE CONSOLE}

uses
  SysUtils;

var
  Name: string;
  Age: Integer;
  Score: Double;

// Procedure (no return value)
procedure Greet(const AName: string);
begin
  WriteLn('Hello, ' + AName + '!');
end;

// Function (returns a value)
function Add(A, B: Integer): Integer;
begin
  Result := A + B;
end;

// Object-oriented programming
type
  TAnimal = class
  private
    FName: string;
  public
    constructor Create(const AName: string);
    function Speak: string; virtual; abstract;
    property Name: string read FName;
  end;

  TDog = class(TAnimal)
  public
    function Speak: string; override;
  end;

constructor TAnimal.Create(const AName: string);
begin
  inherited Create;
  FName := AName;
end;

function TDog.Speak: string;
begin
  Result := Name + ' says woof';
end;

// Main program
begin
  Name := 'Alice';
  Age := 30;
  Score := 9.5;
  
  Greet(Name);
  WriteLn('Sum: ', Add(3, 5));
  
  ReadLn;  // Wait for Enter
end.
```

---

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### জেনেরিক এবং সংগ্রহ
ডেলফি জেনেরিক সমর্থন করে (ডেলফি 2009 সাল থেকে), টাইপ-সেফ কন্টেইনার ক্লাস সক্ষম করে।
```pascal
unit GenericsDemo;

interface

uses
  System.Generics.Collections,
  System.Generics.Defaults,
  SysUtils;

type
  // Generic pair class
  TPair<TKey, TValue> = class
  private
    FKey: TKey;
    FValue: TValue;
  public
    constructor Create(const AKey: TKey; const AValue: TValue);
    property Key: TKey read FKey;
    property Value: TValue read FValue;
  end;

  // Generic stack implementation
  TStack<T> = class
  private
    FItems: TList<T>;
  public
    constructor Create;
    destructor Destroy; override;
    procedure Push(const AItem: T);
    function Pop: T;
    function Peek: T;
    function Count: Integer;
  end;

  // Custom comparer for sorting
  TEmployeeComparer = class(TComparer<TObject>)
  public
    function Compare(const Left, Right: TObject): Integer; override;
  end;

implementation

{ TStack<T> }

constructor TStack<T>.Create;
begin
  inherited Create;
  FItems := TList<T>.Create;
end;

destructor TStack<T>.Destroy;
begin
  FItems.Free;
  inherited;
end;

procedure TStack<T>.Push(const AItem: T);
begin
  FItems.Add(AItem);
end;

function TStack<T>.Pop: T;
begin
  if FItems.Count = 0 then
    raise Exception.Create('Stack is empty');
  Result := FItems[FItems.Count - 1];
  FItems.Delete(FItems.Count - 1);
end;

function TStack<T>.Peek: T;
begin
  if FItems.Count = 0 then
    raise Exception.Create('Stack is empty');
  Result := FItems[FItems.Count - 1];
end;

function TStack<T>.Count: Integer;
begin
  Result := FItems.Count;
end;

end.
```

### বেনামী পদ্ধতি এবং বন্ধ
```pascal
program AnonymousMethods;

{$APPTYPE CONSOLE}

uses
  SysUtils, System.Generics.Collections;

type
  TIntFunction = reference to function(X: Integer): Integer;
  TVoidProc = reference to procedure(const AMsg: string);

var
  Square: TIntFunction;
  Logger: TVoidProc;
  Counter: TProc;

begin
  // Anonymous method — inline function
  Square := function(X: Integer): Integer
  begin
    Result := X * X;
  end;
  WriteLn('5 squared = ', Square(5));

  // Closure — captures outer variable
  // The Count variable persists between calls
  var Count: Integer := 0;
  Counter := procedure
  begin
    Inc(Count);
    WriteLn('Call count: ', Count);
  end;
  Counter;  // Call count: 1
  Counter;  // Call count: 2
  Counter;  // Call count: 3

  // Using anonymous methods with collections
  var Numbers := TList<Integer>.Create;
  try
    Numbers.AddRange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);

    // Filter: keep only even numbers
    var Evens := TList<Integer>.Create;
    try
      Numbers.ForEach(
        procedure(const N: Integer)
        begin
          if N mod 2 = 0 then
            Evens.Add(N);
        end
      );
      Write('Even numbers: ');
      for var N in Evens do
        Write(N, ' ');
      WriteLn;
    finally
      Evens.Free;
    end;
  finally
    Numbers.Free;
  end;

  ReadLn;
end.
```

### ইন্টারফেস এবং নির্ভরতা ইনজেকশন
```pascal
unit DIExample;

interface

uses
  SysUtils;

type
  // Interface definitions
  ILogger = interface
    ['{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}']
    procedure Log(const AMessage: string);
  end;

  IRepository = interface
    ['{B2C3D4E5-F6A7-8901-BCDE-F12345678901}']
    function FindById(const AId: Integer): string;
    procedure Save(const AData: string);
  end;

  // Concrete implementations
  TFileLogger = class(TInterfacedObject, ILogger)
  public
    procedure Log(const AMessage: string);
  end;

  TConsoleLogger = class(TInterfacedObject, ILogger)
  public
    procedure Log(const AMessage: string);
  end;

  TDatabaseRepository = class(TInterfacedObject, IRepository)
  private
    FLogger: ILogger;
  public
    constructor Create(const ALogger: ILogger);
    function FindById(const AId: Integer): string;
    procedure Save(const AData: string);
  end;

  // Service class using dependency injection
  TUserService = class
  private
    FRepository: IRepository;
    FLogger: ILogger;
  public
    constructor Create(const ARepo: IRepository; const ALogger: ILogger);
    procedure CreateUser(const AName: string);
  end;

implementation

{ TFileLogger }
procedure TFileLogger.Log(const AMessage: string);
begin
  // Write to log file
  WriteLn('[FILE LOG] ', AMessage);
end;

{ TConsoleLogger }
procedure TConsoleLogger.Log(const AMessage: string);
begin
  WriteLn('[CONSOLE] ', AMessage);
end;

{ TDatabaseRepository }
constructor TDatabaseRepository.Create(const ALogger: ILogger);
begin
  inherited Create;
  FLogger := ALogger;
end;

function TDatabaseRepository.FindById(const AId: Integer): string;
begin
  FLogger.Log('Finding record ' + IntToStr(AId));
  Result := 'Record_' + IntToStr(AId);
end;

procedure TDatabaseRepository.Save(const AData: string);
begin
  FLogger.Log('Saving: ' + AData);
end;

{ TUserService }
constructor TUserService.Create(const ARepo: IRepository; const ALogger: ILogger);
begin
  FRepository := ARepo;
  FLogger := ALogger;
end;

procedure TUserService.CreateUser(const AName: string);
begin
  FLogger.Log('Creating user: ' + AName);
  FRepository.Save(AName);
end;

end.
```

### ভিসিএল কম্পোনেন্ট প্যাটার্ন
```pascal
unit MainForm;

interface

uses
  Winapi.Windows, Winapi.Messages,
  System.SysUtils, System.Classes,
  Vcl.Graphics, Vcl.Controls, Vcl.Forms,
  Vcl.Dialogs, Vcl.StdCtrls, Vcl.ExtCtrls,
  Vcl.Grids, Vcl.DBGrids, Data.DB;

type
  TfrmMain = class(TForm)
    pnlTop: TPanel;
    btnSearch: TButton;
    btnExport: TButton;
    edtSearch: TEdit;
    dbgResults: TDBGrid;
    StatusBar: TStatusBar;
    procedure FormCreate(Sender: TObject);
    procedure btnSearchClick(Sender: TObject);
    procedure btnExportClick(Sender: TObject);
    procedure dbgResultsDblClick(Sender: TObject);
  private
    procedure SetupDataSet;
    procedure FilterData(const ASearchText: string);
    procedure ExportToCSV(const AFileName: string);
    procedure UpdateStatusBar(const AMessage: string);
  public
    { Public declarations }
  end;

var
  frmMain: TfrmMain;

implementation

{$R *.dfm}

procedure TfrmMain.FormCreate(Sender: TObject);
begin
  SetupDataSet;
  UpdateStatusBar('Ready');
end;

procedure TfrmMain.btnSearchClick(Sender: TObject);
begin
  if Trim(edtSearch.Text) = '' then
  begin
    ShowMessage('Please enter a search term');
    edtSearch.SetFocus;
    Exit;
  end;
  FilterData(edtSearch.Text);
  UpdateStatusBar('Search complete');
end;

procedure TfrmMain.btnExportClick(Sender: TObject);
begin
  ExportToCSV('export_' + FormatDateTime('yyyymmdd', Now) + '.csv');
  UpdateStatusBar('Export complete');
end;

procedure TfrmMain.dbgResultsDblClick(Sender: TObject);
begin
  ShowMessage('Selected: ' + dbgResults.Fields[1].AsString);
end;

procedure TfrmMain.SetupDataSet;
begin
  // Configure dataset and connect to DBGrid
  StatusBar.SimpleText := 'Initializing...';
end;

procedure TfrmMain.FilterData(const ASearchText: string);
begin
  // Apply filter to dataset
end;

procedure TfrmMain.ExportToCSV(const AFileName: string);
begin
  // Export DBGrid data to CSV file
end;

procedure TfrmMain.UpdateStatusBar(const AMessage: string);
begin
  StatusBar.SimpleText := AMessage;
end;

end.
```

---

## আর্কিটেকচার এবং সিস্টেম ডিজাইন
### কম্পোনেন্ট আর্কিটেকচার
ডেলফির ভিসিএল (ভিজ্যুয়াল কম্পোনেন্ট লাইব্রেরি) এবং এফএমএক্স (ফায়ারমঙ্কি) একটি উপাদান অনুক্রমের উপর নির্মিত। প্রতিটি ভিজ্যুয়াল উপাদান`TComponent`থেকে উত্তরাধিকার সূত্রে প্রাপ্ত।
```
TObject
└── TPersistent
    └── TComponent
        ├── TControl
        │   ├── TWinControl
        │   │   ├── TForm          (window/form)
        │   │   ├── TButton        (push button)
        │   │   ├── TEdit          (text input)
        │   │   ├── TPanel         (container panel)
        │   │   ├── TDBGrid        (database grid)
        │   │   └── TListBox       (list box)
        │   └── TGraphicControl
        │       ├── TLabel         (text label)
        │       ├── TImage         (image display)
        │       └── TShape         (geometric shapes)
        ├── TDataSet               (database dataset base)
        │   ├── TFDQuery           (FireDAC query)
        │   ├── TClientDataSet     (in-memory dataset)
        │   └── TADODataSet        (ADO database)
        └── TDataModule            (non-visual container)
```

### সাধারণ প্রকল্প ডিরেক্টরি কাঠামো
```
delphi-project/
├── src/
│   ├── Project.dpr              * Main project file
│   ├── MainForm.pas             * Main form unit
│   ├── MainForm.dfm             * Main form definition (binary)
│   ├── MainForm.fmx             * FMX form definition (text XML)
│   ├── DataModule.pas           * Data access module
│   ├── BusinessLogic.pas        * Business logic unit
│   └── Utils.pas                * Utility functions
├── packages/
│   ├── CustomComponents.bpl     * Component package
│   └── CustomComponents.dpk     * Package source
├── lib/                         * Compiled units
├── dcu/                         * Delphi compiled units
├── resources/
│   ├── images/                  * Application images
│   └── icons/                   * Application icons
├── Project.dproj                * Project configuration (XML)
└── README.md
```

### .dproj প্রজেক্ট ফাইল
```xml
<Project xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
    <PropertyGroup>
        <ProjectGuid>{12345678-ABCD-EF01-2345-6789ABCDEF01}</ProjectGuid>
        <MainSource>Project.dpr</MainSource>
        <Base>True</Base>
        <Config Condition="'$(Config)'==''">Debug</Config>
        <Platform>Win32</Platform>
        <AppType>Application</AppType>
        <FrameworkType>VCL</FrameworkType>
        <DCC_DCCCompiler>DCC32</DCC_DCCCompiler>
    </PropertyGroup>
    <PropertyGroup Condition="'$(Config)'=='Base'">
        <Base>true</Base>
    </PropertyGroup>
    <PropertyGroup Condition="'$(Config)'=='Debug'">
        <DCC_Optimize>false</DCC_Optimize>
        <DCC_GenerateStackFrames>true</DCC_GenerateStackFrames>
        <DCC_DebugDCUs>true</DCC_DebugDCUs>
    </PropertyGroup>
    <PropertyGroup Condition="'$(Config)'=='Release'">
        <DCC_Optimize>true</DCC_Optimize>
        <DCC_DebugInformation>0</DCC_DebugInformation>
        <DCC_LocalDebugSymbols>false</DCC_LocalDebugSymbols>
        <DCC_SymbolReferenceInfo>0</DCC_SymbolReferenceInfo>
    </PropertyGroup>
</Project>
```

---

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### কম্পাইলার নির্দেশিকা রেফারেন্স
| নির্দেশিকা | উদ্দেশ্য | উদাহরণ |
|------------|---------|---------|
| `{$APPTYPE CONSOLE}`| কনসোল অ্যাপ্লিকেশন | `{$APPTYPE CONSOLE}`|
| `{$APPTYPE GUI}`| GUI অ্যাপ্লিকেশন (ডিফল্ট) | `{$APPTYPE GUI}`|
| `{$DEFINE DEBUG}`| শর্তসাপেক্ষ প্রতীক সংজ্ঞায়িত করুন | `{$DEFINE DEBUG}`|
| `{$IFDEF symbol}`| শর্তাধীন সংকলন | `{$IFDEF DEBUG}`|
| `{$R *.dfm}`| ফর্ম রিসোর্স অন্তর্ভুক্ত করুন | `{$R *.dfm}`|
| `{$WARNINGS OFF}`| সতর্কতা দমন | `{$WARNINGS OFF}`|
| `{$HINTS OFF}`| ইঙ্গিত দমন | `{$HINTS OFF}`|
| `{$OPTIMIZATION ON}`| অপ্টিমাইজার সক্ষম করুন | `{$OPTIMIZATION ON}`|
| `{$STRINGCHECKS ON}`| স্ট্রিং পরিসীমা চেক সক্ষম করুন | `{$STRINGCHECKS ON}`|
### কমান্ড লাইন থেকে বিল্ডিং
```batch
REM 32-bit Windows build (DCC32)
dcc32 Project.dpr -NSVcl;System;Winapi -R resources -E bin\win32

REM 64-bit Windows build (DCC64)
dcc64 Project.dpr -NSVcl;System;Winapi -R resources -E bin\win64

REM Using MSBuild (modern approach)
msbuild Project.dproj /p:Config=Release /p:Platform=Win32

REM Free Pascal / Lazarus (cross-platform, open source)
fpc -Mdelphi -dLCL -Fu"lib/units" src/Project.lpr
```

### প্যাকেজ কনফিগারেশন (.dpk)
```pascal
package CustomComponents;

{$R *.res}
{$IFDEF RELEASE}
  {$OPTIMIZATION ON}
  {$DEBUG OFF}
{$ENDIF}

requires
  rtl,
  vcl;

contains
  CustomButton in 'src\CustomButton.pas',
  CustomGrid in 'src\CustomGrid.pas',
  CustomChart in 'src\CustomChart.pas';

end.
```

---

## পরীক্ষা এবং ডিবাগিং
### IDE ডিবাগার বৈশিষ্ট্য
ডেলফির আইডিইতে একটি পূর্ণ বৈশিষ্ট্যযুক্ত সমন্বিত ডিবাগার রয়েছে।
| বৈশিষ্ট্য | বর্ণনা |
|---------|---------------|
| **ব্রেকপয়েন্ট** | যেকোনো এক্সিকিউটেবল লাইনে সেট করুন; শর্তসাপেক্ষ ব্রেকপয়েন্ট সমর্থিত |
| **ওয়াচ উইন্ডো** | রিয়েল-টাইমে পরিবর্তনশীল মান পর্যবেক্ষণ করুন |
| **কল স্ট্যাক** | স্থানীয় ভেরিয়েবল সহ সম্পূর্ণ কল চেইন দেখুন |
| **CPU উইন্ডো** | সোর্স কোডের পাশাপাশি জেনারেট করা সমাবেশ দেখুন |
| **মেমরি ভিউ** | যে কোনো ঠিকানায় কাঁচা মেমরি পরিদর্শন করুন |
| **ইভেন্ট ব্রেকপয়েন্ট** | ব্যতিক্রম, DLL লোড, থ্রেড ঘটনা |
| **দূরবর্তী ডিবাগিং** | দূরবর্তী মেশিনে চলমান ডিবাগ অ্যাপ্লিকেশন |
| **ডেটা ভিজ্যুয়ালাইজেশন** | ডেটাসেট, স্ট্রিং, সংগ্রহের জন্য কাস্টম ভিজ্যুয়ালাইজার |
### DUnit টেস্টিং ফ্রেমওয়ার্ক
```pascal
unit TestBusinessLogic;

interface

uses
  TestFramework, SysUtils, BusinessLogic;

type
  TestTPriceCalculator = class(TTestCase)
  private
    FCalc: TPriceCalculator;
  public
    procedure SetUp; override;
    procedure TearDown; override;
  published
    procedure TestBasePrice;
    procedure TestDiscountCalculation;
    procedure TestTaxCalculation;
    procedure TestFinalPrice;
    procedure TestNegativePriceRaisesException;
    procedure TestZeroQuantity;
  end;

implementation

procedure TestTPriceCalculator.SetUp;
begin
  FCalc := TPriceCalculator.Create;
end;

procedure TestTPriceCalculator.TearDown;
begin
  FCalc.Free;
end;

procedure TestTPriceCalculator.TestBasePrice;
begin
  CheckEquals(100.00, FCalc.CalculateBasePrice(10, 10.00),
    'Base price should be quantity * unit price');
end;

procedure TestTPriceCalculator.TestDiscountCalculation;
begin
  CheckEquals(90.00, FCalc.ApplyDiscount(100.00, 10),
    '10% discount on 100 should be 90');
  CheckEquals(100.00, FCalc.ApplyDiscount(100.00, 0),
    '0% discount should not change price');
end;

procedure TestTPriceCalculator.TestTaxCalculation;
begin
  CheckEquals(122.00, FCalc.AddTax(100.00, 22),
    '22% tax on 100 should be 122');
end;

procedure TestTPriceCalculator.TestFinalPrice;
begin
  CheckEquals(109.80,
    FCalc.CalculateFinalPrice(10, 10.00, 10, 22),
    'Final price: 100 base, 10% discount, 22% tax');
end;

procedure TestTPriceCalculator.TestNegativePriceRaisesException;
begin
  ExpectedException := EInvalidArgument;
  FCalc.CalculateBasePrice(-1, 10.00);
end;

procedure TestTPriceCalculator.TestZeroQuantity;
begin
  CheckEquals(0.00, FCalc.CalculateBasePrice(0, 10.00),
    'Zero quantity should give zero price');
end;

initialization
  RegisterTest(TestTPriceCalculator.Suite);

end.
```

### ডিবাগিং ওয়ার্কফ্লো
```
1. Set breakpoints at suspicious code locations
2. Run the application (F9)
3. When breakpoint hits:
   a. Inspect variables in the Watch window
   b. Step through code (F7 = into, F8 = over)
   c. Check the Call Stack window for execution path
   d. Use Evaluate/Modify (Ctrl+F7) to test expressions
4. For memory issues:
   a. Enable ReportMemoryLeaksOnShutdown
   b. Use FastMM full debug mode
   c. Check for dangling pointers after Free
```

---

## ইন্টারঅপারেবিলিটি
### COM/ActiveX ইন্টিগ্রেশন
```pascal
unit COMExample;

interface

uses
  Winapi.Windows, System.Win.ComObj, ActiveX;

// Create and use a COM object
procedure UseExcelCOM;

// Implement a COM server
type
  TMyCOMObject = class(TAutoObject, IMyCOMInterface)
  protected
    function Get_Version: string; safecall;
    procedure ProcessData(const AInput: string); safecall;
  end;

implementation

uses
  ComServ;

procedure UseExcelCOM;
var
  ExcelApp: OleVariant;
  Workbook: OleVariant;
begin
  ExcelApp := CreateOleObject('Excel.Application');
  try
    ExcelApp.Visible := True;
    Workbook := ExcelApp.Workbooks.Add;
    Workbook.Sheets[1].Cells[1, 1] := 'Hello from Delphi';
    Workbook.Sheets[1].Cells[1, 2] := 42;
    Workbook.SaveAs('C:\temp\delphi_output.xlsx');
  finally
    ExcelApp.Quit;
  end;
end;

end.
```

### C/C++ DLL কল করা হচ্ছে
```pascal
unit DLLInterop;

interface

uses
  Winapi.Windows, SysUtils;

// Import functions from a C DLL
function AddNumbers(A, B: Integer): Integer; cdecl;
  external 'mathlib.dll' name 'add_numbers';

function ProcessString(Input: PAnsiChar; Output: PAnsiChar;
  MaxLen: Integer): Integer; cdecl;
  external 'stringlib.dll' name 'process_string';

// Import with dynamic loading
type
  TEncryptFunc = function(const AData: PAnsiChar;
    AKey: Integer): PAnsiChar; cdecl;

var
  EncryptData: TEncryptFunc;

procedure LoadCryptoLibrary;
procedure UnloadCryptoLibrary;

implementation

var
  CryptoLib: HMODULE;

procedure LoadCryptoLibrary;
begin
  CryptoLib := LoadLibrary('crypto.dll');
  if CryptoLib = 0 then
    raise Exception.Create('Failed to load crypto.dll');
  
  @EncryptData := GetProcAddress(CryptoLib, 'encrypt_data');
  if not Assigned(EncryptData) then
    raise Exception.Create('encrypt_data not found');
end;

procedure UnloadCryptoLibrary;
begin
  if CryptoLib <> 0 then
  begin
    FreeLibrary(CryptoLib);
    CryptoLib := 0;
  end;
end;

end.
```

### .NET ইন্টারঅপারেবিলিটি
```pascal
// Delphi Prism / Oxygene can interop with .NET assemblies
// Modern approach: use Java2OP for Android, or WinRT for Windows

// WinRT / Windows Runtime interop
uses
  Winapi.WinRT, Winapi.UI.Notifications;

procedure ShowToastNotification(const AMessage: string);
var
  ToastXML: string;
  ToastDoc: IXmlDocument;
  Toast: IToastNotification;
  Notifier: IToastNotifier;
begin
  ToastXML := '<toast><visual><binding template="ToastText01">' +
    '<text id="1">' + AMessage + '</text>' +
    '</binding></visual></toast>';
  
  ToastDoc := TXmlDocument.Create as IXmlDocument;
  ToastDoc.LoadXml(ToastXML);
  
  Toast := TToastNotification.Create(ToastDoc) as IToastNotification;
  Notifier := TToastNotificationManager.CreateToastNotifier('MyApp');
  Notifier.Show(Toast);
end;
```

---

## ডিজাইন প্যাটার্ন
### প্যাটার্ন 1: সিঙ্গেলটন (থ্রেড-সেফ)
```pascal
type
  TAppConfig = class
  private
    class var FInstance: TAppConfig;
    class var FLock: TObject;
    FSettings: TStringList;
    constructor CreatePrivate;
  public
    class function GetInstance: TAppConfig; static;
    class procedure Release; static;
    function GetSetting(const AKey: string): string;
    procedure SetSetting(const AKey, AValue: string);
  end;

class constructor TAppConfig.Create;
begin
  FLock := TObject.Create;
end;

constructor TAppConfig.CreatePrivate;
begin
  inherited Create;
  FSettings := TStringList.Create;
  FSettings.LoadFromFile('config.ini');
end;

class function TAppConfig.GetInstance: TAppConfig;
begin
  TMonitor.Enter(FLock);
  try
    if FInstance = nil then
      FInstance := TAppConfig.CreatePrivate;
    Result := FInstance;
  finally
    TMonitor.Exit(FLock);
  end;
end;
```

### প্যাটার্ন 2: পর্যবেক্ষক (ইভেন্ট-চালিত)
```pascal
type
  TDataChangeEvent = procedure(Sender: TObject; const AFieldName: string;
    const AOldValue, ANewValue: string) of object;

  TDataStore = class
  private
    FData: TDictionary<string, string>;
    FOnChange: TDataChangeEvent;
  public
    constructor Create;
    destructor Destroy; override;
    procedure SetValue(const AKey, AValue: string);
    function GetValue(const AKey: string): string;
    property OnChange: TDataChangeEvent read FOnChange write FOnChange;
  end;

procedure TDataStore.SetValue(const AKey, AValue: string);
var
  OldValue: string;
begin
  if FData.TryGetValue(AKey, OldValue) then
  begin
    if OldValue <> AValue then
    begin
      FData[AKey] := AValue;
      if Assigned(FOnChange) then
        FOnChange(Self, AKey, OldValue, AValue);
    end;
  end
  else
  begin
    FData.Add(AKey, AValue);
    if Assigned(FOnChange) then
      FOnChange(Self, AKey, '', AValue);
  end;
end;
```

### প্যাটার্ন 3: কারখানার পদ্ধতি
```pascal
type
  // Base report class
  TReport = class
  public
    procedure Generate; virtual; abstract;
    class function GetReportType: string; virtual; abstract;
  end;

  TReportClass = class of TReport;

  // Concrete reports
  TPDFReport = class(TReport)
  public
    procedure Generate; override;
    class function GetReportType: string; override;
  end;

  TCSVReport = class(TReport)
  public
    procedure Generate; override;
    class function GetReportType: string; override;
  end;

  // Factory
  TReportFactory = class
  private
    class var FRegistry: TDictionary<string, TReportClass>;
  public
    class constructor Create;
    class function CreateReport(const AType: string): TReport;
    class procedure RegisterReport(const AType: string;
      AClass: TReportClass);
  end;

class constructor TReportFactory.Create;
begin
  FRegistry := TDictionary<string, TReportClass>.Create;
  RegisterReport('PDF', TPDFReport);
  RegisterReport('CSV', TCSVReport);
end;

class function TReportFactory.CreateReport(const AType: string): TReport;
var
  ReportClass: TReportClass;
begin
  if not FRegistry.TryGetValue(AType, ReportClass) then
    raise Exception.CreateFmt('Unknown report type: %s', [AType]);
  Result := ReportClass.Create;
end;
```

---

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### মেমরি ম্যানেজমেন্ট
```pascal
// Proper memory management pattern
procedure ProcessLargeData;
var
  Buffer: TBytes;
  Stream: TMemoryStream;
begin
  // Use TBytes (managed array) — automatically freed
  SetLength(Buffer, 1024 * 1024);  // 1MB
  try
    // Process buffer...
    FillChar(Buffer[0], Length(Buffer), 0);
  finally
    // Buffer is automatically freed when it goes out of scope
  end;

  // Use try-finally for unmanaged objects
  Stream := TMemoryStream.Create;
  try
    Stream.WriteBuffer(Buffer[0], Length(Buffer));
    Stream.SaveToFile('output.bin');
  finally
    Stream.Free;  // Always free in finally block
  end;
end;

// Use interfaces for automatic reference counting
procedure ProcessWithInterfaces;
var
  Processor: IDataProcessor;
begin
  Processor := TDataProcessor.Create;
  // No Free needed — reference counting handles cleanup
  Processor.Execute;
end;
```

### VCL/FMX অপ্টিমাইজেশান টিপস
| টেকনিক | প্রভাব | বর্ণনা |
|------------|---------|---------------|
| **বিগিনআপডেট/শেষ আপডেট** | উচ্চ | পুনরায় রং রোধ করতে তালিকা/গ্রিড আপডেট মোড়ানো |
| **ডাবল বাফারিং** | মাঝারি | ফ্লিকার কমাতে`DoubleBuffered := True`সেট করুন |
| **ভার্চুয়াল তালিকা** | উচ্চ | বড় ডেটাসেটের জন্য`TVirtualStringTree`ব্যবহার করুন |
| **স্ট্রিং ইন্টারিং** | মাঝারি | স্ট্রিং ধ্রুবক পুনরায় ব্যবহার করুন; বারবার সংমিশ্রণ এড়িয়ে চলুন |
| **অবজেক্ট পুলিং** | মাঝারি | ঘন ঘন তৈরি/ধ্বংস করা বস্তু পুনঃব্যবহার করুন
| **অলস লোডিং** | উচ্চ | শুধুমাত্র প্রয়োজন হলেই ডেটা/ফর্ম লোড করুন
| **কম্পাইলার অপ্টিমাইজেশান** | মাঝারি | রিলিজ বিল্ডের জন্য`{$O+}`সক্ষম করুন |
---

## স্থাপনা এবং বাস্তব-বিশ্ব ব্যবহার
### স্থাপনার বিকল্প
```
Delphi Deployment Targets:
├── Windows (VCL/FMX)
│   ├── Standalone .exe (no dependencies)
│   ├── Installer (Inno Setup, InstallShield)
│   └── MSIX / Windows Store package
├── macOS (FMX)
│   └── .app bundle
├── iOS (FMX)
│   └── IPA via Xcode toolchain
├── Android (FMX)
│   └── APK/AAB via Android SDK
└── Linux (FPC/Lazarus only)
    └── ELF binary
```

### বাস্তব-বিশ্ব ব্যবহারের ক্ষেত্রে
| শিল্প | আবেদন | কেন ডেলফি |
|------------|-------------|------------|
| **অর্থ** | ট্রেডিং প্ল্যাটফর্ম, ব্যাংকিং ড্যাশবোর্ড | দ্রুত নেটিভ GUI, ডাটাবেস সংযোগ |
| **স্বাস্থ্যসেবা** | মেডিকেল ইমেজিং, রোগী ব্যবস্থাপনা | ভিসিএল উপাদান, নেটিভ কর্মক্ষমতা |
| **উৎপাদন** | SCADA সিস্টেম, শিল্প নিয়ন্ত্রণ | সরাসরি হার্ডওয়্যার অ্যাক্সেস, রিয়েল-টাইম প্রতিক্রিয়া |
| **সরকার** | অভ্যন্তরীণ প্রশাসনিক সরঞ্জাম | উত্তরাধিকার সিস্টেম ধারাবাহিকতা |
| **টেলিকম** | নেটওয়ার্ক মনিটরিং ড্যাশবোর্ড | দ্রুত ডেটা ভিজ্যুয়ালাইজেশন |
| **শিক্ষা** | শিক্ষামূলক সফটওয়্যার, ই-লার্নিং টুলস | দ্রুত উন্নয়ন, মাল্টিমিডিয়া সমর্থন |
---

## কখন ডেলফি ব্যবহার করবেন
| দৃশ্যকল্প | কেন ডেলফি | ভাল বিকল্প |
|------------|------------|---------|
| উত্তরাধিকার ডেলফি রক্ষণাবেক্ষণ | বিদ্যমান কোডবেস | — |
| উইন্ডোজ ডেস্কটপ অ্যাপস (দ্রুত) | ভিসিএল পরিপক্ক এবং দ্রুত | C# (WPF/WinForms) |
| ডাটাবেস ফ্রন্ট-এন্ডস | চমৎকার তথ্য উপাদান | C#, জাভা |
| ক্রস-প্ল্যাটফর্ম ডেস্কটপ (কুলুঙ্গি) | FireMonkey বিদ্যমান | C#, ফ্লটার, ইলেক্ট্রন |
| নতুন Windows GUI ডেভেলপমেন্ট | সম্ভব কিন্তু সম্প্রদায় সঙ্কুচিত হচ্ছে | C# (WPF/WinUI 3) |
| ওয়েব ডেভেলপমেন্ট | উপযুক্ত নয় | জাভাস্ক্রিপ্ট, পাইথন, সি# |
| মোবাইল অ্যাপস | FMX এর মাধ্যমে সম্ভব কিন্তু সীমিত | সুইফট, কোটলিন, ফ্লাটার |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: ডেলফির ভিসিএল ফ্রেমওয়ার্ক কীভাবে কাজ করে?
**A:** ভিসিএল উইন্ডোজ এপিআই নিয়ন্ত্রণগুলিকে অবজেক্ট-ওরিয়েন্টেড হায়ারার্কিতে মোড়ানো করে। ফর্ম, বোতাম, এবং গ্রিড সব ক্লাস:
```pascal
type
  TMainForm = class(TForm)
    Button1: TButton;
    Memo1: TMemo;
    procedure Button1Click(Sender: TObject);
  end;

procedure TMainForm.Button1Click(Sender: TObject);
begin
  Memo1.Lines.Add('Button clicked!');
end;
```

### প্রশ্ন 2: আমি কীভাবে ডেলফিতে উপাদান তৈরি করব?
**A:** TCcomponent বা TCcontrol থেকে উত্তরাধিকারী:
```pascal
type
  TMyComponent = class(TComponent)
  private
    FValue: Integer;
  protected
    procedure Notification(AComponent: TComponent; Operation: TOperation); override;
  published
    property Value: Integer read FValue write FValue default 0;
  end;
```

### প্রশ্ন 3: ডেলফি এবং ফ্রি প্যাসকেলের মধ্যে পার্থক্য কী?
**A:** Delphi হল Embarcadero দ্বারা একটি বাণিজ্যিক IDE/কম্পাইলার। ফ্রি প্যাসকেল হল ওপেন সোর্স কম্পাইলার এবং লাজারাস হল ফ্রি IDE। উভয়ই অবজেক্ট প্যাসকেল সিনট্যাক্স ব্যবহার করে।
### প্রশ্ন 4: আমি কিভাবে ডেলফিতে ডাটাবেস নিয়ে কাজ করব?
**A:** FireDAC বা dbExpress উপাদান ব্যবহার করুন:
```pascal
FDConnection1.ConnectionString := 'DriverID=SQLite;Database=mydb.db';
FDConnection1.Open;
FDQuery1.SQL.Text := 'SELECT * FROM users';
FDQuery1.Open;
while not FDQuery1.Eof do
begin
  Memo1.Lines.Add(FDQuery1.FieldByName('name').AsString);
  FDQuery1.Next;
end;
```

### প্রশ্ন 5: ডেলফি কি আজও প্রাসঙ্গিক?
**A:** লিগ্যাসি উইন্ডোজ অ্যাপ্লিকেশন বজায় রাখার জন্য, হ্যাঁ। নতুন প্রকল্পের জন্য, বেশিরভাগ বিকাশকারীরা C# বা ওয়েব প্রযুক্তি পছন্দ করে। বিনামূল্যে প্যাসকেল/লাজারস একটি বিনামূল্যে ক্রস-প্ল্যাটফর্ম বিকল্প প্রদান করে।
---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি ডেটা-সচেতন ফর্ম তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি ফর্ম তৈরি করুন যা ডাটাবেস রেকর্ড প্রদর্শন এবং সম্পাদনা করে।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
ডেটাসেটের সাথে আবদ্ধ ডেটা-সচেতন উপাদানগুলি ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```pascal
procedure TMainForm.FormCreate(Sender: TObject);
begin
  FDConnection1.Open;
  FDQuery1.Open;
  DataSource1.DataSet := FDQuery1;
  DBGrid1.DataSource := DataSource1;
  DBNavigator1.DataSource := DataSource1;
end;

procedure TMainForm.btnSaveClick(Sender: TObject);
begin
  FDQuery1.Post;
  ShowMessage('Record saved');
end;
```

**ধাপ 4: প্রসারিত করুন**
বৈধতা, ত্রুটি পরিচালনা, এবং অনুসন্ধান/ফিল্টার কার্যকারিতা যোগ করুন।
---

## সারাংশ
ডেলফি একটি ঐতিহাসিকভাবে গুরুত্বপূর্ণ ভাষা যা উইন্ডোজের জন্য দ্রুত অ্যাপ্লিকেশন বিকাশের পথপ্রদর্শক। আধুনিক ডেলফি নেটিভ উইন্ডোজ অ্যাপ্লিকেশন এবং ডাটাবেস ফ্রন্ট-এন্ডের জন্য সক্ষম, তবে এর সম্প্রদায় এবং বাস্তুতন্ত্র যথেষ্ট সঙ্কুচিত হয়েছে। বিদ্যমান ডেলফি কোডবেসগুলি বজায় রাখার জন্য, এটি অপরিহার্য। নতুন প্রকল্পগুলির জন্য, বেশিরভাগ বিকাশকারীরা C#, ওয়েব প্রযুক্তি বা ক্রস-প্ল্যাটফর্ম ফ্রেমওয়ার্কগুলিতে স্থানান্তরিত হয়েছে। ওপেন সোর্স ফ্রি প্যাসকেল/লাজারাস প্রকল্প অবজেক্ট প্যাসকেল ভাষায় আগ্রহীদের জন্য একটি বিনামূল্যের বিকল্প প্রদান করে।