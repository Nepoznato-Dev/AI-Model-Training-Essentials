<!--
---
# Metadata
title: "Ada — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ada ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ada, ecosystem, tooling, compilers, safety-critical, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Ada — 생태계 및 툴링 가이드
이 가이드에서는 Ada 생태계의 필수 도구, 라이브러리 및 인프라를 다룹니다.
---

## 컴파일러 및 구현
| 컴파일러 | 유형 | 메모 |
|----------|------|-------|
| **그나트** | 오픈 소스 | GCC 기반, 가장 널리 사용됨 |
| **GNAT 커뮤니티** | 무료 | AdaCore의 무료 버전 |
| **GNAT 프로** | 상업용 | 안전 인증, AdaCore |
| **오브젝트에이다** | 상업용 | 안전이 중요한 Windows |
| **야누스/에이다** | 상업용 | 임베디드 시스템 |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## 시스템 구축 및 패키지 관리
| 도구 | 목적 |
|------|---------|
| **알리르** | 최신 패키지 관리자(권장) |
| **GPR빌드** | 프로젝트 빌드 도구 |
| **GPR(GNAT 프로젝트)** | 프로젝트 파일 형식 |
| **만들기** | 클래식 빌드 |
```toml
# alire.toml
name = "myapp"
description = "My Ada application"
version = "0.1.0"

[[depends-on]]
gnat = "^13"
gnatcoll = "^24"

[[pins]]
```

```bash
alr init --bin myapp      # create project
alr build                 # build
alr run                   # run
alr get --build gnatcoll  # get dependency
alr search                # search packages
alr index                 # update index
```

```gpr
-- myproject.gpr
project Myproject is
   for Source_Dirs use ("src/**");
   for Object_Dir use "obj";
   for Main use ("main.adb");
   
   package Compiler is
      for Default_Switches ("Ada") use ("-gnatwa", "-gnatVa", "-O2");
   end Compiler;
   
   package Binder is
      for Default_Switches ("Ada") use ("-E");  -- store exceptions
   end Binder;
end Myproject;
```

---

## 안전 및 검증
| 도구 | 목적 |
|------|---------|
| **GNAT증명** | 정식 검증 |
| **스파크** | 안전에 중요한 하위 집합 |
| **코드피어** | 정적 분석 |
| **폴리스페이스** | 런타임 검증 |
| **보장** | 정적 분석 |
```ada
-- SPARK example
package Stack with
   SPARK_Mode
is
   type Bounded_Stack (Capacity : Positive) is tagged private;
   
   procedure Push (S : in out Bounded_Stack; Element : Integer)
      with Pre  => not S.Is_Full,
           Post => not S.Is_Empty and S.Top = Element;
   
   function Is_Full (S : Bounded_Stack) return Boolean;
   function Is_Empty (S : Bounded_Stack) return Boolean;
   
private
   type Bounded_Stack (Capacity : Positive) is tagged record
      Data : array (1 .. Capacity) of Integer;
      Top_Index : Natural := 0;
   end record;
end Stack;
```

---

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **AU단위** | 단위 테스트 프레임워크 |
| **아벤** | 간단한 테스트 |
| **GNAT테스트** | 코드 기반 테스트 |
| **gprbuild** | 빌드 및 테스트 |
```ada
with AUnit.Simple_Test_Cases;
with AUnit.Test_Suites;
with AUnit.Run;
with AUnit.Reporter.Text;

package Stack_Test is
   type Test_Case is new AUnit.Simple_Test_Cases.Test_Case with null record;
   
   function Name (T : Test_Case) return AUnit.Message_String;
   procedure Run_Test (T : in out Test_Case);
end Stack_Test;

package body Stack_Test is
   function Name (T : Test_Case) return AUnit.Message_String is
   begin
      return new String'("Stack Tests");
   end Name;
   
   procedure Run_Test (T : in out Test_Case) is
      S : Bounded_Stack (10);
   begin
      Push (S, 42);
      AUnit.Assertions.Assert (Top (S) = 42, "Top should be 42");
      AUnit.Assertions.Assert (not Is_Empty (S), "Should not be empty");
   end Run_Test;
end Stack_Test;
```

---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **Ada.컨테이너** | 벡터, 지도, 세트 |
| **Ada.Strings** | 문자열 처리 |
| **Ada.Text_IO** | 콘솔 I/O |
| **Ada.캘린더** | 날짜/시간 |
| **GNAT콜** | GNAT 유틸리티 |
| **AWS** | Ada 웹 서버 |
| **XML/Ada** | XML 구문 분석 |
| **GID** | 이미지 디코딩 |
| **SDLA다** | SDL2 바인딩 |
| **GLFW** | OpenGL 윈도우화 |
| **Cortex GNAT 런타임** | 임베디드(ARM) |
---

## 동시성
| 기능 | 목적 |
|---------|---------|
| **작업** | 동시 스레드 |
| **보호된 객체** | 동기화된 데이터 |
| **문 선택** | 랑데뷰 |
| **참가 전화** | 동기화 |
```ada
task type Worker is
   entry Do_Work (Item : in Integer);
end Worker;

task body Worker is
   Value : Integer;
begin
   loop
      select
         accept Do_Work (Item : in Integer) do
            Value := Item;
         end Do_Work;
         Process (Value);
      or
         terminate;
      end select;
   end loop;
end Worker;
```

---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **GPS(GNAT 프로그래밍 스튜디오)** | AdaCore의 IDE |
| **VS 코드 + Ada** | Ada 언어 지원 |
| **Emacs + ada 모드** | 클래식 Ada 환경 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **정적 바이너리** | GNAT는 정적 바이너리를 생성합니다 |
| **크로스 컴파일** | GNAT 크로스 컴파일 |
| **내장형** | 베어메탈, RTOS(Ravenscar) |
| **도커** | 컨테이너화 |
| **안전인증** | DO-178C, IEC 61508, 공통 기준 |
---

## 요약
Ada의 생태계는 안전이 중요하고 신뢰성이 높은 시스템을 위해 특별히 구축되었습니다. 표준 툴체인은 컴파일용 **GNAT**(GCC 기반), 패키지 관리용 **Alire**, 빌드용 **GPRbuild**, 공식 검증용 **GNATprove** 및 **SPARK**, 테스트용 **AUnit**입니다. Ada는 항공우주(DO-178C), 국방, 철도, 의료 기기 및 정확성이 가장 중요한 모든 영역에서 탁월합니다. Ada의 강점은 강력한 타이핑, 동시성(작업, 보호 개체), 형식 검증(SPARK) 및 안전 인증입니다. 생태계는 안전이 중요한 임베디드 시스템에 필수적입니다.