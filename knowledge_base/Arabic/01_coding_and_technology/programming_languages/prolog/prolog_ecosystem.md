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
# Prolog - دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والتطبيقات والبنية التحتية الأساسية في نظام Prolog البيئي.
---

## تطبيقات البرولوج
| التنفيذ | اكتب | ملاحظات |
|---------------|------|-------|
| **SWI-Prolog** | مفتوح المصدر | الأكثر شعبية وغنية بالميزات |
| **مقدمة جنو** | مفتوح المصدر | التجميع الأصلي |
| ** برولوج سكراير ** | مفتوح المصدر | حديثة ومتوافقة مع ISO |
| **مقدمة تريلا** | مفتوح المصدر | سريع وخفيف الوزن |
| **ECLiPSe** | مفتوح المصدر | برمجة منطق القيد |
| **سيكستوس** | تجاري | عالية الأداء |
| **XSB** | مفتوح المصدر | الجدولة، دلالات راسخة |
```bash
swipl --version           # check version
swipl script.pl           # run script
swipl                     # interactive REPL
swipl -g main -t halt script.pl  # run goal
```

---

## إدارة الحزم
| أداة | الغرض |
|------|---------|
| **حزمة SWI-Prolog** | مدير الحزم |
| ** تسجيل حزمة Prolog ** | مستودع الحزمة |
```prolog
% Install pack in SWI-Prolog
?- pack_install(strings).
?- pack_install(http).
?- pack_list.              % list installed
?- pack_upgrade(strings).  % upgrade
```

---

## الويب وHTTP
| مكتبة | الغرض |
|---------|--------|
| **http_unix_daemon** | خادم HTTP الخفي |
| **http_server** | خادم HTTP مدمج |
| **بينجينز** | برولوج الويب |
| **كليوباتريا** | إطار الويب الدلالي |
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

## قاعدة البيانات والبيانات
| تكنولوجيا | الغرض |
|------------|---------|
| **ODBC** | اتصال قاعدة البيانات |
| ** سكليتي ** | قاعدة البيانات المدمجة |
| ** بيركلي دي بي ** | متجر القيمة الرئيسية |
| **SGML/XML** | تحليل XML |
| **SGML/RDF** | الويب الدلالي |
| **حقائق برولوج** | قاعدة المعرفة المضمنة |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **بلونيت** | اختبار الوحدة المدمجة (SWI) |
| **فحص سريع** | الاختبار على أساس الملكية |
| **الاختبار المتزامن** | تنفيذ الاختبار الموازي |
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

## برمجة القيد
| مكتبة | الغرض |
|---------|--------|
| **CLP(FD)** | قيود المجال المحدودة |
| **CLP(ب)** | القيود المنطقية |
| **CLP(QR)** | القيود العقلانية |
| ** لجنة حقوق الإنسان ** | قواعد التعامل مع القيد |
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

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **القوائم** | التلاعب بالقائمة |
| **تطبيق** | المسندات ذات الترتيب الأعلى |
| **الإملاء** | عمليات القاموس |
| **سلاسل** | التعامل مع السلسلة |
| **المآخذ** | برمجة الشبكات |
| **سل** | TLS/SSL |
| **التشفير** | التشفير |
| **سجمل** | تحليل XML/HTML |
| **http/json** | التعامل مع JSON |
| **يوري** | التعامل مع URI |
| **العملية** | إدارة العمليات |
| **الموضوع** | متعدد الخيوط |
| **المجموع** | التجميع |
| **الجدولة** | الحفظ |
---

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **SWI-Prolog IDE** | بيئة تطوير متكاملة مدمجة |
| **رمز VS + Prolog** | دعم اللغة |
| **إيماكس + وضع البرولوج** | بيئة برولوج الكلاسيكية |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| ** مستقل قابل للتنفيذ ** | `swipl-ld`أو الحالة المحفوظة |
| ** عامل الميناء ** | في حاويات |
| **خدمات الويب** | خادم HTTP |
| **مضمن** | برولوج مضمن |
```bash
# Create standalone executable
swipl -o myapp -g main -t halt -c script.pl

# Save state
swipl -o mystate.sav -c script.pl
swipl mystate.sav    # run saved state
```

---

## ملخص
يتمحور النظام البيئي لـ Prolog حول البرمجة المنطقية وحل القيود. التنفيذ القياسي هو: **SWI-Prolog** باعتباره الأكثر شيوعًا، و**GNU Prolog** للتجميع الأصلي، و**Scryer Prolog** للتوافق الحديث مع ISO. تتضمن المكتبات الرئيسية **CLP(FD)** لبرمجة القيود، و**http_server** لخدمات الويب، و**ODBC** لقواعد البيانات، و**plunit** للاختبار. يتفوق Prolog في الذكاء الاصطناعي، والأنظمة المتخصصة، ومعالجة اللغة الطبيعية، وإثبات النظرية، والرضا عن القيود. يعد النظام البيئي ضروريًا للتفكير الرمزي وتمثيل المعرفة ومشاكل التحسين التوافقي.