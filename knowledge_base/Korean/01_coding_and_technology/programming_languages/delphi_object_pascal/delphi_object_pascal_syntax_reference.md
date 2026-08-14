---
# Metadata
title: "Delphi / Object Pascal — Syntax Reference"
description: "Detailed syntax reference for Delphi/Object Pascal covering operators, control flow, classes, interfaces, generics, records, properties, and advanced OOP patterns."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [delphi, object-pascal, syntax-reference, oop, generics, vcl, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# 델파이/오브젝트 파스칼 — 구문 참조
이 문서는 Delphi/Object Pascal에 대한 포괄적이고 구조화된 구문 참조를 제공합니다. 이는 철저한 구문 패턴, OOP 기능, 제네릭, 레코드 및 언어 관용구에 중점을 두어 주요 Delphi 참조를 보완합니다.
---

## 연산자 및 표현식
| 카테고리 | 운영자 | 설명 | 예 |
|------------|------------|---------------|---------|
| **산술** | `+`| 추가 | `A + B`|
| | `-`| 빼기 | `A - B`|
| | `*`| 곱셈 | `A * B`|
| | `/`| 실제 분할 |  `A / B`(항상 Real 반환) |
| | `div`| 정수 나눗셈 |  `A div B`(정수 반환) |
| | `mod`| 모듈러스 | `A mod B`|
| **비교** | `=`| 같음 | `A = B`|
| | `<>`| 같지 않음 | `A <> B`|
| | `<`| 미만 | `A < B`|
| | `>`| 보다 큼 | `A > B`|
| | `<=`| 작거나 같음 | `A <= B`|
| | `>=`| 크거나 같음 | `A >= B`|
| **논리적** | `and`| 논리 AND | `A and B`|
| | `or`| 논리적 OR | `A or B`|
| | `not`| 논리적 NOT | `not A`|
| | `xor`| 독점 OR | `A xor B`|
| **문자열** | `+`| 연결 | `'Hello' + ' ' + 'World'`|
| **설정** | `in`| 회원 | `X in [1, 2, 3]`|
| | `+`| 연합 | `SetA + SetB`|
| | `-`| 차이 | `SetA - SetB`|
| | `*`| 교차로 | `SetA * SetB`|
| **과제** | `:=`| 값 할당 | `X := 42`|
| **주소** | `@`| 주소 | `P := @X`|
| | `^`| 역참조 | `P^`|
---

## 제어 흐름
```pascal
// If-then-else
if X > 0 then
  WriteLn('Positive')
else if X = 0 then
  WriteLn('Zero')
else
  WriteLn('Negative');

// Case statement
case DayOfWeek of
  1: WriteLn('Monday');
  2: WriteLn('Tuesday');
  3, 4, 5: WriteLn('Midweek');
  6..7: WriteLn('Weekend');
else
  WriteLn('Invalid day');
end;

// For loop (known count)
for I := 1 to 10 do
  WriteLn(I);

for I := 10 downto 1 do
  WriteLn(I);

// While loop (condition first)
while X > 0 do
begin
  WriteLn(X);
  Dec(X);
end;

// Repeat-until loop (condition last, executes at least once)
repeat
  WriteLn(X);
  Dec(X);
until X = 0;

// For-in loop (enumerable collections)
for Item in Collection do
  Process(Item);

// Inline variable declaration (Delphi 10.3+)
for var I := 0 to List.Count - 1 do
  WriteLn(List[I]);
```

---

## 데이터 유형 및 변수
```pascal
// Scalar types
var
  B: Boolean;          // True or False
  C: Char;             // Single character
  I: Integer;          // 32-bit signed integer
  L: Int64;            // 64-bit signed integer
  D: Double;           // 64-bit floating point
  E: Extended;         // 80-bit floating point (x86)
  S: string;           // Unicode string (reference-counted)
  SA: AnsiString;      // ANSI string

// Enumerated types
type
  TColor = (Red, Green, Blue, Yellow);
  TDay = (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday);

var
  MyColor: TColor;
  Today: TDay;

begin
  MyColor := Green;
  Today := Monday;
  if Ord(MyColor) = 1 then WriteLn('Green is index 1');
end;

// Subrange types
type
  TPercent = 0..100;
  TLetter = 'A'..'Z';

// Set types
type
  TColors = set of TColor;
  TDigits = set of 0..9;

var
  Palette: TColors;
begin
  Palette := [Red, Blue];
  Include(Palette, Green);
  if Green in Palette then WriteLn('Has green');
end;

// Records (value types)
type
  TPoint = record
    X: Double;
    Y: Double;
    function DistanceTo(const Other: TPoint): Double;
  end;

  TPoint3D = record
    X, Y, Z: Double;
    class function Origin: TPoint3D; static;
    class operator Add(const A, B: TPoint3D): TPoint3D;
  end;

class operator TPoint3D.Add(const A, B: TPoint3D): TPoint3D;
begin
  Result.X := A.X + B.X;
  Result.Y := A.Y + B.Y;
  Result.Z := A.Z + B.Z;
end;
```

---

## 클래스 및 OOP
```pascal
type
  // Base class
  TShape = class
  private
    FColor: TColor;
    FVisible: Boolean;
  protected
    procedure SetColor(const Value: TColor); virtual;
    function GetArea: Double; virtual; abstract;
  public
    constructor Create; virtual;
    destructor Destroy; override;
    procedure Draw; virtual;
    property Color: TColor read FColor write SetColor;
    property Visible: Boolean read FVisible write FVisible default True;
  end;

  // Derived class
  TCircle = class(TShape)
  private
    FRadius: Double;
  protected
    function GetArea: Double; override;
  public
    constructor Create; override;
    constructor CreateWithRadius(ARadius: Double);
    property Radius: Double read FRadius write FRadius;
  end;

  // Abstract class
  TAnimal = class abstract
  public
    function Speak: string; virtual; abstract;
    procedure Feed; virtual;
  end;

  // Sealed class (cannot be inherited)
  TFinalClass = class sealed
  end;

  // Class with class methods and class vars
  TCounter = class
  private
    class var FCount: Integer;
  public
    class procedure Increment; static;
    class function GetCount: Integer; static;
    class constructor Create;  // Class constructor (runs once)
  end;

constructor TShape.Create;
begin
  inherited Create;
  FColor := Red;
  FVisible := True;
end;

destructor TShape.Destroy;
begin
  // Cleanup
  inherited;
end;

constructor TCircle.CreateWithRadius(ARadius: Double);
begin
  inherited Create;
  FRadius := ARadius;
end;

function TCircle.GetArea: Double;
begin
  Result := Pi * FRadius * FRadius;
end;
```

---

## 인터페이스
```pascal
type
  // Interface definition (GUID required for COM interop)
  ISerializable = interface
    ['{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}']
    function Serialize: string;
    procedure Deserialize(const AData: string);
  end;

  IPrintable = interface
    ['{B2C3D4E5-F6A7-8901-BCDE-F12345678901}']
    function ToString: string;
    procedure Print;
  end;

  // Class implementing multiple interfaces
  TDocument = class(TInterfacedObject, ISerializable, IPrintable)
  private
    FContent: string;
  public
    function Serialize: string;
    procedure Deserialize(const AData: string);
    function ToString: string; override;
    procedure Print;
  end;

// Usage with automatic reference counting
var
  Doc: ISerializable;
begin
  Doc := TDocument.Create;  // No Free needed — interface ref counting
  Doc.Serialize;
end;
```

---

## 제네릭
```pascal
type
  // Generic class
  TRepository<T: class, constructor> = class
  private
    FItems: TObjectList<T>;
  public
    constructor Create;
    destructor Destroy; override;
    procedure Add(const AItem: T);
    function FindById(AId: Integer): T;
    function GetAll: TArray<T>;
    property Count: Integer read GetCount;
  end;

  // Generic record with constraints
  TOptional<T> = record
  private
    FValue: T;
    FHasValue: Boolean;
  public
    class function Empty: TOptional<T>; static;
    class function Of(const AValue: T): TOptional<T>; static;
    function HasValue: Boolean;
    function GetValue: T;
    function GetValueOrDefault(const ADefault: T): T;
  end;

  // Generic method
  TUtils = class
  public
    class function Max<T>(const A, B: T): T; static;
    class procedure Swap<T>(var A, B: T); static;
  end;

  // Generic interface
  IComparer<T> = interface
    function Compare(const A, B: T): Integer;
  end;
```

---

## 예외 처리
```pascal
// Try-except-finally
try
  Stream := TFileStream.Create('data.bin', fmOpenRead);
  try
    Stream.ReadBuffer(Buffer, SizeOf(Buffer));
    ProcessData(Buffer);
  except
    on E: EReadError do
      WriteLn('Read error: ', E.Message);
    on E: EStreamError do
      WriteLn('Stream error: ', E.Message);
    on E: Exception do
      WriteLn('Unexpected: ', E.ClassName, ' - ', E.Message);
  end;
finally
  Stream.Free;  // Always executed
end;

// Custom exceptions
type
  EValidationError = class(Exception)
  private
    FField: string;
  public
    constructor Create(const AField, AMessage: string);
    property Field: string read FField;
  end;

raise EValidationError.Create('Email', 'Invalid email format');
```

---

## 요약
Delphi/Object Pascal은 깔끔하고 읽기 쉬운 구문과 강력한 OOP 기능을 결합합니다. 클래스, 인터페이스, 제네릭 및 레코드는 애플리케이션 개발을 위한 전체 툴킷을 제공합니다. 언어의 명시적인 시작/끝 블록, 유형이 지정된 변수, 대소문자를 구분하지 않는 식별자 덕분에 언어에 접근하기 쉽습니다. VCL/FMX 프레임워크는 신속한 애플리케이션 개발을 위해 시각적 구성 요소 라이브러리를 사용하여 언어를 확장합니다. 엔터프라이즈 Windows 애플리케이션과 데이터베이스 프런트엔드의 경우 Delphi는 여전히 생산적인 선택입니다.