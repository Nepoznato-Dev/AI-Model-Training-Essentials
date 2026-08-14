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
# دلفی / آبجکت پاسکال
دلفی یک زبان برنامه نویسی شی گرا بر اساس پاسکال است که در ابتدا توسط Borland (بعدها Embarcadero، اکنون Idera) توسعه یافت. اولین بار در سال 1995 با نام "Delphi 1" منتشر شد و برای توسعه سریع برنامه های کاربردی (RAD) برنامه های دسکتاپ ویندوز طراحی شد. این زبان به طور رسمی به عنوان Object Pascal شناخته می شود و Delphi IDE یک طراح فرم بصری، ابزارهای پایگاه داده یکپارچه و یک کامپایلر قدرتمند را ارائه می دهد.
دلفی یکی از محبوب ترین ابزارهای توسعه ویندوز در اواخر دهه 1990 و اوایل دهه 2000 بود. در حالی که محبوبیت آن به طور قابل توجهی کاهش یافته است، یک پایگاه کاربری اختصاصی را حفظ می کند، به ویژه در برنامه های کاربردی دسکتاپ سازمانی، قسمت های جلویی پایگاه داده و نگهداری سیستم قدیمی. مدرن دلفی (11/12) از توسعه کراس پلتفرم برای Windows، macOS، iOS و Android از طریق چارچوب FireMonkey (FMX) پشتیبانی می کند.
---

## چرا دلفی مهم است
- **توسعه سریع برنامه**: طراح فرم بصری + کامپایل بومی ساختن رابط کاربری گرافیکی ویندوز را بسیار سریع ساخت.
- **عملکرد بومی**: مستقیماً در کد ماشین کامپایل می شود - بدون نیاز به زمان اجرا یا VM.
- **اتصال پایگاه داده**: اجزای پایگاه داده از لحاظ تاریخی عالی (dbExpress، FireDAC، ADO).
- **پایه کدهای قدیمی**: بسیاری از برنامه های کاربردی سازمانی هنوز در دلفی اجرا می شوند. تعمیر و نگهداری یک مهارت خاص است.
- **کراس پلتفرم (مدرن)**: فریم ورک FireMonkey ویندوز، macOS، iOS و Android را از یک پایگاه کد واحد هدف قرار می دهد.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **جمعیت رو به زوال** | بسیار کوچکتر از جوامع سی شارپ، جاوا یا جاوا اسکریپت | انجمن های فعال اما کوچک؛ پشتیبانی تجاری از Idera |
| **اکوسیستم محدود** | کتابخانه های شخص ثالث کمتر از زبان های مدرن | از کتابخانه مؤلفه VCL/FMX استفاده کنید. نوشتن اجزای سفارشی |
| **در درجه اول متمرکز بر ویندوز** | پشتیبانی کراس پلتفرم (FMX) بلوغ کمتری دارد | از C#، Flutter یا فن آوری های وب برای کراس پلتفرم واقعی |
| **هزینه صدور مجوز** | IDE تجاری به مجوز پولی نیاز دارد | جایگزین منبع باز: پاسکال رایگان / لازاروس |
| **مشکل استخدام** | توسعه دهندگان دلفی کمتری وارد بازار می شوند | حفظ سیستم های موجود؛ انتقال ویژگی های جدید به پشته های مدرن |
---

## اصول نحو
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

## نحو و الگوهای پیشرفته
### ژنریک ها و مجموعه ها
دلفی از ژنریک ها (از دلفی 2009) پشتیبانی می کند و کلاس های کانتینر ایمن نوع را فعال می کند.
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

### روش ها و بسته های ناشناس
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

### رابط ها و تزریق وابستگی
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

### الگوهای مؤلفه VCL
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

## معماری و طراحی سیستم
### معماری کامپوننت
VCL (کتابخانه اجزای بصری) و FMX (FireMonkey) دلفی بر اساس یک سلسله مراتب مؤلفه ساخته شده اند. هر عنصر بصری از`TComponent`به ارث می رسد.
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

### ساختار دایرکتوری پروژه معمولی
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

### فایل پروژه .dproj
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

