<!--
---
# Metadata
title: "Prolog"
description: "Comprehensive reference for the Prolog programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prolog, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
#prolog
Prolog (Pemrograman dalam Logika) adalah bahasa pemrograman logika yang dibuat pada tahun 1972 oleh Alain Colmerauer dan Philippe Roussel. Tidak seperti bahasa lain dalam daftar ini, Prolog tidak memberi tahu komputer *bagaimana* memecahkan suatu masalah — Anda menyatakan *apa* yang benar (fakta dan aturan), dan mesin inferensi Prolog mencari jawabannya melalui deduksi logis.
Prolog adalah bahasa pilihan untuk sistem pakar, pemrosesan bahasa alami, dan penelitian AI pada tahun 1980an. Ini mendukung proyek Sistem Komputer Generasi Kelima Jepang dan digunakan di Watson IBM untuk pemahaman bahasa alami. Saat ini, Prolog digunakan dalam penyelesaian kendala, penjadwalan, inferensi tipe, penalaran hukum, dan masalah apa pun yang secara alami dinyatakan sebagai hubungan logis.
**Constraint Logic Programming (CLP)** memperluas Prolog dengan pemecah kendala untuk penjadwalan, perutean, dan alokasi sumber daya — masalah yang sangat sulit dalam bahasa imperatif.
---

## Mengapa Prolog Penting
- **Pemrograman deklaratif**: Jelaskan apa yang benar, bukan cara menghitungnya. Mesin melakukan pekerjaannya.
- **Pencocokan dan penyatuan pola**: Algoritme penyatuan Prolog lebih canggih dibandingkan pencocokan pola dalam bahasa lain.
- **Penelusuran mundur**: Secara otomatis mengeksplorasi semua kemungkinan solusi. Tidak diperlukan algoritma pencarian manual.
- **Wajar untuk masalah logika**: Sistem pakar, mesin aturan, pemeriksa tipe, pengurai tata bahasa — semuanya dipetakan langsung ke Prolog.
- **Pemecahan kendala**: CLP(FD) memecahkan masalah penjadwalan, alokasi, dan kombinatorial dengan elegan.
- **Pemikiran berbeda**: Prolog Pembelajaran mengubah cara Anda mendekati pemecahan masalah — Anda mulai berpikir dalam hubungan dan batasan.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Paradigma yang sangat berbeda** | Tanpa variabel (hanya binding), tanpa loop, tanpa penugasan | Berpikirlah dalam hubungan dan rekursi, bukan perubahan keadaan |
| **Kinerja** | Lambat untuk komputasi numerik dan data besar | Gunakan untuk alasan; mendelegasikan komputasi ke C/bahasa lain |
| **Kesulitan melakukan debug** | Sulit untuk melacak kemunduran dan kegagalan penyatuan | Gunakan alat penelusuran/debug; tulis predikat deterministik |
| **Potong operator (!)** | Dibutuhkan untuk efisiensi tetapi merusak kemurnian logis | Gunakan evaluasi if-then-else atau tabel jika memungkinkan |
| **Ekosistem terbatas** | Sedikit perpustakaan, kerangka kerja, atau sumber daya komunitas | SWI-Prolog merupakan implementasi terlengkap |
| **Bukan untuk aplikasi umum** | Web, seluler, GUI — bukan kekuatan Prolog | Gunakan sebagai mesin penalaran di balik aplikasi web |
---

## Dasar Sintaks
```prolog
% Facts (things that are true)
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).

male(tom).
male(bob).
female(liz).
female(ann).
female(pat).

% Rules (logical implications)
father(X, Y) :- parent(X, Y), male(X).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Recursion
my_length([], 0).
my_length([_|Tail], N) :-
    my_length(Tail, N1),
    N is N1 + 1.

% List processing
my_append([], L, L).
my_append([H|T1], L2, [H|T3]) :-
    my_append(T1, L2, T3).

my_member(X, [X|_]).
my_member(X, [_|Tail]) :- my_member(X, Tail).

% Negation as failure
dislikes(X, Y) :- \+ likes(X, Y).

% Cut (commit to choices)
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).

% Constraint Logic Programming
:- use_module(library(clpfd)).
solve_sudoku(Rows) :-
    append(Rows, Vs), Vs ins 1..9,
    maplist(all_different, Rows),
    columns(Rows, Cols),
    maplist(all_different, Cols),
    maplist(label, Rows).
```

