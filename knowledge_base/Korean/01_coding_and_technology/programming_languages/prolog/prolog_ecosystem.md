---
# Metadata
title: "Prolog — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Prolog ecosystem including implementations, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [prolog, ecosystem, tooling, logic-programming, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "11 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# 프롤로그 — 생태계 및 툴링 가이드
이 가이드는 Prolog 생태계의 필수 도구, 구현 및 인프라를 다룹니다.
---

## 프롤로그 구현
| 구현 | 유형 | 메모 |
|---------------|------|-------|
| **SWI-프롤로그** | 오픈 소스 | 가장 인기 있고 기능이 풍부한 |
| **GNU 프롤로그** | 오픈 소스 | 네이티브 컴파일 |
| **스크라이어 프롤로그** | 오픈 소스 | 최신, ISO 준수 |
| **트렐라 프롤로그** | 오픈 소스 | 빠르고 가벼운 |
| **ECLiPSe** | 오픈 소스 | 제약 논리 프로그래밍 |
| **SICStus** | 상업용 | 고성능 |
| **XSB** | 오픈 소스 | 표 작성, 근거가 충분한 의미론 |
```bash
swipl --version           # check version
swipl script.pl           # run script
swipl                     # interactive REPL
swipl -g main -t halt script.pl  # run goal
```

---

## 패키지 관리
| 도구 | 목적 |
|------|---------|
| **SWI-프롤로그 팩** | 패키지 관리자 |
| **프롤로그 팩 레지스트리** | 패키지 저장소 |
```prolog
% Install pack in SWI-Prolog
?- pack_install(strings).
?- pack_install(http).
?- pack_list.              % list installed
?- pack_upgrade(strings).  % upgrade
```

---

## 웹 & HTTP
| 도서관 | 목적 |
|---------|---------|
| **http_unix_daemon** | HTTP 서버 데몬 |
| **http_서버** | 내장 HTTP 서버 |
| **P엔진** | 웹 프롤로그 |
| **클리오파트리아** | 시맨틱 웹 프레임워크 |
```prolog
% SWI-Prolog HTTP server
:- use_module(library(http/http_server)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/json)).

:- http_handler(root(.), handle_home, []).
:- http_handler(root(users/ID), handle_user(ID), []).

handle_home(_Request) :-
    reply_html_page(
        title('Home'),
        h1('Hello from Prolog!')
    ).

handle_user(ID, _Request) :-
    atom_string(ID, IdStr),
    reply_json_dict(json{id=IdStr, name="User"}).

:- initialization(http_server([port(8080)])).
```

---

## 데이터베이스 및 데이터
| 기술 | 목적 |
|------------|---------|
| **ODBC** | 데이터베이스 연결 |
| **SQLite** | 내장형 데이터베이스 |
| **버클리 DB** | 키-값 저장소 |
| **SGML/XML** | XML 구문 분석 |
| **SGML/RDF** | 시맨틱 웹 |
| **프롤로그 사실** | 내장된 지식 기반 |
```prolog
% ODBC database access
:- use_module(library(odbc)).

query_users :-
    odbc_connect('mydb', Conn, [user('admin'), password('secret')]),
    odbc_query(Conn, 'SELECT name, age FROM users WHERE age > 18', row(Name, Age)),
    format('~w is ~w years old~n', [Name, Age]),
    odbc_disconnect(Conn).
```

---

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **플루니트** | 내장 단위 테스트(SWI) |
| **빠른 확인** | 속성 기반 테스트 |
| **동시 테스트** | 병렬 테스트 실행 |
```prolog
:- begin_tests(user_service).

test(find_existing_user) :-
    setup_test_db,
    find_user(1, User),
    assertion(User.name == "Alice").

test(not_found) :-
    setup_test_db,
    \+ find_user(999, _).

test(find_all_adults) :-
    setup_test_db,
    findall(User, adult(User), Adults),
    assertion(length(Adults, 3)).

:- end_tests(user_service).

% Run tests
% ?- run_tests.
```

---

## 제약 프로그래밍
| 도서관 | 목적 |
|---------|---------|
| **CLP(FD)** | 유한 도메인 제약 |
| **CLP(B)** | 부울 제약조건 |
| **CLP(QR)** | 합리적인 제약 |
| **CHR** | 제약조건 처리 규칙 |
```prolog
% CLP(FD) example - Sudoku solver
:- use_module(library(clpfd)).

sudoku(Rows) :-
    length(Rows, 9),
    maplist(same_length(Rows), Rows),
    append(Rows, Vs), Vs ins 1..9,
    maplist(all_distinct, Rows),
    transpose(Rows, Columns),
    maplist(all_distinct, Columns),
    Rows = [As,Bs,Cs,Ds,Es,Fs,Gs,Hs,Is],
    blocks([As,Bs,Cs]), blocks([Ds,Es,Fs]), blocks([Gs,Hs,Is]).

blocks([A,B,C]) :-
    append([A,B,C], Vs),
    length(Vs, 27),
    chunks(Vs, 3, Bs),
    maplist(all_distinct, Bs).

chunks([], _, []).
chunks([X,Y,Z|Rest], N, [[X,Y,Z]|Bs]) :-
    chunks(Rest, N, Bs).
```

---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **목록** | 목록 조작 |
| **신청** | 고차 술어 |
| **받아쓰기** | 사전 작업 |
| **문자열** | 문자열 처리 |
| **소켓** | 네트워크 프로그래밍 |
| **ssl** | TLS/SSL |
| **암호화폐** | 암호화 |
| **sgml** | XML/HTML 구문 분석 |
| **http/json** | JSON 처리 |
| **우리** | URI 처리 |
| **프로세스** | 프로세스 관리 |
| **스레드** | 멀티스레딩 |
| **집계** | 집계 |
| **테이블링** | 메모 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **SWI-프롤로그 IDE** | 내장 IDE |
| **VS 코드 + 프롤로그** | 언어 지원 |
| **Emacs + 프롤로그 모드** | 클래식 프롤로그 환경 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **독립 실행형 실행 파일** | `swipl-ld`또는 저장된 상태 |
| **도커** | 컨테이너화 |
| **웹 서비스** | HTTP 서버 |
| **내장형** | 임베디드 프롤로그 |
```bash
# Create standalone executable
swipl -o myapp -g main -t halt -c script.pl

# Save state
swipl -o mystate.sav -c script.pl
swipl mystate.sav    # run saved state
```

---

## 요약
Prolog의 생태계는 논리 프로그래밍과 제약 조건 해결에 중점을 두고 있습니다. 표준 구현은 가장 널리 사용되는 **SWI-Prolog**, 기본 컴파일용 **GNU Prolog**, 최신 ISO 규격용 **Scryer Prolog**입니다. 주요 라이브러리에는 제약 프로그래밍용 **CLP(FD)**, 웹 서비스용 **http_server**, 데이터베이스용 **ODBC**, 테스트용 **plunit**이 포함됩니다. Prolog는 인공 지능, 전문가 시스템, 자연어 처리, 정리 증명 및 제약 조건 만족에 탁월합니다. 생태계는 상징적 추론, 지식 표현, 조합 최적화 문제에 필수적입니다.