## پیکربندی پروژه و سیستم ساخت
### مرجع دستورات کامپایلر
| بخشنامه | هدف | مثال |
|-----------|---------|---------|
| `{$APPTYPE CONSOLE}`| اپلیکیشن کنسول | `{$APPTYPE CONSOLE}`|
| `{$APPTYPE GUI}`| برنامه رابط کاربری گرافیکی (پیش فرض) | `{$APPTYPE GUI}`|
| `{$DEFINE DEBUG}`| تعریف نماد شرطی | `{$DEFINE DEBUG}`|
| `{$IFDEF symbol}`| تالیف مشروط | `{$IFDEF DEBUG}`|
| `{$R *.dfm}`| شامل منبع فرم | `{$R *.dfm}`|
| `{$WARNINGS OFF}`| سرکوب هشدارها | `{$WARNINGS OFF}`|
| `{$HINTS OFF}`| سرکوب نکات | `{$HINTS OFF}`|
| `{$OPTIMIZATION ON}`| فعال کردن بهینه ساز | `{$OPTIMIZATION ON}`|
| `{$STRINGCHECKS ON}`| فعال کردن بررسی محدوده رشته | `{$STRINGCHECKS ON}`|
### ساختمان از خط فرمان
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

### پیکربندی بسته (dpk.)
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

## تست و اشکال زدایی
### ویژگی های اشکال زدا IDE
IDE دلفی شامل یک دیباگر یکپارچه با امکانات کامل است.
| ویژگی | توضیحات |
|---------|-------------|
| **نقاط گسست** | تنظیم بر روی هر خط اجرایی. نقاط شکست شرطی پشتیبانی شده |
| **پنجره ساعت** | نظارت بر مقادیر متغیر در زمان واقعی |
| **پشته تماس** | مشاهده زنجیره تماس کامل با متغیرهای محلی |
| **پنجره سی پی یو** | نمایش اسمبلی تولید شده در کنار کد منبع |
| **نمایش حافظه** | حافظه خام را در هر آدرسی بررسی کنید |
| **نقاط شکست رویداد** | شکستن استثناها، بارگذاری های DLL، رویدادهای رشته |
| **اشکال زدایی از راه دور** | اشکال زدایی برنامه های در حال اجرا بر روی ماشین های راه دور |
| **تجسم داده** | بصری سازهای سفارشی برای مجموعه داده ها، رشته ها، مجموعه ها |
### چارچوب تست DUnit
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

### اشکال زدایی گردش کار
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

## قابلیت همکاری
### یکپارچه سازی COM/ActiveX
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

### فراخوانی DLL های C/C++
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

### .NET قابلیت همکاری
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

## الگوهای طراحی
### الگوی 1: Singleton (Thread-Safe)
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

### الگوی 2: مشاهده‌گر (رویداد محور)
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

### الگوی 3: روش کارخانه
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

## عملکرد و بهینه سازی
### مدیریت حافظه
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

### نکات بهینه سازی VCL/FMX
| تکنیک | تاثیر | توضیحات |
|-----------|--------|-------------|
| **BeginUpdate/EndUpdate** | بالا | بسته بندی لیست/به روز رسانی شبکه برای جلوگیری از رنگ آمیزی مجدد |
| **بافر دوگانه** | متوسط ​​|`DoubleBuffered := True`را برای کاهش سوسو زدن تنظیم کنید
| **لیست های مجازی** | بالا | استفاده از`TVirtualStringTree`برای مجموعه داده های بزرگ |
| **ترنینگ رشته** | متوسط ​​| استفاده مجدد از ثابت های رشته اجتناب از الحاق مکرر |
| **تجمیع اشیاء** | متوسط ​​| استفاده مجدد از اشیاء مکرر ایجاد/تخریب شده |
| **بارگذاری تنبل** | بالا | بارگذاری داده ها/فرم ها فقط در صورت نیاز |
| **بهینه سازی کامپایلر** | متوسط ​​|`{$O+}`را برای بیلدهای انتشار فعال کنید |
---

## استقرار و استفاده در دنیای واقعی
### گزینه های استقرار
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

