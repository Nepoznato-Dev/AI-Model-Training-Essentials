<!--
---
# Metadata
title: "Delphi / Object Pascal"
description: "Comprehensive reference for the Delphi/Object Pascal programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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

-->
# ڈیلفی / آبجیکٹ پاسکل
ڈیلفی پاسکل پر مبنی ایک آبجیکٹ پر مبنی پروگرامنگ زبان ہے، جو اصل میں بورلینڈ (بعد میں ایمبارکیڈرو، اب آئیڈیرا) نے تیار کی تھی۔ پہلی بار 1995 میں "Delphi 1" کے نام سے جاری کیا گیا، اسے ونڈوز ڈیسک ٹاپ ایپلی کیشنز کی تیز رفتار ایپلی کیشن ڈویلپمنٹ (RAD) کے لیے ڈیزائن کیا گیا تھا۔ زبان کو رسمی طور پر آبجیکٹ پاسکل کے نام سے جانا جاتا ہے، اور Delphi IDE ایک بصری شکل ڈیزائنر، مربوط ڈیٹا بیس ٹولز، اور ایک طاقتور مرتب فراہم کرتا ہے۔
ڈیلفی 1990 کی دہائی کے آخر اور 2000 کی دہائی کے اوائل میں ونڈوز کے سب سے مشہور ڈویلپمنٹ ٹولز میں سے ایک تھا۔ اگرچہ اس کی مقبولیت میں نمایاں کمی آئی ہے، یہ ایک وقف صارف بنیاد کو برقرار رکھتا ہے، خاص طور پر انٹرپرائز ڈیسک ٹاپ ایپلی کیشنز، ڈیٹا بیس فرنٹ اینڈز، اور لیگیسی سسٹم مینٹیننس میں۔ Modern Delphi (11/12) FireMonkey (FMX) فریم ورک کے ذریعے Windows، macOS، iOS، اور Android کے لیے کراس پلیٹ فارم کی ترقی کی حمایت کرتا ہے۔
---

## ڈیلفی کیوں اہمیت رکھتی ہے۔
- **تیز رفتار ایپلی کیشن ڈویلپمنٹ**: بصری فارم ڈیزائنر + مقامی تالیف نے ونڈوز GUI کو انتہائی تیز بنایا۔
- **مقامی کارکردگی**: براہ راست مشین کوڈ پر مرتب کرتا ہے — رن ٹائم یا VM کی ضرورت نہیں ہے۔
- **ڈیٹا بیس کنیکٹیویٹی**: تاریخی طور پر بہترین ڈیٹا بیس اجزاء (dbExpress، FireDAC، ADO)۔
- **لیگیسی کوڈ بیسز**: بہت سی انٹرپرائز ایپلی کیشنز اب بھی ڈیلفی پر چلتی ہیں۔ دیکھ بھال ایک خاص مہارت ہے.
- **کراس پلیٹ فارم (جدید)**: فائر مانکی فریم ورک ونڈوز، میک او ایس، آئی او ایس اور اینڈرائیڈ کو ایک کوڈ بیس سے نشانہ بناتا ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **کمیونٹی ** | C#، Java، یا JavaScript کمیونٹیز سے بہت چھوٹا | فعال لیکن چھوٹے فورمز؛ Idera کی طرف سے تجارتی تعاون |
| **محدود ماحولیاتی نظام** | جدید زبانوں سے کم تھرڈ پارٹی لائبریریاں | VCL/FMX جزو لائبریری کا استعمال کریں؛ اپنی مرضی کے اجزاء لکھیں |
| **بنیادی طور پر ونڈوز پر مرکوز** | کراس پلیٹ فارم سپورٹ (FMX) کم بالغ ہے | حقیقی کراس پلیٹ فارم کے لیے C#، فلٹر، یا ویب ٹیکنالوجیز استعمال کریں۔
| **لائسنسنگ لاگت** | کمرشل IDE کے لیے ایک ادا شدہ لائسنس کی ضرورت ہے | اوپن سورس متبادل: مفت پاسکل / لازارس |
| ** ملازمت میں دشواری** | کم ڈیلفی ڈویلپرز مارکیٹ میں داخل ہو رہے ہیں | موجودہ نظام کو برقرار رکھنا؛ نئی خصوصیات کو جدید اسٹیک میں منتقل کریں |
---

