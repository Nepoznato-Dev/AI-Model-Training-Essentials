---
# Metadata
title: "Lisp & Clojure — Version History & Evolution"
description: "Comprehensive version history and evolution of Lisp from 1958 to modern Clojure."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Lisp & Clojure — সংস্করণ ইতিহাস এবং বিবর্তন
## লিস্প টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| লিস্প 1.5 | 1962 | **প্রথম বাস্তবায়িত লিস্প** (জন ম্যাকার্থি, এমআইটি) |
| ম্যাকলিস্প | 1960 | এমআইটি মেইনফ্রেম লিস্প |
| ইন্টারলিস্প | 1967 | জেরক্স PARC — কাঠামোগত সম্পাদনা |
| স্কিম | 1975 | **মিনিমালিস্ট লিস্প** (সুসম্যান অ্যান্ড স্টিল, এমআইটি) |
| কমন লিস্প | 1984 | **স্ট্যান্ডার্ডাইজড লিস্প** (গাই স্টিল, এএনএসআই 1994) |
| Emacs Lisp | 1985 | Emacs সম্পাদকের জন্য লিস্প |
| স্কিম R5RS | 1998 | সংশোধিত⁵ প্রতিবেদন — ব্যাপকভাবে গৃহীত স্কিম মান |
| স্কিম R6RS | 2007 | মডিউল সিস্টেম, ইউনিকোড |
| স্কিম R7RS | 2013 | ছোট ভাষা (R7RS-small) |
| ক্লোজার | 2007 | **জেভিএমে আধুনিক লিস্প** (রিচ হিকি) |
| Clojure 1.0 | 2009 | প্রথম স্থিতিশীল মুক্তি |
| ক্লোজার 1.3 | 2011 | প্রোটোকল,`defrecord`|
| ক্লোজার 1.4 | 2012 | পাঠক শর্তাবলী |
| ক্লোজার 1.5 | 2013 | ট্রান্সডুসার (পরে) |
| ক্লোজার 1.7 | 2015 | **ট্রান্সডুসার**, পাঠক শর্তাবলী |
| ক্লোজার 1.8 | 2016 | `spec`(ডেটা যাচাইকরণ),`clojure.spec`|
| ক্লোজার 1.9 | 2017 | **`spec`স্থিতিশীল**, উন্নত ত্রুটি বার্তা |
| ক্লোজার 1.10 | 2018 | আরও ভাল ত্রুটি বার্তা,`clj`CLI |
| ক্লোজার 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| ক্লোজার 1.12 | 2024 | **জাভা ইন্টারপ উন্নতি**,`definterface`|
## প্রধান মাইলফলক
### প্রারম্ভিক লিস্প (1958-1970)
- **1958**: জন ম্যাকার্থি এমআইটি-তে লিস্প তৈরি করেন - "লিস্ট প্রসেসিং"
- **1962**: লিস্প 1.5 — প্রথম বাস্তবায়িত সংস্করণ
- মূল উদ্ভাবন: **আবর্জনা সংগ্রহ**, **পুনরাবৃত্তি**, **হোমোইকোনিসিটি** (কোড = ডেটা)
-`eval`— সর্বজনীন ফাংশন
-`cond`,`car`/`cdr`,`cons`, ল্যাম্বদা
### স্কিম (1975-বর্তমান)
- **1975**: গাই স্টিল এবং জেরাল্ড সুসম্যান এমআইটি-তে স্কিম তৈরি করেন
- **দর্শন**: মিনিমালিস্ট — ছোট মূল, শক্তিশালী বিমূর্ততা
- লেক্সিকাল স্কোপিং (বেশিরভাগ ভাষার আগে)
- প্রথম শ্রেণীর ধারাবাহিকতা
- স্বাস্থ্যকর ম্যাক্রো
- টেল-কল অপ্টিমাইজেশান (বাধ্যতামূলক)
### কমন লিস্প (1984-বর্তমান)
- **1984**: গাই স্টিল "কমন লিস্প দ্য ল্যাঙ্গুয়েজ" প্রকাশ করেছেন
- **1994**: ANSI কমন লিস্প স্ট্যান্ডার্ড (ANSI X3.226)
- **"রান্নাঘরের সিঙ্ক" লিস্প** — বিশাল স্ট্যান্ডার্ড লাইব্রেরি
- CLOS (সাধারণ লিস্প অবজেক্ট সিস্টেম) - সবচেয়ে শক্তিশালী OOP
- কন্ডিশন সিস্টেম - রিস্টার্টযোগ্য ত্রুটি
- লুপ ম্যাক্রো — শক্তিশালী পুনরাবৃত্তি DSL
### ক্লোজার (2007-বর্তমান)
- **2007**: রিচ হিকি JVM-এর জন্য Clojure — Lisp তৈরি করেছে
- **দর্শন**: ব্যবহারিক, সমসাময়িক, অপরিবর্তনীয়
- স্থায়ী অপরিবর্তনীয় ডেটা স্ট্রাকচার
- STM (সফ্টওয়্যার লেনদেন মেমরি)
-`core.async`(CSP-শৈলীর একত্রীকরণ)
- বিরামহীন জাভা ইন্টারপ
- REPL-চালিত উন্নয়ন
## সিনট্যাক্স বিবর্তন
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

## বৈশিষ্ট্য বিবর্তন
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

## মূল ডিজাইনের নীতি
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

## ইকোসিস্টেম বৃদ্ধি
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
