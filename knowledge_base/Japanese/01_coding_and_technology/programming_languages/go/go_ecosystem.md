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
# Go — エコシステムとツールのガイド
このガイドでは、Go エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## ツールチェーン (組み込み)
|ツール |目的 |
|-----|----------|
| **ビルドに行く** |パッケージと依存関係をコンパイルする |
| **テストに行く** |テストを実行する |
| **獣医に行く** |静的解析 |
| **すぐに行きましょう** |コードのフォーマット |
| **モッドに行く** |モジュール管理 |
| **ドキュメントに行きます** |ドキュメントビューア |
| **生成に行く** |コード生成 |
| **インストールに行く** |コンパイルしてインストールする |
| **走りに行きます** |コンパイルして実行します |
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

## サードパーティ製ツール
|ツール |目的 |
|-----|----------|
| **ゴランシリント** |マルチリンターアグリゲータ |
| **ゴファンプ** |より厳密なフォーマッタ |
| **静的チェック** |高度な静的解析 |
| **航空** |開発用のライブリロード |
| **ゴモック / モックゲン** |モックフレームワーク |
| **盗品** | Swagger ドキュメント ジェネレーター |
| **ブフ** |プロトコルバッファツール |
---

## Web フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **ネット/http** |標準ライブラリ |シンプルな API、依存関係なし |
| **ジン** |パフォーマンス |高速 HTTP、ミドルウェア |
| **エコー** |最小限 |クリーンな API 設計 |
| **繊維** |特急っぽい | Node.js 開発者に精通した |
| **チ** |ルーター |軽量、stdlib 互換 |
| **ヒューマ** |オープンAPI | API ファーストの設計 |
---

## gRPC と API
|ツール |目的 |
|-----|----------|
| **google.golang.org/grpc** | gRPC フレームワーク |
| **コネクトゴー** | gRPC-Web、gRPC、REST |
| **protoc-gen-go** | Protobuf コード生成 |
| **grpc ゲートウェイ** | REST から gRPC プロキシへ |
---

## データベース
|パッケージ |データベース |
|----------|----------|
| **データベース/SQL** |標準 SQL インターフェイス |
| **pgx** | PostgreSQL ドライバー (高速) |
| **ゴーム** |完全な ORM |
| **sqlc** | SQL からタイプセーフな Go を生成する |
| **エント** |エンティティ フレームワーク (Facebook) |
| **go-redis** | Redis クライアント |
| **モンゴ ドライバー** | MongoDB クライアント |
---

## テスト
|ツール |目的 |
|-----|----------|
| **テスト中** |組み込みのテスト フレームワーク |
| **証言します** |アサーションとモック |
| **go-cmp** |詳しい比較 |
| **httptest** | HTTP テスト ユーティリティ |
| **ゴーファズ / ファズ** |ファズテスト |
| **ベンチ統計** |ベンチマーク比較 |
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

## CLI ツール
|パッケージ |目的 |
|----------|----------|
| **コブラ** | CLI フレームワーク (kubectl はこれを使用します) |
| **urfave/cli** |シンプルな CLI ビルダー |
| **タピオカティー** |端末UI（魅力） |
| **リップグロス** |ターミナルのスタイリング |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **VS コード + gopls** |公式 Go LSP |
| **ゴーランド** |完全な JetBrains Go IDE |
| **Neovim + gopls** |ターミナルベース |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **静的バイナリ** | `CGO_ENABLED=0 go build`|
| **クロスコンパイル** | `GOOS=linux GOARCH=amd64 go build`|
| **ドッカー** |マルチステージビルド、ディストロレス |
| **コンテナ** |小さな画像 (~10MB) |
---

＃＃ まとめ
Go のエコシステムは実用的で最小限です。標準ライブラリは HTTP、JSON、テストなどをカバーしており、多くの場合フレームワークが不要になります。最新のスタックは次のとおりです。依存関係には **go modules**、リンティングには **golangci-lint**、Web には **Gin** または **Chi**、データベースには **pgx** または **sqlc**、CLI には **cobra**、デプロイメントには **静的バイナリ** です。 Go の強みはそのシンプルさです。高速なコンパイル、小さなバイナリ、および単一のバイナリ展開モデルです。