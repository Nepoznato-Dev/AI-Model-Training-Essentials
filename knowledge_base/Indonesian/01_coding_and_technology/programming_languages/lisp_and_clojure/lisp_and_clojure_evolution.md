---
# Metadata
title: "Lisp & Clojure — Version History & Evolution"
description: "Comprehensive version history and evolution of Lisp from 1958 to modern Clojure."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [lisp, clojure, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Lisp & Clojure — Riwayat Versi & Evolusi
## Garis Waktu Cacat
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| Cadel 1.5 | 1962 | **Lisp yang pertama kali diimplementasikan** (John McCarthy, MIT) |
| Maclisp | 1960-an | Cadel mainframe MIT |
| Interlisp | 1967 | Xerox PARC — penyuntingan terstruktur |
| Skema | 1975 | **Lisp Minimalis** (Sussman & Steele, MIT) |
| Cadel Umum | 1984 | **Lisp Standar** (Guy Steele, ANSI 1994) |
| Emacs Cadel | 1985 | Cadel untuk editor Emacs |
| Skema R5RS | 1998 | Laporan yang Direvisi⁵ — standar Skema yang diadopsi secara luas |
| Skema R6RS | 2007 | Sistem modul, Unicode |
| Skema R7RS | 2013 | Bahasa kecil (R7RS-kecil) |
| Clojure | 2007 | **Lisp Modern di JVM** (Cupang Kaya) |
| Klojure 1.0 | 2009 | Rilis stabil pertama |
| Klojure 1.3 | 2011 | Protokol,`defrecord`|
| Klojure 1.4 | 2012 | Persyaratan pembaca |
| Klojure 1.5 | 2013 | Transduser (nanti) |
| Klojure 1.7 | 2015 | **Transduser**, kondisi pembaca |
| Klojure 1.8 | 2016 | `spec`(validasi data),`clojure.spec`|
| Klojure 1.9 | 2017 | **`spec`stabil**, pesan kesalahan ditingkatkan |
| Klojure 1.10 | 2018 | Pesan kesalahan yang lebih baik,`clj`CLI |
| Klojure 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Klojure 1.12 | 2024 | **Peningkatan interop Java**,`definterface`|
## Tonggak Penting
### Cadel Awal (1958–1970an)
- **1958**: John McCarthy membuat Lisp di MIT — "Pemrosesan Daftar"
- **1962**: Lisp 1.5 — versi pertama yang diimplementasikan
- Inovasi utama: **pengumpulan sampah**, **rekursi**, **homoikonisitas** (kode = data)
-`eval`— fungsi universal
- `cond`,`car`/ `cdr`, `cons`, lambda
### Skema (1975–sekarang)
- **1975**: Guy Steele & Gerald Sussman membuat Skema di MIT
- **Filsafat**: Minimalis — inti kecil, abstraksi kuat
- Pelingkupan leksikal (sebelum sebagian besar bahasa)
- Lanjutan kelas satu
- Makro higienis
- Optimasi panggilan ekor (wajib)
### Cadel Umum (1984–sekarang)
- **1984**: Guy Steele menerbitkan "Common Lisp the Language"
- **1994**: Standar ANSI Common Lisp (ANSI X3.226)
- **Lisp "wastafel dapur"** — perpustakaan standar yang sangat besar
- CLOS (Common Lisp Object System) — OOP paling kuat
- Sistem kondisi — kesalahan yang dapat dimulai ulang
- Loop makro — DSL iterasi yang kuat
### Clojure (2007–sekarang)
- **2007**: Rich Hickey menciptakan Clojure — Lisp untuk JVM
- **Filsafat**: Praktis, bersamaan, tidak dapat diubah
- Struktur data yang tidak dapat diubah dan persisten
- STM (Memori Transaksional Perangkat Lunak)
-`core.async`(konkurensi gaya CSP)
- Interop Java yang mulus
- Pengembangan berbasis REPL
## Evolusi Sintaks
```lisp
;; Lisp 1.5 (1962): The essentials
(defun factorial (n)
  (cond ((= n 0) 1)
        (t (* n (factorial (- n 1))))))

;; Scheme (1975): Minimalist, lexical scoping
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

;; Common Lisp (1984): CLOS, condition system
(defclass shape ()
  ((x :initarg :x :accessor shape-x)
   (y :initarg :y :accessor shape-y)))

(defclass circle (shape)
  ((radius :initarg :radius :accessor circle-radius)))

(defgeneric area (shape))

(defmethod area ((c circle))
  (* pi (expt (circle-radius c) 2)))

;; Clojure (2007): Modern, immutable, JVM
(defn factorial [n]
  (reduce * (range 1 (inc n))))

;; Clojure: Persistent data structures
(def m {:name "Alice" :age 30})
(def m2 (assoc m :email "alice@example.com"))  ; original unchanged

;; Clojure: Transducers (1.7)
(def xf (comp (filter even?) (map #(* % %))))
(transduce xf + 0 (range 10))

;; Clojure: spec (1.8+)
(require '[clojure.spec.alpha :as s])
(s/def ::name string?)
(s/def ::age (s/and int? #(<= 0 % 150)))
(s/def ::person (s/keys :req [::name ::age]))

;; Clojure: core.async (channels)
(require '[clojure.core.async :refer [go chan >! <!]])
(go (let [c (chan)]
      (>! c "hello")
      (println (<! c))))
```

## Evolusi Fitur
```
Lisp 1.5 (1962):  car/cdr/cons, eval, cond, lambda
Scheme (1975):    Lexical scoping, continuations, hygienic macros, TCO
Common Lisp (1984): CLOS, conditions, loop, defstruct, defmacro
Clojure (2007):   Persistent data structures, STM, Java interop
Clojure 1.7 (2015): Transducers, reader conditionals
Clojure 1.8 (2016): spec (data validation)
Clojure 1.9 (2017): spec stable, improved errors
Clojure 1.11 (2022): update-keys, update-vals
Clojure 1.12 (2024): Java interop improvements
```

## Prinsip Desain Utama
```
Lisp (general):
1. "Code is data" — homoiconicity (programs are lists)
2. "Macros" — extend the language itself
3. "REPL-driven" — interactive development
4. "Functional" — functions are first-class

Clojure-specific:
5. "Immutable by default" — persistent data structures
6. "Concurrency" — STM, atoms, agents, core.async
7. "Practical" — Java interop, real-world libraries
8. "Simple" — few concepts, compose freely
```

## Pertumbuhan Ekosistem
```
1958: Lisp created by John McCarthy at MIT
1962: Lisp 1.5 — first implementation
1975: Scheme — minimalist Lisp
1984: Common Lisp — standardized, comprehensive
1994: ANSI Common Lisp standard
2007: Clojure — Lisp on the JVM
2009: Clojure 1.0 — stable release
2015: Clojure 1.7 — transducers
2016: Clojure 1.8 — spec
2024: Clojure 1.12 — Java interop
2025: Lisp family powers:
       - Emacs (Emacs Lisp)
       - Racket (modern Scheme)
       - Clojure (web, data, concurrent systems)
       - Arc, Hy, Janet (Lisp dialects)
       Used by: NASA (JPL), Amazon, Apple, Nubank, CircleCI
```
