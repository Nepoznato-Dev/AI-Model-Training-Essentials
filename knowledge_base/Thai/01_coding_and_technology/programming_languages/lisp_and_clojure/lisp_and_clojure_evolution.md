<!--
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

-->
# Lisp & Clojure - ประวัติเวอร์ชันและวิวัฒนาการ
## ไทม์ไลน์กระเพื่อม
| เวอร์ชั่น | ปี | ธีมหลัก |
|---------|-|-----------|
| เสียงกระหึ่ม 1.5 | 2505 | **ติดตั้ง Lisp ครั้งแรก** (John McCarthy, MIT) |
| แมคลิสป์ | ทศวรรษ 1960 | MIT เมนเฟรม Lisp |
| อินเตอร์ลิสป์ | 2510 | Xerox PARC — การแก้ไขแบบมีโครงสร้าง |
| โครงการ | 1975 | **Minimalist Lisp** (Sussman & Steele, MIT) |
| เสียงกระเพื่อมทั่วไป | 1984 | **เสียงกระเพื่อมมาตรฐาน** (Guy Steele, ANSI 1994) |
| อีแมคส์ ลิสป์ | 1985 | ตัวแก้ไข Lisp สำหรับ Emacs |
| โครงการ R5RS | 1998 | รายงานฉบับปรับปรุง⁵ — มาตรฐานโครงการที่นำมาใช้กันอย่างแพร่หลาย |
| โครงการ R6RS | 2550 | ระบบโมดูล Unicode |
| โครงการ R7RS | 2013 | ภาษาเล็ก (R7RS-เล็ก) |
| ปิดบัง | 2550 | **Modern Lisp บน JVM** (Rich Hickey) |
| โคลจูร์ 1.0 | 2552 | การเปิดตัวที่เสถียรครั้งแรก |
| โคลจูร์ 1.3 | 2554 | โปรโตคอล`defrecord`|
| โคลจูร์ 1.4 | 2555 | เงื่อนไขของผู้อ่าน |
| โคลจูร์ 1.5 | 2013 | ทรานสดิวเซอร์ (ภายหลัง) |
| โคลจูร์ 1.7 | 2558 | **ทรานสดิวเซอร์** เงื่อนไขของผู้อ่าน |
| โคลจูร์ 1.8 | 2559 | `spec`(การตรวจสอบข้อมูล),`clojure.spec`|
| โคลจูร์ 1.9 | 2017 | **`spec`เสถียร** ปรับปรุงข้อความแสดงข้อผิดพลาด |
| โคลจูเร่ 1.10 | 2018 | ข้อความแสดงข้อผิดพลาดที่ดีกว่า`clj`CLI |
| โคลจูเร่ 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| โคลจูเร่ 1.12 | 2024 | **การปรับปรุงการทำงานร่วมกันของ Java**,`definterface`|
## เหตุการณ์สำคัญที่สำคัญ
### ในช่วงต้นเสียงกระเพื่อม (1958–1970)
- **1958**: John McCarthy สร้าง Lisp ที่ MIT — "List Processing"
- **1962**: Lisp 1.5 — เวอร์ชันที่ใช้งานครั้งแรก
- นวัตกรรมที่สำคัญ: **การเก็บขยะ**, **การเรียกซ้ำ**, **ความเป็นเอกภาพ** (รหัส = ข้อมูล)
-`eval`— ฟังก์ชันสากล
-`cond`,`car`/`cdr`,`cons`, แลมบ์ดา
### โครงการ (พ.ศ. 2518–ปัจจุบัน)
- **1975**: Guy Steele และ Gerald Sussman สร้าง Scheme ที่ MIT
- **ปรัชญา**: มินิมัลลิสต์ — แกนกลางขนาดเล็ก นามธรรมอันทรงพลัง
- การกำหนดขอบเขตคำศัพท์ (ก่อนภาษาส่วนใหญ่)
- ความต่อเนื่องชั้นหนึ่ง
- มาโครสุขอนามัย
- การเพิ่มประสิทธิภาพการโทรหาง (จำเป็น)
### เสียงกระเพื่อมทั่วไป (1984–ปัจจุบัน)
- **1984**: Guy Steele ตีพิมพ์ "Common Lisp the Language"
- **1994**: มาตรฐาน ANSI Common Lisp (ANSI X3.226)
- **Lisp "อ่างล้างจาน"** — ห้องสมุดมาตรฐานขนาดใหญ่
- CLOS (Common Lisp Object System) — OOP ที่ทรงพลังที่สุด
- ระบบเงื่อนไข - ข้อผิดพลาดที่สามารถรีสตาร์ทได้
- วนรอบมาโคร — DSL วนซ้ำอันทรงพลัง
### โคลจูร์ (2550–ปัจจุบัน)
- **2007**: Rich Hickey สร้าง Clojure — Lisp สำหรับ JVM
- **ปรัชญา**: ใช้ได้จริง เกิดขึ้นพร้อมกัน ไม่เปลี่ยนรูป
- โครงสร้างข้อมูลที่ไม่เปลี่ยนรูปถาวร
- STM (ซอฟต์แวร์หน่วยความจำธุรกรรม)
-`core.async`(การทำงานพร้อมกันแบบ CSP)
- การทำงานร่วมกันของ Java แบบไม่มีรอยต่อ
- การพัฒนาที่ขับเคลื่อนด้วย REPL
## วิวัฒนาการไวยากรณ์
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

## วิวัฒนาการคุณสมบัติ
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

## หลักการออกแบบที่สำคัญ
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

## การเติบโตของระบบนิเวศ
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
