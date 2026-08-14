---
# Metadata
title: "OCaml — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the OCaml ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ocaml, ecosystem, tooling, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "13 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# OCaml — 생태계 및 툴링 가이드
이 가이드에서는 OCaml 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## OCaml 구현
| 구현 | 메모 |
|---------------|-------|
| **OCaml 5** | 효과 및 병렬성을 갖춘 현재 |
| **OCaml 4.14** | 최신 4.x(널리 사용됨) |
| **이유** | 대체 구문(Facebook) |
| **재스크립트** | Modern Reason 후속 버전(BuckleScript) |
| **OCaml 네이티브** | 네이티브 코드로 컴파일 |
| **js_of_ocaml** | JavaScript로 컴파일 |
```bash
ocaml --version           # check version
ocamlfind list            # list packages
dune build                # build project
dune runtest              # run tests
dune exec ./main.exe      # run executable
```

---

## 빌드 도구 및 패키지 관리
| 도구 | 목적 |
|------|---------|
| **듄** | 빌드 시스템(표준) |
| **오팜** | 패키지 관리자 |
| **오캠찾기** | 도서관 찾기 |
| **듄 프로젝트** | 프로젝트 구성 |
| **이시** | 대체 패키지 관리자 |
```bash
# opam
opam init                 # initialize
opam install dune         # install package
opam list                 # list installed
opam update               # update index
opam upgrade              # upgrade packages

# Create project
dune init proj myapp      # new project
dune build                # build
dune runtest              # run tests
```

```lisp
;; dune-project
(lang dune 3.12)
(name myapp)
(generate_opam_files true)

;; dune (executable)
(executable
 (public_name myapp)
 (name main)
 (libraries core async cohttp-lwt-unix))

;; dune (library)
(library
 (name mylib)
 (public_name mylib)
 (libraries core))
```

```opam
# myapp.opam
opam-version: "2.0"
synopsis: "My OCaml application"
depends: [
  "ocaml" {>= "5.0"}
  "dune" {>= "3.0"}
  "core" {>= "v0.16"}
  "async" {>= "v0.16"}
]
```

---

## 웹 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **꿈** | 풀스택 | 최신 웹(Express에서 영감을 받음) |
| **공동http** | HTTP | HTTP 클라이언트/서버 |
| **아편** | 경량 | 시나트라 같은 |
| **옥시겐** | 풀스택 | Eliom(클라이언트-서버) |
| **변형** | 경량 | 웹 프레임워크 |
| **Lwt** | 비동기 | 협동 스레딩 |
| **비동기** | 비동기 | 제인 스트리트의 비동기 |
```ocaml
(* Dream example *)
let () =
  Dream.run
  @@ Dream.logger
  @@ Dream.router [
       Dream.get "/" (fun _ -> Dream.html "Hello, World!");
       Dream.get "/users/:id" (fun req ->
         let id = Dream.param "id" req in
         Dream.json {|{"id": "|} ^ id ^ {|"}|});
     ]
```

---

## 데이터베이스
| 기술 | 유형 |
|------------|------|
| **칵티** | 유형이 안전한 데이터베이스 |
| **PG'OCaml** | PostgreSQL(유형 안전) |
| **sqlite3-ocaml** | SQLite 바인딩 |
| **mysql-ocaml** | MySQL 바인딩 |
| **postgresql-ocaml** | PostgreSQL 바인딩 |
| **어민** | Git과 유사한 데이터베이스 |
```ocaml
(* Caqti example *)
module Db = Caqti_connect_sig(S)

let find_user (module Db : Db) id =
  Db.find_opt
    (Caqti_type.(int ->! t2 int string)
       "SELECT id, name FROM users WHERE id = ?")
    id
```

---

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **알코테스트** | 빠르고 다채로운 테스트 |
| **단위** | 단위 테스트(xUnit 스타일) |
| **Q체크** | 속성 기반 테스트 |
| **지렛대** | 퍼지 테스트 |
| **ppx_expect** | 테스트 예상(제인 스트리트) |
```ocaml
(* Alcotest example *)
let test_find () =
  let service = UserService.create () in
  let user = UserService.find service 1 in
  Alcotest.(check (option string)) "found user" (Some "Alice") (Option.map User.name user)

let test_not_found () =
  let service = UserService.create () in
  let user = UserService.find service 999 in
  Alcotest.(check (option string)) "not found" None (Option.map User.name user)

let () =
  Alcotest.run "UserService" [
    "find", [
      Alcotest.test_case "finds user" `Quick test_find;
      Alcotest.test_case "not found" `Quick test_not_found;
    ];
  ]
```

---

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **ocaml형식** | 코드 서식 |
| **ocp-들여쓰기** | 들여쓰기 |
| **ocaml-lsp** | 언어 서버 |
| **ppx** | 구문 확장 |
| **멀린** | IDE 지원(완성, 유형) |
```bash
ocamlformat --inplace src/*.ml  # format
dune build @fmt                 # check formatting
```

---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **코어/베이스** | Jane Street의 표준 라이브러리 |
| **Stdlib** | OCaml 표준 라이브러리 |
| **결과** | 오류 처리 |
| **컨테이너** | 데이터 구조 |
| **배터리** | 확장된 표준 라이브러리 |
| **Lwt** | 경량 스레드 |
| **비동기** | 비동기 프로그래밍 |
| **에이오** | 효과 기반 I/O(OCaml 5) |
| **도메인** | 병렬성(OCaml 5) |
| **ppx_파생** | 함수 파생 ​​|
| **ppx_yojson_conv** | JSON 파생 |
| **요존** | JSON 구문 분석 |
| **옹스트롬** | 파서 결합자 |
| **멘히르** | 파서 생성기 |
| **오캠그래프** | 그래프 라이브러리 |
| **자리스** | 임의 정밀도 |
| **단위** | 테스트 |
---

## 형식적 방법
| 도구 | 목적 |
|------|---------|
| **코크** | 증명 도우미(OCaml 작성) |
| **왜3** | 프로그램 검증 |
| **Alt-Ergo** | SMT 솔버 |
| **OCaml + 증명** | 검증된 프로그램 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **VS 코드 + ocaml 플랫폼** | 최고의 OCaml LSP |
| **Emacs + tuareg + 멀린** | 클래식 OCaml 환경 |
| **빔 + 멀린** | Vim 통합 |
| **Neovim + ocaml-lsp** | 터미널 기반 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **네이티브 바이너리** |  `dune build`는 네이티브 바이너리를 생성합니다 |
| **정적 연결** | 완전 정적 바이너리 |
| **도커** | 컨테이너화 |
| **오팜 스위치** | 여러 OCaml 버전 |
| **크로스 컴파일** | 크로스 컴파일 |
---

## 요약
OCaml의 생태계는 정확성, 성능 및 기능적 프로그래밍에 중점을 두고 있습니다. 표준 스택은 런타임용 **OCaml 5**, 빌드용 **Dune**, 패키지용 **opam**, 웹용 **Dream** 또는 **Cohttp**, 데이터베이스용 **Caqti**, 테스트용 **Alcotest**, 형식 지정용 **ocamlformat**, IDE 지원용 **Merlin**입니다. OCaml은 컴파일러, 공식 검증, 금융 시스템 및 정확성과 성능이 중요한 모든 분야에서 탁월합니다. OCaml 5의 효과 시스템과 병렬성(도메인)은 언어에 현대적인 동시성을 제공합니다. 생태계는 컴파일러(Coq, F*), 정리 증명자, 높은 보증 소프트웨어를 구축하는 데 필수적입니다.