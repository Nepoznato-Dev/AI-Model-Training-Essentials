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
# เดลฟี / วัตถุปาสคาล
Delphi เป็นภาษาโปรแกรมเชิงวัตถุซึ่งมีพื้นฐานมาจาก Pascal ซึ่งเดิมพัฒนาโดย Borland (ต่อมาคือ Embarcadero ปัจจุบันคือ Idera) เปิดตัวครั้งแรกในปี 1995 ในชื่อ "Delphi 1" ได้รับการออกแบบมาเพื่อการพัฒนาแอปพลิเคชันอย่างรวดเร็ว (RAD) ของแอปพลิเคชันเดสก์ท็อป Windows ภาษานี้มีชื่ออย่างเป็นทางการว่า Object Pascal และ Delphi IDE มอบเครื่องมือออกแบบรูปแบบภาพ เครื่องมือฐานข้อมูลแบบรวม และคอมไพเลอร์ที่ทรงพลัง
Delphi เป็นหนึ่งในเครื่องมือพัฒนา Windows ที่ได้รับความนิยมมากที่สุดในช่วงปลายทศวรรษ 1990 และต้นปี 2000 แม้ว่าความนิยมจะลดลงอย่างมาก แต่ก็สามารถรักษาฐานผู้ใช้ไว้โดยเฉพาะในแอปพลิเคชันเดสก์ท็อประดับองค์กร ส่วนหน้าของฐานข้อมูล และการบำรุงรักษาระบบเดิม Modern Delphi (11/12) รองรับการพัฒนาข้ามแพลตฟอร์มสำหรับ Windows, macOS, iOS และ Android ผ่านเฟรมเวิร์ก FireMonkey (FMX)
---

## ทำไมเดลฟีถึงมีความสำคัญ
- **การพัฒนาแอปพลิเคชันอย่างรวดเร็ว**: โปรแกรมออกแบบฟอร์มภาพ + การคอมไพล์แบบเนทีฟทำให้การสร้าง Windows GUI รวดเร็วมาก
- **ประสิทธิภาพดั้งเดิม**: คอมไพล์ไปยังรหัสเครื่องโดยตรง โดยไม่ต้องใช้รันไทม์หรือ VM
- **การเชื่อมต่อฐานข้อมูล**: ส่วนประกอบฐานข้อมูลที่ยอดเยี่ยมในอดีต (dbExpress, FireDAC, ADO)
- **ฐานรหัสเดิม**: แอปพลิเคชันระดับองค์กรจำนวนมากยังคงทำงานบน Delphi การบำรุงรักษาเป็นทักษะเฉพาะ
- **ข้ามแพลตฟอร์ม (สมัยใหม่)**: เฟรมเวิร์ก FireMonkey กำหนดเป้าหมายไปที่ Windows, macOS, iOS และ Android จากโค้ดเบสเดียว
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ชุมชนเสื่อมถอย** | เล็กกว่าชุมชน C#, Java หรือ JavaScript มาก ฟอรัมที่มีการใช้งานแต่มีขนาดเล็ก การสนับสนุนเชิงพาณิชย์จาก Idera |
| **ระบบนิเวศมีจำกัด** | ไลบรารีของบุคคลที่สามน้อยกว่าภาษาสมัยใหม่ | ใช้ไลบรารีคอมโพเนนต์ VCL/FMX เขียนส่วนประกอบที่กำหนดเอง |
| **เน้น Windows เป็นหลัก** | การสนับสนุนข้ามแพลตฟอร์ม (FMX) ยังไม่บรรลุนิติภาวะ | ใช้ C#, Flutter หรือเทคโนโลยีเว็บสำหรับ | ข้ามแพลตฟอร์มอย่างแท้จริง
| **ค่าลิขสิทธิ์** | Commercial IDE ต้องมีใบอนุญาตแบบชำระเงิน | ทางเลือกโอเพ่นซอร์ส: ฟรี Pascal / Lazarus |
| **จ้างลำบาก** | นักพัฒนา Delphi เข้าสู่ตลาดน้อยลง | บำรุงรักษาระบบที่มีอยู่ ย้ายคุณสมบัติใหม่ไปยังสแต็กที่ทันสมัย ​​|
---

