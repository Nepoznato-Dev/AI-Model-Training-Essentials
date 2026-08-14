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
# Lisp ve Clojure — Sürüm Geçmişi ve Gelişimi
## Lisp Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| Lisp 1.5 | 1962 | **Lisp'in ilk uygulamaya konması** (John McCarthy, MIT) |
| Maclisp | 1960'lar | MIT ana bilgisayarı Lisp |
| Interlisp | 1967 | Xerox PARC — yapılandırılmış düzenleme |
| Şema | 1975 | **Minimalist Lisp** (Sussman ve Steele, MIT) |
| Ortak Lisp | 1984 | **Standartlaştırılmış Lisp** (Guy Steele, ANSI 1994) |
| Emacs Lisp | 1985 | Emacs editörü için Lisp |
| Şema R5RS | 1998 | Revize Edilmiş⁵ Rapor — yaygın olarak benimsenen Şema standardı |
| Şema R6RS | 2007 | Modül sistemi, Unicode |
| Şema R7RS | 2013 | Küçük dil (R7RS-küçük) |
| Clojure | 2007 | **JVM'de Modern Lisp** (Rich Hickey) |
| Clojure 1.0 | 2009 | İlk kararlı sürüm |
| Clojure 1.3 | 2011 | Protokoller,`defrecord`|
| Clojure 1.4 | 2012 | Okuyucu koşullu ifadeleri |
| Clojure 1.5 | 2013 | Dönüştürücüler (daha sonra) |
| Clojure 1.7 | 2015 | **Dönüştürücüler**, okuyucu koşul cümleleri |
| Clojure 1.8 | 2016 | `spec`(veri doğrulama),`clojure.spec`|
| Clojure 1.9 | 2017 | **`spec`kararlı**, geliştirilmiş hata mesajları |
| Clojure 1.10 | 2018 | Daha iyi hata mesajları,`clj`CLI |
| Clojure 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Clojure 1.12 | 2024 | **Java birlikte çalışma iyileştirmeleri**,`definterface`|
## Önemli Kilometre Taşları
### Erken Lisp (1958–1970'ler)
- **1958**: John McCarthy, MIT'de Lisp'i yarattı — "Liste İşleme"
- **1962**: Lisp 1.5 — uygulanan ilk sürüm
- Temel yenilikler: **çöp toplama**, **özyineleme**, **homoikoniklik** (kod = veri)
-`eval`— evrensel işlev
-`cond`,`car`/`cdr`,`cons`, lambda
### Şeması (1975 – günümüz)
- **1975**: Guy Steele ve Gerald Sussman MIT'de Plan oluşturdu
- **Felsefe**: Minimalist — küçük çekirdek, güçlü soyutlamalar
- Sözcüksel kapsam belirleme (çoğu dilden önce)
- Birinci sınıf devamlar
- Hijyenik makrolar
- Kuyruk çağrısı optimizasyonu (zorunlu)
### Common Lisp (1984-günümüz)
- **1984**: Guy Steele "Common Lisp the Language"ı yayınladı
- **1994**: ANSI Common Lisp standardı (ANSI X3.226)
- **"Mutfak lavabosu" Lisp** — muazzam standart kütüphane
- CLOS (Common Lisp Object System) — en güçlü OOP
- Durum sistemi — yeniden başlatılabilir hatalar
- Döngü makrosu — güçlü yinelemeli DSL
### Clojure (2007 – günümüz)
- **2007**: Rich Hickey, JVM için Clojure — Lisp'i yarattı
- **Felsefe**: Pratik, eşzamanlı, değişmez
- Kalıcı, değişmez veri yapıları
- STM (Yazılım İşlemsel Bellek)
-`core.async`(CSP tarzı eşzamanlılık)
- Sorunsuz Java birlikte çalışma
- REPL odaklı geliştirme
## Söz Dizimi Gelişimi
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

## Özellik Gelişimi
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

## Temel Tasarım İlkeleri
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

## Ekosistem Büyümesi
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