---

## Sintaks & Pola Tingkat Lanjut
### Penyelaman Mendalam Unifikasi
Unifikasi adalah mekanisme inti Prolog — ini adalah cara Prolog "mencocokkan" istilah dan mengikat variabel.
```prolog
% Unification rules:
% 1. Two constants unify if they are identical
%    ?- hello = hello.     -> true
%    ?- hello = world.     -> false
%
% 2. A variable unifies with anything (binding)
%    ?- X = hello.         -> X = hello
%    ?- X = Y.             -> X = Y (shared variable)
%
% 3. Complex terms unify if functors match and all args unify
%    ?- f(X, b) = f(a, Y). -> X = a, Y = b
%    ?- f(a, b) = f(a, c). -> false
%
% 4. Lists unify element by element
%    ?- [H|T] = [1, 2, 3]. -> H = 1, T = [2, 3]

% The == operator (structural equality, no binding)
% ?- X == X.      -> true
% ?- X == Y.      -> false (different variables)
% ?- X = Y, X == Y. -> true (after unification)
```

### Mundur dan Poin Pilihan
```prolog
% Prolog creates choice points when multiple clauses can match
perm([], []).
perm(L, [H|T]) :-
    select(H, L, Rest),
    perm(Rest, T).

% ?- perm([1,2,3], P).
% P = [1,2,3] ; P = [1,3,2] ; P = [2,1,3] ; ...

% Collecting all solutions
?- findall(X, member(X, [1,2,3,4,5]), All).
% All = [1, 2, 3, 4, 5]

?- bagof(X, parent(Y, X), Children).
% Y = tom, Children = [bob, liz] ;
% Y = bob, Children = [ann, pat].

% Cut operator — prevents backtracking
classify(X, positive) :- X > 0, !.
classify(X, negative) :- X < 0, !.
classify(0, zero).
```

### Tata Bahasa Klausul Pasti (DCG)
```prolog
% Simple sentence parser
sentence --> noun_phrase, verb_phrase.
noun_phrase --> determiner, noun.
verb_phrase --> verb.
verb_phrase --> verb, noun_phrase.

determiner --> [the].
determiner --> [a].
noun --> [cat].
noun --> [dog].
noun --> [mouse].
verb --> [chased].
verb --> [ate].

% ?- phrase(sentence, [the, cat, chased, the, mouse]).
% true

% DCG with parse tree construction
sentence(s(NP, VP)) --> noun_phrase(NP), verb_phrase(VP).
noun_phrase(np(Det, N)) --> determiner(Det), noun(N).
verb_phrase(vp(V, NP)) --> verb(V), noun_phrase(NP).
verb_phrase(vp(V)) --> verb(V).

determiner(det(the)) --> [the].
noun(noun(cat)) --> [cat].
verb(verb(chased)) --> [chased].
```

### Pemrograman Logika Kendala (CLP)
```prolog
:- use_module(library(clpfd)).

% SEND + MORE = MONEY puzzle
send_more_money([S,E,N,D,M,O,R,Y]) :-
    Vars = [S,E,N,D,M,O,R,Y],
    Vars ins 0..9,
    all_different(Vars),
    S #> 0, M #> 0,
      S*1000 + E*100 + N*10 + D
    + M*1000 + O*100 + R*10 + E
    #= M*10000 + O*1000 + N*100 + E*10 + Y,
    label(Vars).

% N-Queens problem
n_queens(N, Qs) :-
    length(Qs, N),
    Qs ins 1..N,
    all_different(Qs),
    safe_queens(Qs),
    label(Qs).

safe_queens([]).
safe_queens([Q|Qs]) :-
    no_attack(Q, Qs, 1),
    safe_queens(Qs).

no_attack(_, [], _).
no_attack(Q, [Q1|Qs], D) :-
    Q #\= Q1 + D,
    Q #\= Q1 - D,
    D1 is D + 1,
    no_attack(Q, Qs, D1).
```