## พื้นฐานไวยากรณ์
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

## ไวยากรณ์และรูปแบบขั้นสูง
### ข้อมูลทั่วไปและคอลเลกชัน
Delphi รองรับยาชื่อสามัญ (ตั้งแต่ Delphi 2009) ทำให้สามารถใช้งานคลาสคอนเทนเนอร์ที่ปลอดภัยต่อประเภทได้
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

### วิธีการและการปิดแบบไม่ระบุชื่อ
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

### อินเทอร์เฟซและการฉีดพึ่งพา
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

### รูปแบบส่วนประกอบ VCL
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

## สถาปัตยกรรมและการออกแบบระบบ
### สถาปัตยกรรมส่วนประกอบ
VCL (Visual Component Library) ของ Delphi และ FMX (FireMonkey) สร้างขึ้นจากลำดับชั้นของส่วนประกอบ องค์ประกอบภาพทั้งหมดสืบทอดมาจาก `TComponent`
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

### โครงสร้างไดเร็กทอรีโครงการทั่วไป
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

### ไฟล์โครงการ .dproj
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### การอ้างอิงคำสั่งคอมไพเลอร์
| คำสั่ง | วัตถุประสงค์ | ตัวอย่าง |
|----------|---------|---------|
| `{$APPTYPE CONSOLE}`| แอปพลิเคชันคอนโซล | `{$APPTYPE CONSOLE}`|
| `{$APPTYPE GUI}`| แอปพลิเคชัน GUI (ค่าเริ่มต้น) | `{$APPTYPE GUI}`|
| `{$DEFINE DEBUG}`| กำหนดสัญลักษณ์ตามเงื่อนไข | `{$DEFINE DEBUG}`|
| `{$IFDEF symbol}`| การรวบรวมแบบมีเงื่อนไข | `{$IFDEF DEBUG}`|
| `{$R *.dfm}`| รวมทรัพยากรของฟอร์ม | `{$R *.dfm}`|
| `{$WARNINGS OFF}`| ระงับคำเตือน | `{$WARNINGS OFF}`|
| `{$HINTS OFF}`| ระงับคำแนะนำ | `{$HINTS OFF}`|
| `{$OPTIMIZATION ON}`| เปิดใช้งานเครื่องมือเพิ่มประสิทธิภาพ | `{$OPTIMIZATION ON}`|
| `{$STRINGCHECKS ON}`| เปิดใช้งานการตรวจสอบช่วงสตริง | `{$STRINGCHECKS ON}`|
### อาคารจาก Command Line
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

### การกำหนดค่าแพ็คเกจ (.dpk)
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

## การทดสอบและการดีบัก
### คุณสมบัติดีบักเกอร์ IDE
IDE ของ Delphi มีดีบักเกอร์ในตัวที่มีคุณสมบัติครบถ้วน
| คุณสมบัติ | คำอธิบาย |
|---------|-------------|
| **จุดพัก** | ตั้งค่าบนบรรทัดปฏิบัติการใดๆ รองรับเบรกพอยต์แบบมีเงื่อนไข |
| **หน้าต่างดู** | ตรวจสอบค่าตัวแปรแบบเรียลไทม์ |
| **โทรสแต็ค** | ดูสายโซ่การโทรแบบเต็มพร้อมตัวแปรท้องถิ่น |
| **หน้าต่างซีพียู** | ดูแอสเซมบลีที่สร้างขึ้นพร้อมกับซอร์สโค้ด |
| **มุมมองหน่วยความจำ** | ตรวจสอบหน่วยความจำดิบตามที่อยู่ใด ๆ |
| **จุดพักเหตุการณ์** | ทำลายข้อยกเว้น โหลด DLL เหตุการณ์เธรด |
| **การดีบักระยะไกล** | แก้ไขข้อบกพร่องแอปพลิเคชันที่ทำงานบนเครื่องระยะไกล |
| **การแสดงข้อมูลเป็นภาพ** | เครื่องมือสร้างภาพแบบกำหนดเองสำหรับชุดข้อมูล สตริง คอลเลกชัน |
### กรอบการทดสอบ DUnit
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

