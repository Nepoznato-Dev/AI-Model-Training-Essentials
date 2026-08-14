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
# Prolog - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือที่จำเป็น การใช้งาน และโครงสร้างพื้นฐานในระบบนิเวศของ Prolog
---

## การใช้งาน Prolog
| การนำไปปฏิบัติ | พิมพ์ | หมายเหตุ |
|---------|-|-------|
| **SWI-คำนำ** | โอเพ่นซอร์ส | ยอดนิยมและมีคุณลักษณะหลากหลาย |
| **คำนำ GNU** | โอเพ่นซอร์ส | การรวบรวมพื้นเมือง |
| **คำนำ Scryer** | โอเพ่นซอร์ส | ทันสมัย ​​สอดคล้องตามมาตรฐาน ISO |
| **Trealla อารัมภบท** | โอเพ่นซอร์ส | รวดเร็ว น้ำหนักเบา |
| **ECLiPSe** | โอเพ่นซอร์ส | การเขียนโปรแกรมลอจิกจำกัด |
| **ซิคตัส** | เชิงพาณิชย์ | ประสิทธิภาพสูง |
| **XSB** | โอเพ่นซอร์ส | Tableling ความหมายที่มีรากฐานอย่างดี |
```bash
swipl --version           # check version
swipl script.pl           # run script
swipl                     # interactive REPL
swipl -g main -t halt script.pl  # run goal
```

---

## การจัดการแพ็คเกจ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ชุด SWI-Prolog** | ผู้จัดการแพ็คเกจ |
| **Prolog Pack Registry** | พื้นที่เก็บข้อมูลแพ็กเกจ |
```prolog
% Install pack in SWI-Prolog
?- pack_install(strings).
?- pack_install(http).
?- pack_list.              % list installed
?- pack_upgrade(strings).  % upgrade
```

---

## เว็บและ HTTP
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **http_unix_daemon** | ดีมอนเซิร์ฟเวอร์ HTTP |
| **http_server** | เซิร์ฟเวอร์ HTTP ในตัว |
| **เพนกวิน** | เว็บโปรล็อก |
| **คลีโอปาเตรีย** | กรอบงานเว็บเชิงความหมาย |
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

## ฐานข้อมูลและข้อมูล
| เทคโนโลยี | วัตถุประสงค์ |
|------------|---------|
| **ODBC** | การเชื่อมต่อฐานข้อมูล |
| **SQLite** | ฐานข้อมูลแบบฝัง |
| **เบิร์กลีย์ ดีบี** | ที่เก็บคีย์-ค่า |
| **SGML/XML** | การแยกวิเคราะห์ XML |
| **SGML/RDF** | เว็บความหมาย |
| **ข้อเท็จจริงอารัมภบท** | ฐานความรู้ในตัว |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **แยก** | การทดสอบหน่วยในตัว (SWI) |
| **ตรวจสอบด่วน** | การทดสอบตามคุณสมบัติ |
| **การทดสอบพร้อมกัน** | การดำเนินการทดสอบแบบขนาน |
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

## การเขียนโปรแกรมข้อจำกัด
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **ซีแอลพี(FD)** | ข้อจำกัดโดเมนจำกัด |
| **ซีแอลพี(บี)** | ข้อจำกัดบูลีน |
| **CLP(QR)** | ข้อจำกัดเชิงเหตุผล |
| **CHR** | กฎการจัดการข้อจำกัด |
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

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **รายการ** | การจัดการรายการ |
| **สมัคร** | ภาคแสดงลำดับที่สูงกว่า |
| **คำสั่ง** | การทำงานของพจนานุกรม |
| **สตริง** | การจัดการสตริง |
| **ซ็อกเก็ต** | การเขียนโปรแกรมเครือข่าย |
| **ssl** | TLS/SSL |
| **คริปโต** | การเข้ารหัส |
| **sgml** | การแยกวิเคราะห์ XML/HTML |
| **http/json** | การจัดการ JSON |
| **ยูริ** | การจัดการ URI |
| **กระบวนการ** | การจัดการกระบวนการ |
| **กระทู้** | มัลติเธรด |
| **รวม** | การรวมตัว |
| **การจัดโต๊ะ** | ท่องจำ |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **SWI-Prolog IDE** | IDE ในตัว |
| **VS Code + Prolog** | รองรับภาษา |
| **Emacs + โหมดโปรล็อก** | สภาพแวดล้อม Prolog แบบคลาสสิก |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **ปฏิบัติการแบบสแตนด์อโลน** | `swipl-ld`หรือสถานะที่บันทึกไว้ |
| **นักเทียบท่า** | บรรจุในตู้คอนเทนเนอร์ |
| **บริการทางเว็บ** | เซิร์ฟเวอร์ HTTP |
| **ฝังตัว** | คำนำแบบฝัง |
```bash
# Create standalone executable
swipl -o myapp -g main -t halt -c script.pl

# Save state
swipl -o mystate.sav -c script.pl
swipl mystate.sav    # run saved state
```

---

## สรุป
ระบบนิเวศของ Prolog มุ่งเน้นไปที่การเขียนโปรแกรมเชิงตรรกะและการแก้ไขข้อจำกัด การใช้งานมาตรฐานคือ **SWI-Prolog** เป็นที่นิยมมากที่สุด **GNU Prolog** สำหรับการคอมไพล์แบบเนทีฟ และ **Scryer Prolog** เพื่อความสอดคล้องกับ ISO สมัยใหม่ ไลบรารีหลักประกอบด้วย **CLP(FD)** สำหรับการเขียนโปรแกรมแบบจำกัด **http_server** สำหรับบริการบนเว็บ **ODBC** สำหรับฐานข้อมูล และ **plunit** สำหรับการทดสอบ Prolog เป็นเลิศในด้านปัญญาประดิษฐ์ ระบบผู้เชี่ยวชาญ การประมวลผลภาษาธรรมชาติ การพิสูจน์ทฤษฎีบท และความพึงพอใจในข้อจำกัด ระบบนิเวศเป็นสิ่งจำเป็นสำหรับการให้เหตุผลเชิงสัญลักษณ์ การเป็นตัวแทนความรู้ และปัญหาการหาค่าเหมาะที่สุดแบบผสมผสาน