---

## Arsitektur & Desain Sistem
### Paradigma Pemrograman Logika
```
+---------------------------------------------+
|              Prolog Program                  |
+---------------------------------------------+
|  Facts:     parent(tom, bob).                |
|             color(red).                      |
+---------------------------------------------+
|  Rules:     grandparent(X, Z) :-             |
|               parent(X, Y), parent(Y, Z).    |
+---------------------------------------------+
|  Queries:   ?- grandparent(tom, X).          |
|             -> X = ann ; X = pat.            |
+---------------------------------------------+
```

### Struktur Proyek Khas
```
prolog-project/
├── src/
│   ├── main.pl              * Entry point
│   ├── rules.pl             * Domain rules
│   ├── facts.pl             * Knowledge base
│   ├── utils.pl             * Utility predicates
│   └── grammar.pl           * DCG definitions
├── tests/
│   ├── test_rules.pl        * Unit tests
│   └── test_grammar.pl      * Grammar tests
├── data/
│   └── knowledge_base.pl    * Fact database
├── Makefile
└── README.md
```

### Sistem Modul
```prolog
:- module(validator, [
    validate_user/2,
    validate_email/1,
    check_password/1
]).

% Private predicate
is_valid_length(Str, Min, Max) :-
    string_length(Str, Len),
    Len >= Min, Len =< Max.

% Public predicates
validate_user(User, Errors) :-
    findall(Error, validate_field(User, Error), Errors).

validate_field(user(Name, Email, _), Error) :-
    \+ is_valid_length(Name, 2, 50),
    Error = 'Name must be 2-50 characters'.
validate_field(user(_, Email, _), Error) :-
    \+ validate_email(Email),
    Error = 'Invalid email format'.

validate_email(Email) :-
    atom_string(Email, Str),
    sub_string(Str, _, _, _, @).
```
---

## Konfigurasi Proyek & Sistem Pembangunan
### Konfigurasi SWI-Prolog
```prolog
:- set_prolog_flag(verbose, silent).
:- set_prolog_stack(global, limit(2*10**9)).

:- use_module(library(clpfd)).
:- use_module(library(lists)).
:- use_module(library(apply)).

:- dynamic fact_cache/2.

:- table fibonacci/2.
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, F) :-
    N > 1, N1 is N - 1, N2 is N - 2,
    fibonacci(N1, F1), fibonacci(N2, F2),
    F is F1 + F2.
```

### Menjalankan Program Prolog
```bash
# Interactive mode
swipl
?- [main].
?- halt.

# Run query from command line
swipl -g "solve(X), write(X), nl, halt" -s main.pl

# Compile to standalone executable
swipl -o solver -g main -c main.pl

# Run tests
swipl -g "run_tests, halt" -s tests/test_rules.pl
```

### Konfigurasi Bangun
```makefile
SWIPL    = swipl
TARGET   = solver
SOURCES  = src/main.pl src/rules.pl src/utils.pl

$(TARGET): $(SOURCES)
	$(SWIPL) -o $(TARGET) -g main -c $(SOURCES)

test:
	$(SWIPL) -g "run_tests, halt" -s tests/test_rules.pl

run:
	$(SWIPL) -s src/main.pl

clean:
	rm -f $(TARGET)

.PHONY: test run clean
```

---

## Pengujian & Debugging
### Pelacakan Bawaan
```prolog
?- trace.
?- grandparent(tom, X).
[trace]  Call: (10) grandparent(tom, _1234)
[trace]  Call: (11) parent(tom, _1256)
[trace]  Exit: (11) parent(tom, bob)
[trace]  Exit: (10) grandparent(tom, ann)
X = ann.
?- notrace.

?- spy parent/2.
?- nospy parent/2.
```

