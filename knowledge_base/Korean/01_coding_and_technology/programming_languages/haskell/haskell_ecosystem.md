---
# Metadata
title: "Haskell — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Haskell ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [haskell, ecosystem, tooling, cabal, stack, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Haskell — 생태계 및 도구 가이드
이 가이드는 Haskell 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## 툴체인
| 도구 | 목적 |
|------|---------|
| **GHC** | Glasgow Haskell 컴파일러(컴파일러) |
| **GHC컵** | 하스켈 툴체인 설치 프로그램 |
| **카발** | 빌드 시스템 및 패키지 형식 |
| **스택** | 재현 가능한 빌드 도구 |
| **cabal-설치** | 패키지 관리자 |
| **하스켈 언어 서버(HLS)** | LSP 서버 |
| **ghcid** | 빠른 컴파일 피드백 |
| **포몰루** | 코드 포맷터 |
| **오르몰루** | 코드 포맷터 |
| **힌트** | 린터/제안 |
```bash
ghcup install ghc latest    # install GHC
ghcup install cabal latest  # install Cabal
ghcup install stack latest  # install Stack

cabal init                  # new project
cabal build                 # build
cabal test                  # run tests
cabal run myapp             # run
cabal repl                  # interactive REPL

stack new myapp             # new project
stack build                 # build
stack test                  # run tests
stack exec myapp            # run
```

---

## 패키지 관리
| 도구 | 목적 |
|------|---------|
| **해킹** | 중앙 패키지 저장소(15,000개 이상의 패키지) |
| **스태킹** | 엄선된 호환 패키지 세트 |
| **카발** | 패키지 형식 및 빌드 도구 |
| **스택** | 재현 가능한 빌드(LTS 스냅샷) |
```cabal
-- myapp.cabal
cabal-version: 3.0
name:          myapp
version:       0.1.0.0
build-type:    Simple

executable myapp
  main-is:          Main.hs
  hs-source-dirs:   app
  default-language:  Haskell2010
  build-depends:     base >=4.18
                   , text
                   , aeson
                   , http-types
                   , warp
  ghc-options:      -Wall -Werror
```

```yaml
# stack.yaml
resolver: lts-22.12
packages:
  - .
extra-deps:
  - some-package-1.0.0
```

---

## 웹 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **하인** | 유형 수준 | 유형이 안전한 API |
| **예소드** | 풀스택 | 유형이 안전한 웹 앱 |
| **스코티** | 경량 | 간단한 API(Sinatra 유사) |
| **스팍** | 경량 | 웹 앱 |
| **IHP** | 배터리 포함 | 레일즈와 유사한 하스켈 |
| **미소** | 프론트엔드 | 느릅나무 같은 프런트엔드 |
```haskell
-- Servant API example
type UserAPI =
       "users" :> Get '[JSON] [User]
  :<|> "users" :> Capture "id" Int :> Get '[JSON] User
  :<|> "users" :> ReqBody '[JSON] User :> Post '[JSON] User

server :: Server UserAPI
server = listUsers :<|> getUser :<|> createUser

api :: Proxy UserAPI
api = Proxy

app :: Application
app = serve api server

main :: IO ()
main = run 8080 app
```

---

## 데이터베이스
| 기술 | 유형 |
|------------|------|
| **지속적** | ORM(예소드 생태계) |
| **hasql** | PostgreSQL(고성능) |
| **postgresql-단순** | PostgreSQL(단순) |
| **빔** | 유형이 안전한 SQL |
| **에스크레토** | 유형 안전 ESQL(영구) |
| **헤디스** | Redis 클라이언트 |
| **몽고DB** | MongoDB 드라이버 |
```haskell
-- postgresql-simple example
import Database.PostgreSQL.Simple

main :: IO ()
main = do
  conn <- connect defaultConnectInfo { connectDatabase = "mydb" }
  users <- query_ conn "SELECT id, name, email FROM users" :: IO [User]
  mapM_ print users
```

