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

# Lisp 和 Clojure — 版本歷史與演變
## Lisp 時間線
|版本 |年份|關鍵主題 |
|--------|------|------------|
|口齒不清 1.5 | 1962 | **首次實現 Lisp**（約翰·麥卡錫，麻省理工學院）|
|麥克利斯普 | 20 世紀 60 年代 |麻省理工學院大型主機 Lisp |
|口語| 1967 | Xerox PARC — 結構化編輯 |
|方案| 1975 | **極簡 Lisp** （Sussman & Steele，麻省理工學院）|
|通用 Lisp | 1984 | **標準化 Lisp**（Guy Steele，ANSI 1994）|
| Emacs Lisp | Emacs Lisp 1985 | Emacs 編輯器 Lisp |
|方案R5RS| 1998 |修訂後的⁵報告 — 廣泛採用的計畫標準 |
|方案R6RS| 2007 |模組系統，Unicode |
| R7RS方案 | 2013 |小語言（R7RS-小）|
| Clojure | 2007 | **JVM 上的現代 Lisp** (Rich Hickey) |
| Clojure 1.0 | 2009 |第一個穩定版本 |
| Clojure 1.3 | 2011 |協議，`defrecord` |
| Clojure 1.4 | 2012 |讀者條件 |
| Clojure 1.5 | 2013 |感測器（稍後）|
| Clojure 1.7 | 2015 | 2015 **感應器**，讀者條件 |
| Clojure 1.8 | 2016 | 2016 `spec`（資料驗證）、`clojure.spec` |
| Clojure 1.9 | 2017 | 2017 **`spec`穩定**，改進了錯誤訊息 |
| Clojure 1.10 | 2018 |更好的錯誤訊息，`clj` CLI |
| Clojure 1.11 | 2022 | 2022 `update-keys`、`update-vals`、`abs` |
| Clojure 1.12 | 2024 | 2024 **Java 互通改進**，`definterface` |
## 主要里程碑
### 早期 Lisp (1958–1970s)
- **1958**：John McCarthy 在麻省理工學院創建了 Lisp —“列表處理”
- **1962**：Lisp 1.5 — 第一個實作版本
- 關鍵創新：**垃圾收集**、**遞歸**、**同像性**（代碼 = 資料）
-`eval`— 通用功能
-`cond`、`car`/`cdr`、`cons`、 lambda
### 計畫（1975 年至今）
- **1975**：Guy Steele 和 Gerald Sussman 在麻省理工學院創建計劃
- **哲學**：極簡主義－小核心，強大的抽象
- 詞法範圍（在大多數語言之前）
- 一流的延續
- 衛生宏觀
- 尾調用最佳化（強制）
### Common Lisp（1984 年至今）
- **1984**：Guy Steele 出版“Common Lisp 語言”
- **1994**：ANSI Common Lisp 標準 (ANSI X3.226)
- **「廚房水槽」Lisp** — 龐大的標準庫
- CLOS（Common Lisp 物件系統）－最強大的 OOP
- 條件系統－可重新啟動的錯誤
- 循環宏－強大的迭代DSL
### Clojure（2007 年至今）
- **2007**：Rich Hickey 創建了 Clojure — 用於 JVM 的 Lisp
- **哲學**：實用、並發、不變
- 持久不可變的資料結構
- STM（軟體事務記憶體）
- `core.async`（CSP 式並發）
- 無縫 Java 互通
- REPL驅動的開發
## 語法演變
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

## 功能演變
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

## 關鍵設計原則
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

## 生態系成長
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
