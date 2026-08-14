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
# Lisp & Clojure — 버전 기록 및 진화
## 리스프 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 리스프 1.5 | 1962 | **처음으로 구현된 Lisp** (John McCarthy, MIT) |
| 맥클리프 | 1960년대 | MIT 메인프레임 Lisp |
| 인터리스프 | 1967 | Xerox PARC — 구조화된 편집 |
| 계획 | 1975년 | **미니멀리스트 Lisp** (Sussman & Steele, MIT) |
| 커먼 리스프 | 1984년 | **표준화된 Lisp**(Guy Steele, ANSI 1994) |
| 이맥스 리스프 | 1985 | Emacs 편집기용 Lisp |
| 구성표 R5RS | 1998 | 개정⁵ 보고서 — 널리 채택된 제도 표준 |
| 구성표 R6RS | 2007년 | 모듈 시스템, 유니코드 |
| 구성표 R7RS | 2013 | 작은 언어(R7RS-small) |
| 클로저 | 2007년 | **JVM의 Modern Lisp**(Rich Hickey) |
| 클로저 1.0 | 2009 | 첫 번째 안정 릴리스 |
| 클로저 1.3 | 2011 | 프로토콜,`defrecord`|
| 클로저 1.4 | 2012 | 독자 조건 |
| 클로저 1.5 | 2013 | 변환기(나중에) |
| 클로저 1.7 | 2015 | **변환기**, 판독기 조건 |
| 클로저 1.8 | 2016 |  `spec`(데이터 검증),`clojure.spec`|
| 클로저 1.9 | 2017 | **`spec`안정**, 오류 메시지 개선 |
| 클로저 1.10 | 2018 | 더 나은 오류 메시지,`clj`CLI |
| 클로저 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| 클로저 1.12 | 2024 | **Java 상호 운용성 개선**,`definterface`|
## 주요 이정표
### 초기 Lisp(1958~1970년대)
- **1958**: John McCarthy가 MIT에서 Lisp을 만듭니다 — "목록 처리"
- **1962**: Lisp 1.5 — 최초 구현 버전
- 주요 혁신: **가비지 수집**, **재귀**, **동질성**(코드 = 데이터)
-`eval`— 범용 기능
-`cond`,`car`/`cdr`,`cons`, 람다
### 계획(1975~현재)
- **1975**: Guy Steele 및 Gerald Sussman이 MIT에서 계획 수립
- **철학**: 미니멀리스트 — 작은 핵심, 강력한 추상화
- 어휘 범위 지정(대부분의 언어 이전)
- 일류 연속
- 위생적인 매크로
- 테일콜 최적화(필수)
### 커먼 리스프(1984~현재)
- **1984**: Guy Steele이 "Common Lisp the Language" 출판
- **1994**: ANSI Common Lisp 표준(ANSI X3.226)
- **"주방 싱크대" Lisp** — 대규모 표준 라이브러리
- CLOS(Common Lisp Object System) — 가장 강력한 OOP
- 조건 시스템 - 다시 시작할 수 있는 오류
- 루프 매크로 — 강력한 반복 DSL
### 클로저(2007~현재)
- **2007**: Rich Hickey가 Clojure — JVM용 Lisp 개발
- **철학**: 실용적, 동시성, 불변성
- 지속적 불변 데이터 구조
- STM(소프트웨어 트랜잭션 메모리)
- `core.async`(CSP 스타일 동시성)
- 원활한 Java 상호 운용성
- REPL 기반 개발
## 구문 진화
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

## 기능 진화
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

## 주요 디자인 원칙
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

## 생태계 성장
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
