<!--
---
# Metadata
title: "OCaml — Version History & Evolution"
description: "Comprehensive version history and evolution of OCaml from Caml to modern OCaml."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ocaml, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# OCaml — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 캠 | 1985 | **범주형 추상 기계 언어**(INRIA) |
| 캠 라이트 | 1990 | 라이트웨이트 캠(자비에 르로이) |
| OCaml 1.0 | 1996 | **Objective Caml** — OOP 추가 |
| OCaml 3.0 | 2000 | **주요**: 다형성 방법,`lazy`,`Obj`|
| OCaml 3.05 | 2002 | 네이티브 코드 컴파일러 개선 |
| OCaml 3.10 | 2007년 |  클래스 정의의`module type of`,`let`바인딩 |
| OCaml 3.11 | 2008 | `private`유형 주석,`module type of`|
| OCaml 3.12 | 2010 | 일류 모듈 |
| OCaml 4.00 | 2012 | **주요**: 서명의`module type of`,`val`|
| OCaml 4.01 | 2013 | `Bytes`모듈(변경 가능한 문자열로 구분됨) |
| OCaml 4.02 | 2014 | `Float`모듈,`String`개선 |
| OCaml 4.03 | 2016 | `Result`유형, `Seq`(지연 시퀀스) |
| OCaml 4.04 | 2017 | 시공간 프로파일러,`floatarray`|
| OCaml 4.06 | 2018 | `module`표현식의`let`바인딩 |
| OCaml 4.08 | 2019 | `Binding`개선,`Seq`개선 |
| OCaml 4.10 | 2020 | `Bigarray`개선 |
| OCaml 4.12 | 2021 | `Stdlib`개선 |
| OCaml 4.14 | 2022 | **테일 모듈로 단점** (TMC) |
| OCaml 5.0 | 2022 | **주요**: 효과 핸들러, 병렬 처리(GIL 없음) |
| OCaml 5.1 | 2023년 | `Domain`개선,`Effect`개선 |
| OCaml 5.2 | 2024 | 오류 메시지 개선,`Domain`개선 |
| OCaml 5.3 | 2025 | 지속적인 개발 |
## 주요 이정표
### 캠(1985~1995)
- **1985**: Gérard Huet가 INRIA(프랑스)에서 Caml을 만듭니다.
- **이름**: "범주형 추상 기계 언어"
- **1990**: Caml Light — Xavier Leroy의 경량 버전
- 패턴 매칭, Hindley-Milner 유형 추론
### OCaml 1.0–3.x: OOP 추가(1996–2011)
- **1996**: OCaml(Objective Caml) — 객체 지향 기능 추가
- **3.0 (2000)**: 다형성 방법,`lazy`평가
- **3.10(2007)**:`module type of`
- **3.12 (2010)**: **일류 모듈** — 값으로서의 모듈
### OCaml 4.x: 최신 OCaml(2012~2021)
- **4.00 (2012)**:`module type of`, 향상된 모듈 시스템
- **4.01 (2013)**:`Bytes`모듈 — 기본적으로 변경할 수 없는 문자열
- **4.03 (2016)**:`Result`유형,`Seq`(지연 시퀀스)
- **4.08(2019)**: 오류 메시지 개선
- **4.14(2022)**: TMC(Tail-modulo-cons) — 재귀 생성자를 위한 더 나은 메모리
### OCaml 5.x: 병렬 혁명(2022~현재)
- **5.0(2022)**: **효과 핸들러**, **진정한 병렬 처리**(순수 코드에 대해 GIL 제거)
  -`Domain`— 병렬 계산을 위한 OS 스레드
  -`Effect`— 대수 효과 핸들러(계속)
  - 더 이상 전역 통역사 잠금이 없습니다 — 실제 멀티코어 OCaml
- **5.1(2023)**: 도메인 개선, 효과 핸들러 개선
- **5.2(2024)**: 오류 메시지 개선, 추가 개선
## 구문 진화
```ocaml
(* OCaml 3.x: Pattern matching, modules *)
type shape =
  | Circle of float
  | Rectangle of float * float

let area = function
  | Circle r -> Float.pi *. r *. r
  | Rectangle (w, h) -> w *. h

(* OCaml 3.12: First-class modules *)
module type Printable = sig
  val to_string : t -> string
end

let print (module M : Printable) x =
  print_endline (M.to_string x)

(* OCaml 4.03: Result type *)
let safe_divide x y =
  if y = 0 then Error "division by zero"
  else Ok (x / y)

(* OCaml 4.08: Better error messages *)
let x = 1 +. 2
(* Error: This expression has type int but an expression was expected of type float *)

(* OCaml 5.0: Effect handlers *)
type _ Effect.t += Read : string Effect.t

let with_input input f =
  Effect.Deep.try_with f ()
    { effc = fun (type a) (eff : a Effect.t) ->
        match eff with
        | Read -> Some (fun (k : (a, _) Effect.Deep.continuation) ->
            Effect.Deep.continue k input)
        | _ -> None }

(* OCaml 5.0: Parallelism with Domain *)
let parallel_map f list =
  let domains = List.map (fun x ->
    Domain.spawn (fun () -> f x)
  ) list in
  List.map Domain.join domains

(* OCaml: Functor (module parameter) *)
module MakeSet (Ord : Map.OrderedType) = Set.Make(Ord)
module IntSet = MakeSet(struct type t = int let compare = compare end)
```

## 유형 시스템 진화
```
Caml (1985):       Hindley-Milner type inference, pattern matching
Caml Light (1990): Modules, functors
OCaml 1.0 (1996):  Objects, classes, inheritance
OCaml 3.0 (2000):  Polymorphic methods, lazy
OCaml 3.12 (2010): First-class modules
OCaml 4.03 (2016): Result, Seq
OCaml 4.14 (2022): Tail-modulo-cons
OCaml 5.0 (2022):  Effect handlers, Domain (parallelism)
```

## 주요 디자인 원칙
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## 생태계 성장
```
1985: Caml created at INRIA (France)
1990: Caml Light — lightweight version
1996: OCaml — adds OOP
2002: Jane Street adopts OCaml — financial trading
2010: First-class modules
2012: OPAM package manager
2016: OCaml 4.03 — Result type
2022: OCaml 5.0 — effect handlers, parallelism
2025: OCaml used in:
       - Jane Street (financial trading, largest OCaml shop)
       - Facebook/Flow (JavaScript type checker)
       - Tezos (blockchain)
       - Coq (theorem prover)
       - Infer (Facebook's static analyzer)
       - Ocsigen (web framework)
       Compilers: ocamlc (bytecode), ocamlopt (native)
       Tools: dune (build), opam (packages), merlin (IDE)
```