### ขั้นตอนการแก้ไขข้อบกพร่อง
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

## การทำงานร่วมกัน
### การรวม COM/ActiveX
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

### กำลังเรียก C/C++ DLLs
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

### .NET การทำงานร่วมกัน
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

## รูปแบบการออกแบบ
### รูปแบบ 1: ซิงเกิลตัน (ปลอดภัยต่อเธรด)
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

### รูปแบบ 2: ผู้สังเกตการณ์ (ขับเคลื่อนด้วยเหตุการณ์)
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

### รูปแบบ 3: วิธีการจากโรงงาน
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### การจัดการหน่วยความจำ
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

### เคล็ดลับการเพิ่มประสิทธิภาพ VCL/FMX
| เทคนิค | ผลกระทบ | คำอธิบาย |
|----------|--------|-------------|
| **เริ่มต้นอัปเดต/สิ้นสุดการอัปเดต** | สูง | อัปเดตรายการสรุป/ตารางเพื่อป้องกันการทาสีใหม่ |
| **บัฟเฟอร์สองเท่า** | ปานกลาง | ตั้งค่า`DoubleBuffered := True`เพื่อลดการสั่นไหว |
| **รายการเสมือน** | สูง | ใช้`TVirtualStringTree`สำหรับชุดข้อมูลขนาดใหญ่ |
| **สตริงฝึกงาน** | ปานกลาง | นำค่าคงที่สตริงมาใช้ซ้ำ หลีกเลี่ยงการต่อข้อมูลซ้ำ |
| **การรวมวัตถุ** | ปานกลาง | ใช้วัตถุที่สร้าง/ทำลายบ่อยครั้ง |
| **ขี้เกียจโหลด** | สูง | โหลดข้อมูล/แบบฟอร์มเมื่อจำเป็นเท่านั้น |
| **การเพิ่มประสิทธิภาพคอมไพเลอร์** | ปานกลาง | เปิดใช้งาน`{$O+}`สำหรับ release build |
---

## การปรับใช้และการใช้งานในโลกแห่งความเป็นจริง
### ตัวเลือกการปรับใช้
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

### กรณีการใช้งานจริง
| อุตสาหกรรม | ใบสมัคร | ทำไมต้องเดลฟี |
|----------|-------------|-----------|
| **การเงิน** | แพลตฟอร์มการซื้อขาย แดชบอร์ดการธนาคาร | GUI ดั้งเดิมที่รวดเร็ว, การเชื่อมต่อฐานข้อมูล |
| **การดูแลสุขภาพ** | การถ่ายภาพทางการแพทย์ การจัดการผู้ป่วย | ส่วนประกอบ VCL ประสิทธิภาพดั้งเดิม |
| **การผลิต** | ระบบ SCADA ระบบควบคุมอุตสาหกรรม | การเข้าถึงฮาร์ดแวร์โดยตรง การตอบสนองแบบเรียลไทม์ |
| **รัฐบาล** | เครื่องมือการบริหารภายใน | ความต่อเนื่องของระบบเดิม |
| **โทรคมนาคม** | แดชบอร์ดการตรวจสอบเครือข่าย | การแสดงภาพข้อมูลที่รวดเร็ว |
| **การศึกษา** | ซอฟต์แวร์เพื่อการศึกษา เครื่องมืออีเลิร์นนิง | การพัฒนาอย่างรวดเร็ว รองรับมัลติมีเดีย |
---

