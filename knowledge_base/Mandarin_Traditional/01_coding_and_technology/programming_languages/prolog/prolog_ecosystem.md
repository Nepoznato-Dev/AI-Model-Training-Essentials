<!--
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

-->
# Prolog — 生態系與工具指南
本指南涵蓋了 Prolog 生態系統中的基本工具、實作和基礎設施。
---

## Prolog 實現
|實施 |類型 |筆記|
|----------------|------|--------|
| **SWI-Prolog** |開源|最受歡迎、功能豐富 |
| **GNU Prolog** |開源|原生編譯|
| **占卜者前言** |開源|現代、符合 ISO 標準 |
| **特瑞拉序** |開源|快速、輕量 |
| **ECLiPSe** |開源|約束邏輯程式設計|
| **SICStus** |商業|高效能|
| **XSB** |開源|表格化，有理有據的語意|
```bash
swipl --version           # check version
swipl script.pl           # run script
swipl                     # interactive REPL
swipl -g main -t halt script.pl  # run goal
```

---

## 套件管理
|工具|目的|
|------|---------|
| **SWI-Prolog 套件** |套件管理器 |
| **Prolog 包註冊表** |包存儲庫 |
```prolog
% Install pack in SWI-Prolog
?- pack_install(strings).
?- pack_install(http).
?- pack_list.              % list installed
?- pack_upgrade(strings).  % upgrade
```

---

## 網路和 HTTP
|圖書館 |目的|
|---------|---------|
| **http_unix_daemon** | HTTP 伺服器守護程序 |
| **http_伺服器** |內建HTTP伺服器|
| **P引擎** |網路前言|
| **克莉奧佩特里亞** |語意網框架|
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

## 資料庫和數據
|技術 |目的|
|------------|---------|
| **ODBC** |資料庫連線 |
| **SQLite** |嵌入式資料庫|
| **伯克利資料庫** |鍵值儲存 |
| **SGML/XML** | XML解析|
| **SGML/RDF** |語意網路|
| **Prolog 事實** |內建知識庫|
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

## 測試
|框架|目的|
|------------|---------|
| **普魯特** |內建單元測試 (SWI) |
| **快速檢查** |基於屬性的測試 |
| **並發測試** |並行測試執行 |
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

## 約束編程
|圖書館 |目的|
|---------|---------|
| **中電(FD)** |有限域約束 |
| **CLP(B)** |布林約束 |
| **CLP(QR)** |理性限制|
| **CHR** |約束處理規則|
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

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **列表** |列表操作|
| **申請** |高階謂詞 |
| **聽寫** |字典操作|
| **字串** |字串處理 |
| **插座** |網路程式設計|
| **SSL** | TLS/SSL |
| **加密** |密碼學 |
| **sgml** | XML/HTML 解析 |
| **http/json** | JSON 處理 |
| **烏裡** | URI 處理 |
| **流程** |流程管理|
| **線程** |多線程|
| **聚合** |聚合|
| **提交** |記憶|
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **SWI-Prolog IDE** |內建IDE |
| **VS Code + Prolog** |語言支援 |
| **Emacs + prolog 模式** |經典Prolog環境|
---

## 部署
|方法|筆記|
|--------|--------|
| **獨立執行檔** |`swipl-ld`或已儲存狀態 |
| **碼頭工人** |貨櫃式|
| **網路服務** | HTTP 伺服器 |
| **嵌入式** |嵌入式Prolog |
```bash
# Create standalone executable
swipl -o myapp -g main -t halt -c script.pl

# Save state
swipl -o mystate.sav -c script.pl
swipl mystate.sav    # run saved state
```

---

＃＃ 概括
Prolog 的生態系統以邏輯程式設計和限制條件求解為中心。標準實作是：**SWI-Prolog** 作為最受歡迎的，**GNU Prolog** 用於本機編譯，**Scryer Prolog** 用於現代 ISO 一致性。主要函式庫包括用於約束程式設計的 **CLP(FD)**、用於 Web 服務的 **http_server**、用於資料庫的 **ODBC** 以及用於測試的 **plunit**。 Prolog 擅長人工智慧、專家系統、自然語言處理、定理證明和約束滿足。此生態系統對於符號推理、知識表示和組合最佳化問題至關重要。