### Pengujian Unit dengan PLUnit
```prolog
:- begin_tests(family).

test(father_basic) :-
    father(tom, bob),
    \+ father(liz, bob).

test(grandparent, set(X == [ann, pat])) :-
    findall(X, grandparent(tom, X), Xs),
    member(X, Xs).

test(list_length) :-
    my_length([], 0),
    my_length([a], 1),
    my_length([1,2,3,4], 4).

:- end_tests(family).
```

### Pola Debugging Umum
| Masalah | Gejala | Solusi |
|---------|---------|----------|
| Rekursi tak terbatas | Tumpukan meluap | Periksa casing dasar; tambahkan kondisi penghentian |
| Tidak ada solusi | Kueri mengembalikan false | Periksa urutan instantiasi variabel |
| Terlalu banyak solusi | Duplikat tak terduga | Tambahkan cut (!) atau gunakan`setof`|
| Penyatuan yang salah | Variabel terikat secara tidak benar | Gunakan`=`untuk menguji; periksa fungsi arity |
| Masalah kinerja | Eksekusi lambat | Tambahkan potongan; gunakan`table`; periksa poin pilihan |
---

## Interoperabilitas
### Antarmuka C (FFI)
```c
/* fast_math.c */
#include <SWI-Prolog.h>
static foreign_t pl_fast_add(term_t A, term_t B, term_t Result) {
    long a, b;
    if (PL_get_long(A, &a) && PL_get_long(B, &b))
        return PL_unify_long(Result, a + b);
    return FALSE;
}
install_t install_fast_math() {
    PL_register_foreign("fast_add", 3, pl_fast_add, 0);
}
```

```prolog
:- load_foreign_library(fast_math).
```

### Integrasi Python
```prolog
:- use_module(library(unix)).
call_python(Expression, Result) :-
    process_create(path(python3),
        ['-c', atom_concat('print(', Expression, Cmd))],
        [stdout(pipe(Out))]),
    read_line_to_codes(Out, Codes),
    close(Out), number_codes(Result, Codes).
```

---

## Pola Desain
### Pola 1: Akumulator (Rekursi Ekor)```prolog
acc_length(List, Length) :- acc_length(List, 0, Length).
acc_length([], Acc, Acc).
acc_length([_|T], Acc, Length) :-
    Acc1 is Acc + 1, acc_length(T, Acc1, Length).
```

### Pola 2: Status Threading```prolog
count_matching(_, [], Count, Count).
count_matching(Pred, [H|T], Acc, Count) :-
    (call(Pred, H) -> Acc1 is Acc + 1, count_matching(Pred, T, Acc1, Count)
    ; count_matching(Pred, T, Acc, Count)).
count_matching(Pred, List, Count) :- count_matching(Pred, List, 0, Count).
```

### Pola 3: Hasilkan dan Uji```prolog
pythagorean_triple(N, Triple) :-
    between(1, N, A), between(A, N, B), between(B, N, C),
    C*C =:= A*A + B*B, Triple = (A, B, C).
```

### Pola 4: Daftar Perbedaan```prolog
dlist_append(Front1-Back1, _Front2-Back2, Front1-Back2) :- Back1 = Front2.
to_dlist(L, L-[]).
```

---

## Kinerja & Optimasi
### Potong Optimasi
```prolog
% WITHOUT cut — explores unnecessary alternatives
member_slow(X, [X|_]).
member_slow(X, [_|T]) :- member_slow(X, T).

% WITH green cut — once found, stop searching
member_cut(X, [X|_]) :- !.
member_cut(X, [_|T]) :- member_cut(X, T).
```

### Rekursi Ekor
```prolog
% GOOD: Tail-recursive factorial
factorial_tr(N, F) :- factorial_acc(N, 1, F).
factorial_acc(0, Acc, Acc).
factorial_acc(N, Acc, F) :-
    N > 0, Acc1 is Acc * N, N1 is N - 1,
    factorial_acc(N1, Acc1, F).
