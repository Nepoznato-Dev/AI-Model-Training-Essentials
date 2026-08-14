---
# Metadata
title: "Lisp & Clojure — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Lisp and Clojure ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [lisp, clojure, ecosystem, tooling, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Lisp 및 Clojure — 생태계 및 도구 가이드
이 가이드에서는 Lisp 및 Clojure 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## Lisp 및 Clojure 구현
| 구현 | 언어 | 메모 |
|---------------|----------|-------|
| **클로저** | JVM | JVM의 최신 Lisp |
| **클로저스크립트** | JS | JavaScript로 컴파일된 Clojure |
| **SBCL** | 커먼 리스프 | 고성능 CL |
| **CCL** | 커먼 리스프 | OpenMCL, 빠른 컴파일 |
| **ECL** | 커먼 리스프 | 삽입 가능, C 상호 운용성 |
| **Emacs Lisp** | 이맥스 | 확장 언어 |
| **라켓** | 계획 | 언어 중심 프로그래밍 |
| **간계** | 계획 | GNU 확장 언어 |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## 클로저 툴링
| 도구 | 목적 |
|------|---------|
| **클로저 CLI(clj)** | 공식 CLI 도구 |
| **라이닝겐** | 클래식 프로젝트 도구 |
| **deps.edn** | 종속성 관리 |
| **바바시카** | 빠른 Clojure 스크립팅 |
| **도구.빌드** | 자동화 구축 |
| **shadow-cljs** | ClojureScript 빌드 |
| **그림바퀴** | 라이브 ClojureScript 다시 로드 |
```clojure
;; deps.edn
{:paths ["src" "resources"]
 :deps {org.clojure/clojure {:mvn/version "1.11.1"}
        ring/ring-core {:mvn/version "1.11.0"}
        ring/ring-jetty-adapter {:mvn/version "1.11.0"}
        com.github.seancorfield/next.jdbc {:mvn/version "1.3.909"}}
 
 :aliases
 {:run {:main-opts ["-m" "myapp.core"]}
  :test {:extra-paths ["test"]
         :extra-deps {io.github.cognitect-labs/test-runner {:git/tag "v0.5.1"}}
         :main-opts ["-m" "cognitect.test-runner"]}
  :build {:deps {io.github.clojure/tools.build {:mvn/version "0.9.6"}}
          :ns-default build}}}
```

```bash
clj -M:run                # run with alias
clj -M:test               # run tests
clj -T:build jar          # build JAR
clj -M:nrepl              # start REPL
bb -e '(+ 1 2 3)'        # Babashka inline
```

---

## 공통 Lisp 도구
| 도구 | 목적 |
|------|---------|
| **퀵리스프** | 패키지 관리자 |
| **ASDF** | 시스템 구축 |
| **로스웰** | Lisp 환경 관리자 |
| **QLot** | 로컬 종속성 관리 |
| **슬라임** | 이맥스 리스프 IDE |
| **교활한** | Emacs Lisp IDE(SLIME 포크) |
```lisp
;; Quicklisp
(ql:quickload "hunchentoot")  ; install/load library
(ql:quickload "cl-json")
(ql:update-all-dists)          ; update all

;; ASDF system definition
(asdf:defsystem myapp
  :description "My application"
  :depends-on ("hunchentoot" "cl-json")
  :components ((:file "package")
               (:file "main" :depends-on ("package"))))
```

---

## 웹 프레임워크
| 프레임워크 | 언어 | 유형 |
|------------|----------|------|
| **반지 + 콤포쥬르** | 클로저 | HTTP 핸들러 + 라우팅 |
| **받침대** | 클로저 | 풀스택 웹 |
| **루미너스** | 클로저 | 웹 프레임워크 스택 |
| ** 라이트** | 클로저 | 라우팅 라이브러리 |
| **헌첸투트** | 씨엘 | HTTP 서버 |
| **원시인** | 씨엘 | 웹 프레임워크 |
| **레스타스** | 씨엘 | REST 프레임워크 |
```clojure
;; Ring + Compojure example
(ns myapp.handler
  (:require [compojure.core :refer [defroutes GET POST]]
            [compojure.route :as route]
            [ring.middleware.json :refer [wrap-json-body wrap-json-response]]
            [ring.adapter.jetty :refer [run-jetty]]))

(defroutes app-routes
  (GET "/" [] "Hello, World!")
  (GET "/users/:id" [id] {:status 200 :body {:id id :name "User"}})
  (route/not-found "Not Found"))

(def app (-> app-routes wrap-json-response (wrap-json-body {:keywords? true})))

(defn -main [] (run-jetty app {:port 8080}))
```

---

## 데이터베이스
| 기술 | 언어 | 유형 |
|------------|----------|------|
| **다음.jdbc** | 클로저 | JDBC 래퍼 |
| **HugSQL** | 클로저 | SQL 우선 |
| **꿀SQL** | 클로저 | SQL DSL |
| **clojure.jdbc** | 클로저 | JDBC 인터페이스 |
| **포스트모던** | 씨엘 | 포스트그레SQL |
| **CLSQL** | 씨엘 | SQL 인터페이스 |
| **SxQL** | 씨엘 | SQL DSL |
```clojure
;; next.jdbc example
(require '[next.jdbc :as jdbc]
         '[next.jdbc.result-set :as rs])

(def db {:dbtype "postgresql" :dbname "mydb" :user "admin" :password "secret"})

(defn find-users [min-age]
  (jdbc/execute! db
    ["SELECT id, name, email FROM users WHERE age > ?" min-age]
    {:builder-fn rs/as-unqualified-lower-maps}))
```