## نحوی بنیادی باتیں
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

## اعلی درجے کی نحو اور نمونے۔
### عام اور مجموعہ
ڈیلفی جنرکس کو سپورٹ کرتا ہے (ڈیلفی 2009 سے)، ٹائپ سیف کنٹینر کلاسز کو فعال کرتا ہے۔
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

### گمنام طریقے اور بندشیں۔
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

### انٹرفیس اور انحصار انجیکشن
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

### VCL اجزاء کے پیٹرن
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

## آرکیٹیکچر اور سسٹم ڈیزائن
### جزو فن تعمیر
Delphi's VCL (visual Component Library) اور FMX (FireMonkey) ایک جزو کے درجہ بندی پر بنائے گئے ہیں۔ ہر بصری عنصر`TComponent`سے وراثت میں ملتا ہے۔
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

### عام پروجیکٹ ڈائرکٹری کا ڈھانچہ
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

### .dproj پروجیکٹ فائل
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### مرتب کرنے والے ہدایات کا حوالہ
| ہدایت | مقصد | مثال |
|------------|---------|---------|
| `{$APPTYPE CONSOLE}`| کنسول ایپلی کیشن | `{$APPTYPE CONSOLE}`|
| `{$APPTYPE GUI}`| GUI ایپلیکیشن (پہلے سے طے شدہ) | `{$APPTYPE GUI}`|
| `{$DEFINE DEBUG}`| مشروط علامت کی وضاحت کریں | `{$DEFINE DEBUG}`|
| `{$IFDEF symbol}`| مشروط تالیف | `{$IFDEF DEBUG}`|
| `{$R *.dfm}`| فارم کا وسیلہ شامل کریں | `{$R *.dfm}`|
| `{$WARNINGS OFF}`| انتباہات کو دبائیں | `{$WARNINGS OFF}`|
| `{$HINTS OFF}`| اشارے کو دبائیں | `{$HINTS OFF}`|
| `{$OPTIMIZATION ON}`| آپٹیمائزر کو فعال کریں | `{$OPTIMIZATION ON}`|
| `{$STRINGCHECKS ON}`| سٹرنگ رینج چیکز کو فعال کریں | `{$STRINGCHECKS ON}`|
### کمانڈ لائن سے عمارت
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

### پیکیج کنفیگریشن (.dpk)
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

## ٹیسٹنگ اور ڈیبگنگ
### IDE ڈیبگر کی خصوصیات
Delphi's IDE میں ایک مکمل خصوصیات والا مربوط ڈیبگر شامل ہے۔
| خصوصیت | تفصیل |
|---------|---------------|
| **بریک پوائنٹس** | کسی بھی قابل عمل لائن پر سیٹ کریں؛ مشروط بریک پوائنٹس کی حمایت کی |
| **واچ ونڈو** | ریئل ٹائم میں متغیر اقدار کی نگرانی کریں |
| **کال اسٹیک** | مقامی متغیرات کے ساتھ مکمل کال چین دیکھیں |
| **CPU ونڈو** | ماخذ کوڈ کے ساتھ تیار کردہ اسمبلی دیکھیں |
| **میموری ویو** | کسی بھی پتے پر خام میموری کا معائنہ کریں |
| **ایونٹ بریک پوائنٹس** | مستثنیات پر وقفہ، DLL بوجھ، دھاگے کے واقعات |
| **ریموٹ ڈیبگنگ** | ریموٹ مشینوں پر چلنے والی ڈیبگ ایپلی کیشنز |
| **ڈیٹا ویژولائزیشن** | ڈیٹاسیٹس، سٹرنگز، مجموعوں کے لیے حسب ضرورت ویژولائزر |
### DUnit ٹیسٹنگ فریم ورک
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

