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

# Haskell — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái Haskell.
---

## Chuỗi công cụ
| Công cụ | Mục đích |
|------|----------|
| **GHC** | Trình biên dịch Glasgow Haskell (trình biên dịch) |
| **GHCup** | Trình cài đặt chuỗi công cụ Haskell |
| **Cabal** | Xây dựng định dạng hệ thống và gói |
| **Chồng** | Công cụ xây dựng có thể tái tạo |
| **cabal-cài đặt** | Quản lý gói |
| **haskell-ngôn ngữ-máy chủ (HLS)** | Máy chủ LSP |
| **ghcid** | Phản hồi tổng hợp nhanh |
| **bốn molu** | Trình định dạng mã |
| **ormolu** | Trình định dạng mã |
| **hlint** | Nói dối / gợi ý |
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

## Quản lý gói
| Công cụ | Mục đích |
|------|----------|
| **Hackage** | Kho gói trung tâm (hơn 15.000 gói) |
| **Ngăn xếp** | Bộ gói tương thích, được tuyển chọn |
| **Cabal** | Công cụ xây dựng và định dạng gói |
| **Chồng** | Bản dựng có thể tái tạo (ảnh chụp nhanh LTS) |
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

## Khung web
| Khung | Loại | Tốt nhất cho |
|----------|------|----------|
| **Người hầu** | Cấp loại | API an toàn loại |
| **Vâng** | Toàn ngăn xếp | Ứng dụng web an toàn loại |
| **Scotty** | Nhẹ | API đơn giản (giống Sinatra) |
| **Spock** | Nhẹ | Ứng dụng web |
| **IHP** | Bao gồm pin | Giống như đường ray, Haskell |
| **Miso** | Giao diện người dùng | Giao diện giống Elm |
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

## Cơ sở dữ liệu
| Công nghệ | Loại |
|----------||------|
| **kiên trì** | ORM (Hệ sinh thái Yesod) |
| **hasql** | PostgreSQL (hiệu suất cao) |
| **postgresql-đơn giản** | PostgreSQL (đơn giản) |
| **chùm** | SQL an toàn kiểu |
| **esqueleto** | ESQL an toàn loại (liên tục) |
| **hedis** | Khách hàng Redis |
| **mongoDB** | Trình điều khiển MongoDB |
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

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **HĐơn vị** | Kiểm tra đơn vị (kiểu xUnit) |
| **ngon** | Khung kiểm tra (có thể kết hợp) |
| **thợ săn ngon** | Tích hợp HUnit cho ngon |
| **kiểm tra nhanh ngon miệng** | Thử nghiệm dựa trên tài sản |
| **Kiểm tra nhanh** | Thử nghiệm dựa trên tài sản |
| **nhím** | Dựa trên tài sản (hiện đại) |
| **hspec** | Thử nghiệm kiểu BDD |
| **doctest** | Ví dụ thử nghiệm trong Haddock |
| **khám phá ngon** | Kiểm tra tự động khám phá |
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

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| **hlint** | Gợi ý và linting |
| **bốnmolu / ormolu** | Định dạng mã |
| **haskell sành điệu** | Định dạng mã |
| **làm cỏ** | Phát hiện mã chết |
| **stan** | Phân tích tĩnh |
| **haskell-ngôn ngữ-máy chủ** | Chẩn đoán, hoàn thiện |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **cơ sở** | Thư viện chuẩn (Prelude) |
| **văn bản** | Các loại văn bản hiệu quả |
| **chuỗi byte** | Dữ liệu nhị phân |
| **aison** | Thư viện JSON |
| **thùng chứa** | Bản đồ, bộ, trình tự |
| **container không có thứ tự** | Bản đồ băm, bộ băm |
| **vectơ** | Mảng hiệu quả |
| **stm** | Bộ nhớ giao dịch phần mềm |
| **không đồng bộ** | Tính toán không đồng bộ |
| **optparse-áp dụng** | Phân tích đối số CLI |
| **optparse-generic** | CLI có nguồn gốc tự động |
| **cong vênh** | Máy chủ HTTP |
| **http-khách hàng** | Máy khách HTTP |
| **ống dẫn** | Truyền dữ liệu |
| **ống** | Truyền dữ liệu |
| **phát trực tuyến** | Truyền dữ liệu |
| **ống kính** | Thư viện quang học |
| **megaparsec** | Bộ kết hợp phân tích cú pháp |
| **phân tích cú pháp** | Bộ kết hợp phân tích cú pháp |
| ** thư giãn ** | Khúc dạo đầu hay hơn |
| ** thư giãn ** | Khúc dạo đầu thay thế |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **Mã VS + HLS** | Hỗ trợ LSP Haskell tốt nhất |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Nevim + HLS** | Dựa trên thiết bị đầu cuối với LSP |
| **Emacs + chế độ haskell** | Môi trường Haskell cổ điển |
| **Vim + vim-haskell** | Tích hợp Vim |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Nhị phân tĩnh** | GHC tạo các tệp nhị phân tĩnh |
| **Docker** | Bản dựng nhiều giai đoạn (hình ảnh haskell) |
| **Không** | Bản dựng có thể tái tạo |
| **Kubernetes** | Dàn nhạc |
| **AWS Lambda** | Không có máy chủ (thông qua hal) |
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

## Bản tóm tắt
Hệ sinh thái của Haskell độc đáo ở chỗ nhấn mạnh vào tính chính xác và an toàn kiểu. Chuỗi công cụ tiêu chuẩn là: **GHC** làm trình biên dịch, **GHCup** để cài đặt, **Cabal** hoặc **Stack** cho các bản dựng, **haskell-lingu-server** để hỗ trợ IDE, **hlint** để tìm lỗi mã nguồn, **fourmolu** để định dạng và **tasty + QuickCheck** để thử nghiệm. Các thư viện chính bao gồm **aeson** cho JSON, **text** cho chuỗi, **servant** cho API an toàn loại, **lens** cho quang học và **stm** cho đồng thời. Haskell vượt trội về trình biên dịch, hệ thống tài chính, hệ thống đồng thời và bất cứ nơi nào tính chính xác là điều tối quan trọng. Quá trình học tập rất dốc nhưng phần thưởng xứng đáng là phần mềm hoạt động chính xác khi xây dựng.