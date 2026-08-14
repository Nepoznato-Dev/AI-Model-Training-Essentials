---
# Metadata
title: "OCaml — Version History & Evolution"
description: "Comprehensive version history and evolution of OCaml from Caml to modern OCaml."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ocaml, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# OCaml — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| Caml | 1985 | **Bahasa Mesin Abstrak Kategorikal** (INRIA) |
| Cahaya Caml | 1990 | Caml Ringan (Xavier Leroy) |
| OCaml 1.0 | 1996 | **Tujuan Caml** — menambahkan OOP |
| OCaml 3.0 | 2000 | **Mayor**: Metode polimorfik,`lazy`,`Obj`|
| OCaml 3.05 | 2002 | Peningkatan kompiler kode asli |
| OCaml 3.10 | 2007 |  Binding`module type of`,`let`dalam definisi kelas |
| OCaml 3.11 | 2008 |  Anotasi jenis `private`,`module type of`|
| OCaml 3.12 | 2010 | Modul kelas satu |
| OCaml 4.00 | 2012 | **Mayor**:`module type of`,`val`di tanda tangan |
| OCaml 4.01 | 2013 |  Modul`Bytes`(string yang dapat diubah dipisahkan) |
| OCaml 4.02 | 2014 |  Modul `Float`, peningkatan`String`|
| OCaml 4.03 | 2016 |  Tipe `Result`,`Seq`(urutan malas) |
| OCaml 4.04 | 2017 | Profiler ruangwaktu,`floatarray`|
| OCaml 4.06 | 2018 |  Binding`let`dalam ekspresi`module`|
| OCaml 4.08 | 2019 |  Peningkatan `Binding`, peningkatan`Seq`|
| OCaml 4.10 | 2020 |  Peningkatan`Bigarray`|
| OCaml 4.12 | 2021 |  Peningkatan`Stdlib`|
| OCaml 4.14 | 2022 | **Kekurangan modulo-ekor** (TMC) |
| OCaml 5.0 | 2022 | **Mayor**: Penangan efek, paralelisme (tanpa GIL) |
| OCaml 5.1 | 2023 |  Peningkatan `Domain`, peningkatan`Effect`|
| OCaml 5.2 | 2024 | Peningkatan pesan kesalahan, peningkatan`Domain`|
| OCaml 5.3 | 2025 | Pembangunan yang sedang berlangsung |
## Tonggak Penting
### Caml (1985–1995)
- **1985**: Gérard Huet menciptakan Caml di INRIA (Prancis)
- **Nama**: "Bahasa Mesin Abstrak Kategoris"
- **1990**: Caml Light — versi ringan oleh Xavier Leroy
- Pencocokan pola, inferensi tipe Hindley-Milner
### OCaml 1.0–3.x: Menambahkan OOP (1996–2011)
- **1996**: OCaml (Objective Caml) — menambahkan fitur berorientasi objek
- **3.0 (2000)**: Metode polimorfik, evaluasi `lazy`
- **3.10 (2007)**:`module type of`
- **3.12 (2010)**: **Modul kelas satu** — modul sebagai nilai
### OCaml 4.x: OCaml modern (2012–2021)
- **4.00 (2012)**: `module type of`, sistem modul yang ditingkatkan
- **4.01 (2013)**: Modul`Bytes`— string yang tidak dapat diubah secara default
- **4.03 (2016)**: tipe `Result`,`Seq`(urutan malas)
- **4.08 (2019)**: Peningkatan pesan kesalahan
- **4.14 (2022)**: Tail-modulo-cons (TMC) — memori yang lebih baik untuk konstruktor rekursif
### OCaml 5.x: Revolusi Paralel (2022–sekarang)
- **5.0 (2022)**: **Penanganan efek**, **paralelisme sejati** (menghapus GIL untuk kode murni)
  -`Domain`— thread OS untuk komputasi paralel
  -`Effect`— penangan efek aljabar (lanjutan)
  - Tidak ada lagi Kunci Penerjemah Global — OCaml multicore sesungguhnya
- **5.1 (2023)**: Peningkatan domain, penyempurnaan pengendali efek
- **5.2 (2024)**: Pesan kesalahan yang lebih baik, peningkatan lebih lanjut
## Evolusi Sintaks
```ocaml
(* OCaml 3.x: Pattern matching, modules *)
type shape =
  | Circle of float
  | Rectangle of float * float

let area = function
  | Circle r -> Float.pi *. r *. r
  | Rectangle (w, h) -> w *. h

(* OCaml 3.12: First-class modules *)
module type Printable = sig
  val to_string : t -> string
end

let print (module M : Printable) x =
  print_endline (M.to_string x)

(* OCaml 4.03: Result type *)
let safe_divide x y =
  if y = 0 then Error "division by zero"
  else Ok (x / y)

(* OCaml 4.08: Better error messages *)
let x = 1 +. 2
(* Error: This expression has type int but an expression was expected of type float *)

(* OCaml 5.0: Effect handlers *)
type _ Effect.t += Read : string Effect.t

let with_input input f =
  Effect.Deep.try_with f ()
    { effc = fun (type a) (eff : a Effect.t) ->
        match eff with
        | Read -> Some (fun (k : (a, _) Effect.Deep.continuation) ->
            Effect.Deep.continue k input)
        | _ -> None }

(* OCaml 5.0: Parallelism with Domain *)
let parallel_map f list =
  let domains = List.map (fun x ->
    Domain.spawn (fun () -> f x)
  ) list in
  List.map Domain.join domains

(* OCaml: Functor (module parameter) *)
module MakeSet (Ord : Map.OrderedType) = Set.Make(Ord)
module IntSet = MakeSet(struct type t = int let compare = compare end)
```

## Ketik Evolusi Sistem
```
Caml (1985):       Hindley-Milner type inference, pattern matching
Caml Light (1990): Modules, functors
OCaml 1.0 (1996):  Objects, classes, inheritance
OCaml 3.0 (2000):  Polymorphic methods, lazy
OCaml 3.12 (2010): First-class modules
OCaml 4.03 (2016): Result, Seq
OCaml 4.14 (2022): Tail-modulo-cons
OCaml 5.0 (2022):  Effect handlers, Domain (parallelism)
```

## Prinsip Desain Utama
```
1. "Type safety" — static types catch errors early
2. "Type inference" — no need to annotate everything
3. "Pattern matching" — exhaustive, powerful
4. "Modules & functors" — composable, parameterized
5. "Performance" — native code compiler, fast GC
6. "Pragmatic FP" — functional with pragmatic OOP
7. "Parallelism" — Domain (OCaml 5) for true multicore
```

## Pertumbuhan Ekosistem
```
1985: Caml created at INRIA (France)
1990: Caml Light — lightweight version
1996: OCaml — adds OOP
2002: Jane Street adopts OCaml — financial trading
2010: First-class modules
2012: OPAM package manager
2016: OCaml 4.03 — Result type
2022: OCaml 5.0 — effect handlers, parallelism
2025: OCaml used in:
       - Jane Street (financial trading, largest OCaml shop)
       - Facebook/Flow (JavaScript type checker)
       - Tezos (blockchain)
       - Coq (theorem prover)
       - Infer (Facebook's static analyzer)
       - Ocsigen (web framework)
       Compilers: ocamlc (bytecode), ocamlopt (native)
       Tools: dune (build), opam (packages), merlin (IDE)
```
