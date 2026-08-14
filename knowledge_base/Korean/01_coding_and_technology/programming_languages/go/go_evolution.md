---
# Metadata
title: "Go — Version History & Evolution"
description: "Comprehensive version history and evolution of Go from 1.0 to modern Go."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [go, golang, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Go - 버전 기록 및 진화
## 타임라인
| 버전 | 출시일 | 주요 테마 |
|---------|-------------|------------|
| 1.0 | 2012년 3월 | 첫 번째 안정 릴리스 |
| 1.1 | 2013년 5월 | 성능, 경주 감지기 |
| 1.3 | 2014년 6월 | 네트워크 폴링, 암호화/TLS |
| 1.4 | 2014년 12월 | Go를 사용한 부트스트랩(자체 호스팅) |
| 1.5 | 2015년 8월 | **동시 GC**, 쓰기 장벽 |
| 1.7 | 2016년 8월 | `context`패키지,`testing`하위 테스트 |
| 1.8 | 2017년 2월 |  `http.Server.Shutdown`, 플러그인 |
| 1.9 | 2017년 8월 | 유형 별칭, 병렬`make`|
| 1.10 | 2018년 2월 | `database/sql`연결 풀 |
| 1.11 | 2018년 8월 | **Go 모듈**,`go mod`|
| 1.12 | 2019년 2월 | TLS 1.3, 모듈 버전 관리 |
| 1.13 | 2019년 9월 | `errors.Is/As`, 숫자 리터럴`0b`,`0o`|
| 1.14 | 2020년 2월 | **Windows의 중복된 I/O**, 고루틴 선점 |
| 1.15 | 2020년 8월 | `time.Ticker`/`Timer`재설정, 모듈 프록시 |
| 1.16 | 2021년 2월 | `embed`패키지, `io/fs`, 기본적으로 모듈 인식 |
| 1.17 | 2021년 8월 | 슬라이스에서 배열로의 변환,`unsafe.Slice`|
| 1.18 | 2022년 3월 | **일반**, 퍼징, 작업공간 |
| 1.19 | 2022년 8월 | 문서 코멘트, 메모리 모델 개정 |
| 1.20 | 2023년 2월 |  `errors.Join`, 프로필 기반 최적화 |
| 1.21 | 2023년 8월 | **`slog`**,`min/max`내장,`maps/slices`|
| 1.22 | 2024년 2월 | 정수 범위, 향상된 라우팅 |
| 1.23 | 2024년 8월 | 반복자(`iter`) 패키지, 타이머 변경 |
| 1.24 | 2025년 2월 | `weak`패키지, 향상된 지도 |
## 주요 이정표
### 시작(2009~2012)
- **2009**: Google에서 발표한 Go(Robert Griesemer, Rob Pike, Ken Thompson)
- **2012**: **Go 1.0** — "Go 1 호환성 약속"
### 성능 및 툴링(2012~2018)
- **1.1**: 30% 이상의 성능 개선; 인종 탐지기
- **1.5**: 동시 가비지 수집기(GC는 밀리초에서 마이크로초까지 드롭을 일시 중지함)
- **1.5**: Go 컴파일러 부트스트랩 — Go로 작성됨(더 이상 C 없음)
- **1.7**:`context`패키지가 표준이 됩니다.
### 모듈 및 생태계(2018~2021)
- **1.11**: **Go 모듈** — 공식적인 종속성 관리
- **1.13**:`errors.Is/As`— 오류 래핑이 관용적이 됩니다.
- **1.16**:`embed`패키지 — 컴파일 타임에 파일 포함
### 모던 고(2022~현재)
- **1.18**: **일반** — 제약 조건이 있는 유형 매개변수
- **1.21**:`slog`— stdlib의 구조화된 로깅; `min/max`내장
- **1.22**: 정수 범위(`for i := range 10`)
- **1.23**: Iterator 패키지 — stdlib의 지연 평가
## 제네릭 여정
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## 오류 처리 철학
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## 동시성 진화
```
1.0:  Goroutines + channels — CSP-inspired
1.1:  Race detector
1.4:  Non-blocking syscalls (net poller)
1.5:  Concurrent GC
1.7:  context package for cancellation
1.14: Cooperative goroutine preemption (signals)
1.21: Synchronization improvements
1.23: iter package — iterator pattern
```

## Go 호환성 약속
```
Go 1.0 (2012): "Go 1 will be available for a long time.
  Compatibility is important. Programs that work at Go 1
  will continue to work at every subsequent Go 1 release."

This means:
- No breaking changes to the language spec
- No breaking changes to the standard library
- Only additive changes
- Forward compatibility guaranteed
```

## 생태계 성장
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## 성능의 진화
```
Go 1.0:  Baseline
Go 1.1:  ~30% faster (register-based calling prep)
Go 1.5:  Concurrent GC (pause time: ms → μs)
Go 1.7:  SSA backend (15-30% faster)
Go 1.11: PGO experiments
Go 1.13: Faster map operations
Go 1.18: Generics (initial overhead, optimized in 1.19+)
Go 1.20: Profile-guided optimization
Go 1.22: Faster crypto, improved compiler
```