```

### Daftar Periksa Pengoptimalan
| Teknik | Dampak | Deskripsi |
|-----------|--------|-------------|
| **Rekursi ekor** | Tinggi | Gunakan akumulator untuk ruang tumpukan yang konstan |
| **Potong (hijau)** | Tinggi | Hilangkan poin pilihan yang tidak perlu |
| **Evaluasi yang disajikan** | Tinggi | `:- table pred/N`mengingat hasil |
| **Pengindeksan** | Sedang | Tempatkan argumen yang membeda-bedakan terlebih dahulu |
| **Daftar perbedaan** | Sedang | O(1) rangkaian daftar |
| **CLP(FD) melalui pengujian hasil** | Sangat Tinggi | Gunakan batasan alih-alih kekerasan |
---

## Penerapan & Penggunaan di Dunia Nyata
### Men-deploy Aplikasi Prolog
```bash
# Compile to standalone executable
swipl -o myapp -g main -c main.pl

# Create a saved state
swipl -g main -o myapp.sav -c main.pl
```

### Aplikasi Dunia Nyata
| Domain | Bagaimana Prolog Digunakan | Contoh |
|--------|-------------------|---------|
| **Sistem pakar** | Diagnosis medis, deteksi kesalahan | MYCIN, XCON |
| **NLP** | Penguraian tata bahasa, analisis semantik | Chatbots, sistem QA |
| **Ketik inferensi** | Pemeriksaan tipe Hindley-Milner | Prototipe Haskell/ML |
| **Penjadwalan** | Penjadwalan karyawan, penjadwalan | Penjadwalan kru maskapai penerbangan |
| **Penalaran hukum** | Analisis Hukum Berbasis Aturan | Pemeriksaan kepatuhan |
| **Permintaan basis data** | Datalog untuk analisis data | Mesin souffle |
| **Verifikasi** | Pemeriksaan model | Verifikasi perangkat keras |
| **IBM Watson** | Pemahaman bahasa alami | Bahaya! sistem |
| **Ericsson** | Manajemen telekomunikasi | Validasi konfigurasi jaringan |
---

## Kapan Menggunakan Prolog
| Skenario | Mengapa Prolog | Alternatif Lebih Baik |
|----------|-----------|-------------------|
| Penalaran berbasis aturan | Prolog dibuat untuk ini | Mesin aturan khusus dengan Python/Java |
| Batasan kepuasan | CLP(FD) elegan dan efisien | Pemecah SAT, Alat OR untuk instance besar |
| Penguraian tata bahasa / bahasa | DCG (Tata Bahasa Klausul Pasti) adalah asli | Generator parser (ANTLR, yacc) untuk produksi |
| Sistem pakar | Kesesuaian alami — fakta + aturan = sistem pakar | Mesin aturan bisnis (Mengiler) |
| Penjadwalan / penjadwalan | CLP menyelesaikan ini dengan baik | ATAU-Alat, OptaPlanner |
| Ketik penelitian sistem | Unifikasi adalah fondasinya | Implementasikan di OCaml, Haskell, Rust |
| Aplikasi web | Tidak cocok | Python, Node.js, Buka |
| Ilmu data / ML | Bukan ekosistem | Piton, R |
| Kode yang kritis terhadap kinerja | Prolog lambat untuk komputasi | C, C++, Karat |
| Pemrograman tujuan umum | Mungkin tapi canggung | Python, Buka, Java |
---

## Tanya Jawab Sintetis
### Q1: Apa perbedaan penyatuan Prolog dengan tugas dalam bahasa lain?
**A:** Penyatuan adalah pencocokan pola dua arah, bukan penugasan:
```prolog
% Unification (=) tries to make both sides equal
X = 5.              % X is now 5
5 = X.              % same thing — X is 5
f(X, b) = f(a, Y).  % X = a, Y = b