## เมื่อใดควรใช้เดลฟี
| สถานการณ์ | ทำไมต้องเดลฟี | ทางเลือกที่ดีกว่า |
|----------|-----------|-------------------|
| การบำรุงรักษา Delphi รุ่นเก่า | รหัสฐานที่มีอยู่ | — |
| แอปเดสก์ท็อป Windows (รวดเร็ว) | VCL เป็นผู้ใหญ่และรวดเร็ว | C# (WPF/WinForms) |
| ส่วนหน้าของฐานข้อมูล | องค์ประกอบข้อมูลที่ยอดเยี่ยม | C#, ชวา |
| เดสก์ท็อปข้ามแพลตฟอร์ม (เฉพาะกลุ่ม) | มี FireMonkey อยู่ | C#, กระพือ, อิเล็กตรอน |
| การพัฒนา Windows GUI ใหม่ | เป็นไปได้แต่ชุมชนกำลังหดตัว | C# (WPF/WinUI 3) |
| การพัฒนาเว็บ | ไม่เหมาะ | จาวาสคริปต์, ไพธอน, C# |
| แอพมือถือ | เป็นไปได้ผ่าน FMX แต่จำกัด | Swift, Kotlin, Flutter |
---

## คำถามและคำตอบสังเคราะห์
### คำถามที่ 1: เฟรมเวิร์ก VCL ของ Delphi ทำงานอย่างไร
**ตอบ:** VCL ล้อมรอบการควบคุม Windows API ในลำดับชั้นเชิงวัตถุ แบบฟอร์ม ปุ่ม และกริดล้วนเป็นคลาสทั้งหมด:
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

### Q2: ฉันจะสร้างส่วนประกอบใน Delphi ได้อย่างไร
**A:** สืบทอดจาก TComponent หรือ TControl:
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

### Q3: อะไรคือความแตกต่างระหว่าง Delphi และ Free Pascal?
**ตอบ:** Delphi เป็น IDE/คอมไพเลอร์เชิงพาณิชย์โดย Embarcadero Free Pascal เป็นคอมไพเลอร์โอเพ่นซอร์ส และ Lazarus เป็น IDE ฟรี ทั้งสองใช้ไวยากรณ์ Object Pascal
### Q4: ฉันจะทำงานกับฐานข้อมูลใน Delphi ได้อย่างไร
**ตอบ:** ใช้ส่วนประกอบ FireDAC หรือ dbExpress:
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

### Q5: ปัจจุบัน Delphi ยังคงเกี่ยวข้องอยู่หรือไม่
**ตอบ:** สำหรับการบำรุงรักษาแอปพลิเคชัน Windows รุ่นเก่า ใช่ สำหรับโปรเจ็กต์ใหม่ นักพัฒนาส่วนใหญ่ชอบ C# หรือเทคโนโลยีเว็บ Free Pascal/Lazarus เป็นทางเลือกข้ามแพลตฟอร์มฟรี
---

## การแก้ปัญหาลูกโซ่แห่งความคิด
### ปัญหาที่ 1: การสร้างแบบฟอร์ม Data-Aware
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
สร้างแบบฟอร์มที่แสดงและแก้ไขบันทึกฐานข้อมูล
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้ส่วนประกอบที่รับรู้ข้อมูลซึ่งเชื่อมโยงกับชุดข้อมูล
**ขั้นตอนที่ 3: นำไปใช้**```pascal
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

**ขั้นตอนที่ 4: ขยาย**
เพิ่มการตรวจสอบ การจัดการข้อผิดพลาด และฟังก์ชันการค้นหา/ตัวกรอง
---

## สรุป
Delphi เป็นภาษาที่มีความสำคัญทางประวัติศาสตร์ที่บุกเบิกการพัฒนาแอปพลิเคชั่นอย่างรวดเร็วสำหรับ Windows Modern Delphi ยังคงมีความสามารถสำหรับแอปพลิเคชัน Windows แบบเนทีฟและส่วนหน้าของฐานข้อมูล แต่ชุมชนและระบบนิเวศของมันหดตัวลงอย่างมาก สำหรับการรักษาฐานรหัส Delphi ที่มีอยู่นั้น ยังคงมีความสำคัญ สำหรับโปรเจ็กต์ใหม่ นักพัฒนาส่วนใหญ่ได้ย้ายไปยัง C# เทคโนโลยีเว็บ หรือเฟรมเวิร์กข้ามแพลตฟอร์ม โปรเจ็กต์โอเพ่นซอร์ส Free Pascal / Lazarus มอบทางเลือกฟรีสำหรับผู้ที่สนใจภาษา Object Pascal