### ڈیبگنگ ورک فلو
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

## انٹرآپریبلٹی
### COM/ActiveX انٹیگریشن
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

### C/C++ DLLs کو کال کرنا
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

### .NET انٹرآپریبلٹی
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

## ڈیزائن پیٹرن
### پیٹرن 1: سنگلٹن (تھریڈ سے محفوظ)
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

### پیٹرن 2: مبصر (واقعہ سے چلنے والا)
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

### پیٹرن 3: فیکٹری کا طریقہ
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

## کارکردگی اور اصلاح
### میموری کا انتظام
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

### VCL/FMX آپٹیمائزیشن ٹپس
| تکنیک | اثر | تفصیل |
|------------|---------|------------|
| **Begin Update/End Update** | ہائی | دوبارہ پینٹ کو روکنے کے لیے لپیٹ فہرست/گرڈ اپ ڈیٹس |
| **ڈبل بفرنگ** | میڈیم | ٹمٹماہٹ کو کم کرنے کے لیے`DoubleBuffered := True`سیٹ کریں |
| **ورچوئل فہرستیں** | ہائی | بڑے ڈیٹا سیٹس کے لیے`TVirtualStringTree`استعمال کریں۔
| **سٹرنگ انٹرنگ** | میڈیم | سٹرنگ کنسٹینٹس کو دوبارہ استعمال کریں؛ بار بار جوڑنے سے گریز کریں |
| **آبجیکٹ پولنگ** | میڈیم | کثرت سے تخلیق شدہ / تباہ شدہ اشیاء کو دوبارہ استعمال کریں |
| **سست لوڈنگ** | ہائی | صرف ضرورت پڑنے پر ڈیٹا/فارم لوڈ کریں۔
| **کمپائلر کی اصلاح** | میڈیم | ریلیز کی تعمیر کے لیے`{$O+}`کو فعال کریں |
---

## تعیناتی اور حقیقی دنیا کا استعمال
### تعیناتی کے اختیارات
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

### حقیقی دنیا کے استعمال کے کیسز
| صنعت | درخواست | ڈیلفی کیوں |
|------------|------------|------------|
| **فنانس** | تجارتی پلیٹ فارمز، بینکنگ ڈیش بورڈز | تیز مقامی GUI، ڈیٹا بیس کنیکٹیویٹی |
| **صحت کی دیکھ بھال** | میڈیکل امیجنگ، مریض کا انتظام | VCL اجزاء، مقامی کارکردگی |
| **مینوفیکچرنگ** | SCADA نظام، صنعتی کنٹرول | براہ راست ہارڈ ویئر تک رسائی، اصل وقت کا جواب |
| **حکومت** | داخلی انتظامی اوزار | میراثی نظام کا تسلسل |
| **ٹیلی کام** | نیٹ ورک مانیٹرنگ ڈیش بورڈز | فاسٹ ڈیٹا ویژولائزیشن |
| **تعلیم** | تعلیمی سافٹ ویئر، ای لرننگ ٹولز | تیز رفتار ترقی، ملٹی میڈیا سپورٹ |
---

