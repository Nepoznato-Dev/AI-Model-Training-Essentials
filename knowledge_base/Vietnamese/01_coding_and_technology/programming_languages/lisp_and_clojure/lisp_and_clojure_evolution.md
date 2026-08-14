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

# Lisp & Clojure — Lịch sử và sự phát triển của phiên bản
## Dòng thời gian Lisp
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| Lisp 1.5 | 1962 | **Lisp được triển khai lần đầu tiên** (John McCarthy, MIT) |
| Maclisp | thập niên 1960 | Lisp máy tính lớn của MIT |
| xen kẽ | 1967 | Xerox PARC — chỉnh sửa có cấu trúc |
| Đề án | 1975 | **Nói ngọng tối giản** (Sussman & Steele, MIT) |
| Lisp thông thường | 1984 | **Ngôn ngữ chuẩn hóa** (Guy Steele, ANSI 1994) |
| Emacs Lisp | 1985 | Trình soạn thảo Lisp cho Emacs |
| Sơ đồ R5RS | 1998 | Báo cáo đã sửa đổi⁵ - tiêu chuẩn Đề án được áp dụng rộng rãi |
| Sơ đồ R6RS | 2007 | Hệ thống mô-đun, Unicode |
| Sơ đồ R7RS | 2013 | Ngôn ngữ nhỏ (R7RS-nhỏ) |
| Clojure | 2007 | **Lisp hiện đại trên JVM** (Rich Hickey) |
| Clojure 1.0 | 2009 | Bản phát hành ổn định đầu tiên |
| Clojure 1.3 | 2011 | Giao thức,`defrecord`|
| Clojure 1.4 | 2012 | Đọc điều kiện |
| Clojure 1.5 | 2013 | Đầu dò (sau) |
| Clojure 1.7 | 2015 | **Bộ chuyển đổi**, điều kiện đọc |
| Clojure 1.8 | 2016 | `spec`(xác thực dữ liệu),`clojure.spec`|
| Clojure 1.9 | 2017 | **`spec`ổn định**, thông báo lỗi được cải thiện |
| Clojure 1.10 | 2018 | Thông báo lỗi tốt hơn,`clj`CLI |
| Clojure 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| Clojure 1.12 | 2024 | **Cải tiến tương tác Java**,`definterface`|
## Các cột mốc quan trọng
### Lisp thời kỳ đầu (1958–1970)
- **1958**: John McCarthy tạo Lisp tại MIT — "Xử lý danh sách"
- **1962**: Lisp 1.5 — phiên bản được triển khai đầu tiên
- Những cải tiến quan trọng: **thu gom rác**, **đệ quy**, **đồng âm** (code = data)
-`eval`— chức năng phổ quát
-`cond`,`car`/`cdr`,`cons`, lambda
### Sơ đồ (1975–nay)
- **1975**: Guy Steele & Gerald Sussman tạo ra Đề án tại MIT
- **Triết học**: Tối giản — cốt lõi nhỏ, trừu tượng mạnh mẽ
- Phạm vi từ vựng (trước hầu hết các ngôn ngữ)
- Tiếp tục hạng nhất
- Macro hợp vệ sinh
- Tối ưu hóa cuộc gọi đuôi (bắt buộc)
### Lisp thông dụng (1984–nay)
- **1984**: Guy Steele xuất bản cuốn "Common Lisp the Language"
- **1994**: Tiêu chuẩn ANSI Common Lisp (ANSI X3.226)
- **Lisp "bồn rửa bát"** — thư viện tiêu chuẩn đồ sộ
- CLOS (Hệ thống đối tượng Lisp chung) - OOP mạnh nhất
- Hệ thống điều kiện - lỗi có thể khởi động lại
- Loop macro - DSL lặp mạnh mẽ
### Clojure (2007–nay)
- **2007**: Rich Hickey tạo Clojure — Lisp cho JVM
- **Triết học**: Thực tế, đồng thời, bất biến
- Cấu trúc dữ liệu bất biến liên tục
- STM (Bộ nhớ giao dịch phần mềm)
-`core.async`(đồng thời kiểu CSP)
- Tương tác Java liền mạch
- Phát triển dựa trên REPL
## Tiến hóa cú pháp
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

## Tiến hóa tính năng
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

## Nguyên tắc thiết kế chính
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

## Tăng trưởng hệ sinh thái
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
