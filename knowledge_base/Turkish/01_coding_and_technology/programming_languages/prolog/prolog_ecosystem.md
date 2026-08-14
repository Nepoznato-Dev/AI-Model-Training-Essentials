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
# Prolog — Ekosistem ve Araç İşleme Kılavuzu
Bu kılavuz Prolog ekosistemindeki temel araçları, uygulamaları ve altyapıyı kapsar.
---

## Prolog Uygulamaları
| Uygulama | Tür | Notlar |
|---------------|----------|----------|
| **SWI-Prolog** | Açık kaynak | En popüler, zengin özelliklere sahip |
| **GNU Prolog** | Açık kaynak | Yerel derleme |
| **Scryer Prolog** | Açık kaynak | Modern, ISO uyumlu |
| **Trealla Prolog** | Açık kaynak | Hızlı, hafif |
| **ECLiPSe** | Açık kaynak | Kısıtlama mantığı programlama |
| **SICStus** | Ticari | Yüksek performanslı |
| **XSB** | Açık kaynak | Tablolama, sağlam temellere dayanan anlambilim |
```bash
swipl --version           # check version
swipl script.pl           # run script
swipl                     # interactive REPL
swipl -g main -t halt script.pl  # run goal
```

---

## Paket Yönetimi
| Araç | Amaç |
|------|------------|
| **SWI-Prolog paketi** | Paket yöneticisi |
| **Prolog Paketi Kayıt Defteri** | Paket deposu |
```prolog
% Install pack in SWI-Prolog
?- pack_install(strings).
?- pack_install(http).
?- pack_list.              % list installed
?- pack_upgrade(strings).  % upgrade
```

---

## Web ve HTTP
| Kütüphane | Amaç |
|-----------|-----------|
| **http_unix_daemon** | HTTP sunucusu arka plan programı |
| **http_sunucu** | Yerleşik HTTP sunucusu |
| **Penginler** | Web Girişi |
| **ClioPatria** | Anlamsal web çerçevesi |
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

## Veritabanı ve Veri
| Teknoloji | Amaç |
|---------------|-----------|
| **ODBC** | Veritabanı bağlantısı |
| **SQLite** | Gömülü veritabanı |
| **Berkeley DB** | Anahtar/değer deposu |
| **SGML/XML** | XML ayrıştırma |
| **SGML/RDF** | Anlamsal web |
| **Giriş gerçekleri** | Yerleşik bilgi tabanı |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **birim** | Yerleşik birim testi (SWI) |
| **Hızlı Kontrol** | Mülkiyet bazlı testler |
| **Eşzamanlı test** | Paralel test yürütme |
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

## Kısıtlama Programlama
| Kütüphane | Amaç |
|-----------|-----------|
| **CLP(FD)** | Sonlu etki alanı kısıtlamaları |
| **CLP(B)** | Boole kısıtlamaları |
| **CLP(QR)** | Rasyonel kısıtlamalar |
| **CHR** | Kısıtlama işleme kuralları |
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

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **listeler** | Liste manipülasyonu |
| **uygula** | Yüksek dereceli yüklemler |
| **sözler** | Sözlük işlemleri |
| **dizeler** | Dize işleme |
| **soketler** | Ağ programlama |
| **ssl** | TLS/SSL |
| **kripto** | Kriptografi |
| **sgml** | XML/HTML ayrıştırma |
| **http/json** | JSON işleme |
| **uri** | URI işleme |
| **süreç** | Süreç yönetimi |
| **konu** | Çoklu iş parçacıklı |
| **toplam** | Toplama |
| **tablolama** | Notlandırma |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **SWI-Prolog IDE** | Yerleşik IDE |
| **VS Kodu + Prolog** | Dil desteği |
| **Emacs + prolog modu** | Klasik Prolog ortamı |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Bağımsız çalıştırılabilir** | `swipl-ld`veya kayıtlı durum |
| **Docker** | Konteynerde |
| **Web hizmetleri** | HTTP sunucusu |
| **Gömülü** | Gömülü Prolog |
```bash
# Create standalone executable
swipl -o myapp -g main -t halt -c script.pl

# Save state
swipl -o mystate.sav -c script.pl
swipl mystate.sav    # run saved state
```

---

## Özet
Prolog'un ekosistemi mantıksal programlama ve kısıtlama çözmeye odaklanmıştır. Standart uygulama şu şekildedir: En popüler olarak **SWI-Prolog**, yerel derleme için **GNU Prolog** ve modern ISO uyumluluğu için **Scryer Prolog**. Anahtar kitaplıklar arasında kısıtlama programlama için **CLP(FD)**, web hizmetleri için **http_server**, veritabanları için **ODBC** ve test için **plunit** yer alır. Prolog yapay zeka, uzman sistemler, doğal dil işleme, teorem kanıtlama ve kısıtlama tatmini konularında üstündür. Ekosistem sembolik akıl yürütme, bilgi temsili ve kombinatoryal optimizasyon problemleri için gereklidir.