---

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **HUnit** | 단위 테스트(xUnit 스타일) |
| **맛있어요** | 테스트 프레임워크(구성 가능) |
| **맛있는 사냥** | 맛있는 HUnit 통합 |
| **맛있는 빠른 확인** | 속성 기반 테스트 |
| **빠른 확인** | 속성 기반 테스트 |
| **고슴도치** | 부동산 기반(현대) |
| **hspec** | BDD 스타일 테스트 |
| **문서 테스트** | Haddock의 테스트 예 |
| **맛있는 발견** | 자동 검색 테스트 |
```haskell
-- hspec example
module UserServiceSpec (spec) where

import Test.Hspec
import UserService

spec :: Spec
spec = describe "UserService" $ do
  describe "find" $ do
    it "returns user when found" $ do
      let repo = mkRepo [(1, "Alice")]
          service = mkService repo
      findUser service 1 `shouldReturn` Just (User 1 "Alice")

    it "returns Nothing when not found" $ do
      let repo = mkRepo []
          service = mkService repo
      findUser service 999 `shouldReturn` Nothing

-- QuickCheck property
prop_reverse :: [Int] -> Bool
prop_reverse xs = reverse (reverse xs) == xs
```

---

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **힌트** | 제안 및 보푸라기 |
| **포몰루 / 오르몰루** | 코드 서식 |
| **세련된 하스켈** | 코드 서식 |
| **제초기** | 데드 코드 감지 |
| **스탠** | 정적 분석 |
| **haskell-언어-서버** | 진단, 완료 |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **기본** | 표준 라이브러리(Prelude) |
| **텍스트** | 효율적인 텍스트 유형 |
| **바이트 문자열** | 바이너리 데이터 |
| **애슨** | JSON 라이브러리 |
| **컨테이너** | 맵, 세트, ​​시퀀스 |
| **순서가 지정되지 않은 컨테이너** | 해시 맵, 해시 세트 |
| **벡터** | 효율적인 어레이 |
| **sm** | 소프트웨어 트랜잭션 메모리 |
| **비동기** | 비동기 계산 |
| **optparse 적용** | CLI 인수 구문 분석 |
| **optparse-일반** | 자동 파생 CLI |
| **워프** | HTTP 서버 |
| **http-클라이언트** | HTTP 클라이언트 |
| **도관** | 스트리밍 데이터 |
| **파이프** | 스트리밍 데이터 |
| **스트리밍** | 스트리밍 데이터 |
| **렌즈** | 광학 도서관 |
| **메가파섹** | 파서 결합자 |
| **파섹** | 파서 결합자 |
| **후회** | 더 나은 전주곡 |
| **후회** | 대안적인 전주곡 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **VS 코드 + HLS** | 최고의 Haskell LSP 지원 |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains 하스켈 |
| **네오빔 + HLS** | LSP를 사용한 터미널 기반 |
| **Emacs + 하스켈 모드** | 클래식 하스켈 환경 |
| **Vim + vim-haskell** | Vim 통합 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **정적 바이너리** | GHC는 정적 바이너리를 생성합니다 |
| **도커** | 다단계 빌드(haskell 이미지) |
| **닉스** | 재현 가능한 빌드 |
| **쿠버네티스** | 오케스트레이션 |
| **AWS 람다** | 서버리스(hal을 통해) |
```dockerfile
# Multi-stage Docker build
FROM haskell:9.6 AS builder
WORKDIR /app
COPY . .
RUN cabal build --only-dependencies
RUN cabal build

FROM debian:bookworm-slim
COPY --from=builder /app/dist-newstyle/build/*/myapp /usr/local/bin/
CMD ["myapp"]
```

---

## 요약
Haskell의 생태계는 정확성과 유형 안전성을 강조한다는 점에서 독특합니다. 표준 툴체인은 컴파일러 **GHC**, 설치용 **GHCup**, 빌드용 **Cabal** 또는 **Stack**, IDE 지원용 **haskell-언어-server**, Linting용 **hlint**, 포맷용 **fourmolu**, 테스트용 **tasty + QuickCheck**입니다. 주요 라이브러리에는 JSON용 **aeson**, 문자열용 **text**, 유형 안전 API용 **servant**, 광학용 **lens**, 동시성용 **stm**이 포함됩니다. Haskell은 컴파일러, 금융 시스템, 동시 시스템 등 정확성이 중요한 모든 분야에서 탁월합니다. 학습 곡선은 가파르지만 구성을 통해 올바르게 작동하는 소프트웨어는 보상을 받습니다.