## ڈیلفی کب استعمال کریں۔
| منظر نامہ | ڈیلفی کیوں | بہتر متبادل |
|------------|------------|-------------------|
| میراثی ڈیلفی کی دیکھ بھال | موجودہ کوڈبیس | - |
| ونڈوز ڈیسک ٹاپ ایپس (تیز رفتار) | VCL بالغ اور تیز ہے | C# (WPF/WinForms) |
| ڈیٹا بیس فرنٹ اینڈز | بہترین ڈیٹا اجزاء | C#، Java |
| کراس پلیٹ فارم ڈیسک ٹاپ (طاق) | FireMonkey موجود ہے | C#، لہرانا، الیکٹران |
| نئی ونڈوز GUI ترقی | ممکن ہے لیکن کمیونٹی سکڑ رہی ہے | C# (WPF/WinUI 3) |
| ویب ڈویلپمنٹ | مناسب نہیں | JavaScript, Python, C# |
| موبائل ایپس | FMX کے ذریعے ممکن لیکن محدود | سوئفٹ، کوٹلن، پھڑپھڑانا |
---

## مصنوعی سوال و جواب
### Q1: Delphi کا VCL فریم ورک کیسے کام کرتا ہے؟
**A:** VCL ونڈوز API کنٹرولز کو آبجیکٹ پر مبنی درجہ بندی میں لپیٹتا ہے۔ فارم، بٹن، اور گرڈ سبھی کلاسز ہیں:
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

### Q2: میں Delphi میں اجزاء کیسے بنا سکتا ہوں؟
**A:** TCcomponent یا TControl سے وراثت:
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

### Q3: Delphi اور Free Pascal میں کیا فرق ہے؟
**A:** Delphi Embarcadero کی طرف سے ایک تجارتی IDE/مرتب ہے۔ Free Pascal اوپن سورس کمپائلر ہے، اور Lazarus مفت IDE ہے۔ دونوں آبجیکٹ پاسکل نحو کا استعمال کرتے ہیں۔
### Q4: میں ڈیلفی میں ڈیٹا بیس کے ساتھ کیسے کام کروں؟
**A:** FireDAC یا dbExpress اجزاء استعمال کریں:
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

### Q5: کیا Delphi آج بھی متعلقہ ہے؟
**A:** میراثی ونڈوز ایپلیکیشنز کو برقرار رکھنے کے لیے، ہاں۔ نئے پروجیکٹس کے لیے، زیادہ تر ڈویلپر C# یا ویب ٹیکنالوجیز کو ترجیح دیتے ہیں۔ مفت پاسکل/لازارس ایک مفت کراس پلیٹ فارم متبادل فراہم کرتا ہے۔
---

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: ڈیٹا سے آگاہی فارم بنانا
**مرحلہ 1: مسئلہ کو سمجھیں**
ایک فارم بنائیں جو ڈیٹا بیس ریکارڈز کو دکھاتا اور اس میں ترمیم کرتا ہے۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
ڈیٹا سیٹ سے منسلک ڈیٹا سے آگاہ اجزاء استعمال کریں۔
**مرحلہ 3: نافذ کریں**```pascal
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

**مرحلہ 4: توسیع کریں**
توثیق، غلطی سے نمٹنے، اور تلاش/فلٹر کی فعالیت شامل کریں۔
---

## خلاصہ
ڈیلفی ایک تاریخی طور پر اہم زبان ہے جس نے ونڈوز کے لیے تیز رفتار ایپلیکیشن کی ترقی کا آغاز کیا۔ جدید ڈیلفی مقامی ونڈوز ایپلی کیشنز اور ڈیٹا بیس کے فرنٹ اینڈز کے لیے قابل رہتا ہے، لیکن اس کی کمیونٹی اور ماحولیاتی نظام کافی حد تک سکڑ گیا ہے۔ موجودہ ڈیلفی کوڈ بیس کو برقرار رکھنے کے لیے، یہ ضروری ہے۔ نئے پراجیکٹس کے لیے، زیادہ تر ڈویلپرز C#، ویب ٹیکنالوجیز، یا کراس پلیٹ فارم فریم ورک کی طرف ہجرت کر چکے ہیں۔ اوپن سورس فری پاسکل/لازارس پروجیکٹ آبجیکٹ پاسکل زبان میں دلچسپی رکھنے والوں کے لیے ایک مفت متبادل فراہم کرتا ہے۔