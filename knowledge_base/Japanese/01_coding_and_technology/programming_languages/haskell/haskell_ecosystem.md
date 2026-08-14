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

# Haskell — エコシステムとツールのガイド
このガイドでは、Haskell エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## ツールチェーン
|ツール |目的 |
|-----|----------|
| **GHC** | Glasgow Haskell Compiler (コンパイラ) |
| **GHカップ** | Haskell ツールチェーン インストーラー |
| **陰謀団** |ビルドシステムとパッケージ形式 |
| **スタック** |再現可能なビルドツール |
| **cabal-install** |パッケージマネージャー |
| **haskell 言語サーバー (HLS)** | LSPサーバー |
| **GHCID** |高速コンパイルのフィードバック |
| **フォーモル** |コードフォーマッタ |
| **オルモル** |コードフォーマッタ |
| **リント** |リンター/提案​​ |
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

## パッケージ管理
|ツール |目的 |
|-----|----------|
| **ハッキング** |中央パッケージ リポジトリ (15,000 以上のパッケージ) |
| **スタック** |厳選された互換性のあるパッケージ セット |
| **陰謀団** |パッケージ形式とビルドツール |
| **スタック** |再現可能なビルド (LTS スナップショット) |
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

## Web フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **サーヴァント** |タイプレベル |タイプセーフな API |
| **イェソド** |フルスタック |タイプセーフな Web アプリ |
| **スコッティ** |軽量 |シンプルな API (Sinatra のような) |
| **スポック** |軽量 |ウェブアプリ |
| **IHP** |電池付属 | Rails のような、Haskell |
| **味噌** |フロントエンド | Elm のようなフロントエンド |
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

## データベース
|テクノロジー |タイプ |
|-----------|------|
| **永続的** | ORM (イェソドエコシステム) |
| **hasql** | PostgreSQL (高パフォーマンス) |
| **postgresql-simple** | PostgreSQL (シンプル) |
| **ビーム** |タイプセーフな SQL |
| **エスケレト** |タイプ セーフ ESQL (永続的) |
| **ヘディス** | Redis クライアント |
| **mongoDB** | MongoDB ドライバー |
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

## テスト
|フレームワーク |目的 |
|----------|----------|
| **Hユニット** |単体テスト (xUnit スタイル) |
| **おいしい** |テスト フレームワーク (コンポーザブル) |
| **おいしいフユニット** | HUnit の統合によるおいしい |
| **おいしいクイックチェック** |プロパティベースのテスト |
| **クイックチェック** |プロパティベースのテスト |
| **ハリネズミ** |プロパティベース (最新) |
| **hスペック** | BDD スタイルのテスト |
| **doctest** | Haddock でのテスト例 |
| **おいしい発見** |自動検出テスト |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **リント** |提案とリント |
| **フォーモル / オルモル** |コードのフォーマット |
| **スタイリッシュなハスケル** |コードのフォーマット |
| **草取り** |デッドコード検出 |
| **スタン** |静的解析 |
| **ハスケル言語サーバー** |診断、完了 |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **ベース** |標準ライブラリ (プレリュード) |
| **テキスト** |効率的なテキスト タイプ |
| **バイト文字列** |バイナリデータ |
| **エソン** | JSONライブラリ |
| **コンテナ** |マップ、セット、シーケンス |
| **注文されていないコンテナ** |ハッシュマップ、ハッシュセット |
| **ベクトル** |効率的な配列 |
| **stm** |ソフトウェア トランザクション メモリ |
| **非同期** |非同期計算 |
| **optparse-applicative** | CLI 引数の解析 |
| **optparse-generic** |自動派生 CLI |
| **ワープ** | HTTPサーバー |
| **http-クライアント** | HTTPクライアント |
| **導管** |ストリーミングデータ |
| **パイプ** |ストリーミングデータ |
| **ストリーミング** |ストリーミングデータ |
| **レンズ** |光学ライブラリ |
| **メガパーセク** |パーサーコンビネータ |
| **パーセク** |パーサーコンビネータ |
| **ルード** |より良いプレリュード |
| **ルード** |オルタナティブ・プレリュード |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **VS コード + HLS** |最高の Haskell LSP サポート |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains ハスケル |
| **ネオビム + HLS** | LSP を使用したターミナルベース |
| **Emacs + haskell モード** |クラシック Haskell 環境 |
| **Vim + vim-haskell** | Vim の統合 |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **静的バイナリ** | GHC は静的バイナリを生成します |
| **ドッカー** |マルチステージビルド (Haskell イメージ) |
| **ニックス** |再現可能なビルド |
| **Kubernetes** |オーケストレーション |
| **AWS Lambda** |サーバーレス (hal 経由) |
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

＃＃ まとめ
Haskell のエコシステムは、正確性と型安全性を重視する点で独特です。標準ツールチェーンは次のとおりです。コンパイラとして **GHC**、インストール用に **GHCup**、ビルド用に **Cabal** または **Stack**、IDE サポート用に **haskell-langage-server**、リンティング用に **hlint**、フォーマット用に **fourmolu**、テスト用に **tasty + QuickCheck** です。主要なライブラリには、JSON 用の **aeson**、文字列用の **text**、タイプ セーフ API 用の **servant**、光学用の **lens**、同時実行用の **stm** が含まれます。 Haskell は、コンパイラ、金融システム、並行システムなど、正確性が最優先されるあらゆる分野で優れています。学習曲線は急勾配ですが、その見返りとしては、構築によって正しく動作するソフトウェアが得られます。