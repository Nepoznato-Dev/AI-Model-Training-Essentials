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
# Prolog: Guía de ecosistemas y herramientas
Esta guía cubre las herramientas, implementaciones e infraestructura esenciales en el ecosistema Prolog.
---

## Implementaciones de prólogo
| Implementación | Tipo | Notas |
|---------------|------|-------|
| **SWI-Prólogo** | Código abierto | Más popular, rico en funciones |
| **Prólogo de GNU** | Código abierto | Compilación nativa |
| **Prólogo del Arúspice** | Código abierto | Moderno, conforme a ISO |
| **Trealla Prólogo** | Código abierto | Rápido, ligero |
| **ECLiPSe** | Código abierto | Programación lógica de restricciones |
| **SICStus** | Comercial | Alto rendimiento |
| **XSB** | Código abierto | Presentación, semántica bien fundada |
```bash
swipl --version           # check version
swipl script.pl           # run script
swipl                     # interactive REPL
swipl -g main -t halt script.pl  # run goal
```

---

## Gestión de paquetes
| Herramienta | Propósito |
|------|---------|
| **Paquete SWI-Prolog** | Administrador de paquetes |
| **Registro del paquete Prolog** | Repositorio de paquetes |
```prolog
% Install pack in SWI-Prolog
?- pack_install(strings).
?- pack_install(http).
?- pack_list.              % list installed
?- pack_upgrade(strings).  % upgrade
```

---

## Web y HTTP
| Biblioteca | Propósito |
|---------|---------|
| **http_unix_daemon** | Demonio del servidor HTTP |
| **servidor_http** | Servidor HTTP incorporado |
| **Pmotores** | Prólogo web |
| **ClioPatria** | Marco web semántico |
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

## Base de datos y datos
| Tecnología | Propósito |
|------------|---------|
| **ODBC** | Conectividad de base de datos |
| **SQLite** | Base de datos integrada |
| **Berkeley DB** | Tienda de valores clave |
| **SGML/XML** | Análisis XML |
| **SGML/RDF** | Web semántica |
| **Datos del prólogo** | Base de conocimientos incorporada |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **plunidad** | Pruebas unitarias integradas (SWI) |
| **Comprobación rápida** | Pruebas basadas en propiedades |
| **Pruebas simultáneas** | Ejecución de pruebas en paralelo |
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

## Programación de restricciones
| Biblioteca | Propósito |
|---------|---------|
| **CLP(FD)** | Restricciones de dominio finito |
| **CLP(B)** | Restricciones booleanas |
| **CLP(QR)** | Restricciones racionales |
| **CDH** | Reglas de manejo de restricciones |
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

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **listas** | Manipulación de listas |
| **aplicar** | Predicados de orden superior |
| **dictados** | Operaciones de diccionario |
| **cadenas** | Manejo de cuerdas |
| **enchufes** | Programación de redes |
| **ssl** | TLS/SSL |
| **cripto** | Criptografía |
| **sgml** | Análisis XML/HTML |
| **http/json** | Manejo de JSON |
| **uri** | Manejo de URI |
| **proceso** | Gestión de procesos |
| **hilo** | Subprocesos múltiples |
| **agregado** | Agregación |
| **presentación** | Memorización |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **SWI-Prolog IDE** | IDE incorporado |
| **Código VS + Prólogo** | Soporte de idiomas |
| **Emacs + modo prólogo** | Entorno clásico de Prolog |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Ejecutable independiente** | `swipl-ld`o estado guardado |
| **Acoplador** | En contenedores |
| **Servicios web** | Servidor HTTP |
| **Integrado** | Prólogo integrado |
```bash
# Create standalone executable
swipl -o myapp -g main -t halt -c script.pl

# Save state
swipl -o mystate.sav -c script.pl
swipl mystate.sav    # run saved state
```

---

## Resumen
El ecosistema de Prolog se centra en la programación lógica y la resolución de restricciones. La implementación estándar es: **SWI-Prolog** como la más popular, **GNU Prolog** para compilación nativa y **Scryer Prolog** para conformidad ISO moderna. Las bibliotecas clave incluyen **CLP(FD)** para programación de restricciones, **http_server** para servicios web, **ODBC** para bases de datos y **plunit** para pruebas. Prolog destaca en inteligencia artificial, sistemas expertos, procesamiento del lenguaje natural, demostración de teoremas y satisfacción de restricciones. El ecosistema es esencial para el razonamiento simbólico, la representación del conocimiento y los problemas de optimización combinatoria.