% Once bound, a variable cannot change (in the same scope)
X = 1, X = 2.      % FAILS — X is already 1

% Anonymous variable _ matches anything
f(a, _) = f(a, b).  % true — _ matches b
```

### Q2: Bagaimana cara kerja backtracking di Prolog?
**A:** Saat sasaran gagal, Prolog mundur ke titik pilihan terakhir dan mencoba alternatif berikutnya:
```prolog
% Multiple rules create choice points
color(red). color(green). color(blue).

?- color(X).        % X = red ; X = green ; X = blue ; false.

% Cut (!) prevents backtracking
max(X, Y, X) :- X >= Y, !.
max(_, Y, Y).
% Without cut, max(3, 5, Z) would also try the first rule and fail
```

### Q3: Bagaimana cara bekerja dengan daftar di Prolog?
**A:** Daftar menggunakan pencocokan pola kepala/ekor:
```prolog
% Pattern matching on lists
[X|Xs] = [1, 2, 3].  % X = 1, Xs = [2, 3]

% Common list predicates
my_length([], 0).
my_length([_|T], N) :- my_length(T, N1), N is N1 + 1.

my_append([], L, L).
my_append([H|T], L, [H|R]) :- my_append(T, L, R).

my_member(X, [X|_]).
my_member(X, [_|T]) :- my_member(X, T).
```

### Q4: Kapan sebaiknya saya menggunakan Prolog dibandingkan bahasa lain?
**A:** Prolog unggul dalam:
- Kendala kepuasan (penjadwalan, teka-teki)
- Sistem berbasis aturan (sistem pakar, validasi)
- Grafik/penjelajahan pohon
- Pemrosesan bahasa alami
- Perhitungan simbolis
- Masalah apa pun dapat diungkapkan sebagai hubungan logis
### Q5: Apa kendala umum di Prolog?
**J:** Masalah utama:
- Rekursi tak terbatas — selalu utamakan kasus dasar
- Mundur yang tidak disengaja — gunakan potongan`!`atau`once/1`
- Terjadi pemeriksaan — loop`X = f(X)`secara default (gunakan`unify_with_occurs_check`)
- Potongan hijau (optimasi) vs potongan merah (mengubah arti) — lebih memilih hijau
---

## Pemecahan Masalah Rantai Pemikiran
### Masalah 1: Memecahkan Puzzle N-Queens
**Langkah 1: Pahami Masalahnya**
Tempatkan N ratu di papan catur NxN sehingga tidak ada dua ratu yang saling menyerang.
**Langkah 2: Identifikasi Pendekatannya**
Gunakan pembuatan berbasis batasan: tempatkan ratu kolom demi kolom, periksa keamanannya.
**Langkah 3: Terapkan**```prolog
n_queens(N, Qs) :-
    length(Qs, N),
    numlist(1, N, Rows),
    permutation(Rows, Qs),
    safe_queens(Qs).

safe_queens([]).
safe_queens([Q|Qs]) :-
    no_attack(Q, Qs, 1),
    safe_queens(Qs).

no_attack(_, [], _).
no_attack(Q, [Q1|Qs], D) :-
    Q =\= Q1,
    abs(Q - Q1) =\= D,
    D1 is D + 1,
    no_attack(Q, Qs, D1).
```

**Langkah 4: Verifikasi**
`?- n_queens(8, Qs).`harus menemukan 92 solusi.
### Masalah 2: Membangun Sistem Pakar Sederhana
**Langkah 1: Pahami Masalahnya**
Diagnosis masalah mobil berdasarkan gejalanya.
**Langkah 2: Identifikasi Pendekatannya**
Gunakan aturan Prolog untuk menyandikan pengetahuan diagnostik.
**Langkah 3: Terapkan**```prolog
% Facts about symptoms
symptom(car_wont_start).
symptom(clicking_sound).

