---
# Metadata
title: "Delphi / Object Pascal — Cheat Sheet"
description: "Quick-reference cheat sheet for Delphi syntax and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [delphi, object-pascal, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Delphi / Object Pascal — Bảng tính gian lận
## Cơ bản
```delphi
// Variables
var
  Name: string;
  Age: Integer;
  Pi: Double;
  Active: Boolean;

Name := 'Alice';
Age := 30;
Pi := 3.14159;
Active := True;

const
  MAX = 100;
  Greeting = 'Hello';

// Type conversion
StrToInt('42')
IntToStr(42)
FloatToStr(3.14)
StrToFloat('3.14')
StrToDate('2024-01-01')
DateToStr(Now)

// String operations
Length(Name)
UpperCase(Name)
LowerCase(Name)
Trim(Name)
Pos('lic', Name)
Copy(Name, 1, 3)
StringReplace(Name, 'Alice', 'Bob', [rfReplaceAll])
Format('Hello, %s! Age: %d', [Name, Age])
Name + ' Smith'  // concatenation
```

## Cấu trúc dữ liệu
```delphi
// Dynamic array
var
  Arr: TArray<Integer>;
  Arr := TArray<Integer>.Create(1, 2, 3);
  Arr[0];
  Length(Arr);
  // TList<T>
  var List := TList<Integer>.Create;
  List.Add(1);
  List[0];
  List.Count;
  List.Remove(1);

// TStringList
var SL := TStringList.Create;
SL.Add('Alice');
SL.Add('Bob');
SL[0];
SL.Count;
SL.IndexOf('Alice');
SL.Sort;
SL.Delimiter := ',';
SL.CommaText;

// Dictionary
var Dict := TDictionary<string, Integer>.Create;
Dict.Add('alice', 90);
Dict['bob'] := 85;
Dict.ContainsKey('alice');
Dict.TryGetValue('alice', Score);
Dict.Keys;
Dict.Values;

// Record
type
  TPoint = record
    X, Y: Double;
  end;
var P: TPoint;
P.X := 1.0;
P.Y := 2.0;
```

## Luồng điều khiển
```delphi
// If
if Condition then
  DoSomething
else if Other then
  DoOther
else
  DoDefault;

// Case
case Day of
  1..5: ShowMessage('Weekday');
  6, 7: ShowMessage('Weekend');
else
  ShowMessage('Unknown');
end;

// Loops
for I := 0 to 9 do
  WriteLn(I);

for I := 9 downto 0 do
  WriteLn(I);

for Item in Collection do
  Process(Item);

while Condition do
begin
  DoSomething;
end;

repeat
  DoSomething;
until Condition;
```

## Lớp học
```delphi
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
  Result := Name + ' barks';
end;

// Usage
var Dog := TDog.Create('Rex');
try
  ShowMessage(Dog.Speak);
finally
  Dog.Free;
end;
```

## Quản lý tài nguyên
```delphi
// try/finally
var Stream := TFileStream.Create('data.bin', fmOpenRead);
try
  ProcessData(Stream);
finally
  Stream.Free;
end;

// try/except
try
  Result := StrToInt(UserInput);
except
  on E: EConvertError do
    ShowMessage('Invalid number');
  on E: Exception do
    ShowMessage('Error: ' + E.Message);
end;

// try/except/finally
try
  RiskyOperation;
except
  on E: Exception do HandleError(E);
finally
  Cleanup;
end;
```

## Các mẫu phổ biến
```delphi
// String builder
var SB := TStringBuilder.Create;
try
  for I := 0 to Items.Count - 1 do
    SB.Append(Items[I]).Append(', ');
  Result := SB.ToString;
finally
  SB.Free;
end;

// Anonymous methods
var OnDone := procedure(const Msg: string)
  begin
    ShowMessage(Msg);
  end;

// LINQ-style (System.Generics.Collections)
uses System.Generics.Collections, System.Generics.Defaults;
var Filtered := TArray.FindAll(Arr,
  function(const X: Integer): Boolean
  begin Result := X > 2; end);

// With block
with DateTime do
begin
  Year := 2024;
  Month := 1;
  Day := 1;
end;
```