### موارد استفاده در دنیای واقعی
| صنعت | برنامه | چرا دلفی |
|----------|------------|-----------|
| **مالی** | پلتفرم های معاملاتی، داشبورد بانکی | رابط کاربری گرافیکی بومی سریع، اتصال به پایگاه داده |
| **بهداشت** | تصویربرداری پزشکی، مدیریت بیمار | اجزای VCL، عملکرد بومی |
| **ساخت ** | سیستم های اسکادا کنترل صنعتی | دسترسی مستقیم سخت افزاری، پاسخ در زمان واقعی |
| **دولت** | ابزارهای اداری داخلی | تداوم سیستم میراث |
| ** مخابرات ** | داشبوردهای مانیتورینگ شبکه | تجسم سریع داده |
| **آموزش و پرورش** | نرم افزار آموزشی، ابزار آموزش الکترونیکی | توسعه سریع، پشتیبانی چند رسانه ای |
---

## چه زمانی از دلفی استفاده کنیم
| سناریو | چرا دلفی | جایگزین بهتر |
|----------|----------|------------------|
| تعمیر و نگهداری دلفی میراث | پایگاه کد موجود | — |
| برنامه های دسکتاپ ویندوز (سریع) | VCL بالغ و سریع است | سی شارپ (WPF/WinForms) |
| پیشانی پایگاه داده | اجزای داده عالی | سی شارپ، جاوا |
| دسکتاپ کراس پلتفرم ( طاقچه ) | FireMonkey وجود دارد | سی شارپ، فلوتر، الکترون |
| توسعه رابط کاربری گرافیکی جدید ویندوز | ممکن است اما جامعه در حال کوچک شدن است | سی شارپ (WPF/WinUI 3) |
| توسعه وب | مناسب نیست | جاوا اسکریپت، پایتون، سی شارپ |
| برنامه های موبایل | از طریق FMX امکان پذیر است اما محدود | سوئیفت، کاتلین، فلاتر |
---

## پرسش و پاسخ مصنوعی
### Q1: چارچوب VCL دلفی چگونه کار می کند؟
**A:** VCL کنترل های API ویندوز را در یک سلسله مراتب شی گرا قرار می دهد. فرم ها، دکمه ها و شبکه ها همه کلاس ها هستند:
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

### Q2: چگونه کامپوننت ها را در دلفی ایجاد کنم؟
**A:** ارث بری از TComponent یا TControl:
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

### Q3: تفاوت دلفی و پاسکال رایگان چیست؟
**A:** دلفی یک IDE/کامپایلر تجاری توسط Embarcadero است. Free Pascal کامپایلر منبع باز است و Lazarus IDE رایگان است. هر دو از دستور Object Pascal استفاده می کنند.
### Q4: چگونه با پایگاه های داده در دلفی کار کنم؟
**A:** از اجزای FireDAC یا dbExpress استفاده کنید:
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

### Q5: آیا دلفی هنوز هم مربوط به امروز است؟
**A:** برای حفظ برنامه های قدیمی ویندوز، بله. برای پروژه های جدید، بیشتر توسعه دهندگان سی شارپ یا فناوری های وب را ترجیح می دهند. Pascal/Lazarus رایگان یک جایگزین رایگان بین پلتفرمی ارائه می دهد.
---

## حل مسئله زنجیره ای از فکر
### مشکل 1: ساخت یک فرم داده آگاه
**مرحله 1: مشکل را درک کنید**
فرمی ایجاد کنید که رکوردهای پایگاه داده را نمایش و ویرایش کند.
**مرحله 2: رویکرد را شناسایی کنید**
از اجزای داده آگاه متصل به یک مجموعه داده استفاده کنید.
**مرحله 3: پیاده سازی **```pascal
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

**مرحله 4: تمدید**
اعتبارسنجی، مدیریت خطا، و قابلیت جستجو/فیلتر را اضافه کنید.
---

## خلاصه
دلفی یک زبان مهم تاریخی است که پیشگام توسعه سریع برنامه های کاربردی برای ویندوز است. دلفی مدرن همچنان قادر به استفاده از برنامه های کاربردی ویندوز بومی و بخش های جلویی پایگاه داده است، اما جامعه و اکوسیستم آن به طور قابل توجهی کوچک شده است. برای حفظ پایگاه های کد دلفی موجود، ضروری است. برای پروژه‌های جدید، اکثر توسعه‌دهندگان به C#، فناوری‌های وب یا چارچوب‌های چند پلتفرمی مهاجرت کرده‌اند. پروژه منبع باز Free Pascal / Lazarus یک جایگزین رایگان برای علاقه مندان به زبان Object Pascal فراهم می کند.