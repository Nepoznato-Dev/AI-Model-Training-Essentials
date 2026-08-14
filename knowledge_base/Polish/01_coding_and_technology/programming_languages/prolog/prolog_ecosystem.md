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
# Prolog — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, wdrożenia i infrastrukturę w ekosystemie Prolog.
---

## Implementacje Prologu
| Wdrożenie | Wpisz | Notatki |
|--------------|------|-------|
| **SWI-Prolog** | Otwarte oprogramowanie | Najpopularniejszy, bogaty w funkcje |
| **Prolog GNU** | Otwarte oprogramowanie | Natywna kompilacja |
| **Prolog Wróżbity** | Otwarte oprogramowanie | Nowoczesne, zgodne z ISO |
| **Prolog Trealli** | Otwarte oprogramowanie | Szybki, lekki |
| **ECLiPSe** | Otwarte oprogramowanie | Programowanie logiki z ograniczeniami |
| **SICStus** | Komercyjne | Wysoka wydajność |
| **XSB** | Otwarte oprogramowanie | Składanie, dobrze uzasadniona semantyka |
```bash
swipl --version           # check version
swipl script.pl           # run script
swipl                     # interactive REPL
swipl -g main -t halt script.pl  # run goal
```

---

## Zarządzanie pakietami
| Narzędzie | Cel |
|------|-------------|
| **Pakiet SWI-Prolog** | Menedżer pakietów |
| **Rejestr pakietu Prolog** | Repozytorium pakietów |
```prolog
% Install pack in SWI-Prolog
?- pack_install(strings).
?- pack_install(http).
?- pack_list.              % list installed
?- pack_upgrade(strings).  % upgrade
```

---

## Sieć i HTTP
| Biblioteka | Cel |
|--------|---------|
| **http_unix_daemon** | Demon serwera HTTP |
| **serwer_http** | Wbudowany serwer HTTP |
| **Pinginy** | Prolog sieciowy |
| **KlioPatria** | Semantyczny framework sieciowy |
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

## Baza danych i dane
| Technologia | Cel |
|------------|------------|
| **ODBC** | Łączność z bazą danych |
| **SQLite** | Wbudowana baza danych |
| **Berkeley DB** | Magazyn klucz-wartość |
| **SGML/XML** | Analiza XML |
| **SGML/RDF** | Sieć semantyczna |
| **Fakty z prologu** | Wbudowana baza wiedzy |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **plunity** | Wbudowane testy jednostkowe (SWI) |
| **Szybkie sprawdzenie** | Testowanie oparte na właściwościach |
| **Testowanie równoległe** | Równoległe wykonanie testu |
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

## Programowanie z ograniczeniami
| Biblioteka | Cel |
|--------|---------|
| **CLP(FD)** | Ograniczenia domeny skończonej |
| **CLP(B)** | Ograniczenia logiczne |
| **CLP(QR)** | Racjonalne ograniczenia |
| **CHR** | Zasady obsługi ograniczeń |
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

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **listy** | Manipulacja listą |
| **zastosuj** | Predykaty wyższego rzędu |
| **dyktuje** | Operacje słownikowe |
| **stringi** | Obsługa ciągów |
| **gniazda** | Programowanie sieciowe |
| **ssl** | TLS/SSL |
| **krypto** | Kryptografia |
| **sgml** | Analiza XML/HTML |
| **http/json** | Obsługa JSON |
| **uri** | Obsługa URI |
| **proces** | Zarządzanie procesami |
| **wątek** | Wielowątkowość |
| **łącznie** | Agregacja |
| **złożenie** | Zapamiętywanie |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **SWI-Prolog IDE** | Wbudowane IDE |
| **Kod VS + Prolog** | Obsługa języków |
| **Emacs + tryb prologu** | Klasyczne środowisko Prologu |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Samodzielny plik wykonywalny** | `swipl-ld`lub zapisany stan |
| **Doker** | Kontenerowy |
| **Usługi sieciowe** | Serwer HTTP |
| **Wbudowany** | Wbudowany Prolog |
```bash
# Create standalone executable
swipl -o myapp -g main -t halt -c script.pl

# Save state
swipl -o mystate.sav -c script.pl
swipl mystate.sav    # run saved state
```

---

## Streszczenie
Ekosystem Prologu koncentruje się na programowaniu logicznym i rozwiązywaniu ograniczeń. Standardowa implementacja to: **SWI-Prolog** jako najpopularniejszy, **GNU Prolog** do kompilacji natywnej i **Scryer Prolog** do współczesnej zgodności z ISO. Kluczowe biblioteki obejmują **CLP(FD)** do programowania z ograniczeniami, **http_server** do usług internetowych, **ODBC** do baz danych i **plunit** do testowania. Prolog specjalizuje się w sztucznej inteligencji, systemach ekspertowych, przetwarzaniu języka naturalnego, dowodzeniu twierdzeń i spełnianiu ograniczeń. Ekosystem jest niezbędny do symbolicznego rozumowania, reprezentacji wiedzy i problemów optymalizacji kombinatorycznej.