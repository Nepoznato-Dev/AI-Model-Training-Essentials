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
# Prolog - Mfumo wa Mazingira na Mwongozo wa zana
Mwongozo huu unashughulikia zana muhimu, utekelezaji, na miundombinu katika mfumo ikolojia wa Prolog.
---

## Utekelezaji wa Prog
| Utekelezaji | Andika | Vidokezo |
|--------------|------|--------|
| **SWI-Prolog** | Chanzo-wazi | Maarufu zaidi, yenye vipengele vingi |
| **Utangulizi wa GNU** | Chanzo-wazi | Mkusanyiko wa asili |
| **Scryer Prolog** | Chanzo-wazi | Kisasa, kulingana na ISO |
| **Trealla Prolog** | Chanzo-wazi | Haraka, nyepesi |
| **ECLiPSe** | Chanzo-wazi | Upangaji wa mantiki ya kizuizi |
| **SICStus** | Kibiashara | Utendaji wa juu |
| **XSB** | Chanzo-wazi | Kuweka meza, semantiki zenye msingi mzuri |
```bash
swipl --version           # check version
swipl script.pl           # run script
swipl                     # interactive REPL
swipl -g main -t halt script.pl  # run goal
```

---

## Usimamizi wa Kifurushi
| Zana | Kusudi |
|------|----------|
| **SWI-Prolog pakiti** | Kidhibiti kifurushi |
| **Msajili wa Pakiti ya Prolog** | Hifadhi ya kifurushi |
```prolog
% Install pack in SWI-Prolog
?- pack_install(strings).
?- pack_install(http).
?- pack_list.              % list installed
?- pack_upgrade(strings).  % upgrade
```

---

## Wavuti na HTTP
| Maktaba | Kusudi |
|---------|---------|
| **http_unix_daemon** | Daemoni ya seva ya HTTP |
| **http_server** | Seva ya HTTP iliyojengewa ndani |
| **Pengine** | Prog ya Wavuti |
| **ClioPatria** | Mfumo wa wavuti wa kisemantiki |
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

## Hifadhidata na Data
| Teknolojia | Kusudi |
|------------|---------|
| **ODBC** | Muunganisho wa hifadhidata |
| **SQLite** | Hifadhidata iliyopachikwa |
| **Berkeley DB** | Duka la thamani kuu |
| **SGML/XML** | Uchanganuzi wa XML |
| **SGML/RDF** | Mtandao wa kisemantiki |
| **Ukweli wa utangulizi** | Msingi wa maarifa uliojengwa |
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

##Upimaji
| Mfumo | Kusudi |
|-----------|---------|
| **plunit** | Jaribio la kitengo kilichojengewa ndani (SWI) |
| **Angalia Haraka** | Upimaji kulingana na mali |
| **Jaribio la wakati mmoja** | Utekelezaji wa mtihani sambamba |
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

## Upangaji Vikwazo
| Maktaba | Kusudi |
|---------|---------|
| **CLP(FD)** | Vizuizi vya kikoa vilivyokamilika |
| **CLP(B)** | Vikwazo vya Boolean |
| **CLP(QR)** | Vizuizi vya busara |
| **CHR** | Sheria za kushughulikia vikwazo |
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

## Maktaba Muhimu
| Maktaba | Kusudi |
|---------|---------|
| **orodha** | Udanganyifu wa orodha |
| **tuma** | Vihusishi vya mpangilio wa juu |
| **maelezo** | Shughuli za kamusi |
| **mistari** | Ushughulikiaji wa kamba |
| **soketi** | Kuprogramu mtandao |
| **ssl** | TLS/SSL |
| **crypto** | Crystalgraphy |
| **sgml** | Uchanganuzi wa XML/HTML |
| **http/json** | JSON utunzaji |
| **uri** | URI kushughulikia |
| **mchakato** | Usimamizi wa mchakato |
| ** thread** | Nyuzi nyingi |
| **jumla** | Mkusanyiko |
| **kuweka meza** | Kukariri |
---

## Vitambulisho na Vihariri
| ID | Nguvu |
|-----|------------|
| **SWI-Prolog IDE** | IDE iliyojengwa ndani |
| **VS Code + Prolog** | Usaidizi wa lugha |
| **Emacs + prolog-mode** | Classic Prolog mazingira |
---

## Usambazaji
| Mbinu | Vidokezo |
|--------|-------|
| **Inaweza kutekelezeka pekee** | `swipl-ld`au hali iliyohifadhiwa |
| **Docker** | Imewekwa kwenye vyombo |
| **Huduma za wavuti** | Seva ya HTTP |
| **Imepachikwa** | Prog Iliyopachikwa |
```bash
# Create standalone executable
swipl -o myapp -g main -t halt -c script.pl

# Save state
swipl -o mystate.sav -c script.pl
swipl mystate.sav    # run saved state
```

---

## Muhtasari
Mfumo ikolojia wa Prolog umejikita katika upangaji programu wa kimantiki na utatuzi wa vikwazo. Utekelezaji wa kawaida ni: **SWI-Prolog** kama maarufu zaidi, **GNU Prolog** kwa mkusanyo asilia, na **Scryer Prolog** kwa upatanifu wa kisasa wa ISO. Maktaba muhimu ni pamoja na **CLP(FD)** ya kupanga programu, **http_server** kwa huduma za wavuti, **ODBC** ya hifadhidata, na **plunit** ya majaribio. Prologi inabobea katika akili bandia, mifumo ya kitaalam, uchakataji wa lugha asilia, uthibitishaji wa nadharia na utoshelevu wa vikwazo. Mfumo ikolojia ni muhimu kwa hoja za kiishara, uwakilishi wa maarifa, na matatizo ya utoshelezaji wa pamoja.