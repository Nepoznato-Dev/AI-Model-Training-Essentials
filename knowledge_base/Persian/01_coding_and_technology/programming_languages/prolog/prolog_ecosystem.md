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
# Prolog - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، پیاده سازی ها و زیرساخت های ضروری در اکوسیستم Prolog را پوشش می دهد.
---

## پیاده سازی Prolog
| پیاده سازی | نوع | یادداشت ها |
|---------------|------|-------|
| **SWI-Prolog** | منبع باز | محبوب ترین، با ویژگی های غنی |
| **GNU Prolog** | منبع باز | تالیف بومی |
| **Scryer Prolog** | منبع باز | مدرن، مطابق با ISO |
| **Trealla Prolog** | منبع باز | سریع، سبک |
| **ECLiPSe** | منبع باز | برنامه نویسی منطق محدودیت |
| **SICStus** | تجاری | کارایی بالا |
| **XSB** | منبع باز | جدول بندی، معناشناسی مستدل |
```bash
swipl --version           # check version
swipl script.pl           # run script
swipl                     # interactive REPL
swipl -g main -t halt script.pl  # run goal
```

---

## مدیریت بسته
| ابزار | هدف |
|------|---------|
| **پک SWI-Prolog** | مدیر بسته |
| **رجیستری پک پرولوگ** | مخزن بسته |
```prolog
% Install pack in SWI-Prolog
?- pack_install(strings).
?- pack_install(http).
?- pack_list.              % list installed
?- pack_upgrade(strings).  % upgrade
```

---

## وب و HTTP
| کتابخانه | هدف |
|---------|---------|
| **http_unix_daemon** | دیمون سرور HTTP |
| **http_server** | سرور HTTP داخلی |
| **پنژین** | وب پرولوگ |
| **ClioPatria** | چارچوب وب معنایی |
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

## پایگاه داده و داده ها
| فناوری | هدف |
|------------|---------|
| **ODBC** | اتصال به پایگاه داده |
| **SQLite** | پایگاه داده تعبیه شده |
| **برکلی دی بی** | فروشگاه کلید ارزش |
| **SGML/XML** | تجزیه XML |
| **SGML/RDF** | وب معنایی |
| **حقایق پرولوگ** | پایگاه دانش داخلی |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **پلونیت** | تست واحد داخلی (SWI) |
| **بررسی سریع** | تست مبتنی بر اموال |
| **تست همزمان** | اجرای تست موازی |
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

## برنامه نویسی محدودیت
| کتابخانه | هدف |
|---------|---------|
| **CLP(FD)** | محدودیت دامنه محدود |
| **CLP(B)** | محدودیت های بولی |
| **CLP(QR)** | قیود منطقی |
| **CHR** | قوانین رسیدگی به محدودیت |
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

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **لیست** | دستکاری فهرست |
| **اعمال** | محمولات مرتبه بالاتر |
| **دکتر** | عملیات فرهنگ لغت |
| **رشته** | هندلینگ رشته |
| **پریز** | برنامه نویسی شبکه |
| **ssl** | TLS/SSL |
| **کریپتو** | رمزنگاری |
| **sgml** | تجزیه XML/HTML |
| **http/json** | مدیریت JSON |
| **وری** | مدیریت URI |
| **فرایند** | مدیریت فرآیند |
| **رشته** | چند رشته ای |
| **مجموعه** | تجمع |
| **جدول** | حفظ کردن |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **SWI-Prolog IDE** | IDE داخلی |
| **VS Code + Prolog** | پشتیبانی زبان |
| **Emacs + prolog-mode** | محیط کلاسیک پرولوگ |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **قابل اجرا مستقل** | `swipl-ld`یا حالت ذخیره شده |
| **داکر** | کانتینری |
| **خدمات وب** | سرور HTTP |
| **جاسازی شده** | Embedded Prolog |
```bash
# Create standalone executable
swipl -o myapp -g main -t halt -c script.pl

# Save state
swipl -o mystate.sav -c script.pl
swipl mystate.sav    # run saved state
```

---

## خلاصه
اکوسیستم پرولوگ بر برنامه ریزی منطقی و حل محدودیت متمرکز است. پیاده سازی استاندارد عبارت است از: **SWI-Prolog** به عنوان محبوب ترین، **GNU Prolog** برای کامپایل بومی و **Scryer Prolog** برای انطباق ISO مدرن. کتابخانه های کلیدی شامل **CLP(FD)** برای برنامه نویسی محدودیت، **http_server** برای سرویس های وب، **ODBC** برای پایگاه های داده و **plunit** برای تست می باشد. Prolog در هوش مصنوعی، سیستم های خبره، پردازش زبان طبیعی، اثبات قضیه و رضایت از محدودیت ها برتر است. اکوسیستم برای استدلال نمادین، بازنمایی دانش و مسائل بهینه سازی ترکیبی ضروری است.