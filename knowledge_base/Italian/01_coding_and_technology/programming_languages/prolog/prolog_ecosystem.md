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
# Prolog: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, le implementazioni e l'infrastruttura essenziali nell'ecosistema Prolog.
---

## Implementazioni di Prolog
| Attuazione | Digitare | Note |
|-------|------|-------|
| **Prologo SWI** | Open source | Il più popolare, ricco di funzionalità |
| **Prologo GNU** | Open source | Compilazione nativa |
| **Prologo Veggente** | Open source | Moderno, conforme ISO |
| **Prologo Trealla** | Open source | Veloce, leggero |
| **ECLiPSe** | Open source | Programmazione logica a vincoli |
| **SICStus** | Commerciale | Ad alte prestazioni |
| **XSB** | Open source | Tabella, semantica ben fondata |
```bash
swipl --version           # check version
swipl script.pl           # run script
swipl                     # interactive REPL
swipl -g main -t halt script.pl  # run goal
```

---

## Gestione dei pacchetti
| Strumento | Scopo |
|------|---------|
| **Pacchetto SWI-Prolog** | Gestore pacchetti |
| **Registro del pacchetto Prolog** | Repository dei pacchetti |
```prolog
% Install pack in SWI-Prolog
?- pack_install(strings).
?- pack_install(http).
?- pack_list.              % list installed
?- pack_upgrade(strings).  % upgrade
```

---

## Web e HTTP
| Biblioteca | Scopo |
|---------|---------|
| **http_unix_daemon** | Demone del server HTTP |
| **server_http** | Server HTTP integrato |
| **Pengine** | Prologo Web |
| **ClioPatria** | Framework web semantico |
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

## Database e dati
| Tecnologia | Scopo |
|------------|---------|
| **ODBC** | Connettività del database |
| **SQLite** | Database incorporato |
| **BerkeleyDB** | Negozio di valori-chiave |
| **SGML/XML** | Analisi XML |
| **SGML/RDF** | Rete semantica |
| **Fatti del prologo** | Base di conoscenza integrata |
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

## Test
| Quadro | Scopo |
|-----------|---------|
| **plunità** | Test unitari integrati (SWI) |
| **Controllo rapido** | Test basati sulle proprietà |
| **Test simultanei** | Esecuzione di test paralleli |
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

## Programmazione dei vincoli
| Biblioteca | Scopo |
|---------|---------|
| **CLP(FD)** | Vincoli di dominio finito |
| **CLP(B)** | Vincoli booleani |
| **CLP(QR)** | Vincoli razionali |
| **CHR** | Regole di gestione dei vincoli |
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

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **elenchi** | Manipolazione dell'elenco |
| **applica** | Predicati di ordine superiore |
| **detta** | Operazioni sul dizionario |
| **stringhe** | Gestione delle stringhe |
| **prese** | Programmazione di rete |
| **ssl** | TLS/SSL |
| **cripto** | Crittografia |
| **sgml** | Analisi XML/HTML |
| **http/json** | Gestione JSON |
| **uri** | Gestione dell'URI |
| **processo** | Gestione dei processi |
| **discussione** | Multithreading |
| **aggregato** | Aggregazione |
| **tavolatura** | Memoizzazione |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **IDE SWI-Prolog** | IDE integrato |
| **Codice VS + Prologo** | Supporto linguistico |
| **Emacs + modalità prolog** | Ambiente Prolog classico |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Eseguibile autonomo** | `swipl-ld`o stato salvato |
| **Docker** | Containerizzato |
| **Servizi Web** | ServerHTTP |
| **Incorporato** | Prologo incorporato |
```bash
# Create standalone executable
swipl -o myapp -g main -t halt -c script.pl

# Save state
swipl -o mystate.sav -c script.pl
swipl mystate.sav    # run saved state
```

---

## Riepilogo
L'ecosistema di Prolog è incentrato sulla programmazione logica e sulla risoluzione dei vincoli. L'implementazione standard è: **SWI-Prolog** come la più popolare, **GNU Prolog** per la compilazione nativa e **Scryer Prolog** per la moderna conformità ISO. Le librerie di chiavi includono **CLP(FD)** per la programmazione dei vincoli, **http_server** per servizi Web, **ODBC** per database e **plunit** per test. Prolog eccelle nell'intelligenza artificiale, nei sistemi esperti, nell'elaborazione del linguaggio naturale, nella dimostrazione di teoremi e nella soddisfazione dei vincoli. L'ecosistema è essenziale per il ragionamento simbolico, la rappresentazione della conoscenza e i problemi di ottimizzazione combinatoria.