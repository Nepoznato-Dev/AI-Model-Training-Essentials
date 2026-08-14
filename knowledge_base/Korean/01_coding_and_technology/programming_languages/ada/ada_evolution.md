---
# Metadata
title: "Ada — Version History & Evolution"
description: "Comprehensive version history and evolution of Ada from Ada 83 to modern Ada."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ada, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ada — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 에이다 83 | 1983년 | **첫 번째 표준**(MIL-STD-1815A) — Ada Lovelace |
| 에이다 87 | 1987 | 사소한 개정(정밀도, 접근성 규칙) |
| 에이다 95 | 1995 | **주요**: OOP(태그된 유형), 보호된 개체, 작업 개선 |
| 에이다 2005 | 2005년 | **인터페이스**, 익명 액세스 유형,`for`/`while`루프 개선 |
| 에이다 2012 | 2012 | **관점 지향 프로그래밍**, 계약(사전/사후 조건),`iterator`|
| 에이다 2022 | 2022 | **`with ghost`**, 병렬 구성, 실시간 개선 |
## 주요 이정표
### Ada 83 — 탄생(1983)
- **1983**: 미국 국방부는 임베디드 시스템에 단일 언어를 요구합니다.
- Jean Ichbiah는 CII Honeywell Bull(프랑스)에서 디자인을 이끌고 있습니다.
- Ada Lovelace의 이름을 딴 — 최초의 컴퓨터 프로그래머
- 주요 기능: 강력한 타이핑, 패키지, 작업(동시성), 제네릭, 예외
- **목표**: 안전에 중요한 시스템 — 항공, 국방, 우주
### Ada 95 — 객체 지향 Ada(1995)
- **최초의 ISO 표준화 OO 언어**(Java 표준화 전)
- 태그된 유형(클래스), 클래스 전체 유형, 동적 디스패치
- 보호된 개체(안전한 동시 데이터 액세스)
- 하위 패키지(계층적 라이브러리)
- Pragma 기반 구성
### Ada 2005 — 개선(2005)
- 인터페이스(인터페이스의 다중 상속)
- 익명 액세스 유형(간소화된 포인터)
-`for`루프 개선
- 컨테이너 라이브러리(이중 연결 목록, 벡터, 맵)
- 확장된`return`문
### Ada 2012 — 계약 및 측면(2012)
- **관점 지향 프로그래밍**: 선언에 첨부된`aspect`절
- **계약**:`Pre`,`Post`,`Type_Invariant`— 공식 검증 내장
- 반복자 지원(`for X of Container loop`)
-`overriding`표시기
- 표현 기능 : `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — 병렬 및 고스트(2022)
- **`with ghost`**: 확인을 위한 고스트 코드(프로덕션에서 컴파일됨)
- **병렬 구성**:`parallel`루프,`parallel`블록
- 실시간 개선
- 컨테이너 개선
-`Iterator`측면 개선
## 구문 진화
```ada
-- Ada 83: Package-based design
package Stack is
   procedure Push(Item : in Integer);
   function Pop return Integer;
   Stack_Empty : exception;
end Stack;

package body Stack is
   Max : constant := 100;
   Data : array(1..Max) of Integer;
   Top : Integer range 0..Max := 0;

   procedure Push(Item : in Integer) is
   begin
      Top := Top + 1;
      Data(Top) := Item;
   end Push;

   function Pop return Integer is
      Result : Integer;
   begin
      if Top = 0 then raise Stack_Empty; end if;
      Result := Data(Top);
      Top := Top - 1;
      return Result;
   end Pop;
end Stack;

-- Ada 95: Object-oriented
type Shape is tagged record
   X, Y : Float;
end record;

function Area(S : Shape) return Float is
begin
   return 0.0;
end Area;

type Circle is new Shape with record
   Radius : Float;
end record;

function Area(C : Circle) return Float is
begin
   return 3.14159 * C.Radius ** 2;
end Area;

-- Ada 2012: Contracts and aspects
type Temperature is new Float
   with Dynamic_Predicate => Temperature >= -273.15;

procedure Set_Temp(T : in out Temperature)
   with Pre  => T >= -273.15,
        Post => T'Old < T;  -- temperature must increase

-- Expression functions (Ada 2012)
function Double(X : Integer) return Integer is (X * 2);

-- Ada 2022: Parallel constructs
parallel
   for I in Data'Range loop
      Data(I) := Compute(I);
   end loop;

-- Ada 2022: Ghost code for verification
procedure Process(X : in out Integer)
   with Ghost => True,
        Pre   => X > 0,
        Post  => X > X'Old;
```

## 기능 진화
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## 주요 디자인 원칙
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## 생태계 성장
```
1983: Ada 83 — DoD mandate, defense/aviation adoption
1987: Ada 87 — minor fixes
1995: Ada 95 — OOP, ISO standard
1995: GNAT (GNU NYU Ada Translator) — open source compiler
2005: Ada 2005 — interfaces, containers
2012: Ada 2012 — contracts, aspects
2015: SPARK 2014 — formal verification for Ada
2022: Ada 2022 — parallel, ghost code
2025: Ada used in: aviation (DO-178C), space (ESA), rail, defense
       Compilers: GNAT (open source), ObjectAda, AdaCore tools
       SPARK subset used for formal verification of critical code
```
