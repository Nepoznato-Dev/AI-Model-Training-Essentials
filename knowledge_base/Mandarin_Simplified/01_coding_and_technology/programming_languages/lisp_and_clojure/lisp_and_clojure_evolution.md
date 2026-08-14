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
# Lisp 和 Clojure — 版本历史和演变
## Lisp 时间线
|版本 |年份|关键主题 |
|--------|------|------------|
|口齿不清 1.5 | 1962 | **首次实现 Lisp**（约翰·麦卡锡，麻省理工学院）|
|麦克利斯普 | 20 世纪 60 年代 |麻省理工学院大型机 Lisp |
|口语| 1967 | Xerox PARC — 结构化编辑 |
|方案| 1975 | **极简 Lisp** （Sussman & Steele，麻省理工学院）|
|通用 Lisp | 1984 | **标准化 Lisp**（Guy Steele，ANSI 1994）|
| Emacs Lisp | Emacs Lisp 1985 | Emacs 编辑器 Lisp |
|方案R5RS| 1998 |修订后的⁵报告 — 广泛采用的计划标准 |
|方案R6RS| 2007 |模块系统，Unicode |
| R7RS方案 | 2013 |小语言（R7RS-小）|
| Clojure | 2007 | **JVM 上的现代 Lisp** (Rich Hickey) |
| Clojure 1.0 | 2009 |第一个稳定版本 |
| Clojure 1.3 | 2011 |协议，`defrecord` |
| Clojure 1.4 | 2012 |读者条件 |
| Clojure 1.5 | 2013 |传感器（稍后）|
| Clojure 1.7 | 2015 | 2015 **传感器**，读者条件 |
| Clojure 1.8 | 2016 | 2016  `spec`（数据验证）、`clojure.spec` |
| Clojure 1.9 | 2017 | 2017 **`spec`稳定**，改进了错误消息 |
| Clojure 1.10 | 2018 |更好的错误消息，`clj` CLI |
| Clojure 1.11 | 2022 | 2022  `update-keys`、`update-vals`、`abs` |
| Clojure 1.12 | 2024 | 2024 **Java 互操作改进**，`definterface` |
## 主要里程碑
### 早期 Lisp (1958–1970s)
- **1958**：John McCarthy 在麻省理工学院创建了 Lisp —“列表处理”
- **1962**：Lisp 1.5 — 第一个实现版本
- 关键创新：**垃圾收集**、**递归**、**同像性**（代码 = 数据）
-`eval`— 通用功能
-`cond`、`car`/`cdr`、`cons`、 lambda
### 计划（1975 年至今）
- **1975**：Guy Steele 和 Gerald Sussman 在麻省理工学院创建计划
- **哲学**：极简主义——小核心，强大的抽象
- 词法范围（在大多数语言之前）
- 一流的延续
- 卫生宏观
- 尾调用优化（强制）
### Common Lisp（1984 年至今）
- **1984**：Guy Steele 出版“Common Lisp 语言”
- **1994**：ANSI Common Lisp 标准 (ANSI X3.226)
- **“厨房水槽”Lisp** — 庞大的标准库
- CLOS（Common Lisp 对象系统）——最强大的 OOP
- 条件系统——可重新启动的错误
- 循环宏——强大的迭代DSL
### Clojure（2007 年至今）
- **2007**：Rich Hickey 创建了 Clojure — 用于 JVM 的 Lisp
- **哲学**：实用、并发、不变
- 持久不可变的数据结构
- STM（软件事务内存）
- `core.async`（CSP 式并发）
- 无缝 Java 互操作
- REPL驱动的开发
## 语法演变
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

## 功能演变
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

## 关键设计原则
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

## 生态系统增长
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
