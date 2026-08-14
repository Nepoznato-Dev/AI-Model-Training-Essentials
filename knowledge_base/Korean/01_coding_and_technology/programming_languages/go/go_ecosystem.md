<!--
---
# Metadata
title: "Go — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Go ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [go, golang, ecosystem, tooling, testing, web, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Go — 생태계 및 툴링 가이드
이 가이드는 Go 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## 툴체인(내장)
| 도구 | 목적 |
|------|---------|
| **빌드 시작** | 패키지 및 종속성 컴파일 |
| **테스트하러 가기** | 테스트 실행 |
| **수의사에게 가보세요** | 정적 분석 |
| **fmt로 이동** | 코드 서식 |
| **모드로 이동** | 모듈 관리 |
| **문서로 이동** | 문서 뷰어 |
| **생성하기** | 코드 생성 |
| **설치하러 가기** | 컴파일 및 설치 |
| **달려가세요** | 컴파일 및 실행 |
```bash
go mod init example.com/project  # initialize module
go get github.com/pkg/errors     # add dependency
go mod tidy                      # clean up dependencies
go build -o app ./cmd/app       # build binary
go test ./...                    # run all tests
go test -race ./...              # with race detector
go test -cover ./...             # with coverage
go vet ./...                     # static analysis
```

---

## 타사 도구
| 도구 | 목적 |
|------|---------|
| **golangci-lint** | 다중 언어 수집기 |
| **고품격** | 더욱 엄격한 포맷터 |
| **정적검사** | 고급 정적 분석 |
| **공기** | 개발을 위한 실시간 새로고침 |
| **고목 / 목겐** | 모의 프레임워크 |
| **장식** | Swagger 문서 생성기 |
| **부럽** | 프로토콜 버퍼 도구 |
---

## 웹 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **넷/http** | 표준 라이브러리 | 단순한 API, 종속성 없음 |
| **진** | 성과 | 빠른 HTTP, 미들웨어 |
| **에코** | 최소 | 깔끔한 API 디자인 |
| **섬유** | 익스프레스형 | Node.js 개발자에 익숙함 |
| **치** | 라우터 | 경량, stdlib 호환 |
| **휴마** | 오픈API | API 우선 디자인 |
---

## gRPC 및 API
| 도구 | 목적 |
|------|---------|
| **google.golang.org/grpc** | gRPC 프레임워크 |
| **연결-이동** | gRPC-웹, gRPC, REST |
| **프로톡-겐-고** | Protobuf 코드 생성 |
| **grpc-게이트웨이** | REST에서 gRPC 프록시로 |
---

## 데이터베이스
| 패키지 | 데이터베이스 |
|---------|----------|
| **데이터베이스/SQL** | 표준 SQL 인터페이스 |
| **pgx** | PostgreSQL 드라이버(빠름) |
| **고름** | 전체 ORM |
| **sqlc** | SQL에서 유형이 안전한 Go 생성 |
| **참여** | 엔터티 프레임워크(Facebook) |
| **go-redis** | Redis 클라이언트 |
| **몽고 드라이버** | 몽고DB 클라이언트 |
---

## 테스트
| 도구 | 목적 |
|------|---------|
| **테스트** | 내장된 테스트 프레임워크 |
| **증언** | 주장과 조롱 |
| **go-cmp** | 심층 비교 |
| **http테스트** | HTTP 테스트 유틸리티 |
| **퍼즈/퍼즈** | 퍼지 테스트 |
| **벤치스텟** | 벤치마크 비교 |
```go
func TestAdd(t *testing.T) {
    got := Add(2, 3)
    if got != 5 {
        t.Errorf("Add(2, 3) = %d, want 5", got)
    }
}

// Table-driven tests
func TestAdd(t *testing.T) {
    tests := []struct{
        name string
        a, b, want int
    }{
        {"positive", 2, 3, 5},
        {"zero", 0, 0, 0},
        {"negative", -1, 1, 0},
    }
    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := Add(tt.a, tt.b)
            if got != tt.want {
                t.Errorf("got %d, want %d", got, tt.want)
            }
        })
    }
}
```

---

## CLI 도구
| 패키지 | 목적 |
|---------|---------|
| **코브라** | CLI 프레임워크(kubectl이 이것을 사용함) |
| **urfave/cli** | 간단한 CLI 빌더 |
| **버블티** | 터미널 UI(참) |
| **립글로스** | 터미널 스타일링 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **VS 코드 + gopls** | 공식 Go LSP |
| **고랜드** | 전체 JetBrains Go IDE |
| **Neovim + gopls** | 터미널 기반 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **정적 바이너리** | `CGO_ENABLED=0 go build`|
| **크로스 컴파일** | `GOOS=linux GOARCH=amd64 go build`|
| **도커** | 다단계 빌드, distroless |
| **컨테이너** | 작은 이미지(~10MB) |
---

## 요약
Go의 생태계는 실용적이고 최소화되어 있습니다. 표준 라이브러리는 HTTP, JSON, 테스트 등을 다루며 종종 프레임워크가 필요하지 않습니다. 최신 스택은 종속성을 위한 **go 모듈**, Linting을 위한 **golangci-lint**, 웹용 **Gin** 또는 **Chi**, 데이터베이스용 **pgx** 또는 **sqlc**, CLI용 **cobra**, 배포용 **정적 바이너리**입니다. Go의 강점은 단순성입니다. 즉, 빠른 컴파일, 작은 바이너리, 단일 바이너리 배포 모델입니다.