% Rules
diagnosis(battery_dead) :-
    symptom(car_wont_start),
    symptom(clicking_sound).

diagnosis(starter_motor) :-
    symptom(car_wont_start),
    symptom(single_click),
    \+ symptom(clicking_sound).

diagnosis(out_of_fuel) :-
    symptom(engine_cranks),
    symptom(engine_wont_catch).

% Query
?- diagnosis(X).
```

**Langkah 4: Perpanjang**
Tambahkan skor kepercayaan diri, tanyakan gejala kepada pengguna secara interaktif, dan diagnosa berantai.
---

## Ringkasan
Prolog tidak seperti bahasa pemrograman lainnya. Daripada menulis petunjuk langkah demi langkah, Anda mendeskripsikan hubungan dan batasan — dan mesin mencari solusi melalui inferensi logis. Hal ini membuat Prolog ideal untuk permasalahan yang canggung atau bertele-tele dalam bahasa imperatif: sistem pakar, penjadwalan, penguraian tata bahasa, pemenuhan batasan, dan apa pun yang melibatkan aturan logis. Kebanyakan pemrogram tidak akan pernah menggunakan Prolog dalam produksi, tetapi mempelajarinya akan memperluas pemikiran Anda tentang apa itu pemrograman. Penyatuan, penelusuran mundur, dan spesifikasi masalah deklaratif adalah konsep yang memengaruhi desain bahasa, penelitian AI, dan bahkan pengoptimalan kueri basis data.
### Perbandingan Mesin Prolog
| Fitur | SWI-Prolog | Prolog GNU | Tau Prolog |
|---------|-----------|------------|------------|
| **Lisensi** | BSD (sumber terbuka) | GPL (sumber terbuka) | BSD (sumber terbuka) |
| **Platform** | Windows, Linux, macOS | Windows, Linux, macOS | JavaScript (peramban) |
| **CLP(FD)** | Perpustakaan bawaan | Bawaan | Tidak tersedia |
| **Dukungan DCG** | Penuh | Penuh | Terbatas |
| **Tabel** | Ya | Tidak | Tidak |
| **FFI (panggilan C)** | Ya | Ya | Melalui JavaScript |
| **Jaringan** | HTTP, TCP, TLS | TCP | Melalui JavaScript |
| **Multi-utas** | Ya | Tidak | Tidak |
| **Manajer paket** | `pack_install/1`| Tidak ada | npm |
| **Terbaik untuk** | Produksi, penelitian | Pemecahan kendala | Aplikasi web, pendidikan |
### Aplikasi Web dengan Pengines
```prolog
% SWI-Prolog Pengines — server-side Prolog accessible from web
:- use_module(library(http/http_server)).
:- use_module(library(pengines)).
:- use_module(library(pengines/apps/sandbox)).

:- http_handler(root(.), http_reply_from_files(web, []), [prefix]).
:- http_handler(root(pengines), pengine_application(sandbox)).

:- server(8080).

% Client-side JavaScript calls Prolog predicates via HTTP
% <script>
% new Pengine({
%   server: "/pengines",
%   ask: "grandparent(tom, X)",
%   ondata: function(data) { console.log(data); }
% });
% </script>
```

### Pemrograman meta dengan menegaskan/mencabut
```prolog
% Dynamic knowledge base modification
:- dynamic student/2.

% Add facts at runtime
add_student(Name, Grade) :-
    assert(student(Name, Grade)).

% Remove facts
remove_student(Name) :-
    retract(student(Name, _)).

% Query and modify
promote_students :-
    forall(
        student(Name, Grade),
        (   Grade < 12,
            NewGrade is Grade + 1,
            retract(student(Name, Grade)),
            assert(student(Name, NewGrade))
        )
    ).

% findall + assert pattern (batch operations)
copy_passing_students :-
    findall(Name, (student(Name, Grade), Grade >= 50), PassList),
    forall(member(Name, PassList),
        assert(passed(Name))).
```