---

## 테스트
| 프레임워크 | 언어 | 목적 |
|------------|----------|---------|
| **clojure.test** | 클로저 | 내장된 테스트 |
| **미제** | 클로저 | BDD 스타일 테스트 |
| **기대** | 클로저 | 기대 기반 |
| **테스트.체크** | 클로저 | 속성 기반(QuickCheck) |
| **오전 ​​5시** | 씨엘 | 단위 테스트 |
| **증명** | 씨엘 | 테스트 프레임워크 |
| **리스프 단위** | 씨엘 | 단위 테스트 |
```clojure
;; clojure.test
(ns myapp.user-service-test
  (:require [clojure.test :refer [deftest testing is are]]
            [myapp.user-service :as sut]))

(deftest find-user-test
  (testing "returns user when found"
    (let [repo (atom {1 {:id 1 :name "Alice"}})
          user (sut/find-user repo 1)]
      (is (= "Alice" (:name user)))))
  
  (testing "returns nil when not found"
    (let [repo (atom {})
          user (sut/find-user repo 999)]
      (is (nil? user)))))

;; test.check (property-based)
(require '[clojure.test.check :as tc]
         '[clojure.test.check.generators :as gen]
         '[clojure.test.check.properties :as prop])

(tc/quick-check 100
  (prop/for-all [v (gen/vector gen/int)]
    (= (sort v) (sort (sort v)))))
```

---

## 코드 품질
| 도구 | 언어 | 목적 |
|------|----------|---------|
| **clj-콘도** | 클로저 | 린터 |
| **cljfmt** | 클로저 | 포맷터 |
| **이스트우드** | 클로저 | 린팅 |
| **키빗** | 클로저 | 코드 제안 |
| **알렉스 앤 테리** | 클로저 | 스타일 가이드 |
| **알렉스 플러스** | 씨엘 | 코드 분석 |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## 주요 라이브러리
| 도서관 | 언어 | 목적 |
|---------|----------|---------|
| **core.async** | 클로저 | CSP 동시성 |
| **변환기** | 클로저 | 구성 가능한 알고리즘 |
| **유령** | 클로저 | 데이터 탐색 |
| **스키마** | 클로저 | 데이터 검증 |
| **말리** | 클로저 | 데이터 검증 |
| **데이터.json** | 클로저 | JSON |
| **체셔** | 클로저 | JSON(빠름) |
| **딸꾹질** | 클로저 | HTML 생성 |
| **리프레임** | 클로저스크립트 | SPA 프레임워크 |
| **시약** | 클로저스크립트 | 반응 래퍼 |
| **옴** | 클로저스크립트 | 반응 인터페이스 |
| **코어.매치** | 클로저 | 패턴 매칭 |
| **tools.logging** | 클로저 | 로깅 |
| **마운트** | 클로저 | 상태 관리 |
| **통합** | 클로저 | 구성요소 시스템 |
| **유소켓** | 씨엘 | 소켓 라이브러리 |
| **보르도 스레드** | 씨엘 | 스레딩 |
| **알렉산드리아** | 씨엘 | 유틸리티 라이브러리 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **VS 코드 + 칼바** | 최고의 클로저 IDE |
| **사이더(Emacs)** | 클래식 클로저 IDE |
| **IntelliJ + 필기체** | JetBrains 클로저 |
| **슬라임 / 슬라이** | 커먼 리스프(Emacs) |
| **렘** | 커먼 리스프 IDE |
| **Vim + 벽난로** | 빔 클로저 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **우버자르** |  `clj -T:build jar`(클로저) |
| **GraalVM 네이티브** | 네이티브 이미지(제한적) |
| **도커** | 컨테이너화 |
| **바바시카** | 빠른 스크립팅 |
| **Lisp 바이너리** | 컴파일된 바이너리(SBCL) |
| **쿠버네티스** | 오케스트레이션 |
---

## 요약
Lisp 생태계는 **Clojure**(JVM, 모던), **Common Lisp**(클래식, ANSI), **Racket**(언어 지향) 및 **Emacs Lisp**(편집기 스크립팅) 등 여러 방언에 걸쳐 있습니다. Clojure의 표준 스택은 빌드용 **deps.edn**이 포함된 **Clojure CLI**, 웹용 **Ring + Compojure** 또는 **Pedestal**, 데이터베이스용 **next.jdbc**, 테스트용 **clojure.test**, Linting용 **clj-kondo**, IDE용 **VS Code + Calva** 또는 **CIDER**입니다. Common Lisp는 패키지용으로 **Quicklisp**, 컴파일용으로 **SBCL**, 개발용으로 **SLIME**을 사용합니다. Lisp의 강점은 매크로, 동형성, REPL 기반 개발 및 대화형 프로그래밍입니다. 생태계는 신속한 프로토타이핑, 도메인별 언어 및 데이터 처리에 탁월합니다.