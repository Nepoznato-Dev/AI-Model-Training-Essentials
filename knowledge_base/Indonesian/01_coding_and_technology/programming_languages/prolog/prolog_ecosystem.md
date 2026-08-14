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
# Prolog — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, implementasi, dan infrastruktur penting dalam ekosistem Prolog.
---

## Implementasi Prolog
| Implementasi | Ketik | Catatan |
|---------------|------|-------|
| **SWI-Prolog** | Sumber terbuka | Paling populer, kaya fitur |
| **Prolog GNU** | Sumber terbuka | Kompilasi asli |
| **Prolog Pengikis** | Sumber terbuka | Modern, sesuai ISO |
| **Prolog Treala** | Sumber terbuka | Cepat, ringan |
| **ECLiPSe** | Sumber terbuka | Batasan pemrograman logika |
| **SICStus** | Komersial | Performa tinggi |
| **XSB** | Sumber terbuka | Tabling, semantik yang beralasan |
```bash
swipl --version           # check version
swipl script.pl           # run script
swipl                     # interactive REPL
swipl -g main -t halt script.pl  # run goal
```

---

## Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **Paket SWI-Prolog** | Manajer paket |
| **Registri Paket Prolog** | Repositori paket |
```prolog
% Install pack in SWI-Prolog
?- pack_install(strings).
?- pack_install(http).
?- pack_list.              % list installed
?- pack_upgrade(strings).  % upgrade
```

---

## Web & HTTP
| Perpustakaan | Tujuan |
|---------|---------|
| **http_unix_daemon** | Daemon server HTTP |
| **http_server** | Server HTTP bawaan |
| **Pengine** | Prolog Web |
| **ClioPatria** | Kerangka web semantik |
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

## Basis Data & Data
| Teknologi | Tujuan |
|------------|---------|
| **ODBC** | Konektivitas basis data |
| **SQLite** | Basis data tertanam |
| **Berkeley DB** | Penyimpanan nilai kunci |
| **SGML/XML** | Penguraian XML |
| **SGML/RDF** | Web semantik |
| **Fakta Prolog** | Basis pengetahuan bawaan |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **banyak** | Pengujian unit bawaan (SWI) |
| **Periksa Cepat** | Pengujian berbasis properti |
| **Pengujian serentak** | Eksekusi pengujian paralel |
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

## Pemrograman Kendala
| Perpustakaan | Tujuan |
|---------|---------|
| **CLP(FD)** | Batasan domain terbatas |
| **CLP(B)** | Batasan Boolean |
| **CLP(QR)** | Kendala rasional |
| **CHR** | Aturan penanganan kendala |
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

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **daftar** | Manipulasi daftar |
| **lamar** | Predikat tingkat tinggi |
| **dikte** | Operasi kamus |
| **string** | Penanganan string |
| **soket** | Pemrograman jaringan |
| **ssl** | TLS/SSL |
| **kripto** | Kriptografi |
| **sgml** | Penguraian XML/HTML |
| **http/json** | Penanganan JSON |
| **uri** | Penanganan URI |
| **proses** | Manajemen proses |
| **utas** | Multi-utas |
| **agregat** | Agregasi |
| **penjadwalan** | Memoisasi |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **IDE Prolog SWI** | IDE bawaan |
| **Kode VS + Prolog** | Dukungan bahasa |
| **Emacs + mode prolog** | Lingkungan Prolog Klasik |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Dapat dieksekusi secara mandiri** | `swipl-ld`atau status tersimpan |
| **Buruh pelabuhan** | dalam kontainer |
| **Layanan web** | Server HTTP |
| **Tertanam** | Prolog Tertanam |
```bash
# Create standalone executable
swipl -o myapp -g main -t halt -c script.pl

# Save state
swipl -o mystate.sav -c script.pl
swipl mystate.sav    # run saved state
```

---

## Ringkasan
Ekosistem Prolog berpusat pada pemrograman logika dan penyelesaian kendala. Implementasi standarnya adalah: **SWI-Prolog** sebagai yang paling populer, **GNU Prolog** untuk kompilasi asli, dan **Scryer Prolog** untuk kesesuaian ISO modern. Pustaka utama mencakup **CLP(FD)** untuk pemrograman batasan, **http_server** untuk layanan web, **ODBC** untuk database, dan **plunit** untuk pengujian. Prolog unggul dalam kecerdasan buatan, sistem pakar, pemrosesan bahasa alami, pembuktian teorema, dan kepuasan kendala. Ekosistem sangat penting untuk penalaran simbolik, representasi pengetahuan, dan masalah optimasi kombinatorial.