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
# Lisp と Clojure — バージョン履歴と進化
## Lisp タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
| Lisp 1.5 | 1962年 | **初めて実装された Lisp** (John McCarthy、MIT) |
|マクリスプ | 1960年代 | MIT メインフレーム Lisp |
|インターリスプ | 1967年 | Xerox PARC — 構造化編集 |
|スキーム | 1975年 | **Minimalist Lisp** (サスマン & スティール、マサチューセッツ工科大学) |
|共通Lisp | 1984年 | **標準化された Lisp** (Guy Steele、ANSI 1994) |
| Emacs リスプ | 1985年 | Emacs エディター用の Lisp |
|スキーム R5RS | 1998年 |改訂⁵ レポート — 広く採用されているスキーム標準 |
|スキーム R6RS | 2007年 |モジュールシステム、Unicode |
|スキーム R7RS | 2013年 |小さな言語 (R7RS-small) |
|クロジュア | 2007年 | **JVM 上の最新の Lisp** (Rich Hickey) |
| Clojure 1.0 | 2009年 |最初の安定版リリース |
| Clojure 1.3 | 2011年 |プロトコル、`defrecord` |
| Clojure 1.4 | 2012年 |リーダーの条件文 |
| Clojure 1.5 | 2013年 |トランスデューサー (後ほど) |
| Clojure 1.7 | 2015年 | **トランスデューサー**、リーダーの条件 |
| Clojure 1.8 | 2016年 | `spec`(データ検証)、`clojure.spec` |
| Clojure 1.9 | 2017年 | **`spec`は安定しています**、エラー メッセージが改善されました。
| Clojure 1.10 | 2018年 |エラー メッセージの改善、`clj` CLI |
| Clojure 1.11 | 2022年 |  `update-keys`、`update-vals`、`abs` |
| Clojure 1.12 | 2024年 | **Java 相互運用機能の改善**、`definterface` |
## 主要なマイルストーン
### 初期の Lisp (1958 ～ 1970 年代)
- **1958**: ジョン・マッカーシーが MIT で Lisp — 「リスト処理」を作成
- **1962**: Lisp 1.5 — 最初に実装されたバージョン
- 主な革新: **ガベージ コレクション**、**再帰**、**同形性** (コード = データ)
-`eval`— ユニバーサル関数
-`cond`、`car`/`cdr`、`cons`、 ラムダ
### スキーム (1975 ～現在)
- **1975**: ガイ・スティールとジェラルド・サスマンが MIT で計画を作成
- **哲学**: ミニマリスト — 小さなコア、強力な抽象化
- 語彙のスコープ設定 (ほとんどの言語の前)
- ファーストクラスの継続
- 衛生的なマクロ
- テールコールの最適化 (必須)
### Common Lisp (1984–現在)
- **1984**: Guy Steele が「Common Lisp the Language」を出版
- **1994**: ANSI Common Lisp 標準 (ANSI X3.226)
- **「キッチン シンク」Lisp** — 大規模な標準ライブラリ
- CLOS (Common Lisp Object System) — 最も強力な OOP
- 状態システム — 再開可能なエラー
- ループ マクロ — 強力な反復 DSL
### Clojure (2007–現在)
- **2007**: Rich Hickey が Clojure — JVM 用の Lisp を作成
- **哲学**: 実践的、並行的、不変
- 永続的な不変のデータ構造
- STM (ソフトウェア トランザクション メモリ)
-`core.async`(CSP スタイルの同時実行)
- シームレスな Java 相互運用性
- REPL主導の開発
## 構文の進化
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

## 機能の進化
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

## 主要な設計原則
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

## エコシステムの成長
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
